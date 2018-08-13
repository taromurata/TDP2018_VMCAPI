"""
Unit tests for SecurityContextFilter
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import os
import unittest
import logging

from six.moves import configparser

from vmware.vapi.core import (
    InterfaceIdentifier, MethodResult, MethodDefinition, MethodIdentifier,
    ApiProvider, SecurityContext, ExecutionContext, ProviderDefinition,
    ApplicationContext, InterfaceDefinition, ApiInterface)
from vmware.vapi.data.definition import (
    VoidDefinition, IntegerDefinition, StructDefinition)
from vmware.vapi.data.serializers.introspection import convert_data_def_to_data_value
from vmware.vapi.data.value import StructValue, StringValue, ListValue
from vmware.vapi.data.value import VoidValue, IntegerValue, OptionalValue
from vmware.vapi.lib.constants import SCHEME_ID
from vmware.vapi.lib.std import make_std_error_def
from vmware.vapi.security.client.security_context_filter import (
    LegacySecurityContextFilter, SecurityContextFilter)
from vmware.vapi.security.user_password import USER_PASSWORD_SCHEME_ID, USER_KEY, PASSWORD_KEY

errors = [
    'com.vmware.vapi.std.errors.internal_server_error',
    'com.vmware.vapi.std.errors.invalid_argument',
    'com.vmware.vapi.std.errors.operation_not_found',
    'com.vmware.vapi.std.errors.unauthenticated',
]
error_defs = [make_std_error_def(error) for error in errors]
error_values = [convert_data_def_to_data_value(error_def)
                for error_def in error_defs]
logging.basicConfig(level=logging.INFO)

class MockProvider(ApiProvider):
    def invoke(self, service_id, operation_id, input_value, ctx):
        # Allowed service_id: 'svc'
        if service_id != 'svc':
            return MethodResult(error=error_values[2])
        # Allowed operation_ids: 'op1', 'op2'
        if operation_id == 'op1':
            return MethodResult(output=IntegerValue(10))
        elif operation_id == 'op2':
            if ctx.security_context:
                return MethodResult(output=IntegerValue(20))
            else:
                return MethodResult(error=error_values[3])
        else:
            return MethodResult(error=error_values[2])

class TestSecurityContextFilter(unittest.TestCase):

    def setUp(self):
        self.sec_ctx_filter = LegacySecurityContextFilter(next_provider=MockProvider())

    def test_abstract_security_context_filter(self):
        self.assertRaises(TypeError, SecurityContextFilter)

    def test_authn_op_with_sec_ctx(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: USER_PASSWORD_SCHEME_ID,
             USER_KEY: 'testuser',
             PASSWORD_KEY: 'password'})
        ctx = ExecutionContext(None, sec_ctx)
        input_val = VoidValue()
        method_result = self.sec_ctx_filter.invoke(
            'svc', 'op2', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(20))
        self.assertEqual(method_result.error, None)

    def test_authn_op_with_sec_ctx_on_filter(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: USER_PASSWORD_SCHEME_ID,
             USER_KEY: 'testuser',
             PASSWORD_KEY: 'password'})
        self.sec_ctx_filter.set_security_context(sec_ctx)
        ctx = ExecutionContext(None, None)
        input_val = VoidValue()
        method_result = self.sec_ctx_filter.invoke(
            'svc', 'op2', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(20))
        self.assertEqual(method_result.error, None)

    def test_authn_op_without_sec_ctx(self):
        ctx = ExecutionContext(None, None)
        input_val = VoidValue()
        method_result = self.sec_ctx_filter.invoke(
            'svc', 'op2', input_val, ctx)
        self.assertEqual(method_result.output, None)
        self.assertEqual(method_result.error, error_values[3])

    def test_op_with_sec_ctx_on_filter(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: USER_PASSWORD_SCHEME_ID,
             USER_KEY: 'testuser',
             PASSWORD_KEY: 'password'})
        self.sec_ctx_filter.set_security_context(sec_ctx)
        ctx = ExecutionContext(ApplicationContext(), None)
        input_val = VoidValue()
        method_result = self.sec_ctx_filter.invoke(
            'svc', 'op1', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(10))
        self.assertEqual(method_result.error, None)

    def test_op(self):
        ctx = ExecutionContext(ApplicationContext(), None)
        input_val = VoidValue()
        method_result = self.sec_ctx_filter.invoke(
            'svc', 'op1', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(10))
        self.assertEqual(method_result.error, None)


if __name__ == '__main__':
    unittest.main()
