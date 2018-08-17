# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.networks.
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


class Edges(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EdgesStub)


    def get(self,
            org,
            sddc,
            edge_type,
            prev_edge_id=None,
            start_index=None,
            page_size=None,
            sort_order_ascending=None,
            sort_by=None,
            filter=None,
            ld_rname=None,
            ):
        """
        Retrieve information about all management and compute gateways and
        other routers (NSX Edges).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_type: :class:`str`
        :param edge_type: Retrieve records matching NSX Edge type ('gatewayServices' or
            'distributedRouter'). Specify gatewayServices to find management
            and compute gateways in your SDDC. (required)
        :type  prev_edge_id: :class:`str` or ``None``
        :param prev_edge_id: Provide Edge ID as prevEdgeId to serve as reference for startIndex.
            (optional)
        :type  start_index: :class:`long` or ``None``
        :param start_index: Start index for the current page. Default is 0. (optional)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Number of records per page. Default is 256. (optional)
        :type  sort_order_ascending: :class:`bool` or ``None``
        :param sort_order_ascending: Set to true to fetch records in ascending sorted order. (optional)
        :type  sort_by: :class:`str` or ``None``
        :param sort_by: Sort records using one of the column names (id, name, description,
            tenantId, size, enableFips). (optional)
        :type  filter: :class:`str` or ``None``
        :param filter: Filter records matching the NSX Edge ID, name or description.
            (optional)
        :type  ld_rname: :class:`str` or ``None``
        :param ld_rname: (optional)
        :rtype: :class:`com.vmware.vmc.model_client.PagedEdgeList`
        :return: com.vmware.vmc.model.PagedEdgeList
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'edge_type': edge_type,
                            'prev_edge_id': prev_edge_id,
                            'start_index': start_index,
                            'page_size': page_size,
                            'sort_order_ascending': sort_order_ascending,
                            'sort_by': sort_by,
                            'filter': filter,
                            'ld_rname': ld_rname,
                            })
class Logical(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LogicalStub)


    def create(self,
               org,
               sddc,
               sddc_network,
               ):
        """
        Create a network in an SDDC.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  sddc_network: :class:`com.vmware.vmc.model_client.SddcNetwork`
        :param sddc_network: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc': sddc,
                            'sddc_network': sddc_network,
                            })

    def delete(self,
               org,
               sddc,
               network_id,
               ):
        """
        Delete a network in an SDDC.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  network_id: :class:`str`
        :param network_id: Logical Network Identifier (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'network_id': network_id,
                            })

    def get(self,
            org,
            sddc,
            network_id,
            ):
        """
        Retrieve information about a network in an SDDC.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  network_id: :class:`str`
        :param network_id: Logical Network Identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.SddcNetwork`
        :return: com.vmware.vmc.model.SddcNetwork
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            'network_id': network_id,
                            })

    def get_0(self,
              org,
              sddc,
              page_size=None,
              start_index=None,
              prev_sddc_network_id=None,
              sort_order_ascending=None,
              ):
        """
        Retrieve all networks in an SDDC.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  page_size: :class:`long` or ``None``
        :param page_size: Page size for pagination. (optional)
        :type  start_index: :class:`long` or ``None``
        :param start_index: Start index of page. (optional)
        :type  prev_sddc_network_id: :class:`str` or ``None``
        :param prev_sddc_network_id: Previous logical network id. (optional)
        :type  sort_order_ascending: :class:`bool` or ``None``
        :param sort_order_ascending: Sort order ascending. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.DataPageSddcNetwork`
        :return: com.vmware.vmc.model.DataPageSddcNetwork
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('get_0',
                            {
                            'org': org,
                            'sddc': sddc,
                            'page_size': page_size,
                            'start_index': start_index,
                            'prev_sddc_network_id': prev_sddc_network_id,
                            'sort_order_ascending': sort_order_ascending,
                            })

    def update(self,
               org,
               sddc,
               network_id,
               sddc_network,
               ):
        """
        Modify a network in an SDDC.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  network_id: :class:`str`
        :param network_id: Logical Network Identifier (required)
        :type  sddc_network: :class:`com.vmware.vmc.model_client.SddcNetwork`
        :param sddc_network: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'sddc': sddc,
                            'network_id': network_id,
                            'sddc_network': sddc_network,
                            })
class _EdgesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_type': type.StringType(),
            'prev_edge_id': type.OptionalType(type.StringType()),
            'start_index': type.OptionalType(type.IntegerType()),
            'page_size': type.OptionalType(type.IntegerType()),
            'sort_order_ascending': type.OptionalType(type.BooleanType()),
            'sort_by': type.OptionalType(type.StringType()),
            'filter': type.OptionalType(type.StringType()),
            'ld_rname': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'edge_type': 'edgeType',
                'prev_edge_id': 'prevEdgeId',
                'start_index': 'startIndex',
                'page_size': 'pageSize',
                'sort_order_ascending': 'sortOrderAscending',
                'sort_by': 'sortBy',
                'filter': 'filter',
                'ld_rname': 'LDRname',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'PagedEdgeList'),
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
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.edges',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _LogicalStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'sddc_network': type.ReferenceType('com.vmware.vmc.model_client', 'SddcNetwork'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/sddc/networks',
            request_body_parameter='sddc_network',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'network_id': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/sddc/networks/{networkId}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'network_id': 'networkId',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'network_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/sddc/networks/{networkId}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'network_id': 'networkId',
            },
            query_parameters={
            }
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'page_size': type.OptionalType(type.IntegerType()),
            'start_index': type.OptionalType(type.IntegerType()),
            'prev_sddc_network_id': type.OptionalType(type.StringType()),
            'sort_order_ascending': type.OptionalType(type.BooleanType()),
        })
        get_0_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/sddc/networks',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'page_size': 'pageSize',
                'start_index': 'startIndex',
                'prev_sddc_network_id': 'prevSddcNetworkId',
                'sort_order_ascending': 'sortOrderAscending',
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'network_id': type.StringType(),
            'sddc_network': type.ReferenceType('com.vmware.vmc.model_client', 'SddcNetwork'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/sddc/networks/{networkId}',
            request_body_parameter='sddc_network',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'network_id': 'networkId',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
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
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SddcNetwork'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'DataPageSddcNetwork'),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.logical',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Edges': Edges,
        'Logical': Logical,
        'edges': 'com.vmware.vmc.orgs.sddcs.networks.edges_client.StubFactory',
    }

