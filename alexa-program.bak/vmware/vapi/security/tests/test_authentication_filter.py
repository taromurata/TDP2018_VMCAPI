"""
Unit tests for Authentication Filter
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

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
from vmware.vapi.data.value import StructValue, StringValue, ListValue
from vmware.vapi.lib.std import make_std_error_def
from vmware.vapi.lib.constants import OPERATION_INPUT
from vmware.vapi.data.value import VoidValue, IntegerValue, OptionalValue
from vmware.vapi.security.authentication_handler import AuthenticationHandler
from vmware.vapi.security.authentication_filter import AuthenticationFilter
from vmware.vapi.data.serializers.introspection import convert_data_def_to_data_value
from vmware.vapi.security.user_password import USER_PASSWORD_SCHEME_ID, USER_KEY, PASSWORD_KEY
from vmware.vapi.security.oauth import OAUTH_SCHEME_ID, ACCESS_TOKEN
from vmware.vapi.security.session import SESSION_SCHEME_ID, SESSION_ID
from vmware.vapi.security.sso import SAML_SCHEME_ID, SAML_BEARER_SCHEME_ID, SAML_TOKEN, PRIVATE_KEY
from vmware.vapi.security.user_identity import UserIdentity
from vmware.vapi.lib.constants import SCHEME_ID
from vmware.vapi.settings.config import ProviderConfig
from vmware.vapi.provider.local import LocalProvider

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')

mock_interface_id = InterfaceIdentifier('mock')
mock_method_id = MethodIdentifier(mock_interface_id, 'mock')
mock_interface_def = InterfaceDefinition(mock_interface_id, [mock_method_id])
mock_method_def = MethodDefinition(
    mock_method_id,
    StructDefinition('input', [('input', VoidDefinition())]),
    IntegerDefinition(),
    [])

errors = [
    'com.vmware.vapi.std.errors.internal_server_error',
    'com.vmware.vapi.std.errors.invalid_argument',
    'com.vmware.vapi.std.errors.operation_not_found',
    'com.vmware.vapi.std.errors.unauthenticated',
]
error_defs = [make_std_error_def(error) for error in errors]
error_values = ListValue([convert_data_def_to_data_value(error_def)
                for error_def in error_defs])
logging.basicConfig(level=logging.INFO)

class MockupApiInterface(ApiInterface):
    def __init__(self):
        self.iface_id = InterfaceIdentifier('mock')
        self.method_id = MethodIdentifier(self.iface_id,
                                          'mock')

    def get_identifier(self):
        return self.iface_id

    def get_definition(self):
        return InterfaceDefinition(self.iface_id, [self.method_id])

    def get_method_definition(self, method_id):
        input_ = StructDefinition('mock', [])
        output = IntegerDefinition()
        return MethodDefinition(method_id, input_, output, [])

    def invoke(self, ctx, method_id, input_value):
        return MethodResult(output=IntegerValue(10))


class MockProvider(ApiProvider):

    def invoke(self, service_id, operation_id, input_value, ctx):
        return MethodResult(output=IntegerValue(10))


class UserPwdAuthnHandler(AuthenticationHandler):
    def authenticate(self, sec_ctx):
        if sec_ctx.get(SCHEME_ID) == self.get_supported_scheme():
            if sec_ctx.get(USER_KEY) == 'testuser' and sec_ctx.get(PASSWORD_KEY) == 'password':
                return UserIdentity(sec_ctx.get(USER_KEY))
            else:
                return False
        return None

    def get_supported_scheme(self):
        return USER_PASSWORD_SCHEME_ID


class TestAuthentication(unittest.TestCase):

    def setUp(self):
        provider_config = ProviderConfig()
        provider_config.cfg = configparser.SafeConfigParser()
        provider_config.cfg.add_section('vmware.vapi.security.authentication_filter')
        provider_config.cfg.set('vmware.vapi.security.authentication_filter',
                       'handlers', 'vmware.vapi.security.tests.test_authentication_filter.UserPwdAuthnHandler')
        mock_provider = MockProvider()
        self.authn_filter = AuthenticationFilter(mock_provider, provider_config)

    def test_user_pwd_scheme(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: USER_PASSWORD_SCHEME_ID,
             USER_KEY: 'testuser',
             PASSWORD_KEY: 'password'})
        app_ctx = ApplicationContext()
        ctx = ExecutionContext(app_ctx, sec_ctx)
        input_val = VoidValue()
        method_result = self.authn_filter.invoke(
            'com.pkg.svc', 'op', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(10))
        self.assertEqual(method_result.error, None)

    def test_invalid_user_pwd(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: USER_PASSWORD_SCHEME_ID,
             USER_KEY: 'testuser',
             PASSWORD_KEY: 'invalidpassword'})
        app_ctx = ApplicationContext()
        ctx = ExecutionContext(app_ctx, sec_ctx)
        input_val = VoidValue()
        method_result = self.authn_filter.invoke(
            'com.pkg.svc', 'op', input_val, ctx)
        self.assertEqual(method_result.error.name, 'com.vmware.vapi.std.errors.unauthenticated')

    def test_invalid_user_pwd_scheme(self):
        sec_ctx = SecurityContext(
            {SCHEME_ID: OAUTH_SCHEME_ID,
             ACCESS_TOKEN: 'token'})
        app_ctx = ApplicationContext()
        ctx = ExecutionContext(app_ctx, sec_ctx)
        input_val = VoidValue()
        method_result = self.authn_filter.invoke(
            'com.pkg.svc', 'op', input_val, ctx)
        self.assertEqual(method_result.output, IntegerValue(10))
        self.assertEqual(method_result.error, None)


if __name__ == '__main__':
    unittest.main()
