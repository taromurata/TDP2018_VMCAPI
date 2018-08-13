"""
Unit tests for Authorization Handler
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import os

from vmware.vapi.core import SecurityContext
from vmware.vapi.security.authorization_handler import AuthorizationHandler
from vmware.vapi.security.user_password import USER_PASSWORD_SCHEME_ID, USER_KEY, PASSWORD_KEY
from vmware.vapi.security.oauth import OAUTH_SCHEME_ID, ACCESS_TOKEN
from vmware.vapi.security.session import SESSION_SCHEME_ID, SESSION_ID
from vmware.vapi.security.sso import SAML_SCHEME_ID, SAML_BEARER_SCHEME_ID, SAML_TOKEN, PRIVATE_KEY
from vmware.vapi.security.user_identity import UserIdentity
from vmware.vapi.lib.constants import AUTHN_IDENTITY, SCHEME_ID


class UserPwdAuthzHandler(AuthorizationHandler):
    def authorize(self, service_id, operation_id, sec_ctx):
        user_id = sec_ctx.get(AUTHN_IDENTITY)
        return user_id.get_username() == 'validuser'


class SamlTokenAuthzHandler(AuthorizationHandler):
    def authorize(self, service_id, operation_id, sec_ctx):
        user_id = sec_ctx.get(AUTHN_IDENTITY)
        return (user_id.get_username() == 'valid-saml-user' and
                user_id.get_domain() == 'valid-saml-domain')


class OAuthTokenAuthzHandler(AuthorizationHandler):
    def authorize(self, service_id, operation_id, sec_ctx):
        user_id = sec_ctx.get(AUTHN_IDENTITY)
        return user_id.get_username() == 'valid-oauth-user'


class SessionAuthzHandler(AuthorizationHandler):
    def authorize(self, service_id, operation_id, sec_ctx):
        user_id = sec_ctx.get(AUTHN_IDENTITY)
        return user_id.get_username() == 'valid-session-user'


class TestAuthzHandler(unittest.TestCase):
    def test_valid_user_pwd_handler(self):
        security_context = SecurityContext({SCHEME_ID: USER_PASSWORD_SCHEME_ID,
                                            USER_KEY: 'validuser',
                                            PASSWORD_KEY: 'password',
                                            AUTHN_IDENTITY: UserIdentity('validuser')})
        handler = UserPwdAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertTrue(result)

    def test_unauthorized_user_pwd_handler(self):
        security_context = SecurityContext({SCHEME_ID: USER_PASSWORD_SCHEME_ID,
                                            USER_KEY: 'unauthorizeduser',
                                            PASSWORD_KEY: 'password',
                                            AUTHN_IDENTITY: UserIdentity('unauthorizeduser')})
        handler = UserPwdAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_valid_oauth_handler(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'token',
                                            AUTHN_IDENTITY: UserIdentity('valid-oauth-user')})
        handler = OAuthTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertTrue(result)

    def test_unauthorized_oauth_handler(self):
        security_context = SecurityContext({SCHEME_ID: OAUTH_SCHEME_ID,
                                            ACCESS_TOKEN: 'token',
                                            AUTHN_IDENTITY: UserIdentity('invalid-oauth-user')})
        handler = OAuthTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_valid_saml_hok_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_SCHEME_ID,
                                            PRIVATE_KEY: 'key',
                                            SAML_TOKEN: 'valid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('valid-saml-user',
                                                                         'valid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertTrue(result)

    def test_invalid_user_saml_hok_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_SCHEME_ID,
                                            PRIVATE_KEY: 'key',
                                            SAML_TOKEN: 'invalid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('invalid-saml-user',
                                                                         'valid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_invalid_domain_saml_hok_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_SCHEME_ID,
                                            PRIVATE_KEY: 'key',
                                            SAML_TOKEN: 'invalid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('valid-saml-user',
                                                                         'invalid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_valid_saml_bearer_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_BEARER_SCHEME_ID,
                                            SAML_TOKEN: 'valid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('valid-saml-user',
                                                                         'valid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertTrue(result)

    def test_invalid_user_saml_bearer_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_BEARER_SCHEME_ID,
                                            SAML_TOKEN: 'invalid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('invalid-saml-user',
                                                                         'valid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_invalid_domain_saml_bearer_handler(self):
        security_context = SecurityContext({SCHEME_ID: SAML_BEARER_SCHEME_ID,
                                            SAML_TOKEN: 'invalid-saml-token',
                                            AUTHN_IDENTITY: UserIdentity('valid-saml-user',
                                                                         'invalid-saml-domain')})
        handler = SamlTokenAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)

    def test_valid_session_handler(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'session-id',
                                            AUTHN_IDENTITY: UserIdentity('valid-session-user')})
        handler = SessionAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertTrue(result)

    def test_invalid_session_handler(self):
        security_context = SecurityContext({SCHEME_ID: SESSION_SCHEME_ID,
                                            SESSION_ID: 'invalid-session-id',
                                            AUTHN_IDENTITY: UserIdentity('invalid-session-user')})
        handler = SessionAuthzHandler()
        result = handler.authorize('com.vmware.pkg', 'op', security_context)
        self.assertFalse(result)
