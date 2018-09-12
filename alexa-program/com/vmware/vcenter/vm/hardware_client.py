# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.hardware.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm.hardware_client`` module provides classes for
managing the virtual hardware configuration and state of a virtual machine.
This includes methods for reading and manipulating virtual device configuration
and for querying the runtime state of the devices.

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

class ConnectionState(Enum):
    """
    The ``ConnectionState`` class defines the valid states for a removable
    device that is configured to be connected.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    CONNECTED = None
    """
    The device is connected and working correctly.

    """
    RECOVERABLE_ERROR = None
    """
    Device connection failed due to a recoverable error; for example, the
    virtual device backing is currently in use by another virtual machine.

    """
    UNRECOVERABLE_ERROR = None
    """
    Device connection failed due to an unrecoverable error; for example, the
    virtual device backing does not exist.

    """
    NOT_CONNECTED = None
    """
    The device is not connected.

    """
    UNKNOWN = None
    """
    The device status is unknown.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`ConnectionState` instance.
        """
        Enum.__init__(string)

ConnectionState._set_values([
    ConnectionState('CONNECTED'),
    ConnectionState('RECOVERABLE_ERROR'),
    ConnectionState('UNRECOVERABLE_ERROR'),
    ConnectionState('NOT_CONNECTED'),
    ConnectionState('UNKNOWN'),
])
ConnectionState._set_binding_type(type.EnumType(
    'com.vmware.vcenter.vm.hardware.connection_state',
    ConnectionState))




class IdeAddressInfo(VapiStruct):
    """
    The ``IdeAddressInfo`` class contains information about the address of a
    virtual device that is attached to a virtual IDE adapter of a virtual
    machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 primary=None,
                 master=None,
                ):
        """
        :type  primary: :class:`bool`
        :param primary: Flag specifying whether the device is attached to the primary or
            secondary IDE adapter of the virtual machine.
        :type  master: :class:`bool`
        :param master: Flag specifying whether the device is the master or slave device on
            the IDE adapter.
        """
        self.primary = primary
        self.master = master
        VapiStruct.__init__(self)

IdeAddressInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.ide_address_info', {
        'primary': type.BooleanType(),
        'master': type.BooleanType(),
    },
    IdeAddressInfo,
    False,
    None))



class ScsiAddressInfo(VapiStruct):
    """
    The ``ScsiAddressInfo`` class contains information about the address of a
    virtual device that is attached to a virtual SCSI adapter of a virtual
    machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 bus=None,
                 unit=None,
                ):
        """
        :type  bus: :class:`long`
        :param bus: Bus number of the adapter to which the device is attached.
        :type  unit: :class:`long`
        :param unit: Unit number of the device.
        """
        self.bus = bus
        self.unit = unit
        VapiStruct.__init__(self)

ScsiAddressInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.scsi_address_info', {
        'bus': type.IntegerType(),
        'unit': type.IntegerType(),
    },
    ScsiAddressInfo,
    False,
    None))



class SataAddressInfo(VapiStruct):
    """
    The ``SataAddressInfo`` class contains information about the address of a
    virtual device that is attached to a virtual SATA adapter of a virtual
    machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 bus=None,
                 unit=None,
                ):
        """
        :type  bus: :class:`long`
        :param bus: Bus number of the adapter to which the device is attached.
        :type  unit: :class:`long`
        :param unit: Unit number of the device.
        """
        self.bus = bus
        self.unit = unit
        VapiStruct.__init__(self)

SataAddressInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.sata_address_info', {
        'bus': type.IntegerType(),
        'unit': type.IntegerType(),
    },
    SataAddressInfo,
    False,
    None))



class IdeAddressSpec(VapiStruct):
    """
    The ``IdeAddressSpec`` class contains information for specifying the
    address of a virtual device that is attached to a virtual IDE adapter of a
    virtual machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 primary=None,
                 master=None,
                ):
        """
        :type  primary: :class:`bool` or ``None``
        :param primary: Flag specifying whether the device should be attached to the
            primary or secondary IDE adapter of the virtual machine.
            If None, the server will choose a adapter with an available
            connection. If no IDE connections are available, the request will
            be rejected.
        :type  master: :class:`bool` or ``None``
        :param master: Flag specifying whether the device should be the master or slave
            device on the IDE adapter.
            If None, the server will choose an available connection type. If no
            IDE connections are available, the request will be rejected.
        """
        self.primary = primary
        self.master = master
        VapiStruct.__init__(self)

IdeAddressSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.ide_address_spec', {
        'primary': type.OptionalType(type.BooleanType()),
        'master': type.OptionalType(type.BooleanType()),
    },
    IdeAddressSpec,
    False,
    None))



class ScsiAddressSpec(VapiStruct):
    """
    The ``ScsiAddressSpec`` class contains information for specifying the
    address of a virtual device that is attached to a virtual SCSI adapter of a
    virtual machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 bus=None,
                 unit=None,
                ):
        """
        :type  bus: :class:`long`
        :param bus: Bus number of the adapter to which the device should be attached.
        :type  unit: :class:`long` or ``None``
        :param unit: Unit number of the device.
            If None, the server will choose an available unit number on the
            specified adapter. If there are no available connections on the
            adapter, the request will be rejected.
        """
        self.bus = bus
        self.unit = unit
        VapiStruct.__init__(self)

ScsiAddressSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.scsi_address_spec', {
        'bus': type.IntegerType(),
        'unit': type.OptionalType(type.IntegerType()),
    },
    ScsiAddressSpec,
    False,
    None))



class SataAddressSpec(VapiStruct):
    """
    The ``SataAddressSpec`` class contains information for specifying the
    address of a virtual device that is attached to a virtual SATA adapter of a
    virtual machine.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 bus=None,
                 unit=None,
                ):
        """
        :type  bus: :class:`long`
        :param bus: Bus number of the adapter to which the device should be attached.
        :type  unit: :class:`long` or ``None``
        :param unit: Unit number of the device.
            If None, the server will choose an available unit number on the
            specified adapter. If there are no available connections on the
            adapter, the request will be rejected.
        """
        self.bus = bus
        self.unit = unit
        VapiStruct.__init__(self)

SataAddressSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.sata_address_spec', {
        'bus': type.IntegerType(),
        'unit': type.OptionalType(type.IntegerType()),
    },
    SataAddressSpec,
    False,
    None))



class ConnectionInfo(VapiStruct):
    """
    The ``ConnectionInfo`` class provides information about the state and
    configuration of a removable virtual device.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 state=None,
                 start_connected=None,
                 allow_guest_control=None,
                ):
        """
        :type  state: :class:`ConnectionState`
        :param state: Connection status of the virtual device.
        :type  start_connected: :class:`bool`
        :param start_connected: Flag indicating whether the virtual device should be connected
            whenever the virtual machine is powered on.
        :type  allow_guest_control: :class:`bool`
        :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
            device.
        """
        self.state = state
        self.start_connected = start_connected
        self.allow_guest_control = allow_guest_control
        VapiStruct.__init__(self)

ConnectionInfo._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.connection_info', {
        'state': type.ReferenceType(__name__, 'ConnectionState'),
        'start_connected': type.BooleanType(),
        'allow_guest_control': type.BooleanType(),
    },
    ConnectionInfo,
    False,
    None))



class ConnectionCreateSpec(VapiStruct):
    """
    The ``ConnectionCreateSpec`` class provides a specification for the
    configuration of a newly-created removable device.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 start_connected=None,
                 allow_guest_control=None,
                ):
        """
        :type  start_connected: :class:`bool` or ``None``
        :param start_connected: Flag indicating whether the virtual device should be connected
            whenever the virtual machine is powered on.
            Defaults to false if None.
        :type  allow_guest_control: :class:`bool` or ``None``
        :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
            device.
            Defaults to false if None.
        """
        self.start_connected = start_connected
        self.allow_guest_control = allow_guest_control
        VapiStruct.__init__(self)

ConnectionCreateSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.connection_create_spec', {
        'start_connected': type.OptionalType(type.BooleanType()),
        'allow_guest_control': type.OptionalType(type.BooleanType()),
    },
    ConnectionCreateSpec,
    False,
    None))



class ConnectionUpdateSpec(VapiStruct):
    """
    The ``ConnectionUpdateSpec`` class describes the updates to be made to the
    configuration of a removable virtual device.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 start_connected=None,
                 allow_guest_control=None,
                ):
        """
        :type  start_connected: :class:`bool` or ``None``
        :param start_connected: Flag indicating whether the virtual device should be connected
            whenever the virtual machine is powered on.
            If None, the value is unchanged.
        :type  allow_guest_control: :class:`bool` or ``None``
        :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
            device.
            If None, the value is unchanged.
        """
        self.start_connected = start_connected
        self.allow_guest_control = allow_guest_control
        VapiStruct.__init__(self)

ConnectionUpdateSpec._set_binding_type(type.StructType(
    'com.vmware.vcenter.vm.hardware.connection_update_spec', {
        'start_connected': type.OptionalType(type.BooleanType()),
        'allow_guest_control': type.OptionalType(type.BooleanType()),
    },
    ConnectionUpdateSpec,
    False,
    None))



class Boot(VapiInterface):
    """
    The ``Boot`` class provides methods for configuring the settings used when
    booting a virtual machine.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BootStub)

    class Type(Enum):
        """
        The ``Boot.Type`` class defines the valid firmware types for a virtual
        machine.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BIOS = None
        """
        Basic Input/Output System (BIOS) firmware.

        """
        EFI = None
        """
        Extensible Firmware Interface (EFI) firmware.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('BIOS'),
        Type('EFI'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.boot.type',
        Type))


    class NetworkProtocol(Enum):
        """
        The ``Boot.NetworkProtocol`` class defines the valid network boot protocols
        supported when booting a virtual machine with :attr:`Boot.Type.EFI`
        firmware over the network.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IPV4 = None
        """
        PXE or Apple NetBoot over IPv4.

        """
        IPV6 = None
        """
        PXE over IPv6.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`NetworkProtocol` instance.
            """
            Enum.__init__(string)

    NetworkProtocol._set_values([
        NetworkProtocol('IPV4'),
        NetworkProtocol('IPV6'),
    ])
    NetworkProtocol._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.boot.network_protocol',
        NetworkProtocol))


    class Info(VapiStruct):
        """
        The ``Boot.Info`` class contains information about the virtual machine boot
        process.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'EFI' : [('efi_legacy_boot', True), ('network_protocol', True)],
                    'BIOS' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     efi_legacy_boot=None,
                     network_protocol=None,
                     delay=None,
                     retry=None,
                     retry_delay=None,
                     enter_setup_mode=None,
                    ):
            """
            :type  type: :class:`Boot.Type`
            :param type: Firmware type used by the virtual machine.
            :type  efi_legacy_boot: :class:`bool`
            :param efi_legacy_boot: Flag indicating whether to use EFI legacy boot mode.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Boot.Type.EFI`.
            :type  network_protocol: :class:`Boot.NetworkProtocol`
            :param network_protocol: Protocol to use when attempting to boot the virtual machine over
                the network.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Boot.Type.EFI`.
            :type  delay: :class:`long`
            :param delay: Delay in milliseconds before beginning the firmware boot process
                when the virtual machine is powered on. This delay may be used to
                provide a time window for users to connect to the virtual machine
                console and enter BIOS setup mode.
            :type  retry: :class:`bool`
            :param retry: Flag indicating whether the virtual machine will automatically
                retry the boot process after a failure.
            :type  retry_delay: :class:`long`
            :param retry_delay: Delay in milliseconds before retrying the boot process after a
                failure; applicable only when :attr:`Boot.Info.retry` is true.
            :type  enter_setup_mode: :class:`bool`
            :param enter_setup_mode: Flag indicating whether the firmware boot process will
                automatically enter setup mode the next time the virtual machine
                boots. Note that this flag will automatically be reset to false
                once the virtual machine enters setup mode.
            """
            self.type = type
            self.efi_legacy_boot = efi_legacy_boot
            self.network_protocol = network_protocol
            self.delay = delay
            self.retry = retry
            self.retry_delay = retry_delay
            self.enter_setup_mode = enter_setup_mode
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.boot.info', {
            'type': type.ReferenceType(__name__, 'Boot.Type'),
            'efi_legacy_boot': type.OptionalType(type.BooleanType()),
            'network_protocol': type.OptionalType(type.ReferenceType(__name__, 'Boot.NetworkProtocol')),
            'delay': type.IntegerType(),
            'retry': type.BooleanType(),
            'retry_delay': type.IntegerType(),
            'enter_setup_mode': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Boot.CreateSpec`` class describes settings used when booting a
        virtual machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'EFI' : [('efi_legacy_boot', False), ('network_protocol', False)],
                    'BIOS' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     efi_legacy_boot=None,
                     network_protocol=None,
                     delay=None,
                     retry=None,
                     retry_delay=None,
                     enter_setup_mode=None,
                    ):
            """
            :type  type: :class:`Boot.Type` or ``None``
            :param type: Firmware type to be used by the virtual machine.
                If None, defaults to value that is recommended for the guest OS and
                is supported for the virtual hardware version.
            :type  efi_legacy_boot: :class:`bool` or ``None``
            :param efi_legacy_boot: Flag indicating whether to use EFI legacy boot mode.
                If None, defaults to value that is recommended for the guest OS and
                is supported for the virtual hardware version.
            :type  network_protocol: :class:`Boot.NetworkProtocol` or ``None``
            :param network_protocol: Protocol to use when attempting to boot the virtual machine over
                the network.
                If None, defaults to a system defined default value.
            :type  delay: :class:`long` or ``None``
            :param delay: Delay in milliseconds before beginning the firmware boot process
                when the virtual machine is powered on. This delay may be used to
                provide a time window for users to connect to the virtual machine
                console and enter BIOS setup mode.
                If None, default value is 0.
            :type  retry: :class:`bool` or ``None``
            :param retry: Flag indicating whether the virtual machine should automatically
                retry the boot process after a failure.
                If None, default value is false.
            :type  retry_delay: :class:`long` or ``None``
            :param retry_delay: Delay in milliseconds before retrying the boot process after a
                failure; applicable only when :attr:`Boot.Info.retry` is true.
                If None, default value is 10000.
            :type  enter_setup_mode: :class:`bool` or ``None``
            :param enter_setup_mode: Flag indicating whether the firmware boot process should
                automatically enter setup mode the next time the virtual machine
                boots. Note that this flag will automatically be reset to false
                once the virtual machine enters setup mode.
                If None, the value is unchanged.
            """
            self.type = type
            self.efi_legacy_boot = efi_legacy_boot
            self.network_protocol = network_protocol
            self.delay = delay
            self.retry = retry
            self.retry_delay = retry_delay
            self.enter_setup_mode = enter_setup_mode
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.boot.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Boot.Type')),
            'efi_legacy_boot': type.OptionalType(type.BooleanType()),
            'network_protocol': type.OptionalType(type.ReferenceType(__name__, 'Boot.NetworkProtocol')),
            'delay': type.OptionalType(type.IntegerType()),
            'retry': type.OptionalType(type.BooleanType()),
            'retry_delay': type.OptionalType(type.IntegerType()),
            'enter_setup_mode': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Boot.UpdateSpec`` class describes the updates to the settings used
        when booting a virtual machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'EFI' : [('efi_legacy_boot', False), ('network_protocol', False)],
                    'BIOS' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     efi_legacy_boot=None,
                     network_protocol=None,
                     delay=None,
                     retry=None,
                     retry_delay=None,
                     enter_setup_mode=None,
                    ):
            """
            :type  type: :class:`Boot.Type` or ``None``
            :param type: Firmware type to be used by the virtual machine.
                If None, the value is unchanged.
            :type  efi_legacy_boot: :class:`bool` or ``None``
            :param efi_legacy_boot: Flag indicating whether to use EFI legacy boot mode.
                If None, the value is unchanged.
            :type  network_protocol: :class:`Boot.NetworkProtocol` or ``None``
            :param network_protocol: Protocol to use when attempting to boot the virtual machine over
                the network.
                If None, the value is unchanged.
            :type  delay: :class:`long` or ``None``
            :param delay: Delay in milliseconds before beginning the firmware boot process
                when the virtual machine is powered on. This delay may be used to
                provide a time window for users to connect to the virtual machine
                console and enter BIOS setup mode.
                If None, the value is unchanged.
            :type  retry: :class:`bool` or ``None``
            :param retry: Flag indicating whether the virtual machine should automatically
                retry the boot process after a failure.
                If None, the value is unchanged.
            :type  retry_delay: :class:`long` or ``None``
            :param retry_delay: Delay in milliseconds before retrying the boot process after a
                failure; applicable only when :attr:`Boot.Info.retry` is true.
                If None, the value is unchanged.
            :type  enter_setup_mode: :class:`bool` or ``None``
            :param enter_setup_mode: Flag indicating whether the firmware boot process should
                automatically enter setup mode the next time the virtual machine
                boots. Note that this flag will automatically be reset to false
                once the virtual machine enters setup mode.
                If None, the value is unchanged.
            """
            self.type = type
            self.efi_legacy_boot = efi_legacy_boot
            self.network_protocol = network_protocol
            self.delay = delay
            self.retry = retry
            self.retry_delay = retry_delay
            self.enter_setup_mode = enter_setup_mode
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.boot.update_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Boot.Type')),
            'efi_legacy_boot': type.OptionalType(type.BooleanType()),
            'network_protocol': type.OptionalType(type.ReferenceType(__name__, 'Boot.NetworkProtocol')),
            'delay': type.OptionalType(type.IntegerType()),
            'retry': type.OptionalType(type.BooleanType()),
            'retry_delay': type.OptionalType(type.IntegerType()),
            'enter_setup_mode': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns the boot-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Boot.Info`
        :return: Boot-related settings of the virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })

    def update(self,
               vm,
               spec,
               ):
        """
        Updates the boot-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Boot.UpdateSpec`
        :param spec: Specification for updating the boot-related settings of the virtual
            machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if one of the provided settings is not permitted; for example,
            specifying a negative value for ``delay``.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'spec': spec,
                            })
class Cdrom(VapiInterface):
    """
    The ``Cdrom`` class provides methods for configuring the virtual CD-ROM
    devices of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.Cdrom"
    """
    Resource type for the virtual CD-ROM device.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CdromStub)

    class HostBusAdapterType(Enum):
        """
        The ``Cdrom.HostBusAdapterType`` class defines the valid types of host bus
        adapters that may be used for attaching a Cdrom to a virtual machine.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IDE = None
        """
        Cdrom is attached to an IDE adapter.

        """
        SATA = None
        """
        Cdrom is attached to a SATA adapter.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HostBusAdapterType` instance.
            """
            Enum.__init__(string)

    HostBusAdapterType._set_values([
        HostBusAdapterType('IDE'),
        HostBusAdapterType('SATA'),
    ])
    HostBusAdapterType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.cdrom.host_bus_adapter_type',
        HostBusAdapterType))


    class BackingType(Enum):
        """
        The ``Cdrom.BackingType`` class defines the valid backing types for a
        virtual CD-ROM device.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ISO_FILE = None
        """
        Virtual CD-ROM device is backed by an ISO file.

        """
        HOST_DEVICE = None
        """
        Virtual CD-ROM device is backed by a device on the host where the virtual
        machine is running.

        """
        CLIENT_DEVICE = None
        """
        Virtual CD-ROM device is backed by a device on the client that is connected
        to the virtual machine console.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('ISO_FILE'),
        BackingType('HOST_DEVICE'),
        BackingType('CLIENT_DEVICE'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.cdrom.backing_type',
        BackingType))


    class DeviceAccessType(Enum):
        """
        The ``Cdrom.DeviceAccessType`` class defines the valid device access types
        for a physical device packing of a virtual CD-ROM device.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        EMULATION = None
        """
        ATAPI or SCSI device emulation.

        """
        PASSTHRU = None
        """
        Raw passthru device access.

        """
        PASSTHRU_EXCLUSIVE = None
        """
        Raw passthru device access, with exclusive access to the device.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DeviceAccessType` instance.
            """
            Enum.__init__(string)

    DeviceAccessType._set_values([
        DeviceAccessType('EMULATION'),
        DeviceAccessType('PASSTHRU'),
        DeviceAccessType('PASSTHRU_EXCLUSIVE'),
    ])
    DeviceAccessType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.cdrom.device_access_type',
        DeviceAccessType))


    class BackingInfo(VapiStruct):
        """
        The ``Cdrom.BackingInfo`` class contains information about the physical
        resource backing a virtual CD-ROM device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'ISO_FILE' : [('iso_file', True)],
                    'HOST_DEVICE' : [('host_device', False), ('auto_detect', True), ('device_access_type', True)],
                    'CLIENT_DEVICE' : [('device_access_type', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     iso_file=None,
                     host_device=None,
                     auto_detect=None,
                     device_access_type=None,
                    ):
            """
            :type  type: :class:`Cdrom.BackingType`
            :param type: Backing type for the virtual CD-ROM device.
            :type  iso_file: :class:`str`
            :param iso_file: Path of the image file backing the virtual CD-ROM device.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Cdrom.BackingType.ISO_FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the host device backing the virtual CD-ROM device. 
                This attribute will be None if ``autoDetect`` is true and the
                virtual CD-ROM device is not connected or no suitable device is
                available on the host.
            :type  auto_detect: :class:`bool`
            :param auto_detect: Flag indicating whether the virtual CD-ROM device is configured to
                automatically detect a suitable host device.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Cdrom.BackingType.HOST_DEVICE`.
            :type  device_access_type: :class:`Cdrom.DeviceAccessType`
            :param device_access_type: Access type for the device backing.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Cdrom.BackingType.HOST_DEVICE` or
                :attr:`Cdrom.BackingType.CLIENT_DEVICE`.
            """
            self.type = type
            self.iso_file = iso_file
            self.host_device = host_device
            self.auto_detect = auto_detect
            self.device_access_type = device_access_type
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.backing_info', {
            'type': type.ReferenceType(__name__, 'Cdrom.BackingType'),
            'iso_file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'auto_detect': type.OptionalType(type.BooleanType()),
            'device_access_type': type.OptionalType(type.ReferenceType(__name__, 'Cdrom.DeviceAccessType')),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Cdrom.BackingSpec`` class provides a specification of the physical
        resource backing a virtual CD-ROM device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'ISO_FILE' : [('iso_file', True)],
                    'HOST_DEVICE' : [('host_device', False), ('device_access_type', False)],
                    'CLIENT_DEVICE' : [('device_access_type', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     iso_file=None,
                     host_device=None,
                     device_access_type=None,
                    ):
            """
            :type  type: :class:`Cdrom.BackingType`
            :param type: Backing type for the virtual CD-ROM device.
            :type  iso_file: :class:`str`
            :param iso_file: Path of the image file that should be used as the virtual CD-ROM
                device backing.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Cdrom.BackingType.ISO_FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device that should be used as the virtual CD-ROM device
                backing.
                If None, the virtual CD-ROM device will be configured to
                automatically detect a suitable host device.
            :type  device_access_type: :class:`Cdrom.DeviceAccessType` or ``None``
            :param device_access_type: Access type for the device backing.
                If None, defaults to :attr:`Cdrom.DeviceAccessType.EMULATION`.
            """
            self.type = type
            self.iso_file = iso_file
            self.host_device = host_device
            self.device_access_type = device_access_type
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.backing_spec', {
            'type': type.ReferenceType(__name__, 'Cdrom.BackingType'),
            'iso_file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'device_access_type': type.OptionalType(type.ReferenceType(__name__, 'Cdrom.DeviceAccessType')),
        },
        BackingSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Cdrom.Info`` class contains information about a virtual CD-ROM
        device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IDE' : [('ide', True)],
                    'SATA' : [('sata', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     label=None,
                     ide=None,
                     sata=None,
                     backing=None,
                     state=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  type: :class:`Cdrom.HostBusAdapterType`
            :param type: Type of host bus adapter to which the device is attached.
            :type  label: :class:`str`
            :param label: Device label.
            :type  ide: :class:`IdeAddressInfo`
            :param ide: Address of device attached to a virtual IDE adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Cdrom.HostBusAdapterType.IDE`.
            :type  sata: :class:`SataAddressInfo`
            :param sata: Address of device attached to a virtual SATA adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Cdrom.HostBusAdapterType.SATA`.
            :type  backing: :class:`Cdrom.BackingInfo`
            :param backing: Physical resource backing for the virtual CD-ROM device.
            :type  state: :class:`ConnectionState`
            :param state: Connection status of the virtual device.
            :type  start_connected: :class:`bool`
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
            :type  allow_guest_control: :class:`bool`
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
            """
            self.type = type
            self.label = label
            self.ide = ide
            self.sata = sata
            self.backing = backing
            self.state = state
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.info', {
            'type': type.ReferenceType(__name__, 'Cdrom.HostBusAdapterType'),
            'label': type.StringType(),
            'ide': type.OptionalType(type.ReferenceType(__name__, 'IdeAddressInfo')),
            'sata': type.OptionalType(type.ReferenceType(__name__, 'SataAddressInfo')),
            'backing': type.ReferenceType(__name__, 'Cdrom.BackingInfo'),
            'state': type.ReferenceType(__name__, 'ConnectionState'),
            'start_connected': type.BooleanType(),
            'allow_guest_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Cdrom.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual CD-ROM device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IDE' : [('ide', False)],
                    'SATA' : [('sata', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     ide=None,
                     sata=None,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  type: :class:`Cdrom.HostBusAdapterType` or ``None``
            :param type: Type of host bus adapter to which the device should be attached.
                If None, guest-specific default values will be used
            :type  ide: :class:`IdeAddressSpec` or ``None``
            :param ide: Address for attaching the device to a virtual IDE adapter.
                If None, the server will choose an available address; if none is
                available, the request will fail.
            :type  sata: :class:`SataAddressSpec` or ``None``
            :param sata: Address for attaching the device to a virtual SATA adapter.
                If None, the server will choose an available address; if none is
                available, the request will fail.
            :type  backing: :class:`Cdrom.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual CD-ROM device.
                If None, defaults to automatic detection of a suitable host device.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                Defaults to false if None.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                Defaults to false if None.
            """
            self.type = type
            self.ide = ide
            self.sata = sata
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Cdrom.HostBusAdapterType')),
            'ide': type.OptionalType(type.ReferenceType(__name__, 'IdeAddressSpec')),
            'sata': type.OptionalType(type.ReferenceType(__name__, 'SataAddressSpec')),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Cdrom.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Cdrom.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual CD-ROM device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  backing: :class:`Cdrom.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual CD-ROM device. 
                
                This attribute may only be modified if the virtual machine is not
                powered on or the virtual CD-ROM device is not connected.
                If None, the value is unchanged.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                If None, the value is unchanged.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                If None, the value is unchanged.
            """
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.update_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Cdrom.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Cdrom.Summary`` class contains commonly used information about a
        virtual CD-ROM device.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cdrom=None,
                    ):
            """
            :type  cdrom: :class:`str`
            :param cdrom: Identifier of the virtual CD-ROM device.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Cdrom``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Cdrom``.
            """
            self.cdrom = cdrom
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cdrom.summary', {
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual CD-ROM devices
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Cdrom.Summary`
        :return: List of commonly used information about virtual CD-ROM devices.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            cdrom,
            ):
        """
        Returns information about a virtual CD-ROM device.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: Virtual CD-ROM device identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :rtype: :class:`Cdrom.Info`
        :return: Information about the specified virtual CD-ROM device.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual CD-ROM device is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual CD-ROM device to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Cdrom.CreateSpec`
        :param spec: Specification for the new virtual CD-ROM device.
        :rtype: :class:`str`
        :return: Virtual CD-ROM device identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the CD-ROM device was created but was
            unable to confirm the creation because the identifier of the new
            device could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended or if the virtual machine is
            powered on and virtual CD-ROM type is IDE.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the specified storage address is unavailable; for example, if
            the SCSI adapter requested does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the specified storage address is in use.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the specified storage address is out of bounds.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the guest operating system of the virtual machine is not
            supported and spec includes None attributes that default to
            guest-specific values.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               cdrom,
               spec,
               ):
        """
        Updates the configuration of a virtual CD-ROM device.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: Virtual CD-ROM device identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :type  spec: :class:`Cdrom.UpdateSpec`
        :param spec: Specification for updating the virtual CD-ROM device.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual CD-ROM device is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual CD-ROM
            device.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               cdrom,
               ):
        """
        Removes a virtual CD-ROM device from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: Virtual CD-ROM device identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual CD-ROM device is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended or if the virtual machine is
            powered on and virtual CD-ROM type is IDE.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            })

    def connect(self,
                vm,
                cdrom,
                ):
        """
        Connects a virtual CD-ROM device of a powered-on virtual machine to its
        backing. Connecting the virtual device makes the backing accessible
        from the perspective of the guest operating system. 
        
        For a powered-off virtual machine, the :func:`Cdrom.update` method may
        be used to configure the virtual CD-ROM device to start in the
        connected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: Virtual CD-ROM device identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual CD-ROM device is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual CD-ROM device is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('connect',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            })

    def disconnect(self,
                   vm,
                   cdrom,
                   ):
        """
        Disconnects a virtual CD-ROM device of a powered-on virtual machine
        from its backing. The virtual device is still present and its backing
        configuration is unchanged, but from the perspective of the guest
        operating system, the CD-ROM device is not connected to its backing
        resource. 
        
        For a powered-off virtual machine, the :func:`Cdrom.update` method may
        be used to configure the virtual CD-ROM device to start in the
        disconnected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  cdrom: :class:`str`
        :param cdrom: Virtual CD-ROM device identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Cdrom``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual CD-ROM device is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual CD-ROM device is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('disconnect',
                            {
                            'vm': vm,
                            'cdrom': cdrom,
                            })
class Cpu(VapiInterface):
    """
    The ``Cpu`` class provides methods for configuring the CPU settings of a
    virtual machine.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CpuStub)

    class Info(VapiStruct):
        """
        The ``Cpu.Info`` class contains CPU-related information about a virtual
        machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     count=None,
                     cores_per_socket=None,
                     hot_add_enabled=None,
                     hot_remove_enabled=None,
                    ):
            """
            :type  count: :class:`long`
            :param count: Number of CPU cores.
            :type  cores_per_socket: :class:`long`
            :param cores_per_socket: Number of CPU cores per socket.
            :type  hot_add_enabled: :class:`bool`
            :param hot_add_enabled: Flag indicating whether adding CPUs while the virtual machine is
                running is enabled.
            :type  hot_remove_enabled: :class:`bool`
            :param hot_remove_enabled: Flag indicating whether removing CPUs while the virtual machine is
                running is enabled.
            """
            self.count = count
            self.cores_per_socket = cores_per_socket
            self.hot_add_enabled = hot_add_enabled
            self.hot_remove_enabled = hot_remove_enabled
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cpu.info', {
            'count': type.IntegerType(),
            'cores_per_socket': type.IntegerType(),
            'hot_add_enabled': type.BooleanType(),
            'hot_remove_enabled': type.BooleanType(),
        },
        Info,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Cpu.UpdateSpec`` class describes the updates to be made to the
        CPU-related settings of a virtual machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     count=None,
                     cores_per_socket=None,
                     hot_add_enabled=None,
                     hot_remove_enabled=None,
                    ):
            """
            :type  count: :class:`long` or ``None``
            :param count: New number of CPU cores. The number of CPU cores in the virtual
                machine must be a multiple of the number of cores per socket. 
                
                The supported range of CPU counts is constrained by the configured
                guest operating system and virtual hardware version of the virtual
                machine. 
                
                If the virtual machine is running, the number of CPU cores may only
                be increased if :attr:`Cpu.Info.hot_add_enabled` is true, and may
                only be decreased if :attr:`Cpu.Info.hot_remove_enabled` is true.
                If None, the value is unchanged.
            :type  cores_per_socket: :class:`long` or ``None``
            :param cores_per_socket: New number of CPU cores per socket. The number of CPU cores in the
                virtual machine must be a multiple of the number of cores per
                socket.
                If None, the value is unchanged.
            :type  hot_add_enabled: :class:`bool` or ``None``
            :param hot_add_enabled: Flag indicating whether adding CPUs while the virtual machine is
                running is enabled. 
                
                This attribute may only be modified if the virtual machine is
                powered off.
                If None, the value is unchanged.
            :type  hot_remove_enabled: :class:`bool` or ``None``
            :param hot_remove_enabled: Flag indicating whether removing CPUs while the virtual machine is
                running is enabled. 
                
                This attribute may only be modified if the virtual machine is
                powered off.
                If None, the value is unchanged.
            """
            self.count = count
            self.cores_per_socket = cores_per_socket
            self.hot_add_enabled = hot_add_enabled
            self.hot_remove_enabled = hot_remove_enabled
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.cpu.update_spec', {
            'count': type.OptionalType(type.IntegerType()),
            'cores_per_socket': type.OptionalType(type.IntegerType()),
            'hot_add_enabled': type.OptionalType(type.BooleanType()),
            'hot_remove_enabled': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns the CPU-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Cpu.Info`
        :return: CPU-related settings of the virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })

    def update(self,
               vm,
               spec,
               ):
        """
        Updates the CPU-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Cpu.UpdateSpec`
        :param spec: Specification for updating the CPU-related settings of the virtual
            machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if one of the provided settings is not permitted; for example,
            specifying a negative value for ``count``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if ``hotAddEnabled`` or ``hotRemoveEnabled`` is specified and the
            virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if ``count`` is specified and is greater than ``count``,
            ``hotAddEnabled`` is false, and the virtual machine is not powered
            off.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if ``count`` is specified and is less than ``count``,
            ``hotRemoveEnabled`` is false, and the virtual machine is not
            powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'spec': spec,
                            })
class Disk(VapiInterface):
    """
    The ``Disk`` class provides methods for configuring the virtual disks of a
    virtual machine. A virtual disk has a backing such as a VMDK file. The
    backing has an independent lifecycle from the virtual machine when it is
    detached from the virtual machine. The :func:`Disk.create` method provides
    the ability to create a new virtual disk. When creating a virtual disk, a
    new VMDK file may be created or an existing VMDK file may used as a
    backing. Once a VMDK file is associated with a virtual machine, its
    lifecycle will be bound to the virtual machine. In other words, it will be
    deleted when the virtual machine is deleted. The :func:`Disk.delete` method
    provides the ability to detach a VMDK file from the virtual machine. The
    :func:`Disk.delete` method does not delete the VMDK file that backs the
    virtual disk. Once detached, the VMDK file will not be destroyed when the
    virtual machine to which it was associated is deleted.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.Disk"
    """
    Resource type for the virtual disk.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DiskStub)

    class HostBusAdapterType(Enum):
        """
        The ``Disk.HostBusAdapterType`` class defines the valid types of host bus
        adapters that may be used for attaching a virtual storage device to a
        virtual machine.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IDE = None
        """
        Disk is attached to an IDE adapter.

        """
        SCSI = None
        """
        Disk is attached to a SCSI adapter.

        """
        SATA = None
        """
        Disk is attached to a SATA adapter.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HostBusAdapterType` instance.
            """
            Enum.__init__(string)

    HostBusAdapterType._set_values([
        HostBusAdapterType('IDE'),
        HostBusAdapterType('SCSI'),
        HostBusAdapterType('SATA'),
    ])
    HostBusAdapterType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.disk.host_bus_adapter_type',
        HostBusAdapterType))


    class BackingType(Enum):
        """
        The ``Disk.BackingType`` class defines the valid backing types for a
        virtual disk.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VMDK_FILE = None
        """
        Virtual disk is backed by a VMDK file.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('VMDK_FILE'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.disk.backing_type',
        BackingType))


    class BackingInfo(VapiStruct):
        """
        The ``Disk.BackingInfo`` class contains information about the physical
        resource backing a virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VMDK_FILE' : [('vmdk_file', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     vmdk_file=None,
                    ):
            """
            :type  type: :class:`Disk.BackingType`
            :param type: Backing type for the virtual disk.
            :type  vmdk_file: :class:`str`
            :param vmdk_file: Path of the VMDK file backing the virtual disk.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Disk.BackingType.VMDK_FILE`.
            """
            self.type = type
            self.vmdk_file = vmdk_file
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.backing_info', {
            'type': type.ReferenceType(__name__, 'Disk.BackingType'),
            'vmdk_file': type.OptionalType(type.StringType()),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Disk.BackingSpec`` class provides a specification of the physical
        resource backing a virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VMDK_FILE' : [('vmdk_file', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     vmdk_file=None,
                    ):
            """
            :type  type: :class:`Disk.BackingType`
            :param type: Backing type for the virtual disk.
            :type  vmdk_file: :class:`str`
            :param vmdk_file: Path of the VMDK file backing the virtual disk.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Disk.BackingType.VMDK_FILE`.
            """
            self.type = type
            self.vmdk_file = vmdk_file
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.backing_spec', {
            'type': type.ReferenceType(__name__, 'Disk.BackingType'),
            'vmdk_file': type.OptionalType(type.StringType()),
        },
        BackingSpec,
        False,
        None))


    class VmdkCreateSpec(VapiStruct):
        """
        The ``Disk.VmdkCreateSpec`` class provides a specification for creating a
        new VMDK file to be used as a backing for a virtual disk. The virtual disk
        will be stored in the same directory as the virtual machine's configuration
        file.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     capacity=None,
                     storage_policy=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Base name of the VMDK file. The name should not include the '.vmdk'
                file extension.
                If None, a name (derived from the name of the virtual machine) will
                be chosen by the server.
            :type  capacity: :class:`long` or ``None``
            :param capacity: Capacity of the virtual disk backing in bytes.
                If None, defaults to a guest-specific capacity.
            :type  storage_policy: :class:`Disk.StoragePolicySpec` or ``None``
            :param storage_policy: The ``Disk.StoragePolicySpec`` class contains information about the
                storage policy that is to be associated the with VMDK file. This
                attribute was added in vSphere API 6.7
                If None the default storage policy of the target datastore (if
                applicable) is applied. Currently a default storage policy is only
                supported by object based datastores : VVol & vSAN. For non- object
                datastores, if None then no storage policy would be associated with
                the VMDK file.
            """
            self.name = name
            self.capacity = capacity
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    VmdkCreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.vmdk_create_spec', {
            'name': type.OptionalType(type.StringType()),
            'capacity': type.OptionalType(type.IntegerType()),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'Disk.StoragePolicySpec')),
        },
        VmdkCreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Disk.Info`` class contains information about a virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IDE' : [('ide', True)],
                    'SCSI' : [('scsi', True)],
                    'SATA' : [('sata', True)],
                }
            ),
        ]



        def __init__(self,
                     label=None,
                     type=None,
                     ide=None,
                     scsi=None,
                     sata=None,
                     backing=None,
                     capacity=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  type: :class:`Disk.HostBusAdapterType`
            :param type: Type of host bus adapter to which the device is attached.
            :type  ide: :class:`IdeAddressInfo`
            :param ide: Address of device attached to a virtual IDE adapter.
                Workaround for PR1459646
            :type  scsi: :class:`ScsiAddressInfo`
            :param scsi: Address of device attached to a virtual SCSI adapter.
                Workaround for PR1459646
            :type  sata: :class:`SataAddressInfo`
            :param sata: Address of device attached to a virtual SATA adapter.
                Workaround for PR1459646
            :type  backing: :class:`Disk.BackingInfo`
            :param backing: Physical resource backing for the virtual disk.
            :type  capacity: :class:`long` or ``None``
            :param capacity: Capacity of the virtual disk in bytes.
                If None, virtual disk is inaccessible or disk capacity is 0.
            """
            self.label = label
            self.type = type
            self.ide = ide
            self.scsi = scsi
            self.sata = sata
            self.backing = backing
            self.capacity = capacity
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.info', {
            'label': type.StringType(),
            'type': type.ReferenceType(__name__, 'Disk.HostBusAdapterType'),
            'ide': type.OptionalType(type.ReferenceType(__name__, 'IdeAddressInfo')),
            'scsi': type.OptionalType(type.ReferenceType(__name__, 'ScsiAddressInfo')),
            'sata': type.OptionalType(type.ReferenceType(__name__, 'SataAddressInfo')),
            'backing': type.ReferenceType(__name__, 'Disk.BackingInfo'),
            'capacity': type.OptionalType(type.IntegerType()),
        },
        Info,
        False,
        None))


    class StoragePolicySpec(VapiStruct):
        """
        The ``Disk.StoragePolicySpec`` class contains information about the storage
        policy be associated with a VMDK file. This class was added in vSphere API
        6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policy=None,
                    ):
            """
            :type  policy: :class:`str`
            :param policy: Identifier of the storage policy which should be associated with
                the VMDK file. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
            """
            self.policy = policy
            VapiStruct.__init__(self)

    StoragePolicySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.storage_policy_spec', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.StoragePolicy'),
        },
        StoragePolicySpec,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Disk.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IDE' : [('ide', False)],
                    'SCSI' : [('scsi', False)],
                    'SATA' : [('sata', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     ide=None,
                     scsi=None,
                     sata=None,
                     backing=None,
                     new_vmdk=None,
                    ):
            """
            :type  type: :class:`Disk.HostBusAdapterType` or ``None``
            :param type: Type of host bus adapter to which the device should be attached.
                If None, guest-specific default values will be used
            :type  ide: :class:`IdeAddressSpec` or ``None``
            :param ide: Address for attaching the device to a virtual IDE adapter.
                If None, the server will choose an available address; if none is
                available, the request will fail.
            :type  scsi: :class:`ScsiAddressSpec` or ``None``
            :param scsi: Address for attaching the device to a virtual SCSI adapter.
                If None, the server will choose an available address; if none is
                available, the request will fail.
            :type  sata: :class:`SataAddressSpec` or ``None``
            :param sata: Address for attaching the device to a virtual SATA adapter.
                If None, the server will choose an available address; if none is
                available, the request will fail.
            :type  backing: :class:`Disk.BackingSpec` or ``None``
            :param backing: Existing physical resource backing for the virtual disk. Exactly
                one of ``backing`` or ``newVmdk`` must be specified.
                If None, the virtual disk will not be connected to an existing
                backing.
            :type  new_vmdk: :class:`Disk.VmdkCreateSpec` or ``None``
            :param new_vmdk: Specification for creating a new VMDK backing for the virtual disk.
                Exactly one of ``backing`` or ``newVmdk`` must be specified.
                If None, a new VMDK backing will not be created.
            """
            self.type = type
            self.ide = ide
            self.scsi = scsi
            self.sata = sata
            self.backing = backing
            self.new_vmdk = new_vmdk
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Disk.HostBusAdapterType')),
            'ide': type.OptionalType(type.ReferenceType(__name__, 'IdeAddressSpec')),
            'scsi': type.OptionalType(type.ReferenceType(__name__, 'ScsiAddressSpec')),
            'sata': type.OptionalType(type.ReferenceType(__name__, 'SataAddressSpec')),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Disk.BackingSpec')),
            'new_vmdk': type.OptionalType(type.ReferenceType(__name__, 'Disk.VmdkCreateSpec')),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Disk.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                    ):
            """
            :type  backing: :class:`Disk.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual disk. 
                
                This attribute may only be modified if the virtual machine is not
                powered on.
                If None, the value is unchanged.
            """
            self.backing = backing
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.update_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Disk.BackingSpec')),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Disk.Summary`` class contains commonly used information about a
        virtual disk.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     disk=None,
                    ):
            """
            :type  disk: :class:`str`
            :param disk: Identifier of the virtual Disk.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            """
            self.disk = disk
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.disk.summary', {
            'disk': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual disks belonging to
        the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Disk.Summary`
        :return: List of commonly used information about the virtual disks.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            disk,
            ):
        """
        Returns information about a virtual disk.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  disk: :class:`str`
        :param disk: Virtual disk identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Disk``.
        :rtype: :class:`Disk.Info`
        :return: Information about the specified virtual disk.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual disk is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'disk': disk,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual disk to the virtual machine. While adding the virtual
        disk, a new VMDK file may be created or an existing VMDK file may be
        used to back the virtual disk.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Disk.CreateSpec`
        :param spec: Specification for the new virtual disk.
        :rtype: :class:`str`
        :return: Virtual disk identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Disk``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if system reported that the disk device was created but was unable
            to confirm the creation because the identifier of the new device
            could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended or if the virtual machine is
            powered on and virtual disk type is IDE.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the specified storage address is unavailable; for example, if
            the SCSI adapter requested does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the specified storage address is in use.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the specified storage address is out of bounds or if the
            specified storage policy is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the guest operating system of the virtual machine is not
            supported and spec includes None attributes that default to
            guest-specific values.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               disk,
               spec,
               ):
        """
        Updates the configuration of a virtual disk. An update method can be
        used to detach the existing VMDK file and attach another VMDK file to
        the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  disk: :class:`str`
        :param disk: Virtual disk identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Disk``.
        :type  spec: :class:`Disk.UpdateSpec`
        :param spec: Specification for updating the virtual disk.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual disk is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual disk.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'disk': disk,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               disk,
               ):
        """
        Removes a virtual disk from the virtual machine. This method does not
        destroy the VMDK file that backs the virtual disk. It only detaches the
        VMDK file from the virtual machine. Once detached, the VMDK file will
        not be destroyed when the virtual machine to which it was associated is
        deleted.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  disk: :class:`str`
        :param disk: Virtual disk identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Disk``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual disk is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended or if the virtual machine is
            powered on and virtual disk type is IDE.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'disk': disk,
                            })
class Ethernet(VapiInterface):
    """
    The ``Ethernet`` class provides methods for configuring the virtual
    Ethernet adapters of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.Ethernet"
    """
    Resource type for the virtual Ethernet adapter.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EthernetStub)

    class EmulationType(Enum):
        """
        The ``Ethernet.EmulationType`` class defines the valid emulation types for
        a virtual Ethernet adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        E1000 = None
        """
        E1000 ethernet adapter.

        """
        E1000E = None
        """
        E1000e ethernet adapter.

        """
        PCNET32 = None
        """
        AMD Lance PCNet32 Ethernet adapter.

        """
        VMXNET = None
        """
        VMware Vmxnet virtual Ethernet adapter.

        """
        VMXNET2 = None
        """
        VMware Vmxnet2 virtual Ethernet adapter.

        """
        VMXNET3 = None
        """
        VMware Vmxnet3 virtual Ethernet adapter.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`EmulationType` instance.
            """
            Enum.__init__(string)

    EmulationType._set_values([
        EmulationType('E1000'),
        EmulationType('E1000E'),
        EmulationType('PCNET32'),
        EmulationType('VMXNET'),
        EmulationType('VMXNET2'),
        EmulationType('VMXNET3'),
    ])
    EmulationType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.ethernet.emulation_type',
        EmulationType))


    class MacAddressType(Enum):
        """
        The ``Ethernet.MacAddressType`` class defines the valid MAC address origins
        for a virtual Ethernet adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        MANUAL = None
        """
        MAC address is assigned statically.

        """
        GENERATED = None
        """
        MAC address is generated automatically.

        """
        ASSIGNED = None
        """
        MAC address is assigned by vCenter Server.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`MacAddressType` instance.
            """
            Enum.__init__(string)

    MacAddressType._set_values([
        MacAddressType('MANUAL'),
        MacAddressType('GENERATED'),
        MacAddressType('ASSIGNED'),
    ])
    MacAddressType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.ethernet.mac_address_type',
        MacAddressType))


    class BackingType(Enum):
        """
        The ``Ethernet.BackingType`` class defines the valid backing types for a
        virtual Ethernet adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        STANDARD_PORTGROUP = None
        """
        vSphere standard portgroup network backing.

        """
        HOST_DEVICE = None
        """
        Legacy host device network backing. Imported VMs may have virtual Ethernet
        adapters with this type of backing, but this type of backing cannot be used
        to create or to update a virtual Ethernet adapter.

        """
        DISTRIBUTED_PORTGROUP = None
        """
        Distributed virtual switch backing.

        """
        OPAQUE_NETWORK = None
        """
        Opaque network backing.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('STANDARD_PORTGROUP'),
        BackingType('HOST_DEVICE'),
        BackingType('DISTRIBUTED_PORTGROUP'),
        BackingType('OPAQUE_NETWORK'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.ethernet.backing_type',
        BackingType))


    class BackingInfo(VapiStruct):
        """
        The ``Ethernet.BackingInfo`` class contains information about the physical
        resource backing a virtual Ethernet adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'STANDARD_PORTGROUP' : [('network', False), ('network_name', True)],
                    'DISTRIBUTED_PORTGROUP' : [('network', False), ('distributed_switch_uuid', True), ('distributed_port', False), ('connection_cookie', False)],
                    'OPAQUE_NETWORK' : [('network', False), ('opaque_network_type', True), ('opaque_network_id', True)],
                    'HOST_DEVICE' : [('host_device', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     network=None,
                     network_name=None,
                     host_device=None,
                     distributed_switch_uuid=None,
                     distributed_port=None,
                     connection_cookie=None,
                     opaque_network_type=None,
                     opaque_network_id=None,
                    ):
            """
            :type  type: :class:`Ethernet.BackingType`
            :param type: Backing type for the virtual Ethernet adapter.
            :type  network: :class:`str` or ``None``
            :param network: Identifier of the network backing the virtual Ethernet adapter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
                If None, the identifier of the network backing could not be
                determined.
            :type  network_name: :class:`str`
            :param network_name: Name of the standard portgroup backing the virtual Ethernet
                adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.BackingType.STANDARD_PORTGROUP`.
            :type  host_device: :class:`str`
            :param host_device: Name of the device backing the virtual Ethernet adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.BackingType.HOST_DEVICE`.
            :type  distributed_switch_uuid: :class:`str`
            :param distributed_switch_uuid: UUID of the distributed virtual switch that backs the virtual
                Ethernet adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.BackingType.DISTRIBUTED_PORTGROUP`.
            :type  distributed_port: :class:`str` or ``None``
            :param distributed_port: Key of the distributed virtual port that backs the virtual Ethernet
                adapter.
                This attribute will be None if the virtual Ethernet device is not
                bound to a distributed virtual port; this can happen if the virtual
                machine is powered off or the virtual Ethernet device is not
                connected.
            :type  connection_cookie: :class:`long` or ``None``
            :param connection_cookie: Server-generated cookie that identifies the connection to the port.
                This ookie may be used to verify that the virtual machine is the
                rightful owner of the port.
                This attribute will be None if the virtual Ethernet device is not
                bound to a distributed virtual port; this can happen if the virtual
                machine is powered off or the virtual Ethernet device is not
                connected.
            :type  opaque_network_type: :class:`str`
            :param opaque_network_type: Type of the opaque network that backs the virtual Ethernet adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.BackingType.OPAQUE_NETWORK`.
            :type  opaque_network_id: :class:`str`
            :param opaque_network_id: Identifier of the opaque network that backs the virtual Ethernet
                adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.BackingType.OPAQUE_NETWORK`.
            """
            self.type = type
            self.network = network
            self.network_name = network_name
            self.host_device = host_device
            self.distributed_switch_uuid = distributed_switch_uuid
            self.distributed_port = distributed_port
            self.connection_cookie = connection_cookie
            self.opaque_network_type = opaque_network_type
            self.opaque_network_id = opaque_network_id
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.backing_info', {
            'type': type.ReferenceType(__name__, 'Ethernet.BackingType'),
            'network': type.OptionalType(type.IdType()),
            'network_name': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'distributed_switch_uuid': type.OptionalType(type.StringType()),
            'distributed_port': type.OptionalType(type.StringType()),
            'connection_cookie': type.OptionalType(type.IntegerType()),
            'opaque_network_type': type.OptionalType(type.StringType()),
            'opaque_network_id': type.OptionalType(type.StringType()),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Ethernet.BackingSpec`` class provides a specification of the physical
        resource that backs a virtual Ethernet adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'STANDARD_PORTGROUP' : [('network', True)],
                    'DISTRIBUTED_PORTGROUP' : [('network', True), ('distributed_port', False)],
                    'OPAQUE_NETWORK' : [('network', True)],
                    'HOST_DEVICE' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     network=None,
                     distributed_port=None,
                    ):
            """
            :type  type: :class:`Ethernet.BackingType`
            :param type: Backing type for the virtual Ethernet adapter.
            :type  network: :class:`str`
            :param network: Identifier of the network that backs the virtual Ethernet adapter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of
                :attr:`Ethernet.BackingType.STANDARD_PORTGROUP`,
                :attr:`Ethernet.BackingType.DISTRIBUTED_PORTGROUP`, or
                :attr:`Ethernet.BackingType.OPAQUE_NETWORK`.
            :type  distributed_port: :class:`str` or ``None``
            :param distributed_port: Key of the distributed virtual port that backs the virtual Ethernet
                adapter. Depending on the type of the Portgroup, the port may be
                specified using this field. If the portgroup type is early-binding
                (also known as static), a port is assigned when the Ethernet
                adapter is configured to use the port. The port may be either
                automatically or specifically assigned based on the value of this
                attribute. If the portgroup type is ephemeral, the port is created
                and assigned to a virtual machine when it is powered on and the
                Ethernet adapter is connected. This attribute cannot be specified
                as no free ports exist before use.
                May be used to specify a port when the network specified on the
                ``network`` attribute is a static or early binding distributed
                portgroup. If None, the port will be automatically assigned to the
                Ethernet adapter based on the policy embodied by the portgroup
                type.
            """
            self.type = type
            self.network = network
            self.distributed_port = distributed_port
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.backing_spec', {
            'type': type.ReferenceType(__name__, 'Ethernet.BackingType'),
            'network': type.OptionalType(type.IdType()),
            'distributed_port': type.OptionalType(type.StringType()),
        },
        BackingSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Ethernet.Info`` class contains information about a virtual Ethernet
        adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VMXNET3' : [('upt_compatibility_enabled', True)],
                    'E1000' : [],
                    'E1000E' : [],
                    'PCNET32' : [],
                    'VMXNET' : [],
                    'VMXNET2' : [],
                }
            ),
        ]



        def __init__(self,
                     label=None,
                     type=None,
                     upt_compatibility_enabled=None,
                     mac_type=None,
                     mac_address=None,
                     pci_slot_number=None,
                     wake_on_lan_enabled=None,
                     backing=None,
                     state=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  type: :class:`Ethernet.EmulationType`
            :param type: Ethernet adapter emulation type.
            :type  upt_compatibility_enabled: :class:`bool`
            :param upt_compatibility_enabled: Flag indicating whether Universal Pass-Through (UPT) compatibility
                is enabled on this virtual Ethernet adapter.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Ethernet.EmulationType.VMXNET3`.
            :type  mac_type: :class:`Ethernet.MacAddressType`
            :param mac_type: MAC address type.
            :type  mac_address: :class:`str` or ``None``
            :param mac_address: MAC address.
                May be None if :attr:`Ethernet.Info.mac_type` is
                :attr:`Ethernet.MacAddressType.MANUAL` and has not been specified,
                or if :attr:`Ethernet.Info.mac_type` is
                :attr:`Ethernet.MacAddressType.GENERATED` and the virtual machine
                has never been powered on since the Ethernet adapter was created.
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the virtual Ethernet adapter on the PCI bus. If the PCI
                address is invalid, the server will change it when the VM is
                started or as the device is hot added.
                May be None if the virtual machine has never been powered on since
                the adapter was created.
            :type  wake_on_lan_enabled: :class:`bool`
            :param wake_on_lan_enabled: Flag indicating whether wake-on-LAN is enabled on this virtual
                Ethernet adapter.
            :type  backing: :class:`Ethernet.BackingInfo`
            :param backing: Physical resource backing for the virtual Ethernet adapter.
            :type  state: :class:`ConnectionState`
            :param state: Connection status of the virtual device.
            :type  start_connected: :class:`bool`
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
            :type  allow_guest_control: :class:`bool`
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
            """
            self.label = label
            self.type = type
            self.upt_compatibility_enabled = upt_compatibility_enabled
            self.mac_type = mac_type
            self.mac_address = mac_address
            self.pci_slot_number = pci_slot_number
            self.wake_on_lan_enabled = wake_on_lan_enabled
            self.backing = backing
            self.state = state
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.info', {
            'label': type.StringType(),
            'type': type.ReferenceType(__name__, 'Ethernet.EmulationType'),
            'upt_compatibility_enabled': type.OptionalType(type.BooleanType()),
            'mac_type': type.ReferenceType(__name__, 'Ethernet.MacAddressType'),
            'mac_address': type.OptionalType(type.StringType()),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
            'wake_on_lan_enabled': type.BooleanType(),
            'backing': type.ReferenceType(__name__, 'Ethernet.BackingInfo'),
            'state': type.ReferenceType(__name__, 'ConnectionState'),
            'start_connected': type.BooleanType(),
            'allow_guest_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Ethernet.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual Ethernet adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'VMXNET3' : [('upt_compatibility_enabled', False)],
                    'E1000' : [],
                    'E1000E' : [],
                    'PCNET32' : [],
                    'VMXNET' : [],
                    'VMXNET2' : [],
                }
            ),
            UnionValidator(
                'mac_type',
                {
                    'MANUAL' : [('mac_address', True)],
                    'GENERATED' : [],
                    'ASSIGNED' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     upt_compatibility_enabled=None,
                     mac_type=None,
                     mac_address=None,
                     pci_slot_number=None,
                     wake_on_lan_enabled=None,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  type: :class:`Ethernet.EmulationType` or ``None``
            :param type: Ethernet adapter emulation type.
                If None, defaults to a guest-specific type.
            :type  upt_compatibility_enabled: :class:`bool` or ``None``
            :param upt_compatibility_enabled: Flag indicating whether Universal Pass-Through (UPT) compatibility
                is enabled on this virtual Ethernet adapter.
                If None, defaults to false.
            :type  mac_type: :class:`Ethernet.MacAddressType` or ``None``
            :param mac_type: MAC address type.
                If None, defaults to :attr:`Ethernet.MacAddressType.GENERATED`.
            :type  mac_address: :class:`str`
            :param mac_address: MAC address.
                Workaround for PR1459647
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the virtual Ethernet adapter on the PCI bus. If the PCI
                address is invalid, the server will change when it the VM is
                started or as the device is hot added.
                If None, the server will choose an available address when the
                virtual machine is powered on.
            :type  wake_on_lan_enabled: :class:`bool` or ``None``
            :param wake_on_lan_enabled: Flag indicating whether wake-on-LAN is enabled on this virtual
                Ethernet adapter.
                Defaults to false if None.
            :type  backing: :class:`Ethernet.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual Ethernet adapter.
                If None, the system may try to find an appropriate backing. If one
                is not found, the request will fail.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                Defaults to false if None.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                Defaults to false if None.
            """
            self.type = type
            self.upt_compatibility_enabled = upt_compatibility_enabled
            self.mac_type = mac_type
            self.mac_address = mac_address
            self.pci_slot_number = pci_slot_number
            self.wake_on_lan_enabled = wake_on_lan_enabled
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Ethernet.EmulationType')),
            'upt_compatibility_enabled': type.OptionalType(type.BooleanType()),
            'mac_type': type.OptionalType(type.ReferenceType(__name__, 'Ethernet.MacAddressType')),
            'mac_address': type.OptionalType(type.StringType()),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
            'wake_on_lan_enabled': type.OptionalType(type.BooleanType()),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Ethernet.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Ethernet.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual Ethernet adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     upt_compatibility_enabled=None,
                     mac_type=None,
                     mac_address=None,
                     wake_on_lan_enabled=None,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  upt_compatibility_enabled: :class:`bool` or ``None``
            :param upt_compatibility_enabled: Flag indicating whether Universal Pass-Through (UPT) compatibility
                should be enabled on this virtual Ethernet adapter. 
                
                This attribute may be modified at any time, and changes will be
                applied the next time the virtual machine is powered on.
                If None, the value is unchanged. Must be None if the emulation type
                of the virtual Ethernet adapter is not
                :attr:`Ethernet.EmulationType.VMXNET3`.
            :type  mac_type: :class:`Ethernet.MacAddressType` or ``None``
            :param mac_type: MAC address type. 
                
                This attribute may be modified at any time, and changes will be
                applied the next time the virtual machine is powered on.
                If None, the value is unchanged.
            :type  mac_address: :class:`str` or ``None``
            :param mac_address: MAC address. 
                
                This attribute may be modified at any time, and changes will be
                applied the next time the virtual machine is powered on.
                If None, the value is unchanged. Must be specified if
                :attr:`Ethernet.UpdateSpec.mac_type` is
                :attr:`Ethernet.MacAddressType.MANUAL`. Must be None if the MAC
                address type is not :attr:`Ethernet.MacAddressType.MANUAL`.
            :type  wake_on_lan_enabled: :class:`bool` or ``None``
            :param wake_on_lan_enabled: Flag indicating whether wake-on-LAN shoud be enabled on this
                virtual Ethernet adapter. 
                
                This attribute may be modified at any time, and changes will be
                applied the next time the virtual machine is powered on.
                If None, the value is unchanged.
            :type  backing: :class:`Ethernet.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual Ethernet adapter. 
                
                This attribute may be modified at any time, and changes will be
                applied the next time the virtual machine is powered on.
                If None, the value is unchanged.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                If None, the value is unchanged.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                If None, the value is unchanged.
            """
            self.upt_compatibility_enabled = upt_compatibility_enabled
            self.mac_type = mac_type
            self.mac_address = mac_address
            self.wake_on_lan_enabled = wake_on_lan_enabled
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.update_spec', {
            'upt_compatibility_enabled': type.OptionalType(type.BooleanType()),
            'mac_type': type.OptionalType(type.ReferenceType(__name__, 'Ethernet.MacAddressType')),
            'mac_address': type.OptionalType(type.StringType()),
            'wake_on_lan_enabled': type.OptionalType(type.BooleanType()),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Ethernet.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Ethernet.Summary`` class contains commonly used information about a
        virtual Ethernet adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     nic=None,
                    ):
            """
            :type  nic: :class:`str`
            :param nic: Identifier of the virtual Ethernet adapter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Ethernet``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Ethernet``.
            """
            self.nic = nic
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.ethernet.summary', {
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual Ethernet adapters
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Ethernet.Summary`
        :return: List of commonly used information about virtual Ethernet adapters.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            nic,
            ):
        """
        Returns information about a virtual Ethernet adapter.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  nic: :class:`str`
        :param nic: Virtual Ethernet adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :rtype: :class:`Ethernet.Info`
        :return: Information about the specified virtual Ethernet adapter.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual Ethernet adapter is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'nic': nic,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual Ethernet adapter to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Ethernet.CreateSpec`
        :param spec: Specification for the new virtual Ethernet adapter.
        :rtype: :class:`str`
        :return: Virtual Ethernet adapter identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the Ethernet adapter was created but
            was unable to confirm the creation because the identifier of the
            new adapter could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or network backing is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the virtual machine already has the maximum number of supported
            Ethernet adapters.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the specified PCI address is out of bounds, HOST_DEVICE is
            specified as the type, or a backing cannot be found in the case
            that backing is left None.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the guest operating system of the virtual machine is not
            supported and spec includes None attributes that default to
            guest-specific values.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               nic,
               spec,
               ):
        """
        Updates the configuration of a virtual Ethernet adapter.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  nic: :class:`str`
        :param nic: Virtual Ethernet adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :type  spec: :class:`Ethernet.UpdateSpec`
        :param spec: Specification for updating the virtual Ethernet adapter.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if HOST_DEVICE is specified as the type.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine, virtual Ethernet adapter, or backing
            network is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'nic': nic,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               nic,
               ):
        """
        Removes a virtual Ethernet adapter from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  nic: :class:`str`
        :param nic: Virtual Ethernet adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual Ethernet adapter is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'nic': nic,
                            })

    def connect(self,
                vm,
                nic,
                ):
        """
        Connects a virtual Ethernet adapter of a powered-on virtual machine to
        its backing. Connecting the virtual device makes the backing accessible
        from the perspective of the guest operating system. 
        
        For a powered-off virtual machine, the :func:`Ethernet.update` method
        may be used to configure the virtual Ethernet adapter to start in the
        connected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  nic: :class:`str`
        :param nic: Virtual Ethernet adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual Ethernet adapter is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual Ethernet adapter is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('connect',
                            {
                            'vm': vm,
                            'nic': nic,
                            })

    def disconnect(self,
                   vm,
                   nic,
                   ):
        """
        Disconnects a virtual Ethernet adapter of a powered-on virtual machine
        from its backing. The virtual device is still present and its backing
        configuration is unchanged, but from the perspective of the guest
        operating system, the Ethernet adapter is not connected to its backing
        resource. 
        
        For a powered-off virtual machine, the :func:`Ethernet.update` method
        may be used to configure the virtual Ethernet adapter to start in the
        disconnected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  nic: :class:`str`
        :param nic: Virtual Ethernet adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Ethernet``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual Ethernet adapter is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual Ethernet adapter is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('disconnect',
                            {
                            'vm': vm,
                            'nic': nic,
                            })
class Floppy(VapiInterface):
    """
    The ``Floppy`` class provides methods for configuring the virtual floppy
    drives of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.Floppy"
    """
    Resource type for the virtual floppy drive device.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FloppyStub)

    class BackingType(Enum):
        """
        The ``Floppy.BackingType`` class defines the valid backing types for a
        virtual floppy drive.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        IMAGE_FILE = None
        """
        Virtual floppy drive is backed by an image file.

        """
        HOST_DEVICE = None
        """
        Virtual floppy drive is backed by a device on the host where the virtual
        machine is running.

        """
        CLIENT_DEVICE = None
        """
        Virtual floppy drive is backed by a device on the client that is connected
        to the virtual machine console.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('IMAGE_FILE'),
        BackingType('HOST_DEVICE'),
        BackingType('CLIENT_DEVICE'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.floppy.backing_type',
        BackingType))


    class BackingInfo(VapiStruct):
        """
        The ``Floppy.BackingInfo`` class contains information about the physical
        resource backing a virtual floppy drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IMAGE_FILE' : [('image_file', True)],
                    'HOST_DEVICE' : [('host_device', False), ('auto_detect', True)],
                    'CLIENT_DEVICE' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     image_file=None,
                     host_device=None,
                     auto_detect=None,
                    ):
            """
            :type  type: :class:`Floppy.BackingType`
            :param type: Backing type for the virtual floppy drive.
            :type  image_file: :class:`str`
            :param image_file: Path of the image file backing the virtual floppy drive.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Floppy.BackingType.IMAGE_FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the host device backing the virtual floppy drive. 
                This attribute will be None if ``autoDetect`` is true and the
                virtual floppy drive is not connected or no suitable device is
                available on the host.
            :type  auto_detect: :class:`bool`
            :param auto_detect: Flag indicating whether the virtual floppy drive is configured to
                automatically detect a suitable host device.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Floppy.BackingType.HOST_DEVICE`.
            """
            self.type = type
            self.image_file = image_file
            self.host_device = host_device
            self.auto_detect = auto_detect
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.backing_info', {
            'type': type.ReferenceType(__name__, 'Floppy.BackingType'),
            'image_file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'auto_detect': type.OptionalType(type.BooleanType()),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Floppy.BackingSpec`` class provides a specification of the physical
        resource backing a virtual floppy drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'IMAGE_FILE' : [('image_file', True)],
                    'HOST_DEVICE' : [('host_device', False)],
                    'CLIENT_DEVICE' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     image_file=None,
                     host_device=None,
                    ):
            """
            :type  type: :class:`Floppy.BackingType`
            :param type: Backing type for the virtual floppy drive.
            :type  image_file: :class:`str`
            :param image_file: Path of the image file that should be used as the virtual floppy
                drive backing.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Floppy.BackingType.IMAGE_FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device that should be used as the virtual floppy drive
                backing.
                If None, the virtual floppy drive will be configured to
                automatically detect a suitable host device.
            """
            self.type = type
            self.image_file = image_file
            self.host_device = host_device
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.backing_spec', {
            'type': type.ReferenceType(__name__, 'Floppy.BackingType'),
            'image_file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
        },
        BackingSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Floppy.Info`` class contains information about a virtual floppy
        drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     label=None,
                     backing=None,
                     state=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  backing: :class:`Floppy.BackingInfo`
            :param backing: Physical resource backing for the virtual floppy drive.
            :type  state: :class:`ConnectionState`
            :param state: Connection status of the virtual device.
            :type  start_connected: :class:`bool`
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
            :type  allow_guest_control: :class:`bool`
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
            """
            self.label = label
            self.backing = backing
            self.state = state
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.info', {
            'label': type.StringType(),
            'backing': type.ReferenceType(__name__, 'Floppy.BackingInfo'),
            'state': type.ReferenceType(__name__, 'ConnectionState'),
            'start_connected': type.BooleanType(),
            'allow_guest_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Floppy.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual floppy drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  backing: :class:`Floppy.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual floppy drive.
                If None, defaults to automatic detection of a suitable host device.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                Defaults to false if None.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                Defaults to false if None.
            """
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.create_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Floppy.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Floppy.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual floppy drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  backing: :class:`Floppy.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual floppy drive. 
                
                This attribute may only be modified if the virtual machine is not
                powered on or the virtual floppy drive is not connected.
                If None, the value is unchanged.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                If None, the value is unchanged.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                If None, the value is unchanged.
            """
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.update_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Floppy.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Floppy.Summary`` class contains commonly used information about a
        virtual floppy drive.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     floppy=None,
                    ):
            """
            :type  floppy: :class:`str`
            :param floppy: Identifier of the virtual floppy drive.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Floppy``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Floppy``.
            """
            self.floppy = floppy
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.floppy.summary', {
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual floppy drives
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Floppy.Summary`
        :return: List of commonly used information about virtual floppy drives.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            floppy,
            ):
        """
        Returns information about a virtual floppy drive.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  floppy: :class:`str`
        :param floppy: Virtual floppy drive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :rtype: :class:`Floppy.Info`
        :return: Information about the specified virtual floppy drive.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual floppy drive is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'floppy': floppy,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual floppy drive to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Floppy.CreateSpec`
        :param spec: Specification for the new virtual floppy drive.
        :rtype: :class:`str`
        :return: Virtual floppy drive identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the floppy device was created but was
            unable to confirm the creation because the identifier of the new
            device could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the virtual machine already has the maximum number of supported
            floppy drives.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               floppy,
               spec,
               ):
        """
        Updates the configuration of a virtual floppy drive.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  floppy: :class:`str`
        :param floppy: Virtual floppy drive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :type  spec: :class:`Floppy.UpdateSpec`
        :param spec: Specification for updating the virtual floppy drive.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual floppy drive is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual floppy
            drive.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'floppy': floppy,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               floppy,
               ):
        """
        Removes a virtual floppy drive from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  floppy: :class:`str`
        :param floppy: Virtual floppy drive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual floppy drive is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'floppy': floppy,
                            })

    def connect(self,
                vm,
                floppy,
                ):
        """
        Connects a virtual floppy drive of a powered-on virtual machine to its
        backing. Connecting the virtual device makes the backing accessible
        from the perspective of the guest operating system. 
        
        For a powered-off virtual machine, the :func:`Floppy.update` method may
        be used to configure the virtual floppy drive to start in the connected
        state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  floppy: :class:`str`
        :param floppy: Virtual floppy drive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual floppy drive is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual floppy drive is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('connect',
                            {
                            'vm': vm,
                            'floppy': floppy,
                            })

    def disconnect(self,
                   vm,
                   floppy,
                   ):
        """
        Disconnects a virtual floppy drive of a powered-on virtual machine from
        its backing. The virtual device is still present and its backing
        configuration is unchanged, but from the perspective of the guest
        operating system, the floppy drive is not connected to its backing
        resource. 
        
        For a powered-off virtual machine, the :func:`Floppy.update` method may
        be used to configure the virtual floppy floppy to start in the
        disconnected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  floppy: :class:`str`
        :param floppy: Virtual floppy drive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.Floppy``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual floppy drive is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual floppy drive is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('disconnect',
                            {
                            'vm': vm,
                            'floppy': floppy,
                            })
class Memory(VapiInterface):
    """
    The ``Memory`` class provides methods for configuring the memory settings
    of a virtual machine.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MemoryStub)

    class Info(VapiStruct):
        """
        The ``Memory.Info`` class contains memory-related information about a
        virtual machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'size_MiB': 'size_mib',
                                'hot_add_increment_size_MiB': 'hot_add_increment_size_mib',
                                'hot_add_limit_MiB': 'hot_add_limit_mib',
                                }

        def __init__(self,
                     size_mib=None,
                     hot_add_enabled=None,
                     hot_add_increment_size_mib=None,
                     hot_add_limit_mib=None,
                    ):
            """
            :type  size_mib: :class:`long`
            :param size_mib: Memory size in mebibytes.
            :type  hot_add_enabled: :class:`bool`
            :param hot_add_enabled: Flag indicating whether adding memory while the virtual machine is
                running is enabled. 
                
                Some guest operating systems may consume more resources or perform
                less efficiently when they run on hardware that supports adding
                memory while the machine is running.
            :type  hot_add_increment_size_mib: :class:`long` or ``None``
            :param hot_add_increment_size_mib: The granularity, in mebibytes, at which memory can be added to a
                running virtual machine. 
                
                When adding memory to a running virtual machine, the amount of
                memory added must be at least
                :attr:`Memory.Info.hot_add_increment_size_mib` and the total memory
                size of the virtual machine must be a multiple of
                {\\\\@link>hotAddIncrementSize}.
                Only set when :attr:`Memory.Info.hot_add_enabled` is true and the
                virtual machine is running.
            :type  hot_add_limit_mib: :class:`long` or ``None``
            :param hot_add_limit_mib: The maximum amount of memory, in mebibytes, that can be added to a
                running virtual machine.
                Only set when :attr:`Memory.Info.hot_add_enabled` is true and the
                virtual machine is running.
            """
            self.size_mib = size_mib
            self.hot_add_enabled = hot_add_enabled
            self.hot_add_increment_size_mib = hot_add_increment_size_mib
            self.hot_add_limit_mib = hot_add_limit_mib
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.memory.info', {
            'size_MiB': type.IntegerType(),
            'hot_add_enabled': type.BooleanType(),
            'hot_add_increment_size_MiB': type.OptionalType(type.IntegerType()),
            'hot_add_limit_MiB': type.OptionalType(type.IntegerType()),
        },
        Info,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Memory.UpdateSpec`` class describes the updates to be made to the
        memory-related settings of a virtual machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'size_MiB': 'size_mib',
                                }

        def __init__(self,
                     size_mib=None,
                     hot_add_enabled=None,
                    ):
            """
            :type  size_mib: :class:`long` or ``None``
            :param size_mib: New memory size in mebibytes. 
                
                The supported range of memory sizes is constrained by the
                configured guest operating system and virtual hardware version of
                the virtual machine. 
                
                If the virtual machine is running, this value may only be changed
                if :attr:`Memory.Info.hot_add_enabled` is true, and the new memory
                size must satisfy the constraints specified by
                :attr:`Memory.Info.hot_add_increment_size_mib` and
                :attr:`Memory.Info.hot_add_limit_mib`.
                If None, the value is unchanged.
            :type  hot_add_enabled: :class:`bool` or ``None``
            :param hot_add_enabled: Flag indicating whether adding memory while the virtual machine is
                running should be enabled. 
                
                Some guest operating systems may consume more resources or perform
                less efficiently when they run on hardware that supports adding
                memory while the machine is running. 
                
                This attribute may only be modified if the virtual machine is not
                powered on.
                If None, the value is unchanged.
            """
            self.size_mib = size_mib
            self.hot_add_enabled = hot_add_enabled
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.memory.update_spec', {
            'size_MiB': type.OptionalType(type.IntegerType()),
            'hot_add_enabled': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns the memory-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Memory.Info`
        :return: Memory-related settings of the virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })

    def update(self,
               vm,
               spec,
               ):
        """
        Updates the memory-related settings of a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Memory.UpdateSpec`
        :param spec: Specification for updating the memory-related settings of the
            virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if one of the provided settings is not permitted; for example,
            specifying a negative value for ``sizeMiB``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if ``hotAddEnabled`` is specified and the virtual machine is not
            powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if ``sizeMiB`` is specified, ``hotAddEnabled`` is false, and the
            virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'spec': spec,
                            })
class Parallel(VapiInterface):
    """
    The ``Parallel`` class provides methods for configuring the virtual
    parallel ports of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.ParallelPort"
    """
    Resource type for the virtual parallel port.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ParallelStub)

    class BackingType(Enum):
        """
        The ``Parallel.BackingType`` class defines the valid backing types for a
        virtual parallel port.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FILE = None
        """
        Virtual parallel port is backed by a file.

        """
        HOST_DEVICE = None
        """
        Virtual parallel port is backed by a device on the host where the virtual
        machine is running.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('FILE'),
        BackingType('HOST_DEVICE'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.parallel.backing_type',
        BackingType))


    class BackingInfo(VapiStruct):
        """
        The ``Parallel.BackingInfo`` class contains information about the physical
        resource backing a virtual parallel port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('file', True)],
                    'HOST_DEVICE' : [('host_device', False), ('auto_detect', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     file=None,
                     host_device=None,
                     auto_detect=None,
                    ):
            """
            :type  type: :class:`Parallel.BackingType`
            :param type: Backing type for the virtual parallel port.
            :type  file: :class:`str`
            :param file: Path of the file backing the virtual parallel port.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Parallel.BackingType.FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device backing the virtual parallel port. 
                This attribute will be None if ``autoDetect`` is true and the
                virtual parallel port is not connected or no suitable device is
                available on the host.
            :type  auto_detect: :class:`bool`
            :param auto_detect: Flag indicating whether the virtual parallel port is configured to
                automatically detect a suitable host device.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Parallel.BackingType.HOST_DEVICE`.
            """
            self.type = type
            self.file = file
            self.host_device = host_device
            self.auto_detect = auto_detect
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.backing_info', {
            'type': type.ReferenceType(__name__, 'Parallel.BackingType'),
            'file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'auto_detect': type.OptionalType(type.BooleanType()),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Parallel.BackingSpec`` class provides a specification of the physical
        resource backing a virtual parallel port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('file', True)],
                    'HOST_DEVICE' : [('host_device', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     file=None,
                     host_device=None,
                    ):
            """
            :type  type: :class:`Parallel.BackingType`
            :param type: Backing type for the virtual parallel port.
            :type  file: :class:`str`
            :param file: Path of the file that should be used as the virtual parallel port
                backing.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Parallel.BackingType.FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device that should be used as the virtual parallel port
                backing.
                If None, the virtual parallel port will be configured to
                automatically detect a suitable host device.
            """
            self.type = type
            self.file = file
            self.host_device = host_device
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.backing_spec', {
            'type': type.ReferenceType(__name__, 'Parallel.BackingType'),
            'file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
        },
        BackingSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Parallel.Info`` class contains information about a virtual parallel
        port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     label=None,
                     backing=None,
                     state=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  backing: :class:`Parallel.BackingInfo`
            :param backing: Physical resource backing for the virtual parallel port.
            :type  state: :class:`ConnectionState`
            :param state: Connection status of the virtual device.
            :type  start_connected: :class:`bool`
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
            :type  allow_guest_control: :class:`bool`
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
            """
            self.label = label
            self.backing = backing
            self.state = state
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.info', {
            'label': type.StringType(),
            'backing': type.ReferenceType(__name__, 'Parallel.BackingInfo'),
            'state': type.ReferenceType(__name__, 'ConnectionState'),
            'start_connected': type.BooleanType(),
            'allow_guest_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Parallel.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual parallel port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  backing: :class:`Parallel.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual parallel port.
                If None, defaults to automatic detection of a suitable host device.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                Defaults to false if None.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                Defaults to false if None.
            """
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.create_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Parallel.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Parallel.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual parallel port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  backing: :class:`Parallel.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual parallel port. 
                
                This attribute may only be modified if the virtual machine is not
                powered on or the virtual parallel port is not connected.
                If None, the value is unchanged.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                If None, the value is unchanged.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                If None, the value is unchanged.
            """
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.update_spec', {
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Parallel.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Parallel.Summary`` class contains commonly used information about a
        virtual parallel port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     port=None,
                    ):
            """
            :type  port: :class:`str`
            :param port: Identifier of the virtual parallel port.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.ParallelPort``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.ParallelPort``.
            """
            self.port = port
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.parallel.summary', {
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual parallel ports
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Parallel.Summary`
        :return: List of commonly used information about virtual parallel ports.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            port,
            ):
        """
        Returns information about a virtual parallel port.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual parallel port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :rtype: :class:`Parallel.Info`
        :return: Information about the specified virtual parallel port.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual parallel port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual parallel port to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Parallel.CreateSpec`
        :param spec: Specification for the new virtual parallel port.
        :rtype: :class:`str`
        :return: Virtual parallel port identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the parallel port device was created
            but was unable to confirm the creation because the identifier of
            the new device could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the virtual machine already has the maximum number of supported
            parallel ports.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               port,
               spec,
               ):
        """
        Updates the configuration of a virtual parallel port.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual parallel port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :type  spec: :class:`Parallel.UpdateSpec`
        :param spec: Specification for updating the virtual parallel port.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual parallel port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual parallel
            port.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'port': port,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               port,
               ):
        """
        Removes a virtual parallel port from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual parallel port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual parallel port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def connect(self,
                vm,
                port,
                ):
        """
        Connects a virtual parallel port of a powered-on virtual machine to its
        backing. Connecting the virtual device makes the backing accessible
        from the perspective of the guest operating system. 
        
        For a powered-off virtual machine, the :func:`Parallel.update` method
        may be used to configure the virtual parallel port to start in the
        connected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual parallel port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual parallel port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual parallel port is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('connect',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def disconnect(self,
                   vm,
                   port,
                   ):
        """
        Disconnects a virtual parallel port of a powered-on virtual machine
        from its backing. The virtual device is still present and its backing
        configuration is unchanged, but from the perspective of the guest
        operating system, the parallel port is not connected to its backing. 
        
        For a powered-off virtual machine, the :func:`Parallel.update` method
        may be used to configure the virtual parallel port to start in the
        disconnected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual parallel port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ParallelPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual parallel port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual parallel port is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('disconnect',
                            {
                            'vm': vm,
                            'port': port,
                            })
class Serial(VapiInterface):
    """
    The ``Serial`` class provides methods for configuring the virtual serial
    ports of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.SerialPort"
    """
    Resource type for the virtual serial port device.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SerialStub)

    class BackingType(Enum):
        """
        The ``Serial.BackingType`` class defines the valid backing types for a
        virtual serial port.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FILE = None
        """
        Virtual serial port is backed by a file.

        """
        HOST_DEVICE = None
        """
        Virtual serial port is backed by a device on the host where the virtual
        machine is running.

        """
        PIPE_SERVER = None
        """
        Virtual serial port is backed by a named pipe server. The virtual machine
        will accept a connection from a host application or another virtual machine
        on the same host. This is useful for capturing debugging information sent
        through the virtual serial port.

        """
        PIPE_CLIENT = None
        """
        Virtual serial port is backed by a named pipe client. The virtual machine
        will connect to the named pipe provided by a host application or another
        virtual machine on the same host. This is useful for capturing debugging
        information sent through the virtual serial port.

        """
        NETWORK_SERVER = None
        """
        Virtual serial port is backed by a network server. This backing may be used
        to create a network-accessible serial port on the virtual machine,
        accepting a connection from a remote system.

        """
        NETWORK_CLIENT = None
        """
        Virtual serial port is backed by a network client. This backing may be used
        to create a network-accessible serial port on the virtual machine,
        initiating a connection to a remote system.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackingType` instance.
            """
            Enum.__init__(string)

    BackingType._set_values([
        BackingType('FILE'),
        BackingType('HOST_DEVICE'),
        BackingType('PIPE_SERVER'),
        BackingType('PIPE_CLIENT'),
        BackingType('NETWORK_SERVER'),
        BackingType('NETWORK_CLIENT'),
    ])
    BackingType._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.serial.backing_type',
        BackingType))


    class BackingInfo(VapiStruct):
        """
        The ``Serial.BackingInfo`` class contains information about the physical
        resource backing a virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('file', True)],
                    'HOST_DEVICE' : [('host_device', False), ('auto_detect', True)],
                    'PIPE_SERVER' : [('pipe', True), ('no_rx_loss', True)],
                    'PIPE_CLIENT' : [('pipe', True), ('no_rx_loss', True)],
                    'NETWORK_SERVER' : [('network_location', True), ('proxy', False)],
                    'NETWORK_CLIENT' : [('network_location', True), ('proxy', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     file=None,
                     host_device=None,
                     auto_detect=None,
                     pipe=None,
                     no_rx_loss=None,
                     network_location=None,
                     proxy=None,
                    ):
            """
            :type  type: :class:`Serial.BackingType`
            :param type: Backing type for the virtual serial port.
            :type  file: :class:`str`
            :param file: Path of the file backing the virtual serial port.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Serial.BackingType.FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device backing the virtual serial port. 
                This attribute will be None if ``autoDetect`` is true and the
                virtual serial port is not connected or no suitable device is
                available on the host.
            :type  auto_detect: :class:`bool`
            :param auto_detect: Flag indicating whether the virtual serial port is configured to
                automatically detect a suitable host device.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Serial.BackingType.HOST_DEVICE`.
            :type  pipe: :class:`str`
            :param pipe: Name of the pipe backing the virtual serial port.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Serial.BackingType.PIPE_SERVER` or
                :attr:`Serial.BackingType.PIPE_CLIENT`.
            :type  no_rx_loss: :class:`bool`
            :param no_rx_loss: Flag that enables optimized data transfer over the pipe. When the
                value is true, the host buffers data to prevent data overrun. This
                allows the virtual machine to read all of the data transferred over
                the pipe with no data loss.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Serial.BackingType.PIPE_SERVER` or
                :attr:`Serial.BackingType.PIPE_CLIENT`.
            :type  network_location: :class:`str`
            :param network_location: URI specifying the location of the network service backing the
                virtual serial port. 
                
                * If :attr:`Serial.BackingInfo.type` is
                  :attr:`Serial.BackingType.NETWORK_SERVER`, this attribute is the
                  location used by clients to connect to this server. The hostname
                  part of the URI should either be empty or should specify the
                  address of the host on which the virtual machine is running.
                * If :attr:`Serial.BackingInfo.type` is
                  :attr:`Serial.BackingType.NETWORK_CLIENT`, this attribute is the
                  location used by the virtual machine to connect to the remote
                  server.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Serial.BackingType.NETWORK_SERVER` or
                :attr:`Serial.BackingType.NETWORK_CLIENT`.
            :type  proxy: :class:`str` or ``None``
            :param proxy: Proxy service that provides network access to the network backing.
                If set, the virtual machine initiates a connection with the proxy
                service and forwards the traffic to the proxy.
                If None, no proxy service is configured.
            """
            self.type = type
            self.file = file
            self.host_device = host_device
            self.auto_detect = auto_detect
            self.pipe = pipe
            self.no_rx_loss = no_rx_loss
            self.network_location = network_location
            self.proxy = proxy
            VapiStruct.__init__(self)

    BackingInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.backing_info', {
            'type': type.ReferenceType(__name__, 'Serial.BackingType'),
            'file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'auto_detect': type.OptionalType(type.BooleanType()),
            'pipe': type.OptionalType(type.StringType()),
            'no_rx_loss': type.OptionalType(type.BooleanType()),
            'network_location': type.OptionalType(type.URIType()),
            'proxy': type.OptionalType(type.URIType()),
        },
        BackingInfo,
        False,
        None))


    class BackingSpec(VapiStruct):
        """
        The ``Serial.BackingSpec`` class provides a specification of the physical
        resource backing a virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('file', True)],
                    'HOST_DEVICE' : [('host_device', False)],
                    'PIPE_SERVER' : [('pipe', True), ('no_rx_loss', False)],
                    'PIPE_CLIENT' : [('pipe', True), ('no_rx_loss', False)],
                    'NETWORK_SERVER' : [('network_location', True), ('proxy', False)],
                    'NETWORK_CLIENT' : [('network_location', True), ('proxy', False)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     file=None,
                     host_device=None,
                     pipe=None,
                     no_rx_loss=None,
                     network_location=None,
                     proxy=None,
                    ):
            """
            :type  type: :class:`Serial.BackingType`
            :param type: Backing type for the virtual serial port.
            :type  file: :class:`str`
            :param file: Path of the file backing the virtual serial port.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Serial.BackingType.FILE`.
            :type  host_device: :class:`str` or ``None``
            :param host_device: Name of the device backing the virtual serial port. 
                If None, the virtual serial port will be configured to
                automatically detect a suitable host device.
            :type  pipe: :class:`str`
            :param pipe: Name of the pipe backing the virtual serial port.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Serial.BackingType.PIPE_SERVER` or
                :attr:`Serial.BackingType.PIPE_CLIENT`.
            :type  no_rx_loss: :class:`bool` or ``None``
            :param no_rx_loss: Flag that enables optimized data transfer over the pipe. When the
                value is true, the host buffers data to prevent data overrun. This
                allows the virtual machine to read all of the data transferred over
                the pipe with no data loss.
                If None, defaults to false.
            :type  network_location: :class:`str`
            :param network_location: URI specifying the location of the network service backing the
                virtual serial port. 
                
                * If :attr:`Serial.BackingSpec.type` is
                  :attr:`Serial.BackingType.NETWORK_SERVER`, this attribute is the
                  location used by clients to connect to this server. The hostname
                  part of the URI should either be empty or should specify the
                  address of the host on which the virtual machine is running.
                * If :attr:`Serial.BackingSpec.type` is
                  :attr:`Serial.BackingType.NETWORK_CLIENT`, this attribute is the
                  location used by the virtual machine to connect to the remote
                  server.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of :attr:`Serial.BackingType.NETWORK_SERVER` or
                :attr:`Serial.BackingType.NETWORK_CLIENT`.
            :type  proxy: :class:`str` or ``None``
            :param proxy: Proxy service that provides network access to the network backing.
                If set, the virtual machine initiates a connection with the proxy
                service and forwards the traffic to the proxy.
                If None, no proxy service should be used.
            """
            self.type = type
            self.file = file
            self.host_device = host_device
            self.pipe = pipe
            self.no_rx_loss = no_rx_loss
            self.network_location = network_location
            self.proxy = proxy
            VapiStruct.__init__(self)

    BackingSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.backing_spec', {
            'type': type.ReferenceType(__name__, 'Serial.BackingType'),
            'file': type.OptionalType(type.StringType()),
            'host_device': type.OptionalType(type.StringType()),
            'pipe': type.OptionalType(type.StringType()),
            'no_rx_loss': type.OptionalType(type.BooleanType()),
            'network_location': type.OptionalType(type.URIType()),
            'proxy': type.OptionalType(type.URIType()),
        },
        BackingSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Serial.Info`` class contains information about a virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     label=None,
                     yield_on_poll=None,
                     backing=None,
                     state=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  yield_on_poll: :class:`bool`
            :param yield_on_poll: CPU yield behavior. If set to true, the virtual machine will
                periodically relinquish the processor if its sole task is polling
                the virtual serial port. The amount of time it takes to regain the
                processor will depend on the degree of other virtual machine
                activity on the host.
            :type  backing: :class:`Serial.BackingInfo`
            :param backing: Physical resource backing for the virtual serial port.
            :type  state: :class:`ConnectionState`
            :param state: Connection status of the virtual device.
            :type  start_connected: :class:`bool`
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
            :type  allow_guest_control: :class:`bool`
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
            """
            self.label = label
            self.yield_on_poll = yield_on_poll
            self.backing = backing
            self.state = state
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.info', {
            'label': type.StringType(),
            'yield_on_poll': type.BooleanType(),
            'backing': type.ReferenceType(__name__, 'Serial.BackingInfo'),
            'state': type.ReferenceType(__name__, 'ConnectionState'),
            'start_connected': type.BooleanType(),
            'allow_guest_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Serial.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     yield_on_poll=None,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  yield_on_poll: :class:`bool` or ``None``
            :param yield_on_poll: CPU yield behavior. If set to true, the virtual machine will
                periodically relinquish the processor if its sole task is polling
                the virtual serial port. The amount of time it takes to regain the
                processor will depend on the degree of other virtual machine
                activity on the host.
                If None, defaults to false.
            :type  backing: :class:`Serial.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual serial port.
                If None, defaults to automatic detection of a suitable host device.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                Defaults to false if None.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                Defaults to false if None.
            """
            self.yield_on_poll = yield_on_poll
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.create_spec', {
            'yield_on_poll': type.OptionalType(type.BooleanType()),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Serial.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Serial.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     yield_on_poll=None,
                     backing=None,
                     start_connected=None,
                     allow_guest_control=None,
                    ):
            """
            :type  yield_on_poll: :class:`bool` or ``None``
            :param yield_on_poll: CPU yield behavior. If set to true, the virtual machine will
                periodically relinquish the processor if its sole task is polling
                the virtual serial port. The amount of time it takes to regain the
                processor will depend on the degree of other virtual machine
                activity on the host. 
                
                This attribute may be modified at any time, and changes applied to
                a connected virtual serial port take effect immediately.
                If None, the value is unchanged.
            :type  backing: :class:`Serial.BackingSpec` or ``None``
            :param backing: Physical resource backing for the virtual serial port. 
                
                This attribute may only be modified if the virtual machine is not
                powered on or the virtual serial port is not connected.
                If None, the value is unchanged.
            :type  start_connected: :class:`bool` or ``None``
            :param start_connected: Flag indicating whether the virtual device should be connected
                whenever the virtual machine is powered on.
                If None, the value is unchanged.
            :type  allow_guest_control: :class:`bool` or ``None``
            :param allow_guest_control: Flag indicating whether the guest can connect and disconnect the
                device.
                If None, the value is unchanged.
            """
            self.yield_on_poll = yield_on_poll
            self.backing = backing
            self.start_connected = start_connected
            self.allow_guest_control = allow_guest_control
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.update_spec', {
            'yield_on_poll': type.OptionalType(type.BooleanType()),
            'backing': type.OptionalType(type.ReferenceType(__name__, 'Serial.BackingSpec')),
            'start_connected': type.OptionalType(type.BooleanType()),
            'allow_guest_control': type.OptionalType(type.BooleanType()),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Serial.Summary`` class contains commonly used information about a
        virtual serial port.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     port=None,
                    ):
            """
            :type  port: :class:`str`
            :param port: Identifier of the virtual serial port.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.SerialPort``. When methods return
                a value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.SerialPort``.
            """
            self.port = port
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.serial.summary', {
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual serial ports
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Serial.Summary`
        :return: List of commonly used information about virtual serial ports.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'vm': vm,
                            })

    def get(self,
            vm,
            port,
            ):
        """
        Returns information about a virtual serial port.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual serial port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :rtype: :class:`Serial.Info`
        :return: Information about the specified virtual serial port.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual serial port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual serial port to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Serial.CreateSpec`
        :param spec: Specification for the new virtual serial port.
        :rtype: :class:`str`
        :return: Virtual serial port identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the serial port device was created but
            was unable to confirm the creation because the identifier of the
            new device could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if the virtual machine already has the maximum number of supported
            serial ports.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('create',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def update(self,
               vm,
               port,
               spec,
               ):
        """
        Updates the configuration of a virtual serial port.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual serial port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :type  spec: :class:`Serial.UpdateSpec`
        :param spec: Specification for updating the virtual serial port.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual serial port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual serial port.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'port': port,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               port,
               ):
        """
        Removes a virtual serial port from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual serial port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual serial port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered off.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('delete',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def connect(self,
                vm,
                port,
                ):
        """
        Connects a virtual serial port of a powered-on virtual machine to its
        backing. Connecting the virtual device makes the backing accessible
        from the perspective of the guest operating system. 
        
        For a powered-off virtual machine, the :func:`Serial.update` method may
        be used to configure the virtual serial port to start in the connected
        state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual serial port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual serial port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual serial port is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('connect',
                            {
                            'vm': vm,
                            'port': port,
                            })

    def disconnect(self,
                   vm,
                   port,
                   ):
        """
        Disconnects a virtual serial port of a powered-on virtual machine from
        its backing. The virtual device is still present and its backing
        configuration is unchanged, but from the perspective of the guest
        operating system, the serial port is not connected to its backing. 
        
        For a powered-off virtual machine, the :func:`Serial.update` method may
        be used to configure the virtual serial port to start in the
        disconnected state when the virtual machine is powered on.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  port: :class:`str`
        :param port: Virtual serial port identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SerialPort``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual serial port is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the virtual serial port is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is not powered on.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine is busy performing another operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('disconnect',
                            {
                            'vm': vm,
                            'port': port,
                            })
class _BootStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/boot',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Boot.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/boot',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Boot.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.boot',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _CdromStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/cdrom',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/cdrom/{cdrom}',
            path_variables={
                'vm': 'vm',
                'cdrom': 'cdrom',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Cdrom.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/cdrom',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
            'spec': type.ReferenceType(__name__, 'Cdrom.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/cdrom/{cdrom}',
            path_variables={
                'vm': 'vm',
                'cdrom': 'cdrom',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/cdrom/{cdrom}',
            path_variables={
                'vm': 'vm',
                'cdrom': 'cdrom',
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        connect_input_value_validator_list = [
        ]
        connect_output_validator_list = [
        ]
        connect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/cdrom/{cdrom}/connect',
            path_variables={
                'vm': 'vm',
                'cdrom': 'cdrom',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'cdrom': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disconnect_input_value_validator_list = [
        ]
        disconnect_output_validator_list = [
        ]
        disconnect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/cdrom/{cdrom}/disconnect',
            path_variables={
                'vm': 'vm',
                'cdrom': 'cdrom',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Cdrom.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Cdrom.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Cdrom'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
            'connect': {
                'input_type': connect_input_type,
                'output_type': type.VoidType(),
                'errors': connect_error_dict,
                'input_value_validator_list': connect_input_value_validator_list,
                'output_validator_list': connect_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disconnect': {
                'input_type': disconnect_input_type,
                'output_type': type.VoidType(),
                'errors': disconnect_error_dict,
                'input_value_validator_list': disconnect_input_value_validator_list,
                'output_validator_list': disconnect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.cdrom',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _CpuStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/cpu',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Cpu.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/cpu',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Cpu.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.cpu',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DiskStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/disk',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'disk': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/disk/{disk}',
            path_variables={
                'vm': 'vm',
                'disk': 'disk',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Disk.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/disk',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'disk': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
            'spec': type.ReferenceType(__name__, 'Disk.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/disk/{disk}',
            path_variables={
                'vm': 'vm',
                'disk': 'disk',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'disk': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/disk/{disk}',
            path_variables={
                'vm': 'vm',
                'disk': 'disk',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Disk.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Disk.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Disk'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.disk',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _EthernetStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/ethernet',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/ethernet/{nic}',
            path_variables={
                'vm': 'vm',
                'nic': 'nic',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Ethernet.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/ethernet',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
            'spec': type.ReferenceType(__name__, 'Ethernet.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/ethernet/{nic}',
            path_variables={
                'vm': 'vm',
                'nic': 'nic',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/ethernet/{nic}',
            path_variables={
                'vm': 'vm',
                'nic': 'nic',
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        connect_input_value_validator_list = [
        ]
        connect_output_validator_list = [
        ]
        connect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/ethernet/{nic}/connect',
            path_variables={
                'vm': 'vm',
                'nic': 'nic',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'nic': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disconnect_input_value_validator_list = [
        ]
        disconnect_output_validator_list = [
        ]
        disconnect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/ethernet/{nic}/disconnect',
            path_variables={
                'vm': 'vm',
                'nic': 'nic',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Ethernet.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Ethernet.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Ethernet'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
            'connect': {
                'input_type': connect_input_type,
                'output_type': type.VoidType(),
                'errors': connect_error_dict,
                'input_value_validator_list': connect_input_value_validator_list,
                'output_validator_list': connect_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disconnect': {
                'input_type': disconnect_input_type,
                'output_type': type.VoidType(),
                'errors': disconnect_error_dict,
                'input_value_validator_list': disconnect_input_value_validator_list,
                'output_validator_list': disconnect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.ethernet',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _FloppyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/floppy',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/floppy/{floppy}',
            path_variables={
                'vm': 'vm',
                'floppy': 'floppy',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Floppy.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/floppy',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
            'spec': type.ReferenceType(__name__, 'Floppy.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/floppy/{floppy}',
            path_variables={
                'vm': 'vm',
                'floppy': 'floppy',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/floppy/{floppy}',
            path_variables={
                'vm': 'vm',
                'floppy': 'floppy',
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        connect_input_value_validator_list = [
        ]
        connect_output_validator_list = [
        ]
        connect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/floppy/{floppy}/connect',
            path_variables={
                'vm': 'vm',
                'floppy': 'floppy',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'floppy': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disconnect_input_value_validator_list = [
        ]
        disconnect_output_validator_list = [
        ]
        disconnect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/floppy/{floppy}/disconnect',
            path_variables={
                'vm': 'vm',
                'floppy': 'floppy',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Floppy.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Floppy.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.Floppy'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
            'connect': {
                'input_type': connect_input_type,
                'output_type': type.VoidType(),
                'errors': connect_error_dict,
                'input_value_validator_list': connect_input_value_validator_list,
                'output_validator_list': connect_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disconnect': {
                'input_type': disconnect_input_type,
                'output_type': type.VoidType(),
                'errors': disconnect_error_dict,
                'input_value_validator_list': disconnect_input_value_validator_list,
                'output_validator_list': disconnect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.floppy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _MemoryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/memory',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Memory.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/memory',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Memory.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.memory',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ParallelStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/parallel',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/parallel/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Parallel.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/parallel',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
            'spec': type.ReferenceType(__name__, 'Parallel.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/parallel/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/parallel/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        connect_input_value_validator_list = [
        ]
        connect_output_validator_list = [
        ]
        connect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/parallel/{port}/connect',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disconnect_input_value_validator_list = [
        ]
        disconnect_output_validator_list = [
        ]
        disconnect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/parallel/{port}/disconnect',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Parallel.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Parallel.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ParallelPort'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
            'connect': {
                'input_type': connect_input_type,
                'output_type': type.VoidType(),
                'errors': connect_error_dict,
                'input_value_validator_list': connect_input_value_validator_list,
                'output_validator_list': connect_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disconnect': {
                'input_type': disconnect_input_type,
                'output_type': type.VoidType(),
                'errors': disconnect_error_dict,
                'input_value_validator_list': disconnect_input_value_validator_list,
                'output_validator_list': disconnect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.parallel',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SerialStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/serial',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/vm/{vm}/hardware/serial/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Serial.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/serial',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
            'spec': type.ReferenceType(__name__, 'Serial.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/hardware/serial/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vcenter/vm/{vm}/hardware/serial/{port}',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        connect_input_value_validator_list = [
        ]
        connect_output_validator_list = [
        ]
        connect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/serial/{port}/connect',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'port': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        disconnect_input_value_validator_list = [
        ]
        disconnect_output_validator_list = [
        ]
        disconnect_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/hardware/serial/{port}/disconnect',
            path_variables={
                'vm': 'vm',
                'port': 'port',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Serial.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Serial.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SerialPort'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
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
            'connect': {
                'input_type': connect_input_type,
                'output_type': type.VoidType(),
                'errors': connect_error_dict,
                'input_value_validator_list': connect_input_value_validator_list,
                'output_validator_list': connect_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'disconnect': {
                'input_type': disconnect_input_type,
                'output_type': type.VoidType(),
                'errors': disconnect_error_dict,
                'input_value_validator_list': disconnect_input_value_validator_list,
                'output_validator_list': disconnect_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.serial',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Boot': Boot,
        'Cdrom': Cdrom,
        'Cpu': Cpu,
        'Disk': Disk,
        'Ethernet': Ethernet,
        'Floppy': Floppy,
        'Memory': Memory,
        'Parallel': Parallel,
        'Serial': Serial,
        'adapter': 'com.vmware.vcenter.vm.hardware.adapter_client.StubFactory',
        'boot': 'com.vmware.vcenter.vm.hardware.boot_client.StubFactory',
    }

