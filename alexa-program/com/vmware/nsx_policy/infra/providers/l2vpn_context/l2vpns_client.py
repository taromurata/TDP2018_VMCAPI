# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.providers.l2vpn_context.l2vpns.
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


class PeerConfig(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PeerConfigStub)


    def get(self,
            provider_id,
            l2vpn_id,
            enforcement_point_path=None,
            ):
        """
        Get peer config for the L2Vpn to configure the remote side of the
        tunnel. - no enforcement point path specified: L2Vpn Peer Codes will be
        evaluated on each enforcement point. - {enforcement_point_path}: L2Vpn
        Peer Codes are evaluated only on the given enforcement point.

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  l2vpn_id: :class:`str`
        :param l2vpn_id: L2Vpn id (required)
        :type  enforcement_point_path: :class:`str` or ``None``
        :param enforcement_point_path: String Path of the enforcement point (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.AggregateL2VpnPeerConfig`
        :return: com.vmware.nsx_policy.model.AggregateL2VpnPeerConfig
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
                            'l2vpn_id': l2vpn_id,
                            'enforcement_point_path': enforcement_point_path,
                            })
class Statistics(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatisticsStub)


    def get(self,
            provider_id,
            l2vpn_id,
            enforcement_point_path=None,
            ):
        """
        Get statistics of an L2Vpn. - no enforcement point path specified:
        Stats will be evaluated on each enforcement point. -
        {enforcement_point_path}: Stats are evaluated only on the given
        enforcement point.

        :type  provider_id: :class:`str`
        :param provider_id: Provider id (required)
        :type  l2vpn_id: :class:`str`
        :param l2vpn_id: L2Vpn id (required)
        :type  enforcement_point_path: :class:`str` or ``None``
        :param enforcement_point_path: String Path of the enforcement point (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.AggregateL2VpnStatistics`
        :return: com.vmware.nsx_policy.model.AggregateL2VpnStatistics
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
                            'l2vpn_id': l2vpn_id,
                            'enforcement_point_path': enforcement_point_path,
                            })
class _PeerConfigStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'l2vpn_id': type.StringType(),
            'enforcement_point_path': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/providers/{provider-id}/l2vpn-context/l2vpns/{l2vpn-id}/peer-config',
            path_variables={
                'provider_id': 'provider-id',
                'l2vpn_id': 'l2vpn-id',
            },
            query_parameters={
                'enforcement_point_path': 'enforcement_point_path',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AggregateL2VpnPeerConfig'),
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
            self, iface_name='com.vmware.nsx_policy.infra.providers.l2vpn_context.l2vpns.peer_config',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatisticsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'provider_id': type.StringType(),
            'l2vpn_id': type.StringType(),
            'enforcement_point_path': type.OptionalType(type.StringType()),
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
            HasFieldsOfValidator()
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/providers/{provider-id}/l2vpn-context/l2vpns/{l2vpn-id}/statistics',
            path_variables={
                'provider_id': 'provider-id',
                'l2vpn_id': 'l2vpn-id',
            },
            query_parameters={
                'enforcement_point_path': 'enforcement_point_path',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AggregateL2VpnStatistics'),
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
            self, iface_name='com.vmware.nsx_policy.infra.providers.l2vpn_context.l2vpns.statistics',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'PeerConfig': PeerConfig,
        'Statistics': Statistics,
    }

