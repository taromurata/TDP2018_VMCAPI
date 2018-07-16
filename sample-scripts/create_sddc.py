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

from organization_operations import *
from vmc_util import *

def main(info_file, sddc_spec):
    vmc_util = VMCUtil()
    vmc_util.read_info(info_file)
    vmc_util.login()
    vmc_util.create_sddc(sddc_spec)

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('-f', '--file', action='store', type=str)
    parser.add_argument('-c', '--config_file', action='store', type=str)
    args = parser.parse_args()

    sddc_spec = json.load(open(args.config_file, "r"))

    main(args.file, sddc_spec['sddc'])

