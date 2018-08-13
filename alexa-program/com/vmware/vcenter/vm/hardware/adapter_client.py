# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.hardware.adapter.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm.hardware.adapter_client`` module provides classes
for managing the configuration and state of the virtual adapters belonging to a
virtual machine. This includes methods for reading and manipulating the
conifguration of USB adapters and host bus adapters. 

Note that classes for adapters with no configurable properties or runtime
state, such as IDE and PCI adapters, are omitted.

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


class Sata(VapiInterface):
    """
    The ``Sata`` class provides methods for configuring the virtual SATA
    adapters of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.SataAdapter"
    """
    Resource type for the virtual SATA adapter device.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SataStub)

    class Type(Enum):
        """
        The ``Sata.Type`` class defines the valid emulation types for a virtual
        SATA adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        AHCI = None
        """
        AHCI host bus adapter.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('AHCI'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.adapter.sata.type',
        Type))


    class Info(VapiStruct):
        """
        The ``Sata.Info`` class contains information about a virtual SATA adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     label=None,
                     type=None,
                     bus=None,
                     pci_slot_number=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  type: :class:`Sata.Type`
            :param type: Adapter type.
            :type  bus: :class:`long`
            :param bus: SATA bus number.
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the SATA adapter on the PCI bus.
                May be None if the virtual machine has never been powered on since
                the adapter was created.
            """
            self.label = label
            self.type = type
            self.bus = bus
            self.pci_slot_number = pci_slot_number
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.sata.info', {
            'label': type.StringType(),
            'type': type.ReferenceType(__name__, 'Sata.Type'),
            'bus': type.IntegerType(),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Sata.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual SATA adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                     bus=None,
                     pci_slot_number=None,
                    ):
            """
            :type  type: :class:`Sata.Type` or ``None``
            :param type: Adapter type.
                If None, a guest-specific default value will be used.
            :type  bus: :class:`long` or ``None``
            :param bus: SATA bus number.
                If None, the server will choose an available bus number; if none is
                available, the request will fail.
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the SATA adapter on the PCI bus.
                If None, the server will choose an available address when the
                virtual machine is powered on.
            """
            self.type = type
            self.bus = bus
            self.pci_slot_number = pci_slot_number
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.sata.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Sata.Type')),
            'bus': type.OptionalType(type.IntegerType()),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
        },
        CreateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Sata.Summary`` class contains commonly used information about a
        Virtual SATA adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     adapter=None,
                    ):
            """
            :type  adapter: :class:`str`
            :param adapter: Identifier of the virtual SATA adapter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.SataAdapter``. When methods return
                a value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.SataAdapter``.
            """
            self.adapter = adapter
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.sata.summary', {
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SataAdapter'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual SATA adapters
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Sata.Summary`
        :return: List of commonly used information about virtual SATA adapters.
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
            adapter,
            ):
        """
        Returns information about a virtual SATA adapter.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  adapter: :class:`str`
        :param adapter: Virtual SATA adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SataAdapter``.
        :rtype: :class:`Sata.Info`
        :return: Information about the specified virtual SATA adapter.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual SATA adapter is not found.
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
                            'adapter': adapter,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual SATA adapter to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Sata.CreateSpec`
        :param spec: Specification for the new virtual SATA adapter.
        :rtype: :class:`str`
        :return: Virtual SATA adapter identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SataAdapter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the SATA adapter was created but was
            unable to confirm the creation because the identifier of the new
            adapter could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if there are no more available SATA buses on the virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the specified SATA bus or PCI address is in use.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the specified SATA bus or PCI address is out of bounds.
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

    def delete(self,
               vm,
               adapter,
               ):
        """
        Removes a virtual SATA adapter from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  adapter: :class:`str`
        :param adapter: Virtual SATA adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.SataAdapter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual SATA adapter is not found.
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
                            'adapter': adapter,
                            })
class Scsi(VapiInterface):
    """
    The ``Scsi`` class provides methods for configuring the virtual SCSI
    adapters of a virtual machine.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.vm.hardware.ScsiAdapter"
    """
    Resource type for the virtual SCSI adapter device.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ScsiStub)

    class Type(Enum):
        """
        The ``Scsi.Type`` class defines the valid emulation types for a virtual
        SCSI adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BUSLOGIC = None
        """
        BusLogic host bus adapter.

        """
        LSILOGIC = None
        """
        LSI Logic host bus adapter.

        """
        LSILOGICSAS = None
        """
        LSI Logic SAS 1068 host bus adapter.

        """
        PVSCSI = None
        """
        Paravirtualized host bus adapter.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('BUSLOGIC'),
        Type('LSILOGIC'),
        Type('LSILOGICSAS'),
        Type('PVSCSI'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.type',
        Type))


    class Sharing(Enum):
        """
        The ``Scsi.Sharing`` class defines the valid bus sharing modes for a
        virtual SCSI adapter.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NONE = None
        """
        The virtual SCSI bus is not shared.

        """
        VIRTUAL = None
        """
        The virtual SCSI bus is shared between two or more virtual machines. In
        this case, no physical machine is involved.

        """
        PHYSICAL = None
        """
        The virtual SCSI bus is shared between two or more virtual machines
        residing on different physical hosts.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Sharing` instance.
            """
            Enum.__init__(string)

    Sharing._set_values([
        Sharing('NONE'),
        Sharing('VIRTUAL'),
        Sharing('PHYSICAL'),
    ])
    Sharing._set_binding_type(type.EnumType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.sharing',
        Sharing))


    class Info(VapiStruct):
        """
        The ``Scsi.Info`` class contains information about a virtual SCSI adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     label=None,
                     type=None,
                     scsi=None,
                     pci_slot_number=None,
                     sharing=None,
                    ):
            """
            :type  label: :class:`str`
            :param label: Device label.
            :type  type: :class:`Scsi.Type`
            :param type: Adapter type.
            :type  scsi: :class:`com.vmware.vcenter.vm.hardware_client.ScsiAddressInfo`
            :param scsi: Address of the SCSI adapter on the SCSI bus.
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the SCSI adapter on the PCI bus. If the PCI address is
                invalid, the server will change it when the VM is started or as the
                device is hot added.
                May be None if the virtual machine has never been powered on since
                the adapter was created.
            :type  sharing: :class:`Scsi.Sharing`
            :param sharing: Bus sharing mode.
            """
            self.label = label
            self.type = type
            self.scsi = scsi
            self.pci_slot_number = pci_slot_number
            self.sharing = sharing
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.info', {
            'label': type.StringType(),
            'type': type.ReferenceType(__name__, 'Scsi.Type'),
            'scsi': type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'ScsiAddressInfo'),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
            'sharing': type.ReferenceType(__name__, 'Scsi.Sharing'),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Scsi.CreateSpec`` class provides a specification for the
        configuration of a newly-created virtual SCSI adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                     bus=None,
                     pci_slot_number=None,
                     sharing=None,
                    ):
            """
            :type  type: :class:`Scsi.Type` or ``None``
            :param type: Adapter type.
                If None, a guest-specific default value will be used.
            :type  bus: :class:`long` or ``None``
            :param bus: SCSI bus number.
                If None, the server will choose an available bus number; if none is
                available, the request will fail.
            :type  pci_slot_number: :class:`long` or ``None``
            :param pci_slot_number: Address of the SCSI adapter on the PCI bus. If the PCI address is
                invalid, the server will change it when the VM is started or as the
                device is hot added.
                If None, the server will choose an available address when the
                virtual machine is powered on.
            :type  sharing: :class:`Scsi.Sharing` or ``None``
            :param sharing: Bus sharing mode.
                If None, the adapter will default to :attr:`Scsi.Sharing.NONE`.
            """
            self.type = type
            self.bus = bus
            self.pci_slot_number = pci_slot_number
            self.sharing = sharing
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.create_spec', {
            'type': type.OptionalType(type.ReferenceType(__name__, 'Scsi.Type')),
            'bus': type.OptionalType(type.IntegerType()),
            'pci_slot_number': type.OptionalType(type.IntegerType()),
            'sharing': type.OptionalType(type.ReferenceType(__name__, 'Scsi.Sharing')),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Scsi.UpdateSpec`` class describes the updates to be made to the
        configuration of a virtual SCSI adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     sharing=None,
                    ):
            """
            :type  sharing: :class:`Scsi.Sharing` or ``None``
            :param sharing: Bus sharing mode. 
                
                This attribute may only be modified if the virtual machine is not
                powered on.
                If None, the value is unchanged.
            """
            self.sharing = sharing
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.update_spec', {
            'sharing': type.OptionalType(type.ReferenceType(__name__, 'Scsi.Sharing')),
        },
        UpdateSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Scsi.Summary`` class contains commonly used information about a
        Virtual SCSI adapter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     adapter=None,
                    ):
            """
            :type  adapter: :class:`str`
            :param adapter: Identifier of the virtual SCSI adapter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.ScsiAdapter``. When methods return
                a value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
            """
            self.adapter = adapter
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.hardware.adapter.scsi.summary', {
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ScsiAdapter'),
        },
        Summary,
        False,
        None))



    def list(self,
             vm,
             ):
        """
        Returns commonly used information about the virtual SCSI adapters
        belonging to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`list` of :class:`Scsi.Summary`
        :return: List of commonly used information about virtual SCSI adapters.
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
            adapter,
            ):
        """
        Returns information about a virtual SCSI adapter.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  adapter: :class:`str`
        :param adapter: Virtual SCSI adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
        :rtype: :class:`Scsi.Info`
        :return: Information about the specified virtual SCSI adapter.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual SCSI adapter is not found.
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
                            'adapter': adapter,
                            })

    def create(self,
               vm,
               spec,
               ):
        """
        Adds a virtual SCSI adapter to the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Scsi.CreateSpec`
        :param spec: Specification for the new virtual SCSI adapter.
        :rtype: :class:`str`
        :return: Virtual SCSI adapter identifier.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reported that the SCSI adapter was created but was
            unable to confirm the creation because the identifier of the new
            adapter could not be determined.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if there are no more available SCSI buses on the virtual machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the specified SCSI bus is in use.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the specified SATA bus or PCI address is out of bounds.
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
               adapter,
               spec,
               ):
        """
        Updates the configuration of a virtual SCSI adapter.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  adapter: :class:`str`
        :param adapter: Virtual SCSI adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
        :type  spec: :class:`Scsi.UpdateSpec`
        :param spec: Specification for updating the virtual SCSI adapter.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual SCSI adapter is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if one or more of the attributes specified in the ``spec``
            parameter cannot be modified due to the current power state of the
            virtual machine or the connection state of the virtual SCSI
            adapter.
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
                            'adapter': adapter,
                            'spec': spec,
                            })

    def delete(self,
               vm,
               adapter,
               ):
        """
        Removes a virtual SCSI adapter from the virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  adapter: :class:`str`
        :param adapter: Virtual SCSI adapter identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is suspended
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine or virtual SCSI adapter is not found.
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
                            'adapter': adapter,
                            })
class _SataStub(ApiInterfaceStub):
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/sata',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SataAdapter'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/sata/{adapter}',
            path_variables={
                'vm': 'vm',
                'adapter': 'adapter',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Sata.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/sata',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SataAdapter'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/sata/{adapter}',
            path_variables={
                'vm': 'vm',
                'adapter': 'adapter',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Sata.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Sata.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.SataAdapter'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
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
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.hardware.adapter.sata',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ScsiStub(ApiInterfaceStub):
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/scsi',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ScsiAdapter'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}',
            path_variables={
                'vm': 'vm',
                'adapter': 'adapter',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Scsi.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/scsi',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ScsiAdapter'),
            'spec': type.ReferenceType(__name__, 'Scsi.UpdateSpec'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}',
            path_variables={
                'vm': 'vm',
                'adapter': 'adapter',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'adapter': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ScsiAdapter'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
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
            url_template='/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}',
            path_variables={
                'vm': 'vm',
                'adapter': 'adapter',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Scsi.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Scsi.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.vcenter.vm.hardware.ScsiAdapter'),
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
            self, iface_name='com.vmware.vcenter.vm.hardware.adapter.scsi',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Sata': Sata,
        'Scsi': Scsi,
    }

