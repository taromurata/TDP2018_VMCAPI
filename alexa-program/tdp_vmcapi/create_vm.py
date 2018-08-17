#!/usr/bin/env python3
#
# https://github.com/vmware/vsphere-automation-sdk-python
#

import argparse
import yaml
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

from vsphere_util import *


def main(info_file):
    vsphere_util = vSphereUtil()
    vsphere_util.read_info(info_file)
    vsphere_util.login()
    vsphere_util.list_vms()

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('-f', '--file', action='store', type=str)
    args = parser.parse_args()

    main(args.file)
