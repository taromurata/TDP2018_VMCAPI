#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2018 tmurata <tmurata@ubuntu>
#
# Distributed under terms of the MIT license.

"""

"""

from organization_operations import *

print('test')

def main():
    org_operations = OperationsOnOrganizations()
    org_operations.options()
    org_operations.setup()
    org_operations.list_orgs()

if __name__ == '__main__':
    main()
