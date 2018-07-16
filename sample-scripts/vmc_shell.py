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
            cmd = input()

            if cmd in {'l', 'ls', 'list_sddc'}:
                # XXX: get_sddc
                continue
            elif cmd in {'exit', 'exit()'}:
                print('Bye!')
                break;
            else:
                self.print_help()
                continue

    def print_help(self):
        print('Help doc is now under construction.\nSorry! :P')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-f', '--file', action='store', type=str)
    args = parser.parse_args()

    if args.file:
        vmcshell = VMCPyShell(args.file)
    else:
        print('usage: ./vmc_shell.py -f [info_file]')

