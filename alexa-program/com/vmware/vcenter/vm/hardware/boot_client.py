# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.hardware.boot.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm.hardware.boot_client`` module provides classes for
managing the virtual devices used to boot a virtual machine.

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


class Device(VapiInterface):
    """
    The ``Device`` class provides methods for configuring the device order used
    when booting a virtual machine. 
    
    The boot order may be specified using a mixture of device classes and
    device instances, chosen from among the following: 
    
    * :attr:`Device.Type.CDROM`: Boot from a virtual CD-ROM drive; the device
      instance(s) will be chosen by the BIOS subsystem.
    * :attr:`Device.Type.FLOPPY`: Boot from a virtual floppy drive; the device
      instance(s) will be chosen by the BIOS subsystem.
    * :attr:`Device.Type.DISK`: Boot from a virtual disk device; the device
      instance is specified explicitly in :attr:`Device.Entry.disks` list, and
      multiple instances may be specified in the list.
    * :attr:`Device.Type.ETHERNET`: Boot from a virtual Ethernet adapter; the
      device instance is specified explicitly as :attr:`Device.Entry.nic`, and
      multiple adapters may be specified in the boot order list.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DeviceStub)

    class Type(Enum):
        """
        The ``Device.Type`` class defines the valid device types that may be used
        as bootable devices.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        CDROM = None
        """
        Virtual CD-ROM device.

        """
        DISK = None
        """
        Virtual disk device.

        """
        ETHERNET = None
        """
        Virtual Ethernet adapter.

        """
        FLOPPY = None
        """
        Virtual floppy drive.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('CDROM'),
        Type('DISK'),
        Type('ETHERNET'),
        Type('FLOPPY'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.boot.device.type',
        Type))


    class EntryCreateSpec(VapiStruct):
        """
        The class ``Device.EntryCreateSpec`` specifies a list of bootable virtual
        device classes. When a VM is being created and a :class:`list` of
        ``Device.EntryCreateSpec`` is specified, the boot order of the specific
        device instances are not specified in this class. The boot order of the
        specific device instance will be the order in which the Ethernet and Disk
        devices appear in the ``nics`` and ``disks`` respectively.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                    ):
            """
            :type  type: :class:`Device.Type`
            :param type: Virtual Boot device type.
            """
            self.type = type
            VapiStruct.__init__(self)

    EntryCreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.boot.device.entry_create_spec', {
            'type': type.ReferenceType(__name__, 'Device.Type'),
        },
        EntryCreateSpec,
        False,
        None))


    class Entry(VapiStruct):
        """
        The ``Device.Entry`` class specifies a bootable virtual device class or
        specific bootable virtual device(s).

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'ETHERNET' : [('nic', True)],
                    'DISK' : [('disks', True)],
                    'CDROM' : [],
                    'FLOPPY' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     nic=None,
                     disks=None,
                    ):
            """
            :type  type: :class:`Device.Type`
            :param type: Virtual device type.
            :type  nic: :class:`str`
            :param nic: Virtual Ethernet device. Ethernet device to use as boot device for
                this entry.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Ethernet``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Ethernet``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Device.Type.ETHERNET`.
            :type  disks: :class:`list` of :class:`str`
            :param disks: Virtual disk device. List of virtual disks in boot order.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is :attr:`Device.Type.DISK`.
            """
            self.type = type
            self.nic = nic
            self.disks = disks
            VapiStruct.__init__(self)

    Entry._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.boot.device.entry', {
            'type': type.ReferenceType(__name__, 'Device.Type'),
            'nic': type.OptionalType(type.IdType()),
            'disks': type.OptionalType(type.ListType(type.IdType())),
        },
        Entry,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns an ordered list of boot devices for the virtual machine. If the
        :class:`list` is empty, the virtual machine uses a default boot
        sequence.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Device.Entry`
        :return: Ordered list of configured boot devices.
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

    def set(self,
            vm,
            devices,
            ):
        """
        Sets the virtual devices that will be used to boot the virtual machine.
        The virtual machine will check the devices in order, attempting to boot
        from each, until the virtual machine boots successfully. If the
        :class:`list` is empty, the virtual machine will use a default boot
        sequence. There should be no more than one instance of
        :class:`Device.Entry` for a given device type except
        :attr:`Device.Type.ETHERNET` in the :class:`list`.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  devices: :class:`list` of :class:`Device.Entry`
        :param devices: Ordered list of boot devices.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found, or if any of the specified
            virtual devices is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if a any of the CDROM, DISK, ETHERNET, FLOPPY values appears in
            more than one ``Device.Entry`` with the exception of
            :attr:`Device.Type.ETHERNET`, which may appear multiple times if
            the virtual machine has been configured with multiple Ethernet
            adapters.
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
        return self._invoke('set',
                            {
                            'vm': vm,
                            'devices': devices,
                            })
class _DeviceStub(ApiInterfaceStub):
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
            url_template='/vcenter/vm/{vm}/hardware/boot/device',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'devices': type.ListType(type.ReferenceType(__name__, 'Device.Entry')),
        })
        set_error_dict = {
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
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/vcenter/vm/{vm}/hardware/boot/device',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Device.Entry')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.boot.device',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Device': Device,
    }

