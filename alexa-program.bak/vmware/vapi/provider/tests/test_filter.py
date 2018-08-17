"""
Unit tests for Api Provider Filter
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import unittest

from vmware.vapi.provider.local import LocalProvider
from vmware.vapi.provider.filter import ApiProviderFilter

logging.basicConfig(level=logging.DEBUG)

class Filter1(ApiProviderFilter):
    def invoke(self, service_id, operation_id, input_value, ctx):
        return ApiProviderFilter.invoke(self, service_id, operation_id, input_value, ctx)

class Filter2(Filter1):
    pass

class TestApiProviderFilter(unittest.TestCase):
    def setUp(self):
        self.filter = Filter1(
            next_provider=Filter2(
                next_provider=LocalProvider()))

    def test_find_first_api_filter(self):
        self.assertIsInstance(
            self.filter.find_first_api_filter(Filter1.__name__), Filter1)
        self.assertIsInstance(
            self.filter.find_first_api_filter(Filter2.__name__), Filter2)

    def test_find_first_api_filter_invalid(self):
        self.assertIsNone(self.filter.find_first_api_filter('bogus'))

    def test_get_api_provider(self):
        self.assertIsInstance(
            self.filter.get_api_provider(), LocalProvider)

    def test_get_api_provider_invalid(self):
        filter_only = Filter1()
        self.assertIsNone(filter_only.get_api_provider())

if __name__ == "__main__":
   unittest.main()
