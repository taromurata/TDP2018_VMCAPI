# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.networking.interfaces.
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


class Ipv4(VapiInterface):
    """
    The ``Ipv4`` class provides methods to perform IPv4 network configuration
    for interfaces. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _Ipv4Stub)

    class Mode(Enum):
        """
        The ``Ipv4.Mode`` class defines different IPv4 address assignment modes.
        This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DHCP = None
        """
        The IPv4 address is automatically assigned by a DHCP server. This class
        attribute was added in vSphere API 6.7

        """
        STATIC = None
        """
        The IPv4 address is static. This class attribute was added in vSphere API
        6.7

        """
        UNCONFIGURED = None
        """
        The IPv4 protocol is not configured. This class attribute was added in
        vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Mode` instance.
            """
            Enum.__init__(string)

    Mode._set_values([
        Mode('DHCP'),
        Mode('STATIC'),
        Mode('UNCONFIGURED'),
    ])
    Mode._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.interfaces.ipv4.mode',
        Mode))


    class Config(VapiStruct):
        """
        The ``Ipv4.Config`` class provides defines the IPv4 configuration of a
        network interface. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'mode',
                {
                    'STATIC' : [('address', True), ('prefix', True)],
                    'DHCP' : [],
                    'UNCONFIGURED' : [],
                }
            ),
        ]



        def __init__(self,
                     mode=None,
                     address=None,
                     prefix=None,
                     default_gateway=None,
                    ):
            """
            :type  mode: :class:`Ipv4.Mode`
            :param mode: The Address assignment mode. This attribute was added in vSphere
                API 6.7
            :type  address: :class:`str`
            :param address: The IPv4 address, for example, "10.20.80.191". This attribute was
                added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``mode`` is :attr:`Ipv4.Mode.STATIC`.
            :type  prefix: :class:`long`
            :param prefix: The IPv4 CIDR prefix, for example, 24. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion. This attribute was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``mode`` is :attr:`Ipv4.Mode.STATIC`.
            :type  default_gateway: :class:`str` or ``None``
            :param default_gateway: The IPv4 address of the default gateway. This configures the global
                default gateway on the appliance with the specified gateway address
                and interface. This gateway replaces the existing default gateway
                configured on the appliance. However, if the gateway address is
                link-local, then it is added for that interface. This does not
                support configuration of multiple global default gateways through
                different interfaces. This attribute was added in vSphere API 6.7
                If None, the defaultGateway was never set.
            """
            self.mode = mode
            self.address = address
            self.prefix = prefix
            self.default_gateway = default_gateway
            VapiStruct.__init__(self)

    Config._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv4.config', {
            'mode': type.ReferenceType(__name__, 'Ipv4.Mode'),
            'address': type.OptionalType(type.StringType()),
            'prefix': type.OptionalType(type.IntegerType()),
            'default_gateway': type.OptionalType(type.StringType()),
        },
        Config,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Ipv4.Info`` class defines current IPv4 configuration state of a
        network interface. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'mode',
                {
                    'STATIC' : [('address', True), ('prefix', True), ('default_gateway', True)],
                    'DHCP' : [('address', True), ('prefix', True), ('default_gateway', True)],
                    'UNCONFIGURED' : [],
                }
            ),
        ]



        def __init__(self,
                     configurable=None,
                     mode=None,
                     address=None,
                     prefix=None,
                     default_gateway=None,
                    ):
            """
            :type  configurable: :class:`bool`
            :param configurable: The specified network interface is configurable or not. This
                attribute was added in vSphere API 6.7
            :type  mode: :class:`Ipv4.Mode`
            :param mode: The Address assignment mode. This attribute was added in vSphere
                API 6.7
            :type  address: :class:`str`
            :param address: The IPv4 address, for example, "10.20.80.191". This attribute was
                added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``mode`` is one of :attr:`Ipv4.Mode.STATIC` or
                :attr:`Ipv4.Mode.DHCP`.
            :type  prefix: :class:`long`
            :param prefix: The IPv4 CIDR prefix, for example, 24. See
                http://www.oav.net/mirrors/cidr.html for netmask-to-prefix
                conversion. This attribute was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``mode`` is one of :attr:`Ipv4.Mode.STATIC` or
                :attr:`Ipv4.Mode.DHCP`.
            :type  default_gateway: :class:`str`
            :param default_gateway: The IPv4 address of the default gateway. This configures the global
                default gateway on the appliance with the specified gateway address
                and interface. This gateway replaces the existing default gateway
                configured on the appliance. However, if the gateway address is
                link-local, then it is added for that interface. This does not
                support configuration of multiple global default gateways through
                different interfaces. This attribute was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``mode`` is one of :attr:`Ipv4.Mode.STATIC` or
                :attr:`Ipv4.Mode.DHCP`.
            """
            self.configurable = configurable
            self.mode = mode
            self.address = address
            self.prefix = prefix
            self.default_gateway = default_gateway
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv4.info', {
            'configurable': type.BooleanType(),
            'mode': type.ReferenceType(__name__, 'Ipv4.Mode'),
            'address': type.OptionalType(type.StringType()),
            'prefix': type.OptionalType(type.IntegerType()),
            'default_gateway': type.OptionalType(type.StringType()),
        },
        Info,
        False,
        None))



    def set(self,
            interface_name,
            config,
            ):
        """
        Set IPv4 network configuration for specific network interface. This
        method was added in vSphere API 6.7

        :type  interface_name: :class:`str`
        :param interface_name: Network interface to update, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :type  config: :class:`Ipv4.Config`
        :param config: The IPv4 Network configuration to set.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified NIC is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the IP is used as PNID
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the specified NIC is busy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('set',
                            {
                            'interface_name': interface_name,
                            'config': config,
                            })

    def get(self,
            interface_name,
            ):
        """
        Get IPv4 network configuration for specific NIC. This method was added
        in vSphere API 6.7

        :type  interface_name: :class:`str`
        :param interface_name: The Network interface to query, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :rtype: :class:`Ipv4.Info`
        :return: The IPv4 configuration for the queried NIC.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified NIC is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('get',
                            {
                            'interface_name': interface_name,
                            })
class Ipv6(VapiInterface):
    """
    The ``Ipv6`` class provides methods to perform IPv6 network configuration
    for interfaces. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _Ipv6Stub)

    class Origin(Enum):
        """
        The ``Ipv6.Origin`` class defines IPv6 address origin values. This
        enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DHCP = None
        """
        The IPv6 address is assigned by a DHCP server. See RFC 4293. This class
        attribute was added in vSphere API 6.7

        """
        RANDOM = None
        """
        The IPv6 address is assigned randomly by the system. See RFC 4293. This
        class attribute was added in vSphere API 6.7

        """
        MANUAL = None
        """
        The IPv6 address was manually configured to a specified address, for
        example, by user configuration. See RFC 4293. This class attribute was
        added in vSphere API 6.7

        """
        LINKLAYER = None
        """
        The IPv6 address is assigned by IPv6 Stateless Address Auto-configuration
        (SLAAC). See RFC 4293. This class attribute was added in vSphere API 6.7

        """
        OTHER = None
        """
        The IPv6 address is assigned by a mechanism other than manual, DHCP, SLAAC,
        or random. See RFC 4293. This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Origin` instance.
            """
            Enum.__init__(string)

    Origin._set_values([
        Origin('DHCP'),
        Origin('RANDOM'),
        Origin('MANUAL'),
        Origin('LINKLAYER'),
        Origin('OTHER'),
    ])
    Origin._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.interfaces.ipv6.origin',
        Origin))


    class Status(Enum):
        """
        The ``Ipv6.Status`` class defines IPv6 address status values. See RFC 4293.
        This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        TENTATIVE = None
        """
        The IPv6 address is in the process of being verified as unique. An address
        in this state cannot be used for general communication. It can be used to
        determine the uniqueness of the address. This class attribute was added in
        vSphere API 6.7

        """
        UNKNOWN = None
        """
        The status of this address cannot be determined. This class attribute was
        added in vSphere API 6.7

        """
        INACCESSIBLE = None
        """
        The IPv6 address is inaccessible because the interface to which this
        address is assigned is not operational. This class attribute was added in
        vSphere API 6.7

        """
        INVALID = None
        """
        The IPv6 address is not a valid address. It should not appear as the
        destination or source address of a packet. This class attribute was added
        in vSphere API 6.7

        """
        DUPLICATE = None
        """
        The IPv6 address is not unique on the link and cannot be used. This class
        attribute was added in vSphere API 6.7

        """
        PREFERRED = None
        """
        This is a valid IPv6 address that can appear as the destination or source
        address of a packet. This class attribute was added in vSphere API 6.7

        """
        DEPRECATED = None
        """
        The is a valid but deprecated IPv6 address. This address cannot be used as
        a source address in new communications, although packets addressed to such
        an address are processed as expected. This class attribute was added in
        vSphere API 6.7

        """
        OPTIMISTIC = None
        """
        The IPv6 address is available for use, subject to restrictions, while its
        uniqueness on a link is being verified. This class attribute was added in
        vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('TENTATIVE'),
        Status('UNKNOWN'),
        Status('INACCESSIBLE'),
        Status('INVALID'),
        Status('DUPLICATE'),
        Status('PREFERRED'),
        Status('DEPRECATED'),
        Status('OPTIMISTIC'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.appliance.networking.interfaces.ipv6.status',
        Status))


    class Address(VapiStruct):
        """
        The ``Ipv6.Address`` class provides the structure used to name an IPv6
        address. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     prefix=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: The IPv6 address, for example, fc00:10:20:83:20c:29ff:fe94:bb5a.
                This attribute was added in vSphere API 6.7
            :type  prefix: :class:`long`
            :param prefix: The IPv6 CIDR prefix, for example, 64. This attribute was added in
                vSphere API 6.7
            """
            self.address = address
            self.prefix = prefix
            VapiStruct.__init__(self)

    Address._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv6.address', {
            'address': type.StringType(),
            'prefix': type.IntegerType(),
        },
        Address,
        False,
        None))


    class AddressInfo(VapiStruct):
        """
        The ``Ipv6.AddressInfo`` class provides the structure that you can use to
        get information about an IPv6 address along with its origin and status.
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     origin=None,
                     status=None,
                     address=None,
                     prefix=None,
                    ):
            """
            :type  origin: :class:`Ipv6.Origin`
            :param origin: The Origin of the IPv6 address. For more information, see RFC 4293.
                This attribute was added in vSphere API 6.7
            :type  status: :class:`Ipv6.Status`
            :param status: The Status of the IPv6 address. For more information, see RFC 4293.
                This attribute was added in vSphere API 6.7
            :type  address: :class:`str`
            :param address: The IPv6 address, for example, fc00:10:20:83:20c:29ff:fe94:bb5a.
                This attribute was added in vSphere API 6.7
            :type  prefix: :class:`long`
            :param prefix: The IPv6 CIDR prefix, for example, 64. This attribute was added in
                vSphere API 6.7
            """
            self.origin = origin
            self.status = status
            self.address = address
            self.prefix = prefix
            VapiStruct.__init__(self)

    AddressInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv6.address_info', {
            'origin': type.ReferenceType(__name__, 'Ipv6.Origin'),
            'status': type.ReferenceType(__name__, 'Ipv6.Status'),
            'address': type.StringType(),
            'prefix': type.IntegerType(),
        },
        AddressInfo,
        False,
        None))


    class Config(VapiStruct):
        """
        The ``Ipv6.Config`` class provides the structure that you can use to
        configure IPv6 on a particular interface. Addresses can be assigned by
        DHCP, SLAAC or STATIC, as IPv6 permits multiple addresses per interface.
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     dhcp=None,
                     autoconf=None,
                     addresses=None,
                     default_gateway=None,
                    ):
            """
            :type  dhcp: :class:`bool`
            :param dhcp: An address will be assigned by a DHCP server. This attribute was
                added in vSphere API 6.7
            :type  autoconf: :class:`bool`
            :param autoconf: An address will be assigned by Stateless Address Autoconfiguration
                (SLAAC). This attribute was added in vSphere API 6.7
            :type  addresses: :class:`list` of :class:`Ipv6.Address`
            :param addresses: The list of addresses to be statically assigned. This attribute was
                added in vSphere API 6.7
            :type  default_gateway: :class:`str`
            :param default_gateway: The default gateway for static IP address assignment. This
                configures the global IPv6 default gateway on the appliance with
                the specified gateway address and interface. This gateway replaces
                the existing default gateway configured on the appliance. However,
                if the gateway address is link-local, then it is added for that
                interface. This does not support configuration of multiple global
                default gateways through different interfaces. This attribute was
                added in vSphere API 6.7
            """
            self.dhcp = dhcp
            self.autoconf = autoconf
            self.addresses = addresses
            self.default_gateway = default_gateway
            VapiStruct.__init__(self)

    Config._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv6.config', {
            'dhcp': type.BooleanType(),
            'autoconf': type.BooleanType(),
            'addresses': type.ListType(type.ReferenceType(__name__, 'Ipv6.Address')),
            'default_gateway': type.StringType(),
        },
        Config,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Ipv6.Info`` class provides the structure that defines an existing
        IPv6 configuration on a particular interface. This structure is read only.
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     dhcp=None,
                     autoconf=None,
                     addresses=None,
                     default_gateway=None,
                     configurable=None,
                    ):
            """
            :type  dhcp: :class:`bool`
            :param dhcp: DHCP is on. This attribute was added in vSphere API 6.7
            :type  autoconf: :class:`bool`
            :param autoconf: Stateless Address Autoconfiguration (SLAAC) is on. This attribute
                was added in vSphere API 6.7
            :type  addresses: :class:`list` of :class:`Ipv6.AddressInfo`
            :param addresses: List of addresses with their origins and statuses. This attribute
                was added in vSphere API 6.7
            :type  default_gateway: :class:`str`
            :param default_gateway: The default gateway for static IP address assignment. This
                configures the global IPv6 default gateway on the appliance with
                the specified gateway address and interface. This gateway replaces
                the existing default gateway configured on the appliance. However,
                if the gateway address is link-local, then it is added for that
                interface. This does not support configuration of multiple global
                default gateways through different interfaces. This attribute was
                added in vSphere API 6.7
            :type  configurable: :class:`bool`
            :param configurable: Is NIC configurable or not. This attribute was added in vSphere API
                6.7
            """
            self.dhcp = dhcp
            self.autoconf = autoconf
            self.addresses = addresses
            self.default_gateway = default_gateway
            self.configurable = configurable
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.networking.interfaces.ipv6.info', {
            'dhcp': type.BooleanType(),
            'autoconf': type.BooleanType(),
            'addresses': type.ListType(type.ReferenceType(__name__, 'Ipv6.AddressInfo')),
            'default_gateway': type.StringType(),
            'configurable': type.BooleanType(),
        },
        Info,
        False,
        None))



    def set(self,
            interface_name,
            config,
            ):
        """
        Set IPv6 network configuration for specific interface. This method was
        added in vSphere API 6.7

        :type  interface_name: :class:`str`
        :param interface_name: Network interface to update, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :type  config: :class:`Ipv6.Config`
        :param config: The IPv6 configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            The specified NIC is busy.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            The specified NIC is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('set',
                            {
                            'interface_name': interface_name,
                            'config': config,
                            })

    def get(self,
            interface_name,
            ):
        """
        Get IPv6 network configuration for specific interface. This method was
        added in vSphere API 6.7

        :type  interface_name: :class:`str`
        :param interface_name: Network interface to query, for example, "nic0".
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.networking.interfaces``.
        :rtype: :class:`Ipv6.Info`
        :return: IPv6 configuration.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified NIC is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error.
        """
        return self._invoke('get',
                            {
                            'interface_name': interface_name,
                            })
class _Ipv4Stub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'interface_name': type.IdType(resource_types='com.vmware.appliance.networking.interfaces'),
            'config': type.ReferenceType(__name__, 'Ipv4.Config'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/networking/interfaces/{interface_name}/ipv4',
            path_variables={
                'interface_name': 'interface_name',
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
            url_template='/appliance/networking/interfaces/{interface_name}/ipv4',
            path_variables={
                'interface_name': 'interface_name',
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
                'output_type': type.ReferenceType(__name__, 'Ipv4.Info'),
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
            self, iface_name='com.vmware.appliance.networking.interfaces.ipv4',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _Ipv6Stub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'interface_name': type.IdType(resource_types='com.vmware.appliance.networking.interfaces'),
            'config': type.ReferenceType(__name__, 'Ipv6.Config'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/networking/interfaces/{interface_name}/ipv6',
            path_variables={
                'interface_name': 'interface_name',
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
            url_template='/appliance/networking/interfaces/{interface_name}/ipv6',
            path_variables={
                'interface_name': 'interface_name',
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
                'output_type': type.ReferenceType(__name__, 'Ipv6.Info'),
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
            self, iface_name='com.vmware.appliance.networking.interfaces.ipv6',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Ipv4': Ipv4,
        'Ipv6': Ipv6,
    }

