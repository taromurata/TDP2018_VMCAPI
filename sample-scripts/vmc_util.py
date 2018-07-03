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
from tabulate import tabulate

from vmware.vapi.vmc.client import create_vmc_client

class VMCUtil():
    def __init__(self):
        self.info_file = None
        self.refresh_token = None
        self.main_org_id = None
        self.vmc_client = None

    def read_info(self, info_file):
        """Read VMC information from info file."""
        info = yaml.load(open(info_file, 'r+'))

        self.refresh_token = info['vmc']['refresh_token']
        self.main_org_id = info['vmc']['main_org_id']

    def login(self):
        """Login to VMware Cloud on AWS."""
        self.vmc_client = create_vmc_client(self.refresh_token)

    def list_sddc(self):
        sddcs = self.vmc_client.orgs.Sddcs.list(self.main_org_id)
        if not sddcs:
            raise ValueError('This func requires at least one SDDC associated'
                             'with the calling user')
        print("\n# List SDDCs")
        self.print_output(sddcs)

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

