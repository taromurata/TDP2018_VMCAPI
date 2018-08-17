"""
Unit tests for Authentication Handler
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import os

from vmware.vapi.core import SecurityContext
from vmware.vapi.security.authentication_handler import AuthenticationHandler
from vmware.vapi.security.user_password import USER_PASSWORD_SCHEME_ID, USER_KEY, PASSWORD_KEY
from vmware.vapi.security.oauth import OAUTH_SCHEME_ID, ACCESS_TOKEN
from vmware.vapi.security.session import SESSION_SCHEME_ID, SESSION_ID
from vmware.vapi.security.sso import SAML_SCHEME_ID, SAML_BEARER_SCHEME_ID, SAML_TOKEN, PRIVATE_KEY
from vmware.vapi.security.user_identity import UserIdentity
from vmware.vapi.lib.constants import SCHEME_ID


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


class SamlHoKTokenAuthnHandler(AuthenticationHandler):
    def authenticate(self, sec_ctx):
        if sec_ctx.get(SCHEME_ID) == self.get_supported_scheme():
            if sec_ctx.get(SAML_TOKEN) == 'saml-token':
                return UserIdentity('saml-user', 'saml-domain')
            else:
                return False

    def get_supported_scheme(self):
        return SAML_SCHEME_ID


class SamlBearerTokenAuthnHandler(AuthenticationHandler):
    def authenticate(self, sec_ctx):
        if sec_ctx.get(SCHEME_ID) == self.get_supported_scheme():
            if sec_ctx.get(SAML_TOKEN) == 'saml-bearer-token':
                return UserIdentity('saml-bearer-user', 'saml-bearer-domain')
            else:
                return False

    def get_supported_scheme(self):
        return SAML_BEARER_SCHEME_ID


class OAuthTokenAuthnHandler(AuthenticationHandler):
    def authenticate(self, sec_ctx):
        if sec_ctx.get(SCHEME_ID) == self.get_supported_scheme():
            if sec_ctx.get(ACCESS_TOKEN) == 'token':
                return UserIdentity('oauth-user')
            else:
                return False
        return None

    def get_supported_scheme(self):
        return OAUTH_SCHEME_ID


class SessionAuthnHandler(AuthenticationHandler):
    def authenticate(self, sec_ctx):
        if sec_ctx.get(SCHEME_ID) == self.get_supported_scheme():
            if sec_ctx.get(SESSION_ID) == 'session-id':
                return UserIdentity('session-user')
            else:
                return False
        return None

    def get_supported_scheme(self):
        return SESSION_SCHEME_ID


class TestAuthnHandler(unittest.TestCase):
    def test_valid_user_pwd_handler(self):
        security_context = SecurityContext({SCHEME_ID: USER_PASSWORD_SCHEME_ID,
                                            USER_KEY: 'testuser',
                                            PASSWORD_KEY: 'password'})
        handler = UserPwdAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result.get_username(), 'testuser')
        self.assertEqual(result.get_domain(), None)

    def test_invalid_user_pwd_handler(self):
        security_context = SecurityContext({SCHEME_ID: USER_PASSWORD_SCHEME_ID,
                                            USER_KEY: 'testuser',
                                            PASSWORD_KEY: 'pwd'})
        handler = UserPwdAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertFalse(result)

    def test_user_pwd_handler_invalid_scheme(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'token'})
        handler = UserPwdAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result, None)

    def test_valid_oauth_handler(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'token'})
        handler = OAuthTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result.get_username(), 'oauth-user')
        self.assertEqual(result.get_domain(), None)

    def test_invalid_oauth_handler(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'invalid-token'})
        handler = OAuthTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertFalse(result)

    def test_oauth_handler_invalid_scheme(self):
        security_context = SecurityContext({SCHEME_ID: USER_PASSWORD_SCHEME_ID,
                                            USER_KEY: 'testuser',
                                            PASSWORD_KEY: 'password'})
        handler = OAuthTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result, None)

    def test_valid_saml_hok_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_SCHEME_ID,
                                            PRIVATE_KEY: 'key',
                                            SAML_TOKEN: 'saml-token'})
        handler = SamlHoKTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result.get_username(), 'saml-user')
        self.assertEqual(result.get_domain(), 'saml-domain')

    def test_invalid_saml_hok_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_SCHEME_ID,
                                            PRIVATE_KEY: 'key',
                                            SAML_TOKEN: 'invalid-saml-token'})
        handler = SamlHoKTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertFalse(result)

    def test_saml_hok_handler_invalid_scheme(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'invalid-session-id'})
        handler = SamlBearerTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result, None)

    def test_valid_saml_bearer_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_BEARER_SCHEME_ID,
                                            SAML_TOKEN: 'saml-bearer-token'})
        handler = SamlBearerTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result.get_username(), 'saml-bearer-user')
        self.assertEqual(result.get_domain(), 'saml-bearer-domain')

    def test_invalid_saml_bearer_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_BEARER_SCHEME_ID,
                                            SAML_TOKEN: 'invalid-saml-token'})
        handler = SamlBearerTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertFalse(result)

    def test_saml_bearer_handler_invalid_scheme(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'invalid-session-id'})
        handler = SamlBearerTokenAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result, None)

    def test_valid_session_handler(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'session-id'})
        handler = SessionAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result.get_username(), 'session-user')
        self.assertEqual(result.get_domain(), None)

    def test_invalid_session_handler(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'invalid-session-id'})
        handler = SessionAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertFalse(result)

    def test_session_handler_invalid_scheme(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'token'})
        handler = SessionAuthnHandler()
        result = handler.authenticate(security_context)
        self.assertEqual(result, None)
