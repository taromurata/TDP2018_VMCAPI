"""
Unit tests for Property parser
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import os

from vmware.vapi.lib.converter import Converter


class TestPropertyParser(unittest.TestCase):

    def test_capitalize(self):
        self.assertEqual(Converter.capitalize('abc'), 'Abc')

    def test_uncapitalize(self):
        self.assertEqual(Converter.uncapitalize('Abc'), 'abc')

    def test_capwords_to_underscore(self):
        self.assertEqual(Converter.mixedcase_to_underscore('CapWords'),
                         'cap_words')
        self.assertEqual(Converter.mixedcase_to_underscore('cap_words'),
                         'cap_words')

    def test_mixedcase_to_underscore(self):
        self.assertEqual(Converter.mixedcase_to_underscore('mixedCase'),
                         'mixed_case')
        self.assertEqual(Converter.mixedcase_to_underscore('mixed_case'),
                         'mixed_case')

    def test_underscore_to_mixedcase(self):
        self.assertEqual(Converter.underscore_to_mixedcase('mixed_case'),
                         'mixedCase')
        self.assertEqual(Converter.underscore_to_mixedcase('mixedCase'),
                         'mixedCase')

    def test_underscore_to_capwords(self):
        self.assertEqual(Converter.underscore_to_capwords('cap_words'),
                         'CapWords')
        self.assertEqual(Converter.underscore_to_capwords('CapWords'),
                         'CapWords')

    def test_pepify(self):
        self.assertEqual(Converter.pepify('class'), 'class_')
