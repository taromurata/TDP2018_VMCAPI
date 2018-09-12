"""
Introspection services
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

from com.vmware.vapi.std.introspection_client import Operation
from vmware.vapi.core import (
    InterfaceIdentifier, MethodIdentifier, MethodDefinition)
from vmware.vapi.data.serializers.introspection import (
    convert_data_value_to_data_def)
from vmware.vapi.lib.log import get_vapi_logger
from vmware.vapi.stdlib.client.factories import StubConfigurationFactory

logger = get_vapi_logger(__name__)


localizable_message_def = Operation.DataDefinition(
    type=Operation.DataDefinition.DataType.STRUCTURE,
    name='com.vmware.vapi.std.localizable_message',
    fields={
        'default_message': Operation.DataDefinition(
            type=Operation.DataDefinition.DataType.STRING
        ),
        'args': Operation.DataDefinition(
            type=Operation.DataDefinition.DataType.LIST,
            element_definition=Operation.DataDefinition(
                type=Operation.DataDefinition.DataType.STRING
            )
        ),
        'id': Operation.DataDefinition(
            type=Operation.DataDefinition.DataType.STRING
        )
    }
)


def make_introspection_error_def(error_name):
    """
    Create an instance of
    :class:`com.vmware.vapi.std.introspection_client.Operation.DataDefinition` that
    represents the standard error specified

    :type  error_name: :class:`str`
    :param error_name: Fully qualified error name of one of the vAPI standard errors
    :rtype: :class:`com.vmware.vapi.std.introspection_client.Operation.DataDefinition`
    :return: Error definition instance for the given error name
    """
    return Operation.DataDefinition(
        type=Operation.DataDefinition.DataType.ERROR,
        name=error_name,
        fields={
            'messages': Operation.DataDefinition(
                type=Operation.DataDefinition.DataType.LIST,
                element_definition=localizable_message_def
            ),
            'data': Operation.DataDefinition(
                type=Operation.DataDefinition.DataType.OPTIONAL,
                element_definition=Operation.DataDefinition(
                    type=Operation.DataDefinition.DataType.DYNAMIC_STRUCTURE)
            )
        }
    )


class IntrospectableApiProvider(object):
    """
    Helper class for invoking the 'get' operation in the service
    'com.vmware.vapi.std.introspection.Operation'
    """
    def __init__(self, connector):
        """
        Initialize IntrospectableApiProvider

        :type  connector: :class:`vmware.vapi.protocol.client.connector.Connector`
        :param Connector: Protocol connector to use for operation invocations
        """
        stub_config = StubConfigurationFactory.new_std_configuration(connector)
        self._operation = Operation(stub_config)

    def get_method(self, service_id, operation_id):
        """
        Get method definition for the specified operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`vmware.vapi.core.MethodDefinition`
        :return: Method definition of the specified operation
        """
        info = self._operation.get(service_id=service_id, operation_id=operation_id)
        input_def = convert_data_value_to_data_def(
            info.input_definition.get_struct_value())
        output_def = convert_data_value_to_data_def(
            info.output_definition.get_struct_value())
        error_defs = [convert_data_value_to_data_def(error_def.get_struct_value())
                      for error_def in info.error_definitions]
        interface_id = InterfaceIdentifier(service_id)
        method_id = MethodIdentifier(interface_id, operation_id)
        method_definition = MethodDefinition(method_id,
                                             input_def,
                                             output_def,
                                             error_defs)
        return method_definition
