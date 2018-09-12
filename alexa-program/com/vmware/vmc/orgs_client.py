# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.
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


class AccountLink(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AccountLinkStub)


    def create(self,
               org,
               ):
        """
        Gets a link that can be used on a customer's account to start the
        linking process.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
             Generic Error
        """
        return self._invoke('create',
                            {
                            'org': org,
                            })
class OfferInstances(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _OfferInstancesStub)


    def list(self,
             org,
             region,
             product_type,
             ):
        """
        List all offers available for the specific product type in the specific
        region

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  region: :class:`str`
        :param region: Region for the offer (required)
        :type  product_type: :class:`str`
        :param product_type: Type of the product in offers (required)
        :rtype: :class:`com.vmware.vmc.model_client.OfferInstancesHolder`
        :return: com.vmware.vmc.model.OfferInstancesHolder
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad Request. Type of the product not supported.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'region': region,
                            'product_type': product_type,
                            })
class Providers(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProvidersStub)


    def list(self,
             org,
             ):
        """
        

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.AwsCloudProvider`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Organization doesn't exist
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class SddcTemplates(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcTemplatesStub)


    def delete(self,
               org,
               template_id,
               ):
        """
        Delete SDDC template identified by given id.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  template_id: :class:`str`
        :param template_id: SDDC Template identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'template_id': template_id,
                            })

    def get(self,
            org,
            template_id,
            ):
        """
        Get configuration template by given template id.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  template_id: :class:`str`
        :param template_id: SDDC Template identifier (required)
        :rtype: :class:`com.vmware.vmc.model_client.SddcTemplate`
        :return: com.vmware.vmc.model.SddcTemplate
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC Template with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'template_id': template_id,
                            })

    def list(self,
             org,
             ):
        """
        List all available SDDC configuration templates in an organization

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SddcTemplate`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class Sddcs(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SddcsStub)


    def create(self,
               org,
               sddc_config,
               ):
        """
        Provision an SDDC in target cloud

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc_config: :class:`com.vmware.vmc.model_client.AwsSddcConfig`
        :param sddc_config: sddcConfig (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'sddc_config': sddc_config,
                            })

    def delete(self,
               org,
               sddc,
               retain_configuration=None,
               template_name=None,
               ):
        """
        Delete SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  retain_configuration: :class:`str` or ``None``
        :param retain_configuration: If = 'true', the SDDC's configuration is retained as a template for
            later use. This flag is applicable only to SDDCs in ACTIVE state.
            (optional)
        :type  template_name: :class:`str` or ``None``
        :param template_name: Only applicable when retainConfiguration is also set to 'true'.
            When set, this value will be used as the name of the SDDC
            configuration template generated. (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             The sddc is not in a state that's valid for deletion
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Access not allowed to the operation for the current user
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'sddc': sddc,
                            'retain_configuration': retain_configuration,
                            'template_name': template_name,
                            })

    def get(self,
            org,
            sddc,
            ):
        """
        Get SDDC

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Sddc`
        :return: com.vmware.vmc.model.Sddc
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the SDDC with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'sddc': sddc,
                            })

    def list(self,
             org,
             ):
        """
        List all the SDDCs of an organization

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.Sddc`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            })
class Subscriptions(VapiInterface):
    """
    
    """
    GET_0_OFFER_TYPE_TERM = "TERM"
    """
    Possible value for ``offerType`` of method :func:`Subscriptions.get_0`.

    """
    GET_0_OFFER_TYPE_ON_DEMAND = "ON_DEMAND"
    """
    Possible value for ``offerType`` of method :func:`Subscriptions.get_0`.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SubscriptionsStub)


    def create(self,
               org,
               subscription_request,
               ):
        """
        Initiates the creation of a subscription

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  subscription_request: :class:`com.vmware.vmc.model_client.SubscriptionRequest`
        :param subscription_request: subscriptionRequest (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('create',
                            {
                            'org': org,
                            'subscription_request': subscription_request,
                            })

    def delete(self,
               org,
               subscription,
               ):
        """
        Initiates subscription cancellation. Returns Task object.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  subscription: :class:`str`
        :param subscription: SubscriptionId for an sddc. (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
            Bad Request. Check if the subscription id is still valid and if the
            Sddc is in a state that can be deleted. More information will be
            available in the error_messages field.
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('delete',
                            {
                            'org': org,
                            'subscription': subscription,
                            })

    def get(self,
            org,
            subscription,
            ):
        """
        Get subscription details for a given subscription id

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  subscription: :class:`str`
        :param subscription: SubscriptionId for an sddc. (required)
        :rtype: :class:`com.vmware.vmc.model_client.SubscriptionDetails`
        :return: com.vmware.vmc.model.SubscriptionDetails
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'subscription': subscription,
                            })

    def get_0(self,
              org,
              offer_type=None,
              ):
        """
        Returns all subscriptions for a given org id

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  offer_type: :class:`str` or ``None``
        :param offer_type: Offer Type \\\\* \\\\`ON_DEMAND\\\\` - on-demand subscription \\\\*
            \\\\`TERM\\\\` - term subscription \\\\* All subscriptions if not
            specified (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.SubscriptionDetails`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.InternalServerError` 
            Server error. Check retryable flag to see if request should be
            retried.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not Found
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get_0',
                            {
                            'org': org,
                            'offer_type': offer_type,
                            })
class Tasks(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TasksStub)


    def get(self,
            org,
            task,
            ):
        """
        Retrieve details of a task.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  task: :class:`str`
        :param task: task Id (required)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the task with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('get',
                            {
                            'org': org,
                            'task': task,
                            })

    def list(self,
             org,
             filter=None,
             ):
        """
        List all tasks with optional filtering.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  filter: :class:`str` or ``None``
        :param filter: Filter expression Binary Operators: 'eq', 'ne', 'lt', 'gt', 'le',
            'ge' Nested attributes are composed using '.' Dates must be
            formatted as YYYY-MM-DD Strings should enclosed in single quotes,
            escape single quote with two single quotes The special literal
            'created' will be mapped to the time the resource was first
            created. NOTE: currently only ANDs of ORs is implemented. NOTE2:
            currently only range operators are implemented for created date.
            Examples: - $filter=(created gt '2016-08-09') and (org_id eq
            278710ff4e-6b6d-4d4e-aefb-ca637f38609e) - $filter=(created eq
            '2016-08-09') - $filter=(created gt '2016-08-09') and (sddc.status
            eq 'READY') (optional)
        :rtype: :class:`list` of :class:`com.vmware.vmc.model_client.Task`
        :return: 
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('list',
                            {
                            'org': org,
                            'filter': filter,
                            })

    def update(self,
               org,
               task,
               action=None,
               ):
        """
        Request that a running task be canceled. This is advisory only, some
        tasks may not be cancelable, and some tasks might take an arbitrary
        amount of time to respond to a cancelation request. The task must be
        monitored to determine subsequent status.

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  task: :class:`str`
        :param task: task Id (required)
        :type  action: :class:`str` or ``None``
        :param action: If = 'cancel', task will be canceled (optional)
        :rtype: :class:`com.vmware.vmc.model_client.Task`
        :return: com.vmware.vmc.model.Task
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Invalid action or bad argument
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Cannot find the task with given identifier
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
             Unauthorized
        """
        return self._invoke('update',
                            {
                            'org': org,
                            'task': task,
                            'action': action,
                            })
class _AccountLinkStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/account-link',
            path_variables={
                'org': 'org',
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
        }
        rest_metadata = {
            'create': create_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.account_link',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _OfferInstancesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'region': type.StringType(),
            'product_type': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/offer-instances',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'region': 'region',
                'product_type': 'product_type',
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'OfferInstancesHolder'),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.offer_instances',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _ProvidersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/providers',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'AwsCloudProvider')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.providers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcTemplatesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'template_id': type.StringType(),
        })
        delete_error_dict = {
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
            url_template='/vmc/api/orgs/{org}/sddc-templates/{templateId}',
            path_variables={
                'org': 'org',
                'template_id': 'templateId',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'template_id': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddc-templates/{templateId}',
            path_variables={
                'org': 'org',
                'template_id': 'templateId',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddc-templates',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SddcTemplate'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SddcTemplate')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddc_templates',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SddcsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc_config': type.ReferenceType('com.vmware.vmc.model_client', 'AwsSddcConfig'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs',
            request_body_parameter='sddc_config',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'retain_configuration': type.OptionalType(type.StringType()),
            'template_name': type.OptionalType(type.StringType()),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
                'retain_configuration': 'retain_configuration',
                'template_name': 'template_name',
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/sddcs',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Sddc'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'Sddc')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _SubscriptionsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'subscription_request': type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionRequest'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/subscriptions',
            request_body_parameter='subscription_request',
            path_variables={
                'org': 'org',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'subscription': type.StringType(),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
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
            url_template='/vmc/api/orgs/{org}/subscriptions/{subscription}',
            path_variables={
                'org': 'org',
                'subscription': 'subscription',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'subscription': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions/{subscription}',
            path_variables={
                'org': 'org',
                'subscription': 'subscription',
            },
            query_parameters={
            }
        )

        # properties for get_0 operation
        get_0_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'offer_type': type.OptionalType(type.StringType()),
        })
        get_0_error_dict = {
            'com.vmware.vapi.std.errors.internal_server_error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InternalServerError'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_0_input_value_validator_list = [
        ]
        get_0_output_validator_list = [
        ]
        get_0_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/subscriptions',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'offer_type': 'offer_type',
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionDetails'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get_0': {
                'input_type': get_0_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'SubscriptionDetails')),
                'errors': get_0_error_dict,
                'input_value_validator_list': get_0_input_value_validator_list,
                'output_validator_list': get_0_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'get_0': get_0_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.subscriptions',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)

class _TasksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'task': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/tasks/{task}',
            path_variables={
                'org': 'org',
                'task': 'task',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'filter': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vmc/api/orgs/{org}/tasks',
            path_variables={
                'org': 'org',
            },
            query_parameters={
                'filter': '$filter',
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'task': type.StringType(),
            'action': type.OptionalType(type.StringType()),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/tasks/{task}',
            path_variables={
                'org': 'org',
                'task': 'task',
            },
            query_parameters={
                'action': 'action',
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vmc.model_client', 'Task')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.ReferenceType('com.vmware.vmc.model_client', 'Task'),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.tasks',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'AccountLink': AccountLink,
        'OfferInstances': OfferInstances,
        'Providers': Providers,
        'SddcTemplates': SddcTemplates,
        'Sddcs': Sddcs,
        'Subscriptions': Subscriptions,
        'Tasks': Tasks,
        'account_link': 'com.vmware.vmc.orgs.account_link_client.StubFactory',
        'sddcs': 'com.vmware.vmc.orgs.sddcs_client.StubFactory',
    }

