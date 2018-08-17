# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.deployment.install.psc.
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


class Replicated(VapiInterface):
    """
    The ``Replicated`` class provides methods to check if the configuring
    vCenter Server can be replicated to the remote PSC. This class was added in
    vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ReplicatedStub)


    def check(self,
              spec,
              ):
        """
        Checks whether the provided remote PSC is reachable and can be
        replicated. This method was added in vSphere API 6.7

        :type  spec: :class:`com.vmware.vcenter.deployment_client.ReplicatedPscSpec`
        :param spec: Information to configure a replicated PSC.
        :rtype: :class:`com.vmware.vcenter.deployment_client.CheckInfo`
        :return: Information about the success or failure of the checks that were
            performed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if external PSC credentials are not valid when configuring PSC to
            replicate with an external existing PSC.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is not in INITIALIZED state.
        """
        return self._invoke('check',
                            {
                            'spec': spec,
                            })
class Standalone(VapiInterface):
    """
    The ``Standalone`` class provides methods to check if the values provided
    for the standalone PSC satisfies the requirements. This class was added in
    vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StandaloneStub)


    def check(self,
              spec,
              ):
        """
        Checks that the information to configure a non-replicated PSC satisfies
        the requirements. This method was added in vSphere API 6.7

        :type  spec: :class:`com.vmware.vcenter.deployment_client.StandalonePscSpec`
        :param spec: Information to configure a non-replicated PSC.
        :rtype: :class:`com.vmware.vcenter.deployment_client.CheckInfo`
        :return: Information about the success or failure of the checks that were
            performed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is not in INITIALIZED state.
        """
        return self._invoke('check',
                            {
                            'spec': spec,
                            })
class _ReplicatedStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ReplicatedPscSpec'),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/deployment/install/psc/replicated?action=check',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check': {
                'input_type': check_input_type,
                'output_type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'CheckInfo'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': check_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'check': check_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.deployment.install.psc.replicated',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _StandaloneStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.vcenter.deployment_client', 'StandalonePscSpec'),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/deployment/install/psc/standalone?action=check',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'check': {
                'input_type': check_input_type,
                'output_type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'CheckInfo'),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': check_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'check': check_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.deployment.install.psc.standalone',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Replicated': Replicated,
        'Standalone': Standalone,
    }

