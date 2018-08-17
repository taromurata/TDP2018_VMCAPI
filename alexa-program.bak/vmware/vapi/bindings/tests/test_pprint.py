#!/usr/bin/env python
"""
Unit tests for VapiStruct pretty printer
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
from six.moves import cStringIO

from vmware.vapi.bindings.struct import (VapiStruct, PrettyPrinter)


class TestStructPrinter(unittest.TestCase):

    def test_struct_primitive(self):
        class Properties(VapiStruct):
            def __init__(self, int_val, str_val, bool_val):
                self.int_val = int_val
                self.str_val = str_val
                self.bool_val = bool_val
                VapiStruct.__init__(self)

        value = Properties(int_val=10,
                           str_val='hello',
                           bool_val=True)
        output = cStringIO()
        PrettyPrinter(stream=output).pprint(value)
        expected_output = """Properties(
    bool_val=True,
    int_val=10,
    str_val='hello',
),
"""
        self.assertEqual(expected_output, output.getvalue())

    def test_struct_generic(self):
        class Properties(VapiStruct):
            def __init__(self, list_val, opt_val=None):
                self.list_val = list_val
                self.opt_val = opt_val
                VapiStruct.__init__(self)

        value = Properties(list_val=[10,20,30],
                           opt_val=None)
        output = cStringIO()
        PrettyPrinter(stream=output).pprint(value)
        expected_output = """Properties(
    list_val=[
        10,
        20,
        30,
    ],
    opt_val=None,
),
"""
        self.assertEqual(expected_output, output.getvalue())

    def test_struct_with_struct(self):
        class Properties(VapiStruct):
            def __init__(self, int_val, struct_val=None):
                self.int_val = int_val
                self.struct_val = struct_val

        value_nested = Properties(int_val=20)
        value = Properties(int_val=10, struct_val=value_nested)
        output = cStringIO()
        PrettyPrinter(stream=output).pprint(value)
        expected_output = """Properties(
    int_val=10,
    struct_val=Properties(
        int_val=20,
        struct_val=None,
    ),
),
"""
        self.assertEqual(expected_output, output.getvalue())

if __name__ == '__main__':
   unittest.main()
