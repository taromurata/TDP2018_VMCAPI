# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm_template.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.vm_template_client`` module provides classes and
classes that will let its client manage VMTX template in Content Library.

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


class LibraryItems(VapiInterface):
    """
    The ``LibraryItems`` class provides methods to deploy virtual machines from
    library items containing virtual machine templates, as well as methods to
    create library items containing virtual machine templates. The
    ``LibraryItems`` class also provides an operation to retrieve information
    about the template contained in the library item. This class was added in
    vSphere API 6.8
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LibraryItemsStub)

    class CreateSpec(VapiStruct):
        """
        The ``LibraryItems.CreateSpec`` class defines the information required to
        create a library item containing a virtual machine template. This class was
        added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     source_vm=None,
                     name=None,
                     description=None,
                     library=None,
                     vm_home_storage=None,
                     disk_storage=None,
                     disk_storage_overrides=None,
                     placement=None,
                    ):
            """
            :type  source_vm: :class:`str`
            :param source_vm: Identifier of the source virtual machine to create the library item
                from. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``VirtualMachine``.
            :type  name: :class:`str`
            :param name: Name of the library item. This attribute was added in vSphere API
                6.8
            :type  description: :class:`str` or ``None``
            :param description: Description of the library item. This attribute was added in
                vSphere API 6.8
                If None, the newly created library item has the same description as
                the source virtual machine.
            :type  library: :class:`str`
            :param library: Identifier of the library in which the new library item should be
                created. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
            :type  vm_home_storage: :class:`LibraryItems.CreateSpecVmHomeStorage` or ``None``
            :param vm_home_storage: Storage location for the virtual machine template's configuration
                and log files. This attribute was added in vSphere API 6.8
                If None, the virtual machine template's configuration and log files
                are placed on the default storage backing associated with the
                library specified by ``library``.
            :type  disk_storage: :class:`LibraryItems.CreateSpecDiskStorage` or ``None``
            :param disk_storage: Storage specification for the virtual machine template's disks.
                This attribute was added in vSphere API 6.8
                If both ``diskStorageOverrides`` and ``diskStorage`` are None, the
                virtual machine template's disks are placed in the default storage
                backing associated with the library specified by ``library``. 
                
                If ``diskStorageOverrides`` is None and ``diskStorage`` is
                specified, all of the virtual machine template's disks are created
                with the storage spec specified by ``diskStorage``. 
                
                If ``diskStorageOverrides`` is specified and ``diskStorage`` is
                None, disks with identifiers that are not in
                ``diskStorageOverrides`` are placed in the default storage backing
                associated with the library specified by ``library``. 
                
                If both ``diskStorageOverrides`` and ``diskStorage`` are specified,
                disks with identifiers that are not in ``diskStorageOverrides`` are
                created with the storage spec specified by ``diskStorage``. 
            :type  disk_storage_overrides: (:class:`dict` of :class:`str` and :class:`LibraryItems.CreateSpecDiskStorage`) or ``None``
            :param disk_storage_overrides: Storage specification for individual disks in the virtual machine
                template. This is specified as a mapping between disk identifiers
                in the source virtual machine and their respective storage
                specifications. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If both ``diskStorageOverrides`` and ``diskStorage`` are None, the
                virtual machine template's disks are placed in the default storage
                backing associated with the library specified by ``library``. 
                
                If ``diskStorageOverrides`` is None and ``diskStorage`` is
                specified, all of the virtual machine template's disks are created
                with the storage spec specified by ``diskStorage``. 
                
                If ``diskStorageOverrides`` is specified and ``diskStorage`` is
                None, disks with identifiers that are not in
                ``diskStorageOverrides`` are placed in the default storage backing
                associated with the library specified by ``library``. 
                
                If both ``diskStorageOverrides`` and ``diskStorage`` are specified,
                disks with identifiers that are not in ``diskStorageOverrides`` are
                created with the storage spec specified by ``diskStorage``. 
            :type  placement: :class:`LibraryItems.CreatePlacementSpec` or ``None``
            :param placement: Information used to place the virtual machine template. This
                attribute was added in vSphere API 6.8
                This attribute is currently required. In the future, if this
                attribute is None, the system will place the virtual machine
                template on a suitable resource. 
                
                If specified, each attribute will be used for placement. If the
                attributes result in disjoint placement, the operation will fail.
                If the attributes along with the placement values of the source
                virtual machine result in disjoint placement, the operation will
                fail. 
            """
            self.source_vm = source_vm
            self.name = name
            self.description = description
            self.library = library
            self.vm_home_storage = vm_home_storage
            self.disk_storage = disk_storage
            self.disk_storage_overrides = disk_storage_overrides
            self.placement = placement
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_spec', {
            'source_vm': type.IdType(resource_types='VirtualMachine'),
            'name': type.StringType(),
            'description': type.OptionalType(type.StringType()),
            'library': type.IdType(resource_types='com.vmware.content.Library'),
            'vm_home_storage': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CreateSpecVmHomeStorage')),
            'disk_storage': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CreateSpecDiskStorage')),
            'disk_storage_overrides': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.CreateSpecDiskStorage'))),
            'placement': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CreatePlacementSpec')),
        },
        CreateSpec,
        False,
        None))


    class CreatePlacementSpec(VapiStruct):
        """
        The ``LibraryItems.CreatePlacementSpec`` class contains information used to
        place a virtual machine template onto resources within the vCenter
        inventory. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     folder=None,
                     resource_pool=None,
                     host=None,
                     cluster=None,
                    ):
            """
            :type  folder: :class:`str` or ``None``
            :param folder: Virtual machine folder into which the virtual machine template
                should be placed. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                If None, the virtual machine template will be placed in the same
                folder as the source virtual machine.
            :type  resource_pool: :class:`str` or ``None``
            :param resource_pool: Resource pool into which the virtual machine template should be
                placed. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
                If None, the system will attempt to choose a suitable resource pool
                for the virtual machine template; if a resource pool cannot be
                chosen, the library item creation operation will fail.
            :type  host: :class:`str` or ``None``
            :param host: Host onto which the virtual machine template should be placed. If
                ``host`` and ``resourcePool`` are both specified, ``resourcePool``
                must belong to ``host``. If ``host`` and ``cluster`` are both
                specified, ``host`` must be a member of ``cluster``. This attribute
                was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute may be None if ``resourcePool`` or ``cluster`` is
                specified. If None, the system will attempt to choose a suitable
                host for the virtual machine template; if a host cannot be chosen,
                the library item creation operation will fail.
            :type  cluster: :class:`str` or ``None``
            :param cluster: Cluster onto which the virtual machine template should be placed.
                If ``cluster`` and ``resourcePool`` are both specified,
                ``resourcePool`` must belong to ``cluster``. If ``cluster`` and
                ``host`` are both specified, ``host`` must be a member of
                ``cluster``. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
                If ``resourcePool`` or ``host`` is specified, it is recommended
                that this attribute be None.
            """
            self.folder = folder
            self.resource_pool = resource_pool
            self.host = host
            self.cluster = cluster
            VapiStruct.__init__(self)

    CreatePlacementSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_placement_spec', {
            'folder': type.OptionalType(type.IdType()),
            'resource_pool': type.OptionalType(type.IdType()),
            'host': type.OptionalType(type.IdType()),
            'cluster': type.OptionalType(type.IdType()),
        },
        CreatePlacementSpec,
        False,
        None))


    class CreateSpecVmHomeStoragePolicy(VapiStruct):
        """
        The ``LibraryItems.CreateSpecVmHomeStoragePolicy`` class defines the
        storage policy specification for a virtual machine template's configuration
        and log files. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`LibraryItems.CreateSpecVmHomeStoragePolicy.Type`
            :param type: Policy type to be used when creating the virtual machine template's
                configuration and log files. This attribute was added in vSphere
                API 6.8
            :type  policy: :class:`str`
            :param policy: Identifier for the storage policy to use. This attribute was added
                in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItems.CreateSpecVmHomeStoragePolicy.Type.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class Type(Enum):
            """
            Policy type for the virtual machine template's configuration and log files.
            This enumeration was added in vSphere API 6.8

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy. This class attribute was added in vSphere API 6.8

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Type` instance.
                """
                Enum.__init__(string)

        Type._set_values([
            Type('USE_SPECIFIED_POLICY'),
        ])
        Type._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm_template.library_items.create_spec_vm_home_storage_policy.type',
            Type))

    CreateSpecVmHomeStoragePolicy._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_spec_vm_home_storage_policy', {
            'type': type.ReferenceType(__name__, 'LibraryItems.CreateSpecVmHomeStoragePolicy.Type'),
            'policy': type.OptionalType(type.IdType()),
        },
        CreateSpecVmHomeStoragePolicy,
        False,
        None))


    class CreateSpecVmHomeStorage(VapiStruct):
        """
        The ``LibraryItems.CreateSpecVmHomeStorage`` class defines the storage
        specification for a virtual machine template's configuration and log files.
        This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str` or ``None``
            :param datastore: Identifier of the datastore for the virtual machine template's
                configuration and log files. This attribute was added in vSphere
                API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is currently required. If None, ``storagePolicy``
                must be set. The server picks a datastore that is compatible with
                the specified storage policy. 
                
                If both ``datastore`` and ``storagePolicy`` are specified, and the
                storage policy is incompatible with the ``datastore``, then the
                virtual machine template will be flagged as being out of compliance
                with the specified storage policy. 
            :type  storage_policy: :class:`LibraryItems.CreateSpecVmHomeStoragePolicy` or ``None``
            :param storage_policy: Storage policy for the virtual machine template's configuration and
                log files. This attribute was added in vSphere API 6.8
                If None, ``datastore`` must be specified and the virtual machine
                template's configuration and log files are created with the default
                storage policy associated with the ``datastore``.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    CreateSpecVmHomeStorage._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_spec_vm_home_storage', {
            'datastore': type.OptionalType(type.IdType()),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CreateSpecVmHomeStoragePolicy')),
        },
        CreateSpecVmHomeStorage,
        False,
        None))


    class CreateSpecDiskStoragePolicy(VapiStruct):
        """
        The ``LibraryItems.CreateSpecDiskStoragePolicy`` class defines the storage
        policy specification for a virtual machine template's disks. This class was
        added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`LibraryItems.CreateSpecDiskStoragePolicy.Type`
            :param type: Policy type to be used when creating a virtual machine template's
                disk. This attribute was added in vSphere API 6.8
            :type  policy: :class:`str`
            :param policy: Identifier for the storage policy to use. This attribute was added
                in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItems.CreateSpecDiskStoragePolicy.Type.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class Type(Enum):
            """
            Policy type for a virtual machine template's disk. This enumeration was
            added in vSphere API 6.8

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy. This class attribute was added in vSphere API 6.8

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Type` instance.
                """
                Enum.__init__(string)

        Type._set_values([
            Type('USE_SPECIFIED_POLICY'),
        ])
        Type._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm_template.library_items.create_spec_disk_storage_policy.type',
            Type))

    CreateSpecDiskStoragePolicy._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_spec_disk_storage_policy', {
            'type': type.ReferenceType(__name__, 'LibraryItems.CreateSpecDiskStoragePolicy.Type'),
            'policy': type.OptionalType(type.IdType()),
        },
        CreateSpecDiskStoragePolicy,
        False,
        None))


    class CreateSpecDiskStorage(VapiStruct):
        """
        The ``LibraryItems.CreateSpecDiskStorage`` class defines the storage
        specification for a virtual machine template's disks. This class was added
        in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str` or ``None``
            :param datastore: Identifier for the datastore associated with a virtual machine
                template's disk. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is currently required. If None, ``storagePolicy``
                must be set. The server picks a datastore that is compatible with
                the specified storage policy. 
                
                If both ``datastore`` and ``storagePolicy`` are specified, and the
                storage policy is incompatible with the ``datastore``, then the
                disk will be flagged as being out of compliance with the specified
                storage policy. 
            :type  storage_policy: :class:`LibraryItems.CreateSpecDiskStoragePolicy` or ``None``
            :param storage_policy: Storage policy for a virtual machine template's disk. This
                attribute was added in vSphere API 6.8
                If None, ``datastore`` must be specified and the virtual machine
                template's disk is created with the default storage policy
                associated with the ``datastore``.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    CreateSpecDiskStorage._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.create_spec_disk_storage', {
            'datastore': type.OptionalType(type.IdType()),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CreateSpecDiskStoragePolicy')),
        },
        CreateSpecDiskStorage,
        False,
        None))


    class DeploySpec(VapiStruct):
        """
        The ``LibraryItems.DeploySpec`` class defines the deployment parameters
        that can be specified for the ``deploy`` method. This class was added in
        vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     vm_home_storage=None,
                     disk_storage=None,
                     disk_storage_overrides=None,
                     placement=None,
                     powered_on=None,
                     guest_customization=None,
                     hardware_customization=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the deployed virtual machine. This attribute was added in
                vSphere API 6.8
            :type  description: :class:`str` or ``None``
            :param description: Description of the deployed virtual machine. This attribute was
                added in vSphere API 6.8
                If None, the deployed virtual machine has the same description as
                the source library item.
            :type  vm_home_storage: :class:`LibraryItems.DeploySpecVmHomeStorage` or ``None``
            :param vm_home_storage: Storage location for the deployed virtual machine's configuration
                and log files. This attribute was added in vSphere API 6.8
                If None, the deployed virtual machine's configuration and log files
                are created with the same storage spec as the source virtual
                machine template's configuration and log files.
            :type  disk_storage: :class:`LibraryItems.DeploySpecDiskStorage` or ``None``
            :param disk_storage: Storage specification for the deployed virtual machine's disks.
                This attribute was added in vSphere API 6.8
                If both ``diskStorageOverrides`` and ``diskStorage`` are None, the
                deployed virtual machine's disks are created with the same storage
                spec as the corresponding disks in the source virtual machine
                template contained in the library item. 
                
                If ``diskStorageOverrides`` is None and ``diskStorage`` is
                specified, all of the deployed virtual machine's disks are created
                with the storage spec specified by ``diskStorage``. 
                
                If ``diskStorageOverrides`` is specified and ``diskStorage`` is
                None, disks with identifiers that are not in
                ``diskStorageOverrides`` are created with the same storage spec as
                the corresponding disks in the source virtual machine template
                contained in the library item. 
                
                If both ``diskStorageOverrides`` and ``diskStorage`` are specified,
                disks with identifiers that are not in ``diskStorageOverrides`` are
                created with the storage spec specified by ``diskStorage``. 
            :type  disk_storage_overrides: (:class:`dict` of :class:`str` and :class:`LibraryItems.DeploySpecDiskStorage`) or ``None``
            :param disk_storage_overrides: Storage specification for individual disks in the deployed virtual
                machine. This is specified as a mapping between disk identifiers in
                the source virtual machine template contained in the library item
                and their storage specifications. This attribute was added in
                vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If both ``diskStorageOverrides`` and ``diskStorage`` are None, the
                deployed virtual machine's disks are created with the same storage
                spec as the corresponding disks in the source virtual machine
                template contained in the library item. 
                
                If ``diskStorageOverrides`` is None and ``diskStorage`` is
                specified, all of the deployed virtual machine's disks are created
                with the storage spec specified by ``diskStorage``. 
                
                If ``diskStorageOverrides`` is specified and ``diskStorage`` is
                None, disks with identifiers that are not in
                ``diskStorageOverrides`` are created with the same storage spec as
                the corresponding disks in the source virtual machine template
                contained in the library item. 
                
                If both ``diskStorageOverrides`` and ``diskStorage`` are specified,
                disks with identifiers that are not in ``diskStorageOverrides`` are
                created with the storage spec specified by ``diskStorage``. 
            :type  placement: :class:`LibraryItems.DeployPlacementSpec` or ``None``
            :param placement: Information used to place the deployed virtual machine. This
                attribute was added in vSphere API 6.8
                This attribute is currently required. In the future, if this
                attribute is None, the system will use the values from the source
                virtual machine template contained in the library item. 
                
                If specified, each attribute will be used for placement. If the
                attributes result in disjoint placement, the operation will fail.
                If the attributes along with the placement values of the source
                virtual machine template result in disjoint placement, the
                operation will fail. 
            :type  powered_on: :class:`bool` or ``None``
            :param powered_on: Specifies whether the deployed virtual machine should be powered on
                after deployment. This attribute was added in vSphere API 6.8
                If None, the virtual machine will not be powered on after
                deployment.
            :type  guest_customization: :class:`LibraryItems.GuestCustomizationSpec` or ``None``
            :param guest_customization: Guest customization spec to apply to the deployed virtual machine.
                This attribute was added in vSphere API 6.8
                If None, the guest operating system is not customized after
                deployment.
            :type  hardware_customization: :class:`LibraryItems.HardwareCustomizationSpec` or ``None``
            :param hardware_customization: Hardware customization spec which specifies updates to the deployed
                virtual machine. This attribute was added in vSphere API 6.8
                If None, the deployed virtual machine has the same hardware
                configuration as the source virtual machine template contained in
                the library item.
            """
            self.name = name
            self.description = description
            self.vm_home_storage = vm_home_storage
            self.disk_storage = disk_storage
            self.disk_storage_overrides = disk_storage_overrides
            self.placement = placement
            self.powered_on = powered_on
            self.guest_customization = guest_customization
            self.hardware_customization = hardware_customization
            VapiStruct.__init__(self)

    DeploySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_spec', {
            'name': type.StringType(),
            'description': type.OptionalType(type.StringType()),
            'vm_home_storage': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.DeploySpecVmHomeStorage')),
            'disk_storage': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.DeploySpecDiskStorage')),
            'disk_storage_overrides': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.DeploySpecDiskStorage'))),
            'placement': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.DeployPlacementSpec')),
            'powered_on': type.OptionalType(type.BooleanType()),
            'guest_customization': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.GuestCustomizationSpec')),
            'hardware_customization': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.HardwareCustomizationSpec')),
        },
        DeploySpec,
        False,
        None))


    class HardwareCustomizationSpec(VapiStruct):
        """
        The ``LibraryItems.HardwareCustomizationSpec`` class defines the hardware
        customization options that are applied to the deployed virtual machine.
        This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     nics=None,
                     disks_to_remove=None,
                     disks_to_update=None,
                     cpu_update=None,
                     memory_update=None,
                    ):
            """
            :type  nics: (:class:`dict` of :class:`str` and :class:`LibraryItems.EthernetUpdateSpec`) or ``None``
            :param nics: Map of Ethernet network adapters to update. This attribute was
                added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``.
                If None, all Ethernet adapters will remain connected to the same
                network as they were in the source virtual machine template. An
                Ethernet adapter with a MacAddressType of MANUAL will not change.
                An Ethernet adapter with a MacAddressType of GENERATED or ASSIGNED
                will receive a new address.
            :type  disks_to_remove: :class:`set` of :class:`str` or ``None``
            :param disks_to_remove: Idenfiers of disks to remove from the deployed virtual machine.
                This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If None, all disks will be copied.
            :type  disks_to_update: (:class:`dict` of :class:`str` and :class:`LibraryItems.DiskUpdateSpec`) or ``None``
            :param disks_to_update: Disk update specification for individual disks in the deployed
                virtual machine. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If None, disks in the deployed virtual machine will have the same
                settings as the corresponding disks in the source virtual machine
                template contained in the library item.
            :type  cpu_update: :class:`LibraryItems.CpuUpdateSpec` or ``None``
            :param cpu_update: CPU update specification for the deployed virtual machine. This
                attribute was added in vSphere API 6.8
                If {\\\\@term.unset}, the deployed virtual machine has the same CPU
                settings as the source virtual machine template contained in the
                library item.
            :type  memory_update: :class:`LibraryItems.MemoryUpdateSpec` or ``None``
            :param memory_update: Memory update specification for the deployed virtual machine. This
                attribute was added in vSphere API 6.8
                If {\\\\@term.unset}, the deployed virtual machine has the same
                memory settings as the source virtual machine template contained in
                the library item.
            """
            self.nics = nics
            self.disks_to_remove = disks_to_remove
            self.disks_to_update = disks_to_update
            self.cpu_update = cpu_update
            self.memory_update = memory_update
            VapiStruct.__init__(self)

    HardwareCustomizationSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.hardware_customization_spec', {
            'nics': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.EthernetUpdateSpec'))),
            'disks_to_remove': type.OptionalType(type.SetType(type.IdType())),
            'disks_to_update': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.DiskUpdateSpec'))),
            'cpu_update': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.CpuUpdateSpec')),
            'memory_update': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.MemoryUpdateSpec')),
        },
        HardwareCustomizationSpec,
        False,
        None))


    class DiskUpdateSpec(VapiStruct):
        """
        The ``LibraryItems.DiskUpdateSpec`` class describes updates to the
        configuration of a virtual disk in the deployed virtual machine. This class
        was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     capacity=None,
                    ):
            """
            :type  capacity: :class:`long`
            :param capacity: Updated capacity of the virtual disk backing in bytes. This value
                has to be larger than the original capacity of the disk. This
                attribute was added in vSphere API 6.8
            """
            self.capacity = capacity
            VapiStruct.__init__(self)

    DiskUpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.disk_update_spec', {
            'capacity': type.IntegerType(),
        },
        DiskUpdateSpec,
        False,
        None))


    class CpuUpdateSpec(VapiStruct):
        """
        The ``LibraryItems.CpuUpdateSpec`` class describes updates to the CPU
        configuration of the deployed virtual machine. This class was added in
        vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     num_cpus=None,
                     num_cores_per_socket=None,
                    ):
            """
            :type  num_cpus: :class:`long` or ``None``
            :param num_cpus: Number of virtual processors in the deployed virtual machine. This
                attribute was added in vSphere API 6.8
                If {\\\\@term.unset}, the deployed virtual machine has the same CPU
                count as the source virtual machine template contained in the
                library item.
            :type  num_cores_per_socket: :class:`long` or ``None``
            :param num_cores_per_socket: Number of cores among which to distribute CPUs in the deployed
                virtual machine. This attribute was added in vSphere API 6.8
                If {\\\\@term.unset}, the deployed virtual machine has the same
                number of cores per socket as the source virtual machine template
                contained in the library item.
            """
            self.num_cpus = num_cpus
            self.num_cores_per_socket = num_cores_per_socket
            VapiStruct.__init__(self)

    CpuUpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.cpu_update_spec', {
            'num_cpus': type.OptionalType(type.IntegerType()),
            'num_cores_per_socket': type.OptionalType(type.IntegerType()),
        },
        CpuUpdateSpec,
        False,
        None))


    class MemoryUpdateSpec(VapiStruct):
        """
        The ``LibraryItems.MemoryUpdateSpec`` class describes updates to the memory
        configuration of the deployed virtual machine. This class was added in
        vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     memory=None,
                    ):
            """
            :type  memory: :class:`long` or ``None``
            :param memory: Size of a virtual machine's memory in MB. This attribute was added
                in vSphere API 6.8
                If {\\\\@term.unset}, the deployed virtual machine has the same
                memory size as the source virtual machine template.
            """
            self.memory = memory
            VapiStruct.__init__(self)

    MemoryUpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.memory_update_spec', {
            'memory': type.OptionalType(type.IntegerType()),
        },
        MemoryUpdateSpec,
        False,
        None))


    class EthernetUpdateSpec(VapiStruct):
        """
        The ``LibraryItems.EthernetUpdateSpec`` class describes the network that
        the ethernet adapter of the deployed virtual machine should be connected
        to. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     network=None,
                    ):
            """
            :type  network: :class:`str` or ``None``
            :param network: Identifier of the network backing the virtual Ethernet adapter.
                This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
                This attribute is currently required. 
                
                If None, the virtual Ethernet adapter will be connected to same
                network as it was in the source virtual machine template. 
            """
            self.network = network
            VapiStruct.__init__(self)

    EthernetUpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.ethernet_update_spec', {
            'network': type.OptionalType(type.IdType()),
        },
        EthernetUpdateSpec,
        False,
        None))


    class DeployPlacementSpec(VapiStruct):
        """
        The ``LibraryItems.DeployPlacementSpec`` class contains information used to
        place a virtual machine onto resources within the vCenter inventory. This
        class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     folder=None,
                     resource_pool=None,
                     host=None,
                     cluster=None,
                    ):
            """
            :type  folder: :class:`str` or ``None``
            :param folder: Virtual machine folder into which the deployed virtual machine
                should be placed. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                This attribute is currently required. 
                
                If None, the system will attempt to choose a suitable folder for
                the virtual machine; if a folder cannot be chosen, the virtual
                machine deployment operation will fail. 
            :type  resource_pool: :class:`str` or ``None``
            :param resource_pool: Resource pool into which the deployed virtual machine should be
                placed. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
                If None, the system will attempt to choose a suitable resource pool
                for the virtual machine; if a resource pool cannot be chosen, the
                virtual machine deployment operation will fail.
            :type  host: :class:`str` or ``None``
            :param host: Host onto which the virtual machine should be placed. If ``host``
                and ``resourcePool`` are both specified, ``resourcePool`` must
                belong to ``host``. If ``host`` and ``cluster`` are both specified,
                ``host`` must be a member of ``cluster``. This attribute was added
                in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute may be None if ``resourcePool`` or ``cluster`` is
                specified. If None, the system will attempt to choose a suitable
                host for the virtual machine; if a host cannot be chosen, the
                virtual machine deployment operation will fail.
            :type  cluster: :class:`str` or ``None``
            :param cluster: Cluster onto which the deployed virtual machine should be placed.
                If ``cluster`` and ``resourcePool`` are both specified,
                ``resourcePool`` must belong to ``cluster``. If ``cluster`` and
                ``host`` are both specified, ``host`` must be a member of
                ``cluster``. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
                If ``resourcePool`` or ``host`` is specified, it is recommended
                that this attribute be None.
            """
            self.folder = folder
            self.resource_pool = resource_pool
            self.host = host
            self.cluster = cluster
            VapiStruct.__init__(self)

    DeployPlacementSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_placement_spec', {
            'folder': type.OptionalType(type.IdType()),
            'resource_pool': type.OptionalType(type.IdType()),
            'host': type.OptionalType(type.IdType()),
            'cluster': type.OptionalType(type.IdType()),
        },
        DeployPlacementSpec,
        False,
        None))


    class DeploySpecVmHomeStoragePolicy(VapiStruct):
        """
        The ``LibraryItems.DeploySpecVmHomeStoragePolicy`` class defines the
        storage policy specification for the deployed virtual machine's
        configuration and log files. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                    'USE_SOURCE_POLICY' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`LibraryItems.DeploySpecVmHomeStoragePolicy.Type`
            :param type: Policy type to be used when creating the deployed virtual machine's
                configuration and log files. This attribute was added in vSphere
                API 6.8
            :type  policy: :class:`str`
            :param policy: Identifier for the storage policy to use. This attribute was added
                in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItems.DeploySpecVmHomeStoragePolicy.Type.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class Type(Enum):
            """
            Policy type for the deployed virtual machine's configuration and log files.
            This enumeration was added in vSphere API 6.8

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy. This class attribute was added in vSphere API 6.8

            """
            USE_SOURCE_POLICY = None
            """
            Use the storage policy that is associated with the source virtual machine
            template's configuration and log files. This class attribute was added in
            vSphere API 6.8

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Type` instance.
                """
                Enum.__init__(string)

        Type._set_values([
            Type('USE_SPECIFIED_POLICY'),
            Type('USE_SOURCE_POLICY'),
        ])
        Type._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm_template.library_items.deploy_spec_vm_home_storage_policy.type',
            Type))

    DeploySpecVmHomeStoragePolicy._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_spec_vm_home_storage_policy', {
            'type': type.ReferenceType(__name__, 'LibraryItems.DeploySpecVmHomeStoragePolicy.Type'),
            'policy': type.OptionalType(type.IdType()),
        },
        DeploySpecVmHomeStoragePolicy,
        False,
        None))


    class DeploySpecVmHomeStorage(VapiStruct):
        """
        The ``LibraryItems.DeploySpecVmHomeStorage`` class defines the storage
        specification for a deployed virtual machine's configuration and log files.
        This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str` or ``None``
            :param datastore: Identifier of the datastore for the deployed virtual machine's
                configuration and log files. This attribute was added in vSphere
                API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is currently required. If None, ``storagePolicy``
                must be set. The server picks a datastore that is compatible with
                the specified storage policy. 
                
                If both ``datastore`` and ``storagePolicy`` are specified, and the
                storage policy is incompatible with the ``datastore``, then the
                deployed virtual machine will be flagged as being out of compliance
                with the specified storage policy. 
            :type  storage_policy: :class:`LibraryItems.DeploySpecVmHomeStoragePolicy` or ``None``
            :param storage_policy: Storage policy for the deployed virtual machine's configuration and
                log files. This attribute was added in vSphere API 6.8
                If None, ``datastore`` must be specified and the deployed virtual
                machine's configuration and log files are created with the default
                storage policy associated with the ``datastore``.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    DeploySpecVmHomeStorage._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_spec_vm_home_storage', {
            'datastore': type.OptionalType(type.IdType()),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.DeploySpecVmHomeStoragePolicy')),
        },
        DeploySpecVmHomeStorage,
        False,
        None))


    class DeploySpecDiskStoragePolicy(VapiStruct):
        """
        The ``LibraryItems.DeploySpecDiskStoragePolicy`` class describes the
        storage policy specification for the deployed virtual machine's disks. This
        class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                    'USE_SOURCE_POLICY' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`LibraryItems.DeploySpecDiskStoragePolicy.Type`
            :param type: Policy type to be used when creating the deployed virtual machine's
                disk. This attribute was added in vSphere API 6.8
            :type  policy: :class:`str`
            :param policy: Identifier of the storage policy to use. This attribute was added
                in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`LibraryItems.DeploySpecDiskStoragePolicy.Type.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class Type(Enum):
            """
            Policy type for the deployed virtual machine's disk. This enumeration was
            added in vSphere API 6.8

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy. This class attribute was added in vSphere API 6.8

            """
            USE_SOURCE_POLICY = None
            """
            Use the storage policy that is associated with the corresponding disk in
            the source virtual machine template. This class attribute was added in
            vSphere API 6.8

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Type` instance.
                """
                Enum.__init__(string)

        Type._set_values([
            Type('USE_SPECIFIED_POLICY'),
            Type('USE_SOURCE_POLICY'),
        ])
        Type._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm_template.library_items.deploy_spec_disk_storage_policy.type',
            Type))

    DeploySpecDiskStoragePolicy._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_spec_disk_storage_policy', {
            'type': type.ReferenceType(__name__, 'LibraryItems.DeploySpecDiskStoragePolicy.Type'),
            'policy': type.OptionalType(type.IdType()),
        },
        DeploySpecDiskStoragePolicy,
        False,
        None))


    class DeploySpecDiskStorage(VapiStruct):
        """
        The ``LibraryItems.DeploySpecDiskStorage`` class contains the storage
        specification for disks in the virtual machine. This class was added in
        vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str` or ``None``
            :param datastore: Identifier for the datastore associated the deployed virtual
                machine's disk. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is currently required. If None, ``storagePolicy``
                must be set. The server picks a datastore that is compatible with
                the specified storage policy. 
                
                If both ``datastore`` and ``storagePolicy`` are specified, and the
                storage policy is incompatible with the ``datastore``, then the
                disk will be flagged as being out of compliance with the specified
                storage policy. 
            :type  storage_policy: :class:`LibraryItems.DeploySpecDiskStoragePolicy` or ``None``
            :param storage_policy: Storage policy for the deployed virtual machine's disk. This
                attribute was added in vSphere API 6.8
                If None, ``datastore`` must be specified and the deployed virtual
                machine's disk is created with the default storage policy
                associated with the ``datastore``.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    DeploySpecDiskStorage._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.deploy_spec_disk_storage', {
            'datastore': type.OptionalType(type.IdType()),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.DeploySpecDiskStoragePolicy')),
        },
        DeploySpecDiskStorage,
        False,
        None))


    class GuestCustomizationSpec(VapiStruct):
        """
        The ``LibraryItems.GuestCustomizationSpec`` class contains information
        required to customize the deployed virtual machine. This class was added in
        vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Name of the customization specification. This attribute was added
                in vSphere API 6.8
                If None, no guest customization is performed.
            """
            self.name = name
            VapiStruct.__init__(self)

    GuestCustomizationSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.guest_customization_spec', {
            'name': type.OptionalType(type.StringType()),
        },
        GuestCustomizationSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``LibraryItems.Info`` class contains information about a virtual
        machine template item in content library. This class was added in vSphere
        API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'guest_OS': 'guest_os',
                                }

        def __init__(self,
                     guest_os=None,
                     cpu=None,
                     memory=None,
                     vm_home_storage=None,
                     disks=None,
                     nics=None,
                     vm_template=None,
                    ):
            """
            :type  guest_os: :class:`com.vmware.vcenter.vm_client.GuestOS`
            :param guest_os: Configured guest operating system of the virtual machine template.
                This attribute was added in vSphere API 6.8
            :type  cpu: :class:`LibraryItems.CpuInfo`
            :param cpu: CPU configuration of the virtual machine template. This attribute
                was added in vSphere API 6.8
            :type  memory: :class:`LibraryItems.MemoryInfo`
            :param memory: Memory configuration of the virtual machine template. This
                attribute was added in vSphere API 6.8
            :type  vm_home_storage: :class:`LibraryItems.VmHomeStorageInfo`
            :param vm_home_storage: Storage information about the virtual machine template's
                configuration and log files. This attribute was added in vSphere
                API 6.8
            :type  disks: :class:`dict` of :class:`str` and :class:`LibraryItems.DiskInfo`
            :param disks: Storage information about the virtual machine template's virtual
                disks. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            :type  nics: :class:`dict` of :class:`str` and :class:`LibraryItems.EthernetInfo`
            :param nics: Information about the virtual machine template's virtual ethernet
                adapters. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``.
            :type  vm_template: :class:`str`
            :param vm_template: Identifier of the virtual machine template contained in the library
                item. This field is used to identify the virtual machine template
                in legacy APIs. This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``VirtualMachine``.
            """
            self.guest_os = guest_os
            self.cpu = cpu
            self.memory = memory
            self.vm_home_storage = vm_home_storage
            self.disks = disks
            self.nics = nics
            self.vm_template = vm_template
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.info', {
            'guest_OS': type.ReferenceType('com.vmware.vcenter.vm_client', 'GuestOS'),
            'cpu': type.ReferenceType(__name__, 'LibraryItems.CpuInfo'),
            'memory': type.ReferenceType(__name__, 'LibraryItems.MemoryInfo'),
            'vm_home_storage': type.ReferenceType(__name__, 'LibraryItems.VmHomeStorageInfo'),
            'disks': type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.DiskInfo')),
            'nics': type.MapType(type.IdType(), type.ReferenceType(__name__, 'LibraryItems.EthernetInfo')),
            'vm_template': type.IdType(resource_types='VirtualMachine'),
        },
        Info,
        False,
        None))


    class CpuInfo(VapiStruct):
        """
        The ``LibraryItems.CpuInfo`` class contains CPU related information about
        the virtual machine template. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     count=None,
                     cores_per_socket=None,
                    ):
            """
            :type  count: :class:`long`
            :param count: Number of CPU cores. This attribute was added in vSphere API 6.8
            :type  cores_per_socket: :class:`long`
            :param cores_per_socket: Number of CPU cores per socket. This attribute was added in vSphere
                API 6.8
            """
            self.count = count
            self.cores_per_socket = cores_per_socket
            VapiStruct.__init__(self)

    CpuInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.cpu_info', {
            'count': type.IntegerType(),
            'cores_per_socket': type.IntegerType(),
        },
        CpuInfo,
        False,
        None))


    class MemoryInfo(VapiStruct):
        """
        The ``LibraryItems.MemoryInfo`` class contains memory related information
        about the virtual machine template. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'size_MiB': 'size_mib',
                                }

        def __init__(self,
                     size_mib=None,
                    ):
            """
            :type  size_mib: :class:`long`
            :param size_mib: Memory size in mebibytes. This attribute was added in vSphere API
                6.8
            """
            self.size_mib = size_mib
            VapiStruct.__init__(self)

    MemoryInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.memory_info', {
            'size_MiB': type.IntegerType(),
        },
        MemoryInfo,
        False,
        None))


    class VmHomeStorageInfo(VapiStruct):
        """
        The ``LibraryItems.VmHomeStorageInfo`` class contains storage information
        about the virtual machine template's configuration and log files. This
        class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str`
            :param datastore: Identifier of the datastore where the virtual machine template's
                configuration and log files are stored. This attribute was added in
                vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
            :type  storage_policy: :class:`str` or ``None``
            :param storage_policy: Identifier of the storage policy associated with the virtual
                machine template's configuration and log files. This attribute was
                added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                If None, the virtual machine template's configuration and log files
                do not have a storage policy associated with them.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    VmHomeStorageInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.vm_home_storage_info', {
            'datastore': type.IdType(resource_types='Datastore'),
            'storage_policy': type.OptionalType(type.IdType()),
        },
        VmHomeStorageInfo,
        False,
        None))


    class DiskInfo(VapiStruct):
        """
        The ``LibraryItems.DiskInfo`` class contains information about the virtual
        machine template's virtual disk. This class was added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     capacity=None,
                     disk_storage=None,
                    ):
            """
            :type  capacity: :class:`long` or ``None``
            :param capacity: Capacity of the virtual disk in bytes. This attribute was added in
                vSphere API 6.8
                This attribute will be None if the virtual disk is inaccessible.
            :type  disk_storage: :class:`LibraryItems.DiskStorageInfo`
            :param disk_storage: Disk storage related information. This attribute was added in
                vSphere API 6.8
            """
            self.capacity = capacity
            self.disk_storage = disk_storage
            VapiStruct.__init__(self)

    DiskInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.disk_info', {
            'capacity': type.OptionalType(type.IntegerType()),
            'disk_storage': type.ReferenceType(__name__, 'LibraryItems.DiskStorageInfo'),
        },
        DiskInfo,
        False,
        None))


    class DiskStorageInfo(VapiStruct):
        """
        The ``LibraryItems.DiskStorageInfo`` class contains storage related
        information about a virtual machine template's virtual disk. This class was
        added in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     storage_policy=None,
                    ):
            """
            :type  datastore: :class:`str`
            :param datastore: Identifier of the datastore where the disk is stored. This
                attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
            :type  storage_policy: :class:`str` or ``None``
            :param storage_policy: Identifier of the storage policy associated with the virtual disk.
                This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.spbm.StorageProfile``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.spbm.StorageProfile``.
                If None, the virtual disk does not have a storage policy associated
                with it.
            """
            self.datastore = datastore
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    DiskStorageInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.disk_storage_info', {
            'datastore': type.IdType(resource_types='Datastore'),
            'storage_policy': type.OptionalType(type.IdType()),
        },
        DiskStorageInfo,
        False,
        None))


    class EthernetInfo(VapiStruct):
        """
        The ``LibraryItems.EthernetInfo`` class contains information about a
        virtual machine template's virtual Ethernet adapter. This class was added
        in vSphere API 6.8

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backing_type=None,
                     mac_type=None,
                     network=None,
                    ):
            """
            :type  backing_type: :class:`LibraryItems.EthernetInfo.NetworkBackingType`
            :param backing_type: Network backing type for the virtual Ethernet adapter. This
                attribute was added in vSphere API 6.8
            :type  mac_type: :class:`LibraryItems.EthernetInfo.MacAddressType`
            :param mac_type: MAC address type of the ethernet adapter. This attribute was added
                in vSphere API 6.8
            :type  network: :class:`str` or ``None``
            :param network: Identifier of the network backing the virtual Ethernet adapter.
                This attribute was added in vSphere API 6.8
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
                This attribute will be None if the identifier of the network
                backing could not be determined.
            """
            self.backing_type = backing_type
            self.mac_type = mac_type
            self.network = network
            VapiStruct.__init__(self)

        class NetworkBackingType(Enum):
            """
            The ``LibraryItems.EthernetInfo.NetworkBackingType`` class defines valid
            network backing types for a virtual Ethernet adapter. This enumeration was
            added in vSphere API 6.8

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
            vSphere standard portgroup network backing. This class attribute was added
            in vSphere API 6.8

            """
            HOST_DEVICE = None
            """
            Legacy host device network backing. Imported VMs may have virtual Ethernet
            adapters with this type of backing, but this type of backing cannot be used
            to create or to update a virtual Ethernet adapter. This class attribute was
            added in vSphere API 6.8

            """
            DISTRIBUTED_PORTGROUP = None
            """
            Distributed virtual switch backing. This class attribute was added in
            vSphere API 6.8

            """
            OPAQUE_NETWORK = None
            """
            Opaque network backing. This class attribute was added in vSphere API 6.8

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`NetworkBackingType` instance.
                """
                Enum.__init__(string)

        NetworkBackingType._set_values([
            NetworkBackingType('STANDARD_PORTGROUP'),
            NetworkBackingType('HOST_DEVICE'),
            NetworkBackingType('DISTRIBUTED_PORTGROUP'),
            NetworkBackingType('OPAQUE_NETWORK'),
        ])
        NetworkBackingType._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm_template.library_items.ethernet_info.network_backing_type',
            NetworkBackingType))

        class MacAddressType(Enum):
            """
            The ``LibraryItems.EthernetInfo.MacAddressType`` class defines the valid
            MAC address origins for a virtual Ethernet adapter. This enumeration was
            added in vSphere API 6.8

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
            MAC address is assigned statically. This class attribute was added in
            vSphere API 6.8

            """
            GENERATED = None
            """
            MAC address is generated automatically. This class attribute was added in
            vSphere API 6.8

            """
            ASSIGNED = None
            """
            MAC address is assigned by vCenter Server. This class attribute was added
            in vSphere API 6.8

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
            'com.vmware.vcenter.vm_template.library_items.ethernet_info.mac_address_type',
            MacAddressType))

    EthernetInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm_template.library_items.ethernet_info', {
            'backing_type': type.ReferenceType(__name__, 'LibraryItems.EthernetInfo.NetworkBackingType'),
            'mac_type': type.ReferenceType(__name__, 'LibraryItems.EthernetInfo.MacAddressType'),
            'network': type.OptionalType(type.IdType()),
        },
        EthernetInfo,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Creates a library item in content library from a virtual machine. This
        method creates a library item in content library whose content is a
        virtual machine template created from the source virtual machine, using
        the supplied create specification. The virtual machine template is
        stored in a newly created library item. This method was added in
        vSphere API 6.8

        :type  spec: :class:`LibraryItems.CreateSpec`
        :param spec: information used to create the library item from the source virtual
            machine.
        :rtype: :class:`str`
        :return: Identifier of the newly created library item.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if an entity with the name specified by
            :attr:`LibraryItems.CreateSpec.name` already exists in the folder
            specified by :attr:`LibraryItems.CreatePlacementSpec.folder`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
             if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if :class:`LibraryItems.CreateSpec` contains invalid arguments.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation cannot be performed because of the source virtual
            machine's current state.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the source virtual machine specified by
            :attr:`LibraryItems.CreateSpec.source_vm` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library specified by :attr:`LibraryItems.CreateSpec.library`
            does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there was an error accessing a file from the source virtual
            machine.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
             if the source virtual machine is busy.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             if any of the services involved in the method are unavailable.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if any of the resources needed to create the virtual machine
            template could not be allocated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user that requested the method cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user that requested the method is not authorized to perform
            the method.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.Library`` referenced by the
              attribute :attr:`LibraryItems.CreateSpec.library` requires
              ``ContentLibrary.AddLibraryItem``.
            * The resource ``VirtualMachine`` referenced by the attribute
              :attr:`LibraryItems.CreateSpec.source_vm` requires ``System.Read``.
            * The resource ``Datastore`` referenced by the attribute
              :attr:`LibraryItems.CreateSpecVmHomeStorage.datastore` requires
              ``System.Read``.
            * The resource ``com.vmware.spbm.StorageProfile`` referenced by the
              attribute :attr:`LibraryItems.CreateSpecVmHomeStoragePolicy.policy`
              requires ``System.Read``.
            * The resource ``Datastore`` referenced by the attribute
              :attr:`LibraryItems.CreateSpecDiskStorage.datastore` requires
              ``System.Read``.
            * The resource ``com.vmware.spbm.StorageProfile`` referenced by the
              attribute :attr:`LibraryItems.CreateSpecDiskStoragePolicy.policy`
              requires ``System.Read``.
            * The resource ``com.vmware.vcenter.vm.hardware.Disk`` referenced
              by the :class:`dict` key of attribute
              :attr:`LibraryItems.CreateSpec.disk_storage_overrides` requires
              ``System.Read``.
            * The resource ``Folder`` referenced by the attribute
              :attr:`LibraryItems.CreatePlacementSpec.folder` requires
              ``System.Read``.
            * The resource ``ResourcePool`` referenced by the attribute
              :attr:`LibraryItems.CreatePlacementSpec.resource_pool` requires
              ``System.Read``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`LibraryItems.CreatePlacementSpec.host` requires
              ``System.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              attribute :attr:`LibraryItems.CreatePlacementSpec.cluster` requires
              ``System.Read``.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def deploy(self,
               template_library_item,
               spec,
               ):
        """
        Deploys a virtual machine as a copy of the source virtual machine
        template contained in the library item specified by
        ``template_library_item``. It uses the deployment specification in
        ``spec``. If :attr:`LibraryItems.DeploySpec.powered_on` and/or
        :attr:`LibraryItems.DeploySpec.guest_customization` are specified, the
        server triggers the power on and/or guest customization operations,
        which are executed asynchronously. This method was added in vSphere API
        6.8

        :type  template_library_item: :class:`str`
        :param template_library_item: identifier of the content library item containing the source
            virtual machine template to be deployed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  spec: :class:`LibraryItems.DeploySpec`
        :param spec:  specification of how the virtual machine should be deployed.
        :rtype: :class:`str`
        :return: Identifier of the deployed virtual machine.
            The return value will be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if a virtual machine with the name specified by
            :attr:`LibraryItems.DeploySpec.name` already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
             if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if ``spec`` contains invalid arguments.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if either a specified host or a specified datastore is in an
            invalid state for the deployment, such as maintenance mode.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``template_library_item`` cannot
            be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if any resource specified by a attribute of the
            :class:`LibraryItems.DeploySpec` class, specified by ``spec``
            cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there was an error accessing the source virtual machine template
            contained in the library item specified by
            ``template_library_item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if there an error accessing any of the resources specified in the
            ``spec``.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             if any of the services involved in the method are unavailable.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if there was an error in allocating any of the resources required
            by the method.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user that requested the method cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user that requested the method is not authorized to perform
            the method.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``template_library_item`` requires
              ``VirtualMachine.Provisioning.DeployTemplate``.
            * The resource ``Datastore`` referenced by the attribute
              :attr:`LibraryItems.DeploySpecVmHomeStorage.datastore` requires
              ``System.Read``.
            * The resource ``com.vmware.spbm.StorageProfile`` referenced by the
              attribute :attr:`LibraryItems.DeploySpecVmHomeStoragePolicy.policy`
              requires ``System.Read``.
            * The resource ``Datastore`` referenced by the attribute
              :attr:`LibraryItems.DeploySpecDiskStorage.datastore` requires
              ``System.Read``.
            * The resource ``com.vmware.spbm.StorageProfile`` referenced by the
              attribute :attr:`LibraryItems.DeploySpecDiskStoragePolicy.policy`
              requires ``System.Read``.
            * The resource ``com.vmware.vcenter.vm.hardware.Disk`` referenced
              by the :class:`dict` key of attribute
              :attr:`LibraryItems.DeploySpec.disk_storage_overrides` requires
              ``System.Read``.
            * The resource ``Folder`` referenced by the attribute
              :attr:`LibraryItems.DeployPlacementSpec.folder` requires
              ``System.Read``.
            * The resource ``ResourcePool`` referenced by the attribute
              :attr:`LibraryItems.DeployPlacementSpec.resource_pool` requires
              ``System.Read``.
            * The resource ``HostSystem`` referenced by the attribute
              :attr:`LibraryItems.DeployPlacementSpec.host` requires
              ``System.Read``.
            * The resource ``ClusterComputeResource`` referenced by the
              attribute :attr:`LibraryItems.DeployPlacementSpec.cluster` requires
              ``System.Read``.
            * The resource ``com.vmware.vcenter.vm.hardware.Ethernet``
              referenced by the :class:`dict` key of attribute
              :attr:`LibraryItems.HardwareCustomizationSpec.nics` requires
              ``System.Read``.
            * The resource ``Network`` referenced by the attribute
              :attr:`LibraryItems.EthernetUpdateSpec.network` requires
              ``System.Read``.
            * The resource ``com.vmware.vcenter.vm.hardware.Disk`` referenced
              by the attribute
              :attr:`LibraryItems.HardwareCustomizationSpec.disks_to_remove`
              requires ``System.Read``.
            * The resource ``com.vmware.vcenter.vm.hardware.Disk`` referenced
              by the :class:`dict` key of attribute
              :attr:`LibraryItems.HardwareCustomizationSpec.disks_to_update`
              requires ``System.Read``.
        """
        return self._invoke('deploy',
                            {
                            'template_library_item': template_library_item,
                            'spec': spec,
                            })

    def get(self,
            template_library_item,
            ):
        """
        Returns information about a virtual machine template contained in the
        library item specified by ``template_library_item``. This method was
        added in vSphere API 6.8

        :type  template_library_item: :class:`str`
        :param template_library_item: identifier of the library item containing the virtual machine
            template.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :rtype: :class:`LibraryItems.Info` or ``None``
        :return: Information about the virtual machine template item contained in
            the library item.
            If None, the library item specified by ``template_library_item``
            does not contain a virtual machine template.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
             if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library item could not be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine template's configuration state cannot be
            accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             if any of the services involved in the method are unavailable.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             if the user that requested the method cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user that requested the method is not authorized to perform
            the method.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``template_library_item`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'template_library_item': template_library_item,
                            })
class _LibraryItemsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'LibraryItems.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/vm-template/library-items',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for deploy operation
        deploy_input_type = type.StructType('operation-input', {
            'template_library_item': type.IdType(resource_types='com.vmware.content.library.Item'),
            'spec': type.ReferenceType(__name__, 'LibraryItems.DeploySpec'),
        })
        deploy_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        deploy_input_value_validator_list = [
        ]
        deploy_output_validator_list = [
        ]
        deploy_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm-template/library-items/{item}',
            path_variables={
                'template_library_item': 'item',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'template_library_item': type.IdType(resource_types='com.vmware.content.library.Item'),
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
            url_template='/vcenter/vm-template/library-items/{item}',
            path_variables={
                'template_library_item': 'item',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.library.Item'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'deploy': {
                'input_type': deploy_input_type,
                'output_type': type.IdType(resource_types='VirtualMachine'),
                'errors': deploy_error_dict,
                'input_value_validator_list': deploy_input_value_validator_list,
                'output_validator_list': deploy_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.OptionalType(type.ReferenceType(__name__, 'LibraryItems.Info')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'deploy': deploy_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm_template.library_items',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'LibraryItems': LibraryItems,
    }

