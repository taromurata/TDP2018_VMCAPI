# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.networks.segments.
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


class StaticArp(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StaticArpStub)


    def delete(self,
               network_id,
               segment_id,
               ):
        """
        Delete static ARP config

        :type  network_id: :class:`str`
        :param network_id: Network ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
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
                            'network_id': network_id,
                            'segment_id': segment_id,
                            })

    def get(self,
            network_id,
            segment_id,
            ):
        """
        Read static ARP config

        :type  network_id: :class:`str`
        :param network_id: Network ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :return: com.vmware.nsx_policy.model.StaticARPConfig
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
                            'network_id': network_id,
                            'segment_id': segment_id,
                            })

    def patch(self,
              network_id,
              segment_id,
              static_arp_config,
              ):
        """
        Create static ARP config with network and segment IDs provided if it
        doesn't exist, update with provided config if it's already created.

        :type  network_id: :class:`str`
        :param network_id: Network ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  static_arp_config: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :param static_arp_config: (required)
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
                            'network_id': network_id,
                            'segment_id': segment_id,
                            'static_arp_config': static_arp_config,
                            })

    def update(self,
               network_id,
               segment_id,
               static_arp_config,
               ):
        """
        Create static ARP config with network and segment IDs provided if it
        doesn't exist, update with provided config if it's already created.

        :type  network_id: :class:`str`
        :param network_id: Network ID (required)
        :type  segment_id: :class:`str`
        :param segment_id: Segment ID (required)
        :type  static_arp_config: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :param static_arp_config: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.StaticARPConfig`
        :return: com.vmware.nsx_policy.model.StaticARPConfig
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
                            'network_id': network_id,
                            'segment_id': segment_id,
                            'static_arp_config': static_arp_config,
                            })
class _StaticArpStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'network_id': type.StringType(),
            'segment_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/networks/{network-id}/segments/{segment-id}/static-arp',
            path_variables={
                'network_id': 'network-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'network_id': type.StringType(),
            'segment_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/networks/{network-id}/segments/{segment-id}/static-arp',
            path_variables={
                'network_id': 'network-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'network_id': type.StringType(),
            'segment_id': type.StringType(),
            'static_ARP_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
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
            url_template='/policy/api/v1/infra/networks/{network-id}/segments/{segment-id}/static-arp',
            request_body_parameter='static_ARP_config',
            path_variables={
                'network_id': 'network-id',
                'segment_id': 'segment-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'network_id': type.StringType(),
            'segment_id': type.StringType(),
            'static_ARP_config': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
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
            url_template='/policy/api/v1/infra/networks/{network-id}/segments/{segment-id}/static-arp',
            request_body_parameter='static_ARP_config',
            path_variables={
                'network_id': 'network-id',
                'segment_id': 'segment-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'StaticARPConfig'),
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
            self, iface_name='com.vmware.nsx_policy.infra.networks.segments.static_arp',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'StaticArp': StaticArp,
    }

