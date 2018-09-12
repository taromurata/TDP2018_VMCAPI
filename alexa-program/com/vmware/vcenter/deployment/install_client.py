# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.deployment.install.
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


class RemotePsc(VapiInterface):
    """
    The ``RemotePsc`` class provides methods to check if the deployed vCenter
    Server can register with the remote PSC. This class was added in vSphere
    API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RemotePscStub)


    def check(self,
              spec,
              ):
        """
        Checks whether the remote PSC is reachable and the deployed vCenter
        Server can be registered with the remote PSC. This method was added in
        vSphere API 6.7

        :type  spec: :class:`com.vmware.vcenter.deployment_client.RemotePscSpec`
        :param spec: Information to connect to the remote PSC.
        :rtype: :class:`com.vmware.vcenter.deployment_client.CheckInfo`
        :return: Information about the success or failure of the checks that were
            performed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if external PSC credentials are not valid when configuring a
            VCSA_EXTERNAL appliance.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is not in INITIALIZED state.
        """
        return self._invoke('check',
                            {
                            'spec': spec,
                            })
class _RemotePscStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.vcenter.deployment_client', 'RemotePscSpec'),
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
            url_template='/vcenter/deployment/install/remote-psc?action=check',
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
            self, iface_name='com.vmware.vcenter.deployment.install.remote_psc',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'RemotePsc': RemotePsc,
        'psc': 'com.vmware.vcenter.deployment.install.psc_client.StubFactory',
    }

