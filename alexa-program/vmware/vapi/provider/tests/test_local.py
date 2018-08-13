"""
Unit tests for Local Api Provider
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import unittest

from six.moves import configparser

from vmware.vapi.core import (
    ApiInterface,
    MethodDefinition,
    MethodResult,
    InterfaceIdentifier,
    MethodIdentifier,
    ExecutionContext,
    InterfaceDefinition
    )
from vmware.vapi.data.definition import (
    IntegerDefinition,
    StructDefinition,
    VoidDefinition
    )
from vmware.vapi.data.value import (
    IntegerValue, StructValue, ErrorValue, StringValue, OptionalValue,
    ListValue, VoidValue)
from vmware.vapi.lib.std import make_error_value_from_msgs, make_std_error_def
from vmware.vapi.lib.constants import OPERATION_INPUT
from vmware.vapi.message import Message
from vmware.vapi.l10n.runtime import message_factory
from vmware.vapi.provider.local import LocalProvider
from vmware.vapi.stdlib.client.introspection import IntrospectableApiProvider
from vmware.vapi.protocol.client.local_connector import LocalConnector
from vmware.vapi.settings.config import ProviderConfig, Sections
from vmware.vapi.data.serializers.introspection import convert_data_def_to_data_value

logging.basicConfig(level=logging.DEBUG)

### Data used by the mockup classes and the test methods

interface_id = InterfaceIdentifier('mockup_interface')

# Method names
missing_input_definition = 'missing_input_definition'
invalid_input_definition = 'invalid_input_definition'
missing_output_definition = 'missing_output_definition'
invalid_output_definition = 'invalid_output_definition'
mock_definition = 'mock'

report_declared_error = 'report_declared_error'
report_undeclared_error = 'report_undeclared_error'
raise_python_exception = 'raise_python_exception'
return_invalid_output = 'return_invalid_output'

# Method identifiers
missing_input_definition_id = MethodIdentifier(interface_id,
                                               missing_input_definition)
invalid_input_definition_id = MethodIdentifier(interface_id,
                                               invalid_input_definition)
missing_output_definition_id = MethodIdentifier(interface_id,
                                                missing_output_definition)
invalid_output_definition_id = MethodIdentifier(interface_id,
                                                invalid_output_definition)
mock_definition_id = MethodIdentifier(interface_id,
                                      mock_definition)

report_declared_error_id = MethodIdentifier(interface_id, report_declared_error)
report_undeclared_error_id = MethodIdentifier(interface_id,
                                              report_undeclared_error)
raise_python_exception_id = MethodIdentifier(interface_id,
                                             raise_python_exception)
return_invalid_output_id = MethodIdentifier(interface_id,
                                             return_invalid_output)

method_id_dict = {
    missing_input_definition: missing_input_definition_id,
    invalid_input_definition: invalid_input_definition_id,
    missing_output_definition: missing_output_definition_id,
    invalid_output_definition: invalid_output_definition_id,

    report_declared_error: report_declared_error_id,
    report_undeclared_error: report_undeclared_error_id,
    raise_python_exception: raise_python_exception_id,
    return_invalid_output: return_invalid_output_id,
}

internal_server_error_def = make_std_error_def(
    'com.vmware.vapi.std.errors.internal_server_error')
invalid_argument_def = make_std_error_def(
    'com.vmware.vapi.std.errors.invalid_argument')
not_found_error_def = make_std_error_def('com.vmware.vapi.std.errors.not_found')
operation_not_found_def = make_std_error_def(
    'com.vmware.vapi.std.errors.operation_not_found')

error_values = ListValue([
    convert_data_def_to_data_value(internal_server_error_def),
    convert_data_def_to_data_value(invalid_argument_def),
    convert_data_def_to_data_value(operation_not_found_def)
])


_msg = Message('mockup.message.id', 'mockup error message')
not_found_error = make_error_value_from_msgs(not_found_error_def, _msg)

param_name = 'param'


class MockupApiInterface(ApiInterface):
    def __init__(self):
        pass

    def get_identifier(self):
        return interface_id

    def get_definition(self):
        return InterfaceDefinition(interface_id,
            [missing_input_definition_id, invalid_input_definition_id,
             missing_output_definition_id, invalid_output_definition_id,
             mock_definition_id, report_declared_error_id,
             report_undeclared_error_id, raise_python_exception_id,
             return_invalid_output_id])

    def get_method_definition(self, method_id):
        name = method_id.get_name()
        if name == 'bogus_method':
            return None

        if name == missing_input_definition:
            input_ = None
        elif name == invalid_input_definition:
            input_ = 'not a StructDefinition'
        elif name == mock_definition:
            input_ = StructDefinition(OPERATION_INPUT, [])
        else:
            input_ = StructDefinition(OPERATION_INPUT,
                                      [(param_name, IntegerDefinition())])
        if name == missing_output_definition:
            output = None
        elif name == invalid_input_definition:
            output = 'not a DataDefinition'
        else:
            output = VoidDefinition()
        errors = []
        if name == report_declared_error:
            errors.append(not_found_error_def)
        return MethodDefinition(method_id, input_, output, errors)

    def invoke(self, ctx, method_id, input_value):
        name = method_id.get_name()
        if name == raise_python_exception:
            raise RuntimeError()
        elif name == return_invalid_output:
            return MethodResult(output=StructValue())
        elif name == mock_definition:
            return MethodResult(output=VoidValue())
        return MethodResult(error=not_found_error)


# This method is need for test_register_duplicate_interface
def register_instance():
    """
    Specify the instances that should be
    registered with the api provider
    """
    return [MockupApiInterface()]


class TestLocalProvider(unittest.TestCase):
    def setUp(self):
        mockup_api_interface = MockupApiInterface()
        self.local_provider = LocalProvider()
        self.local_provider.add_interface(mockup_api_interface)
        connector = LocalConnector(self.local_provider)
        self.introspection = IntrospectableApiProvider(connector)

    def _test_method_failure(self, operation_id, error, message_id=None, *args):
        ctx = ExecutionContext()
        method_id = method_id_dict[operation_id]
        service_id = method_id.get_interface_identifier().get_name()

        if isinstance(error, ErrorValue):
            expected_error_value = error
        else:
            msg = message_factory.get_message(message_id, *args)
            expected_error_value = make_error_value_from_msgs(error, msg)

        provider = self.local_provider
        method_def = self.introspection.get_method(service_id, operation_id)
        input_value = method_def.get_input_definition().new_value()
        input_value.set_field(param_name, IntegerValue(0))
        method_result = provider.invoke(service_id, operation_id, input_value, ctx)

        self.assertEquals(None, method_result.output)
        self.assertEquals(expected_error_value, method_result.error)

    def _test_operation_not_found(self, interface_name, method_name, error, message_id, *args):
        ctx = ExecutionContext()
        expected_msg = message_factory.get_message(message_id, *args)
        expected_error_value = make_error_value_from_msgs(error, expected_msg)

        method_result = self.local_provider.invoke(
                interface_name,
                method_name,
                StructValue(),
                ctx)

        self.assertEquals(None, method_result.output)
        self.assertEquals(expected_error_value, method_result.error)

    def test_add_duplicate_interface(self):
        mockup_api_interface = MockupApiInterface()
        self.local_provider = LocalProvider()
        self.local_provider.add_interface(mockup_api_interface)
        self.assertRaises(Exception,
                          self.local_provider.add_interface,
                          mockup_api_interface)

    def test_register_duplicate_interface(self):
        self.local_provider = LocalProvider()
        properties = ProviderConfig()
        properties.cfg = configparser.SafeConfigParser()
        properties.cfg.add_section(Sections.ENDPOINT)
        properties.cfg.set(Sections.ENDPOINT,
                       'local.interfaces',
                       'test.vmware.vapi.provider.test_local,' +
                       'test.vmware.vapi.provider.test_local')
        self.assertRaises(Exception,
                          self.local_provider.register_by_properties,
                          properties)

    def test_report_declared_error(self):
        self._test_method_failure(report_declared_error, not_found_error)

    def test_report_undeclared_error(self):
        msg = message_factory.get_message(
                'vapi.method.status.errors.invalid',
                not_found_error.name,
                str(method_id_dict[report_undeclared_error].get_name()))
        expected_error = make_error_value_from_msgs(
            internal_server_error_def, *([msg, _msg]))
        self._test_method_failure(report_undeclared_error, expected_error)

    def test_raise_python_exception(self):
        self._test_method_failure(
            raise_python_exception,
            internal_server_error_def,
            'vapi.method.invoke.exception',
            str(RuntimeError()))

    def test_invalid_input(self):
        ctx = ExecutionContext()
        expected_msg = message_factory.get_message('vapi.method.input.invalid')
        expected_error_value = make_error_value_from_msgs(
            invalid_argument_def, expected_msg)

        method_result = self.local_provider.invoke(
                service_id=raise_python_exception_id.get_interface_identifier().get_name(),
                operation_id=raise_python_exception_id.get_name(),
                input_value=IntegerValue(),
                ctx=ctx)

        self.assertEquals(None, method_result.output)
        self.assertEquals(expected_error_value, method_result.error)

    def test_input_validation_failure(self):
        ctx = ExecutionContext()
        expected_msg0 = message_factory.get_message(
                'vapi.data.structure.field.invalid', 'param',
                OPERATION_INPUT)
        expected_msg1 = message_factory.get_message(
                'vapi.data.validate.mismatch', 'Integer', 'Structure')
        expected_error_value = make_error_value_from_msgs(
                invalid_argument_def,
                expected_msg0, expected_msg1)

        service_id = raise_python_exception_id.get_interface_identifier().get_name()
        operation_id = raise_python_exception_id.get_name()
        method_def = self.introspection.get_method(service_id, operation_id)
        input_value = method_def.get_input_definition().new_value()
        input_value.set_field(param_name, StructValue())
        method_result = self.local_provider.invoke(
            service_id=service_id,
            operation_id=operation_id,
            input_value=input_value,
            ctx=ctx)

        self.assertEquals(None, method_result.output)
        self.assertEquals(expected_error_value, method_result.error)

    def test_output_validation_failure(self):
        self._test_method_failure(
            return_invalid_output,
            internal_server_error_def,
            'vapi.data.validate.mismatch',
            'Void',
            'Structure')

    def test_missing_interface(self):
        interface_name = 'bogus_interface'
        method_name = 'test_method'

        self._test_operation_not_found(
            interface_name,
            method_name,
            operation_not_found_def,
            'vapi.method.input.invalid.interface',
            interface_name)

    def test_missing_method(self):
        interface_name = interface_id.get_name()
        method_name = 'bogus_method'

        self._test_operation_not_found(
            interface_name,
            method_name,
            operation_not_found_def,
            'vapi.method.input.invalid.method',
            method_name)

    def test_introspection_operation_get(self):
        ctx = ExecutionContext()
        input_val = StructValue(OPERATION_INPUT)
        input_val.set_field('service_id', StringValue('mockup_interface'))
        input_val.set_field('operation_id', StringValue('mock'))
        actual_output = self.local_provider.invoke(
            'com.vmware.vapi.std.introspection.operation', 'get', input_val, ctx)
        expected_output = StructValue(name='com.vmware.vapi.std.introspection.operation.info')
        input_def_value = StructValue('com.vmware.vapi.std.introspection.operation.data_definition')
        input_def_value.set_field('fields', OptionalValue(ListValue(values=[])))
        input_def_value.set_field('element_definition', OptionalValue())
        input_def_value.set_field('type', StringValue('STRUCTURE'))
        input_def_value.set_field('name', OptionalValue(StringValue(OPERATION_INPUT)))
        expected_output.set_field('input_definition', input_def_value)
        output_def_value = StructValue('com.vmware.vapi.std.introspection.operation.data_definition')
        output_def_value.set_field('fields', OptionalValue())
        output_def_value.set_field('element_definition', OptionalValue())
        output_def_value.set_field('type', StringValue('VOID'))
        output_def_value.set_field('name', OptionalValue())
        expected_output.set_field('output_definition', output_def_value)
        expected_output.set_field('error_definitions', error_values)
        self.assertEqual(actual_output.output, expected_output)

    def test_success(self):
        ctx = ExecutionContext()
        service_id = interface_id.get_name()
        operation_id = mock_definition

        method_def = self.introspection.get_method(service_id, operation_id)
        input_value = method_def.get_input_definition().new_value()
        input_value.set_field(param_name, IntegerValue(10))
        method_result = self.local_provider.invoke(
            service_id, operation_id, input_value, ctx)
        self.assertTrue(method_result.success())
        self.assertEqual(method_result.output, VoidValue())

    def test_success_2(self):
        ctx = ExecutionContext()
        service_id = interface_id.get_name()
        operation_id = mock_definition

        input_value = StructValue(OPERATION_INPUT)
        input_value.set_field(param_name, IntegerValue(10))
        method_result = self.local_provider.invoke(
            service_id, operation_id, input_value, ctx)
        self.assertTrue(method_result.success())
        self.assertEqual(method_result.output, VoidValue())


if __name__ == "__main__":
   unittest.main()
