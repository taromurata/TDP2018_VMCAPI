#!/usr/bin/env python

"""
Unit tests for DataValue <-> Python native value (de)serialization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import logging
import unicodedata

from vmware.vapi.bindings.type import URIType
from vmware.vapi.data.value import StringValue
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.exception import CoreException

class TestURIBindingType(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)
        self.typ = URIType()

    def _convert(self, uri_string):
        self.assertEqual(TypeConverter.convert_to_vapi(uri_string, self.typ),
                         StringValue(uri_string))
        self.assertEqual(
            TypeConverter.convert_to_python(StringValue(uri_string), self.typ),
            uri_string)

    def test_uri(self):
        self._convert('../../a.txt')
        self._convert('http://jsmith@www.example.com')
        self._convert('urn:uuid:6e8bc430-9c3a-11d9-9669-0800200c9a66')
        self._convert('http://[::FFFF:129.144.52.38]:80/index.html')
        self._convert('http://www.example.com')
        # percent encoded ascii
        self._convert('http://www.example.co%6D')
        self._convert('http://www.example.co%6d')
        # percent encoded space
        self._convert('http://www.example.com/small%20big')
        # percent encoded non ascii
        self._convert('http://%D1%82%D0%B5%D1%81%D1%82')
        #IPv6 address
        self._convert('http://[fc00:10:23:68::107]:55555/vapi')

    def test_iri(self):
        cyrillic_letter = unicodedata.lookup('CYRILLIC CAPITAL LETTER KA')
        self._convert('urn:' + cyrillic_letter)

    def _convert_fail(self, uri_string):
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          uri_string, self.typ)
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_python,
                          StringValue(uri_string), self.typ)

    def test_uri_fail(self):
        # bad percent encoding
        self._convert_fail('http://%???')

        # Character outside BMP place
        # OLD ITALIC LETTER A is U+10300 which is in Unicode Plane 1
        old_italic_letter = unicodedata.lookup('OLD ITALIC LETTER A')
        self._convert_fail('urn:' + old_italic_letter)

        # IPv6 missing closing bracket
        self._convert_fail('http://[FEDC:BA98:7654:3210:FEDC:BA98:7654:3210')

        # IPv6 illegal symbol
        self._convert_fail('http://[::FFFF:129.144.52.38???]')


if __name__ == '__main__':
   unittest.main()
