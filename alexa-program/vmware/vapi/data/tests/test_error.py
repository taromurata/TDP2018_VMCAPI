"""
Unit tests for ErrorValue
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import six
import unittest

from vmware.vapi.data.value import (
    ListValue,
    StringValue,
    StructValue,
    )
from vmware.vapi.lib.std import (
    make_error_value_from_msgs,
    make_std_error_def,
    _make_struct_value_from_message,
)
from vmware.vapi.message import Message


class TestErrorValue(unittest.TestCase):
    def setUp(self):
        self.error_name = 'suites.test_error.TestErrorValue.SampleError'
        self.error_def = make_std_error_def(self.error_name)
        self.message1 = Message('suites.test_error.TestErrorValue.message1',
                                'Message 1 - %s %s', 'arg1', 'arg2')
        self.message2 = Message('suites.test_error.TestErrorValue.message2',
                                'Message 2')
        self.message3 = Message('suites.test_error.TestErrorValue.message3',
                                'Message 3')
        self.single_message = (self.message1, )
        self.multiple_messages = (self.message1, self.message2, self.message3)

    def test_single_message_list_construction(self):
        ev = make_error_value_from_msgs(self.error_def, *self.single_message)

        self.assertEqual(self.error_name, ev.name)
        messages = ev.get_field('messages')
        self.assertEqual(len(self.single_message), len(messages))
        it = iter(messages)
        self.assertEqual(_make_struct_value_from_message(self.message1),
                         six.advance_iterator(it))
        self.assertRaises(StopIteration, lambda it: six.advance_iterator(it), it)

    def test_multiple_message_list_construction(self):
        ev = make_error_value_from_msgs(self.error_def, *self.multiple_messages)

        self.assertEqual(self.error_name, ev.name)
        messages = ev.get_field('messages')
        self.assertEqual(len(self.multiple_messages), len(messages))
        it = iter(messages)
        self.assertEqual(_make_struct_value_from_message(self.message1),
                         six.advance_iterator(it))
        self.assertEqual(_make_struct_value_from_message(self.message2),
                         six.advance_iterator(it))
        self.assertEqual(_make_struct_value_from_message(self.message3),
                         six.advance_iterator(it))
        self.assertRaises(StopIteration, lambda it: six.advance_iterator(it), it)

    def test_error_value_as_data_value(self):
        ev = make_error_value_from_msgs(self.error_def, *self.multiple_messages)
        self.assertTrue(isinstance(ev, StructValue))
        self.assertEqual(self.error_name, ev.name)
        self.assertFalse(ev.get_field_names() is None)
        self.assertEqual(2, len(ev.get_field_names()))
        self.assertTrue('messages' in ev.get_field_names())

        msg_struct1 = StructValue('localizable_message')
        msg_struct1.set_field('id', StringValue(self.message1.id))
        msg_struct1.set_field('default_message',
                              StringValue(self.message1.def_msg))
        args_list = ListValue()
        args_list.add_all((StringValue(s) for s in self.message1.args))
        msg_struct1.set_field('args', args_list)
        msg_struct2 = StructValue('localizable_message')
        msg_struct2.set_field('id', StringValue(self.message2.id))
        msg_struct2.set_field('default_message',
                              StringValue(self.message2.def_msg))
        msg_struct2.set_field('args', ListValue())
        msg_struct3 = StructValue('localizable_message')
        msg_struct3.set_field('id', StringValue(self.message3.id))
        msg_struct3.set_field('default_message',
                              StringValue(self.message3.def_msg))
        msg_struct3.set_field('args', ListValue())
        messages = ListValue()
        messages.add_all([msg_struct1, msg_struct2, msg_struct3])
        expected_data_value = ev = make_error_value_from_msgs(self.error_def)
        expected_data_value.set_field('messages', messages)
        self.assertEqual(expected_data_value, ev)
