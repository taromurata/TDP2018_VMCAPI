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
        self.org_id = None
        self.vmc_client = None

        self.region = None
        self.sddc_id = None
        self.sddc_name = None
        self.interval_sec = None

    def read_info(self, info_file):
        """Read VMC information from info file."""
        info = yaml.load(open(info_file, 'r+'))

        self.refresh_token = info['vmc']['refresh_token']
        self.org_id = info['vmc']['main_org_id']

        # XXX: for test only. these values should be input interactively
        self.sddc_id = info['vmc']['sddc_id']
        self.sddc_name = info['vmc']['sddc_name']
        self.region = info['vmc']['region']
        self.interval_sec = info['vmc']['interval_sec']

    def login(self):
        """Login to VMware Cloud on AWS."""
        self.vmc_client = create_vmc_client(self.refresh_token)

    def list_sddc(self):
        sddcs = self.vmc_client.orgs.Sddcs.list(self.org_id)
        if not sddcs:
            raise ValueError('This func requires at least one SDDC associated'
                             'with the calling user')
        print("\n# List SDDCs")
        self.print_output(sddcs)

    def create_sddc(sddc_create_spec):
        # XXX:
        # account_id = self.vmc_client.orgs.account_link.ConnectedAccounts.get(
        #     self.org_id)[0].id
        account_id =

        vpc_map = self.vmc_client.orgs.account_link.CompatibleSubnets.get(
            org=self.org_id,
            linked_account_id=account_id).vpc_map

        customer_subnet_id = self.get_subnet_id(vpc_map)
        if not customer_subnet_id:
            raise ValueError('No available subnet for region {}'.format(self.region))

        sddc_config = AwsSddcConfig(
            region=self.region,
            name=self.sddc_name,
            account_link_sddc_config=[AccountLinkSddcConfig(
                customer_subnet_ids=[customer_subnet_id],
                connected_account_id=account_id)],
            provider=os.environ.get('VMC_PROVIDER', SddcConfig.PROVIDER_AWS),
            num_hosts=1,
            deployment_type=SddcConfig.DEPLOYMENT_TYPE_SINGLEAZ)

        try:
            task = self.vmc_client.orgs.Sddcs.create(org=self.org_id,
                                                     sddc_config=sddc_config)
        except InvalidRequest as e:
            # Convert InvalidRequest to ErrorResponse to get error message
            error_response = e.data.convert_to(ErrorResponse)
            raise Exception(error_response.error_messages)

        wait_for_task(task_client=self.vmc_client.orgs.Tasks,
                      org_id=self.org_id,
                      task_id=task.id,
                      interval_sec=self.interval_sec)

        print('\n# Example: SDDC created:')
        self.sddc_id = task.resource_id
        sddc = self.vmc_client.orgs.Sddcs.get(self.org_id, self.sddc_id)
        self.print_output([sddc])

    def delete_sddc(self):
        try:
            task = self.vmc_client.orgs.Sddcs.delete(org=self.org_id,
                                                     sddc=self.sddc_id)
        except InvalidRequest as e:
            # Convert InvalidRequest to ErrorResponse to get error message
            error_response = e.data.convert_to(ErrorResponse)
            raise Exception(error_response.error_messages)

        wait_for_task(task_client=self.vmc_client.orgs.Tasks,
                      org_id=self.org_id,
                      task_id=task.id,
                      interval_sec=self.interval_sec)

        print('\n# Example: Remaining SDDCs:'.format(self.org_id))
        sddcs = self.vmc_client.orgs.Sddcs.list(self.org_id)
        self.print_output(sddcs)

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

    def list_vms_in_sddc(self):
        # TODO: WIP
        print("Not implemented yet.")

        return
