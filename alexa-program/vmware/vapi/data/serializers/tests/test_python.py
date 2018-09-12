#!/usr/bin/env python

"""
Unit tests for DataValue <-> Python native value (de)serialization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import six
import unittest

from vmware.vapi.data.value import *
from vmware.vapi.data.definition import *
from vmware.vapi.data.serializers.python import build_py_value, build_data_value
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.lib.constants import DYNAMIC_STRUCTURE


class TestPyConverter(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_void(self):
        # Void Conversion
        data_def = VoidDefinition()
        data_val = build_data_value(None, data_def)
        self.assertEqual(data_val, VoidValue())
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, None)

    def test_integer(self):
        # Integer Conversion
        data_def = IntegerDefinition()
        data_val = build_data_value(10, data_def)
        self.assertEqual(data_val, IntegerValue(10))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, 10)
        self.assertTrue(isinstance(py_val, six.integer_types))

    def test_double(self):
        # Double Conversion
        data_def = DoubleDefinition()
        data_val = build_data_value(11.11, data_def)
        self.assertEqual(data_val, DoubleValue(11.11))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, 11.11)
        self.assertTrue(isinstance(py_val, float))

    def test_string(self):
        # String Conversion
        data_def = StringDefinition()
        data_val = build_data_value('test', data_def)
        self.assertEqual(data_val, StringValue('test'))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, 'test')
        self.assertTrue(isinstance(py_val, str))

    def test_boolean(self):
        # Boolean Conversion
        data_def = BooleanDefinition()
        data_val = build_data_value(True, data_def)
        self.assertEqual(data_val, BooleanValue(True))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, True)
        self.assertTrue(isinstance(py_val, bool))
        data_def = BooleanDefinition()
        data_val = build_data_value(False, data_def)
        self.assertEqual(data_val, BooleanValue(False))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, False)
        self.assertTrue(isinstance(py_val, bool))

    def test_opaque(self):
        data_def = OpaqueDefinition()
        data_val = IntegerValue(10)
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, data_val)
        py_val2 = build_data_value(10, data_def)
        self.assertEqual(py_val2, 10)

    def test_optional(self):
        data_def = OptionalDefinition(IntegerDefinition())
        data_val = build_data_value(10, data_def)
        self.assertEqual(data_val, OptionalValue(value=IntegerValue(10)))
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, 10)
        self.assertTrue(isinstance(py_val, six.integer_types))

        data_val = build_data_value(None, data_def)
        self.assertEqual(data_val, OptionalValue())
        py_val = build_py_value(data_val, data_def)
        self.assertEqual(py_val, None)

    class Properties(VapiStruct):
        _canonical_to_pep8_names = {
            'strVal' : 'str_val',
            'boolVal' : 'bool_val',
            'intVal' : 'int_val',
            'optVal' : 'opt_val',
            'listVal' : 'list_val'
        }
        def __init__(self, int_val, str_val, bool_val, opt_val, list_val):
            self.int_val = int_val
            self.str_val = str_val
            self.bool_val = bool_val
            self.opt_val = opt_val
            self.list_val = list_val
            VapiStruct.__init__(self)

    def test_structure(self):
        fields = [
            ('int_val', IntegerDefinition()),
            ('str_val', StringDefinition()),
            ('bool_val', BooleanDefinition()),
            ('opt_val', OptionalDefinition(IntegerDefinition())),
            ('list_val', ListDefinition(IntegerDefinition())),
        ]
        data_def = StructDefinition('Properties', fields)

        py_val = TestPyConverter.Properties(10, 'testing', True, 10, [10, 20, 30])
        data_valc = build_data_value(py_val, data_def)
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(data_valc, data_val)
        py_valc = build_py_value(data_valc, data_def, impl=self)
        self.assertEqual(py_val, py_valc)
        # Negative tests
        self.assertRaises(CoreException,
                          build_data_value,
                          TestPyConverter.Properties(None, 'testing', True, 10,
                                                     [10, 20, 30]),
                          data_def)
        self.assertRaises(CoreException,
                          build_data_value,
                          TestPyConverter.Properties(5.33, 'testing', True, 10,
                                                     [10, 20, 30]),
                          data_def)

    def test_dynamic_structure(self):
        data_def = DynamicStructDefinition()
        py_dict_val = {
            'int_val': 10,
            'str_val': 'testing',
            'bool_val': True,
            'opt_val': None,
            'list_val': [10, 20, 30],
            'struct_val': {
                'int_val': 100,
                'bool_val': False
            }
        }
        data_valc = build_data_value(py_dict_val, data_def)
        data_val = StructValue(DYNAMIC_STRUCTURE)
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue())
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        struct_val = StructValue(DYNAMIC_STRUCTURE)
        struct_val.set_field('int_val', IntegerValue(100))
        struct_val.set_field('bool_val', BooleanValue(False))
        data_val.set_field('struct_val', struct_val)
        self.assertEqual(data_valc, data_val)

    def test_dynamic_structure_neg(self):
        data_def = DynamicStructDefinition()
        py_val = TestPyConverter.Properties(10, 'testing', True, 10, [10, 20, 30])
        py_dict_val = {
            'struct_val': py_val,
        }
        self.assertRaises(CoreException,
                          build_data_value,
                          py_dict_val,
                          data_def)

if __name__ == '__main__':
    unittest.main()
