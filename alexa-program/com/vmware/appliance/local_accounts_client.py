# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.local_accounts.
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


class Policy(VapiInterface):
    """
    The ``Policy`` class provides methods to manage local user accounts. This
    class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PolicyStub)

    class Info(VapiStruct):
        """
        The ``Policy.Info`` class defines the global password policy. This class
        was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     max_days=None,
                     min_days=None,
                     warn_days=None,
                    ):
            """
            :type  max_days: :class:`long` or ``None``
            :param max_days: Maximum number of days a password may be used. If the password is
                older than this, a password change will be forced. This attribute
                was added in vSphere API 6.7
                If None then the restriction will be ignored.
            :type  min_days: :class:`long` or ``None``
            :param min_days: Minimum number of days allowed between password changes. Any
                password changes attempted sooner than this will be rejected. This
                attribute was added in vSphere API 6.7
                If None then the restriction will be ignored.
            :type  warn_days: :class:`long` or ``None``
            :param warn_days: Number of days warning given before a password expires. A zero
                means warning is given only upon the day of expiration. This
                attribute was added in vSphere API 6.7
                If None then no warning will be provided.
            """
            self.max_days = max_days
            self.min_days = min_days
            self.warn_days = warn_days
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.local_accounts.policy.info', {
            'max_days': type.OptionalType(type.IntegerType()),
            'min_days': type.OptionalType(type.IntegerType()),
            'warn_days': type.OptionalType(type.IntegerType()),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Get the global password policy. This method was added in vSphere API
        6.7


        :rtype: :class:`Policy.Info`
        :return: Global password policy
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)

    def set(self,
            policy,
            ):
        """
        Set the global password policy. This method was added in vSphere API
        6.7

        :type  policy: :class:`Policy.Info`
        :param policy: Global password policy
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed policy values are < -1 or > 99999
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('set',
                            {
                            'policy': policy,
                            })
class _PolicyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/local-accounts/global-policy',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'policy': type.ReferenceType(__name__, 'Policy.Info'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/local-accounts/global-policy',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Policy.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.local_accounts.policy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policy': Policy,
    }

