"""
Unit tests for l10n formatter
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import locale
import unittest

from vmware.vapi.bindings.datetime_helper import DateTimeConverter
from vmware.vapi.l10n.formatter import StringFormatter
from vmware.vapi.l10n.constants import DEFAULT_LOCALE

class TestFormatter(unittest.TestCase):
    def setUp(self):
        locale.setlocale(locale.LC_ALL, DEFAULT_LOCALE)

    def test_simple(self):
        actual_result = StringFormatter.format_msg('very first message',
                                                   [])
        self.assertEqual('very first message', actual_result)

    def test_string(self):
        actual_result = StringFormatter.format_msg('some string %s',
                                                   ['foo'])
        self.assertEqual('some string foo', actual_result)

    def test_long(self):
        actual_result = StringFormatter.format_msg('some long %d',
                                                   [123456])
        self.assertEqual('some long 123456', actual_result)

    def test_long_with_grouping(self):
        actual_result = StringFormatter.format_msg('some long %,d',
                                                   [123456])
        self.assertEqual('some long 123,456', actual_result)

    def test_double(self):
        actual_result = StringFormatter.format_msg('some double %f',
                                                   [123])
        self.assertEqual('some double 123.000000', actual_result)

        actual_result = StringFormatter.format_msg('some double %f',
                                                   [123.456])
        self.assertEqual('some double 123.456000', actual_result)

        actual_result = StringFormatter.format_msg('some double %.3f',
                                                   [123])
        self.assertEqual('some double 123.000', actual_result)

        actual_result = StringFormatter.format_msg('some double %.3f',
                                                   [123.45])
        self.assertEqual('some double 123.450', actual_result)

        actual_result = StringFormatter.format_msg('some double %.3f',
                                                   [123.4567])
        self.assertEqual('some double 123.457', actual_result)

        actual_result = StringFormatter.format_msg('some double %.3f',
                                                   [123456.789])
        self.assertEqual('some double 123456.789', actual_result)

    def test_double_with_grouping(self):
        actual_result = StringFormatter.format_msg('some double %,.3f',
                                                   [123456.789])
        self.assertEqual('some double 123,456.789', actual_result)

    def test_datetime(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        actual_result = StringFormatter.format_msg('some date %tc',
                                                   [dt])
        self.assertEqual('some date Sat 04 Mar 1978 05:06:07 AM', actual_result)

    def test_multiple_args(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        actual_result = StringFormatter.format_msg(
            'long %d, float %.3f, date %tc',
            [123456, 123456.789, dt])
        self.assertEqual(
            'long 123456, float 123456.789, date Sat 04 Mar 1978 05:06:07 AM',
            actual_result)

    def test_multiple_args_with_grouping(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        actual_result = StringFormatter.format_msg(
            'long %,d, float %,.3f, date %tc',
            [123456, 123456.789, dt])
        self.assertEqual(
            'long 123,456, float 123,456.789, date Sat 04 Mar 1978 05:06:07 AM',
            actual_result)

    def test_reorder_args_1(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        actual_result = StringFormatter.format_msg(
            'long %1$d, float %2$.3f, date %3$tc',
            [123456, 123456.789, dt])
        self.assertEqual(
            'long 123456, float 123456.789, date Sat 04 Mar 1978 05:06:07 AM',
            actual_result)

    def test_reorder_args_2(self):
        datetime_msg = '1978-03-04T05:06:07.100Z'
        dt = DateTimeConverter.convert_to_datetime(datetime_msg)
        actual_result = StringFormatter.format_msg(
            'long %3$d, float %2$.3f, date %1$tc',
            [dt, 123456.789, 123456])
        self.assertEqual(
            'long 123456, float 123456.789, date Sat 04 Mar 1978 05:06:07 AM',
            actual_result)


if __name__ == "__main__":
    unittest.main()
