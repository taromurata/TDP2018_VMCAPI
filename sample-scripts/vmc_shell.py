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

from vmc_util import *


class VMCPyShell:
    def __init__(self, info_file):
        print('Welcome to VMC Python Shell!')
        self.vmcutil = VMCUtil()
        self.vmcutil.read_info(info_file)
        self.vmcutil.login()
        print('Logged in to VMC using given info.')
        self.main_loop()

    def main_loop(self):
        while True:
            print("VMCPyShell > ", end="")
            cmd = input().strip()

            # Main loop.
            if cmd in {'l', 'ls', 'list_sddc'}:
                self.vmcutil.list_sddc()
                continue
            elif cmd in {'get_org_id', 'id'}:
                print('org_id: {}'.format(self.vmcutil.org_id))
                continue
            elif cmd in {'delete_sddc'}:
                self.delete_sddc_id()
                continue
            elif cmd in {'create_sddc'}:
                self.create_sddc_by_file()
                continue
            elif cmd in {'create_sddc_i', 'create_sddc_interactive'}:
                self.create_sddc_interactive()
            elif cmd in {'exit', 'exit()'}:
                print('Bye!')
                break;
            else:
                self.print_help()
                continue

    def delete_sddc_id(self):
        print('sddc_id to delete [sddc resource id]: ', end="")
        sddc_id = input().strip()
        self.vmcutil.delete_sddc_id(sddc_id)

    def create_sddc_by_file(self):
        print('sddc spec file?: ', end="")
        sddc_spec_file = input().strip()
        if os.path.isfile(sddc_spec_file):
            sddc_spec = json.load(open(args.config_file, "r"))
            self.vmcutil.create_sddc(sddc_spec)
        else:
            print("No such file: {}".format(sddc_spec_file))

    def create_sddc_interactive(self):
        # TODO: Implement a confirmation process.
        print('sddc_name    : ', end=""); sddc_name     = input().strip()
        print('sddc_provider: ', end=""); sddc_provider = input().strip()
        print('sddc_region  : ', end=""); sddc_region   = input().strip()
        print('num_hosts    : ', end=""); num_hosts     = input().strip()
        print('account_id   : ', end=""); account_id    = input().strip()
        print('subnet_id    : ', end=""); subnet_id     = input().strip()

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
    args = parser.parse_args()

    error_message = 'usage: ./vmc_shell.py -f [info_file]'

    if args.file:
        vmcshell = VMCPyShell(args.file)
    else:
        print('Input the info_file: ', end="")
        info_file = input()
        if os.path.isfile(info_file):
            vmcshell = VMCPyShell(info_file)
        else:
            print(error_message, file=sys.stderr)

