#!/usr/bin/env python

"""
Unit tests for the REST de/serializer
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import base64
import decimal
import unittest
import logging
import json
import six

from vmware.vapi.core import ExecutionContext, MethodResult, SecurityContext
from vmware.vapi.data.value import (
    VoidValue,
    IntegerValue,
    DoubleValue,
    StringValue,
    SecretValue,
    BooleanValue,
    BlobValue,
    OptionalValue,
    ListValue,
    StructValue,
    ErrorValue,
)
from vmware.vapi.data.serializers.rest import RestSerializer
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.rest import OperationRestMetadata
from vmware.vapi.lib.std import (
    _make_struct_value_from_message, make_error_value_from_msgs,
    make_std_error_def)
from vmware.vapi.message import Message
from vmware.vapi.security.user_password import (
    create_user_password_security_context)
from vmware.vapi.security.session import (
    create_session_security_context, REST_SESSION_ID_KEY)

logging.basicConfig(level=logging.DEBUG)


class TestRequestSerializer(unittest.TestCase):
    def test_empty_input_no_metadata(self):
        input_val = StructValue(
            name='operation-input',
            values={})
        url_path, headers, actual_body, cookies = \
            RestSerializer.serialize_request(
                input_value=input_val, ctx=None, rest_metadata=None,
                is_vapi_rest=True)
        expected_body = '{}'
        expected_headers = {}
        self.assertIsNone(url_path)
        self.assertEqual(expected_headers, headers)
        self.assertIsNone(cookies)
        self.assertEqual(expected_body, actual_body)

    def test_string_input(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
            })
        _, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=None,
            is_vapi_rest=True)
        expected_body = '{"string_val":"string1"}'
        expected_headers = {}
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_url_path_without_path_variable(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/foo/bar',
            path_variables={
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/bar'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_url_path_with_integer_path_variable(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'int_val_url': IntegerValue(100),
            })
        rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/foo/{intValUrl}',
            path_variables={
                'int_val_url': 'intValUrl'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/100'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_url_path_with_path_variable(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'string_val_url': StringValue('string2'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/foo/{stringValUrl}',
            path_variables={
                'string_val_url': 'stringValUrl'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/string2'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_url_path_with_query_param(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar?action=start'
            )
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/bar?action=start'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_query_params(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'action1_val': StringValue('start'),
                'action2_val': StringValue('stop'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar',
            query_parameters={
                'action1_val': 'action1',
                'action2_val': 'action2'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_paths = [
            '/foo/bar?action1=start&action2=stop',
            '/foo/bar?action2=stop&action1=start']
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertTrue(url_path in expected_url_paths)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_query_params_boolean(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'action1_val': BooleanValue(value=False)
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar',
            query_parameters={
                'action1_val': 'action1',
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/bar?action1=false'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_query_params_optionals(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'action1_val': OptionalValue(value=StringValue('start')),
                'action2_val': OptionalValue()
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar',
            query_parameters={
                'action1_val': 'action1',
                'action2_val': 'action2'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/bar?action1=start'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_invalid_query_params(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'action1_val': OptionalValue(value=StringValue('start')),
                'action2_val': ListValue([])
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar',
            query_parameters={
                'action1_val': 'action1',
                'action2_val': 'action2'
            })
        self.assertRaises(CoreException, RestSerializer.serialize_request,
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)

    def test_url_path_with_query_param_and_other_query_params(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'string_val': StringValue('string1'),
                'action2_val': StringValue('stop'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo/bar?action1=start',
            query_parameters={
                'action2_val': 'action2'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_paths = [
            '/foo/bar?action1=start&action2=stop',
            '/foo/bar?action2=stop&action1=start']
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertTrue(url_path in expected_url_paths)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_request_body_annotation(self):
        spec_val = StructValue(
            name='spec',
            values={
                'string_val': StringValue('string1'),
            })
        input_val = StructValue(
            name='operation-input',
            values={
                'spec_val': spec_val
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST', url_template='/foo',
            request_body_parameter='spec_val')
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_all_annotations(self):
        input_val = StructValue(
            name='operation-input',
            values={
                'spec_val': StructValue(
                    name='spec',
                    values={
                        'string_val': StringValue('string1'),
                    }),
                'string_val_url': StringValue('string2'),
                'action_val': StringValue('stop'),
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST', url_template='/foo/{stringValUrl}',
            request_body_parameter='spec_val',
            path_variables={
                'string_val_url': 'stringValUrl'
            },
            query_parameters={
                'action_val': 'action'
            })
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo/string2?action=stop'
        expected_headers = {}
        expected_body = '{"string_val":"string1"}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_username_security_context(self):
        input_val = StructValue(
            name='operation-input',
            values={})
        user, password = 'user', 'pwd'
        sec_ctx = create_user_password_security_context(user, password)
        _, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=ExecutionContext(security_context=sec_ctx),
            rest_metadata=None, is_vapi_rest=True)
        expected_body = '{}'
        if six.PY2:
            b64_credentials = base64.b64encode('%s:%s' % (user, password))
            authorization_val = 'Basic %s' % b64_credentials
        else:
            b64_credentials = base64.b64encode(bytes('%s:%s' % (user, password),
                                                     'utf-8'))
            authorization_val = b'Basic ' + b64_credentials
        expected_headers = {
            'Authorization': authorization_val
        }
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_session_security_context(self):
        input_val = StructValue(
            name='operation-input',
            values={})
        session_id = 'some-session-id'
        sec_ctx = create_session_security_context(session_id)
        _, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=ExecutionContext(security_context=sec_ctx),
            rest_metadata=None, is_vapi_rest=True)
        expected_body = '{}'
        expected_headers = {
            REST_SESSION_ID_KEY: session_id
        }
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)

    def test_body(self):
        spec_val = StructValue(
            name='spec',
            values={
                'string_val': StringValue('string1'),
            })
        input_val = StructValue(
            name='operation-input',
            values={
                'spec_val': spec_val
            })
        rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/foo')
        url_path, actual_headers, actual_body, _ = RestSerializer.serialize_request(
            input_value=input_val, ctx=None, rest_metadata=rest_metadata,
            is_vapi_rest=True)
        expected_url_path = '/foo'
        expected_headers = {}
        expected_body = '{"spec_val":{"string_val":"string1"}}'
        self.assertEqual(expected_url_path, url_path)
        self.assertEqual(expected_headers, actual_headers)
        self.assertEqual(expected_body, actual_body)


class TestVapiResponseDeserializer(unittest.TestCase):

    def test_string_value(self):
        input_status = 200
        input_response = '{"value":"vm-100"}'
        expected_result = MethodResult(output=StringValue('vm-100'))
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_struct_value(self):
        input_status = 200
        input_response = '{"value":{"id":"vm-100", "name":"Linux VM"}}'
        expected_result = MethodResult(output=StructValue(values={
            'id': StringValue('vm-100'),
            'name': StringValue('Linux VM')
        }))
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_optional_value(self):
        input_status = 200
        input_response = '{"value":null}'
        expected_result = MethodResult(output=OptionalValue())
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_void_value(self):
        input_status = 200
        input_response = ''
        expected_result = MethodResult(output=VoidValue())
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_not_found_error_value(self):
        input_status = 404
        input_response = '{"type":"com.vmware.vapi.std.errors.not_found","value":{"messages":[{"args":["datacenter-21"],"default_message":"Datacenter with identifier \'datacenter-21\' does not exist.","id":"com.vmware.api.vcenter.datacenter.not_found"}]}}'
        msg_val = StructValue(
            values={
                'id': StringValue('com.vmware.api.vcenter.datacenter.not_found'),
                'default_message': StringValue('Datacenter with identifier \'datacenter-21\' does not exist.'),
                'args': ListValue([StringValue('datacenter-21')])
            })
        error_val = ErrorValue('com.vmware.vapi.std.errors.not_found',
                               {'messages': ListValue([msg_val])})
        expected_result = MethodResult(error=error_val)
        logging.debug(expected_result)
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_successful_status_202(self):
        input_status = 202
        input_response = '{"value":"vm-100"}'
        expected_result = MethodResult(output=StringValue('vm-100'))
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=True)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)


class TestNonVapiResponseDeserializer(unittest.TestCase):

    def test_string_value(self):
        input_status = 200
        input_response = '"vm-100"'
        expected_result = MethodResult(output=StringValue('vm-100'))
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=False)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)

    def test_struct_value(self):
        input_status = 200
        input_response = '{"id":"vm-100", "name":"Linux VM"}'
        expected_result = MethodResult(output=StructValue(values={
            'id': StringValue('vm-100'),
            'name': StringValue('Linux VM')
        }))
        actual_result = RestSerializer.deserialize_response(
            status=input_status, response_str=input_response, is_vapi_rest=False)
        self.assertEqual(expected_result.output, actual_result.output)
        self.assertEqual(expected_result.error, actual_result.error)


if __name__ == "__main__":
    unittest.main()
