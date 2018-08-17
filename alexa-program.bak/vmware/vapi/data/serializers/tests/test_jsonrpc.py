#!/usr/bin/env python

"""
Unit tests for the vapi json rpc protocol
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import decimal
import unittest
import logging
import json

from vmware.vapi.data.serializers.jsonrpc import (
    VAPI_INVOKE,
    JsonRpcDictToVapi, VAPIJsonEncoder,
    deserialize_request, deserialize_response,
    vapi_jsonrpc_request_factory,
    JsonRpc20Error,
    vapi_jsonrpc_error_parse_error,
    vapi_jsonrpc_error_invalid_request,
    vapi_jsonrpc_error_method_not_found,
    vapi_jsonrpc_error_invalid_params,
    vapi_jsonrpc_error_internal_error,
    vapi_jsonrpc_error_transport_error,
    canonicalize_double
)
from vmware.vapi.core import ExecutionContext
from vmware.vapi.data.type import Type
from vmware.vapi.lib.std import make_std_error_def
from vmware.vapi.protocol.client.http_lib import HTTPMethod, HTTPResponse, HTTPRequest
from vmware.vapi.protocol.client.rpc.provider import HTTPProvider, RpcProvider
from vmware.vapi.protocol.server.msg.json_handler import get_protocol_handler
from vmware.vapi.protocol.client.msg.json_connector import get_protocol_connector
from vmware.vapi.provider.local import LocalProvider

from vmware.vapi.core import (
    ApiInterface,
    InterfaceIdentifier,
    MethodIdentifier,
    InterfaceDefinition,
    MethodDefinition,
    MethodResult,
)

from vmware.vapi.data.definition import (
    VoidDefinition,
    IntegerDefinition,
    DoubleDefinition,
    StringDefinition,
    SecretDefinition,
    BooleanDefinition,
    BlobDefinition,
    OpaqueDefinition,
    OptionalDefinition,
    ListDefinition,
    StructDefinition,
    ErrorDefinition,
)

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

logging.basicConfig(level=logging.DEBUG)

def build_adhoc_data_value(data_def):
    instance = data_def.new_value()
    if data_def.type == Type.STRUCTURE or data_def.type == Type.ERROR:
        for field_name in data_def.get_field_names():
            field_def = data_def.get_field(field_name)
            field_instance = build_adhoc_data_value(field_def)
            instance.set_field(field_name, field_instance)
    elif data_def.type == Type.LIST:
        # TODO: Randomize list len?
        instance.add_all([build_adhoc_data_value(data_def.element_type) for val in range(1,7)])
    elif data_def.type == Type.OPTIONAL:
        # TODO: Randomize optional set or not set?
        instance = data_def.new_value(build_adhoc_data_value(data_def.element_type))
    return instance

fake_iface_id = 'vmware.test.fake.iface'
null_method_id = 'Null'
null_method_def = MethodDefinition(MethodIdentifier(
    InterfaceIdentifier(fake_iface_id), null_method_id),
    VoidDefinition(),
    VoidDefinition(),
    [make_std_error_def('error1'),
     make_std_error_def('error2')]
    )
echo_method_id = 'Echo'
echo_method_def = MethodDefinition(MethodIdentifier(
    InterfaceIdentifier(fake_iface_id), echo_method_id),
    StructDefinition('struct',
       [('int', IntegerDefinition()),
        ('str', StringDefinition())]
    ),
    StructDefinition('struct',
       [('int', IntegerDefinition()),
        ('str', StringDefinition())]
    ),
    [make_std_error_def('e1'),
     make_std_error_def('e2'),
     make_std_error_def('e3')])


class FakeInterface(ApiInterface):
    def __init__(self):
        self.if_id = InterfaceIdentifier(fake_iface_id)
        self.operations = {
            null_method_id: null_method_def,
            echo_method_id: echo_method_def
        }
        self.if_def = InterfaceDefinition(
            self.if_id,
            [MethodIdentifier(self.if_id, null_method_id),
             MethodIdentifier(self.if_id, echo_method_id),]
        )

    def get_identifier(self):
        return self.if_id

    def get_definition(self):
        return self.if_def

    def get_method_definition(self, method_id):
        return self.operations.get(method_id.get_name())

    def invoke(self, ctx, method_id, input_value):
        return MethodResult(output=input_value)

class LocalRpcProvider(HTTPProvider):
    def __init__(self, api_provider):
        self.connected = False
        self.api_provider = api_provider

    def connect(self):
        self.connected = True
        return self.connected

    def disconnect(self):
        self.connected = False

    def do_request(self, http_request):
        if self.connected:
            return HTTPResponse(
                status=200, headers=None,
                body=self.api_provider.handle_request(http_request.body))
        else:
            raise Exception('Not connected')


class TestJsonRpc(unittest.TestCase):

    def setUp(self):
        """ setup """
        self.to_vapi = JsonRpcDictToVapi
        api_iface = FakeInterface()
        self.provider = LocalProvider()
        self.provider.add_interface(api_iface)

    def tearDown(self):
        """ tear down """

    def to_json(self, value):
        return json.dumps(value,
                          check_circular=False,
                          separators=(',', ':'),
                          cls=VAPIJsonEncoder)

    def to_vapi_data_value(self, value):
        python_dict = json.loads(value, parse_float=decimal.Decimal)
        return self.to_vapi.data_value(python_dict)

    def to_vapi_method_result(self, value):
        python_dict = json.loads(value, parse_float=decimal.Decimal)
        return self.to_vapi.method_result(python_dict)

    def get_data_definition(self):
        # Get a cover all data definitions
        data_defs = [
            VoidDefinition(),
            IntegerDefinition(),
            DoubleDefinition(),
            StringDefinition(),
            SecretDefinition(),
            BooleanDefinition(),
            BlobDefinition(),
            OpaqueDefinition(),
            OptionalDefinition(IntegerDefinition()),
            ListDefinition(IntegerDefinition()),
            StructDefinition('struct',
                [ ('int', IntegerDefinition()),
                  ('str', StringDefinition()),
                  ('struct', StructDefinition('struct1',
                      [('double', DoubleDefinition()),
                       ('secret', SecretDefinition())])),
                  ('list', ListDefinition(StructDefinition('struct1',
                      [('double', DoubleDefinition()),
                       ('secret', SecretDefinition())]))),
                  ('optional', ListDefinition(StructDefinition('struct1',
                      [('double', DoubleDefinition()),
                       ('secret', SecretDefinition())]))) ]),
            ErrorDefinition('error',
                [ ('int', IntegerDefinition()),
                  ('str', StringDefinition()) ]),
        ]
        return data_defs


    def get_error_value(self):
        error_value = ErrorValue('struct0')
        error_value.set_field('int', IntegerValue(7))
        error_value.set_field('optional', OptionalValue(StringValue("123")))
        error_value.set_field('optional1', OptionalValue())
        return error_value

    def get_struct_value(self):
        struct_value = StructValue('struct0')
        struct_value.set_field('int', IntegerValue(7))
        struct_value.set_field('optional', OptionalValue(StringValue("123")))
        struct_value.set_field('optional1', OptionalValue())
        return struct_value

    def get_data_values(self):
        # Data values
        list_value = ListValue()
        list_value.add_all([IntegerValue(val) for val in range(1,15)])
        data_values = [
            VoidValue(),
            IntegerValue(3),
            DoubleValue(decimal.Decimal('7.2')),
            StringValue('blah'),
            SecretValue(),
            BooleanValue(True),
            BlobValue(b"a blob"),
            BlobValue(b"0\x82\x04\x00"),
            list_value,
            OptionalValue(),
            OptionalValue(IntegerValue(7)),
            StructValue('name'),
            self.get_struct_value(),
            self.get_error_value(),
        ]
        struct_value = StructValue('struct')
        for idx, data_val in enumerate(data_values):
            struct_value.set_field(str(idx), data_val)
        data_values.append(struct_value)
        return data_values

    def test_method_result(self):
        # Method result
        error_value = self.get_error_value()
        method_result = MethodResult(error=error_value)
        self.assertEqual(self.to_vapi_method_result(self.to_json(method_result)).error, method_result.error)

        data_values = self.get_data_values()
        for data_value in data_values:
            method_result = MethodResult(output=data_value)
            self.assertEqual(self.to_vapi_method_result(self.to_json(method_result)).output, method_result.output)

    def test_data_value_conversion(self):
        data_values = self.get_data_values()
        for data_value in data_values:
            json_value = self.to_json(data_value)
            self.assertEqual(self.to_vapi_data_value(json_value),
                             data_value)

        json_value = self.to_json(DoubleValue(17.0))
        self.assertEqual('1.7E1', json_value)
        vapi_value = self.to_vapi_data_value('1.7E1')
        self.assertEqual(DoubleValue(decimal.Decimal('1.7E1')), vapi_value)

    def test_jsonrpc_invalid_params_1(self):
        invalid_json = '{"STRUCTURE": {"vapi.struct": {}}, "bogus": "bogus"}'
        self.assertRaises(JsonRpc20Error, self.to_vapi_data_value, invalid_json)

    def test_jsonrpc_invalid_params_2(self):
        invalid_json = '{"STRUCTURE": {"vapi.struct": {}, "bogus": "bogus"}}'
        self.assertRaises(JsonRpc20Error, self.to_vapi_data_value, invalid_json)

    def test_jsonrpc_invalid_binary_value(self):
        invalid_json = '{"BINARY": "bogus"}'
        self.assertRaises(JsonRpc20Error, self.to_vapi_data_value, invalid_json)

    def test_json_rpc_positive(self):
        requests = [
            # id can be null, number, string, or omitted
            ('{"jsonrpc": "2.0", "method": "subtract", "id": null}', None),
            ('{"jsonrpc": "2.0", "method": "subtract", "id": 3}',
             '{"jsonrpc": "2.0", "result": 0, "id": 3}'),
            ('{"jsonrpc": "2.0", "method": "subtract", "id": "string_id"}',
             '{"jsonrpc": "2.0", "result": 0, "id": "string_id"}'),

            # Accept keyed parameters. Do not accept array parameters
            ('{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}',
             '{"jsonrpc": "2.0", "result": 19, "id": 3}'),
        ]

        for request_str, response_str in requests:
            request = deserialize_request(request_str)
            self.assertFalse(request.notification)
            if response_str:
                response = deserialize_response(response_str)
                request.validate_response(response)
                request.serialize()

        notifications = [
            '{"jsonrpc": "2.0", "method": "subtract"}',
        ]
        for notification_str in notifications:
            request = deserialize_request(notification_str)
            self.assertTrue(request.notification)
            request.serialize_notification()


    def test_json_rpc_request_negative(self):
        requests = [
            ('', JsonRpc20Error.PARSE_ERROR),
            ('sjlfskfdl', JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "method": "foobar, "params": "bar", "baz"]',
             JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "method": 1, "params": "bar"}',
             JsonRpc20Error.INVALID_REQUEST),
            ('{"jsonrpc": "2.0", "method": "a_method", "params": "bar"}',
             JsonRpc20Error.INVALID_REQUEST),
        ]

        for request_str, error_code in requests:
            try:
                logging.info("request str: %s", request_str)
                deserialize_request(request_str)
                self.assertTrue(False)
            except JsonRpc20Error as err:
                logging.info("err: %s", str(err))
                self.assertTrue(err.code == error_code)

        # Negative validate test
        requests = [
            # Mismatch version
            ('{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}',
             '{"version": "1.1", "result": 19, "id": 3}', JsonRpc20Error.INVALID_PARAMS),

            # Mismatch id
            ('{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}',
             '{"jsonrpc": "2.0", "result": 19, "id": 4}', JsonRpc20Error.INVALID_PARAMS),
            # Mismatch id type
            ('{"jsonrpc": "2.0", "method": "subtract", "params": {"subtrahend": 23, "minuend": 42}, "id": 3}',
             '{"jsonrpc": "2.0", "result": 19, "id": "3"}', JsonRpc20Error.INVALID_PARAMS),

            # Notification should have no response
            ('{"jsonrpc": "2.0", "method": "subtract"}',
             '{"jsonrpc": "2.0", "result": 0}',
             JsonRpc20Error.INVALID_PARAMS),
        ]
        for request_str, response_str, error_code in requests:
            request = deserialize_request(request_str)
            if response_str:
                try:
                    response = deserialize_response(response_str)
                except JsonRpc20Error as err:
                    self.assertTrue(err.code == error_code)
                    continue

                try:
                    request.validate_response(response)
                    self.assertTrue(False)
                except JsonRpc20Error as err:
                    logging.info("err: %s", str(err))
                    self.assertTrue(err.code == error_code)


    def test_json_rpc_response_positive(self):
        err_responses = [
            # message / data is optional
            ('{"jsonrpc": "2.0", "error": {"code": -32600}, "id": null}',
             JsonRpc20Error.INVALID_REQUEST),
            # data is primitive / structured
            ('{"jsonrpc": "2.0", "error": {"code": -32600, "data": "somedata"}, "id": null}',
             JsonRpc20Error.INVALID_REQUEST),
            ('{"jsonrpc": "2.0", "error": {"code": -32600, "data": {"key": "somedata"}}, "id": null}',
             JsonRpc20Error.INVALID_REQUEST),

            ('{"jsonrpc": "2.0", "error": {"code": -32600, "message": "Invalid Request."}, "id": null}',
             JsonRpc20Error.INVALID_REQUEST),
            ('{"jsonrpc": "2.0", "error": {"code": -32700, "message": "Parse error."}, "id": null}',
             JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "error": {"code": -32601, "message": "Method not found."}, "id": "1"}',
             JsonRpc20Error.METHOD_NOT_FOUND),
            ('{"jsonrpc": "2.0", "error": {"code": -32602, "message": "Invalid params."}, "id": "1"}',
             JsonRpc20Error.INVALID_PARAMS),
            ('{"jsonrpc": "2.0", "error": {"code": -32603, "message": "Internal error."}, "id": 1}',
             JsonRpc20Error.INTERNAL_ERROR),
        ]
        for response_str, error_code in err_responses:
            response = deserialize_response(response_str)
            self.assertTrue(response.error.code == error_code)
            response.serialize()


    def test_json_rpc_response_negative(self):
        responses = [
            ('', JsonRpc20Error.PARSE_ERROR),
            ('sjlfskfdl', JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "result": "foobar, "error": "bar"}',
             JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "result": "foobar, "error": "bar", "id": null}',
             JsonRpc20Error.PARSE_ERROR),
            ('{"jsonrpc": "2.0", "result": "foobar, "error": {"code": -32603}, "id": null}',
             JsonRpc20Error.PARSE_ERROR),
            ('{"result": 19, "id": 3}', JsonRpc20Error.INVALID_PARAMS),
        ]
        for response_str, error_code in responses:
            try:
                logging.info("response str: %s", response_str)
                deserialize_response(response_str)
                self.assertTrue(False)
            except JsonRpc20Error as err:
                logging.info("err: %s", str(err))
                self.assertTrue(err.code == error_code)

    def test_json_error_factory(self):
        exceptions = [
            (vapi_jsonrpc_error_parse_error, "testing",
             JsonRpc20Error.PARSE_ERROR),
            (vapi_jsonrpc_error_invalid_request, 3,
             JsonRpc20Error.INVALID_REQUEST),
            (vapi_jsonrpc_error_method_not_found, {"a_dict" : 3},
             JsonRpc20Error.METHOD_NOT_FOUND),
            (vapi_jsonrpc_error_invalid_params, None,
             JsonRpc20Error.INVALID_PARAMS),
            (vapi_jsonrpc_error_internal_error, 3.14159,
             JsonRpc20Error.INTERNAL_ERROR),
            (vapi_jsonrpc_error_transport_error, "blah",
             JsonRpc20Error.TRANSPORT_ERROR),
        ]

        for exception_factory, data, error_code in exceptions:
            error = exception_factory(data=data)
            self.assertTrue(error.code == error_code)

    def get_loopback_connector(self, provider):
        protocol_handler = get_protocol_handler(provider)
        rpc_provider = LocalRpcProvider(protocol_handler)
        return get_protocol_connector(rpc_provider)

    def test_json_loopback_positive(self):
        connector = self.get_loopback_connector(self.provider)
        remote = connector.get_api_provider()

        for method_def in [null_method_def, echo_method_def]:
            # invoke_method
            ctx = ExecutionContext()
            params = build_adhoc_data_value(method_def.get_input_definition())
            method_id = echo_method_def.get_identifier().get_name()
            remote_result = remote.invoke(fake_iface_id,
                                          method_id,
                                          params,
                                          ctx)

            local_result = self.provider.invoke(fake_iface_id, method_id, params, ctx)
            if remote_result.success():
                # Validate result output
                method_def.get_output_definition().validate(remote_result.output)
                # Validate direct call
                self.assertEqual(remote_result.output, local_result.output)
            else:
                self.assertTrue(remote_result.error, local_result.error)

    def test_json_loopback_negative(self):
        connector = self.get_loopback_connector(self.provider)
        remote = connector.get_api_provider()
        # Bogus interface / method
        ctx = connector.new_context()
        params = VoidValue()
        result = remote.invoke('bogus.interface', 'bogus', params, ctx)
        self.assertFalse(result.success())
        self.assertTrue(result.error == self.provider.invoke('bogus.interface', 'bogus',
                                                             params, ctx).error)
        logging.error("error: %s", str(result.error))


    # test_json_handle_request_positive should be covered by test_json_loopback_positive
    def test_json_handle_request_negative(self):
        protocol_handler = get_protocol_handler(self.provider)
        rpc_provider = LocalRpcProvider(protocol_handler)
        rpc_provider.connect()

        id_ = 12
        requests = [
            (vapi_jsonrpc_request_factory(method="bogus", params=None, id=id_),
             JsonRpc20Error.METHOD_NOT_FOUND),
            (vapi_jsonrpc_request_factory(method=VAPI_INVOKE,
                                          params={"bogus": 12}, id=id_),
             JsonRpc20Error.INVALID_PARAMS),
        ]

        for request, error_code in requests:
            http_response = rpc_provider.do_request(
                HTTPRequest(method=HTTPMethod.POST, body=request.serialize()))
            response = deserialize_response(http_response.body)
            request.validate_response(response)
            error = response.error
            logging.info("error: %s", error)
            self.assertTrue(error)
            self.assertTrue(error.code == error_code)

    def test_decimal_json_request(self):
        ctx = ExecutionContext()
        template_request = (
            '{"params":{"input":%s,"serviceId":"mock","ctx":{"appCtx":{}},' +
            '"operationId":"mock"},"jsonrpc":' +
            '"2.0","method":"invoke","id":1}'
        )
        template_response = (
            '{"jsonrpc":"2.0","id":1,"result":{"output": %s}}'
        )
        for val, canonical_val in [
                    ('-12.34e4', '-1.234E5'),
                    ('1E-130', '1.0E-130'),
                    ('0.0E-0', '0.0E0'),
                    ('1.2', '1.2E0'),
                    ('1111111.1111100021e-30', '1.1111111111100021E-24'),
                    ('12312423.0', '1.2312423E7'),
                    ('0.000234E-10', '2.34E-14'),
                    ('17', '1.7E1')]:
            decimal_val = decimal.Decimal(val)
            canonical_decimal_val = canonicalize_double(decimal_val)
            data_value = DoubleValue(decimal_val)
            params = {
                'ctx': ctx,
                'serviceId': 'mock',
                'operationId': 'mock',
                'input': data_value
            }
            actual_request = vapi_jsonrpc_request_factory(
                method=VAPI_INVOKE, params=params, id=1).serialize()
            expected_request = template_request % canonical_decimal_val
            self.assertEqual(
                json.loads(actual_request, parse_float=decimal.Decimal),
                json.loads(expected_request, parse_float=decimal.Decimal))
            response_msg = template_response % canonical_val
            response = deserialize_response(response_msg)
            method_result = JsonRpcDictToVapi.method_result(response.result)
            self.assertTrue(method_result.success())
            self.assertTrue(isinstance(method_result.output, DoubleValue))
            self.assertEqual(method_result.output,
                             DoubleValue(decimal.Decimal(canonical_val)))


## Test main
#
if __name__ == "__main__":
    unittest.main()
