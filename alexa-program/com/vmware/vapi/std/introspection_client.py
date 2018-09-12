# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.introspection.
#---------------------------------------------------------------------------

"""
The :mod:`com.vmware.vapi.std.introspection_client` module provides classes
that expose basic information about the vAPI classes registered with a vAPI
provider.

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


class Operation(VapiInterface):
    """
    The :class:`Operation` service provides operations to retrieve information
    about the operations present in a vAPI service.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OperationStub)

    class DataDefinition(VapiStruct):
        """
        The :class:`Operation.DataDefinition` structure describes a vAPI data type.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'OPTIONAL' : [('element_definition', True)],
                    'LIST' : [('element_definition', True)],
                    'STRUCTURE' : [('name', True), ('fields', True)],
                    'STRUCTURE_REF' : [('name', True)],
                    'ERROR' : [('name', True), ('fields', True)],
                    'BINARY' : [],
                    'BOOLEAN' : [],
                    'DOUBLE' : [],
                    'DYNAMIC_STRUCTURE' : [],
                    'ANY_ERROR' : [],
                    'LONG' : [],
                    'OPAQUE' : [],
                    'SECRET' : [],
                    'STRING' : [],
                    'VOID' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     element_definition=None,
                     name=None,
                     fields=None,
                    ):
            """
            :type  type: :class:`Operation.DataDefinition.DataType`
            :param type: Data type of the value.
            :type  element_definition: :class:`Operation.DataDefinition`
            :param element_definition: Contains the element definition for generic data types like List
                and Optional.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of
                :attr:`Operation.DataDefinition.DataType.OPTIONAL` or
                :attr:`Operation.DataDefinition.DataType.LIST`.
            :type  name: :class:`str`
            :param name: Fully qualified name of the structure.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of
                :attr:`Operation.DataDefinition.DataType.STRUCTURE`,
                :attr:`Operation.DataDefinition.DataType.STRUCTURE_REF`, or
                :attr:`Operation.DataDefinition.DataType.ERROR`.
            :type  fields: :class:`dict` of :class:`str` and :class:`Operation.DataDefinition`
            :param fields: Fields of the structure type. The key of the map is the canonical
                name of the field and the value is the
                :class:`Operation.DataDefinition` for the field. The order of the
                structure fields defined in IDL is not maintained by the
                :class:`Operation` service.
                This attribute is optional and it is only relevant when the value
                of ``type`` is one of
                :attr:`Operation.DataDefinition.DataType.STRUCTURE` or
                :attr:`Operation.DataDefinition.DataType.ERROR`.
            """
            self.type = type
            self.element_definition = element_definition
            self.name = name
            self.fields = fields
            VapiStruct.__init__(self)

        class DataType(Enum):
            """
            The :class:`Operation.DataDefinition.DataType` enumeration provides values
            representing the data types supported by the vAPI infrastructure.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            BINARY = None
            """
            Indicates the value is a binary type.

            """
            BOOLEAN = None
            """
            Indicates the value is a boolean type. The possible values are True and
            False equivalent of the language used to invoke this operation.

            """
            DOUBLE = None
            """
            Indicates the value is a double type. It is a 64 bit floating point number.

            """
            DYNAMIC_STRUCTURE = None
            """
            Indicates the value is a dynamic structure. This means, any data of type
            :attr:`Operation.DataDefinition.DataType.STRUCTURE` can be used.

            """
            ERROR = None
            """
            Indicates the value is a specific error type.

            """
            ANY_ERROR = None
            """
            Indicates the value is arbitrary error type. This means, any data of type
            :attr:`Operation.DataDefinition.DataType.ERROR` can be used.

            """
            LIST = None
            """
            Indicates the value is a list data type. Any value of this type can have
            zero or more elements in the list.

            """
            LONG = None
            """
            Indicates the value is a long data type. It is a 64 bit signed integer
            number.

            """
            OPAQUE = None
            """
            Indicates the value is an opaque type. This means, data of any
            :class:`Operation.DataDefinition.DataType` can be used.

            """
            OPTIONAL = None
            """
            Indicates the value is an optional data type. Any value of this type can be
            null.

            """
            SECRET = None
            """
            Indicates the value is a secret data type. This is used for sensitive
            information. The server will not log any data of this type and if possible
            wipe the data from the memory after usage.

            """
            STRING = None
            """
            Indicates the value is a string data type. This is a unicode string.

            """
            STRUCTURE = None
            """
            Indicates the value is a structure data type. A structure has string
            identifier and a set of fields with corresponding values.

            """
            STRUCTURE_REF = None
            """
            Indicates the value is a structure reference. This is used to break
            circular dependencies in the type references. This just has a string
            identifier of the structure. Clients have to maintain a list of structures
            already visited and use that to resolve this reference.

            """
            VOID = None
            """
            Indicates the value is a void data type.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`DataType` instance.
                """
                Enum.__init__(string)

        DataType._set_values([
            DataType('BINARY'),
            DataType('BOOLEAN'),
            DataType('DOUBLE'),
            DataType('DYNAMIC_STRUCTURE'),
            DataType('ERROR'),
            DataType('ANY_ERROR'),
            DataType('LIST'),
            DataType('LONG'),
            DataType('OPAQUE'),
            DataType('OPTIONAL'),
            DataType('SECRET'),
            DataType('STRING'),
            DataType('STRUCTURE'),
            DataType('STRUCTURE_REF'),
            DataType('VOID'),
        ])
        DataType._set_binding_type(type.EnumType(
            'com.vmware.vapi.std.introspection.operation.data_definition.data_type',
            DataType))

    DataDefinition._set_binding_type(type.StructType(
        'com.vmware.vapi.std.introspection.operation.data_definition', {
            'type': type.ReferenceType(__name__, 'Operation.DataDefinition.DataType'),
            'element_definition': type.OptionalType(type.ReferenceType(__name__, 'Operation.DataDefinition')),
            'name': type.OptionalType(type.StringType()),
            'fields': type.OptionalType(type.MapType(type.StringType(), type.ReferenceType(__name__, 'Operation.DataDefinition'))),
        },
        DataDefinition,
        False,
        None))


    class Info(VapiStruct):
        """
        Information about a vAPI operation.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     input_definition=None,
                     output_definition=None,
                     error_definitions=None,
                    ):
            """
            :type  input_definition: :class:`Operation.DataDefinition`
            :param input_definition: :class:`Operation.DataDefinition` describing the operation input. 
                
                The :attr:`Operation.DataDefinition.type` of this field will be
                :attr:`Operation.DataDefinition.DataType.STRUCTURE`. The keys of
                :attr:`Operation.DataDefinition.fields` are the names of the
                operation parameters, and the values of
                :attr:`Operation.DataDefinition.fields` describe the type of the
                operation parameters.
            :type  output_definition: :class:`Operation.DataDefinition`
            :param output_definition: :class:`Operation.DataDefinition` describing the operation output.
            :type  error_definitions: :class:`list` of :class:`Operation.DataDefinition`
            :param error_definitions: List of :class:`Operation.DataDefinition` describing the errors
                that the operation might report. 
                
                The :attr:`Operation.DataDefinition.type` of every element in this
                list will be :attr:`Operation.DataDefinition.DataType.ERROR`.
            """
            self.input_definition = input_definition
            self.output_definition = output_definition
            self.error_definitions = error_definitions
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.std.introspection.operation.info', {
            'input_definition': type.ReferenceType(__name__, 'Operation.DataDefinition'),
            'output_definition': type.ReferenceType(__name__, 'Operation.DataDefinition'),
            'error_definitions': type.ListType(type.ReferenceType(__name__, 'Operation.DataDefinition')),
        },
        Info,
        False,
        None))



    def list(self,
             service_id,
             ):
        """
        Returns the set of operation identifiers for a given vAPI service.

        :type  service_id: :class:`str`
        :param service_id: service identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`set` of :class:`str`
        :return: set of operation identifiers for a given vAPI service.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.operation``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the service identifier does not exist.
        """
        return self._invoke('list',
                            {
                            'service_id': service_id,
                            })

    def get(self,
            service_id,
            operation_id,
            ):
        """
        Returns the :class:`Operation.Info` for a given vAPI operation.

        :type  service_id: :class:`str`
        :param service_id: service identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :type  operation_id: :class:`str`
        :param operation_id: operation identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        :rtype: :class:`Operation.Info`
        :return: :class:`Operation.Info` for a given vAPI operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the operation identifier does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the service identifier does not exist.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            'operation_id': operation_id,
                            })
class Provider(VapiInterface):
    """
    The :class:`Provider` service provides operations to retrieve information
    about a vAPI Provider. A provider is a container that exposes one or more
    vAPI services.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProviderStub)

    class Info(VapiStruct):
        """
        Information about a vAPI provider

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     checksum=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: Identifier of the provider
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.provider``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.provider``.
            :type  checksum: :class:`str`
            :param checksum: Checksum of the information present in the provider. 
                
                Clients can use this information to check if the service
                information has changed. When a new service is added or removed
                (or) one of the existing service information is modified, the value
                of the checksum changes. 
                
                 The information used to calculate the checksum includes: 
                
                * service identifiers
                * operation identifiers inside the service
                * input, output and error definitions of an operation
            """
            self.id = id
            self.checksum = checksum
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.std.introspection.provider.info', {
            'id': type.IdType(resource_types='com.vmware.vapi.provider'),
            'checksum': type.StringType(),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Returns a :class:`Provider.Info` describing the vAPI provider on which
        the operation is invoked


        :rtype: :class:`Provider.Info`
        :return: :class:`Provider.Info` describing the vAPI provider on which the
            operation is invoked
        """
        return self._invoke('get', None)
class Service(VapiInterface):
    """
    The :class:`Service` service provides operations to retrieve information
    about the services exposed by a vAPI provider. A provider is a container
    that exposes one or more vAPI services.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)

    class Info(VapiStruct):
        """
        Information about a vAPI service

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     operations=None,
                    ):
            """
            :type  operations: :class:`set` of :class:`str`
            :param operations: Set of identifiers of operations present in the service
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.vapi.operation``.
            """
            self.operations = operations
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.std.introspection.service.info', {
            'operations': type.SetType(type.IdType()),
        },
        Info,
        False,
        None))



    def list(self):
        """
        Returns the set of service identifiers.


        :rtype: :class:`set` of :class:`str`
        :return: set of service identifiers
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)

    def get(self,
            id,
            ):
        """
        Returns the :class:`Service.Info` for the specified service

        :type  id: :class:`str`
        :param id: service identifier
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`Service.Info`
        :return: :class:`Service.Info` for the specified service
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the service identifier does not exist
        """
        return self._invoke('get',
                            {
                            'id': id,
                            })
class _OperationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
            'operation_id': type.IdType(resource_types='com.vmware.vapi.operation'),
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
                'output_type': type.SetType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Operation.Info'),
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
            self, iface_name='com.vmware.vapi.std.introspection.operation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ProviderStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {}
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Provider.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.std.introspection.provider',
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
            'id': type.IdType(resource_types='com.vmware.vapi.service'),
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
                'output_type': type.SetType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Service.Info'),
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
            self, iface_name='com.vmware.vapi.std.introspection.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Operation': Operation,
        'Provider': Provider,
        'Service': Service,
    }

