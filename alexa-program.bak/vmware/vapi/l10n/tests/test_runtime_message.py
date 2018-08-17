"""
Unit tests for l10n runtime
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import unittest

from vmware.vapi.l10n.runtime import message_factory
from vmware.vapi.message import Message

class TestFormatter(unittest.TestCase):
    def test_message(self):
        actual_result = message_factory.get_message('vapi.connection', 'svc')
        expected_result = Message('vapi.connection',
                                  'Could not connect to svc',
                                  'svc')
        self.assertEqual(expected_result, actual_result)

    def test_unknown_message(self):
        actual_result = message_factory.get_message('bogus', 'hello')
        expected_result = Message('vapi.message.unknown',
                                  "Unknown message ID bogus requested with parameters ('hello',)",
                                  )
        self.assertEqual(expected_result, actual_result)
