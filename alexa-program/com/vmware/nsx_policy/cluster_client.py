# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.cluster.
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


class Backups(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BackupsStub)


    def retrievesshfingerprint(self,
                               remote_server_fingerprint_request,
                               ):
        """
        Get SHA256 fingerprint of ECDSA key of remote server. The caller should
        independently verify that the key is trusted.

        :type  remote_server_fingerprint_request: :class:`com.vmware.nsx_policy.model_client.RemoteServerFingerprintRequest`
        :param remote_server_fingerprint_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RemoteServerFingerprint`
        :return: com.vmware.nsx_policy.model.RemoteServerFingerprint
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
        return self._invoke('retrievesshfingerprint',
                            {
                            'remote_server_fingerprint_request': remote_server_fingerprint_request,
                            })
class Nodes(VapiInterface):
    """
    
    """
    CREATE_ACTION_NODE = "add_cluster_node"
    """
    Possible value for ``action`` of method :func:`Nodes.create`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NodesStub)


    def create(self,
               add_cluster_node_spec,
               action,
               ):
        """
        Adds a new management node or controller node to the NSX cluster. A
        single node can perform one role, either management or control, not
        both.

        :type  add_cluster_node_spec: :class:`com.vmware.nsx_policy.model_client.AddClusterNodeSpec`
        :param add_cluster_node_spec: (required)
        :type  action: :class:`str`
        :param action: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterNodeConfig`
        :return: com.vmware.nsx_policy.model.ClusterNodeConfig
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
                            'add_cluster_node_spec': add_cluster_node_spec,
                            'action': action,
                            })

    def delete(self,
               node_id,
               ):
        """
        Removes the specified manager or control node from the NSX cluster.
        Before you can remove a node from the cluster, you must shut down the
        manager or controller service with the \\\\"stop service manager\\\\"
        or the \\\\"stop service controller\\\\" command.

        :type  node_id: :class:`str`
        :param node_id: (required)
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
                            'node_id': node_id,
                            })

    def get(self,
            node_id,
            ):
        """
        Returns information about the specified NSX cluster node.

        :type  node_id: :class:`str`
        :param node_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterNodeConfig`
        :return: com.vmware.nsx_policy.model.ClusterNodeConfig
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
                            'node_id': node_id,
                            })

    def list(self,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Returns information about all NSX cluster nodes.

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
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterNodeConfigListResult`
        :return: com.vmware.nsx_policy.model.ClusterNodeConfigListResult
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def revokemissingnodes(self,
                           revoke_node_request,
                           ):
        """
        Revoke Missing Nodes from the Cluster

        :type  revoke_node_request: :class:`com.vmware.nsx_policy.model_client.RevokeNodeRequest`
        :param revoke_node_request: (required)
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
        return self._invoke('revokemissingnodes',
                            {
                            'revoke_node_request': revoke_node_request,
                            })
class Restore(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RestoreStub)


    def advance(self,
                advance_cluster_restore_request,
                ):
        """
        Advance any currently suspended restore operation. The operation might
        have been suspended because (1) the user had suspended it previously,
        or (2) the operation is waiting for user input, to be provided as a
        part of the POST request body. This operation is only valid when a GET
        cluster/restore/status returns a status with value SUSPENDED.
        Otherwise, a 409 response is returned.

        :type  advance_cluster_restore_request: :class:`com.vmware.nsx_policy.model_client.AdvanceClusterRestoreRequest`
        :param advance_cluster_restore_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('advance',
                            {
                            'advance_cluster_restore_request': advance_cluster_restore_request,
                            })

    def cancel(self):
        """
        Cancel any currently running restore operation. If there exists a
        currently running step, it is allowed to finish. The system is not
        rolled back to the pre-restore state. This operation is only valid when
        a GET cluster/restore/status returns a status with value RUNNING or
        SUSPENDED. Otherwise, a 409 response is returned.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('cancel', None)

    def retry(self):
        """
        Retry any currently in-progress, failed restore operation. Only the
        last step of the multi-step restore operation would have failed,and
        only that step is retried. This operation is only valid when a GET
        cluster/restore/status returns a status with value FAILED. Otherwise, a
        409 response is returned.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('retry', None)

    def start(self,
              initiate_cluster_restore_request,
              ):
        """
        Start the restore of an NSX cluster, from some previously backed-up
        configuration. This operation is only valid when a GET
        cluster/restore/status returns a status with value NOT_STARTED.
        Otherwise, a 409 response is returned.

        :type  initiate_cluster_restore_request: :class:`com.vmware.nsx_policy.model_client.InitiateClusterRestoreRequest`
        :param initiate_cluster_restore_request: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('start',
                            {
                            'initiate_cluster_restore_request': initiate_cluster_restore_request,
                            })

    def suspend(self):
        """
        Suspend any currently running restore operation. The restore operation
        is made up of a number of steps. When this call is issued, any
        currently running step is allowed to finish (successfully or with
        errors), and the next step (and therefore the entire restore operation)
        is suspended until a subsequent resume or cancel call is issued. This
        operation is only valid when a GET cluster/restore/status returns a
        status with value RUNNING. Otherwise, a 409 response is returned.


        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterRestoreStatus`
        :return: com.vmware.nsx_policy.model.ClusterRestoreStatus
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
             Service Unavailable
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request, Precondition Failed
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
             Internal Server Error
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
             Conflict
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('suspend', None)
class Status(VapiInterface):
    """
    
    """
    GET_SOURCE_REALTIME = "realtime"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """
    GET_SOURCE_CACHED = "cached"
    """
    Possible value for ``source`` of method :func:`Status.get`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StatusStub)


    def get(self,
            source=None,
            ):
        """
        Returns status information for the NSX cluster control role and
        management role.

        :type  source: :class:`str` or ``None``
        :param source: Data source type. (optional)
        :rtype: :class:`com.vmware.nsx_policy.model_client.ClusterStatus`
        :return: com.vmware.nsx_policy.model.ClusterStatus
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
                            'source': source,
                            })
class _BackupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for retrievesshfingerprint operation
        retrievesshfingerprint_input_type = type.StructType('operation-input', {
            'remote_server_fingerprint_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RemoteServerFingerprintRequest'),
        })
        retrievesshfingerprint_error_dict = {
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
        retrievesshfingerprint_input_value_validator_list = [
        ]
        retrievesshfingerprint_output_validator_list = [
        ]
        retrievesshfingerprint_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/backups?action=retrieve_ssh_fingerprint',
            request_body_parameter='remote_server_fingerprint_request',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'retrievesshfingerprint': {
                'input_type': retrievesshfingerprint_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RemoteServerFingerprint'),
                'errors': retrievesshfingerprint_error_dict,
                'input_value_validator_list': retrievesshfingerprint_input_value_validator_list,
                'output_validator_list': retrievesshfingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'retrievesshfingerprint': retrievesshfingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.cluster.backups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _NodesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'add_cluster_node_spec': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AddClusterNodeSpec'),
            'action': type.StringType(),
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
            url_template='/policy/api/v1/cluster/nodes',
            request_body_parameter='add_cluster_node_spec',
            path_variables={
            },
            query_parameters={
                'action': 'action',
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/policy/api/v1/cluster/nodes/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'node_id': type.StringType(),
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
            url_template='/policy/api/v1/cluster/nodes/{node-id}',
            path_variables={
                'node_id': 'node-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
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
            url_template='/policy/api/v1/cluster/nodes',
            path_variables={
            },
            query_parameters={
                'cursor': 'cursor',
                'included_fields': 'included_fields',
                'page_size': 'page_size',
                'sort_ascending': 'sort_ascending',
                'sort_by': 'sort_by',
            }
        )

        # properties for revokemissingnodes operation
        revokemissingnodes_input_type = type.StructType('operation-input', {
            'revoke_node_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RevokeNodeRequest'),
        })
        revokemissingnodes_error_dict = {
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
        revokemissingnodes_input_value_validator_list = [
        ]
        revokemissingnodes_output_validator_list = [
        ]
        revokemissingnodes_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/nodes?action=revoke_missing_nodes',
            request_body_parameter='revoke_node_request',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterNodeConfig'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterNodeConfig'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterNodeConfigListResult'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revokemissingnodes': {
                'input_type': revokemissingnodes_input_type,
                'output_type': type.VoidType(),
                'errors': revokemissingnodes_error_dict,
                'input_value_validator_list': revokemissingnodes_input_value_validator_list,
                'output_validator_list': revokemissingnodes_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'revokemissingnodes': revokemissingnodes_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.cluster.nodes',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _RestoreStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for advance operation
        advance_input_type = type.StructType('operation-input', {
            'advance_cluster_restore_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'AdvanceClusterRestoreRequest'),
        })
        advance_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        advance_input_value_validator_list = [
        ]
        advance_output_validator_list = [
        ]
        advance_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=advance',
            request_body_parameter='advance_cluster_restore_request',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {})
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=cancel',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for retry operation
        retry_input_type = type.StructType('operation-input', {})
        retry_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        retry_input_value_validator_list = [
        ]
        retry_output_validator_list = [
        ]
        retry_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=retry',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'initiate_cluster_restore_request': type.ReferenceType('com.vmware.nsx_policy.model_client', 'InitiateClusterRestoreRequest'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=start',
            request_body_parameter='initiate_cluster_restore_request',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for suspend operation
        suspend_input_type = type.StructType('operation-input', {})
        suspend_error_dict = {
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        suspend_input_value_validator_list = [
        ]
        suspend_output_validator_list = [
        ]
        suspend_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/cluster/restore?action=suspend',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'advance': {
                'input_type': advance_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': advance_error_dict,
                'input_value_validator_list': advance_input_value_validator_list,
                'output_validator_list': advance_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': cancel_error_dict,
                'input_value_validator_list': cancel_input_value_validator_list,
                'output_validator_list': cancel_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'retry': {
                'input_type': retry_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': retry_error_dict,
                'input_value_validator_list': retry_input_value_validator_list,
                'output_validator_list': retry_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'start': {
                'input_type': start_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': start_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'suspend': {
                'input_type': suspend_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterRestoreStatus'),
                'errors': suspend_error_dict,
                'input_value_validator_list': suspend_input_value_validator_list,
                'output_validator_list': suspend_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'advance': advance_rest_metadata,
            'cancel': cancel_rest_metadata,
            'retry': retry_rest_metadata,
            'start': start_rest_metadata,
            'suspend': suspend_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.cluster.restore',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _StatusStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'source': type.OptionalType(type.StringType()),
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
            url_template='/policy/api/v1/cluster/status',
            path_variables={
            },
            query_parameters={
                'source': 'source',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'ClusterStatus'),
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
            self, iface_name='com.vmware.nsx_policy.cluster.status',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Backups': Backups,
        'Nodes': Nodes,
        'Restore': Restore,
        'Status': Status,
        'backups': 'com.vmware.nsx_policy.cluster.backups_client.StubFactory',
        'nodes': 'com.vmware.nsx_policy.cluster.nodes_client.StubFactory',
        'restore': 'com.vmware.nsx_policy.cluster.restore_client.StubFactory',
    }

