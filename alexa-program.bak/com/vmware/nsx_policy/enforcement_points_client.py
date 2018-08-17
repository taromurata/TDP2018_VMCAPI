# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.enforcement_points.
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


class ServiceDefinitions(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceDefinitionsStub)


    def create(self,
               enforcement_point_id,
               service_definition_id,
               service_definition,
               ):
        """
        Create a Service Definition on given enforcement point.

        :type  enforcement_point_id: :class:`str`
        :param enforcement_point_id: Enforcement point id (required)
        :type  service_definition_id: :class:`str`
        :param service_definition_id: Id of service definition (required)
        :type  service_definition: :class:`com.vmware.nsx_policy.model_client.ServiceDefinition`
        :param service_definition: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceDefinition`
        :return: com.vmware.nsx_policy.model.ServiceDefinition
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('create',
                            {
                            'enforcement_point_id': enforcement_point_id,
                            'service_definition_id': service_definition_id,
                            'service_definition': service_definition,
                            })

    def get(self,
            enforcement_point_id,
            service_definition_id,
            ):
        """
        Read Service Definition with given service-definition-id.

        :type  enforcement_point_id: :class:`str`
        :param enforcement_point_id: Enforcement point id (required)
        :type  service_definition_id: :class:`str`
        :param service_definition_id: Id of service definition (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceDefinition`
        :return: com.vmware.nsx_policy.model.ServiceDefinition
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'enforcement_point_id': enforcement_point_id,
                            'service_definition_id': service_definition_id,
                            })

    def list(self,
             enforcement_point_id,
             ):
        """
        List all Service Definitions registered on given enforcement point.

        :type  enforcement_point_id: :class:`str`
        :param enforcement_point_id: Enforcement point id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceInsertionServiceListResult`
        :return: com.vmware.nsx_policy.model.ServiceInsertionServiceListResult
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('list',
                            {
                            'enforcement_point_id': enforcement_point_id,
                            })

    def update(self,
               enforcement_point_id,
               service_definition_id,
               service_definition,
               ):
        """
        Update an existing Service Definition on the given enforcement point.

        :type  enforcement_point_id: :class:`str`
        :param enforcement_point_id: Enforcement point id (required)
        :type  service_definition_id: :class:`str`
        :param service_definition_id: Id of service definition (required)
        :type  service_definition: :class:`com.vmware.nsx_policy.model_client.ServiceDefinition`
        :param service_definition: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceDefinition`
        :return: com.vmware.nsx_policy.model.ServiceDefinition
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('update',
                            {
                            'enforcement_point_id': enforcement_point_id,
                            'service_definition_id': service_definition_id,
                            'service_definition': service_definition,
                            })
class _ServiceDefinitionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'enforcement_point_id': type.StringType(),
            'service_definition_id': type.StringType(),
            'service_definition': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceDefinition'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/enforcement-points/{enforcement-point-id}/service-definitions/{service-definition-id}',
            request_body_parameter='service_definition',
            path_variables={
                'enforcement_point_id': 'enforcement-point-id',
                'service_definition_id': 'service-definition-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'enforcement_point_id': type.StringType(),
            'service_definition_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/enforcement-points/{enforcement-point-id}/service-definitions/{service-definition-id}',
            path_variables={
                'enforcement_point_id': 'enforcement-point-id',
                'service_definition_id': 'service-definition-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'enforcement_point_id': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/enforcement-points/{enforcement-point-id}/service-definitions',
            path_variables={
                'enforcement_point_id': 'enforcement-point-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'enforcement_point_id': type.StringType(),
            'service_definition_id': type.StringType(),
            'service_definition': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceDefinition'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/enforcement-points/{enforcement-point-id}/service-definitions/{service-definition-id}',
            request_body_parameter='service_definition',
            path_variables={
                'enforcement_point_id': 'enforcement-point-id',
                'service_definition_id': 'service-definition-id',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceDefinition'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceDefinition'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceInsertionServiceListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceDefinition'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.enforcement_points.service_definitions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ServiceDefinitions': ServiceDefinitions,
    }

