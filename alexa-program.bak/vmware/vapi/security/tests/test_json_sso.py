"""
Unit tests for JSON signing and verification based on SAML Hok token
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import decimal
import json
import os
import unittest

from vmware.vapi.lib.constants import (
    PARAMS, EXECUTION_CONTEXT, SECURITY_CONTEXT, SCHEME_ID)
from vmware.vapi.security.sso import (
    PRIVATE_KEY, SAML_TOKEN, SAML_SCHEME_ID, SIGNATURE,
    TIMESTAMP, EXPIRES, CREATED, DIGEST, SIGNATURE_ALGORITHM,
    JSONSSOSigner, JSONSSOVerifier, key_regex)
from vmware.vapi.lib.jsonlib import DecimalEncoder

DATA_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'resources', 'sso')


class TestJSONSSO(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(DATA_DIR, 'request.json')) as fp:
            self.json_request = fp.read()

        with open(os.path.join(DATA_DIR, 'key.pem')) as fp:
            self.private_key = fp.read()

        with open(os.path.join(DATA_DIR, 'hoktoken.txt')) as fp:
            self.token = fp.read()

        py_obj = self.load(self.json_request)
        ctx = py_obj.get(PARAMS).get(EXECUTION_CONTEXT)
        sec_ctx = ctx.get(SECURITY_CONTEXT)
        sec_ctx[SCHEME_ID] = SAML_SCHEME_ID
        sec_ctx[PRIVATE_KEY] = self.private_key
        sec_ctx[SAML_TOKEN] = self.token
        sec_ctx[SIGNATURE_ALGORITHM] = 'RS256'
        self.json_request = self.dump(py_obj)

    def load(self, input_message):
        return json.loads(input_message, parse_float=decimal.Decimal)

    def dump(self, py_obj):
        return json.dumps(py_obj,
                          check_circular=False,
                          separators=(',', ':'),
                          cls=DecimalEncoder)

    def test_success_sign(self):
        json_request = JSONSSOSigner().process(self.json_request)
        py_obj = self.load(json_request)
        sec_ctx = py_obj.get(PARAMS).get(EXECUTION_CONTEXT).get(SECURITY_CONTEXT)
        self.assertEqual(sec_ctx.get(SCHEME_ID), SAML_SCHEME_ID)
        self.assertNotEqual(sec_ctx.get(TIMESTAMP), None)
        self.assertNotEqual(sec_ctx.get(SIGNATURE_ALGORITHM), None)
        timestamp = sec_ctx.get(TIMESTAMP)
        self.assertNotEqual(timestamp.get(EXPIRES), None)
        self.assertNotEqual(timestamp.get(CREATED), None)
        self.assertNotEqual(sec_ctx.get(SIGNATURE), None)
        signature = sec_ctx.get(SIGNATURE)
        self.assertNotEqual(signature.get(DIGEST), None)
        self.assertNotEqual(signature.get(SAML_TOKEN), None)

    def test_success_verify(self):
        json_request = JSONSSOSigner().process(self.json_request)
        JSONSSOVerifier().process(json_request.encode('utf-8'))

    def test_null_json(self):
        self.assertEqual(JSONSSOSigner().process(None), None)

    def test_null_json_2(self):
        self.assertEqual(JSONSSOVerifier().process(None), None)

    def test_wrong_scheme_id(self):
        json_request = self.json_request.replace(SAML_SCHEME_ID, 'XXX')
        json_request_result = JSONSSOSigner().process(json_request)
        self.assertEqual(json_request, json_request_result)

    def test_wrong_scheme_id_2(self):
        json_request = self.json_request.replace(SAML_SCHEME_ID, 'XXX')
        json_request_result = JSONSSOVerifier().process(json_request.encode('utf-8'))
        self.assertEqual(json_request, json_request_result.decode('utf-8'))

    def test_mess_with_request(self):
        json_request = JSONSSOSigner().process(self.json_request)
        json_request = json_request.replace('sample.first.mirror',
                                            'sample.first.count')
        self.assertRaises(Exception, JSONSSOVerifier().process, json_request)

    def test_mess_with_algorithm(self):
        json_request = JSONSSOSigner().process(self.json_request)
        json_request = json_request.replace('RS256', 'RS512')
        self.assertRaises(Exception, JSONSSOVerifier().process, json_request)

    def test_mess_with_signature(self):
        json_request = JSONSSOSigner().process(self.json_request)
        py_obj = self.load(json_request)
        sec_ctx = py_obj.get(PARAMS).get(EXECUTION_CONTEXT).get(SECURITY_CONTEXT)
        sec_ctx[SIGNATURE][DIGEST] = 'askljdyfasdfhasdkjfhasdlukf'
        json_request = self.dump(py_obj)
        self.assertRaises(Exception, JSONSSOVerifier().process, json_request)

    def test_private_key_regex(self):
        self.assertEqual(key_regex.search('bogus'), None)
        self.assertEqual(key_regex.search('---bogus---'), None)
        self.assertEqual(key_regex.search('---BEGIN bogus---'), None)
        self.assertEqual(key_regex.search('---BEGIN bogus KEY---'), None)
        self.assertEqual(key_regex.search('---BEGIN bogus KEY---\n'), None)
        self.assertEqual(key_regex.search('---BEGINPRIVATE KEY---\n'), None)
        self.assertEqual(key_regex.search('---BEGIN PRIVATEKEY---\n'), None)
        self.assertEqual(key_regex.search('---BEGIN PRIVATE KEY-----\n'), None)
        self.assertEqual(key_regex.search('-----BEGIN PRIVATE KEY---\n'), None)
        self.assertEqual(key_regex.search('-----BEGIN PRIVATE KEY-----'), None)
        self.assertNotEqual(key_regex.search('-----BEGIN PRIVATE KEY-----\n'), None)
        self.assertNotEqual(key_regex.search('-----BEGIN RSA PRIVATE KEY-----\n'), None)
        self.assertNotEqual(key_regex.search('-----BEGIN RSA PRIVATE KEY-----\n'), None)


if __name__ == '__main__':
    unittest.main()
