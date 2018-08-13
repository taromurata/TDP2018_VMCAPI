"""
Unit tests for l10n bindings
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import unittest
import decimal
import locale

from vmware.vapi.bindings.datetime_helper import DateTimeConverter
from vmware.vapi.l10n.constants import DEFAULT_LOCALE
from vmware.vapi.l10n.formatter import StringFormatter
from vmware.vapi.l10n.bundle import DictionaryResourceBundle
from vmware.vapi.stdlib.provider.factories import LocalizableMessageFactory
from com.vmware.vapi.std_provider import LocalizableMessage


class TestBindings(unittest.TestCase):
    def setUp(self):
        locale.setlocale(locale.LC_ALL, DEFAULT_LOCALE)

    def test_simple(self):
        messages = {'foo.str': 'some string'}
        rb = DictionaryResourceBundle(messages)
        lf = LocalizableMessageFactory(rb, StringFormatter)
        actual_result = lf.get_message('foo.str')
        expected_result = LocalizableMessage(default_message='some string',
                                             args=[],
                                             id='foo.str')
        self.assertEqual(expected_result, actual_result)

    def test_complex(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        messages = {'foo.str.complex': 'string %s, long %d, float %f, time %tc'}
        rb = DictionaryResourceBundle(messages)
        lf = LocalizableMessageFactory(rb, StringFormatter)
        actual_result = lf.get_message('foo.str.complex',
                                       'hello', 123, decimal.Decimal('123.456'), dt)
        expected_result = LocalizableMessage(
            default_message='string hello, long 123, float 123.456000, time Sat 04 Mar 1978 05:06:07 AM',
            args=['hello', '123', '123.456', '1978-03-04T05:06:07.100Z'],
            id='foo.str.complex')
        self.assertEqual(expected_result, actual_result)

    def test_unknown(self):
        messages = {}
        rb = DictionaryResourceBundle(messages)
        lf = LocalizableMessageFactory(rb, StringFormatter)
        actual_result = lf.get_message('bogus', 'hello')
        expected_result = LocalizableMessage(
            default_message="Unknown message ID bogus requested with parameters hello",
            args=['bogus', 'hello'],
            id='vapi.message.unknown')
        self.assertEqual(expected_result, actual_result)

    def test_percent_char(self):
        messages = {
            'msg.percent': 'stateId=0%%200%%20405444635',
        }
        rb = DictionaryResourceBundle(messages)
        lf = LocalizableMessageFactory(rb, StringFormatter)
        actual_result = lf.get_message('msg.percent')
        expected_result = LocalizableMessage(
            id='msg.percent',
            args=[],
            default_message="stateId=0%%200%%20405444635"
        )
        self.assertEqual(expected_result, actual_result)

    def test_percent_char_2(self):
        messages = {
            'msg.percent': 'stateId=%%20%s%%20'
        }
        rb = DictionaryResourceBundle(messages)
        lf = LocalizableMessageFactory(rb, StringFormatter)
        actual_result = lf.get_message('msg.percent', 'hello')
        expected_result = LocalizableMessage(
            id='msg.percent',
            args=['hello'],
            default_message="stateId=%%20hello%%20"
        )
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main()
