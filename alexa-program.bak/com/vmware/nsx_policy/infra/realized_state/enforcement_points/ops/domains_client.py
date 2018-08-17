# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.realized_state.enforcement_points.ops.domains.
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


class DiscoverySessions(VapiInterface):
    """
    
    """
    GET_VIEW_VM_CONNECTION = "VM_CONNECTION"
    """
    Possible value for ``view`` of method :func:`DiscoverySessions.get`.

    """
    GET_VIEW_PROCESS_CONNECTION = "PROCESS_CONNECTION"
    """
    Possible value for ``view`` of method :func:`DiscoverySessions.get`.

    """
    GET_VIEW_GROUP_CONNECTION = "GROUP_CONNECTION"
    """
    Possible value for ``view`` of method :func:`DiscoverySessions.get`.

    """
    GET_VIEW_NETWORK_CONNECTION = "NETWORK_CONNECTION"
    """
    Possible value for ``view`` of method :func:`DiscoverySessions.get`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DiscoverySessionsStub)


    def get(self,
            enforcement_point_id,
            domain_id,
            discovery_session_id,
            view=None,
            ):
        """
        Read discovered information for a selected domain/application on
        selected enforcement point. Response contains topology information
        based on the view option specified in the query parameter. An error is
        returned if an unknown view option is specified in the query parameter.
        The topology information will not be populated if the discovery session
        status is in STARTED, IN-PROGRESS or FAILED state.

        :type  enforcement_point_id: :class:`str`
        :param enforcement_point_id: Enforcement point ID (required)
        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  discovery_session_id: :class:`str`
        :param discovery_session_id: Discovery session ID is Domain ID of the domain where discovery
            session was started (required)
        :type  view: :class:`str` or ``None``
        :param view: Option to specify specific view (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RealizedDiscoverySession`
        :return: com.vmware.nsx_policy.model.RealizedDiscoverySession
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
                            'domain_id': domain_id,
                            'discovery_session_id': discovery_session_id,
                            'view': view,
                            })
class _DiscoverySessionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'enforcement_point_id': type.StringType(),
            'domain_id': type.StringType(),
            'discovery_session_id': type.StringType(),
            'view': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/realized-state/enforcement-points/{enforcement-point-id}/ops/domains/{domain-id}/discovery-sessions/{discovery-session-id}',
            path_variables={
                'enforcement_point_id': 'enforcement-point-id',
                'domain_id': 'domain-id',
                'discovery_session_id': 'discovery-session-id',
            },
            query_parameters={
                'view': 'view',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RealizedDiscoverySession'),
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
            self, iface_name='com.vmware.nsx_policy.infra.realized_state.enforcement_points.ops.domains.discovery_sessions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DiscoverySessions': DiscoverySessions,
    }

