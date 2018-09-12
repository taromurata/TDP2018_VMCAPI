# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.networking.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.networking_client`` module provides classes for
managing network configuration of the appliance. The module is available
starting in vSphere 6.5.

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


class Proxy(VapiInterface):
    """
    The ``Proxy`` class provides methods Proxy configuration. This class was
    added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProxyStub)

    class Protocol(Enum):
        """
        ``Proxy.Protocol`` class defines the protocols for which proxying is
        supported. This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        HTTP = None
        """
        Proxy configuration for http. This class attribute was added in vSphere API
        6.7

        """
        HTTPS = None
        """
        Proxy configuration for https. This class attribute was added in vSphere
        API 6.7

        """
        FTP = None
        """
        Proxy configuration for ftp. This class attribute was added in vSphere API
        6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Protocol` instance.
            """
            Enum.__init__(string)

    Protocol._set_values([
        Protocol('HTTP'),
        Protocol('HTTPS'),
        Protocol('FTP'),
    ])
    Protocol._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.proxy.protocol',
        Protocol))


    class ServerStatus(Enum):
        """
        ``Proxy.ServerStatus`` class defines the status of the server associated
        with the test run. This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SERVER_REACHABLE = None
        """
        Server is reachable. This class attribute was added in vSphere API 6.7

        """
        SERVER_UNREACHABLE = None
        """
        Server is unreachable. This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ServerStatus` instance.
            """
            Enum.__init__(string)

    ServerStatus._set_values([
        ServerStatus('SERVER_REACHABLE'),
        ServerStatus('SERVER_UNREACHABLE'),
    ])
    ServerStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.proxy.server_status',
        ServerStatus))


    class Config(VapiStruct):
        """
        The ``Proxy.Config`` class defines proxy configuration. This class was
        added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     server=None,
                     port=None,
                     username=None,
                     password=None,
                     enabled=None,
                    ):
            """
            :type  server: :class:`str`
            :param server: Hostname or IP address of the proxy server. This attribute was
                added in vSphere API 6.7
            :type  port: :class:`long`
            :param port: Port to connect to the proxy server. In a 'get' call, indicates the
                port connected to the proxy server. In a 'set' call, specifies the
                port to connect to the proxy server. A value of -1 indicates the
                default port. This attribute was added in vSphere API 6.7
            :type  username: :class:`str` or ``None``
            :param username: Username for proxy server. This attribute was added in vSphere API
                6.7
                Only :class:`set` if proxy requires username.
            :type  password: :class:`str` or ``None``
            :param password: Password for proxy server. This attribute was added in vSphere API
                6.7
                Only :class:`set` if proxy requires password.
            :type  enabled: :class:`bool`
            :param enabled: In the result of the ``#get`` and ``#list`` methods this attribute
                indicates whether proxying is enabled for a particular protocol. In
                the input to the ``test`` and ``set`` methods this attribute
                specifies whether proxying should be enabled for a particular
                protocol. This attribute was added in vSphere API 6.7
            """
            self.server = server
            self.port = port
            self.username = username
            self.password = password
            self.enabled = enabled
            VapiStruct.__init__(self)

    Config._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.proxy.config', {
            'server': type.StringType(),
            'port': type.IntegerType(),
            'username': type.OptionalType(type.StringType()),
            'password': type.OptionalType(type.SecretType()),
            'enabled': type.BooleanType(),
        },
        Config,
        False,
        None))


    class TestResult(VapiStruct):
        """
        The ``Proxy.TestResult`` class contains information about the test
        operation done on a proxy server. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     message=None,
                    ):
            """
            :type  status: :class:`Proxy.ServerStatus`
            :param status: Status of the proxy server indicating whether the proxy server is
                reachable. This attribute was added in vSphere API 6.7
            :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param message: Message associated with status. This attribute was added in vSphere
                API 6.7
            """
            self.status = status
            self.message = message
            VapiStruct.__init__(self)

    TestResult._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.proxy.test_result', {
            'status': type.ReferenceType(__name__, 'Proxy.ServerStatus'),
            'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        TestResult,
        False,
        None))



    def test(self,
             host,
             protocol,
             config,
             ):
        """
        Tests a proxy configuration by testing the connection to the proxy
        server and test host. This method was added in vSphere API 6.7

        :type  host: :class:`str`
        :param host: A hostname, IPv4 or Ipv6 address.
        :type  protocol: :class:`str`
        :param protocol: Protocol whose proxy is to be tested.
        :type  config: :class:`Proxy.Config`
        :param config: Proxy configuration to test.
        :rtype: :class:`Proxy.TestResult`
        :return: Status of proxy settings.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('test',
                            {
                            'host': host,
                            'protocol': protocol,
                            'config': config,
                            })

    def set(self,
            protocol,
            config,
            ):
        """
        Configures which proxy server to use for the specified protocol. This
        operation sets environment variables for using proxy. In order for this
        configuration to take effect a logout / service restart is required.
        This method was added in vSphere API 6.7

        :type  protocol: :class:`str`
        :param protocol: The protocol for which proxy should be set.
        :type  config: :class:`Proxy.Config`
        :param config: Proxy configuration for the specific protocol.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('set',
                            {
                            'protocol': protocol,
                            'config': config,
                            })

    def delete(self,
               protocol,
               ):
        """
        Deletes a proxy configuration for a specific protocol. This method was
        added in vSphere API 6.7

        :type  protocol: :class:`str`
        :param protocol: ID whose proxy is to be deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('delete',
                            {
                            'protocol': protocol,
                            })

    def list(self):
        """
        Gets proxy configuration for all configured protocols. This method was
        added in vSphere API 6.7


        :rtype: :class:`dict` of :class:`Proxy.Protocol` and :class:`Proxy.Config`
        :return: Proxy configuration for all configured protocols.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('list', None)

    def get(self,
            protocol,
            ):
        """
        Gets the proxy configuration for a specific protocol. This method was
        added in vSphere API 6.7

        :type  protocol: :class:`str`
        :param protocol: The protocol whose proxy configuration is requested.
        :rtype: :class:`Proxy.Config`
        :return: Proxy configuration for a specific protocol.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('get',
                            {
                            'protocol': protocol,
                            })
class NoProxy(VapiInterface):
    """
    The ``NoProxy`` class provides methods to configure a connection that does
    not need a proxy. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NoProxyStub)


    def set(self,
            servers,
            ):
        """
        Sets servers for which no proxy configuration should be applied. This
        operation sets environment variables. In order for this operation to
        take effect, a logout from appliance or a service restart is required.
        If IPv4 is enabled, "127.0.0.1" and "localhost" will always bypass the
        proxy (even if they are not explicitly configured). This method was
        added in vSphere API 6.7

        :type  servers: :class:`list` of :class:`str`
        :param servers: List of strings representing servers to bypass proxy. A server can
            be a FQDN, IP address, FQDN:port or IP:port combinations.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('set',
                            {
                            'servers': servers,
                            })

    def get(self):
        """
        Returns servers for which no proxy configuration will be applied. This
        method was added in vSphere API 6.7


        :rtype: :class:`list` of :class:`str`
        :return: List of servers for which no proxy configuration will be applied.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('get', None)
class Interfaces(VapiInterface):
    """
    ``Interfaces`` class provides methods Provides information about network
    interface.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _InterfacesStub)

    class InterfaceStatus(Enum):
        """
        ``Interfaces.InterfaceStatus`` class Defines interface status

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        down = None
        """
        The interface is down.

        """
        up = None
        """
        The interface is up.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`InterfaceStatus` instance.
            """
            Enum.__init__(string)

    InterfaceStatus._set_values([
        InterfaceStatus('down'),
        InterfaceStatus('up'),
    ])
    InterfaceStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.interfaces.interface_status',
        InterfaceStatus))


    class InterfaceInfo(VapiStruct):
        """
        ``Interfaces.InterfaceInfo`` class Structure that defines properties and
        status of a network interface.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     status=None,
                     mac=None,
                     ipv4=None,
                     ipv6=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Interface name, for example, "nic0", "nic1".
            :type  status: :class:`Interfaces.InterfaceStatus`
            :param status: Interface status.
            :type  mac: :class:`str`
            :param mac: MAC address. For example 00:0C:29:94:BB:5A.
            :type  ipv4: :class:`com.vmware.appliance.networking.interfaces_client.Ipv4.Info` or ``None``
            :param ipv4: IPv4 Address information. This attribute was added in vSphere API
                6.7
                ipv4 This attribute will be None if IPv4 is not enabled.
            :type  ipv6: :class:`com.vmware.appliance.networking.interfaces_client.Ipv6.Info` or ``None``
            :param ipv6: IPv6 Address information. This attribute was added in vSphere API
                6.7
                ipv6 This attribute will be None if IPv6 is not enabled.
            """
            self.name = name
            self.status = status
            self.mac = mac
            self.ipv4 = ipv4
            self.ipv6 = ipv6
            VapiStruct.__init__(self)

    InterfaceInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.interface_info', {
            'name': type.StringType(),
            'status': type.ReferenceType(__name__, 'Interfaces.InterfaceStatus'),
            'mac': type.StringType(),
            'ipv4': type.OptionalType(type.ReferenceType('com.vmware.appliance.networking.interfaces_client', 'Ipv4.Info')),
            'ipv6': type.OptionalType(type.ReferenceType('com.vmware.appliance.networking.interfaces_client', 'Ipv6.Info')),
        },
        InterfaceInfo,
        False,
        None))



    def list(self):
        """
        Get list of available network interfaces, including those that are not
        yet configured.


        :rtype: :class:`list` of :class:`Interfaces.InterfaceInfo`
        :return: List of InterfaceInfo structures.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def get(self,
            interface_name,
            ):
        """
        Get information about a particular network interface.

        :type  interface_name: :class:`str`
        :param interface_name: Network interface, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :rtype: :class:`Interfaces.InterfaceInfo`
        :return: Network interface information.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified interface is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get',
                            {
                            'interface_name': interface_name,
                            })
class _ProxyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'host': type.StringType(),
            'protocol': type.StringType(),
            'config': type.ReferenceType(__name__, 'Proxy.Config'),
        })
        test_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        test_input_value_validator_list = [
        ]
        test_output_validator_list = [
        ]
        test_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/networking/proxy/{protocol}?action=test',
            path_variables={
                'protocol': 'protocol',
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'protocol': type.StringType(),
            'config': type.ReferenceType(__name__, 'Proxy.Config'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/networking/proxy/{protocol}',
            path_variables={
                'protocol': 'protocol',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'protocol': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/appliance/networking/proxy/{protocol}',
            path_variables={
                'protocol': 'protocol',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/proxy',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'protocol': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/proxy/{protocol}',
            path_variables={
                'protocol': 'protocol',
            },
            query_parameters={
            }
        )

        operations = {
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(__name__, 'Proxy.TestResult'),
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.ReferenceType(__name__, 'Proxy.Protocol'), type.ReferenceType(__name__, 'Proxy.Config')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Proxy.Config'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'test': test_rest_metadata,
            'set': set_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.proxy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NoProxyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'servers': type.ListType(type.StringType()),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/networking/noproxy',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/noproxy',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
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
                'output_type': type.ListType(type.StringType()),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'set': set_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.no_proxy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _InterfacesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/interfaces',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'interface_name': type.IdType(resource_types='com.vmware.appliance.networking.interfaces'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/networking/interfaces/{interface_name}',
            path_variables={
                'interface_name': 'interface_name',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Interfaces.InterfaceInfo')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Interfaces.InterfaceInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.interfaces',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Proxy': Proxy,
        'NoProxy': NoProxy,
        'Interfaces': Interfaces,
        'interfaces': 'com.vmware.appliance.networking.interfaces_client.StubFactory',
        'dns': 'com.vmware.appliance.networking.dns_client.StubFactory',
    }

