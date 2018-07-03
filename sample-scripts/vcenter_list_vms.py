#
# https://github.com/vmware/vsphere-automation-sdk-python
#

import argparse
import yaml
import requests
import urllib3
from vmware.vapi.vsphere.client import create_vsphere_client

# Read an info file.
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', action='store', type=str)

args = parser.parse_args()

info = yaml.load(open(args.file, "r+"))
vcenter_ip = info['vcenter']['ip']
vcenter_username = info['vcenter']['username']
vcenter_password = info['vcenter']['password']

# print(vcenter_ip)
# print(vcenter_username)
# print(vcenter_password)

#
session = requests.session()

# Disable cert verification for demo purpose.
# This is not recommended in a production environment.
session.verify = False

# Disable the secure connection warning for demo purpose.
# This is not recommended in a production environment.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Connect to a vCenter Server using username and password
vsphere_client = create_vsphere_client(server=vcenter_ip,
        username=vcenter_username, password=vcenter_password, session=session)

# List all VMs inside the vCenter Server
print(vsphere_client.vcenter.VM.list())

