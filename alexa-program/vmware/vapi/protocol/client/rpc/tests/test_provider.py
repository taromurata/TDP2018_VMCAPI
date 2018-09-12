"""
Unit tests for core data structures
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import unittest

from vmware.vapi.protocol.client.rpc.provider import RpcProvider, HTTPProvider

class TestRpcProvider(unittest.TestCase):
    def test_abstract_rpc_provider(self):
        self.assertRaises(TypeError, RpcProvider)

class TestHTTPProvider(unittest.TestCase):
    def test_abstract_http_provider(self):
        self.assertRaises(TypeError, HTTPProvider)
