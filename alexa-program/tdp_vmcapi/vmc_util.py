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

from com.vmware.vapi.std.errors_client import InvalidRequest
from com.vmware.vmc.model_client import AwsSddcConfig, ErrorResponse, AccountLinkSddcConfig, SddcConfig
from tabulate import tabulate
from vmware.vapi.vmc.client import create_vmc_client

from samples.vmc.helpers.vmc_task_helper import wait_for_task

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

        self.sddc = None

    def set_info(self, info):
        self.refresh_token = info['vmc']['refresh_token']
        self.org_id = info['vmc']['main_org_id']

        # XXX: for test only. these values should be input interactively
        # self.sddc_id = info['vmc']['sddc_id']
        # self.sddc_name = info['vmc']['sddc_name']
        # self.region = info['vmc']['region']
        # self.interval_sec = info['vmc']['interval_sec']
        self.interval_sec = 2 # default value in sample code

    def read_info(self, info_file):
        """Read VMC information from info file."""
        info = yaml.load(open(info_file, 'r'))
        self.set_info(info)

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
        print(sddcs)
        print("returing...")
        return sddcs

    def create_sddc(self, sddc_create_spec):
        """
        Create SDDC

        Parameters
        ----------
        sddc_create_spec : dict

        """

        sddc_config = AwsSddcConfig(
                region=sddc_create_spec['region'],
                name=sddc_create_spec['name'],
                account_link_sddc_config=[AccountLinkSddcConfig(
                    customer_subnet_ids=[sddc_create_spec['subnet_id']],
                    connected_account_id=sddc_create_spec['account_id'])],
                provider=sddc_create_spec['provider'],
                num_hosts=int(sddc_create_spec['num_hosts']),
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

        self.sddc = sddc

        return sddc

    # TODO: Merge to delete methods into one.
    def delete_sddc_id(self, sddc_id):
        try:
            task = self.vmc_client.orgs.Sddcs.delete(org=self.org_id,
                                                     sddc=sddc_id)
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


    def delete_latest_sddc(self):
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

    def list_sddc_resource_ids(self):
        sddcs = self.vmc_client.orgs.Sddcs.list(self.org_id)
        #
        print(type(sddcs[0].resource_config))
        for x in dir(sddcs[0].resource_config):
            print(x)
        #
        if not sddcs:
            raise ValueError('This func requires at least one SDDC associated'
                             'with the calling user')
        print("\n# List SDDC Resource IDs")
        table = []
        for sddc in sddcs:
            table.append([sddc.resource_id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['Resource ID', 'Name', 'AWS Region']))

    def print_output(self, sddcs):
        table = []
        for sddc in sddcs:
            table.append([sddc.id, sddc.name, sddc.resource_config.region])
        print(tabulate(table, ['ID', 'Name', 'AWS Region']))

    def list_vms_in_sddc(self):
        # TODO: WIP
        print("Not implemented yet.")

        return
