#!/usr/bin/env python

"""
Unit tests for the type system
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import decimal

from vmware.vapi.data.value import *
from vmware.vapi.data.definition import *
from vmware.vapi.data.type import Type


class TestValue(unittest.TestCase):
    def setUp(self):
        pass

    ################################################
    #
    # Primitive Type tests
    #
    ################################################
    def test_void_value(self):
        val = VoidDefinition().new_value()
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, VoidValue))
        self.assertEqual(val, val)
        self.assertEqual(hash(val), hash(val))

    def test_integer_value(self):
        val = IntegerDefinition().new_value(22)
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, IntegerValue))
        self.assertEqual(val.value, 22)
        self.assertEqual(val.type, Type.INTEGER)
        val.value = 23
        self.assertEqual(val.value, 23)
        val1 = IntegerDefinition().new_value(23)
        self.assertEqual(val, val1)
        self.assertEqual(hash(val), hash(val1))
        val2 = IntegerDefinition().new_value(22)
        self.assertNotEqual(val, val2)
        self.assertRaises(CoreException, IntegerValue, 22.22)
        self.assertTrue(val2 <= val)
        self.assertTrue(val2 < val)
        self.assertTrue(val > val2)
        self.assertTrue(val >= val2)
        self.assertNotEqual(val, VoidDefinition().new_value())

    def test_double_value(self):
        val = DoubleDefinition().new_value(22.22)
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, DoubleValue))
        self.assertEqual(val.type, Type.DOUBLE)
        self.assertEqual(val.value, decimal.Decimal('22.22'))
        val1 = DoubleDefinition().new_value(22.22)
        self.assertEqual(val, val1)
        self.assertEqual(hash(val), hash(val1))
        val2 = DoubleDefinition().new_value(23.33)
        self.assertNotEqual(val, val2)
        self.assertRaises(CoreException, DoubleValue, "test")
        val3 = DoubleDefinition().new_value(decimal.Decimal('1E-130'))
        self.assertEqual(val3.value, decimal.Decimal('1E-130'))

    def test_double_invalid_value(self):
        self.assertRaises(CoreException, DoubleValue, decimal.Decimal('1E309'))
        self.assertRaises(CoreException, DoubleValue, decimal.Decimal('-1E309'))

    def test_string_value(self):
        val = StringDefinition().new_value("test")
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, StringValue))
        self.assertEqual(val.type, Type.STRING)
        self.assertIsInstance(val.value, str)
        self.assertEqual(val.value, "test")
        val1 = StringDefinition().new_value("test")
        self.assertEqual(val, val1)
        self.assertEqual(hash(val), hash(val1))
        val2 = StringDefinition().new_value("test1")
        self.assertNotEqual(val, val2)
        self.assertRaises(CoreException, StringValue, 11)

    def test_unicode_string_value(self):
        val = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        str_val = StringDefinition().new_value(val)
        self.assertEqual(str_val.value, val)

        val = u'\U0001d120'
        str_val = StringDefinition().new_value(val)
        self.assertEqual(str_val.value, val)

    def test_secret_value(self):
        val = SecretDefinition().new_value("test")
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, SecretValue))
        self.assertEqual(val.type, Type.SECRET)
        self.assertEqual(val.value, "test")
        self.assertEqual(str(val), '<secret>')
        self.assertNotEqual(str(val), 'test')
        val1 = SecretDefinition().new_value("test")
        self.assertEqual(val, val1)
        self.assertEqual(hash(val), hash(val1))
        val2 = SecretDefinition().new_value("test1")
        self.assertNotEqual(val, val2)
        self.assertRaises(CoreException, SecretValue, 11)

    def test_boolean_value(self):
        val = BooleanDefinition().new_value()
        self.assertNotEqual(val, None)
        self.assertTrue(isinstance(val, BooleanValue))
        val.value = True
        self.assertEqual(val.type, Type.BOOLEAN)
        self.assertTrue(BooleanDefinition().valid_instance_of(val))
        self.assertEqual(val.value, True)
        val1 = BooleanDefinition().new_value(True)
        self.assertEqual(val, val1)
        self.assertEqual(hash(val), hash(val1))
        val2 = BooleanDefinition().new_value(False)
        self.assertNotEqual(val, val2)

        self.assertFalse(IntegerDefinition().valid_instance_of(val))
        self.assertRaises(CoreException, BooleanValue, 11)

    ################################################
    #
    # Generic Type tests
    #
    ################################################

    def test_blob_value(self):
        blob_def = BlobDefinition()
        blob_val = blob_def.new_value(b'')
        self.assertNotEqual(blob_val, None)
        self.assertTrue(isinstance(blob_val, BlobValue))
        self.assertEqual(blob_val.type, Type.BLOB)
        # Negative test
        self.assertRaises(CoreException, BlobValue, u'')

    def test_optional(self):
        opt_def = OptionalDefinition(IntegerDefinition())
        opt_val = opt_def.new_value(IntegerValue(10))
        self.assertNotEqual(opt_val, None)
        self.assertEqual(opt_val.type, Type.OPTIONAL)
        self.assertEqual(opt_val.value, IntegerValue(10))

        opt_val2 = opt_def.new_value(IntegerValue(10))
        self.assertEqual(opt_val, opt_val2)
        self.assertEqual(hash(opt_val), hash(opt_val2))
        self.assertNotEqual(opt_val, opt_def.new_value(IntegerValue()))
        self.assertNotEqual(opt_val2, OptionalValue())

    def test_list(self):
        list_def = ListDefinition(IntegerDefinition())
        list_val = list_def.new_value()
        self.assertNotEqual(list_val, None)
        self.assertEqual(list_val.type, Type.LIST)
        self.assertTrue(list_val.is_empty())
        list_val.add(IntegerValue(10))

        list_val2 = list_def.new_value()
        list_val2.add(IntegerValue(10))
        self.assertEqual(list_val, list_val2)

        list_val2.add(IntegerValue(11))
        self.assertNotEqual(list_val, list_val2)

    def test_struct_value(self):
        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def = StructDefinition('test', fields)
        struct_val = struct_def.new_value()
        self.assertNotEqual(struct_val, None)
        self.assertEqual(struct_val.type, Type.STRUCTURE)

        struct_val.set_field('name', StringValue('test'))
        struct_val.set_field('age', IntegerValue(10))
        self.assertEqual(struct_val.get_field('name'), StringValue('test'))

        struct_val2 = struct_def.new_value()
        struct_val2.set_field('name', StringValue('test'))
        struct_val2.set_field('age', IntegerValue(10))
        self.assertEqual(struct_val, struct_val2)

        fields = [('address', OptionalDefinition(StringDefinition())),
                  ('age', IntegerDefinition()),
                  ('name', StringDefinition()),
                  ]
        struct_def2 = StructDefinition('test', fields)
        struct_val3 = struct_def2.new_value()
        struct_val3.set_field('age', IntegerValue(10))
        struct_val3.set_field('name', StringValue('test'))
        self.assertEqual(struct_val, struct_val3)

        struct_val2.set_field('address', OptionalValue(StringValue('Hillview')))
        self.assertNotEqual(struct_val, struct_val2)

        self.assertEqual(struct_val2.get_field('address').value, StringValue('Hillview'))
        self.assertRaises(CoreException, struct_val2.set_field, 'name', None)

        self.assertRaises(CoreException, struct_val2.get_field, 'random')
        self.assertEqual(struct_val2.get_field('name'), StringValue('test'))

    def test_struct_value_unicode(self):
        # Test struct value with unicode struct name/field names
        fields = [(u'name', StringDefinition()),
                  (u'age', IntegerDefinition()),
                  (u'address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def = StructDefinition(u'test', fields)
        struct_val = struct_def.new_value()
        self.assertNotEqual(struct_val, None)
        self.assertEqual(struct_val.type, Type.STRUCTURE)

        struct_val.set_field('name', StringValue('test'))
        struct_val.set_field('age', IntegerValue(10))
        self.assertEqual(struct_val.get_field('name'), StringValue('test'))

        struct_val2 = struct_def.new_value()
        struct_val2.set_field('name', StringValue('test'))
        struct_val2.set_field('age', IntegerValue(10))
        self.assertEqual(struct_val, struct_val2)


if __name__ == "__main__":
    unittest.main()
