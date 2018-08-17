# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vmc.orgs.sddcs.networks.edges.nat.config.
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


class Rules(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RulesStub)


    def add(self,
            org,
            sddc,
            edge_id,
            nat_rules,
            ):
        """
        Append a NAT rule for a management or compute gateway (NSX Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  nat_rules: :class:`com.vmware.vmc.model_client.NatRules`
        :param nat_rules: (required)
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidRequest` 
             Bad request. Request object passed is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             Forbidden. Authorization header not provided.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             Not found. Requested object not found.
        """
        return self._invoke('add',
                            {
                            'org': org,
                            'sddc': sddc,
                            'edge_id': edge_id,
                            'nat_rules': nat_rules,
                            })

    def delete(self,
               org,
               sddc,
               edge_id,
               rule_id,
               ):
        """
        Delete the specific NAT rule for a management or compute gateway (NSX
        Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  rule_id: :class:`long`
        :param rule_id: Rule Identifier. (required)
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
                            'edge_id': edge_id,
                            'rule_id': rule_id,
                            })

    def update(self,
               org,
               sddc,
               edge_id,
               rule_id,
               nsxnatrule,
               ):
        """
        Update the specific NAT rule for a management or compute gateway (NSX
        Edge).

        :type  org: :class:`str`
        :param org: Organization identifier. (required)
        :type  sddc: :class:`str`
        :param sddc: Sddc Identifier. (required)
        :type  edge_id: :class:`str`
        :param edge_id: Edge Identifier. (required)
        :type  rule_id: :class:`long`
        :param rule_id: Rule Identifier. (required)
        :type  nsxnatrule: :class:`com.vmware.vmc.model_client.Nsxnatrule`
        :param nsxnatrule: (required)
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
                            'edge_id': edge_id,
                            'rule_id': rule_id,
                            'nsxnatrule': nsxnatrule,
                            })
class _RulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'nat_rules': type.ReferenceType('com.vmware.vmc.model_client', 'NatRules'),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.invalid_request':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidRequest'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/nat/config/rules',
            request_body_parameter='nat_rules',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'rule_id': type.IntegerType(),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/nat/config/rules/{ruleId}',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
                'rule_id': 'ruleId',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'org': type.StringType(),
            'sddc': type.StringType(),
            'edge_id': type.StringType(),
            'rule_id': type.IntegerType(),
            'nsxnatrule': type.ReferenceType('com.vmware.vmc.model_client', 'Nsxnatrule'),
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
            url_template='/vmc/api/orgs/{org}/sddcs/{sddc}/networks/4.0/edges/{edgeId}/nat/config/rules/{ruleId}',
            request_body_parameter='nsxnatrule',
            path_variables={
                'org': 'org',
                'sddc': 'sddc',
                'edge_id': 'edgeId',
                'rule_id': 'ruleId',
            },
            query_parameters={
            }
        )

        operations = {
            'add': {
                'input_type': add_input_type,
                'output_type': type.VoidType(),
                'errors': add_error_dict,
                'input_value_validator_list': add_input_value_validator_list,
                'output_validator_list': add_output_validator_list,
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
            'add': add_rest_metadata,
            'delete': delete_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vmc.orgs.sddcs.networks.edges.nat.config.rules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=False)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Rules': Rules,
    }

