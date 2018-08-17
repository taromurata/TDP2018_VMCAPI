#!/usr/bin/env python
"""
Unit tests for python VapiStruct class
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import decimal
import json
import logging
import sys
import unittest

from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.type import (
    StructType, StringType, BooleanType, IntegerType, ListType,
    OptionalType, ReferenceType)


class NestedProperties(VapiStruct):
    def __init__(self, int_val=None):
        self.int_val = int_val
        VapiStruct.__init__(self)

NestedProperties._set_binding_type(StructType(
    'nested_properties', {
        'int_val': IntegerType(),
    }, NestedProperties))

class Properties(VapiStruct):
    def __init__(self, int_val=None, str_val=None, bool_val=None,
                 opt_val=None, list_val=None, nested_val=None):
        self.int_val = int_val
        self.str_val = str_val
        self.bool_val = bool_val
        self.opt_val = opt_val
        self.list_val = list_val
        self.nested_val = nested_val
        VapiStruct.__init__(self)

Properties._set_binding_type(StructType(
    'properties', {
        'int_val': IntegerType(),
        'str_val': StringType(),
        'bool_val': BooleanType(),
        'opt_val': OptionalType(IntegerType()),
        'list_val': ListType(IntegerType()),
        'nested_val': ReferenceType(__name__, 'NestedProperties')
    }, Properties))

class TestVapiStruct(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_dict_conversion(self):
        nested_val = NestedProperties(int_val=10)
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30],
                            nested_val=nested_val)
        actual_output = py_val.to_dict()
        expected_output = {
            'int_val': 10,
            'str_val': 'testing',
            'bool_val': True,
            'opt_val': 10,
            'list_val': [10, 20, 30],
            'nested_val': {
                'int_val': 10
            }
        }
        self.assertEqual(actual_output, expected_output)

        # test with unset optional
        nested_val = NestedProperties(int_val=10)
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            list_val=[10, 20, 30],
                            nested_val=nested_val)
        actual_output = py_val.to_dict()
        expected_output = {
            'int_val': 10,
            'str_val': 'testing',
            'bool_val': True,
            'list_val': [10, 20, 30],
            'nested_val': {
                'int_val': 10
            }
        }
        self.assertEqual(actual_output, expected_output)

    def test_json_conversion(self):
        nested_val = NestedProperties(int_val=10)
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30],
                            nested_val=nested_val)
        json_output = py_val.to_json()
        dict_output = json.loads(json_output, parse_float=decimal.Decimal)
        expected_output = {
            'int_val': 10,
            'str_val': 'testing',
            'bool_val': True,
            'opt_val': 10,
            'list_val': [10, 20, 30],
            'nested_val': {
                'int_val': 10
            }
        }
        self.assertEqual(dict_output, expected_output)

        # test with unset optional
        nested_val = NestedProperties(int_val=10)
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            list_val=[10, 20, 30],
                            nested_val=nested_val)
        json_output = py_val.to_json()
        dict_output = json.loads(json_output, parse_float=decimal.Decimal)
        expected_output = {
            'int_val': 10,
            'str_val': 'testing',
            'bool_val': True,
            'list_val': [10, 20, 30],
            'nested_val': {
                'int_val': 10
            }
        }
        self.assertEqual(dict_output, expected_output)

if __name__ == '__main__':
    unittest.main()
