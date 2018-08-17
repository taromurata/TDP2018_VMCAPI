#!/usr/bin/env python

"""
Unit tests for the type system
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import six
import unittest

from vmware.vapi.data.value import *
from vmware.vapi.data.definition import *
from vmware.vapi.data.type import Type
from vmware.vapi.message import Message
from vmware.vapi.exception import CoreException


class TestDefinition(unittest.TestCase):
    def setUp(self):
        localizable_message_def = StructDefinition(
            'LocalizableMessage',
            (('id', StringDefinition()),
             ('default_message', StringDefinition()),
             ('args', ListDefinition(StringDefinition()))))
        self.messages_list_def = ListDefinition(localizable_message_def)

        message1 = Message('suites.test_error.TestErrorValue.message1',
                           'Message 1 - %s %s', 'arg1', 'arg2')
        msg_struct1 = localizable_message_def.new_value()
        msg_struct1.set_field('id', StringValue(message1.id))
        msg_struct1.set_field('default_message', StringValue(message1.def_msg))
        args_list = ListValue()
        args_list.add_all((StringValue(s) for s in message1.args))
        msg_struct1.set_field('args', args_list)
        message2 = Message('suites.test_error.TestErrorValue.message2',
                           'Message 2')
        msg_struct2 = localizable_message_def.new_value()
        msg_struct2.set_field('id', StringValue(message2.id))
        msg_struct2.set_field('default_message', StringValue(message2.def_msg))
        msg_struct2.set_field('args', ListValue())
        message3 = Message('suites.test_error.TestErrorValue.message3',
                           'Message 3')
        msg_struct3 = localizable_message_def.new_value()
        msg_struct3.set_field('id', StringValue(message3.id))
        msg_struct3.set_field('default_message', StringValue(message3.def_msg))
        msg_struct3.set_field('args', ListValue())
        self.messages_list_value = ListValue()
        self.messages_list_value.add_all(
            [msg_struct1, msg_struct2, msg_struct3])

    ################################################
    #
    # Primitive Type tests
    #
    ################################################
    def test_void_definition(self):
        void_def = VoidDefinition()
        self.assertNotEqual(void_def, None)
        self.assertEqual(void_def.type, Type.VOID)
        self.assertEqual(void_def, void_def)
        self.assertEqual(hash(void_def), hash(void_def))
        self.assertNotEqual(void_def, StringDefinition())
        self.assertNotEqual(void_def, "test")

        self.assertFalse(void_def.valid_instance_of(None))
        self.assertFalse(void_def.valid_instance_of(StringValue("test")))

    def test_integer_definition(self):
        int_def = IntegerDefinition()
        self.assertNotEqual(int_def, None)
        self.assertEqual(int_def.type, Type.INTEGER)
        self.assertEqual(int_def, int_def)
        self.assertEqual(hash(int_def), hash(int_def))

        self.assertFalse(int_def.valid_instance_of(None))
        self.assertTrue(int_def.valid_instance_of(IntegerValue(10)))
        self.assertFalse(int_def.valid_instance_of(StringValue("test")))

    def test_double_definition(self):
        d_def = DoubleDefinition()
        self.assertNotEqual(d_def, None)
        self.assertEqual(d_def.type, Type.DOUBLE)
        self.assertEqual(d_def, d_def)
        self.assertEqual(hash(d_def), hash(d_def))

        self.assertFalse(d_def.valid_instance_of(None))
        self.assertTrue(d_def.valid_instance_of(DoubleValue(10.0)))
        self.assertFalse(d_def.valid_instance_of(StringValue("test")))

    def test_string_definition(self):
        s_def = StringDefinition()
        self.assertNotEqual(s_def, None)
        self.assertEqual(s_def.type, Type.STRING)
        self.assertEqual(s_def, s_def)
        self.assertEqual(hash(s_def), hash(s_def))

        self.assertFalse(s_def.valid_instance_of(None))
        self.assertTrue(s_def.valid_instance_of(StringValue("test")))
        self.assertFalse(s_def.valid_instance_of(IntegerValue(10)))

    def test_secret_definition(self):
        s_def = SecretDefinition()
        self.assertNotEqual(s_def, None)
        self.assertEqual(s_def.type, Type.SECRET)
        self.assertEqual(s_def, s_def)
        self.assertEqual(hash(s_def), hash(s_def))

        self.assertFalse(s_def.valid_instance_of(None))
        self.assertTrue(s_def.valid_instance_of(SecretValue("test")))
        self.assertFalse(s_def.valid_instance_of(IntegerValue(10)))

    def test_boolean_definition(self):
        b_def = BooleanDefinition()
        self.assertNotEqual(b_def, None)
        self.assertEqual(b_def.type, Type.BOOLEAN)
        self.assertEqual(b_def, b_def)
        self.assertEqual(hash(b_def), hash(b_def))

    ################################################
    #
    # Generic Type tests
    #
    ################################################

    def test_blob_definition(self):
        blob_def = BlobDefinition()
        self.assertNotEqual(blob_def, None)
        self.assertEqual(blob_def.type, Type.BLOB)

    def test_opaque_definition(self):
        opaque_def = OpaqueDefinition()
        self.assertNotEqual(opaque_def, None)
        self.assertEqual(opaque_def.type, Type.OPAQUE)
        self.assertTrue(opaque_def.valid_instance_of(IntegerValue(10)))

    def test_optional_definition(self):
        opt_def = OptionalDefinition(IntegerDefinition())
        self.assertNotEqual(opt_def, None)
        self.assertEqual(opt_def.type, Type.OPTIONAL)
        self.assertEqual(opt_def.element_type.type, Type.INTEGER)
        self.assertEqual(opt_def, opt_def)
        self.assertEqual(hash(opt_def), hash(opt_def))
        opt_def2 = OptionalDefinition(StringDefinition())
        self.assertNotEqual(opt_def, opt_def2)

        self.assertFalse(opt_def.valid_instance_of(None))
        self.assertFalse(opt_def.valid_instance_of(IntegerValue(10)))
        opt_val = opt_def.new_value(IntegerValue(10))
        self.assertTrue(opt_def.valid_instance_of(opt_val))
        opt_val1 = opt_def.new_value()
        self.assertTrue(opt_def.valid_instance_of(opt_val1))
        opt_val2 = OptionalValue(value=StringValue("test"))
        self.assertFalse(opt_def.valid_instance_of(opt_val2))

    def test_optional_definition_complete_value(self):
        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def = StructDefinition('test', fields)
        struct_ref_def = StructRefDefinition('test')
        struct_ref_def.target = struct_def
        opt_def = OptionalDefinition(struct_ref_def)

        unset_opt_value = OptionalValue()
        opt_def.complete_value(unset_opt_value)
        self.assertFalse(unset_opt_value.is_set())

        to_complete = StructValue('test')
        to_complete.set_field('name', StringValue('the_name'))
        to_complete.set_field('age', IntegerValue(42))

        opt_def.complete_value(OptionalValue(to_complete))
        self.assertEqual(StringValue('the_name'), to_complete.get_field('name'))
        self.assertEqual(IntegerValue(42), to_complete.get_field('age'))
        self.assertTrue(to_complete.has_field('address'))
        self.assertEqual(OptionalValue(), to_complete.get_field('address'))

    def test_list_definition(self):
        list_def = ListDefinition(IntegerDefinition())
        self.assertNotEqual(list_def, None)
        self.assertEqual(list_def.type, Type.LIST)
        self.assertEqual(list_def.element_type.type, Type.INTEGER)
        self.assertEqual(list_def, list_def)
        self.assertEqual(hash(list_def), hash(list_def))
        list_def2 = ListDefinition(StringDefinition())
        self.assertNotEqual(list_def, list_def2)
        self.assertNotEqual(list_def, IntegerDefinition())

        self.assertFalse(list_def.valid_instance_of(None))
        list_val = list_def.new_value()
        list_val.add(IntegerValue(10))
        self.assertTrue(list_def.valid_instance_of(list_val))
        list_val4 = ListValue()
        list_val4.add(IntegerValue(10))

        list_val3 = ListValue()
        list_val3.add(IntegerValue(10))
        list_val3.add(StringValue("test"))
        self.assertFalse(list_def.valid_instance_of(list_val3))

    def test_list_definition_complete_value(self):
        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def = StructDefinition('test', fields)
        list_def = ListDefinition(OptionalDefinition(struct_def))

        empty_list_value = ListValue()
        list_def.complete_value(empty_list_value)
        self.assertTrue(empty_list_value.is_empty())

        list_value_unset_opt = ListValue([OptionalValue()])
        list_def.complete_value(list_value_unset_opt)
        self.assertEqual(1, list_value_unset_opt.size())
        self.assertFalse(six.next(iter(list_value_unset_opt)).is_set())

        to_complete = StructValue('test')
        to_complete.set_field('name', StringValue('the_name'))
        to_complete.set_field('age', IntegerValue(42))

        list_value = ListValue()
        list_value.add(OptionalValue(to_complete))
        list_def.complete_value(list_value)
        self.assertEqual(1, list_value.size())
        self.assertEqual(StringValue('the_name'), to_complete.get_field('name'))
        self.assertEqual(IntegerValue(42), to_complete.get_field('age'))
        self.assertTrue(to_complete.has_field('address'))
        self.assertEqual(OptionalValue(), to_complete.get_field('address'))

    def test_struct_definition(self):
        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def = StructDefinition('test', fields)
        self.assertNotEqual(struct_def, None)
        self.assertEqual(struct_def.type, Type.STRUCTURE)
        self.assertEqual(struct_def, struct_def)
        self.assertEqual(hash(struct_def), hash(struct_def))
        self.assertEqual(set(['name', 'age', 'address']),
                         set(struct_def.get_field_names()))

        struct_def2 = StructDefinition('test2', fields)
        self.assertNotEqual(struct_def, struct_def2)

        fields = [('name', StringDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_def3 = StructDefinition('test', fields)
        self.assertNotEqual(struct_def, struct_def3)

        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', StringDefinition()),
                  ]
        struct_def4 = StructDefinition('test', fields)
        self.assertNotEqual(struct_def, struct_def4)

        fields = [('address', OptionalDefinition(StringDefinition())),
                  ('age', IntegerDefinition()),
                  ('name', StringDefinition()),
                  ]
        struct_def5 = StructDefinition('test', fields)
        self.assertEqual(struct_def, struct_def5)
        self.assertEqual(hash(struct_def), hash(struct_def5))

        self.assertNotEqual(struct_def, IntegerDefinition())

        self.assertFalse(struct_def.valid_instance_of(IntegerValue(10)))
        struct_val = struct_def.new_value()
        struct_val.set_field('name', StringValue('test'))
        struct_val.set_field('age', IntegerValue(10))
        struct_val.set_field('address', OptionalValue())
        self.assertTrue(struct_def.valid_instance_of(struct_val))

        struct_val2 = struct_def2.new_value()
        self.assertFalse(struct_def.valid_instance_of(struct_val2))

        struct_val3 = struct_def3.new_value()
        struct_val.set_field('name', StringValue('test'))
        self.assertFalse(struct_def.valid_instance_of(struct_val3))

        struct_val4 = struct_def4.new_value()
        struct_val4.set_field('name', StringValue('test'))
        struct_val4.set_field('age', IntegerValue(10))
        struct_val4.set_field('address', StringValue('test'))
        self.assertFalse(struct_def.valid_instance_of(struct_val4))

        struct_val5 = StructValue('test')
        struct_val5.set_field('name', StringValue('test'))
        struct_val5.set_field('age', IntegerValue(10))
        struct_val5.set_field('address',
                              OptionalValue(value=StringValue('test')))
        self.assertTrue(struct_def.valid_instance_of(struct_val5))

    def test_dynamic_struct_definition(self):
        dynamic_struct_def = DynamicStructDefinition()
        self.assertNotEqual(dynamic_struct_def, None)
        self.assertEqual(dynamic_struct_def.type, Type.DYNAMIC_STRUCTURE)

    def test_any_error_definition(self):
        any_error_def = AnyErrorDefinition()
        self.assertNotEqual(any_error_def, None)
        self.assertEqual(any_error_def.type, Type.ANY_ERROR)

    def test_struct_ref_definition(self):
        struct_def = StructRefDefinition('test')
        self.assertNotEqual(struct_def, None)
        self.assertEqual(struct_def.type, Type.STRUCTURE_REF)
        self.assertEqual(struct_def.name, 'test')
        self.assertEqual(struct_def, struct_def)
        self.assertEqual(hash(struct_def), hash(struct_def))
        self.assertRaises(CoreException, struct_def.check_resolved)
        try:
            struct_def.target = None
            raise Exception('Target set to None')
        except ValueError:
            pass
        try:
            struct_def.target = StructDefinition('bogus', [])
            raise Exception('Target set to a different structure')
        except CoreException:
            pass
        target = StructDefinition('test',
                                  [('field', StringDefinition())])
        self.assertRaises(CoreException, struct_def.check_resolved)
        struct_def.target = target
        # Should not throw exception after target is set
        struct_def.check_resolved()
        self.assertEqual(struct_def.target, target)

    def test_struct_ref_definition_complete_value(self):
        struct_ref_def = StructRefDefinition('test')
        self.assertIsNone(struct_ref_def.target)
        self.assertRaises(CoreException, struct_ref_def.complete_value, StructValue('test'))

        fields = [('name', StringDefinition()),
                  ('age', IntegerDefinition()),
                  ('address', OptionalDefinition(StringDefinition())),
                  ]
        struct_ref_def.target = StructDefinition('test', fields)
        to_complete = StructValue('test')
        to_complete.set_field('name', StringValue('the_name'))
        to_complete.set_field('age', IntegerValue(42))
        struct_ref_def.complete_value(to_complete)
        self.assertEqual(StringValue('the_name'), to_complete.get_field('name'))
        self.assertEqual(IntegerValue(42), to_complete.get_field('age'))
        self.assertTrue(to_complete.has_field('address'))
        self.assertEqual(OptionalValue(), to_complete.get_field('address'))

    def test_error_definition(self):
        errorName = 'vmware.vapi.data.test_definition.TestError'

        error_def = ErrorDefinition(errorName,
                                    [('messages', self.messages_list_def),
                                     ('boolField', BooleanDefinition()),
                                     ('doubleField', DoubleDefinition()),
                                    ])
        self.assertNotEqual(error_def, None)
        self.assertEqual(error_def.type, Type.ERROR)
        self.assertEqual(error_def, error_def)
        self.assertEqual(hash(error_def), hash(error_def))
        self.assertEqual(set(['messages', 'boolField', 'doubleField', ]),
                         set(error_def.get_field_names()))
        self.assertNotEqual(error_def, IntegerDefinition())
        self.assertFalse(error_def.valid_instance_of(IntegerValue(10)))

        struct_def = StructDefinition(errorName,
                                      [('messages', self.messages_list_def),
                                       ('boolField', BooleanDefinition()),
                                       ('doubleField', DoubleDefinition()),
                                      ])
        self.assertNotEqual(error_def, struct_def)
        self.assertNotEqual(struct_def, error_def)

        error_value = error_def.new_value()
        error_value.set_field('messages', self.messages_list_value)
        error_value.set_field('boolField', BooleanDefinition().new_value(False))
        error_value.set_field('doubleField',
                              DoubleDefinition().new_value(22.22))
        # Include an extra field in the error value to test inclusive validation
        error_value.set_field('stringField',
                              StringDefinition().new_value('hello world'))
        self.assertTrue(error_def.valid_instance_of(error_value))
        self.assertFalse(struct_def.valid_instance_of(error_value))

        struct_value = struct_def.new_value()
        struct_value.set_field('messages', self.messages_list_value)
        struct_value.set_field('boolField',
                               BooleanDefinition().new_value(False))
        struct_value.set_field('doubleField',
                              DoubleDefinition().new_value(22.22))
        self.assertFalse(error_def.valid_instance_of(struct_value))

        struct2_name = 'vmware.vapi.data.test_definition.StructWithErrorField'
        struct2_def = StructDefinition(struct2_name, [('error', error_def)])
        struct2_value = struct2_def.new_value()
        struct2_value.set_field('error', error_value)
        self.assertTrue(struct2_def.valid_instance_of(struct2_value))

if __name__ == "__main__":
    unittest.main()
