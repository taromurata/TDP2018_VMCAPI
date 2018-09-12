# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.realized_state.enforcement_points.
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


class VirtualMachines(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VirtualMachinesStub)


    def list(self,
             enforcement_point_name,
             cursor=None,
             dsl=None,
             included_fields=None,
             page_size=None,
             query=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        This API filters objects of type virtual machines from the specified
        NSX Manager.

        :type  enforcement_point_name: :class:`str`
        :param enforcement_point_name: (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  dsl: :class:`str` or ``None``
        :param dsl: Search DSL (domain specific language) query (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  query: :class:`str` or ``None``
        :param query: Search query (optional)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.SearchResponse`
        :return: com.vmware.nsx_policy.model.SearchResponse
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
                            'enforcement_point_name': enforcement_point_name,
                            'cursor': cursor,
                            'dsl': dsl,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'query': query,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def updatetags(self,
                   enforcement_point_name,
                   virtual_machine_tags_update,
                   ):
        """
        Allows an admin to apply multiple tags to a virtual machine. This
        operation does not store the intent on the policy side. It applies the
        tag directly on the specified enforcement point. This operation will
        replace the existing tags on the virtual machine with the ones that
        have been passed. If the application of tag fails on the enforcement
        point, then an error is reported. The admin will have to retry the
        operation again. Policy framework does not perform a retry. Failure
        could occur due to multiple reasons. For e.g enforcement point is down,
        Enforcement point could not apply the tag due to constraints like max
        tags limit exceeded, etc.

        :type  enforcement_point_name: :class:`str`
        :param enforcement_point_name: (required)
        :type  virtual_machine_tags_update: :class:`com.vmware.nsx_policy.model_client.VirtualMachineTagsUpdate`
        :param virtual_machine_tags_update: (required)
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
        return self._invoke('updatetags',
                            {
                            'enforcement_point_name': enforcement_point_name,
                            'virtual_machine_tags_update': virtual_machine_tags_update,
                            })
class _VirtualMachinesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'enforcement_point_name': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'dsl': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'query': type.OptionalType(type.StringType()),
            'sort_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/infra/realized-state/enforcement-points/{enforcement-point-name}/virtual-machines',
            path_variables={
                'enforcement_point_name': 'enforcement-point-name',
            },
            query_parameters={
                'cursor': 'cursor',
                'dsl': 'dsl',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'query': 'query',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            }
        )

        # properties for updatetags operation
        updatetags_input_type = type.StructType('operation-input', {
            'enforcement_point_name': type.StringType(),
            'virtual_machine_tags_update': type.ReferenceType('com.vmware.nsx_policy.model_client', 'VirtualMachineTagsUpdate'),
        })
        updatetags_error_dict = {
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
        updatetags_input_value_validator_list = [
        ]
        updatetags_output_validator_list = [
        ]
        updatetags_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/infra/realized-state/enforcement-points/{enforcement-point-name}/virtual-machines?action=update_tags',
            request_body_parameter='virtual_machine_tags_update',
            path_variables={
                'enforcement_point_name': 'enforcement-point-name',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'SearchResponse'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'updatetags': {
                'input_type': updatetags_input_type,
                'output_type': type.VoidType(),
                'errors': updatetags_error_dict,
                'input_value_validator_list': updatetags_input_value_validator_list,
                'output_validator_list': updatetags_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'updatetags': updatetags_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.realized_state.enforcement_points.virtual_machines',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'VirtualMachines': VirtualMachines,
        'firewalls': 'com.vmware.nsx_policy.infra.realized_state.enforcement_points.firewalls_client.StubFactory',
        'groups': 'com.vmware.nsx_policy.infra.realized_state.enforcement_points.groups_client.StubFactory',
        'ip_sets': 'com.vmware.nsx_policy.infra.realized_state.enforcement_points.ip_sets_client.StubFactory',
        'mac_sets': 'com.vmware.nsx_policy.infra.realized_state.enforcement_points.mac_sets_client.StubFactory',
        'services': 'com.vmware.nsx_policy.infra.realized_state.enforcement_points.services_client.StubFactory',
    }

