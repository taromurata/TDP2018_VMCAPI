"""
Unit tests for log module
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import unittest

from six.moves import cStringIO

from vmware.vapi.lib.log import (
    get_client_wire_logger, get_provider_wire_logger, get_raw_request_logger)


class TestLogging(unittest.TestCase):

    def setUp(self):
        self.raw_request_logger = get_raw_request_logger()
        self.client_wire_logger = get_client_wire_logger()
        self.provider_wire_logger = get_provider_wire_logger()
        self.log_capture_string = cStringIO()
        self.ch = logging.StreamHandler(self.log_capture_string)
        self.ch.setLevel(logging.DEBUG)
        self.root_logger = logging.getLogger()
        self.root_logger.addHandler(self.ch)

    def tearDown(self):
        self.log_capture_string.close()
        self.root_logger.removeHandler(self.ch)

    def test_raw_request_disabled(self):
        log_str = 'Raw request should not appear in logs'
        self.raw_request_logger.debug(log_str)
        self.assertTrue(log_str not in self.log_capture_string.getvalue())

    def test_raw_request_enabled(self):
        # Enable raw request logger
        self.raw_request_logger.propagate = True
        # Test
        log_str = 'Raw request should appear in logs'
        self.raw_request_logger.debug(log_str)
        self.assertTrue(log_str in self.log_capture_string.getvalue())
        # Disable raw request logger
        self.raw_request_logger.propagate = False

    def test_client_wire_disabled(self):
        log_str = 'Client wire should not appear in logs'
        self.client_wire_logger.debug(log_str)
        self.assertTrue(log_str not in self.log_capture_string.getvalue())

    def test_client_wire_enabled(self):
        # Enable client wire logger
        self.client_wire_logger.propagate = True
        # Test
        log_str = 'Client wire should appear in logs'
        self.client_wire_logger.debug(log_str)
        self.assertTrue(log_str in self.log_capture_string.getvalue())
        # Disable client wire logger
        self.client_wire_logger.propagate = False

    def test_provider_wire_disabled(self):
        log_str = 'Provider wire should not appear in logs'
        self.provider_wire_logger.debug(log_str)
        self.assertTrue(log_str not in self.log_capture_string.getvalue())

    def test_provider_wire_enabled(self):
        # Enable provider wire logger
        self.provider_wire_logger.propagate = True
        # Test
        log_str = 'Provider wire should appear in logs'
        self.provider_wire_logger.debug(log_str)
        self.assertTrue(log_str in self.log_capture_string.getvalue())
        # Disable provider wire logger
        self.provider_wire_logger.propagate = False


if __name__ == "__main__":
    unittest.main()
