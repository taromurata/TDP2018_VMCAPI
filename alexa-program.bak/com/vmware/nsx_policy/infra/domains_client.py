# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.nsx_policy.infra.domains.
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


class CommunicationMaps(VapiInterface):
    """
    
    """
    REVISE_OPERATION_TOP = "insert_top"
    """
    Possible value for ``operation`` of method :func:`CommunicationMaps.revise`.

    """
    REVISE_OPERATION_BOTTOM = "insert_bottom"
    """
    Possible value for ``operation`` of method :func:`CommunicationMaps.revise`.

    """
    REVISE_OPERATION_AFTER = "insert_after"
    """
    Possible value for ``operation`` of method :func:`CommunicationMaps.revise`.

    """
    REVISE_OPERATION_BEFORE = "insert_before"
    """
    Possible value for ``operation`` of method :func:`CommunicationMaps.revise`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CommunicationMapsStub)


    def delete(self,
               domain_id,
               communication_map_id,
               ):
        """
        Deletes the communication map along with all the communication entries

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  communication_map_id: :class:`str`
        :param communication_map_id: (required)
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
                            'communication_map_id': communication_map_id,
                            })

    def get(self,
            domain_id,
            communication_map_id,
            ):
        """
        Read communication-map for a domain.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  communication_map_id: :class:`str`
        :param communication_map_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :return: com.vmware.nsx_policy.model.CommunicationMap
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
                            'communication_map_id': communication_map_id,
                            })

    def list(self,
             domain_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all communication maps for a domain.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.CommunicationMapListResult`
        :return: com.vmware.nsx_policy.model.CommunicationMapListResult
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              domain_id,
              communication_map_id,
              communication_map,
              ):
        """
        Patch the communication map for a domain.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  communication_map_id: :class:`str`
        :param communication_map_id: (required)
        :type  communication_map: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :param communication_map: (required)
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
                            'communication_map_id': communication_map_id,
                            'communication_map': communication_map,
                            })

    def revise(self,
               domain_id,
               communication_map_id,
               communication_map,
               anchor_path=None,
               operation=None,
               ):
        """
        This is used to set a precedence of a communication map w.r.t others.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  communication_map_id: :class:`str`
        :param communication_map_id: (required)
        :type  communication_map: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :param communication_map: (required)
        :type  anchor_path: :class:`str` or ``None``
        :param anchor_path: The communication map/communication entry path if operation is
            'insert_after' or 'insert_before' (optional)
        :type  operation: :class:`str` or ``None``
        :param operation: Operation (optional, default to insert_top)
        :rtype: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :return: com.vmware.nsx_policy.model.CommunicationMap
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
        return self._invoke('revise',
                            {
                            'domain_id': domain_id,
                            'communication_map_id': communication_map_id,
                            'communication_map': communication_map,
                            'anchor_path': anchor_path,
                            'operation': operation,
                            })

    def update(self,
               domain_id,
               communication_map_id,
               communication_map,
               ):
        """
        Create or Update the communication map for a domain. This is a full
        replace. All the CommunicationEntries are replaced.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  communication_map_id: :class:`str`
        :param communication_map_id: (required)
        :type  communication_map: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :param communication_map: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.CommunicationMap`
        :return: com.vmware.nsx_policy.model.CommunicationMap
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
                            'communication_map_id': communication_map_id,
                            'communication_map': communication_map,
                            })
class DiscoverySessions(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DiscoverySessionsStub)


    def delete(self,
               domain_id,
               discovery_session_id,
               ):
        """
        Delete discovery session identified by discovery-session-id

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  discovery_session_id: :class:`str`
        :param discovery_session_id: Discovery Session ID (required)
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
                            'discovery_session_id': discovery_session_id,
                            })

    def get(self,
            domain_id,
            discovery_session_id,
            ):
        """
        Read discovery session identified by discovery-session-id

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  discovery_session_id: :class:`str`
        :param discovery_session_id: Domain ID (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.DiscoverySession`
        :return: com.vmware.nsx_policy.model.DiscoverySession
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
                            'discovery_session_id': discovery_session_id,
                            })

    def list(self,
             domain_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List all the discovery sessions created on a domain.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.DiscoverySessionListResult`
        :return: com.vmware.nsx_policy.model.DiscoverySessionListResult
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              domain_id,
              discovery_session_id,
              discovery_session,
              ):
        """
        Patch discovery session.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  discovery_session_id: :class:`str`
        :param discovery_session_id: Discovery session ID (required)
        :type  discovery_session: :class:`com.vmware.nsx_policy.model_client.DiscoverySession`
        :param discovery_session: (required)
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
                            'discovery_session_id': discovery_session_id,
                            'discovery_session': discovery_session,
                            })

    def update(self,
               domain_id,
               discovery_session_id,
               discovery_session,
               ):
        """
        Create or update discovery session.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  discovery_session_id: :class:`str`
        :param discovery_session_id: Discovery session ID (required)
        :type  discovery_session: :class:`com.vmware.nsx_policy.model_client.DiscoverySession`
        :param discovery_session: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.DiscoverySession`
        :return: com.vmware.nsx_policy.model.DiscoverySession
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
                            'discovery_session_id': discovery_session_id,
                            'discovery_session': discovery_session,
                            })
class DomainDeploymentMaps(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DomainDeploymentMapsStub)


    def delete(self,
               domain_id,
               domain_deployment_map_id,
               ):
        """
        Delete Domain Deployment Map

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  domain_deployment_map_id: :class:`str`
        :param domain_deployment_map_id: domain-deployment-map-id (required)
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
                            'domain_deployment_map_id': domain_deployment_map_id,
                            })

    def get(self,
            domain_id,
            domain_deployment_map_id,
            ):
        """
        Read a Domain Deployment Map

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  domain_deployment_map_id: :class:`str`
        :param domain_deployment_map_id: Domain Deployment Map id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.DomainDeploymentMap`
        :return: com.vmware.nsx_policy.model.DomainDeploymentMap
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
                            'domain_deployment_map_id': domain_deployment_map_id,
                            })

    def list(self,
             domain_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        Paginated list of all Domain Deployment Entries for infra.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.DomainDeploymentMapListResult`
        :return: com.vmware.nsx_policy.model.DomainDeploymentMapListResult
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              domain_id,
              domain_deployment_map_id,
              domain_deployment_map,
              ):
        """
        If the passed Domain Deployment Map does not already exist, create a
        new Domain Deployment Map. If it already exist, patch it.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  domain_deployment_map_id: :class:`str`
        :param domain_deployment_map_id: Domain Deployment Map ID (required)
        :type  domain_deployment_map: :class:`com.vmware.nsx_policy.model_client.DomainDeploymentMap`
        :param domain_deployment_map: (required)
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
                            'domain_deployment_map_id': domain_deployment_map_id,
                            'domain_deployment_map': domain_deployment_map,
                            })

    def update(self,
               domain_id,
               domain_deployment_map_id,
               domain_deployment_map,
               ):
        """
        If the passed Domain Deployment Map does not already exist, create a
        new Domain Deployment Map. If it already exist, replace it.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  domain_deployment_map_id: :class:`str`
        :param domain_deployment_map_id: Domain Deployment Map ID (required)
        :type  domain_deployment_map: :class:`com.vmware.nsx_policy.model_client.DomainDeploymentMap`
        :param domain_deployment_map: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.DomainDeploymentMap`
        :return: com.vmware.nsx_policy.model.DomainDeploymentMap
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
                            'domain_deployment_map_id': domain_deployment_map_id,
                            'domain_deployment_map': domain_deployment_map,
                            })
class EdgeCommunicationMaps(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EdgeCommunicationMapsStub)


    def get(self,
            domain_id,
            edge_communication_map_id,
            ):
        """
        Read Edge FW ns-communication-map for a domain.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  edge_communication_map_id: :class:`str`
        :param edge_communication_map_id: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.EdgeCommunicationMap`
        :return: com.vmware.nsx_policy.model.EdgeCommunicationMap
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
                            'edge_communication_map_id': edge_communication_map_id,
                            })

    def patch(self,
              domain_id,
              edge_communication_map_id,
              edge_communication_map,
              ):
        """
        Update the communication map for a domain. This is a full replace. All
        the CommunicationEntries are replaced.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  edge_communication_map_id: :class:`str`
        :param edge_communication_map_id: (required)
        :type  edge_communication_map: :class:`com.vmware.nsx_policy.model_client.EdgeCommunicationMap`
        :param edge_communication_map: (required)
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
                            'edge_communication_map_id': edge_communication_map_id,
                            'edge_communication_map': edge_communication_map,
                            })

    def update(self,
               domain_id,
               edge_communication_map_id,
               edge_communication_map,
               ):
        """
        Update the communication map for a domain. This is a full replace. All
        the CommunicationEntries are replaced.

        :type  domain_id: :class:`str`
        :param domain_id: (required)
        :type  edge_communication_map_id: :class:`str`
        :param edge_communication_map_id: (required)
        :type  edge_communication_map: :class:`com.vmware.nsx_policy.model_client.EdgeCommunicationMap`
        :param edge_communication_map: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.EdgeCommunicationMap`
        :return: com.vmware.nsx_policy.model.EdgeCommunicationMap
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
                            'edge_communication_map_id': edge_communication_map_id,
                            'edge_communication_map': edge_communication_map,
                            })
class Groups(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _GroupsStub)


    def delete(self,
               domain_id,
               group_id,
               force=None,
               ):
        """
        Delete Group

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  group_id: :class:`str`
        :param group_id: Group ID (required)
        :type  force: :class:`bool` or ``None``
        :param force: Force delete the resource even if it is being used somewhere
            (optional, default to false)
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
                            'group_id': group_id,
                            'force': force,
                            })

    def get(self,
            domain_id,
            group_id,
            ):
        """
        Read group

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  group_id: :class:`str`
        :param group_id: Group ID (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.Group`
        :return: com.vmware.nsx_policy.model.Group
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
                            'group_id': group_id,
                            })

    def list(self,
             domain_id,
             cursor=None,
             included_fields=None,
             page_size=None,
             sort_ascending=None,
             sort_by=None,
             ):
        """
        List Groups for a domain

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
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
        :rtype: :class:`com.vmware.nsx_policy.model_client.GroupListResult`
        :return: com.vmware.nsx_policy.model.GroupListResult
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
                            'cursor': cursor,
                            'included_fields': included_fields,
                            'page_size': page_size,
                            'sort_ascending': sort_ascending,
                            'sort_by': sort_by,
                            })

    def patch(self,
              domain_id,
              group_id,
              group,
              ):
        """
        If a group with the group-id is not already present, create a new
        group. If it already exists, patch the group.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  group_id: :class:`str`
        :param group_id: Group ID (required)
        :type  group: :class:`com.vmware.nsx_policy.model_client.Group`
        :param group: (required)
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
                            'group_id': group_id,
                            'group': group,
                            })

    def update(self,
               domain_id,
               group_id,
               group,
               ):
        """
        If a group with the group-id is not already present, create a new
        group. If it already exists, update the group.

        :type  domain_id: :class:`str`
        :param domain_id: Domain ID (required)
        :type  group_id: :class:`str`
        :param group_id: Group ID (required)
        :type  group: :class:`com.vmware.nsx_policy.model_client.Group`
        :param group: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.Group`
        :return: com.vmware.nsx_policy.model.Group
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
                            'group_id': group_id,
                            'group': group,
                            })
class RedirectionCommunicationMaps(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RedirectionCommunicationMapsStub)


    def delete(self,
               domain_id,
               redirection_map_id,
               ):
        """
        Delete redirection communication map.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
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
                            })

    def get(self,
            domain_id,
            redirection_map_id,
            ):
        """
        Read redirection communication map.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationMap`
        :return: com.vmware.nsx_policy.model.RedirectionCommunicationMap
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
                            })

    def patch(self,
              domain_id,
              redirection_map_id,
              redirection_communication_map,
              ):
        """
        Create or update the redirection communication map.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  redirection_communication_map: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationMap`
        :param redirection_communication_map: (required)
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
                            'redirection_communication_map': redirection_communication_map,
                            })

    def update(self,
               domain_id,
               redirection_map_id,
               redirection_communication_map,
               ):
        """
        Create or update the redirection communication map.

        :type  domain_id: :class:`str`
        :param domain_id: Domain id (required)
        :type  redirection_map_id: :class:`str`
        :param redirection_map_id: Redirection map id (required)
        :type  redirection_communication_map: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationMap`
        :param redirection_communication_map: (required)
        :rtype: :class:`com.vmware.nsx_policy.model_client.RedirectionCommunicationMap`
        :return: com.vmware.nsx_policy.model.RedirectionCommunicationMap
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
                            'redirection_communication_map': redirection_communication_map,
                            })
class _CommunicationMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'communication_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps/{communication-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'communication_map_id': 'communication-map-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'communication_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps/{communication-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'communication_map_id': 'communication-map-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps',
            path_variables={
                'domain_id': 'domain-id',
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
            'communication_map_id': type.StringType(),
            'communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps/{communication-map-id}',
            request_body_parameter='communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'communication_map_id': 'communication-map-id',
            },
            query_parameters={
            }
        )

        # properties for revise operation
        revise_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'communication_map_id': type.StringType(),
            'communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
            'anchor_path': type.OptionalType(type.StringType()),
            'operation': type.OptionalType(type.StringType()),
        })
        revise_error_dict = {
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
        revise_input_value_validator_list = [
        ]
        revise_output_validator_list = [
        ]
        revise_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps/{communication-map-id}?action=revise',
            request_body_parameter='communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'communication_map_id': 'communication-map-id',
            },
            query_parameters={
                'anchor_path': 'anchor_path',
                'operation': 'operation',
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'communication_map_id': type.StringType(),
            'communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/communication-maps/{communication-map-id}',
            request_body_parameter='communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'communication_map_id': 'communication-map-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMapListResult'),
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
            'revise': {
                'input_type': revise_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
                'errors': revise_error_dict,
                'input_value_validator_list': revise_input_value_validator_list,
                'output_validator_list': revise_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'CommunicationMap'),
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
            'revise': revise_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.domains.communication_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _DiscoverySessionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'discovery_session_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/discovery-sessions/{discovery-session-id}',
            path_variables={
                'domain_id': 'domain-id',
                'discovery_session_id': 'discovery-session-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'discovery_session_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/discovery-sessions/{discovery-session-id}',
            path_variables={
                'domain_id': 'domain-id',
                'discovery_session_id': 'discovery-session-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/discovery-sessions',
            path_variables={
                'domain_id': 'domain-id',
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
            'discovery_session_id': type.StringType(),
            'discovery_session': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DiscoverySession'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/discovery-sessions/{discovery-session-id}',
            request_body_parameter='discovery_session',
            path_variables={
                'domain_id': 'domain-id',
                'discovery_session_id': 'discovery-session-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'discovery_session_id': type.StringType(),
            'discovery_session': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DiscoverySession'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/discovery-sessions/{discovery-session-id}',
            request_body_parameter='discovery_session',
            path_variables={
                'domain_id': 'domain-id',
                'discovery_session_id': 'discovery-session-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DiscoverySession'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DiscoverySessionListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DiscoverySession'),
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
            self, iface_name='com.vmware.nsx_policy.infra.domains.discovery_sessions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _DomainDeploymentMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'domain_deployment_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/domain-deployment-maps/{domain-deployment-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'domain_deployment_map_id': 'domain-deployment-map-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'domain_deployment_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/domain-deployment-maps/{domain-deployment-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'domain_deployment_map_id': 'domain-deployment-map-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/domain-deployment-maps',
            path_variables={
                'domain_id': 'domain-id',
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
            'domain_deployment_map_id': type.StringType(),
            'domain_deployment_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DomainDeploymentMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/domain-deployment-maps/{domain-deployment-map-id}',
            request_body_parameter='domain_deployment_map',
            path_variables={
                'domain_id': 'domain-id',
                'domain_deployment_map_id': 'domain-deployment-map-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'domain_deployment_map_id': type.StringType(),
            'domain_deployment_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DomainDeploymentMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/domain-deployment-maps/{domain-deployment-map-id}',
            request_body_parameter='domain_deployment_map',
            path_variables={
                'domain_id': 'domain-id',
                'domain_deployment_map_id': 'domain-deployment-map-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DomainDeploymentMap'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DomainDeploymentMapListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'DomainDeploymentMap'),
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
            self, iface_name='com.vmware.nsx_policy.infra.domains.domain_deployment_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _EdgeCommunicationMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'edge_communication_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/edge-communication-maps/{edge-communication-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'edge_communication_map_id': 'edge-communication-map-id',
            },
            query_parameters={
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'edge_communication_map_id': type.StringType(),
            'edge_communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'EdgeCommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/edge-communication-maps/{edge-communication-map-id}',
            request_body_parameter='edge_communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'edge_communication_map_id': 'edge-communication-map-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'edge_communication_map_id': type.StringType(),
            'edge_communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'EdgeCommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/edge-communication-maps/{edge-communication-map-id}',
            request_body_parameter='edge_communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'edge_communication_map_id': 'edge-communication-map-id',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'EdgeCommunicationMap'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'EdgeCommunicationMap'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'patch': patch_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.nsx_policy.infra.domains.edge_communication_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _GroupsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'group_id': type.StringType(),
            'force': type.OptionalType(type.BooleanType()),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/groups/{group-id}',
            path_variables={
                'domain_id': 'domain-id',
                'group_id': 'group-id',
            },
            query_parameters={
                'force': 'force',
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'group_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/groups/{group-id}',
            path_variables={
                'domain_id': 'domain-id',
                'group_id': 'group-id',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
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
            HasFieldsOfValidator()
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/policy/api/v1/infra/domains/{domain-id}/groups',
            path_variables={
                'domain_id': 'domain-id',
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
            'group_id': type.StringType(),
            'group': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Group'),
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
            HasFieldsOfValidator()
        ]
        patch_output_validator_list = [
        ]
        patch_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/policy/api/v1/infra/domains/{domain-id}/groups/{group-id}',
            request_body_parameter='group',
            path_variables={
                'domain_id': 'domain-id',
                'group_id': 'group-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'group_id': type.StringType(),
            'group': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Group'),
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
            HasFieldsOfValidator()
        ]
        update_output_validator_list = [
            HasFieldsOfValidator()
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/policy/api/v1/infra/domains/{domain-id}/groups/{group-id}',
            request_body_parameter='group',
            path_variables={
                'domain_id': 'domain-id',
                'group_id': 'group-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Group'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'GroupListResult'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'Group'),
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
            self, iface_name='com.vmware.nsx_policy.infra.domains.groups',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _RedirectionCommunicationMapsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
            },
            query_parameters={
            }
        )

        # properties for patch operation
        patch_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'redirection_communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}',
            request_body_parameter='redirection_communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'domain_id': type.StringType(),
            'redirection_map_id': type.StringType(),
            'redirection_communication_map': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationMap'),
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
            url_template='/policy/api/v1/infra/domains/{domain-id}/redirection-communication-maps/{redirection-map-id}',
            request_body_parameter='redirection_communication_map',
            path_variables={
                'domain_id': 'domain-id',
                'redirection_map_id': 'redirection-map-id',
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationMap'),
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
                'output_type': type.ReferenceType('com.vmware.nsx_policy.model_client', 'RedirectionCommunicationMap'),
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
            self, iface_name='com.vmware.nsx_policy.infra.domains.redirection_communication_maps',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'CommunicationMaps': CommunicationMaps,
        'DiscoverySessions': DiscoverySessions,
        'DomainDeploymentMaps': DomainDeploymentMaps,
        'EdgeCommunicationMaps': EdgeCommunicationMaps,
        'Groups': Groups,
        'RedirectionCommunicationMaps': RedirectionCommunicationMaps,
        'communication_maps': 'com.vmware.nsx_policy.infra.domains.communication_maps_client.StubFactory',
        'edge_communication_maps': 'com.vmware.nsx_policy.infra.domains.edge_communication_maps_client.StubFactory',
        'groups': 'com.vmware.nsx_policy.infra.domains.groups_client.StubFactory',
        'redirection_communication_maps': 'com.vmware.nsx_policy.infra.domains.redirection_communication_maps_client.StubFactory',
    }

