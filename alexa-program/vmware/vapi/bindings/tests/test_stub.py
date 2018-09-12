"""
Unit tests for binding stub helper classes
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import requests
import unittest
import uuid

from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubConfiguration, VapiInterface)
from vmware.vapi.bindings.type import (
    StructType, ErrorType, VoidType, BooleanType, StringType, IdType)
from vmware.vapi.core import InterfaceIdentifier, MethodResult
from vmware.vapi.data.value import BooleanValue, StringValue, ErrorValue
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.connect import get_requests_connector
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata
from vmware.vapi.lib.std import make_error_value_from_msgs, make_std_error_def
from vmware.vapi.message import Message
from vmware.vapi.protocol.client.local_connector import get_local_connector
from vmware.vapi.protocol.client.connector import Connector


### Data used by the mockup classes and the test methods

# Method names
report_vapi_success = 'report_vapi_success'
report_vapi_error = 'report_vapi_error'
report_vapi_exception = 'report_vapi_exception'
nonexistent_method = 'nonexistent_method'

# Type names
not_found = 'not_found'
operation_not_found = 'operation_not_found'

# Error definitions
not_found_def = make_std_error_def(not_found)
operation_not_found_def = make_std_error_def(operation_not_found)

### Utility functions used by the mockup classes and the test methods

def input_struct_name(method_name):
    return 'Input%s' % method_name


class MockupNotFound(VapiError):
    def __init__(self, **kwargs):
        self.messages = kwargs.get('messages')
        VapiError.__init__(self)


class MockupServiceNotFound(VapiError):
    def __init__(self, **kwargs):
        self.messages = kwargs.get('messages')
        VapiError.__init__(self)


# Error (binding) types
not_found_error_type = ErrorType(not_found, {}, MockupNotFound)
operation_not_found_error_type = ErrorType(operation_not_found,
                                           {},
                                           MockupServiceNotFound)


class MockupApiProvider(object):
    msg = Message('mockup.message.id', 'mockup error message')

    def invoke(self, service_id, operation_id, input, ctx):
        if operation_id == report_vapi_error:
            error_value = make_error_value_from_msgs(not_found_def, self.msg)
            return MethodResult(error=error_value)
        elif operation_id == report_vapi_success:
            return MethodResult(output=BooleanValue(True))
        elif operation_id == 'echo':
            msg = input.get_field('message')
            return MethodResult(output=msg)
        elif operation_id == 'echo_long_running':
            msg = input.get_field('message')
            return MethodResult(output=msg)
        elif operation_id == 'echo_long_running$task':
            return MethodResult(output=StringValue(str(uuid.uuid4())))
        else:
            error_value = make_error_value_from_msgs(
                operation_not_found_def,
                self.msg)
            return MethodResult(error=error_value)


class TestApiMethodStub(unittest.TestCase):
    interface_id = InterfaceIdentifier('mockup_interface')

    def test_report_success(self):
        config = StubConfiguration(get_local_connector(MockupApiProvider()))
        operations = {
            report_vapi_success: {
                'input_type': StructType(report_vapi_success, {}),
                'output_type': BooleanType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        stub = ApiInterfaceStub('mockup_interface',
                                config=config,
                                operations=operations)
        self.assertEqual(stub.native_invoke(ctx=config.connector.new_context(),
                                            method_name=report_vapi_success,
                                            kwargs={}),
                         True)

    def test_report_vapi_error(self):
        config = StubConfiguration(get_local_connector(MockupApiProvider()))
        operations = {
            report_vapi_error: {
                'input_type': StructType(report_vapi_error, {}),
                'output_type': BooleanType(),
                'errors': {not_found: not_found_error_type},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        stub = ApiInterfaceStub('mockup_interface',
                                config=config,
                                operations=operations)
        self.assertRaises(MockupNotFound,
                          stub.native_invoke,
                          config.connector.new_context(),
                          report_vapi_error,
                          {})

    def test_report_unexpected_error(self):
        config = StubConfiguration(get_local_connector(MockupApiProvider()))
        operations = {
            nonexistent_method: {
                'input_type': StructType(nonexistent_method, {}),
                'output_type': BooleanType(),
                'errors': {not_found: not_found_error_type},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        stub = ApiInterfaceStub('mockup_interface',
                                config=config,
                                operations=operations)
        self.assertRaises(VapiError,
                          stub.native_invoke,
                          config.connector.new_context(),
                          nonexistent_method,
                          {})

    def test_catch_unexpected_error(self):
        config = StubConfiguration(get_local_connector(MockupApiProvider()),
                                   operation_not_found_error_type)
        operations = {
            nonexistent_method: {
                'input_type': StructType(nonexistent_method, {}),
                'output_type': VoidType(),
                'errors': {not_found: not_found_error_type},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        stub = ApiInterfaceStub('mockup_interface',
                                config=config,
                                operations=operations)
        self.assertRaises(MockupServiceNotFound,
                          stub.native_invoke,
                          config.connector.new_context(),
                          nonexistent_method,
                          {})


class MockIface(VapiInterface):
    def __init__(self, config):
        VapiInterface.__init__(self, config, _MockStub)

    def echo(self, **kwargs):
        return self._invoke('echo', {'message': kwargs.get('message')})

    def echo_long_running_task(self, **kwargs):
        return self._invoke('echo_long_running$task', {'message': kwargs.get('message')})

    def echo_long_running(self, **kwargs):
        return self._invoke('echo_long_running', {'message': kwargs.get('message')})

    def invalid(self, **kwargs):
        return self._invoke('invalid', {})


class _MockStub(ApiInterfaceStub):
    interface_id = InterfaceIdentifier('mockup_interface')

    def __init__(self, config):
        operations = {
            'echo': {
                'input_type': StructType('echoInput', {'message': StringType()}),
                'output_type': StringType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            },
            'echo_long_running': {
                'input_type': StructType('echoInput', {'message': StringType()}),
                'output_type': StringType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.TASK,
            },
            'echo_long_running$task': {
                'input_type': StructType('echoInput', {'message': StringType()}),
                'output_type': IdType(resource_types='com.vmware.cis.TASK'),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.TASK,
            },
            'invalid': {
                'input_type': StructType('invalidInput', {}),
                'output_type': StringType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        ApiInterfaceStub.__init__(self, iface_name=self.interface_id,
                                  config=config,
                                  operations=operations)


class _MockRestStub(ApiInterfaceStub):
    interface_id = InterfaceIdentifier('mockup_interface')

    def __init__(self, config):
        operations = {
            'echo': {
                'input_type': StructType('echoInput', {'message': StringType()}),
                'output_type': StringType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            },
            'invalid': {
                'input_type': StructType('invalidInput', {}),
                'output_type': StringType(),
                'errors': {},
                'input_value_validator_list': [],
                'output_validator_list': [],
                'task_type': TaskType.NONE,
            }
        }
        rest_metadata = {
            'echo': OperationRestMetadata(http_method='POST',
                                          url_template='/test/echo?action=echo'),
            'invalid': OperationRestMetadata(http_method='POST',
                                             url_template='/test/echo?action=invalid')
        }
        ApiInterfaceStub.__init__(self, iface_name=self.interface_id,
                                  config=config,
                                  operations=operations,
                                  rest_metadata=rest_metadata,
                                  is_vapi_rest=False)


class MockRestIface(VapiInterface):
    def __init__(self, config):
        VapiInterface.__init__(self, config, _MockRestStub)

    def echo(self, **kwargs):
        return self._invoke('echo', {'message': kwargs.get('message')})

    def invalid(self, **kwargs):
        return self._invoke('invalid', {})



class TestApiInterfaceStub(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        session = requests.session()
        session.verify = False
        cls.rest_connector = get_requests_connector(
            session=session, msg_protocol='rest', url='https://some-url')
        cls.stub_config = StubConfiguration(cls.rest_connector)

    def test_bad_connector(self):
        self.assertRaises(TypeError, MockIface, config=None)

    def test_invoke_valid_method(self):
        connector = get_local_connector(MockupApiProvider())
        self.assertTrue(isinstance(connector, Connector))

        iface = MockIface(StubConfiguration(connector))
        self.assertTrue(isinstance(iface, VapiInterface))

        self.assertEqual(iface.echo(message='hello'), 'hello')

    def test_invoke_echo_long_running_method(self):
        connector = get_local_connector(MockupApiProvider())
        self.assertTrue(isinstance(connector, Connector))

        iface = MockIface(StubConfiguration(connector))
        self.assertTrue(isinstance(iface, VapiInterface))

        result = iface.echo_long_running_task(message='hello')
        self.assertNotEqual(result, 'hello')
        try:
            uuid.UUID(result, version=4)
        except ValueError:
            # There's no assertNotRaises so explicitly fail assert
            # in case a ValueError is thrown for invalid uuid.
            self.assertTrue(False)

    def test_invoke_echo_long_running_false_method(self):
        connector = get_local_connector(MockupApiProvider())
        self.assertTrue(isinstance(connector, Connector))

        iface = MockIface(StubConfiguration(connector))
        self.assertTrue(isinstance(iface, VapiInterface))

        self.assertEqual(iface.echo_long_running(message='hello'), 'hello')

    def test_invoke_invalid_method(self):
        connector = get_local_connector(MockupApiProvider())
        iface = MockIface(StubConfiguration(connector))
        self.assertRaises(Exception, iface.invalid)

    def test_rest_client_provider_without_rest_metadata(self):
        iface = MockIface(self.stub_config)
        self.assertRaises(CoreException, iface.echo, message='hello')

    def test_json_client_provider_for_swagger_services(self):
        connector = get_local_connector(MockupApiProvider())
        iface = MockRestIface(StubConfiguration(connector))
        self.assertRaises(CoreException, iface.echo, message='hello')

if __name__ == "__main__":
   unittest.main()
