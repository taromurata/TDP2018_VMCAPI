#!/usr/bin/env python3
#

import sys
import argparse
import yaml
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

from vsphere_util import *


def main(info_file, config_file, vm_count, vm_name, ope):
    vsphere_util = vSphereUtil()
    vsphere_util.read_info(info_file)
    vsphere_util.login()
    vsphere_util.list_vms()

    vm_config = yaml.load(open(config_file, 'r'))
    # vm_name = vm_config['vm_name_default']

    for i in range(vm_count):
        tmp_vm_name = vm_name + f"{i}"
        vm_config['vm_name_default'] = tmp_vm_name
        vsphere_util.set_default_vm_spec(vm_config)

        if ope == 'create':
            vsphere_util.create_default_vm()
        elif ope == 'poweron':
            vsphere_util.poweron_default_vm()
        elif ope == 'delete':
            vsphere_util.cleanup_default_vm()
        else:
            print(f"Unknow operation {ope}", file=sys.stderr)


if __name__ == '__main__':
    parser = argparse.ArgumentParser();
    parser.add_argument('-f', '--file', action='store', type=str)
    parser.add_argument('-c', '--config_vm', action='store', type=str)
    parser.add_argument('-n', '--num_vms', action='store', type=int)
    parser.add_argument('-d', '--default_name', action='store', type=str)
    parser.add_argument('-o', '--operation', action='store', type=str)
    args = parser.parse_args()

    main(args.file, args.config_vm, args.num_vms, args.default_name, args.operation)

