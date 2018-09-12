#!/usr/bin/env python
# -*- coding: UTF-8 -*-


"""
Unit tests for the vapi clean json serializer
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015-2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import base64
import decimal
import unittest
import logging
import json
import six

from vmware.vapi.data.value import (
    VoidValue,
    IntegerValue,
    DoubleValue,
    StringValue,
    SecretValue,
    BooleanValue,
    BlobValue,
    OptionalValue,
    ListValue,
    StructValue,
    ErrorValue,
)
from vmware.vapi.data.serializers.cleanjson import DataValueConverter, JsonDictToVapi

logging.basicConfig(level=logging.DEBUG)


class TestJsonEncoder(unittest.TestCase):
    def test_struct_value(self):
        input_val = StructValue(
            name='name',
            values={
                'val1': StringValue('val1'),
                'val2': StringValue('val2')
            })
        actual_val = DataValueConverter.convert_to_json(input_val)
        self.assertTrue('"val1":"val1"' in actual_val)
        self.assertTrue('"val2":"val2"' in actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_struct_value_with_optional_set(self):
        input_val = StructValue(
            name='name',
            values={
                'val1': StringValue('val1'),
                'val2': OptionalValue(StringValue('val2'))
            })
        actual_val = DataValueConverter.convert_to_json(input_val)
        self.assertTrue('"val1":"val1"' in actual_val)
        self.assertTrue('"val2":"val2"' in actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_struct_value_with_optional_unset(self):
        input_val = StructValue(
            name='name',
            values={
                'val1': StringValue('val1'),
                'val2': OptionalValue()
            })
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '{"val1":"val1"}'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_error_value(self):
        input_val = ErrorValue(
            name='name',
            values={
                'val1': StringValue('val1'),
                'val2': StringValue('val2')
            })
        actual_val = DataValueConverter.convert_to_json(input_val)
        self.assertTrue('"val1":"val1"' in actual_val)
        self.assertTrue('"val2":"val2"' in actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_list_value(self):
        input_val = ListValue(
            values=[StringValue('val1'), StringValue('val2')]
        )
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '["val1","val2"]'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_optional_value(self):
        input_val = OptionalValue(StringValue('val1'))
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"val1"'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

        input_val = OptionalValue()
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = 'null'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_string_value(self):
        input_val = StringValue('val1')
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"val1"'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_integer_value(self):
        input_val = IntegerValue(10)
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '10'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_boolean_value(self):
        input_val = BooleanValue(True)
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = 'true'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_void_value(self):
        input_val = VoidValue()
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = 'null'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_binary_value(self):
        input_val = BlobValue(b'asdlkfu')
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"%s"' % base64.b64encode(b'asdlkfu').decode('utf-8')

        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_binary_value_2(self):
        input_val = BlobValue(b'0\x82\x04\x00')
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"%s"' % base64.b64encode(b'0\x82\x04\x00').decode('utf-8')

        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_secret_value(self):
        input_val = SecretValue('password')
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"password"'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_default(self):
        input_val = 'hello'
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '"hello"'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        json.loads(actual_val)

    def test_double_value(self):
        input_val = DoubleValue(10.10)
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '1.01E1'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        output = json.loads(actual_val, parse_float=decimal.Decimal)
        self.assertEqual(output, decimal.Decimal('10.10'))

        input_val = DoubleValue(decimal.Decimal('10.10'))
        actual_val = DataValueConverter.convert_to_json(input_val)
        expected_val = '1.01E1'
        self.assertEqual(expected_val, actual_val)
        # Verify json is valid
        output = json.loads(actual_val, parse_float=decimal.Decimal)
        self.assertEqual(output, decimal.Decimal('10.10'))


class TestJsonDecoder(unittest.TestCase):
    def test_string(self):
        input_val = '"val1"'
        expected_val = StringValue('val1')
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_unicode_string(self):
        input_val = '"val??"'
        expected_val = StringValue(u'val??')
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_integer(self):
        input_val = '10'
        expected_val = IntegerValue(10)
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

        input_val = '1000000000000000000000000000000'
        long_val = 1000000000000000000000000000000
        expected_val = IntegerValue(long_val)
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_boolean(self):
        input_val = 'true'
        expected_val = BooleanValue(True)
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

        input_val = 'false'
        expected_val = BooleanValue(False)
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_float(self):
        input_val = '1.01E1'
        expected_val = DoubleValue(decimal.Decimal('10.10'))
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_empty_list(self):
        input_val = '[]'
        expected_val = ListValue()
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_list(self):
        input_val = '["val1","val2"]'
        expected_val = ListValue(
            values=[StringValue('val1'), StringValue('val2')]
        )
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_none(self):
        input_val = 'null'
        expected_val = OptionalValue()
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

    def test_dict(self):
        input_val = '{"int_field":10, "bool_field":true}'
        values = {
            'bool_field': BooleanValue(True),
            'int_field': IntegerValue(10)
        }
        expected_val = StructValue(values=values)
        actual_val = DataValueConverter.convert_to_data_value(input_val)
        self.assertEqual(expected_val, actual_val)

if __name__ == "__main__":
    unittest.main()
