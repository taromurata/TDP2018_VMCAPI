#!/usr/bin/env python3
#

import argparse
import yaml
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

from vsphere_util import *


def main(info_file, config_file, vm_count):
    vsphere_util = vSphereUtil()
    vsphere_util.read_info(info_file)
    vsphere_util.login()
    vsphere_util.list_vms()

    vm_config = yaml.load(open(config_file, 'r'))
    vm_name = vm_config['vm_name_default']

    for i in range(vm_count):
        tmp_vm_name = vm_name + f"{i}"
        vm_config['vm_name_default'] = tmp_vm_name
        vsphere_util.set_default_vm_spec(vm_config)
        vsphere_util.poweron_default_vm()

if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('-f', '--file', action='store', type=str)
    parser.add_argument('-c', '--config_vm', action='store', type=str)
    parser.add_argument('-n', '--num_vms', action='store', type=int)
    args = parser.parse_args()

    main(args.file, args.config_vm, args.num_vms)

