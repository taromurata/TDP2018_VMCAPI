# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.privilege.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.privilege_client`` module provides classes that
expose privilege information for operation elements across all the service
elements. 

An entity has a unique identifier and a resource type. An entity can either be
present in one of the parameter elements or if a parameter is a structure
element, it could also be present in one of the field elements. 

Privileges can be assigned to either operation elements or entities used in the
operation element. A list of privileges can also be applied on a package
element. This list of privileges would be used as a default for all the
operation elements and the entities that do not have any defined privileges.

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
    The ``ComponentData`` class contains the privilege information of the
    component along with its fingerprint.

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
        :param info: Privilege information of the component. This includes information
            about all the modules in the component.
        :type  fingerprint: :class:`str`
        :param fingerprint: Fingerprint of the metadata of the component. 
            
            Privilege information could change when there is an infrastructure
            update. Since the data present in :attr:`ComponentData.info` could
            be quite large, ``fingerprint`` provides a convenient way to check
            if the data for a particular component is updated. 
            
            You should store the fingerprint associated with a component. After
            an update, by invoking the :func:`Component.fingerprint` method,
            you can retrieve the new fingerprint for the component. If the new
            fingerprint and the previously stored fingerprint do not match,
            clients can then use the :func:`Component.get` to retrieve the new
            privilege information for the component.
        """
        self.info = info
        self.fingerprint = fingerprint
        VapiStruct.__init__(self)

ComponentData._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.privilege.component_data', {
        'info': type.ReferenceType(__name__, 'ComponentInfo'),
        'fingerprint': type.StringType(),
    },
    ComponentData,
    False,
    None))



class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class contains the privilege information of a
    component element. 
    
    For an explanation of privilege information contained within component
    elements, see :class:`Component`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 packages=None,
                ):
        """
        :type  packages: :class:`dict` of :class:`str` and :class:`PackageInfo`
        :param packages: Privilege information of all the package elements. The key in the
            :class:`dict` is the identifier of the package element and the
            value in the :class:`dict` is the privilege information for the
            package element. 
            
            For an explanation of privilege information containment within
            package elements, see :class:`Package`.
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
    'com.vmware.vapi.metadata.privilege.component_info', {
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'PackageInfo')),
    },
    ComponentInfo,
    False,
    None))



class OperationInfo(VapiStruct):
    """
    The ``OperationInfo`` class contains privilege information of an operation
    element. 
    
    For an explanation of containment within operation elements, see
    :class:`com.vmware.vapi.metadata.privilege.service_client.Operation`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 privileges=None,
                 privilege_info=None,
                ):
        """
        :type  privileges: :class:`list` of :class:`str`
        :param privileges: List of all privileges assigned to the operation element.
        :type  privilege_info: :class:`list` of :class:`PrivilegeInfo`
        :param privilege_info: Privilege information of all the parameter elements of the
            operation element. For an explanation of containment of privilege
            information within parameter elements, see :class:`PrivilegeInfo`.
        """
        self.privileges = privileges
        self.privilege_info = privilege_info
        VapiStruct.__init__(self)

OperationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.privilege.operation_info', {
        'privileges': type.ListType(type.StringType()),
        'privilege_info': type.ListType(type.ReferenceType(__name__, 'PrivilegeInfo')),
    },
    OperationInfo,
    False,
    None))



class PackageInfo(VapiStruct):
    """
    The ``PackageInfo`` class contains the privilege information of a package
    element. 
    
    For an explanation of privilege information contained within package
    elements, see :class:`Package`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 privileges=None,
                 services=None,
                ):
        """
        :type  privileges: :class:`list` of :class:`str`
        :param privileges: List of default privileges to be used for all the operations
            present in this package. If a particular operation element has no
            explicit privileges defined in the privilege definition file, these
            privileges are used for enforcing authorization.
        :type  services: :class:`dict` of :class:`str` and :class:`ServiceInfo`
        :param services: Information about all service elements contained in this package
            element that contain privilege information. The key in the
            :class:`dict` is the identifier of the service element and the
            value in the :class:`dict` is the privilege information for the
            service element. For an explanation of privilege information
            containment within service elements, see :class:`Service`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.service``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        """
        self.privileges = privileges
        self.services = services
        VapiStruct.__init__(self)

PackageInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.privilege.package_info', {
        'privileges': type.ListType(type.StringType()),
        'services': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ServiceInfo')),
    },
    PackageInfo,
    False,
    None))



class PrivilegeInfo(VapiStruct):
    """
    The ``PrivilegeInfo`` class contains the privilege information for a
    parameter element in an operation element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 property_path=None,
                 privileges=None,
                ):
        """
        :type  property_path: :class:`str`
        :param property_path: The ``propertyPath`` points to an entity that is used in the
            operation element. An entity can either be present in one of the
            parameter elements or if a parameter is a structure element, it
            could also be present in one of the field elements. 
            
            If the privilege is assigned to an entity used in the parameter,
            ``propertyPath`` will just contain the name of the parameter field.
            If the privilege is assigned to an entity in one of the field
            elements of a parameter element that is a structure element, then
            ``propertyPath`` will contain a path to the field element starting
            from the parameter name.
        :type  privileges: :class:`list` of :class:`str`
        :param privileges: List of privileges assigned to the entity that is being referred by
            :attr:`PrivilegeInfo.property_path`.
        """
        self.property_path = property_path
        self.privileges = privileges
        VapiStruct.__init__(self)

PrivilegeInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.privilege.privilege_info', {
        'property_path': type.StringType(),
        'privileges': type.ListType(type.StringType()),
    },
    PrivilegeInfo,
    False,
    None))



class ServiceInfo(VapiStruct):
    """
    The ``ServiceInfo`` class contains privilege information of a service
    element. 
    
    For an explanation of privilege information contained within service
    elements, see :class:`Service`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 operations=None,
                ):
        """
        :type  operations: :class:`dict` of :class:`str` and :class:`OperationInfo`
        :param operations: Information about all operation elements contained in this service
            element that contain privilege information. The key in the
            :class:`dict` is the identifier of the operation element and the
            value in the :class:`dict` is the privilege information for the
            operation element. 
            
            For an explanation of containment of privilege information within
            operation elements, see
            :class:`com.vmware.vapi.metadata.privilege.service_client.Operation`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.operation``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        """
        self.operations = operations
        VapiStruct.__init__(self)

ServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.privilege.service_info', {
        'operations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'OperationInfo')),
    },
    ServiceInfo,
    False,
    None))



class Component(VapiInterface):
    """
    The ``Component`` class provides methods to retrieve privilege information
    of a component element. 
    
    A component element is said to contain privilege information if any one of
    package elements in it contains privilege information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.component"
    """
    Resource type for vAPI component.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComponentStub)


    def list(self):
        """
        Returns the identifiers for the component elements that have privilege
        information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the component elements that have
            privilege information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.component``.
        """
        return self._invoke('list', None)

    def get(self,
            component_id,
            ):
        """
        Retrieves privilege information about the component element
        corresponding to ``component_id``. 
        
        The :class:`ComponentData` contains the privilege information about the
        component element and its fingerprint. It contains information about
        all the package elements that belong to this component element.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`ComponentData`
        :return: The :class:`ComponentData` instance that corresponds to
            ``component_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` does not
            have any privilege information.
        """
        return self._invoke('get',
                            {
                            'component_id': component_id,
                            })

    def fingerprint(self,
                    component_id,
                    ):
        """
        Retrieves the fingerprint computed from the privilege metadata of the
        component element corresponding to ``component_id``. 
        
        The fingerprint provides clients an efficient way to check if the
        metadata for a particular component has been modified on the server.
        The client can do this by comparing the result of this operation with
        the fingerprint returned in the result of :func:`Component.get`.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`str`
        :return: The fingerprint computed from the privilege metadata of the
            component.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` does not
            have any privilege information.
        """
        return self._invoke('fingerprint',
                            {
                            'component_id': component_id,
                            })
class Package(VapiInterface):
    """
    The ``Package`` class provides methods to retrieve privilege information of
    a package element. 
    
    A package element is said to contain privilege information if there is a
    default privilege assigned to all service elements contained in the package
    element or if one of the operation elements contained in one of the service
    elements in this package element has privilege information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.package"
    """
    Resource type for package.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PackageStub)


    def list(self):
        """
        Returns the identifiers for the package elements that have privilege
        information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the package elements that have
            privilege information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.package``.
        """
        return self._invoke('list', None)

    def get(self,
            package_id,
            ):
        """
        Retrieves privilege information about the package element corresponding
        to ``package_id``.

        :type  package_id: :class:`str`
        :param package_id: Identifier of the package element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        :rtype: :class:`PackageInfo`
        :return: The :class:`PackageInfo` instance that corresponds to
            ``package_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the package element associated with ``package_id`` does not have
            any privilege information.
        """
        return self._invoke('get',
                            {
                            'package_id': package_id,
                            })
class Service(VapiInterface):
    """
    The ``Service`` class provides methods to retrieve privilege information of
    a service element. 
    
    A service element is said to contain privilege information if one of the
    operation elements contained in this service element has privilege
    information.
    """
    RESOURCE_TYPE = "com.vmware.vapi.service"
    """
    Resource type for service.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)


    def list(self):
        """
        Returns the identifiers for the service elements that have privilege
        information.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the service elements that have
            privilege information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)

    def get(self,
            service_id,
            ):
        """
        Retrieves privilege information about the service element corresponding
        to ``service_id``.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`ServiceInfo`
        :return: The :class:`ServiceInfo` instance that corresponds to
            ``service_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not have
            any privilege information.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            })
class Source(VapiInterface):
    """
    The ``Source`` class provides methods to manage the sources of privilege
    metadata information. 
    
    The interface definition language infrastructure provides tools to generate
    various kinds of metadata in JSON format from the interface definition
    files and additional properties files. One of the generated files contains
    privilege information. The generated file can be registered as a source of
    metadata. 
    
    The privilege file contains all the data present in the interface
    definition files. Each privilege file contains data about one component
    element. When a privilege file is added as a source, each source
    contributes only one component element's metadata. 
    
    Privilege metadata can also be discovered from a remote server that
    supports the privilege metadata classes (see
    :mod:`com.vmware.vapi.metadata.privilege_client`). Since multiple
    components can be registered with a single metadata server, when a remote
    server is registered as a source, that source can contribute more than one
    component.
    """
    RESOURCE_TYPE = "com.vmware.vapi.metadata.privilege.source"
    """
    Resource type for metadata source.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SourceStub)

    class Info(VapiStruct):
        """
        The ``Source.Info`` class contains the metadata source information.

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
            :param filepath: Absolute file path of the privilege metadata file that has the
                privilege information about one component element. The ``filePath``
                is the path to the file in the server's filesystem.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information for the remote server. This must be in the
                format http(s)://IP:port/namespace. 
                
                The remote server must support the classes in the
                :mod:`com.vmware.vapi.metadata.privilege_client` module. It must
                expose privilege information of one or more components.
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
        'com.vmware.vapi.metadata.privilege.source.info', {
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
        The ``Source.CreateSpec`` class contains the registration information of a
        privilege source.

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
        'com.vmware.vapi.metadata.privilege.source.create_spec', {
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
        Creates a new metadata source. Once the server validates the
        registration information of the metadata source, the privilege metadata
        is retrieved from the source. This populates elements in all the
        classes defined in :mod:`com.vmware.vapi.metadata.privilege_client`
        module.

        :type  source_id: :class:`str`
        :param source_id: metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
        :type  spec: :class:`Source.CreateSpec`
        :param spec: create specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the metadata source identifier is already registered with the
            infrastructure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the type of the source specified in null is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the file specified in null is not a valid JSON file or if the
            format of the privilege metadata in the JSON file is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the URI specified in null is unreachable or if there is a
            transport protocol or message protocol mismatch between the client
            and the server or if the remote server do not have classes present
            in :mod:`com.vmware.vapi.metadata.privilege_client` module.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the file specified in null does not exist.
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
        Deletes an existing privilege metadata source from the infrastructure.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('delete',
                            {
                            'source_id': source_id,
                            })

    def get(self,
            source_id,
            ):
        """
        Retrieves information about the metadata source corresponding to
        ``source_id``.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
        :rtype: :class:`Source.Info`
        :return: The :class:`Source.Info` instance that corresponds to ``source_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('get',
                            {
                            'source_id': source_id,
                            })

    def list(self):
        """
        Returns the identifiers of the metadata sources currently registered
        with the infrastructure.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for metadata sources currently registered.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
        """
        return self._invoke('list', None)

    def reload(self,
               source_id=None,
               ):
        """
        Reloads the privilege metadata from all the metadata sources or of a
        particular metadata source if ``source_id`` is specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
            If unspecified, all the metadata sources are reloaded.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('reload',
                            {
                            'source_id': source_id,
                            })

    def fingerprint(self,
                    source_id=None,
                    ):
        """
        Returns the aggregate fingerprint of metadata from all the metadata
        sources or from a particular metadata source if ``source_id`` is
        specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.privilege.source``.
            If unspecified, the fingerprint of all the metadata sources is
            returned.
        :rtype: :class:`str`
        :return: Aggregate fingerprint of all the metadata sources or of a
            particular metadata source.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
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
            self, iface_name='com.vmware.vapi.metadata.privilege.component',
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
            self, iface_name='com.vmware.vapi.metadata.privilege.package',
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
            self, iface_name='com.vmware.vapi.metadata.privilege.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SourceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.privilege.source'),
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
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.privilege.source'),
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
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.privilege.source'),
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
            self, iface_name='com.vmware.vapi.metadata.privilege.source',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Component': Component,
        'Package': Package,
        'Service': Service,
        'Source': Source,
        'service': 'com.vmware.vapi.metadata.privilege.service_client.StubFactory',
    }

