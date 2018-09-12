# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.networking.dns.
#---------------------------------------------------------------------------

"""


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


class Domains(VapiInterface):
    """
    ``Domains`` class provides methods DNS search domains.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DomainsStub)


    def add(self,
            domain,
            ):
        """
        Add domain to DNS search domains.

        :type  domain: :class:`str`
        :param domain: Domain to add.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'domain': domain,
                            })

    def set(self,
            domains,
            ):
        """
        Set DNS search domains.

        :type  domains: :class:`list` of :class:`str`
        :param domains: List of domains.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'domains': domains,
                            })

    def list(self):
        """
        Get list of DNS search domains.


        :rtype: :class:`list` of :class:`str`
        :return: List of domains.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)
class Hostname(VapiInterface):
    """
    ``Hostname`` class provides methods Performs operations on Fully Qualified
    Doman Name.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HostnameStub)

    class TestStatus(Enum):
        """
        ``Hostname.TestStatus`` class Health indicator

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        In case data has more than one test, this indicates not all tests were
        successful

        """
        green = None
        """
        All tests were successful for given data

        """
        red = None
        """
        All tests failed for given data

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`TestStatus` instance.
            """
            Enum.__init__(string)

    TestStatus._set_values([
        TestStatus('orange'),
        TestStatus('green'),
        TestStatus('red'),
    ])
    TestStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.dns.hostname.test_status',
        TestStatus))


    class MessageStatus(Enum):
        """
        ``Hostname.MessageStatus`` class Individual test result

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        failure = None
        """
        message indicates the test failed.

        """
        success = None
        """
        message indicates that the test was successful.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`MessageStatus` instance.
            """
            Enum.__init__(string)

    MessageStatus._set_values([
        MessageStatus('failure'),
        MessageStatus('success'),
    ])
    MessageStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.dns.hostname.message_status',
        MessageStatus))


    class Message(VapiStruct):
        """
        ``Hostname.Message`` class Test result and message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     message=None,
                     result=None,
                    ):
            """
            :type  message: :class:`str`
            :param message: message
            :type  result: :class:`Hostname.MessageStatus`
            :param result: result of the test
            """
            self.message = message
            self.result = result
            VapiStruct.__init__(self)

    Message._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.dns.hostname.message', {
            'message': type.StringType(),
            'result': type.ReferenceType(__name__, 'Hostname.MessageStatus'),
        },
        Message,
        False,
        None))


    class TestStatusInfo(VapiStruct):
        """
        ``Hostname.TestStatusInfo`` class Overall test result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Hostname.TestStatus`
            :param status: Overall status of tests run.
            :type  messages: :class:`list` of :class:`Hostname.Message`
            :param messages: messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    TestStatusInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.dns.hostname.test_status_info', {
            'status': type.ReferenceType(__name__, 'Hostname.TestStatus'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Hostname.Message')),
        },
        TestStatusInfo,
        False,
        None))



    def test(self,
             name,
             ):
        """
        Test the Fully Qualified Domain Name.

        :type  name: :class:`str`
        :param name: FQDN.
        :rtype: :class:`Hostname.TestStatusInfo`
        :return: FQDN status
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test',
                            {
                            'name': name,
                            })

    def set(self,
            name,
            ):
        """
        Set the Fully Qualified Domain Name.

        :type  name: :class:`str`
        :param name: FQDN.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'name': name,
                            })

    def get(self):
        """
        Get the Fully Qualified Doman Name.


        :rtype: :class:`str`
        :return: FQDN.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Servers(VapiInterface):
    """
    ``Servers`` class provides methods DNS server configuration.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServersStub)

    class DNSServerMode(Enum):
        """
        ``Servers.DNSServerMode`` class Describes DNS Server source (DHCP,static)

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        dhcp = None
        """
        DNS address is automatically assigned by a DHCP server.

        """
        is_static = None
        """
        DNS address is static.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DNSServerMode` instance.
            """
            Enum.__init__(string)

    DNSServerMode._set_values([
        DNSServerMode('dhcp'),
        DNSServerMode('is_static'),
    ])
    DNSServerMode._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.dns.servers.DNS_server_mode',
        DNSServerMode))


    class TestStatus(Enum):
        """
        ``Servers.TestStatus`` class Health indicator

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        In case data has more than one test, this indicates not all tests were
        successful

        """
        green = None
        """
        All tests were successful for given data

        """
        red = None
        """
        All tests failed for given data

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`TestStatus` instance.
            """
            Enum.__init__(string)

    TestStatus._set_values([
        TestStatus('orange'),
        TestStatus('green'),
        TestStatus('red'),
    ])
    TestStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.dns.servers.test_status',
        TestStatus))


    class MessageStatus(Enum):
        """
        ``Servers.MessageStatus`` class Individual test result

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        failure = None
        """
        message indicates the test failed.

        """
        success = None
        """
        message indicates that the test was successful.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`MessageStatus` instance.
            """
            Enum.__init__(string)

    MessageStatus._set_values([
        MessageStatus('failure'),
        MessageStatus('success'),
    ])
    MessageStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.dns.servers.message_status',
        MessageStatus))


    class DNSServerConfig(VapiStruct):
        """
        ``Servers.DNSServerConfig`` class This structure represents the
        configuration state used to determine DNS servers.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     mode=None,
                     servers=None,
                    ):
            """
            :type  mode: :class:`Servers.DNSServerMode`
            :param mode: Define how to determine the DNS servers. Leave the servers argument
                empty if the mode argument is "DHCP". Set the servers argument to a
                comma-separated list of DNS servers if the mode argument is
                "static". The DNS server are assigned from the specified list.
            :type  servers: :class:`list` of :class:`str`
            :param servers: List of the currently used DNS servers.
            """
            self.mode = mode
            self.servers = servers
            VapiStruct.__init__(self)

    DNSServerConfig._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.dns.servers.DNS_server_config', {
            'mode': type.ReferenceType(__name__, 'Servers.DNSServerMode'),
            'servers': type.ListType(type.StringType()),
        },
        DNSServerConfig,
        False,
        None))


    class Message(VapiStruct):
        """
        ``Servers.Message`` class Test result and message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     message=None,
                     result=None,
                    ):
            """
            :type  message: :class:`str`
            :param message: message
            :type  result: :class:`Servers.MessageStatus`
            :param result: result of the test
            """
            self.message = message
            self.result = result
            VapiStruct.__init__(self)

    Message._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.dns.servers.message', {
            'message': type.StringType(),
            'result': type.ReferenceType(__name__, 'Servers.MessageStatus'),
        },
        Message,
        False,
        None))


    class TestStatusInfo(VapiStruct):
        """
        ``Servers.TestStatusInfo`` class Overall test result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Servers.TestStatus`
            :param status: Overall status of tests run.
            :type  messages: :class:`list` of :class:`Servers.Message`
            :param messages: messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    TestStatusInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.dns.servers.test_status_info', {
            'status': type.ReferenceType(__name__, 'Servers.TestStatus'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Servers.Message')),
        },
        TestStatusInfo,
        False,
        None))



    def test(self,
             servers,
             ):
        """
        Test if dns servers are reachable.

        :type  servers: :class:`list` of :class:`str`
        :param servers: DNS servers.
        :rtype: :class:`Servers.TestStatusInfo`
        :return: DNS reacable status
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('test',
                            {
                            'servers': servers,
                            })

    def add(self,
            server,
            ):
        """
        Add a DNS server. This method fails if mode argument is "dhcp"

        :type  server: :class:`str`
        :param server: DNS server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('add',
                            {
                            'server': server,
                            })

    def set(self,
            config,
            ):
        """
        Set the DNS server configuration. If you set the mode argument to
        "DHCP", a DHCP refresh is forced.

        :type  config: :class:`Servers.DNSServerConfig`
        :param config: DNS server configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'config': config,
                            })

    def get(self):
        """
        Get DNS server configuration.


        :rtype: :class:`Servers.DNSServerConfig`
        :return: DNS server configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class _DomainsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'domain': type.StringType(),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/networking/dns/domains',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'domains': type.ListType(type.StringType()),
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
            url_template='/appliance/networking/dns/domains',
            path_variables={
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
            url_template='/appliance/networking/dns/domains',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'add': {
                'input_type': add_input_type,
                'output_type': type.VoidType(),
                'errors': add_error_dict,
                'input_value_validator_list': add_input_value_validator_list,
                'output_validator_list': add_output_validator_list,
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.StringType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'add': add_rest_metadata,
            'set': set_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.dns.domains',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _HostnameStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'name': type.StringType(),
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
            url_template='/appliance/networking/dns/hostname/test',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'name': type.StringType(),
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
            url_template='/appliance/networking/dns/hostname',
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
            url_template='/appliance/networking/dns/hostname',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(__name__, 'Hostname.TestStatusInfo'),
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
                'output_type': type.StringType(),
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
            self, iface_name='com.vmware.appliance.networking.dns.hostname',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ServersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for test operation
        test_input_type = type.StructType('operation-input', {
            'servers': type.ListType(type.StringType()),
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
            url_template='/appliance/networking/dns/servers/test',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'server': type.StringType(),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/networking/dns/servers',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'config': type.ReferenceType(__name__, 'Servers.DNSServerConfig'),
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
            url_template='/appliance/networking/dns/servers',
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
            url_template='/appliance/networking/dns/servers',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'test': {
                'input_type': test_input_type,
                'output_type': type.ReferenceType(__name__, 'Servers.TestStatusInfo'),
                'errors': test_error_dict,
                'input_value_validator_list': test_input_value_validator_list,
                'output_validator_list': test_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'add': {
                'input_type': add_input_type,
                'output_type': type.VoidType(),
                'errors': add_error_dict,
                'input_value_validator_list': add_input_value_validator_list,
                'output_validator_list': add_output_validator_list,
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
                'output_type': type.ReferenceType(__name__, 'Servers.DNSServerConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'test': test_rest_metadata,
            'add': add_rest_metadata,
            'set': set_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.networking.dns.servers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Domains': Domains,
        'Hostname': Hostname,
        'Servers': Servers,
    }

