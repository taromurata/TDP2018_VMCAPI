# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.account_link.
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


class CompatibleSubnets(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CompatibleSubnetsStub)


    def get(self,
            org,
            linked_account_id=None,
            region=None,
            ):
        """
        Gets a customer's compatible subnets for account linking

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  linked_account_id: :class:`str` or ``None``
        :param linked_account_id: The linked connected account identifier (optional)
        :type  region: :class:`str` or ``None``
        :param region: The region of the cloud resources to work in (optional)
        :rtype: :class:`com.vmware.vmc.model_client.AwsCompatibleSubnets`
        :return: com.vmware.vmc.model.AwsCompatibleSubnets
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'linked_account_id': linked_account_id,
                            'region': region,
                            })

    def post(self,
             org,
             ):
        """
        Sets which subnet to use to link accounts and finishes the linking
        process

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.AwsSubnet`
        :return: com.vmware.vmc.model.AwsSubnet
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('post',
                            {
                            'org': org,
                            })
class CompatibleSubnetsAsync(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CompatibleSubnetsAsyncStub)


    def get(self,
            org,
            linked_account_id=None,
            region=None,
            ):
        """
        Gets a customer's compatible subnets for account linking via a task.
        The information is returned as a member of the task (found in
        task.params['subnet_list_result'] when you are notified it is
        complete), and it's documented under ref
        /definitions/AwsCompatibleSubnets

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  linked_account_id: :class:`str` or ``None``
        :param linked_account_id: The linked connected account identifier (optional)
        :type  region: :class:`str` or ``None``
        :param region: The region of the cloud resources to work in (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'linked_account_id': linked_account_id,
                            'region': region,
                            })

    def post(self,
             aws_subnet,
             org,
             ):
        """
        Sets which subnet to use to link accounts and finishes the linking
        process via a task

        :type  aws_subnet: :class:`com.vmware.vmc.model_client.AwsSubnet`
        :param aws_subnet: The subnet chosen by the customer (required)
        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('post',
                            {
                            'aws_subnet': aws_subnet,
                            'org': org,
                            })
class ConnectedAccounts(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ConnectedAccountsStub)


    def delete(self,
               org,
               linked_account_path_id,
               force_even_when_sddc_present=None,
               ):
        """
        Delete a particular connected (linked) account.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  linked_account_path_id: :class:`str`
        :param linked_account_path_id: The linked connected account identifier (required)
        :type  force_even_when_sddc_present: :class:`bool` or ``None``
        :param force_even_when_sddc_present: When true, forcibly removes a connected account even when SDDC's
            are still linked to it. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.AwsCustomerConnectedAccount`
        :return: com.vmware.vmc.model.AwsCustomerConnectedAccount
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            An invalid connected account ID was specified, or the connection
            still has SDDCs active on it.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'linked_account_path_id': linked_account_path_id,
                            'force_even_when_sddc_present': force_even_when_sddc_present,
                            })

    def get(self,
            org,
            ):
        """
        Get a list of connected accounts

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.AwsCustomerConnectedAccount`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            })
class MapCustomerZones(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MapCustomerZonesStub)


    def post(self,
             org,
             map_zones_request,
             ):
        """
        Creates a task to re-map customer's datacenters across zones.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  map_zones_request: :class:`com.vmware.vmc.model_client.MapZonesRequest`
        :param map_zones_request: The zones request information about who to map and what to map.
            (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('post',
                            {
                            'org': org,
                            'map_zones_request': map_zones_request,
                            })
class SddcConnections(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcConnectionsStub)


    def get(self,
            org,
            sddc=None,
            ):
        """
        Get a list of SDDC connections currently setup for the customer's
        organization.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str` or ``None``
        :param sddc: sddc (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.AwsSddcConnection`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })
class _CompatibleSubnetsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'linked_account_id': type.OptionalType(type.StringType()),
            'region': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link/compatible-subnets',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'linked_account_id': 'linkedAccountId',
                'region': 'region',
            }
        )

        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/account-link/compatible-subnets',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'AwsCompatibleSubnets'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'AwsSubnet'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link.compatible_subnets',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _CompatibleSubnetsAsyncStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'linked_account_id': type.OptionalType(type.StringType()),
            'region': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link/compatible-subnets-async',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'linked_account_id': 'linkedAccountId',
                'region': 'region',
            }
        )

        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'aws_subnet': type.ReferenceType('com.vmware.vmc.model_client', 'AwsSubnet'),
            'org': type.StringType(),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/account-link/compatible-subnets-async',
            request_body_parameter='aws_subnet',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link.compatible_subnets_async',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ConnectedAccountsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'linked_account_path_id': type.StringType(),
            'force_even_when_sddc_present': type.OptionalType(type.BooleanType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vmc/api/orgs/{org}/account-link/connected-accounts/{linkedAccountPathId}',
            path_variables={
                'org': 'org',
                'linked_account_path_id': 'linkedAccountPathId',
            },
            query_parameters={
                'force_even_when_sddc_present': 'forceEvenWhenSddcPresent',
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link/connected-accounts',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'AwsCustomerConnectedAccount'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'AwsCustomerConnectedAccount')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link.connected_accounts',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _MapCustomerZonesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for post operation
        post_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'map_zones_request': type.ReferenceType('com.vmware.vmc.model_client', 'MapZonesRequest'),
        })
        post_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        post_input_value_validator_list = [
        ]
        post_output_validator_list = [
        ]
        post_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/account-link/map-customer-zones',
            request_body_parameter='map_zones_request',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'post': {
                'input_type': post_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': post_error_dict,
                'input_value_validator_list': post_input_value_validator_list,
                'output_validator_list': post_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'post': post_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link.map_customer_zones',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcConnectionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.OptionalType(type.StringType()),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link/sddc-connections',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'sddc': 'sddc',
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'AwsSddcConnection')),
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
            self, iface_name='com.vmware.vmc.orgs.account_link.sddc_connections',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'CompatibleSubnets': CompatibleSubnets,
        'CompatibleSubnetsAsync': CompatibleSubnetsAsync,
        'ConnectedAccounts': ConnectedAccounts,
        'MapCustomerZones': MapCustomerZones,
        'SddcConnections': SddcConnections,
    }

