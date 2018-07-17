#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tmurata <tmurata@ubuntu>
#
# Distributed under terms of the MIT license.

"""
VMC on AWS python shell.
"""

import os
import argparse
import json

from getpass import getpass

from vmc_util import *
from vsphere_util import *


class VMCPyShell:
    def __init__(self, info_file):
        print('Welcome to VMC Python Shell!')
        self.vmcutil = VMCUtil()
        self.vmcutil.read_info(info_file)
        self.vmcutil.login()
        print('Logged in to VMC using given info.')

        self.vsphereutil = None

        # Start main loop
        self.main_loop()

    def main_loop(self):
        prompt = 'VMCPyShell> '
        with_vcenter = False
        # Main loop.
        while True:
            cmd = input(prompt).strip()

            if cmd in {'l', 'ls', 'list_sddc'}:
                self.vmcutil.list_sddc()
                continue
            elif cmd in {'r', 'res_id', 'resource_ids'}:
                self.vmcutil.list_sddc_resource_ids()
                continue
            elif cmd in {'get_org_id', 'id'}:
                print('org_id: {}'.format(self.vmcutil.org_id))
                continue
            elif cmd in {'delete_id', 'delete_sddc', 'delete_sddc_id'}:
                self.delete_sddc_id()
                continue
            elif cmd in {'delete', 'delete_latest_sddc'}:
                self.vmcutil.delete_latest_sddc()
                continue
            elif cmd in {'create_sddc'}:
                self.create_sddc_by_file()
                continue
            elif cmd in {'create_sddc_i', 'create_sddc_interactive'}:
                self.create_sddc_interactive()
            elif cmd in {'vcenter', 'login', 'login_vcenter'}:
                # TODO:
                print("Not implemented yet.", file=sys.stderr)
                # self.login_vcenter()
                continue
            elif cmd in {'vcenter_i', 'login_i', 'logini', 'login_vcenter_i'}:
                # TODO:
                print("Not implemented yet.", file=sys.stderr)
                self.login_vcenter_interactive()
                prompt = 'VMCPyShell (w/ VC)> '
                continue
            elif cmd in {'logoff', 'logout', 'logout_vcenter'}:
                # TODO:
                print("Not implemented yet.", file=sys.stderr)
                continue
            elif cmd in {'exit', 'exit()'}:
                print('Bye!')
                #
                # EXIT LOOP
                #
                break;
            elif with_vcenter and cmd in {'list_vms', 'list', 'ls_vm', 'lsvm'}:
                self.vsphereutil.list_vms()
            else:
                self.print_help()
                continue

    def login_vcenter_interactive(self):
        self.vsphereutil = vSphereUtil()

        vcenter_ip = input('vCenter IP: ').strip()
        vcenter_username = input('Username: ').strip()
        vcenter_password = getpass('Password: ').strip()

        self.vsphereutil.set_info({
            'vcenter': {'ip': vcenter_ip,
                        'username': vcenter_username,
                        'password': vcenter_password}})

        self.vsphereutil.login()

        print("Successfully logged in to {}".format(vcenter_ip))

    def delete_sddc_id(self):
        sddc_id = input('sddc_id to delete [sddc resource id]: ').strip()
        self.vmcutil.delete_sddc_id(sddc_id)

    def create_sddc_by_file(self):
        print('sddc spec file?: ', end="")
        sddc_spec_file = input().strip()
        if os.path.isfile(sddc_spec_file):
            sddc_spec = json.load(open(sddc_spec_file, "r"))
            self.vmcutil.create_sddc(sddc_spec)
        else:
            print("No such file: {}".format(sddc_spec_file))

    def create_sddc_interactive(self):
        # TODO: Implement a confirmation process.
        sddc_name     = input('sddc_name    : ').strip()
        sddc_provider = input('sddc_provider: ').strip()
        sddc_region   = input('sddc_region  : ').strip()
        num_hosts     = input('num_hosts    : ').strip()
        account_id    = input('account_id   : ').strip()
        subnet_id     = input('subnet_id    : ').strip()

        sddc_spec = {
                'name': sddc_name,
                'provider': sddc_provider,
                'region': sddc_region,
                'num_hosts': num_hosts,
                'account_id': account_id,
                'subnet_id': subnet_id
                }

        self.vmcutil.create_sddc(sddc_spec)

    def print_help(self):
        print("""
Commands:
    * l, ls, list_sddc:
      - list sddcs associated with your org_id
    * id, get_org_id:
      - print your organization id
    * delete_sddc [sddc_id]:
      - delete sddc
    * create_sddc [sddc_spec_file]
      - create sddc by using configurations in given file.
    * create_sddc_i, create_sddc_interactive
      - create sddc interactively
    * exit
      - exit this script.
        """)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-f', '--file', action='store', type=str)
    parser.add_argument('-d', '--dry_run', action='store_true')
    args = parser.parse_args()

    error_message = 'usage: ./vmc_shell.py -f [info_file]'

    if args.dry_run:
        print("Sorry but dry_run option is not implemeted yet.", file=sys.stderr) 

    if args.file:
        vmcshell = VMCPyShell(args.file)
    else:
        print('Input the info_file: ', end="")
        info_file = input()
        if os.path.isfile(info_file):
            vmcshell = VMCPyShell(info_file)
        else:
            print(error_message, file=sys.stderr)

