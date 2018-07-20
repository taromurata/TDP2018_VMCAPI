#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tmurata <tmurata@ubuntu>
#
# Distributed under terms of the MIT license.

"""
Draft
"""

import sys
import yaml
import requests
import argparse
import atexit
import urllib3
from tabulate import tabulate
#from vmware.vapi.vmc.client import create_vmc_client
from vmware.vapi.vsphere.client import create_vsphere_client

from com.vmware.vcenter.vm_client import Power

from samples.vsphere.common import sample_cli
from samples.vsphere.common import sample_util
from samples.vsphere.common.ssl_helper import get_unverified_session
from samples.vsphere.common.sample_util import pp
from samples.vsphere.vcenter.helper import vm_placement_helper
from samples.vsphere.vcenter.helper.vm_helper import get_vm
from samples.vsphere.vcenter.setup import testbed

from samples.vsphere.contentlibrary.ovfdeploy.deploy_ovf_url import DeployOvfTemplate

class vSphereUtil():
    def __init__(self):
        # self.set_default_vm_spec()
        self.info_file = None
        self.vcenter_ip = None
        self.vcenter_username = None
        self.vcenter_password = None
        self.vsphere_client = None

        self.placement_spec = None

        self.session = requests.session()
        self.session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def set_default_vm_spec(self, vm_spec):
        self.d_datacenter_name = vm_spec['vm_datacenter_name']
        self.d_vm_folder_name = vm_spec['vm_folder_name']
        self.d_datastore_name = vm_spec['vm_datastore_name']
        self.d_vm_guestos = vm_spec['vm_guestos']
        self.d_vm_name_default = vm_spec['vm_name_default']

    def set_info(self, info_dict):
        self.vcenter_ip = info_dict['vcenter']['ip']
        self.vcenter_username = info_dict['vcenter']['username']
        self.vcenter_password = info_dict['vcenter']['password']

    def read_info(self, info_file):
        """Read VMC information from info file."""
        info = yaml.load(open(info_file, 'r+'))
        self.set_info(info)

    def login(self):
        """Login to vCenter."""
        self.vsphere_client = create_vsphere_client(
                server=self.vcenter_ip,
                username=self.vcenter_username,
                password=self.vcenter_password,
                session=self.session)

    def list_vms(self):
        print(self.vsphere_client.vcenter.VM.list())

    def create_default_vm(self):
        """Create default VM using set parameters by set_default_vm_spec."""

        if not self.placement_spec:
            self.placement_spec = vm_placement_helper.get_placement_spec_for_resource_pool(
                    self.vsphere_client,
                    self.d_datacenter_name,
                    self.d_vm_folder_name,
                    self.d_datastore_name)

        vm_create_spec = self.vsphere_client.vcenter.VM.CreateSpec(
                name=self.d_vm_name_default,
                guest_os=self.d_vm_guestos,
                placement=self.placement_spec)

        print('\n# Example: create_default_vm: Creating a VM using spec\n-----')
        print(pp(vm_create_spec))
        print('-----')

        vm = self.vsphere_client.vcenter.VM.create(vm_create_spec)
        print("create_default_vm: Created VM '{}' ({})".format(
            self.d_vm_name_default, vm))

        vm_info = self.vsphere_client.vcenter.VM.get(vm)
        print('vm.get({}) -> {}'.format(vm, pp(vm_info)))
        return vm

    def create_vm(self, vm_info):
        # TODO:
        print('Not implemented yet.', file=sys.stderr)
        return

    def cleanup_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        if vm:
            state = self.vsphere_client.vcenter.vm.Power.get(vm)
            if state == Power.Info(state=Power.State.POWERED_ON):
                self.vsphere_client.vcenter.vm.Power.stop(vm)
            elif state == Power.Info(state=Power.State.SUSPENDED):
                self.vsphere_client.vcenter.vm.Power.start(vm)
                self.vsphere_client.vcenter.vm.Power.stop(vm)
            print("Deleting VM '{}' ({})".format(self.d_vm_name_default, vm))
            self.vsphere_client.vcenter.VM.delete(vm)


    def cleanup_vm(self, vm_info):
        # TODO:
        print('Not implemented yet.', file=sys.stderr)

        return

    def deploy_ovf_url(ovf_url):
        print('Not implemented yet.', file=sys.stderr)
        return

    def poweron_vm(vm_name):
        print('Not implemented yet.', file=sys.stderr)
        return

    def poweron_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        self.vsphere_client.vcenter.vm.Power.start(vm)

    def poweroff_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        self.vsphere_client.vcenter.vm.Power.stop(vm)

    def suspend_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        self.vsphere_client.vcenter.vm.Power.suspend(vm)

    def resume_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        self.vsphere_client.vcenter.vm.Power.resume(vm)

    def reset_default_vm(self):
        vm = get_vm(self.vsphere_client, self.d_vm_name_default)
        self.vsphere_client.vcenter.vm.Power.reset(vm)

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

