#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tmurata <tmurata@ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

import argparse
import sys

from organization_operations import *
from vmc_util import *

print('test')

def main(info_file):
    vmc_util = VMCUtil()
    vmc_util.read_info(info_file)
    print(vmc_util.refresh_token)
    print(vmc_util.org_id)
#    org_operations = OperationsOnOrganizations()
#    org_operations.options()
#    org_operations.setup()
#    org_operations.list_orgs()
    vmc_util.login()
    vmc_util.list_sddc()

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('-f', '--file', action='store', type=str)
    args = parser.parse_args()

    if not args.file:
        sys.exit("usage: ./get_sddc.py -f [config file]")
    main(args.file)
