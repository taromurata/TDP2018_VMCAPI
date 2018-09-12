# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.routing.service.
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


class Operation(VapiInterface):
    """
    Operations to retrieve information about routing in a vAPI operation
    """
    RESOURCE_TYPE = "com.vmware.vapi.operation"
    """
    Resource type for vAPI operation.

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
        Get the IDs of all the vAPI operations in the given service that
        contain routing information

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`list` of :class:`str`
        :return: list of operation identifiers
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
        Get information about a vAPI operation that contains routing
        information

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        :rtype: :class:`com.vmware.vapi.metadata.routing_client.OperationInfo`
        :return: Operation info for the vAPI operation that contains routing
            information.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the service identifier does not exist or if the specified
            operation identifier does not exist in the service.
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
                'output_type': type.ReferenceType('com.vmware.vapi.metadata.routing_client', 'OperationInfo'),
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
            self, iface_name='com.vmware.vapi.metadata.routing.service.operation',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Operation': Operation,
    }

