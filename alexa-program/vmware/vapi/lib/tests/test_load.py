"""
Unit tests for dynamic loading
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest

from vmware.vapi.lib.load import dynamic_import


class TestDynamicImport(unittest.TestCase):

    def test_load_success(self):
        di = dynamic_import('vmware.vapi.lib.load.dynamic_import')
        self.assertEqual(di.__name__, 'dynamic_import')
        self.assertEqual(di.__module__, 'vmware.vapi.lib.load')

    def test_load_failure(self):
        di = dynamic_import('vmware.vapi.lib.loadx.dynamic_import')
        self.assertEqual(di, None)

    def test_load_failure_attr(self):
        di = dynamic_import('vmware.vapi.lib.load.dynamic_importx')
        self.assertEqual(di, None)


if __name__ == "__main__":
    unittest.main()
