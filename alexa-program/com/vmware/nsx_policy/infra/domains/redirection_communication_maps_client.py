# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.domains.redirection_communication_maps.
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


class CommunicationEntries(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CommunicationEntriesStub)


    def delete(self,
               domain_id,
               redirection_map_id,
               communication_entry_id,
               ):
        """
        Delete RedirectionCommunicationEntry

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection Map ID (required)
        :type  communication_entry_id: :class:`str`
        :param communication_entry_id: RedirectionCommunicationEntry ID (required)
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
                            'domain_id': domain_id,
                            'redirection_map_id': redirection_map_id,
                            'communication_entry_id': communication_entry_id,
                            })

    def get(self,
            domain_id,
            redirection_map_id,
            communication_entry_id,
            ):
        """
        Read communication entry

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  communication_entry_id: :class:`str`
        :param communication_entry_id: Communication entry id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationEntry`
        :return: com.vmware.nsx_policy.model.RedirectionCommunicationEntry
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
                            'domain_id': domain_id,
                            'redirection_map_id': redirection_map_id,
                            'communication_entry_id': communication_entry_id,
                            })

    def list(self,
             domain_id,
             redirection_map_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List communication entries

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  cursor: :class:`str` or ``None``
        :param cursor: Opaque cursor to be used for getting next page of records (supplied
            by current result page) (optional)
        :type  included_fields: :class:`str` or ``None``
        :param included_fields: Comma separated list of fields that should be included in query
            result (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Maximum number of results to return in this page (server may return
            fewer) (optional, default to 1000)
        :type  sort_ascending: :class:`bool` or ``None``
        :param sort_ascending: (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Field by which records are sorted (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationEntryListResult`
        :return: com.vmware.nsx_policy.model.RedirectionCommunicationEntryListResult
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
                            'domain_id': domain_id,
                            'redirection_map_id': redirection_map_id,
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              domain_id,
              redirection_map_id,
              communication_entry_id,
              redirection_communication_entry,
              ):
        """
        Create a communication entry with the communication-entry-id is not
        already present, otherwise update the communication entry.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  communication_entry_id: :class:`str`
        :param communication_entry_id: Communication entry id (required)
        :type  redirection_communication_entry: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationEntry`
        :param redirection_communication_entry: (required)
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
                            'domain_id': domain_id,
                            'redirection_map_id': redirection_map_id,
                            'communication_entry_id': communication_entry_id,
                            'redirection_communication_entry': redirection_communication_entry,
                            })

    def update(self,
               domain_id,
               redirection_map_id,
               communication_entry_id,
               redirection_communication_entry,
               ):
        """
        Create a communication entry with the communication-entry-id is not
        already present, otherwise update the communication entry.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  communication_entry_id: :class:`str`
        :param communication_entry_id: Communication entry id (required)
        :type  redirection_communication_entry: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationEntry`
        :param redirection_communication_entry: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationEntry`
        :return: com.vmware.nsx_policy.model.RedirectionCommunicationEntry
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
                            'domain_id': domain_id,
                            'redirection_map_id': redirection_map_id,
                            'communication_entry_id': communication_entry_id,
                            'redirection_communication_entry': redirection_communication_entry,
                            })
class _CommunicationEntriesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'communication_entry_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}/communication-entries/{communication-entry-id}',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
                'communication_entry_id': 'communication-entry-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'communication_entry_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}/communication-entries/{communication-entry-id}',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
                'communication_entry_id': 'communication-entry-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'cursor': type.OptionalType(type.StringType()),
            'included_fields': type.OptionalType(type.StringType()),
            'page_size': type.OptionalType(type.IntegerType()),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}/communication-entries',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'communication_entry_id': type.StringType(),
            'redirection_communication_entry': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationEntry'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}/communication-entries/{communication-entry-id}',
            request_body_parameter='redirection_communication_entry',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
                'communication_entry_id': 'communication-entry-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'communication_entry_id': type.StringType(),
            'redirection_communication_entry': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationEntry'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}/communication-entries/{communication-entry-id}',
            request_body_parameter='redirection_communication_entry',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
                'communication_entry_id': 'communication-entry-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationEntry'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationEntryListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationEntry'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.domains.redirection_communication_maps.communication_entries',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'CommunicationEntries': CommunicationEntries,
    }
