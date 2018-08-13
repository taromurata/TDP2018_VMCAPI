# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.logging.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.logging_client`` module provides classes for
managing log forwarding in the appliance. The module is available starting in
vSphere 6.5.

"""

__author__ = 'VMware, Inc.'
__docformat__ = 'restructuredtext en'

import sys

from vmware.vapi.bindings import type
from vmware.vapi.bindings.converter import TypeConverter
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.error import VapiError
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.stub import (
    ApiInterfaceStub, StubFactoryBase, VapiInterface)
from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.data.validator import (UnionValidator, HasFieldsOfValidator)
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.constants import TaskType
from vmware.vapi.lib.rest import OperationRestMetadata


class Forwarding(VapiInterface):
    """
    The ``Forwarding`` class provides methods to manage forwarding of log
    messages to remote logging servers. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ForwardingStub)

    class Protocol(Enum):
        """
        The ``Forwarding.Protocol`` class defines transport protocols for outbound
        log messages. This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        TLS = None
        """
        Log messages will be forwarded to the remote host by using the TLS
        protocol. This class attribute was added in vSphere API 6.7

        """
        UDP = None
        """
        Log messages will be forwarded to the remote host using the UDP protocol.
        This class attribute was added in vSphere API 6.7

        """
        TCP = None
        """
        Log messages will be forwarded to the remote host using the TCP protocol.
        This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Protocol` instance.
            """
            Enum.__init__(string)

    Protocol._set_values([
        Protocol('TLS'),
        Protocol('UDP'),
        Protocol('TCP'),
    ])
    Protocol._set_binding_type(type.EnumType(
        'com.vmware.appliance.logging.forwarding.protocol',
        Protocol))


    class Config(VapiStruct):
        """
        The ``Forwarding.Config`` class defines the configuration for log message
        forwarding to remote logging servers. This class was added in vSphere API
        6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hostname=None,
                     port=None,
                     protocol=None,
                    ):
            """
            :type  hostname: :class:`str`
            :param hostname: FQDN or IP address of the logging server to which messages are
                forwarded. This attribute was added in vSphere API 6.7
            :type  port: :class:`long`
            :param port: The port on which the remote logging server is listening for
                forwarded log messages. This attribute was added in vSphere API 6.7
            :type  protocol: :class:`Forwarding.Protocol`
            :param protocol: Transport protocol used to forward log messages. This attribute was
                added in vSphere API 6.7
            """
            self.hostname = hostname
            self.port = port
            self.protocol = protocol
            VapiStruct.__init__(self)

    Config._set_binding_type(type.StructType(
        'com.vmware.appliance.logging.forwarding.config', {
            'hostname': type.StringType(),
            'port': type.IntegerType(),
            'protocol': type.ReferenceType(__name__, 'Forwarding.Protocol'),
        },
        Config,
        False,
        None))


    class ConnectionStatus(VapiStruct):
        """


        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'state',
                {
                    'DOWN' : [('message', False)],
                    'UP' : [],
                    'UNKNOWN' : [],
                }
            ),
        ]



        def __init__(self,
                     hostname=None,
                     state=None,
                     message=None,
                    ):
            """
            :type  hostname: :class:`str`
            :param hostname: FQDN or IP address of the configured remote logging servers. This
                attribute was added in vSphere API 6.7
            :type  state: :class:`Forwarding.ConnectionStatus.State`
            :param state: State of the configured remote logging server. This attribute was
                added in vSphere API 6.7
            :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param message: Message associated with the state of the configured remote logging
                server. This attribute was added in vSphere API 6.7
                If None, there is no message to be shown.
            """
            self.hostname = hostname
            self.state = state
            self.message = message
            VapiStruct.__init__(self)

        class State(Enum):
            """
            The ``Forwarding.ConnectionStatus.State`` class defines the state values
            that a remote logging server can be in. This enumeration was added in
            vSphere API 6.7

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            UP = None
            """
            The remote logging server is reachable. This class attribute was added in
            vSphere API 6.7

            """
            DOWN = None
            """
            The remote logging server is not reachable. This class attribute was added
            in vSphere API 6.7

            """
            UNKNOWN = None
            """
            The status of remote logging server is unknown. This class attribute was
            added in vSphere API 6.7

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`State` instance.
                """
                Enum.__init__(string)

        State._set_values([
            State('UP'),
            State('DOWN'),
            State('UNKNOWN'),
        ])
        State._set_binding_type(type.EnumType(
            'com.vmware.appliance.logging.forwarding.connection_status.state',
            State))

    ConnectionStatus._set_binding_type(type.StructType(
        'com.vmware.appliance.logging.forwarding.connection_status', {
            'hostname': type.StringType(),
            'state': type.ReferenceType(__name__, 'Forwarding.ConnectionStatus.State'),
            'message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        ConnectionStatus,
        False,
        None))



    def test(self,
             send_test_message=None,
             ):
        """
        Validates the current log forwarding configuration by checking the
        liveness of the remote machine and optionally sending a test diagnostic
        log message from the appliance to all configured logging servers to
        allow manual end-to-end validation. The message that is sent is: "This
        is a diagnostic log test message from vCenter Server.". This method was
        added in vSphere API 6.7

        :type  send_test_message: :class:`bool` or ``None``
        :param send_test_message: Flag specifying whether a default test message should be sent to
            the configured logging servers.
            If None, no test message will be sent to the configured remote
            logging servers.
        :rtype: :class:`list` of :class:`Forwarding.ConnectionStatus`
        :return: Information about the status of the connection to each of the
            remote logging servers.
        """
        return self._invoke('test',
                            {
                            'send_test_message': send_test_message,
                            })

    def set(self,
            cfg_list,
            ):
        """
        Sets the configuration for forwarding log messages to remote log
        servers. This method was added in vSphere API 6.7

        :type  cfg_list: :class:`list` of :class:`Forwarding.Config`
        :param cfg_list: The cfgList is a list of Config structure that contains the log
            message forwarding rules in terms of the host, port, protocol of
            the log message.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if an invalid configuration is provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the number of configurations exceeds the maximum number of
            supported configurations.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if there is any internal error during the execution of the
            operation.
        """
        return self._invoke('set',
                            {
                            'cfg_list': cfg_list,
                            })

    def get(self):
        """
        Returns the configuration for forwarding log messages to remote logging
        servers. This method was added in vSphere API 6.7


        :rtype: :class:`list` of :class:`Forwarding.Config`
        :return: Information about the configuration for forwarding log messages to
            remote logging servers.
        """
        return self._invoke('get', None)
class _ForwardingStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'send_test_message': type.OptionalType(type.BooleanType()),
        })
        test_error_dict = {}
        test_input_value_validator_list = [
        ]
        test_output_validator_list = [
        ]
        test_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/logging/forwarding?action=test',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'cfg_list': type.ListType(type.ReferenceType(__name__, 'Forwarding.Config')),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/logging/forwarding',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {}
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/logging/forwarding',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'test': {
                'input_type': test_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Forwarding.ConnectionStatus')),
                'errors': test_error_dict,
                'input_value_validator_list': test_input_value_validator_list,
                'output_validator_list': test_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Forwarding.Config')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'test': test_rest_metadata,
            'set': set_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.logging.forwarding',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Forwarding': Forwarding,
    }

