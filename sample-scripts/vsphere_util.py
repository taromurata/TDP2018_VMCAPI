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

class vSphereUtil():
    def __init__(self):
        self.set_default_vm_spec()
        self.info_file = None
        self.vcenter_ip = None
        self.vcenter_username = None
        self.vcenter_password = None
        self.vsphere_client = None

        self.session = requests.session()
        self.session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def set_default_vm_spec(self, vm_spec):
        self.d_datacenter_name = vm_spec['vm_datacenter_name']
        self.d_vm_folder_name = vm_spec['vm_folder_name']
        self.d_datastore_name = vm_spec['vm_datastore_name']
        # TODO:

        print('Not implemented yet.', file=sys.stderr)

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
        return

    def create_vm(self, vm_info):
        # TODO:
        print('Not implemented yet.', file=sys.stderr)
        return

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

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

