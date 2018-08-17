# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.providers.service_instances.
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


class ServiceInstanceEndpoints(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceInstanceEndpointsStub)


    def delete(self,
               provider_id,
               service_instance_id,
               service_instance_endpoint_id,
               ):
        """
        Delete policy service instance endpoint

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  service_instance_endpoint_id: :class:`str`
        :param service_instance_endpoint_id: Service instance endpoint id (required)
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
        return self._invoke('delete',
                            {
                            'provider_id': provider_id,
                            'service_instance_id': service_instance_id,
                            'service_instance_endpoint_id': service_instance_endpoint_id,
                            })

    def get(self,
            provider_id,
            service_instance_id,
            service_instance_endpoint_id,
            ):
        """
        Read service instance endpoint

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  service_instance_endpoint_id: :class:`str`
        :param service_instance_endpoint_id: Service instance endpoint id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceInstanceEndpoint`
        :return: com.vmware.nsx_policy.model.ServiceInstanceEndpoint
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
                            'provider_id': provider_id,
                            'service_instance_id': service_instance_id,
                            'service_instance_endpoint_id': service_instance_endpoint_id,
                            })

    def patch(self,
              provider_id,
              service_instance_id,
              service_instance_endpoint_id,
              service_instance_endpoint,
              ):
        """
        Create Service instance endpoint.

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  service_instance_endpoint_id: :class:`str`
        :param service_instance_endpoint_id: Service instance endpoint id (required)
        :type  service_instance_endpoint: :class:`com.vmware.nsx_policy.model_client.ServiceInstanceEndpoint`
        :param service_instance_endpoint: (required)
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
        return self._invoke('patch',
                            {
                            'provider_id': provider_id,
                            'service_instance_id': service_instance_id,
                            'service_instance_endpoint_id': service_instance_endpoint_id,
                            'service_instance_endpoint': service_instance_endpoint,
                            })

    def update(self,
               provider_id,
               service_instance_id,
               service_instance_endpoint_id,
               service_instance_endpoint,
               ):
        """
        Create service instance endpoint.

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  service_instance_id: :class:`str`
        :param service_instance_id: Service instance id (required)
        :type  service_instance_endpoint_id: :class:`str`
        :param service_instance_endpoint_id: Service instance endpoint id (required)
        :type  service_instance_endpoint: :class:`com.vmware.nsx_policy.model_client.ServiceInstanceEndpoint`
        :param service_instance_endpoint: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ServiceInstanceEndpoint`
        :return: com.vmware.nsx_policy.model.ServiceInstanceEndpoint
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
                            'provider_id': provider_id,
                            'service_instance_id': service_instance_id,
                            'service_instance_endpoint_id': service_instance_endpoint_id,
                            'service_instance_endpoint': service_instance_endpoint,
                            })
class _ServiceInstanceEndpointsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'service_instance_endpoint_id': type.StringType(),
        })
        delete_error_dict = {
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
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/policy/api/v1/infra/providers/{provider-id}/service-instances/{service-instance-id}/service-instance-endpoints/{service-instance-endpoint-id}',
            path_variables={
                'provider_id': 'provider-id',
                'service_instance_id': 'service-instance-id',
                'service_instance_endpoint_id': 'service-instance-endpoint-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'service_instance_endpoint_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/providers/{provider-id}/service-instances/{service-instance-id}/service-instance-endpoints/{service-instance-endpoint-id}',
            path_variables={
                'provider_id': 'provider-id',
                'service_instance_id': 'service-instance-id',
                'service_instance_endpoint_id': 'service-instance-endpoint-id',
            },
            query_parameters={
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'service_instance_endpoint_id': type.StringType(),
            'service_instance_endpoint': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceInstanceEndpoint'),
        })
        patch_error_dict = {
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
        patch_input_value_validator_list = [
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/providers/{provider-id}/service-instances/{service-instance-id}/service-instance-endpoints/{service-instance-endpoint-id}',
            request_body_parameter='service_instance_endpoint',
            path_variables={
                'provider_id': 'provider-id',
                'service_instance_id': 'service-instance-id',
                'service_instance_endpoint_id': 'service-instance-endpoint-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'service_instance_id': type.StringType(),
            'service_instance_endpoint_id': type.StringType(),
            'service_instance_endpoint': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceInstanceEndpoint'),
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
            url_template='/policy/api/v1/infra/providers/{provider-id}/service-instances/{service-instance-id}/service-instance-endpoints/{service-instance-endpoint-id}',
            request_body_parameter='service_instance_endpoint',
            path_variables={
                'provider_id': 'provider-id',
                'service_instance_id': 'service-instance-id',
                'service_instance_endpoint_id': 'service-instance-endpoint-id',
            },
            query_parameters={
            }
        )

        operations = {
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceInstanceEndpoint'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'patch': {
                'input_type': patch_input_type,
                'output_type': type.VoidType(),
                'errors': patch_error_dict,
                'input_value_validator_list': patch_input_value_validator_list,
                'output_validator_list': patch_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ServiceInstanceEndpoint'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.providers.service_instances.service_instance_endpoints',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'ServiceInstanceEndpoints': ServiceInstanceEndpoints,
    }

