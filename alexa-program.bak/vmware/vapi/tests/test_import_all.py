"""
Import all the modules in vmware package to get coverage for all files
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import pkgutil
import unittest

import vmware

# Since this is in runtime testsuite, don't import client modules for code coverage
packages_to_ignore = ['vmware.vapi.client', 'vmware.vapi.wsgi']

class TestCoverage(unittest.TestCase):

    def test_coverage(self):
        to_process = [('vmware', vmware)]
        while len(to_process) > 0:
            prefix, element = to_process.pop()
            for _, mod_name, is_pkg in pkgutil.iter_modules(element.__path__):
                new_prefix = prefix + '.' + mod_name
                if new_prefix in packages_to_ignore:
                    continue
                try:
                    mod = __import__(new_prefix)
                except Exception:
                    pass
                if is_pkg:
                    for ns in new_prefix.split('.')[1:]:
                        mod = getattr(mod, ns)
                    to_process.append((prefix + '.' + mod_name, mod))

if __name__ == '__main__':
    unittest.main()
