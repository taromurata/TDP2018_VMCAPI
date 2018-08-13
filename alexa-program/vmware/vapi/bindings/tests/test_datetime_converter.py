#!/usr/bin/env python

"""
Unit tests for DataValue <-> Python native value (de)serialization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import datetime
import logging
import unittest

from vmware.vapi.bindings.datetime_helper import convert_to_utc
from vmware.vapi.bindings.type import DateTimeType
from vmware.vapi.data.value import StringValue
from vmware.vapi.bindings.converter import TypeConverter, RestConverter
from vmware.vapi.exception import CoreException


class GMT1(datetime.tzinfo):
    """
    GMT1 timezone
    """
    def utcoffset(self, dt):
        return datetime.timedelta(hours=1) + self.dst(dt)

    def dst(self, dt):
        # DST starts last Sunday in March
        d = datetime.datetime(dt.year, 4, 1)   # ends last Sunday in October
        self.dston = d - datetime.timedelta(days=d.weekday() + 1)
        d = datetime.datetime(dt.year, 11, 1)
        self.dstoff = d - datetime.timedelta(days=d.weekday() + 1)
        if self.dston <=  dt.replace(tzinfo=None) < self.dstoff:
            return datetime.timedelta(hours=1)
        else:
            return datetime.timedelta(0)

    def tzname(self,dt):
         return "GMT +1"


class UTC(datetime.tzinfo):
    """
    tzinfo class for UTC timezone
    """
    def utcoffset(self, dt):
        return datetime.timedelta(0)

    def tzname(self, dt):
        return 'UTC'

    def dst(self, dt):
        return datetime.timedelta(0)

class GenericTZInfo(datetime.tzinfo):
    def __init__(self, td):
        self.td = td

    def utcoffset(self, dt):
        return self.td

    def dst(self, dt):
        return self.td

class TestDateTimeBindingTypeConverter(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.typ = DateTimeType()

    def test_basic(self):
        dt = datetime.datetime.utcnow()

        string_val = TypeConverter.convert_to_vapi(dt, self.typ)
        self.assertTrue(isinstance(string_val, StringValue))

        dt_new = TypeConverter.convert_to_python(string_val, self.typ)
        self.assertTrue(isinstance(dt_new, datetime.datetime))
        self.assertEqual(dt.year, dt_new.year)
        self.assertEqual(dt.month, dt_new.month)
        self.assertEqual(dt.day, dt_new.day)
        self.assertEqual(dt.hour, dt_new.hour)
        self.assertEqual(dt.minute, dt_new.minute)
        self.assertEqual(dt.second, dt_new.second)

        string_val_new = TypeConverter.convert_to_vapi(dt_new, self.typ)
        self.assertEqual(string_val, string_val_new)

    def _convert(self, dt, dt_str):
        dt_str = StringValue(dt_str)
        self.assertEqual(TypeConverter.convert_to_vapi(dt, self.typ),
                         dt_str)
        self.assertEqual(TypeConverter.convert_to_python(dt_str, self.typ),
                         dt)

    def test_min(self):
        dt = datetime.datetime(year=1, month=1, day=1)
        dt_str = '0001-01-01T00:00:00.000Z'
        self._convert(dt, dt_str)

    def test_max(self):
        dt = datetime.datetime(year=9999, month=12, day=31, hour=23,
                      minute=59, second=59, microsecond=999000)
        dt_str = '9999-12-31T23:59:59.999Z'
        self._convert(dt, dt_str)

    def test_fractional_seconds(self):
        dt = datetime.datetime(year=1878, month=3, day=4, hour=5,
                      minute=6, second=7, microsecond=000)
        dt_str = '1878-03-04T05:06:07.000Z'
        self._convert(dt, dt_str)

        dt = datetime.datetime(year=1878, month=3, day=4, hour=5,
                      minute=6, second=7, microsecond=1000)
        dt_str = '1878-03-04T05:06:07.001Z'
        self._convert(dt, dt_str)

        dt = datetime.datetime(year=1878, month=3, day=4, hour=5,
                      minute=6, second=7, microsecond=10000)
        dt_str = '1878-03-04T05:06:07.010Z'
        self._convert(dt, dt_str)

        dt = datetime.datetime(year=1878, month=3, day=4, hour=5,
                      minute=6, second=7, microsecond=100000)
        dt_str = '1878-03-04T05:06:07.100Z'
        self._convert(dt, dt_str)

    def test_tz(self):
        class TZ(datetime.tzinfo):
            def utcoffset(self, dt): return datetime.timedelta(minutes=-30)
        dt = datetime.datetime(1,1,1, tzinfo=TZ())
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          dt, self.typ)

    def test_utc_time_conversion(self):
        dt1 = datetime.datetime(2006, 11, 21, 16, 30, tzinfo=GMT1())
        utc_dt = convert_to_utc(dt1)
        self.assertEqual(TypeConverter.convert_to_vapi(utc_dt, self.typ),
                         StringValue('2006-11-21T15:30:00.000Z'))

    def _parse_fail(self, dt_str):
        dt_str = StringValue(dt_str)
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_python,
                          dt_str, self.typ)

    def test_invalid_datetime_str(self):
        # extra character at the end
        self._parse_fail("1878-03-04T05:06:07.000ZZ")

        # missing '-' between year and month
        self._parse_fail("187803-04T05:06:07.000Z")

        # missing '-' between month and day
        self._parse_fail("1878-0304T05:06:07.000Z")

        # missing 'T' between day and hour
        self._parse_fail("1878-03-0405:06:07.000Z")

        # missing ':' between hour and minute
        self._parse_fail("1878-03-04T0506:07.000Z")

        # missing ':' between minute and second
        self._parse_fail("1878-03-04T05:0607.000Z")

        # illegal symbol 'x' in various positions
        self._parse_fail("x1878-03-04T05:06:07.000Z")
        self._parse_fail("1878x-03-04T05:06:07.000Z")
        self._parse_fail("1878-x03-04T05:06:07.000Z")
        self._parse_fail("1878-03x-04T05:06:07.000Z")
        self._parse_fail("1878-03-x04T05:06:07.000Z")
        self._parse_fail("1878-03-04xT05:06:07.000Z")
        self._parse_fail("1878-03-04Tx05:06:07.000Z")
        self._parse_fail("1878-03-04T05x:06:07.000Z")
        self._parse_fail("1878-03-04T05:x06:07.000Z")
        self._parse_fail("1878-03-04T05:06x:07.000Z")
        self._parse_fail("1878-03-04T05:06:x07.000Z")
        self._parse_fail("1878-03-04T05:06:07x.000Z")
        self._parse_fail("1878-03-04T05:06:07.x000Z")
        self._parse_fail("1878-03-04T05:06:07.000xZ")
        self._parse_fail("1878-03-04T05:06:07.000Zx")

    def test_invalid_timezone(self):
        # no timezone
        self._parse_fail("1878-03-04T05:06:07.000")

        # non UTC timezone
        self._parse_fail("1878-03-04T05:06:07+05:00")
        self._parse_fail("1878-03-04T05:06:07-11:00")

        # +00:00 and -00:00 are not allowed as UTC representations
        self._parse_fail("1878-03-04T05:06:07+00:00")
        self._parse_fail("1878-03-04T05:06:07-00:00")

    def test_invalid_year(self):
        # year not a number
        self._parse_fail("187a-03-04T05:06:07.000Z")
        self._parse_fail("18aa-03-04T05:06:07.000Z")
        self._parse_fail("1aaa-03-04T05:06:07.000Z")
        self._parse_fail("aaaa-03-04T05:06:07.000Z")

        # years BC : 0000 = 1 BC, -0001 = 2 BC
        self._parse_fail("0000-03-04T05:06:07.000Z")
        self._parse_fail("-0000-03-04T05:06:07.000Z")
        self._parse_fail("+0000-03-04T05:06:07.000Z")
        self._parse_fail("-0001-03-04T05:06:07.000Z")

        # less than 4 digits for year
        self._parse_fail("188-03-04T05:06:07.000Z")
        self._parse_fail("18-03-04T05:06:07.000Z")
        self._parse_fail("1-03-04T05:06:07.000Z")
        self._parse_fail("-03-04T05:06:07.000Z")

        # more than 4 digits for year
        self._parse_fail("11878-03-04T05:06:07.000Z")
        self._parse_fail("111878-03-04T05:06:07.000Z")
        self._parse_fail("999999999999999999999999991878-03-04T05:06:07.000Z")
        self._parse_fail("187899999999999999999999999999-03-04T05:06:07.000Z")

        # In ISO 8601 more than 4 digit years use an "expanded representation"
        # and have '+' in the beginning. But they are forbidden in the DateTime
        # format.
        self._parse_fail("+11878-03-04T05:06:07.000Z")
        self._parse_fail("+111878-03-04T05:06:07.000Z")

    def test_invalid_month(self):
        # 31 February
        self._parse_fail("1878-02-31T05:06:07.000Z")

        # 31 April
        self._parse_fail("1878-04-31T05:06:07.000Z")

        # less than 2 digits for month
        self._parse_fail("1878-3-04T05:06:07.000Z")
        self._parse_fail("1878--04T05:06:07.000Z")

        # more than 2 digits for month
        self._parse_fail("1878-003-04T05:06:07.000Z")
        self._parse_fail("1878-9999999999999999999999999903-04T05:06:07.000Z")
        self._parse_fail("1878-0399999999999999999999999999-04T05:06:07.000Z")

        # month number out of range
        self._parse_fail("1878-00-04T05:06:07.000Z")
        self._parse_fail("1878-13-04T05:06:07.000Z")
        self._parse_fail("1878-14-04T05:06:07.000Z")
        self._parse_fail("1878-99-04T05:06:07.000Z")

        # month not a number
        self._parse_fail("1878-0a-04T05:06:07.000Z")
        self._parse_fail("1878-aa-04T05:06:07.000Z")

    def test_invalid_day(self):
        # less than 2 digits for day
        self._parse_fail("1878-03-4T05:06:07.000Z")
        self._parse_fail("1878-03-T05:06:07.000Z")

        # more than 2 digits for day
        self._parse_fail("1878-03-004T05:06:07.000Z")
        self._parse_fail("1878-03-9999999999999999999999999904T05:06:07.000Z")
        self._parse_fail("1878-03-0499999999999999999999999999T05:06:07.000Z")

        # day number out of range
        self._parse_fail("1878-03-00T05:06:07.000Z")
        self._parse_fail("1878-03-32T05:06:07.000Z")
        self._parse_fail("1878-03-99T05:06:07.000Z")

        # day not a number
        self._parse_fail("1878-03-0aT05:06:07.000Z")
        self._parse_fail("1878-03-aaT05:06:07.000Z")

    def test_invalid_hour(self):
        # less than 2 digits for hour
        self._parse_fail("1878-03-04T5:06:07.000Z")
        self._parse_fail("1878-03-04T:06:07.000Z")

        # more than 2 digits for hour
        self._parse_fail("1878-03-04T005:06:07.000Z")
        self._parse_fail("1878-03-04T9999999999999999999999999905:06:07.000Z")
        self._parse_fail("1878-03-04T0599999999999999999999999999:06:07.000Z")

        # hour number out of range
        self._parse_fail("1878-03-04T24:06:07.000Z")
        self._parse_fail("1878-03-04T25:06:07.000Z")
        self._parse_fail("1878-03-04T99:06:07.000Z")

        # hour not a number
        self._parse_fail("1878-03-04T0a:06:07.000Z")
        self._parse_fail("1878-03-04Taa:06:07.000Z")

    def test_invalid_minutes(self):
        # less than 2 digits for minutes
        self._parse_fail("1878-03-04T05:6:07.000Z")
        self._parse_fail("1878-03-04T05::07.000Z")

        # more than 2 digits for minutes
        self._parse_fail("1878-03-04T05:006:07.000Z")
        self._parse_fail("1878-03-04T05:9999999999999999999999999906:07.000Z")
        self._parse_fail("1878-03-04T05:0699999999999999999999999999:07.000Z")

        # minutes number out of range
        self._parse_fail("1878-03-04T05:60:07.000Z")
        self._parse_fail("1878-03-04T05:61:07.000Z")
        self._parse_fail("1878-03-04T05:99:07.000Z")

        # minutes not a number
        self._parse_fail("1878-03-04T05:0a:07.000Z")
        self._parse_fail("1878-03-04T05:aa:07.000Z")

    def test_invalid_seconds(self):
        # less than 2 digits for seconds
        self._parse_fail("1878-03-04T05:06:7.000Z")
        self._parse_fail("1878-03-04T05:06:.000Z")

        # more than 2 digits for seconds
        self._parse_fail("1878-03-04T05:06:007.000Z")
        self._parse_fail("1878-03-04T05:06:9999999999999999999999999907.000Z")
        self._parse_fail("1878-03-04T05:06:0799999999999999999999999999.000Z")

        # seconds number out of range
        self._parse_fail("1878-03-04T05:06:60.000Z")
        self._parse_fail("1878-03-04T05:06:61.000Z")
        self._parse_fail("1878-03-04T05:06:99.000Z")

        # seconds not a number
        self._parse_fail("1878-03-04T05:06:0a.000Z")
        self._parse_fail("1878-03-04T05:06:aa.000Z")

    def test_invalid_microseconds(self):
        # less than 3 digits for fractional seconds
        self._parse_fail("1878-03-04T05:06:07.00Z")
        self._parse_fail("1878-03-04T05:06:07.0Z")
        self._parse_fail("1878-03-04T05:06:07.Z")
        self._parse_fail("1878-03-04T05:06:07Z")

        # more than 3 digits for fractional seconds
        self._parse_fail("1878-03-04T05:06:07.0000Z")
        self._parse_fail("1878-03-04T05:06:07.0001Z")
        self._parse_fail("1878-03-04T05:06:07.99999999999999999999999999999Z")

        # fractional seconds not a number
        self._parse_fail("1878-03-04T05:06:07.00aZ")
        self._parse_fail("1878-03-04T05:06:07.0a0Z")
        self._parse_fail("1878-03-04T05:06:07.a00Z")


class TestRFC3339DateTimeBindingTypeConverter(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.typ = DateTimeType()

    def _convert(self, dt, dt_str):
        dt_str = StringValue(dt_str)
        self.assertEqual(
            TypeConverter.convert_to_vapi(
                dt, self.typ, rest_converter_mode=RestConverter.SWAGGER_REST),
            dt_str)
        self.assertEqual(
            TypeConverter.convert_to_python(
                dt_str, self.typ,
                rest_converter_mode=RestConverter.SWAGGER_REST),
            dt)

    def _parse_fail(self, dt_str):
        dt_str = StringValue(dt_str)
        self.assertRaises(
            CoreException, TypeConverter.convert_to_python, dt_str, self.typ,
            rest_converter_mode=RestConverter.SWAGGER_REST)

    def test_invalid_datetime_str(self):
        # extra character at the end
        self._parse_fail("1878-03-04T05:06:07.000ZZ")

        # missing '-' between year and month
        self._parse_fail("187803-04T05:06:07.000Z")

        # missing '-' between month and day
        self._parse_fail("1878-0304T05:06:07.000Z")

        # missing 'T' between day and hour
        self._parse_fail("1878-03-0405:06:07.000Z")

        # missing ':' between hour and minute
        self._parse_fail("1878-03-04T0506:07.000Z")

        # missing ':' between minute and second
        self._parse_fail("1878-03-04T05:0607.000Z")

        # illegal symbol 'x' in various positions
        self._parse_fail("x1878-03-04T05:06:07.000Z")
        self._parse_fail("1878x-03-04T05:06:07.000Z")
        self._parse_fail("1878-x03-04T05:06:07.000Z")
        self._parse_fail("1878-03x-04T05:06:07.000Z")
        self._parse_fail("1878-03-x04T05:06:07.000Z")
        self._parse_fail("1878-03-04xT05:06:07.000Z")
        self._parse_fail("1878-03-04Tx05:06:07.000Z")
        self._parse_fail("1878-03-04T05x:06:07.000Z")
        self._parse_fail("1878-03-04T05:x06:07.000Z")
        self._parse_fail("1878-03-04T05:06x:07.000Z")
        self._parse_fail("1878-03-04T05:06:x07.000Z")
        self._parse_fail("1878-03-04T05:06:07x.000Z")
        self._parse_fail("1878-03-04T05:06:07.x000Z")
        self._parse_fail("1878-03-04T05:06:07.000xZ")
        self._parse_fail("1878-03-04T05:06:07.000Zx")

    def test_invalid_timezone(self):
        # no timezone
        self._parse_fail("1878-03-04T05:06:07.000")

    def test_invalid_year(self):
        # year not a number
        self._parse_fail("187a-03-04T05:06:07.000Z")
        self._parse_fail("18aa-03-04T05:06:07.000Z")
        self._parse_fail("1aaa-03-04T05:06:07.000Z")
        self._parse_fail("aaaa-03-04T05:06:07.000Z")

        # years BC : 0000 = 1 BC, -0001 = 2 BC
        self._parse_fail("0000-03-04T05:06:07.000Z")
        self._parse_fail("-0000-03-04T05:06:07.000Z")
        self._parse_fail("+0000-03-04T05:06:07.000Z")
        self._parse_fail("-0001-03-04T05:06:07.000Z")

        # less than 4 digits for year
        self._parse_fail("188-03-04T05:06:07.000Z")
        self._parse_fail("18-03-04T05:06:07.000Z")
        self._parse_fail("1-03-04T05:06:07.000Z")
        self._parse_fail("-03-04T05:06:07.000Z")

        # more than 4 digits for year
        self._parse_fail("11878-03-04T05:06:07.000Z")
        self._parse_fail("111878-03-04T05:06:07.000Z")
        self._parse_fail("999999999999999999999999991878-03-04T05:06:07.000Z")
        self._parse_fail("187899999999999999999999999999-03-04T05:06:07.000Z")

        # In ISO 8601 more than 4 digit years use an "expanded representation"
        # and have '+' in the beginning. But they are forbidden in the DateTime
        # format.
        self._parse_fail("+11878-03-04T05:06:07.000Z")
        self._parse_fail("+111878-03-04T05:06:07.000Z")

    def test_invalid_month(self):
        # 31 February
        self._parse_fail("1878-02-31T05:06:07.000Z")

        # 31 April
        self._parse_fail("1878-04-31T05:06:07.000Z")

        # less than 2 digits for month
        self._parse_fail("1878-3-04T05:06:07.000Z")
        self._parse_fail("1878--04T05:06:07.000Z")

        # more than 2 digits for month
        self._parse_fail("1878-003-04T05:06:07.000Z")
        self._parse_fail("1878-9999999999999999999999999903-04T05:06:07.000Z")
        self._parse_fail("1878-0399999999999999999999999999-04T05:06:07.000Z")

        # month number out of range
        self._parse_fail("1878-00-04T05:06:07.000Z")
        self._parse_fail("1878-13-04T05:06:07.000Z")
        self._parse_fail("1878-14-04T05:06:07.000Z")
        self._parse_fail("1878-99-04T05:06:07.000Z")

        # month not a number
        self._parse_fail("1878-0a-04T05:06:07.000Z")
        self._parse_fail("1878-aa-04T05:06:07.000Z")

    def test_invalid_day(self):
        # less than 2 digits for day
        self._parse_fail("1878-03-4T05:06:07.000Z")
        self._parse_fail("1878-03-T05:06:07.000Z")

        # more than 2 digits for day
        self._parse_fail("1878-03-004T05:06:07.000Z")
        self._parse_fail("1878-03-9999999999999999999999999904T05:06:07.000Z")
        self._parse_fail("1878-03-0499999999999999999999999999T05:06:07.000Z")

        # day number out of range
        self._parse_fail("1878-03-00T05:06:07.000Z")
        self._parse_fail("1878-03-32T05:06:07.000Z")
        self._parse_fail("1878-03-99T05:06:07.000Z")

        # day not a number
        self._parse_fail("1878-03-0aT05:06:07.000Z")
        self._parse_fail("1878-03-aaT05:06:07.000Z")

    def test_invalid_hour(self):
        # less than 2 digits for hour
        self._parse_fail("1878-03-04T5:06:07.000Z")
        self._parse_fail("1878-03-04T:06:07.000Z")

        # more than 2 digits for hour
        self._parse_fail("1878-03-04T005:06:07.000Z")
        self._parse_fail("1878-03-04T0599999999999999999999999999:06:07.000Z")

        # hour number out of range
        self._parse_fail("1878-03-04T24:06:07.000Z")
        self._parse_fail("1878-03-04T25:06:07.000Z")
        self._parse_fail("1878-03-04T99:06:07.000Z")

        # hour not a number
        self._parse_fail("1878-03-04T0a:06:07.000Z")
        self._parse_fail("1878-03-04Taa:06:07.000Z")

    def test_invalid_minutes(self):
        # less than 2 digits for minutes
        self._parse_fail("1878-03-04T05:6:07.000Z")
        self._parse_fail("1878-03-04T05::07.000Z")

        # more than 2 digits for minutes
        self._parse_fail("1878-03-04T05:006:07.000Z")
        self._parse_fail("1878-03-04T05:9999999999999999999999999906:07.000Z")
        self._parse_fail("1878-03-04T05:0699999999999999999999999999:07.000Z")

        # minutes number out of range
        self._parse_fail("1878-03-04T05:60:07.000Z")
        self._parse_fail("1878-03-04T05:61:07.000Z")
        self._parse_fail("1878-03-04T05:99:07.000Z")

        # minutes not a number
        self._parse_fail("1878-03-04T05:0a:07.000Z")
        self._parse_fail("1878-03-04T05:aa:07.000Z")

    def test_invalid_seconds(self):
        # less than 2 digits for seconds
        self._parse_fail("1878-03-04T05:06:7.000Z")
        self._parse_fail("1878-03-04T05:06:.000Z")

        # more than 2 digits for seconds
        self._parse_fail("1878-03-04T05:06:007.000Z")
        self._parse_fail("1878-03-04T05:06:9999999999999999999999999907.000Z")
        self._parse_fail("1878-03-04T05:06:0799999999999999999999999999.000Z")

        # seconds number out of range
        self._parse_fail("1878-03-04T05:06:60.000Z")
        self._parse_fail("1878-03-04T05:06:61.000Z")
        self._parse_fail("1878-03-04T05:06:99.000Z")

        # seconds not a number
        self._parse_fail("1878-03-04T05:06:0a.000Z")
        self._parse_fail("1878-03-04T05:06:aa.000Z")

    def test_invalid_microseconds(self):
        # fractional seconds not a number
        self._parse_fail("1878-03-04T05:06:07.00aZ")
        self._parse_fail("1878-03-04T05:06:07.0a0Z")
        self._parse_fail("1878-03-04T05:06:07.a00Z")

    def _verify_correct(self, dt_str, dt):
        dt_str = StringValue(dt_str)
        self.assertEqual(
        TypeConverter.convert_to_python(
            dt_str, self.typ, rest_converter_mode=RestConverter.SWAGGER_REST),
        dt)

    def test_valid_timezones(self):
        self._verify_correct(
            '1878-03-04T05:06:07+01:01',
            datetime.datetime(
                year=1878, month=3, day=4, hour=5, minute=6, second=7,
                tzinfo=GenericTZInfo(datetime.timedelta(hours=1, minutes=1))).astimezone(UTC()))
        self._verify_correct(
            '1878-03-04T05:06:07-01:01',
            datetime.datetime(
                year=1878, month=3, day=4, hour=5, minute=6, second=7,
                tzinfo=GenericTZInfo(-datetime.timedelta(hours=1, minutes=1))).astimezone(UTC()))

    def test_valid_microseconds(self):
        # fractional seconds not a number
        self._verify_correct(
            '1878-03-04T05:06:07.123456Z',
            datetime.datetime(
                year=1878, month=3, day=4, hour=5, minute=6, second=7,
                microsecond=123456))
        self._verify_correct(
            '1878-03-04T05:06:07.123456789Z',
            datetime.datetime(
                year=1878, month=3, day=4, hour=5, minute=6, second=7,
                microsecond=123456))

if __name__ == '__main__':
   unittest.main()
