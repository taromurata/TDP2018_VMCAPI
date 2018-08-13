# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.authentication.service.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.authentication.service_client`` module provides
classes to retrieve authentication information for operation elements.

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
    The ``Operation`` class provides methods to retrieve authentication
    information of an operation element. 
    
    An operation element is said to contain authentication information if
    authentication schemes are specified in the authentication definition file.
    """
    RESOURCE_TYPE = "com.vmware.vapi.operation"
    """
    Resource type for operation.

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
        Returns the identifiers for the operation elements contained in the
        service element corresponding to ``service_id`` that have
        authentication information.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`list` of :class:`str`
        :return: List of identifiers for the operation elements contained in the
            service element that have authentication information.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.operation``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not have
            any operation elements that have authentication information.
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
        Retrieves the authentication information about an operation element
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
        :rtype: :class:`com.vmware.vapi.metadata.authentication_client.OperationInfo`
        :return: The
            :class:`com.vmware.vapi.metadata.authentication_client.OperationInfo`
            instance that corresponds to ``operation_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the operation element associated with ``operation_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the operation element associated with ``operation_id`` does not
            have any authentication information.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            'operation_id': operation_id,
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
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vapi.metadata.authentication_client', 'OperationInfo'),
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
            self, iface_name='com.vmware.vapi.metadata.authentication.service.operation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Operation': Operation,
    }

