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
        self.info_file = None
        self.vcenter_ip = None
        self.vcenter_username = None
        self.vcenter_password = None
        self.vsphere_client = None

        self.session = requests.session()
        self.session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def read_info(self, info_file):
        """Read VMC information from info file."""
        info = yaml.load(open(info_file, 'r+'))

        self.vcenter_ip = info['vcenter']['ip']
        self.vcenter_username = info['vcenter']['username']
        self.vcenter_password = info['vcenter']['password']

    def login(self):
        """Login to vCenter."""
        self.vsphere_client = create_vsphere_client(
                server=self.vcenter_ip,
                username=self.vcenter_username,
                password=self.vcenter_password,
                session=self.session)

    def list_vms(self):
        print(self.vsphere_client.vcenter.VM.list())


    def create_vm(vm_info):
        # TODO:

        return

    def cleanup_vm(vm_info):
        # TODO:

        return

    def deploy_ovf_url(ovf_url):

    def poweron_vm(vm_name):
        return

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

