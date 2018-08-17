"""
Unit tests for Oauth2 security helpers
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest

from vmware.vapi.security.oauth import (
    create_oauth_security_context, OAUTH_SCHEME_ID, ACCESS_TOKEN)
from vmware.vapi.lib.constants import SCHEME_ID


class TestOauth(unittest.TestCase):
    def test_security_context(self):
        ctx = create_oauth_security_context('token')
        self.assertEqual(ctx[SCHEME_ID], OAUTH_SCHEME_ID)
        self.assertEqual(ctx[ACCESS_TOKEN], 'token')


if __name__ == '__main__':
    unittest.main()
