"""
Unit tests for Local Api Provider
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest

from vmware.vapi.core import (
    ApiInterface,
    MethodDefinition,
    MethodResult,
    InterfaceIdentifier,
    MethodIdentifier,
    InterfaceDefinition
    )
from vmware.vapi.data.definition import (
    StructDefinition,
    StringDefinition,
    OpaqueDefinition,
    VoidDefinition,
    BooleanDefinition,
    ErrorDefinition,
    )
from vmware.vapi.data.value import (
    BooleanValue,
    VoidValue,
    StructValue,
    ErrorValue,
    StringValue,
    OptionalValue,
    ListValue
    )
from vmware.vapi.message import Message
from vmware.vapi.core import ExecutionContext
from vmware.vapi.provider.local import LocalProvider
from vmware.vapi.provider.interposer import InterposerProvider, NotFound, InvalidArgument
from vmware.vapi.lib.constants import (MAP_ENTRY, OPERATION_INPUT)
from vmware.vapi.lib.std import make_std_error_def, make_error_value_from_msgs
from vmware.vapi.data.serializers.introspection import convert_data_def_to_data_value
from vmware.vapi.bindings.error import VapiError

import logging
logging.basicConfig()

### Data used by the mockup classes and the test methods
interface_name = 'com.vmware.pkg1.mockup_interface'
interface_id = InterfaceIdentifier(interface_name)

interface_name_2 = 'com.vmware.pkg2.mockup_interface'
interface_id_2 = InterfaceIdentifier(interface_name_2)

# Method names
mock_method_name = 'mockup_method'
pre_method_name = 'mockup_pre'
post_method_name = 'mockup_post'
veto_method_name = 'mockup_veto'

# Method identifiers
mock_method_id = MethodIdentifier(interface_id, mock_method_name)
pre_method_id = MethodIdentifier(interface_id, pre_method_name)
post_method_id = MethodIdentifier(interface_id, post_method_name)
veto_method_id = MethodIdentifier(interface_id, veto_method_name)

method_id_dict = {
    mock_method_name : mock_method_id,
    pre_method_name : pre_method_id,
    post_method_name : post_method_id,
    veto_method_name : veto_method_id,
}

input_def = StructDefinition(
    'input',
    [('service_name', StringDefinition()),
     ('operation_name', StringDefinition()),
     ('operation_input', OpaqueDefinition()),
    ]
)
mock_input_def = StructDefinition(
    'input',
    [('raise', BooleanDefinition())]
)
not_found_error_def = make_std_error_def('com.vmware.vapi.std.errors.not_found')
errors = [
    'com.vmware.vapi.std.errors.not_found',
    'com.vmware.vapi.std.errors.internal_server_error',
    'com.vmware.vapi.std.errors.invalid_argument',
    'com.vmware.vapi.std.errors.operation_not_found',
]
error_defs = [make_std_error_def(error) for error in errors]
error_values = ListValue([convert_data_def_to_data_value(error_def)
                          for error_def in error_defs])

class MockupApiInterface(ApiInterface):
    def __init__(self, interface_id):
        self._interface_id = interface_id
        self.counters = {}
        for name in [mock_method_name, pre_method_name,
                     post_method_name, veto_method_name]:
            self.counters[name] = 0

    def get_identifier(self):
        return self._interface_id

    def get_definition(self):
        return InterfaceDefinition(self._interface_id,
            [mock_method_id, pre_method_id, post_method_id, veto_method_id])

    def get_method_definition(self, method_id):
        name = method_id.get_name()
        if name == mock_method_name:
            input_ = mock_input_def
        else:
            input_ = input_def
        output = VoidDefinition()
        errors = [not_found_error_def]
        return MethodDefinition(method_id, input_, output, errors)

    def invoke(self, ctx, method_id, input_):
        name = method_id.get_name()
        self.counters[name] = self.counters.get(name, 0) + 1
        if name == veto_method_name:
            method_input = input_.get_field('operation_input')
            raise_error = method_input.get_field('raise')
            if raise_error.value:
                msg = Message('mockup.message.id', 'mockup error message')
                return MethodResult(error=make_error_value_from_msgs(
                    not_found_error_def, msg))
        return MethodResult(output=VoidValue())


class InterposerInfo(object):
    def __init__(self, service_name, operation_name, type_, packages):
        self.service_name = service_name
        self.operation_name = operation_name
        self.type = type_
        self.packages = packages


class TestInterposer(unittest.TestCase):

    def setUp(self):
        self.api_iface = MockupApiInterface(interface_id)
        self.api_iface_2 = MockupApiInterface(interface_id_2)
        provider = LocalProvider()
        provider.add_interface(self.api_iface)
        provider.add_interface(self.api_iface_2)

        self.provider = InterposerProvider(provider)

    def _invoke(self, raise_error=False):
        ctx = ExecutionContext()
        input_ = StructValue('input')
        input_.set_field('raise', BooleanValue(raise_error))
        return self.provider.invoke(
            interface_name, mock_method_name, input_, ctx)

    def test_pre_interposer(self):
        info = InterposerInfo(interface_name, pre_method_name,
                              'pre', ['com.vmware'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        self._invoke()
        # Verify if pre interposer was called
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)

        # remove interposer and verify it's not called anymore
        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 2)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)

    def test_post_interposer(self):
        info = InterposerInfo(interface_name, post_method_name,
                              'post', ['com.vmware'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        self._invoke()
        # Verify if post interposer was called
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(post_method_id.get_name()), 1)

        # remove interposer and verify it's not called anymore
        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 2)
        self.assertEqual(self.api_iface.counters.get(post_method_id.get_name()), 1)

    def test_veto_interposer_success(self):
        info = InterposerInfo(interface_name, veto_method_name,
                              'veto', ['com.vmware'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        result = self._invoke()
        # Verify if veto interposer was called
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 1)
        self.assertTrue(result.success())

        # remove interposer and verify it's not called anymore
        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 2)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 1)

    def test_veto_interposer_failure(self):
        info = InterposerInfo(interface_name, veto_method_name,
                              'veto', ['com.vmware'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        result = self._invoke(True)
        # Verify if veto interposer was called
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 0)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 1)
        self.assertFalse(result.success())

        # remove interposer and verify it's not called anymore
        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 1)

    def test_interposer_all_interposers(self):
        info = InterposerInfo(interface_name, pre_method_name,
                              'pre', ['com.vmware'])
        pre_interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(pre_interposer_id), info)
        info = InterposerInfo(interface_name, post_method_name,
                              'post', ['com.vmware'])
        post_interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(post_interposer_id), info)
        info = InterposerInfo(interface_name, veto_method_name,
                              'veto', ['com.vmware'])
        veto_interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(veto_interposer_id), info)

        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(post_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 1)

        self._invoke(True)
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(post_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(veto_method_id.get_name()), 2)

        self.provider.remove(pre_interposer_id)
        self.provider.remove(post_interposer_id)
        self.provider.remove(veto_interposer_id)

    def test_interposer_invalid_method(self):
        info = InterposerInfo('mock', 'invalid',
                              'pre', ['com.vmware'])
        self.assertRaises(VapiError,
                          self.provider.add,
                          info)

    def test_interposer_invalid_type(self):
        info = InterposerInfo(interface_name, pre_method_name,
                              'invalid', [])
        self.assertRaises(InvalidArgument,
                          self.provider.add,
                          info)

    def test_interposer_specific_pkg_pos(self):
        info = InterposerInfo(interface_name, pre_method_name,
                              'pre', ['com.vmware.pkg1'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)

        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 2)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 1)

    def test_interposer_specific_pkg_neg(self):
        info = InterposerInfo(interface_name, pre_method_name,
                              'pre', ['com.vmware.pkg2'])
        interposer_id = self.provider.add(info)
        self.assertEqual(self.provider.get(interposer_id), info)

        self._invoke()
        # Verify if pre interposer was not called
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 1)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 0)

        self.provider.remove(interposer_id)
        self.assertRaises(NotFound, self.provider.get, interposer_id)
        self._invoke()
        self.assertEqual(self.api_iface.counters.get(mock_method_id.get_name()), 2)
        self.assertEqual(self.api_iface.counters.get(pre_method_id.get_name()), 0)

    def test_introspection_operation_get(self):
        ctx = ExecutionContext()
        input_val = StructValue(OPERATION_INPUT)
        input_val.set_field('service_id', StringValue('com.vmware.pkg1.mockup_interface'))
        input_val.set_field('operation_id', StringValue('mockup_method'))

        expected_output = StructValue(
            name='com.vmware.vapi.std.introspection.operation.info')
        input_param_def_value = StructValue(
            'com.vmware.vapi.std.introspection.operation.data_definition')
        input_param_def_value.set_field('element_definition', OptionalValue())
        input_param_def_value.set_field('type', StringValue('BOOLEAN'))
        input_param_def_value.set_field('name', OptionalValue())
        input_param_def_value.set_field('fields', OptionalValue())
        input_param_value = StructValue(MAP_ENTRY)
        input_param_value.set_field('value', input_param_def_value)
        input_param_value.set_field('key', StringValue(value='raise'))
        input_def_value = StructValue('com.vmware.vapi.std.introspection.operation.data_definition')
        input_def_value.set_field('fields', OptionalValue(ListValue([input_param_value])))
        input_def_value.set_field('element_definition', OptionalValue())
        input_def_value.set_field('type', StringValue('STRUCTURE'))
        input_def_value.set_field('name', OptionalValue(StringValue('input')))
        expected_output.set_field('input_definition', input_def_value)
        output_def_value = StructValue('com.vmware.vapi.std.introspection.operation.data_definition')
        output_def_value.set_field('fields', OptionalValue())
        output_def_value.set_field('element_definition', OptionalValue())
        output_def_value.set_field('type', StringValue('VOID'))
        output_def_value.set_field('name', OptionalValue())
        expected_output.set_field('output_definition', output_def_value)
        expected_output.set_field('error_definitions', error_values)
        actual_output = self.provider.invoke(
            'com.vmware.vapi.std.introspection.operation',
            'get', input_val, ctx)
        self.assertEqual(actual_output.output, expected_output)


if __name__ == "__main__":
   unittest.main()
