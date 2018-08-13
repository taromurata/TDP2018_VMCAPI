# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.metamodel.service.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.metamodel.service_client`` module provides
classes to retrieve metamodel information about the elements contained in a
service element.

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


class Hidden(VapiInterface):
    """
    The ``Hidden`` class provides methods to retrieve the list of classes that
    are hidden and should not be exposed in various presentation layers of API
    infrastructure.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _HiddenStub)


    def list(self):
        """
        Returns the class identifiers that should be hidden.


        :rtype: :class:`list` of :class:`str`
        :return: The list of class identifiers that should be hidden.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)
class Operation(VapiInterface):
    """
    The ``Operation`` class provides methods to retrieve metamodel information
    of an operation element in the interface definition language.
    """
    RESOURCE_TYPE = "com.vmware.vapi.operation"
    """
    Resource type for operation element.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OperationStub)


    def list(self,
             service_id,
             ):
        """
        Returns the identifiers for the operation elements that are defined in
        the scope of ``service_id``.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the operation elements that are defined
            in the scope of ``service_id``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.operation``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not
            exist in any of the package elements.
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
        Retrieves the metamodel information about an operation element
        corresponding to ``operation_id`` contained in the service element
        corresponding to ``service_id``.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        :rtype: :class:`com.vmware.vapi.metadata.metamodel_client.OperationInfo`
        :return: The
            :class:`com.vmware.vapi.metadata.metamodel_client.OperationInfo`
            instance that corresponds to ``operation_id`` defined in scope
            ``service_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not
            exist in any of the package elements.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the operation element associated with ``operation_id`` does not
            exist in the service element.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            'operation_id': operation_id,
                            })
class _HiddenStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
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
            self, iface_name='com.vmware.vapi.metadata.metamodel.service.hidden',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

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
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vapi.metadata.metamodel_client', 'OperationInfo'),
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
            self, iface_name='com.vmware.vapi.metadata.metamodel.service.operation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Hidden': Hidden,
        'Operation': Operation,
    }

