# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.datastore.
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


class DefaultPolicy(VapiInterface):
    """
    The ``DefaultPolicy`` class provides methods related to storage policies
    associated with datastore object. The :func:`DefaultPolicy.get` method
    provides information about the default storage policy associated with the
    specific datastore. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DefaultPolicyStub)


    def get(self,
            datastore,
            ):
        """
        Returns the identifier of the current default storage policy associated
        with the specified datastore. This method was added in vSphere API 6.7

        :type  datastore: :class:`str`
        :param datastore: Identifier of the datastore for which the default policy is
            requested.
            The parameter must be an identifier for the resource type:
            ``Datastore``.
        :rtype: :class:`str` or ``None``
        :return: Identifier of the default storage policy associated with the
            specified datastore.
            The return value will be an identifier for the resource type:
            ``com.vmware.vcenter.StoragePolicy``.
            this field is None if there is no default storage policy associated
            with the datastore.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the specified datastore does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required priveleges.
        """
        return self._invoke('get',
                            {
                            'datastore': datastore,
                            })
class _DefaultPolicyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'datastore': type.IdType(resource_types='Datastore'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/datastore/{datastore}/default-policy',
            path_variables={
                'datastore': 'datastore',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.OptionalType(type.IdType()),
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
            self, iface_name='com.vmware.vcenter.datastore.default_policy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DefaultPolicy': DefaultPolicy,
    }

