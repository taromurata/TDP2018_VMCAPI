# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.routing.
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


class ComponentData(VapiStruct):
    """
    Routing information of the vAPI component along with its checksum

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 info=None,
                 fingerprint=None,
                ):
        """
        :type  info: :class:`ComponentInfo`
        :param info: Routing information of the vAPI component
        :type  fingerprint: :class:`str`
        :param fingerprint: Fingerprint of metadata of a vAPI component
        """
        self.info = info
        self.fingerprint = fingerprint
        VapiStruct.__init__(self)

ComponentData._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.component_data', {
        'info': type.ReferenceType(__name__, 'ComponentInfo'),
        'fingerprint': type.StringType(),
    },
    ComponentData,
    False,
    None))



class ComponentInfo(VapiStruct):
    """
    Information about a vAPI component that contains routing information For an
    explanation of routing information within components, see
    :class:`Component`

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 packages=None,
                ):
        """
        :type  packages: :class:`dict` of :class:`str` and :class:`PackageInfo`
        :param packages: Routing information of all the vAPI packages. The key in the map is
            the ID of the package and the value in the map is the routing
            information for the package For an explanation of routing
            information within packages, see :class:`Package`
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.package``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        """
        self.packages = packages
        VapiStruct.__init__(self)

ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.component_info', {
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'PackageInfo')),
    },
    ComponentInfo,
    False,
    None))



class OperationInfo(VapiStruct):
    """
    Information about a vAPI operation that contains routing information. For
    an explanation of containment within operations, see null

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 routing_info=None,
                ):
        """
        :type  routing_info: :class:`RoutingInfo`
        :param routing_info: The routing information assigned for this operation. For an
            explanation of routing information, see :class:`RoutingInfo`
        """
        self.routing_info = routing_info
        VapiStruct.__init__(self)

OperationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.operation_info', {
        'routing_info': type.ReferenceType(__name__, 'RoutingInfo'),
    },
    OperationInfo,
    False,
    None))



class PackageInfo(VapiStruct):
    """
    Information about a vAPI package containing routing information. 
    
    For an explanation of routing information within packages, see
    :class:`Package`

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 routing_info=None,
                 services=None,
                ):
        """
        :type  routing_info: :class:`RoutingInfo`
        :param routing_info: The routing information to be used for all the operations present
            in this package. If a particular operation has no explicit routing
            information defined in the routing definition file, this routing
            info will be used for enforcing routing.
        :type  services: :class:`dict` of :class:`str` and :class:`ServiceInfo`
        :param services: Information about all services in this package that contain routing
            information. The key in the map is the ID of the service and the
            value in the map is the routing information for the service For an
            explanation of routing information within service, see
            :class:`Service`
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.service``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        """
        self.routing_info = routing_info
        self.services = services
        VapiStruct.__init__(self)

PackageInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.package_info', {
        'routing_info': type.ReferenceType(__name__, 'RoutingInfo'),
        'services': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ServiceInfo')),
    },
    PackageInfo,
    False,
    None))



class RoutingInfo(VapiStruct):
    """
    Routing information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 routing_path=None,
                 routing_strategy=None,
                 operation_hints=None,
                 id_types=None,
                ):
        """
        :type  routing_path: :class:`str`
        :param routing_path: The initial version of the routing info allowed routing by single
            parameter. Clients requested allowing them to place more than one
            parameters so that the routing is performed by the first non-null
            argument in the list. To achieve that we have added method
            com.vmware.vapi.metadata.RoutingInfo#getRoutingPaths() which should
            be preferred over
            com.vmware.vapi.metadata.RoutingInfo#getRoutingPath() which is
            deprecated. The deprecated method will return string representation
            of the comma-separated list of ids, while the
            com.vmware.vapi.metadata.RoutingInfo#getRoutingPaths() will return
            instance of ``java.util.List<String>`` containing the ids.
        :type  routing_strategy: :class:`str`
        :param routing_strategy: The routingStrategy is the actual strategy, based on which will be
            performed the routing. If the routingStrategy is IDROUTE, in
            :attr:`RoutingInfo.routing_path` must be assigned the id for the
            routing. There are also default strategies like IDFIRSTROUTE, LOCAL
            for which there is no need to specify routingPath. The name of
            these strategies is clear about where we should look for an ID to
            route, or if we need ID at all.
        :type  operation_hints: :class:`list` of :class:`str`
        :param operation_hints: This is comma-separated list of hints from the input ini file. Here
            the user must mention the type of the invoked method, e.g.
            HINTS(create) or HINTS(delete). In the future we expect this field
            to contain other hints also e.g. HINTS(create,lazy).
        :type  id_types: :class:`dict` of :class:`str` and :class:`str`
        :param id_types: This is map of specifically predefined resource types in the
            routing metadata. For example id types that do not require storage
            in the Inventory Service. Those type of objects are called
            'positioned' - it is well known in advance where those objects will
            be routed, because their ids contain VC server guid. Example:
            Content Library Sessions are considered transient objects that do
            not need to be persisted in the IS. Routing ini file must contain
            section: [types] com.vmware.content.DownloadSession=positioned The
            map therefore will contain: {{"com.vmware.content.DownloadSession",
            "positioned"}} Note: This should not be final solution. To avoid
            duplication, currently this map will be stored only in one
            RoutingInfo object across the whole ProductModel. In the future, it
            might be moved to a common place as ComponentInfo, for example.
        """
        self.routing_path = routing_path
        self.routing_strategy = routing_strategy
        self.operation_hints = operation_hints
        self.id_types = id_types
        VapiStruct.__init__(self)

RoutingInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.routing_info', {
        'routing_path': type.StringType(),
        'routing_strategy': type.StringType(),
        'operation_hints': type.ListType(type.StringType()),
        'id_types': type.MapType(type.StringType(), type.StringType()),
    },
    RoutingInfo,
    False,
    None))



class ServiceInfo(VapiStruct):
    """
    Information about a vAPI service that has routing information A service is
    said to contain routing information if any of its operations have routing
    information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 routing_info=None,
                 operations=None,
                ):
        """
        :type  routing_info: :class:`RoutingInfo`
        :param routing_info: The routing information to be used for all the operations present
            in this service. If a particular operation has no explicit routing
            information defined in the routing definition file, this routing
            info will be used for enforcing routing.
        :type  operations: :class:`dict` of :class:`str` and :class:`OperationInfo`
        :param operations: Information about all operations in this service that contain
            routing Information. The key in the map is the ID of the operation
            and the value in the map is the routing information for this
            operation. 
            
            For an explanation of routing information within operations, see
            null
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.operation``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        """
        self.routing_info = routing_info
        self.operations = operations
        VapiStruct.__init__(self)

ServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.routing.service_info', {
        'routing_info': type.ReferenceType(__name__, 'RoutingInfo'),
        'operations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'OperationInfo')),
    },
    ServiceInfo,
    False,
    None))



class Component(VapiInterface):
    """
    Operations to retrieve information about the routing information in a vAPI
    component. A Component is said to contain routing information if any of its
    packages, services or methods contain routing information
    """
    RESOURCE_TYPE = "com.vmware.vapi.component"
    """
    Resource type for vAPI Component.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComponentStub)


    def list(self):
        """
        List all the vAPI components that contain operations which have routing
        information.


        :rtype: :class:`list` of :class:`str`
        :return: list of fully qualified component names
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.component``.
        """
        return self._invoke('list', None)

    def get(self,
            component_id,
            ):
        """
        Get the routing information for a vAPI component

        :type  component_id: :class:`str`
        :param component_id:  fully qualified component name
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`ComponentData`
        :return: routing information for the vAPI component
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the component name does not exist
        """
        return self._invoke('get',
                            {
                            'component_id': component_id,
                            })

    def fingerprint(self,
                    component_id,
                    ):
        """
        Checksum of all routing metadata for a vAPI component on the server

        :type  component_id: :class:`str`
        :param component_id:  fully qualified component name
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`str`
        :return: checksum of routing metadata for a vAPI component
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the component name does not exist
        """
        return self._invoke('fingerprint',
                            {
                            'component_id': component_id,
                            })
class Package(VapiInterface):
    """
    Operations to retrieve information about routing information in a vAPI
    package A Package is said to contain routing information if there is a
    default RoutingInfo assigned to all operations within a package or if one
    of the operations within this package has explicit routing information
    """
    RESOURCE_TYPE = "com.vmware.vapi.package"
    """
    Resource type for vAPI package.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PackageStub)


    def list(self):
        """
        List of all vAPI packages that have routing information


        :rtype: :class:`list` of :class:`str`
        :return: list of fully qualified package names
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.package``.
        """
        return self._invoke('list', None)

    def get(self,
            package_id,
            ):
        """
        Get the routing information for a vAPI package

        :type  package_id: :class:`str`
        :param package_id: fully qualified package name
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        :rtype: :class:`PackageInfo`
        :return: routing information for the vAPI package
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the package name does not exist
        """
        return self._invoke('get',
                            {
                            'package_id': package_id,
                            })
class Service(VapiInterface):
    """
    Operations to retrieve information about routing information of a vAPI
    service
    """
    RESOURCE_TYPE = "com.vmware.vapi.service"
    """
    Resource type for vAPI Service.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)


    def list(self):
        """
        Get list of all vAPI services that have operations with routing
        information


        :rtype: :class:`list` of :class:`str`
        :return: list of fully qualified service names
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)

    def get(self,
            service_id,
            ):
        """
        Get the routing information for a vAPI service

        :type  service_id: :class:`str`
        :param service_id: fully qualified service name
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`ServiceInfo`
        :return: identifier information for the vAPI service
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the service name does not exist
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            })
class Source(VapiInterface):
    """
    Operations to manage the metadata sources for routing information
    """
    RESOURCE_TYPE = "com.vmware.vapi.metadata.source"
    """
    Resource type for vAPI metadata source.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SourceStub)

    class Info(VapiStruct):
        """
        Metadata source info.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('filepath', True)],
                    'REMOTE' : [('address', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     type=None,
                     filepath=None,
                     address=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: Description of the source.
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: Type of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the file that has the metadata information.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: URI of the remote vAPI endpoint. This should be of the format
                http(s):IP:port/namespace.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.routing.source.info', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        Metadata source create spec.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('filepath', True)],
                    'REMOTE' : [('address', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     type=None,
                     filepath=None,
                     address=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: English language human readable description of the source.
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: Type of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the metamodel metadata file that has the
                metamodel information about one component element.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information of the remote server. This should be of the
                format http(s)://IP:port/namespace. 
                
                The remote server should contain the classes in
                :mod:`com.vmware.vapi.metadata.metamodel_client` module. It could
                expose metamodel information of one or more components.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.routing.source.create_spec', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        CreateSpec,
        False,
        None))



    def create(self,
               source_id,
               spec,
               ):
        """
        Create a new metadata source.

        :type  source_id: :class:`str`
        :param source_id:  metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :type  spec: :class:`Source.CreateSpec`
        :param spec:  create specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
             If the metadata source identifier is already present.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If type of the source specified in \\\\@{link CreateSpec#type} is
            invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the file specified in \\\\@{link CreateSpec#filepath} is not a
            valid json file.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the URI specified in \\\\@{link CreateSpec#address} is
            unreachable or not a vAPI compatible server.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the file specified in \\\\@{link CreateSpec#filepath} does not
            exist.
        """
        return self._invoke('create',
                            {
                            'source_id': source_id,
                            'spec': spec,
                            })

    def delete(self,
               source_id,
               ):
        """
        Delete a metadata source.

        :type  source_id: :class:`str`
        :param source_id:  Metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the metadata source identifier is not found.
        """
        return self._invoke('delete',
                            {
                            'source_id': source_id,
                            })

    def get(self,
            source_id,
            ):
        """
        Get the details about a metadata source.

        :type  source_id: :class:`str`
        :param source_id:  Metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :rtype: :class:`Source.Info`
        :return: Metadata source info.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the metadata source identifier is not found.
        """
        return self._invoke('get',
                            {
                            'source_id': source_id,
                            })

    def list(self):
        """
        List all the metadata sources.


        :rtype: :class:`list` of :class:`str`
        :return: List of all metadata sources.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.metadata.source``.
        """
        return self._invoke('list', None)

    def reload(self,
               source_id=None,
               ):
        """
        Reload metadata from all the sources or of a particular source.

        :type  source_id: :class:`str` or ``None``
        :param source_id:  Metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
             If unspecified, all the sources are reloaded
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the metadata source identifier is not found.
        """
        return self._invoke('reload',
                            {
                            'source_id': source_id,
                            })

    def fingerprint(self,
                    source_id=None,
                    ):
        """
        Returns the fingerprint of all the sources or of a particular source.

        :type  source_id: :class:`str` or ``None``
        :param source_id:  Metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
             If unspecified, fingerprint of all the sources is returned
        :rtype: :class:`str`
        :return: fingerprint of all the sources or of a particular source.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             If the metadata source identifier is not found.
        """
        return self._invoke('fingerprint',
                            {
                            'source_id': source_id,
                            })
class _ComponentStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ComponentData'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.routing.component',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PackageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'package_id': type.IdType(resource_types='com.vmware.vapi.package'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'PackageInfo'),
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
            self, iface_name='com.vmware.vapi.metadata.routing.package',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ServiceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ServiceInfo'),
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
            self, iface_name='com.vmware.vapi.metadata.routing.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SourceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
            'spec': type.ReferenceType(__name__, 'Source.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for reload operation
        reload_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        reload_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reload_input_value_validator_list = [
        ]
        reload_output_validator_list = [
        ]
        reload_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Source.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reload': {
                'input_type': reload_input_type,
                'output_type': type.VoidType(),
                'errors': reload_error_dict,
                'input_value_validator_list': reload_input_value_validator_list,
                'output_validator_list': reload_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'reload': reload_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.routing.source',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Component': Component,
        'Package': Package,
        'Service': Service,
        'Source': Source,
        'service': 'com.vmware.vapi.metadata.routing.service_client.StubFactory',
    }

