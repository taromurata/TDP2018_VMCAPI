"""
Unit tests for core data structures
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import unittest

from vmware.vapi.core import (
    ApiProvider, MethodIdentifier, InterfaceIdentifier, MethodDefinition)
from vmware.vapi.data.definition import (
    ErrorDefinition,
    StructDefinition,
    VoidDefinition,
    )

class TestMethodDefinition(unittest.TestCase):
    def setUp(self):
        self.ERROR1_NAME = 'error1'
        self.ERROR2_NAME = 'error2'
        self.ERROR3_NAME = 'error3'
        self.BOGUS_ERROR_NAME = "bogus_error_name"

        self.error_def1 = ErrorDefinition(self.ERROR1_NAME, [])
        self.error_def2 = ErrorDefinition(self.ERROR2_NAME, [])
        self.error_def3 = ErrorDefinition(self.ERROR3_NAME, [])

    def test_get_error_definition(self):
        method_def = MethodDefinition(
            MethodIdentifier(InterfaceIdentifier('interface'), 'method1'),
            StructDefinition('method1_input', []),
            VoidDefinition(),
            [self.error_def1, self.error_def2, self.error_def3])

        self.assertEquals(self.error_def1,
                          method_def.get_error_definition(self.ERROR1_NAME))
        self.assertEquals(self.error_def2,
                          method_def.get_error_definition(self.ERROR2_NAME))
        self.assertEquals(self.error_def3,
                          method_def.get_error_definition(self.ERROR3_NAME))
        self.assertEquals(
            None, method_def.get_error_definition(self.BOGUS_ERROR_NAME))

class TestApiProvider(unittest.TestCase):
    def test_api_provider_abstract(self):
        self.assertRaises(TypeError, ApiProvider)
