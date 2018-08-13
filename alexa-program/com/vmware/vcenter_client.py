# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter_client`` module provides classes for managing VMware
vSphere environments. The module is available starting in vSphere 6.5.

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


class Cluster(VapiInterface):
    """
    The ``Cluster`` class provides methods to manage clusters in the vCenter
    Server.
    """
    RESOURCE_TYPE = "ClusterComputeResource"
    """
    The resource type for the vCenter Cluster

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ClusterStub)

    class FilterSpec(VapiStruct):
        """
        The ``Cluster.FilterSpec`` class contains attributes used to filter the
        results when listing clusters (see :func:`Cluster.list`). If multiple
        attributes are specified, only clusters matching all of the attributes
        match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     clusters=None,
                     names=None,
                     folders=None,
                     datacenters=None,
                    ):
            """
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: Identifiers of clusters that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None or empty, clusters with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that clusters must have to match the filter (see
                :attr:`Cluster.Info.name`).
                If None or empty, clusters with any name match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the cluster for the cluster to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, clusters in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the cluster for the cluster to match
                the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, clusters in any datacenter match the filter.
            """
            self.clusters = clusters
            self.names = names
            self.folders = folders
            self.datacenters = datacenters
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.cluster.filter_spec', {
            'clusters': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Cluster.Summary`` class contains commonly used information about a
        cluster in vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     cluster=None,
                     name=None,
                     ha_enabled=None,
                     drs_enabled=None,
                    ):
            """
            :type  cluster: :class:`str`
            :param cluster: Identifier of the cluster.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
            :type  name: :class:`str`
            :param name: Name of the cluster.
            :type  ha_enabled: :class:`bool`
            :param ha_enabled: Flag indicating whether the vSphere HA feature is enabled for the
                cluster.
            :type  drs_enabled: :class:`bool`
            :param drs_enabled: Flag indicating whether the vSphere DRS service is enabled for the
                cluster.
            """
            self.cluster = cluster
            self.name = name
            self.ha_enabled = ha_enabled
            self.drs_enabled = drs_enabled
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.cluster.summary', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
            'name': type.StringType(),
            'ha_enabled': type.BooleanType(),
            'drs_enabled': type.BooleanType(),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Cluster.Info`` class contains information about a cluster in vCenter
        Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     resource_pool=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the cluster
            :type  resource_pool: :class:`str`
            :param resource_pool: Identifier of the root resource pool of the cluster
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
            """
            self.name = name
            self.resource_pool = resource_pool
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.cluster.info', {
            'name': type.StringType(),
            'resource_pool': type.IdType(resource_types='ResourcePool'),
        },
        Info,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) clusters in vCenter matching the :class:`Cluster.FilterSpec`.

        :type  filter: :class:`Cluster.FilterSpec` or ``None``
        :param filter: Specification of matching clusters for which information should be
            returned.
            If None, the behavior is equivalent to a
            :class:`Cluster.FilterSpec` with all attributes None which means
            all clusters match the filter.
        :rtype: :class:`list` of :class:`Cluster.Summary`
        :return: Commonly used information about the clusters matching the
            :class:`Cluster.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 clusters match the :class:`Cluster.FilterSpec`.
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
                            'filter': filter,
                            })

    def get(self,
            cluster,
            ):
        """
        Retrieves information about the cluster corresponding to ``cluster``.

        :type  cluster: :class:`str`
        :param cluster: Identifier of the cluster.
            The parameter must be an identifier for the resource type:
            ``ClusterComputeResource``.
        :rtype: :class:`Cluster.Info`
        :return: The :class:`Cluster.Info` instances that corresponds to the
            ``cluster``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no cluster associated with ``cluster`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session id is missing from the request or the corresponding
            session object cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't not have the required privileges.
        """
        return self._invoke('get',
                            {
                            'cluster': cluster,
                            })
class Datacenter(VapiInterface):
    """
    The ``Datacenter`` class provides methods to manage datacenters in the
    vCenter Server.
    """
    RESOURCE_TYPE = "Datacenter"
    """
    The resource type for the vCenter Datacenter

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DatacenterStub)

    class CreateSpec(VapiStruct):
        """
        The ``Datacenter.CreateSpec`` class defines the information used to create
        a datacenter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     folder=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the datacenter to be created.
            :type  folder: :class:`str` or ``None``
            :param folder: Datacenter folder in which the new datacenter should be created.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                This attribute is currently required. In the future, if this
                attribute is None, the system will attempt to choose a suitable
                folder for the datacenter; if a folder cannot be chosen, the
                datacenter creation operation will fail.
            """
            self.name = name
            self.folder = folder
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.datacenter.create_spec', {
            'name': type.StringType(),
            'folder': type.OptionalType(type.IdType()),
        },
        CreateSpec,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Datacenter.FilterSpec`` class contains attributes used to filter the
        results when listing datacenters (see :func:`Datacenter.list`). If multiple
        attributes are specified, only datacenters matching all of the attributes
        match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datacenters=None,
                     names=None,
                     folders=None,
                    ):
            """
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Identifiers of datacenters that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, datacenters with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that datacenters must have to match the filter (see
                :attr:`Datacenter.Info.name`).
                If None or empty, datacenters with any name match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the datacenters for the datacenter to
                match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, datacenters in any folder match the filter.
            """
            self.datacenters = datacenters
            self.names = names
            self.folders = folders
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.datacenter.filter_spec', {
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'folders': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Datacenter.Summary`` class contains commonly used information about a
        datacenter in vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datacenter=None,
                     name=None,
                    ):
            """
            :type  datacenter: :class:`str`
            :param datacenter: Identifier of the datacenter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datacenter``.
            :type  name: :class:`str`
            :param name: Name of the datacenter.
            """
            self.datacenter = datacenter
            self.name = name
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.datacenter.summary', {
            'datacenter': type.IdType(resource_types='Datacenter'),
            'name': type.StringType(),
        },
        Summary,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Datacenter.Info`` class contains information about a datacenter in
        vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     datastore_folder=None,
                     host_folder=None,
                     network_folder=None,
                     vm_folder=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the datacenter.
            :type  datastore_folder: :class:`str`
            :param datastore_folder: The root datastore folder associated with the datacenter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
            :type  host_folder: :class:`str`
            :param host_folder: The root host and cluster folder associated with the datacenter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
            :type  network_folder: :class:`str`
            :param network_folder: The root network folder associated with the datacenter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
            :type  vm_folder: :class:`str`
            :param vm_folder: The root virtual machine folder associated with the datacenter.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
            """
            self.name = name
            self.datastore_folder = datastore_folder
            self.host_folder = host_folder
            self.network_folder = network_folder
            self.vm_folder = vm_folder
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.datacenter.info', {
            'name': type.StringType(),
            'datastore_folder': type.IdType(resource_types='Folder'),
            'host_folder': type.IdType(resource_types='Folder'),
            'network_folder': type.IdType(resource_types='Folder'),
            'vm_folder': type.IdType(resource_types='Folder'),
        },
        Info,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Create a new datacenter in the vCenter inventory

        :type  spec: :class:`Datacenter.CreateSpec`
        :param spec: Specification for the new datacenter to be created.
        :rtype: :class:`str`
        :return: The identifier of the newly created datacenter
            The return value will be an identifier for the resource type:
            ``Datacenter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the datacenter with the same name is already present.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the datacenter name is empty or invalid as per the underlying
            implementation.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the folder is not specified and the system cannot choose a
            suitable one.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the datacenter folder cannot be found.
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
                            'spec': spec,
                            })

    def delete(self,
               datacenter,
               force=None,
               ):
        """
        Delete an empty datacenter from the vCenter Server

        :type  datacenter: :class:`str`
        :param datacenter: Identifier of the datacenter to be deleted.
            The parameter must be an identifier for the resource type:
            ``Datacenter``.
        :type  force: :class:`bool` or ``None``
        :param force: If true, delete the datacenter even if it is not empty.
            If None a :class:`com.vmware.vapi.std.errors_client.ResourceInUse`
            exception will be reported if the datacenter is not empty. This is
            the equivalent of passing the value false.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no datacenter associated with ``datacenter`` in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the datacenter associated with ``datacenter`` is not empty.
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
                            'datacenter': datacenter,
                            'force': force,
                            })

    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) datacenters in vCenter matching the
        :class:`Datacenter.FilterSpec`.

        :type  filter: :class:`Datacenter.FilterSpec` or ``None``
        :param filter: Specification of matching datacenters for which information should
            be returned.
            If None, the behavior is equivalent to a
            :class:`Datacenter.FilterSpec` with all attributes None which means
            all datacenters match the filter.
        :rtype: :class:`list` of :class:`Datacenter.Summary`
        :return: Commonly used information about the datacenters matching the
            :class:`Datacenter.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 datacenters match the
            :class:`Datacenter.FilterSpec`.
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
                            'filter': filter,
                            })

    def get(self,
            datacenter,
            ):
        """
        Retrieves information about the datacenter corresponding to
        ``datacenter``.

        :type  datacenter: :class:`str`
        :param datacenter: Identifier of the datacenter.
            The parameter must be an identifier for the resource type:
            ``Datacenter``.
        :rtype: :class:`Datacenter.Info`
        :return: The :class:`Datacenter.Info` instances that corresponds to the
            ``datacenter``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no datacenter associated with ``datacenter`` in the
            system.
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
                            'datacenter': datacenter,
                            })
class Datastore(VapiInterface):
    """
    The Datastore class provides methods for manipulating a datastore.
    """
    RESOURCE_TYPE = "Datastore"
    """
    The resource type for the vCenter datastore

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DatastoreStub)

    class Type(Enum):
        """
        The ``Datastore.Type`` class defines the supported types of vCenter
        datastores.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VMFS = None
        """
        VMware File System (ESX Server only).

        """
        NFS = None
        """
        Network file system v3 (linux & esx servers only).

        """
        NFS41 = None
        """
        Network file system v4.1 (linux & esx servers only).

        """
        CIFS = None
        """
        Common Internet File System.

        """
        VSAN = None
        """
        Virtual SAN (ESX Server only).

        """
        VFFS = None
        """
        Flash Read Cache (ESX Server only).

        """
        VVOL = None
        """
        vSphere Virtual Volume (ESX Server only).

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('VMFS'),
        Type('NFS'),
        Type('NFS41'),
        Type('CIFS'),
        Type('VSAN'),
        Type('VFFS'),
        Type('VVOL'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.datastore.type',
        Type))


    class Info(VapiStruct):
        """
        The ``Datastore.Info`` class contains information about a datastore.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     type=None,
                     accessible=None,
                     free_space=None,
                     multiple_host_access=None,
                     thin_provisioning_supported=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the datastore.
            :type  type: :class:`Datastore.Type`
            :param type: Type (VMFS, NFS, NFS41, CIFS, VSAN, VFFS, VVOL) of the datastore.
            :type  accessible: :class:`bool`
            :param accessible: Whether or not this datastore is accessible.
            :type  free_space: :class:`long` or ``None``
            :param free_space: Available space of this datastore, in bytes. 
                
                 The server periodically updates this value.
                This attribute will be None if the available space of this
                datastore is not known.
            :type  multiple_host_access: :class:`bool`
            :param multiple_host_access: Whether or not ore than one host in the datacenter has been
                configured with access to the datastore.
            :type  thin_provisioning_supported: :class:`bool`
            :param thin_provisioning_supported: Whether or not the datastore supports thin provisioning on a per
                file basis. When thin provisioning is used, backing storage is
                lazily allocated.
            """
            self.name = name
            self.type = type
            self.accessible = accessible
            self.free_space = free_space
            self.multiple_host_access = multiple_host_access
            self.thin_provisioning_supported = thin_provisioning_supported
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.datastore.info', {
            'name': type.StringType(),
            'type': type.ReferenceType(__name__, 'Datastore.Type'),
            'accessible': type.BooleanType(),
            'free_space': type.OptionalType(type.IntegerType()),
            'multiple_host_access': type.BooleanType(),
            'thin_provisioning_supported': type.BooleanType(),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Datastore.FilterSpec`` class contains attributes used to filter the
        results when listing datastores (see :func:`Datastore.list`). If multiple
        attributes are specified, only datastores matching all of the attributes
        match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastores=None,
                     names=None,
                     types=None,
                     folders=None,
                     datacenters=None,
                    ):
            """
            :type  datastores: :class:`set` of :class:`str` or ``None``
            :param datastores: Identifiers of datastores that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datastore``.
                If None or empty, datastores with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that datastores must have to match the filter (see
                :attr:`Datastore.Info.name`).
                If None or empty, datastores with any name match the filter.
            :type  types: :class:`set` of :class:`Datastore.Type` or ``None``
            :param types: Types that datastores must have to match the filter (see
                :attr:`Datastore.Summary.type`).
                If None or empty, datastores with any type match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the datastore for the datastore to match
                the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, datastores in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the datastore for the datastore to
                match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, datastores in any datacenter match the filter.
            """
            self.datastores = datastores
            self.names = names
            self.types = types
            self.folders = folders
            self.datacenters = datacenters
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.datastore.filter_spec', {
            'datastores': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'types': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'Datastore.Type'))),
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Datastore.Summary`` class contains commonly used information about a
        datastore.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                     name=None,
                     type=None,
                     free_space=None,
                     capacity=None,
                    ):
            """
            :type  datastore: :class:`str`
            :param datastore: Identifier of the datastore.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
            :type  name: :class:`str`
            :param name: Name of the datastore.
            :type  type: :class:`Datastore.Type`
            :param type: Type (VMFS, NFS, NFS41, CIFS, VSAN, VFFS, VVOL) of the datatore.
            :type  free_space: :class:`long` or ``None``
            :param free_space: Available space of this datastore, in bytes. 
                
                 The server periodically updates this value.
                This attribute will be None if the available space of this
                datastore is not known.
            :type  capacity: :class:`long` or ``None``
            :param capacity: Capacity of this datastore, in bytes. 
                
                 The server periodically updates this value.
                This attribute will be None if the capacity of this datastore is
                not known.
            """
            self.datastore = datastore
            self.name = name
            self.type = type
            self.free_space = free_space
            self.capacity = capacity
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.datastore.summary', {
            'datastore': type.IdType(resource_types='Datastore'),
            'name': type.StringType(),
            'type': type.ReferenceType(__name__, 'Datastore.Type'),
            'free_space': type.OptionalType(type.IntegerType()),
            'capacity': type.OptionalType(type.IntegerType()),
        },
        Summary,
        False,
        None))



    def get(self,
            datastore,
            ):
        """
        Retrieves information about the datastore indicated by ``datastore``.

        :type  datastore: :class:`str`
        :param datastore: Identifier of the datastore for which information should be
            retrieved.
            The parameter must be an identifier for the resource type:
            ``Datastore``.
        :rtype: :class:`Datastore.Info`
        :return: information about the datastore.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the datastore indicated by ``datastore`` does not exist.
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
                            'datastore': datastore,
                            })

    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) datastores in vCenter matching the
        :class:`Datastore.FilterSpec`.

        :type  filter: :class:`Datastore.FilterSpec` or ``None``
        :param filter: Specification of matching datastores for which information should
            be returned.
            If None, the behavior is equivalent to a
            :class:`Datastore.FilterSpec` with all attributes None which means
            all datastores match the filter.
        :rtype: :class:`list` of :class:`Datastore.Summary`
        :return: Commonly used information about the datastores matching the
            :class:`Datastore.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Datastore.FilterSpec.types` attribute contains a
            value that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Datastore.FilterSpec.types` attribute contains a
            value that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 datastores match the
            :class:`Datastore.FilterSpec`.
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
                            'filter': filter,
                            })
class Folder(VapiInterface):
    """
    The Folder class provides methods for manipulating a vCenter Server folder.
    """
    RESOURCE_TYPE = "Folder"
    """
    The resource type for the vCenter folder

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FolderStub)

    class Type(Enum):
        """
        The ``Folder.Type`` class defines the type of a vCenter Server folder. The
        type of a folder determines what what kinds of children can be contained in
        the folder.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DATACENTER = None
        """
        A folder that can contain datacenters.

        """
        DATASTORE = None
        """
        A folder that can contain datastores.

        """
        HOST = None
        """
        A folder that can contain compute resources (hosts and clusters).

        """
        NETWORK = None
        """
        A folder that can contain networkds.

        """
        VIRTUAL_MACHINE = None
        """
        A folder that can contain virtual machines.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('DATACENTER'),
        Type('DATASTORE'),
        Type('HOST'),
        Type('NETWORK'),
        Type('VIRTUAL_MACHINE'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.folder.type',
        Type))


    class FilterSpec(VapiStruct):
        """
        The ``Folder.FilterSpec`` class contains attributes used to filter the
        results when listing folders (see :func:`Folder.list`). If multiple
        attributes are specified, only folders matching all of the attributes match
        the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     folders=None,
                     names=None,
                     type=None,
                     parent_folders=None,
                     datacenters=None,
                    ):
            """
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Identifiers of folders that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, folders with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that folders must have to match the filter (see
                :attr:`Folder.Summary.name`).
                If None or empty, folders with any name match the filter.
            :type  type: :class:`Folder.Type` or ``None``
            :param type: Type that folders must have to match the filter (see
                :attr:`Folder.Summary.type`).
                If None, folders with any type match the filter.
            :type  parent_folders: :class:`set` of :class:`str` or ``None``
            :param parent_folders: Folders that must contain the folder for the folder to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, folder in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the folder for the folder to match
                the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, folder in any datacenter match the filter.
            """
            self.folders = folders
            self.names = names
            self.type = type
            self.parent_folders = parent_folders
            self.datacenters = datacenters
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.folder.filter_spec', {
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'type': type.OptionalType(type.ReferenceType(__name__, 'Folder.Type')),
            'parent_folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Folder.Summary`` class contains commonly used information about a
        folder.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     folder=None,
                     name=None,
                     type=None,
                    ):
            """
            :type  folder: :class:`str`
            :param folder: Identifier of the folder.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
            :type  name: :class:`str`
            :param name: Name of the vCenter Server folder.
            :type  type: :class:`Folder.Type`
            :param type: Type (DATACENTER, DATASTORE, HOST, NETWORK, VIRTUAL_MACHINE) of the
                vCenter Server folder.
            """
            self.folder = folder
            self.name = name
            self.type = type
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.folder.summary', {
            'folder': type.IdType(resource_types='Folder'),
            'name': type.StringType(),
            'type': type.ReferenceType(__name__, 'Folder.Type'),
        },
        Summary,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) folders in vCenter matching the :class:`Folder.FilterSpec`.

        :type  filter: :class:`Folder.FilterSpec` or ``None``
        :param filter: Specification of matching folders for which information should be
            returned.
            If None, the behavior is equivalent to a :class:`Folder.FilterSpec`
            with all attributes None which means all folders match the filter.
        :rtype: :class:`list` of :class:`Folder.Summary`
        :return: Commonly used information about the folders matching the
            :class:`Folder.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Folder.FilterSpec.type` attribute contains a value
            that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 folders match the :class:`Folder.FilterSpec`.
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
                            'filter': filter,
                            })
class Host(VapiInterface):
    """
    The ``Host`` class provides methods to manage hosts in the vCenter Server.
    """
    RESOURCE_TYPE = "HostSystem"
    """
    The resource type for the vCenter Host.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HostStub)

    class ConnectionState(Enum):
        """
        The ``Host.ConnectionState`` class defines the connection status of a host.

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
        Host is connected to the vCenter Server

        """
        DISCONNECTED = None
        """
        Host is disconnected from the vCenter Server

        """
        NOT_RESPONDING = None
        """
        VirtualCenter is not receiving heartbeats from the server. The state
        automatically changes to connected once heartbeats are received again.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ConnectionState` instance.
            """
            Enum.__init__(string)

    ConnectionState._set_values([
        ConnectionState('CONNECTED'),
        ConnectionState('DISCONNECTED'),
        ConnectionState('NOT_RESPONDING'),
    ])
    ConnectionState._set_binding_type(type.EnumType(
        'com.vmware.vcenter.host.connection_state',
        ConnectionState))


    class PowerState(Enum):
        """
        The ``Host.PowerState`` class defines the power states of a host.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        POWERED_ON = None
        """
        The host is powered on. A host that is entering standby mode is also in
        this state.

        """
        POWERED_OFF = None
        """
        The host was specifically powered off by the user through vCenter server.
        This state is not a cetain state, because after vCenter server issues the
        command to power off the host, the host might crash, or kill all the
        processes but fail to power off.

        """
        STANDBY = None
        """
        The host was specifically put in standby mode, either explicitly by the
        user, or automatically by DPM. This state is not a cetain state, because
        after VirtualCenter issues the command to put the host in standby state,
        the host might crash, or kill all the processes but fail to enter standby
        mode. A host that is exiting standby mode is also in this state.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`PowerState` instance.
            """
            Enum.__init__(string)

    PowerState._set_values([
        PowerState('POWERED_ON'),
        PowerState('POWERED_OFF'),
        PowerState('STANDBY'),
    ])
    PowerState._set_binding_type(type.EnumType(
        'com.vmware.vcenter.host.power_state',
        PowerState))


    class CreateSpec(VapiStruct):
        """
        The ``Host.CreateSpec`` class defines the information used to create a
        host.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'thumbprint_verification',
                {
                    'THUMBPRINT' : [('thumbprint', True)],
                    'NONE' : [],
                }
            ),
        ]



        def __init__(self,
                     hostname=None,
                     port=None,
                     user_name=None,
                     password=None,
                     folder=None,
                     thumbprint_verification=None,
                     thumbprint=None,
                     force_add=None,
                    ):
            """
            :type  hostname: :class:`str`
            :param hostname: The IP address or DNS resolvable name of the host.
            :type  port: :class:`long` or ``None``
            :param port: The port of the host.
                If None, port 443 will be used.
            :type  user_name: :class:`str`
            :param user_name: The administrator account on the host.
            :type  password: :class:`str`
            :param password: The password for the administrator account on the host.
            :type  folder: :class:`str` or ``None``
            :param folder: Host and cluster folder in which the new standalone host should be
                created.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                This attribute is currently required. In the future, if this
                attribute is None, the system will attempt to choose a suitable
                folder for the host; if a folder cannot be chosen, the host
                creation operation will fail.
            :type  thumbprint_verification: :class:`Host.CreateSpec.ThumbprintVerification`
            :param thumbprint_verification: Type of host's SSL certificate verification to be done.
            :type  thumbprint: :class:`str`
            :param thumbprint: The thumbprint of the SSL certificate, which the host is expected
                to have. The thumbprint is always computed using the SHA1 hash and
                is the string representation of that hash in the format:
                xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx where,
                'x' represents a hexadecimal digit.
                This attribute is optional and it is only relevant when the value
                of ``thumbprintVerification`` is
                :attr:`Host.CreateSpec.ThumbprintVerification.THUMBPRINT`.
            :type  force_add: :class:`bool` or ``None``
            :param force_add: Whether host should be added to the vCenter Server even if it is
                being managed by another vCenter Server. The original vCenterServer
                loses connection to the host.
                If None, forceAdd is default to false.
            """
            self.hostname = hostname
            self.port = port
            self.user_name = user_name
            self.password = password
            self.folder = folder
            self.thumbprint_verification = thumbprint_verification
            self.thumbprint = thumbprint
            self.force_add = force_add
            VapiStruct.__init__(self)

        class ThumbprintVerification(Enum):
            """
            The ``Host.CreateSpec.ThumbprintVerification`` class defines the thumbprint
            verification schemes for a host's SSL certificate.

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
            Accept the host's thumbprint without verifying it.

            """
            THUMBPRINT = None
            """
            Host's SSL certificate verified by checking its thumbprint against the
            specified thumbprint.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`ThumbprintVerification` instance.
                """
                Enum.__init__(string)

        ThumbprintVerification._set_values([
            ThumbprintVerification('NONE'),
            ThumbprintVerification('THUMBPRINT'),
        ])
        ThumbprintVerification._set_binding_type(type.EnumType(
            'com.vmware.vcenter.host.create_spec.thumbprint_verification',
            ThumbprintVerification))

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.host.create_spec', {
            'hostname': type.StringType(),
            'port': type.OptionalType(type.IntegerType()),
            'user_name': type.StringType(),
            'password': type.SecretType(),
            'folder': type.OptionalType(type.IdType()),
            'thumbprint_verification': type.ReferenceType(__name__, 'Host.CreateSpec.ThumbprintVerification'),
            'thumbprint': type.OptionalType(type.StringType()),
            'force_add': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Host.FilterSpec`` class contains attributes used to filter the
        results when listing hosts (see :func:`Host.list`). If multiple attributes
        are specified, only hosts matching all of the attributes match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     hosts=None,
                     names=None,
                     folders=None,
                     datacenters=None,
                     standalone=None,
                     clusters=None,
                     connection_states=None,
                    ):
            """
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: Identifiers of hosts that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                If None or empty, hosts with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that hosts must have to match the filter (see
                :attr:`Host.Summary.name`).
                If None or empty, hosts with any name match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the hosts for the hosts to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, hosts in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the hosts for the hosts to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, hosts in any datacenter match the filter.
            :type  standalone: :class:`bool` or ``None``
            :param standalone: If true, only hosts that are not part of a cluster can match the
                filter, and if false, only hosts that are are part of a cluster can
                match the filter.
                If None Hosts can match filter independent of whether they are part
                of a cluster or not. If this field is true and
                :attr:`Host.FilterSpec.clusters` os not empty, no hosts will match
                the filter.
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: Clusters that must contain the hosts for the hosts to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None or empty, hosts in any cluster and hosts that are not in a
                cluster match the filter. If this attribute is not empty and
                :attr:`Host.FilterSpec.standalone` is true, no hosts will match the
                filter.
            :type  connection_states: :class:`set` of :class:`Host.ConnectionState` or ``None``
            :param connection_states: Connection states that a host must be in to match the filter (see
                :attr:`Host.Summary.connection_state`.
                If None or empty, hosts in any connection state match the filter.
            """
            self.hosts = hosts
            self.names = names
            self.folders = folders
            self.datacenters = datacenters
            self.standalone = standalone
            self.clusters = clusters
            self.connection_states = connection_states
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.host.filter_spec', {
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
            'standalone': type.OptionalType(type.BooleanType()),
            'clusters': type.OptionalType(type.SetType(type.IdType())),
            'connection_states': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'Host.ConnectionState'))),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Host.Summary`` class contains commonly used information about a host
        in vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'connection_state',
                {
                    'CONNECTED' : [('power_state', True)],
                    'DISCONNECTED' : [],
                    'NOT_RESPONDING' : [],
                }
            ),
        ]



        def __init__(self,
                     host=None,
                     name=None,
                     connection_state=None,
                     power_state=None,
                    ):
            """
            :type  host: :class:`str`
            :param host: Identifier of the host.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
            :type  name: :class:`str`
            :param name: Name of the host.
            :type  connection_state: :class:`Host.ConnectionState`
            :param connection_state: Connection status of the host
            :type  power_state: :class:`Host.PowerState`
            :param power_state: Power state of the host
                This attribute is optional and it is only relevant when the value
                of ``connectionState`` is :attr:`Host.ConnectionState.CONNECTED`.
            """
            self.host = host
            self.name = name
            self.connection_state = connection_state
            self.power_state = power_state
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.host.summary', {
            'host': type.IdType(resource_types='HostSystem'),
            'name': type.StringType(),
            'connection_state': type.ReferenceType(__name__, 'Host.ConnectionState'),
            'power_state': type.OptionalType(type.ReferenceType(__name__, 'Host.PowerState')),
        },
        Summary,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Add a new standalone host in the vCenter inventory. The newly connected
        host will be in connected state. The vCenter Server will verify the SSL
        certificate before adding the host to its inventory. In the case where
        the SSL certificate cannot be verified because the Certificate
        Authority is not recognized or the certificate is self signed, the
        vCenter Server will fall back to thumbprint verification mode as
        defined by :class:`Host.CreateSpec.ThumbprintVerification`.

        :type  spec: :class:`Host.CreateSpec`
        :param spec: Specification for the new host to be created.
        :rtype: :class:`str`
        :return: The newly created identifier of the host in vCenter.
            The return value will be an identifier for the resource type:
            ``HostSystem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the host with the same name is already present.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if installation of VirtualCenter agent on a host fails.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the host name is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the host folder is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the SSL thumbprint specified is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the host folder id does not support vSphere compute resource as
            its children type.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no folder associated with the ``folder`` attribute in
            the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the host is already being managed by another vCenter Server
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if there are not enough licenses to add the host.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user name or password for the administration account on the
            host are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the software version on the host is not supported.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def delete(self,
               host,
               ):
        """
        Remove a standalone host from the vCenter Server.

        :type  host: :class:`str`
        :param host: Identifier of the host to be deleted.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no host associated with ``host`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if the host associated with ``host`` is in a vCenter cluster
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
                            'host': host,
                            })

    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) hosts in vCenter matching the :class:`Host.FilterSpec`.

        :type  filter: :class:`Host.FilterSpec` or ``None``
        :param filter: Specification of matching hosts for which information should be
            returned.
            If None, the behavior is equivalent to a :class:`Host.FilterSpec`
            with all attributes None which means all hosts match the filter.
        :rtype: :class:`list` of :class:`Host.Summary`
        :return: Commonly used information about the hosts matching the
            :class:`Host.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Host.FilterSpec.connection_states` attribute contains
            a value that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 hosts match the :class:`Host.FilterSpec`.
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
                            'filter': filter,
                            })

    def connect(self,
                host,
                ):
        """
        Connect to the host corresponding to ``host`` previously added to the
        vCenter server.

        :type  host: :class:`str`
        :param host: Identifier of the host to be reconnected.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the host associated with ``host`` is already connected.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no host associated with ``host`` in the system.
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
                            'host': host,
                            })

    def disconnect(self,
                   host,
                   ):
        """
        Disconnect the host corresponding to ``host`` from the vCenter server

        :type  host: :class:`str`
        :param host: Identifier of the host to be disconnected.
            The parameter must be an identifier for the resource type:
            ``HostSystem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the host associated with ``host`` is already disconnected.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no host associated with ``host`` in the system.
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
                            'host': host,
                            })
class Network(VapiInterface):
    """
    The Network class provides methods for manipulating a vCenter Server
    network.
    """
    RESOURCE_TYPE = "Network"
    """
    The resource type for the vCenter network

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NetworkStub)

    class Type(Enum):
        """
        The ``Network.Type`` class defines the type of a vCenter Server network.
        The type of a network can be used to determine what features it supports
        and which APIs can be used to find more information about the network or
        change its configuration.

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
        XXX: ESX based (created and managed on ESX)

        """
        DISTRIBUTED_PORTGROUP = None
        """
        XXX: vCenter based (create and managed through vCenter)

        """
        OPAQUE_NETWORK = None
        """
        A network for whose configuration is managed outside of vSphere. The
        identifer and name of the network is made available through vSphere so that
        host and virtual machine virtual ethernet devices can connect to them.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('STANDARD_PORTGROUP'),
        Type('DISTRIBUTED_PORTGROUP'),
        Type('OPAQUE_NETWORK'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vcenter.network.type',
        Type))


    class FilterSpec(VapiStruct):
        """
        The ``Network.FilterSpec`` class contains attributes used to filter the
        results when listing networks (see :func:`Network.list`). If multiple
        attributes are specified, only networks matching all of the attributes
        match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     networks=None,
                     names=None,
                     types=None,
                     folders=None,
                     datacenters=None,
                    ):
            """
            :type  networks: :class:`set` of :class:`str` or ``None``
            :param networks: Identifiers of networks that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Network``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Network``.
                If None or empty, networks with any identifier match the filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that networks must have to match the filter (see
                :attr:`Network.Summary.name`).
                If None or empty, networks with any name match the filter.
            :type  types: :class:`set` of :class:`Network.Type` or ``None``
            :param types: Types that networks must have to match the filter (see
                :attr:`Network.Summary.type`).
                If None, networks with any type match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the network for the network to match the
                filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, networks in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the network for the network to match
                the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, networks in any datacenter match the filter.
            """
            self.networks = networks
            self.names = names
            self.types = types
            self.folders = folders
            self.datacenters = datacenters
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.network.filter_spec', {
            'networks': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'types': type.OptionalType(type.SetType(type.ReferenceType(__name__, 'Network.Type'))),
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Network.Summary`` class contains commonly used information about a
        network.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     network=None,
                     name=None,
                     type=None,
                    ):
            """
            :type  network: :class:`str`
            :param network: Identifier of the network.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Network``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Network``.
            :type  name: :class:`str`
            :param name: Name of the network.
            :type  type: :class:`Network.Type`
            :param type: Type (STANDARD_PORTGROUP, DISTRIBUTED_PORTGROUP, OPAQUE_NETWORK) of
                the vCenter Server network.
            """
            self.network = network
            self.name = name
            self.type = type
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.network.summary', {
            'network': type.IdType(resource_types='Network'),
            'name': type.StringType(),
            'type': type.ReferenceType(__name__, 'Network.Type'),
        },
        Summary,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) networks in vCenter matching the :class:`Network.FilterSpec`.

        :type  filter: :class:`Network.FilterSpec` or ``None``
        :param filter: Specification of matching networks for which information should be
            returned.
            If None, the behavior is equivalent to a
            :class:`Network.FilterSpec` with all attributes None which means
            all networks match the filter.
        :rtype: :class:`list` of :class:`Network.Summary`
        :return: Commonly used information about the networks matching the
            :class:`Network.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Network.FilterSpec.types` attribute contains a value
            that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 networks match the :class:`Network.FilterSpec`.
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
                            'filter': filter,
                            })
class ResourcePool(VapiInterface):
    """
    The ResourcePool class provides methods for manipulating a vCenter Server
    resource pool. 
    
    This class does not include virtual appliances in the inventory of resource
    pools even though part of the behavior of a virtual appliance is to act
    like a resource pool.
    """
    RESOURCE_TYPE = "ResourcePool"
    """
    The resource type for the vCenter resource pool

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ResourcePoolStub)

    class Info(VapiStruct):
        """
        The ``ResourcePool.Info`` class contains information about a resource pool.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     resource_pools=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: Name of the vCenter Server resource pool.
            :type  resource_pools: :class:`set` of :class:`str`
            :param resource_pools: Identifiers of the child resource pools contained in this resource
                pool.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``ResourcePool``.
            """
            self.name = name
            self.resource_pools = resource_pools
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.resource_pool.info', {
            'name': type.StringType(),
            'resource_pools': type.SetType(type.IdType()),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``ResourcePool.FilterSpec`` class contains attributes used to filter
        the results when listing resource pools (see :func:`ResourcePool.list`). If
        multiple attributes are specified, only resource pools matching all of the
        attributes match the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     resource_pools=None,
                     names=None,
                     parent_resource_pools=None,
                     datacenters=None,
                     hosts=None,
                     clusters=None,
                    ):
            """
            :type  resource_pools: :class:`set` of :class:`str` or ``None``
            :param resource_pools: Identifiers of resource pools that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``ResourcePool``.
                If None or empty, resource pools with any identifier match the
                filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that resource pools must have to match the filter (see
                :attr:`ResourcePool.Info.name`).
                If None or empty, resource pools with any name match the filter.
            :type  parent_resource_pools: :class:`set` of :class:`str` or ``None``
            :param parent_resource_pools: Resource pools that must contain the resource pool for the resource
                pool to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``ResourcePool``.
                If None or empty, resource pools in any resource pool match the
                filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the resource pool for the resource
                pool to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, resource pools in any datacenter match the
                filter.
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: Hosts that must contain the resource pool for the resource pool to
                match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                If None or empty, resource pools in any host match the filter.
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: Clusters that must contain the resource pool for the resource pool
                to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None or empty, resource pools in any cluster match the filter.
            """
            self.resource_pools = resource_pools
            self.names = names
            self.parent_resource_pools = parent_resource_pools
            self.datacenters = datacenters
            self.hosts = hosts
            self.clusters = clusters
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.resource_pool.filter_spec', {
            'resource_pools': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'parent_resource_pools': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'clusters': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``ResourcePool.Summary`` class contains commonly used information about
        a resource pool in vCenter Server.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     resource_pool=None,
                     name=None,
                    ):
            """
            :type  resource_pool: :class:`str`
            :param resource_pool: Identifier of the resource pool.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
            :type  name: :class:`str`
            :param name: Name of the resource pool.
            """
            self.resource_pool = resource_pool
            self.name = name
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.resource_pool.summary', {
            'resource_pool': type.IdType(resource_types='ResourcePool'),
            'name': type.StringType(),
        },
        Summary,
        False,
        None))



    def get(self,
            resource_pool,
            ):
        """
        Retrieves information about the resource pool indicated by
        ``resource_pool``.

        :type  resource_pool: :class:`str`
        :param resource_pool: Identifier of the resource pool for which information should be
            retrieved.
            The parameter must be an identifier for the resource type:
            ``ResourcePool``.
        :rtype: :class:`ResourcePool.Info`
        :return: information about the resource pool.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the resource pool indicated by ``resource_pool`` does not exist.
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
                            'resource_pool': resource_pool,
                            })

    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) resource pools in vCenter matching the
        :class:`ResourcePool.FilterSpec`.

        :type  filter: :class:`ResourcePool.FilterSpec` or ``None``
        :param filter: Specification of matching resource pools for which information
            should be returned.
            If None, the behavior is equivalent to a
            :class:`ResourcePool.FilterSpec` with all attributes None which
            means all resource pools match the filter.
        :rtype: :class:`list` of :class:`ResourcePool.Summary`
        :return: Commonly used information about the resource pools matching the
            :class:`ResourcePool.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 resource pools match the
            :class:`ResourcePool.FilterSpec`.
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
                            'filter': filter,
                            })
class VM(VapiInterface):
    """
    The ``VM`` class provides methods for managing the lifecycle of a virtual
    machine.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VMStub)

    class PlacementSpec(VapiStruct):
        """
        The ``VM.PlacementSpec`` class contains information used to place a virtual
        machine onto resources within the vCenter inventory.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     folder=None,
                     resource_pool=None,
                     host=None,
                     cluster=None,
                     datastore=None,
                    ):
            """
            :type  folder: :class:`str` or ``None``
            :param folder: Virtual machine folder into which the virtual machine should be
                placed.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type: ``Folder``.
                When methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type: ``Folder``.
                This attribute is currently required. In the future, if this
                attribute is None, the system will attempt to choose a suitable
                folder for the virtual machine; if a folder cannot be chosen, the
                virtual machine creation operation will fail.
            :type  resource_pool: :class:`str` or ``None``
            :param resource_pool: Resource pool into which the virtual machine should be placed.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``ResourcePool``.
                This attribute is currently required if both ``host`` and
                ``cluster`` are None. In the future, if this attribute is None, the
                system will attempt to choose a suitable resource pool for the
                virtual machine; if a resource pool cannot be chosen, the virtual
                machine creation operation will fail.
            :type  host: :class:`str` or ``None``
            :param host: Host onto which the virtual machine should be placed. 
                
                If ``host`` and ``resourcePool`` are both specified,
                ``resourcePool`` must belong to ``host``. 
                
                If ``host`` and ``cluster`` are both specified, ``host`` must be a
                member of ``cluster``.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``HostSystem``.
                This attribute may be None if ``resourcePool`` or ``cluster`` is
                specified. If None, the system will attempt to choose a suitable
                host for the virtual machine; if a host cannot be chosen, the
                virtual machine creation operation will fail.
            :type  cluster: :class:`str` or ``None``
            :param cluster: Cluster into which the virtual machine should be placed. 
                
                If ``cluster`` and ``resourcePool`` are both specified,
                ``resourcePool`` must belong to ``cluster``. 
                
                If ``cluster`` and ``host`` are both specified, ``host`` must be a
                member of ``cluster``.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``ClusterComputeResource``.
                If ``resourcePool`` or ``host`` is specified, it is recommended
                that this attribute be None.
            :type  datastore: :class:`str` or ``None``
            :param datastore: Datastore on which the virtual machine's configuration state should
                be stored. This datastore will also be used for any virtual disks
                that are created as part of the virtual machine creation operation.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
                This attribute is currently required. In the future, if this
                attribute is None, the system will attempt to choose suitable
                storage for the virtual machine; if storage cannot be chosen, the
                virtual machine creation operation will fail.
            """
            self.folder = folder
            self.resource_pool = resource_pool
            self.host = host
            self.cluster = cluster
            self.datastore = datastore
            VapiStruct.__init__(self)

    PlacementSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.VM.placement_spec', {
            'folder': type.OptionalType(type.IdType()),
            'resource_pool': type.OptionalType(type.IdType()),
            'host': type.OptionalType(type.IdType()),
            'cluster': type.OptionalType(type.IdType()),
            'datastore': type.OptionalType(type.IdType()),
        },
        PlacementSpec,
        False,
        None))


    class StoragePolicySpec(VapiStruct):
        """
        The ``VM.StoragePolicySpec`` class contains information about the storage
        policy to be associated with a virtual machine object. This class was added
        in vSphere API 6.7

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
                the virtual machine. This attribute was added in vSphere API 6.7
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
        'com.vmware.vcenter.VM.storage_policy_spec', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.StoragePolicy'),
        },
        StoragePolicySpec,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        Document-based creation spec.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'guest_OS': 'guest_os',
                                }

        def __init__(self,
                     guest_os=None,
                     name=None,
                     placement=None,
                     hardware_version=None,
                     boot=None,
                     boot_devices=None,
                     cpu=None,
                     memory=None,
                     disks=None,
                     nics=None,
                     cdroms=None,
                     floppies=None,
                     parallel_ports=None,
                     serial_ports=None,
                     sata_adapters=None,
                     scsi_adapters=None,
                     storage_policy=None,
                    ):
            """
            :type  guest_os: :class:`com.vmware.vcenter.vm_client.GuestOS`
            :param guest_os: Guest OS.
            :type  name: :class:`str` or ``None``
            :param name: Virtual machine name.
                If None, a default name will be generated by the server.
            :type  placement: :class:`VM.PlacementSpec` or ``None``
            :param placement: Virtual machine placement information.
                This attribute is currently required. In the future, if this
                attribute is None, the system will attempt to choose suitable
                resources on which to place the virtual machine.
            :type  hardware_version: :class:`com.vmware.vcenter.vm_client.Hardware.Version` or ``None``
            :param hardware_version: Virtual hardware version.
                If None, defaults to the most recent version supported by the
                server.
            :type  boot: :class:`com.vmware.vcenter.vm.hardware_client.Boot.CreateSpec` or ``None``
            :param boot: Boot configuration.
                If None, guest-specific default values will be used.
            :type  boot_devices: :class:`list` of :class:`com.vmware.vcenter.vm.hardware.boot_client.Device.EntryCreateSpec` or ``None``
            :param boot_devices: Boot device configuration.
                If None, a server-specific boot sequence will be used.
            :type  cpu: :class:`com.vmware.vcenter.vm.hardware_client.Cpu.UpdateSpec` or ``None``
            :param cpu: CPU configuration.
                If None, guest-specific default values will be used.
            :type  memory: :class:`com.vmware.vcenter.vm.hardware_client.Memory.UpdateSpec` or ``None``
            :param memory: Memory configuration.
                If None, guest-specific default values will be used.
            :type  disks: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Disk.CreateSpec` or ``None``
            :param disks: List of disks.
                If None, a single blank virtual disk of a guest-specific size will
                be created on the same storage as the virtual machine
                configuration, and will use a guest-specific host bus adapter type.
                If the guest-specific size is 0, no virtual disk will be created.
            :type  nics: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Ethernet.CreateSpec` or ``None``
            :param nics: List of Ethernet adapters.
                If None, no Ethernet adapters will be created.
            :type  cdroms: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Cdrom.CreateSpec` or ``None``
            :param cdroms: List of CD-ROMs.
                If None, no CD-ROM devices will be created.
            :type  floppies: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Floppy.CreateSpec` or ``None``
            :param floppies: List of floppy drives.
                If None, no floppy drives will be created.
            :type  parallel_ports: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Parallel.CreateSpec` or ``None``
            :param parallel_ports: List of parallel ports.
                If None, no parallel ports will be created.
            :type  serial_ports: :class:`list` of :class:`com.vmware.vcenter.vm.hardware_client.Serial.CreateSpec` or ``None``
            :param serial_ports: List of serial ports.
                If None, no serial ports will be created.
            :type  sata_adapters: :class:`list` of :class:`com.vmware.vcenter.vm.hardware.adapter_client.Sata.CreateSpec` or ``None``
            :param sata_adapters: List of SATA adapters.
                If None, any adapters necessary to connect the virtual machine's
                storage devices will be created; this includes any devices that
                explicitly specify a SATA host bus adapter, as well as any devices
                that do not specify a host bus adapter if the guest's preferred
                adapter type is SATA.
            :type  scsi_adapters: :class:`list` of :class:`com.vmware.vcenter.vm.hardware.adapter_client.Scsi.CreateSpec` or ``None``
            :param scsi_adapters: List of SCSI adapters.
                If None, any adapters necessary to connect the virtual machine's
                storage devices will be created; this includes any devices that
                explicitly specify a SCSI host bus adapter, as well as any devices
                that do not specify a host bus adapter if the guest's preferred
                adapter type is SCSI. The type of the SCSI adapter will be a
                guest-specific default type.
            :type  storage_policy: :class:`VM.StoragePolicySpec` or ``None``
            :param storage_policy: The ``VM.StoragePolicySpec`` class contains information about the
                storage policy that is to be associated with the virtual machine
                home (which contains the configuration and log files). This
                attribute was added in vSphere API 6.7
                If None the datastore default storage policy (if applicable) is
                applied. Currently a default storage policy is only supported by
                object datastores : VVol and vSAN. For non-object datastores, if
                None then no storage policy would be associated with the virtual
                machine home.
            """
            self.guest_os = guest_os
            self.name = name
            self.placement = placement
            self.hardware_version = hardware_version
            self.boot = boot
            self.boot_devices = boot_devices
            self.cpu = cpu
            self.memory = memory
            self.disks = disks
            self.nics = nics
            self.cdroms = cdroms
            self.floppies = floppies
            self.parallel_ports = parallel_ports
            self.serial_ports = serial_ports
            self.sata_adapters = sata_adapters
            self.scsi_adapters = scsi_adapters
            self.storage_policy = storage_policy
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.VM.create_spec', {
            'guest_OS': type.ReferenceType('com.vmware.vcenter.vm_client', 'GuestOS'),
            'name': type.OptionalType(type.StringType()),
            'placement': type.OptionalType(type.ReferenceType(__name__, 'VM.PlacementSpec')),
            'hardware_version': type.OptionalType(type.ReferenceType('com.vmware.vcenter.vm_client', 'Hardware.Version')),
            'boot': type.OptionalType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Boot.CreateSpec')),
            'boot_devices': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware.boot_client', 'Device.EntryCreateSpec'))),
            'cpu': type.OptionalType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Cpu.UpdateSpec')),
            'memory': type.OptionalType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Memory.UpdateSpec')),
            'disks': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Disk.CreateSpec'))),
            'nics': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Ethernet.CreateSpec'))),
            'cdroms': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Cdrom.CreateSpec'))),
            'floppies': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Floppy.CreateSpec'))),
            'parallel_ports': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Parallel.CreateSpec'))),
            'serial_ports': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Serial.CreateSpec'))),
            'sata_adapters': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware.adapter_client', 'Sata.CreateSpec'))),
            'scsi_adapters': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware.adapter_client', 'Scsi.CreateSpec'))),
            'storage_policy': type.OptionalType(type.ReferenceType(__name__, 'VM.StoragePolicySpec')),
        },
        CreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        Document-based info.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'guest_OS': 'guest_os',
                                }

        def __init__(self,
                     guest_os=None,
                     name=None,
                     power_state=None,
                     hardware=None,
                     boot=None,
                     boot_devices=None,
                     cpu=None,
                     memory=None,
                     disks=None,
                     nics=None,
                     cdroms=None,
                     floppies=None,
                     parallel_ports=None,
                     serial_ports=None,
                     sata_adapters=None,
                     scsi_adapters=None,
                    ):
            """
            :type  guest_os: :class:`com.vmware.vcenter.vm_client.GuestOS`
            :param guest_os: Guest OS.
            :type  name: :class:`str`
            :param name: Virtual machine name.
            :type  power_state: :class:`com.vmware.vcenter.vm_client.Power.State`
            :param power_state: Power state of the virtual machine.
            :type  hardware: :class:`com.vmware.vcenter.vm_client.Hardware.Info`
            :param hardware: Virtual hardware version information.
            :type  boot: :class:`com.vmware.vcenter.vm.hardware_client.Boot.Info`
            :param boot: Boot configuration.
            :type  boot_devices: :class:`list` of :class:`com.vmware.vcenter.vm.hardware.boot_client.Device.Entry`
            :param boot_devices: Boot device configuration. If the :class:`list` has no entries, a
                server-specific default boot sequence is used.
            :type  cpu: :class:`com.vmware.vcenter.vm.hardware_client.Cpu.Info`
            :param cpu: CPU configuration.
            :type  memory: :class:`com.vmware.vcenter.vm.hardware_client.Memory.Info`
            :param memory: Memory configuration.
            :type  disks: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Disk.Info`
            :param disks: List of disks.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            :type  nics: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Ethernet.Info`
            :param nics: List of Ethernet adapters.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Ethernet``.
            :type  cdroms: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Cdrom.Info`
            :param cdroms: List of CD-ROMs.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Cdrom``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Cdrom``.
            :type  floppies: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Floppy.Info`
            :param floppies: List of floppy drives.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Floppy``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Floppy``.
            :type  parallel_ports: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Parallel.Info`
            :param parallel_ports: List of parallel ports.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.ParallelPort``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.ParallelPort``.
            :type  serial_ports: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware_client.Serial.Info`
            :param serial_ports: List of serial ports.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.SerialPort``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.SerialPort``.
            :type  sata_adapters: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware.adapter_client.Sata.Info`
            :param sata_adapters: List of SATA adapters.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.SataAdapter``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.SataAdapter``.
            :type  scsi_adapters: :class:`dict` of :class:`str` and :class:`com.vmware.vcenter.vm.hardware.adapter_client.Scsi.Info`
            :param scsi_adapters: List of SCSI adapters.
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.ScsiAdapter``. When methods
                return a value of this class as a return value, the key in the
                attribute :class:`dict` will be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.ScsiAdapter``.
            """
            self.guest_os = guest_os
            self.name = name
            self.power_state = power_state
            self.hardware = hardware
            self.boot = boot
            self.boot_devices = boot_devices
            self.cpu = cpu
            self.memory = memory
            self.disks = disks
            self.nics = nics
            self.cdroms = cdroms
            self.floppies = floppies
            self.parallel_ports = parallel_ports
            self.serial_ports = serial_ports
            self.sata_adapters = sata_adapters
            self.scsi_adapters = scsi_adapters
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.VM.info', {
            'guest_OS': type.ReferenceType('com.vmware.vcenter.vm_client', 'GuestOS'),
            'name': type.StringType(),
            'power_state': type.ReferenceType('com.vmware.vcenter.vm_client', 'Power.State'),
            'hardware': type.ReferenceType('com.vmware.vcenter.vm_client', 'Hardware.Info'),
            'boot': type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Boot.Info'),
            'boot_devices': type.ListType(type.ReferenceType('com.vmware.vcenter.vm.hardware.boot_client', 'Device.Entry')),
            'cpu': type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Cpu.Info'),
            'memory': type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Memory.Info'),
            'disks': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Disk.Info')),
            'nics': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Ethernet.Info')),
            'cdroms': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Cdrom.Info')),
            'floppies': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Floppy.Info')),
            'parallel_ports': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Parallel.Info')),
            'serial_ports': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware_client', 'Serial.Info')),
            'sata_adapters': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware.adapter_client', 'Sata.Info')),
            'scsi_adapters': type.MapType(type.IdType(), type.ReferenceType('com.vmware.vcenter.vm.hardware.adapter_client', 'Scsi.Info')),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``VM.FilterSpec`` class contains attributes used to filter the results
        when listing virtual machines (see :func:`VM.list`). If multiple attributes
        are specified, only virtual machines matching all of the attributes match
        the filter.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vms=None,
                     names=None,
                     folders=None,
                     datacenters=None,
                     hosts=None,
                     clusters=None,
                     resource_pools=None,
                     power_states=None,
                    ):
            """
            :type  vms: :class:`set` of :class:`str` or ``None``
            :param vms: Identifiers of virtual machines that can match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``VirtualMachine``.
                If None or empty, virtual machines with any identifier match the
                filter.
            :type  names: :class:`set` of :class:`str` or ``None``
            :param names: Names that virtual machines must have to match the filter (see
                :attr:`VM.Info.name`).
                If None or empty, virtual machines with any name match the filter.
            :type  folders: :class:`set` of :class:`str` or ``None``
            :param folders: Folders that must contain the virtual machine for the virtual
                machine to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Folder``. When methods return a value of this class as a return
                value, the attribute will contain identifiers for the resource
                type: ``Folder``.
                If None or empty, virtual machines in any folder match the filter.
            :type  datacenters: :class:`set` of :class:`str` or ``None``
            :param datacenters: Datacenters that must contain the virtual machine for the virtual
                machine to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``Datacenter``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``Datacenter``.
                If None or empty, virtual machines in any datacenter match the
                filter.
            :type  hosts: :class:`set` of :class:`str` or ``None``
            :param hosts: Hosts that must contain the virtual machine for the virtual machine
                to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``HostSystem``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``HostSystem``.
                If None or empty, virtual machines on any host match the filter.
            :type  clusters: :class:`set` of :class:`str` or ``None``
            :param clusters: Clusters that must contain the virtual machine for the virtual
                machine to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ClusterComputeResource``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``ClusterComputeResource``.
                If None or empty, virtual machines in any cluster match the filter.
            :type  resource_pools: :class:`set` of :class:`str` or ``None``
            :param resource_pools: Resource pools that must contain the virtual machine for the
                virtual machine to match the filter.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``ResourcePool``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``ResourcePool``.
                If None or empty, virtual machines in any resource pool match the
                filter.
            :type  power_states: :class:`set` of :class:`com.vmware.vcenter.vm_client.Power.State` or ``None``
            :param power_states: Power states that a virtual machine must be in to match the filter
                (see :attr:`com.vmware.vcenter.vm_client.Power.Info.state`.
                If None or empty, virtual machines in any power state match the
                filter.
            """
            self.vms = vms
            self.names = names
            self.folders = folders
            self.datacenters = datacenters
            self.hosts = hosts
            self.clusters = clusters
            self.resource_pools = resource_pools
            self.power_states = power_states
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.VM.filter_spec', {
            'vms': type.OptionalType(type.SetType(type.IdType())),
            'names': type.OptionalType(type.SetType(type.StringType())),
            'folders': type.OptionalType(type.SetType(type.IdType())),
            'datacenters': type.OptionalType(type.SetType(type.IdType())),
            'hosts': type.OptionalType(type.SetType(type.IdType())),
            'clusters': type.OptionalType(type.SetType(type.IdType())),
            'resource_pools': type.OptionalType(type.SetType(type.IdType())),
            'power_states': type.OptionalType(type.SetType(type.ReferenceType('com.vmware.vcenter.vm_client', 'Power.State'))),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``VM.Summary`` class contains commonly used information about a virtual
        machine.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'memory_size_MiB': 'memory_size_mib',
                                }

        def __init__(self,
                     vm=None,
                     name=None,
                     power_state=None,
                     cpu_count=None,
                     memory_size_mib=None,
                    ):
            """
            :type  vm: :class:`str`
            :param vm: Identifier of the virtual machine.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``VirtualMachine``.
            :type  name: :class:`str`
            :param name: Name of the Virtual machine.
            :type  power_state: :class:`com.vmware.vcenter.vm_client.Power.State`
            :param power_state: Power state of the virtual machine.
            :type  cpu_count: :class:`long` or ``None``
            :param cpu_count: Number of CPU cores.
                This attribute will be None if the virtual machine configuration is
                not available. For example, the configuration information would be
                unavailable if the server is unable to access the virtual machine
                files on disk, and is often also unavailable during the intial
                phases of virtual machine creation.
            :type  memory_size_mib: :class:`long` or ``None``
            :param memory_size_mib: Memory size in mebibytes.
                This attribute will be None if the virtual machine configuration is
                not available. For example, the configuration information would be
                unavailable if the server is unable to access the virtual machine
                files on disk, and is often also unavailable during the intial
                phases of virtual machine creation.
            """
            self.vm = vm
            self.name = name
            self.power_state = power_state
            self.cpu_count = cpu_count
            self.memory_size_mib = memory_size_mib
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.VM.summary', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'name': type.StringType(),
            'power_state': type.ReferenceType('com.vmware.vcenter.vm_client', 'Power.State'),
            'cpu_count': type.OptionalType(type.IntegerType()),
            'memory_size_MiB': type.OptionalType(type.IntegerType()),
        },
        Summary,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Creates a virtual machine.

        :type  spec: :class:`VM.CreateSpec`
        :param spec: Virtual machine specification.
        :rtype: :class:`str`
        :return: ID of newly-created virtual machine.
            The return value will be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if a virtual machine with the specified name already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if any of the specified parameters are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if any of the resources specified in spec could not be found
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if a specified resource (eg. host) is not accessible.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInUse` 
            if any of the specified storage addresses (eg. IDE, SATA, SCSI)
            result in a storage address conflict.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if any of the resources needed to create the virtual machine could
            not be allocated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if ``guestOS`` is not supported for the requested virtual hardware
            version and spec includes None attributes that default to
            guest-specific values.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def get(self,
            vm,
            ):
        """
        Returns information about a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`VM.Info`
        :return: Information about the specified virtual machine.
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

    def delete(self,
               vm,
               ):
        """
        Deletes a virtual machine.

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the virtual machine is running (powered on).
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the virtual machine is not found.
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
                            })

    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) virtual machines in vCenter matching the
        :class:`VM.FilterSpec`.

        :type  filter: :class:`VM.FilterSpec` or ``None``
        :param filter: Specification of matching virtual machines for which information
            should be returned.
            If None, the behavior is equivalent to a :class:`VM.FilterSpec`
            with all attributes None which means all virtual machines match the
            filter.
        :rtype: :class:`list` of :class:`VM.Summary`
        :return: Commonly used information about the virtual machines matching the
            :class:`VM.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`VM.FilterSpec.power_states` attribute contains a
            value that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 virtual machines match the
            :class:`VM.FilterSpec`.
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
                            'filter': filter,
                            })
class Deployment(VapiInterface):
    """
    The ``Deployment`` class provides methods to get the status of the vCenter
    appliance deployment. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DeploymentStub)

    class Task(VapiStruct):
        """
        The ``Deployment.Task`` class contains attributes to describe a particular
        deployment task. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'status',
                {
                    'RUNNING' : [('progress', True), ('result', False), ('start_time', True)],
                    'BLOCKED' : [('progress', True), ('result', False), ('start_time', True)],
                    'SUCCEEDED' : [('progress', True), ('result', False), ('start_time', True), ('end_time', True)],
                    'FAILED' : [('progress', True), ('result', False), ('error', False), ('start_time', True), ('end_time', True)],
                    'PENDING' : [],
                }
            ),
        ]



        def __init__(self,
                     progress=None,
                     result=None,
                     description=None,
                     service=None,
                     operation=None,
                     parent=None,
                     target=None,
                     status=None,
                     cancelable=None,
                     error=None,
                     start_time=None,
                     end_time=None,
                     user=None,
                    ):
            """
            :type  progress: :class:`com.vmware.cis.task_client.Progress`
            :param progress: The progress info of this deployment task. This attribute was added
                in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``#status`` is one of
                :attr:`com.vmware.cis.task_client.Status.RUNNING`,
                :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  result: :class:`com.vmware.vcenter.deployment_client.Notifications` or ``None``
            :param result: Result of the task. This attribute was added in vSphere API 6.7
                This attribute will be None if result is not available at the
                current step of the task.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the operation associated with the task.
            :type  service: :class:`str`
            :param service: Name of the service containing the operation.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.service``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.service``.
            :type  operation: :class:`str`
            :param operation: Name of the operation associated with the task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.operation``.
            :type  parent: :class:`str` or ``None``
            :param parent: Parent of the current task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.task``. When methods return a value of this class
                as a return value, the attribute will be an identifier for the
                resource type: ``com.vmware.cis.task``.
                This attribute will be None if the task has no parent.
            :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
            :param target: Identifier of the target created by the operation or an existing
                one the operation performed on.
                This attribute will be None if the operation has no target or
                multiple targets.
            :type  status: :class:`com.vmware.cis.task_client.Status`
            :param status: Status of the operation associated with the task.
            :type  cancelable: :class:`bool`
            :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
                value may change as the operation progresses.
            :type  error: :class:`Exception` or ``None``
            :param error: Description of the error if the operation status is "FAILED".
                If None the description of why the operation failed will be
                included in the result of the operation (see
                :attr:`com.vmware.cis.task_client.Info.result`).
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the operation is started.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.RUNNING`,
                :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the operation is completed.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  user: :class:`str` or ``None``
            :param user: Name of the user who performed the operation.
                This attribute will be None if the operation is performed by the
                system.
            """
            self.progress = progress
            self.result = result
            self.description = description
            self.service = service
            self.operation = operation
            self.parent = parent
            self.target = target
            self.status = status
            self.cancelable = cancelable
            self.error = error
            self.start_time = start_time
            self.end_time = end_time
            self.user = user
            VapiStruct.__init__(self)

    Task._set_binding_type(type.StructType(
        'com.vmware.vcenter.deployment.task', {
            'progress': type.OptionalType(type.ReferenceType('com.vmware.cis.task_client', 'Progress')),
            'result': type.OptionalType(type.ReferenceType('com.vmware.vcenter.deployment_client', 'Notifications')),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'service': type.IdType(resource_types='com.vmware.vapi.service'),
            'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
            'parent': type.OptionalType(type.IdType()),
            'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
            'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
            'cancelable': type.BooleanType(),
            'error': type.OptionalType(type.AnyErrorType()),
            'start_time': type.OptionalType(type.DateTimeType()),
            'end_time': type.OptionalType(type.DateTimeType()),
            'user': type.OptionalType(type.StringType()),
        },
        Task,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Deployment.Info`` class contains attributes to describe the state of
        the appliance. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'status',
                {
                    'RUNNING' : [('progress', True), ('start_time', True)],
                    'BLOCKED' : [('progress', True), ('start_time', True)],
                    'SUCCEEDED' : [('progress', True), ('start_time', True), ('end_time', True)],
                    'FAILED' : [('progress', True), ('error', False), ('start_time', True), ('end_time', True)],
                    'PENDING' : [],
                }
            ),
        ]



        def __init__(self,
                     state=None,
                     progress=None,
                     subtask_order=None,
                     subtasks=None,
                     description=None,
                     service=None,
                     operation=None,
                     parent=None,
                     target=None,
                     status=None,
                     cancelable=None,
                     error=None,
                     start_time=None,
                     end_time=None,
                     user=None,
                    ):
            """
            :type  state: :class:`com.vmware.vcenter.deployment_client.ApplianceState`
            :param state: State of the vCenter Server Appliance. This attribute was added in
                vSphere API 6.7
            :type  progress: :class:`com.vmware.cis.task_client.Progress`
            :param progress: The progress info of the current appliance status. This attribute
                was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``#status`` is one of
                :attr:`com.vmware.cis.task_client.Status.RUNNING`,
                :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  subtask_order: :class:`list` of :class:`str` or ``None``
            :param subtask_order: The ordered list of subtasks for this deployment operation. This
                attribute was added in vSphere API 6.7
                Only :class:`set` when the appliance state is RUNNING_IN_PROGRESS,
                FAILED, CANCELLED and SUCCEEDED.
            :type  subtasks: (:class:`dict` of :class:`str` and :class:`Deployment.Task`) or ``None``
            :param subtasks: The map of the deployment subtasks and their status infomation.
                This attribute was added in vSphere API 6.7
                Only :class:`set` when the appliance state is RUNNING_IN_PROGRESS,
                FAILED, CANCELLED and SUCCEEDED.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the operation associated with the task.
            :type  service: :class:`str`
            :param service: Name of the service containing the operation.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.service``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.service``.
            :type  operation: :class:`str`
            :param operation: Name of the operation associated with the task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.operation``.
            :type  parent: :class:`str` or ``None``
            :param parent: Parent of the current task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.task``. When methods return a value of this class
                as a return value, the attribute will be an identifier for the
                resource type: ``com.vmware.cis.task``.
                This attribute will be None if the task has no parent.
            :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
            :param target: Identifier of the target created by the operation or an existing
                one the operation performed on.
                This attribute will be None if the operation has no target or
                multiple targets.
            :type  status: :class:`com.vmware.cis.task_client.Status`
            :param status: Status of the operation associated with the task.
            :type  cancelable: :class:`bool`
            :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
                value may change as the operation progresses.
            :type  error: :class:`Exception` or ``None``
            :param error: Description of the error if the operation status is "FAILED".
                If None the description of why the operation failed will be
                included in the result of the operation (see
                :attr:`com.vmware.cis.task_client.Info.result`).
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the operation is started.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.RUNNING`,
                :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the operation is completed.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  user: :class:`str` or ``None``
            :param user: Name of the user who performed the operation.
                This attribute will be None if the operation is performed by the
                system.
            """
            self.state = state
            self.progress = progress
            self.subtask_order = subtask_order
            self.subtasks = subtasks
            self.description = description
            self.service = service
            self.operation = operation
            self.parent = parent
            self.target = target
            self.status = status
            self.cancelable = cancelable
            self.error = error
            self.start_time = start_time
            self.end_time = end_time
            self.user = user
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.deployment.info', {
            'state': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ApplianceState'),
            'progress': type.OptionalType(type.ReferenceType('com.vmware.cis.task_client', 'Progress')),
            'subtask_order': type.OptionalType(type.ListType(type.StringType())),
            'subtasks': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'Deployment.Task'))),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'service': type.IdType(resource_types='com.vmware.vapi.service'),
            'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
            'parent': type.OptionalType(type.IdType()),
            'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
            'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
            'cancelable': type.BooleanType(),
            'error': type.OptionalType(type.AnyErrorType()),
            'start_time': type.OptionalType(type.DateTimeType()),
            'end_time': type.OptionalType(type.DateTimeType()),
            'user': type.OptionalType(type.StringType()),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Get the current status of the appliance deployment. This method was
        added in vSphere API 6.7


        :rtype: :class:`Deployment.Info`
        :return: Info structure containing the status information about the
            appliance.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if appliance state cannot be determined.
        """
        return self._invoke('get', None)

    def rollback(self):
        """
        Rollback a failed appliance so it can be configured once again. This
        method was added in vSphere API 6.7


        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the appliance is not in FAILED state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        """
        return self._invoke('rollback', None)
class _ClusterStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Cluster.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/cluster',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'cluster': type.IdType(resource_types='ClusterComputeResource'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/cluster/{cluster}',
            path_variables={
                'cluster': 'cluster',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Cluster.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Cluster.Info'),
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
            self, iface_name='com.vmware.vcenter.cluster',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DatacenterStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Datacenter.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/datacenter',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'datacenter': type.IdType(resource_types='Datacenter'),
            'force': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
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
            url_template='/vcenter/datacenter/{datacenter}',
            path_variables={
                'datacenter': 'datacenter',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Datacenter.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/datacenter',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'datacenter': type.IdType(resource_types='Datacenter'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/datacenter/{datacenter}',
            path_variables={
                'datacenter': 'datacenter',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='Datacenter'),
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Datacenter.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Datacenter.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.datacenter',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DatastoreStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'datastore': type.IdType(resource_types='Datastore'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/datastore/{datastore}',
            path_variables={
                'datastore': 'datastore',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Datastore.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/datastore',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Datastore.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Datastore.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.datastore',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _FolderStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Folder.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/folder',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Folder.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.folder',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _HostStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Host.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/host',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInUse'),
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
            url_template='/vcenter/host/{host}',
            path_variables={
                'host': 'host',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Host.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/host',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for connect operation
        connect_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        connect_error_dict = {
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/host/{host}/connect',
            path_variables={
                'host': 'host',
            },
            query_parameters={
            }
        )

        # properties for disconnect operation
        disconnect_input_type = type.StructType('operation-input', {
            'host': type.IdType(resource_types='HostSystem'),
        })
        disconnect_error_dict = {
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/host/{host}/disconnect',
            path_variables={
                'host': 'host',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='HostSystem'),
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Host.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
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
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
            'connect': connect_rest_metadata,
            'disconnect': disconnect_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.host',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NetworkStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Network.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/network',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Network.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.network',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ResourcePoolStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'resource_pool': type.IdType(resource_types='ResourcePool'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/vcenter/resource-pool/{resource-pool}',
            path_variables={
                'resource_pool': 'resource-pool',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'ResourcePool.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/resource-pool',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ResourcePool.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'ResourcePool.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.resource_pool',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _VMStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'VM.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
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
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm',
            path_variables={
            },
            query_parameters={
            }
        )

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
            url_template='/vcenter/vm/{vm}',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
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
            url_template='/vcenter/vm/{vm}',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'VM.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
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
            url_template='/vcenter/vm',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='VirtualMachine'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'VM.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
                'output_type': type.ListType(type.ReferenceType(__name__, 'VM.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.VM',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DeploymentStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/deployment',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for rollback operation
        rollback_input_type = type.StructType('operation-input', {})
        rollback_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        rollback_input_value_validator_list = [
        ]
        rollback_output_validator_list = [
        ]
        rollback_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/deployment?action=rollback',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Deployment.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'rollback': {
                'input_type': rollback_input_type,
                'output_type': type.VoidType(),
                'errors': rollback_error_dict,
                'input_value_validator_list': rollback_input_value_validator_list,
                'output_validator_list': rollback_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'rollback': rollback_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.deployment',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Cluster': Cluster,
        'Datacenter': Datacenter,
        'Datastore': Datastore,
        'Folder': Folder,
        'Host': Host,
        'Network': Network,
        'ResourcePool': ResourcePool,
        'VM': VM,
        'Deployment': Deployment,
        'vm': 'com.vmware.vcenter.vm_client.StubFactory',
        'datastore': 'com.vmware.vcenter.datastore_client.StubFactory',
        'storage': 'com.vmware.vcenter.storage_client.StubFactory',
        'deployment': 'com.vmware.vcenter.deployment_client.StubFactory',
        'services': 'com.vmware.vcenter.services_client.StubFactory',
        'system_config': 'com.vmware.vcenter.system_config_client.StubFactory',
    }

