# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.hvc.management.
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


class Administrators(VapiInterface):
    """
    The ``Administrators`` provides methods to update, delete, and list groups
    in the local sso group. This is limited to the Hybrid Linked Mode service.
    **Warning:** This class is available as technical preview. It may be
    changed in a future release.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _AdministratorsStub)


    def add(self,
            group_name,
            ):
        """
        Add the local sso group with the new group. **Warning:** This method is
        available as technical preview. It may be changed in a future release.

        :type  group_name: :class:`str`
        :param group_name: Name of the new group to be added. Ex - xyz\\\\@abc.com where xyz
            is the group name and abc.com is the domain name
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('add',
                            {
                            'group_name': group_name,
                            })

    def remove(self,
               group_name,
               ):
        """
        Remove the group from the local sso group. **Warning:** This method is
        available as technical preview. It may be changed in a future release.

        :type  group_name: :class:`str`
        :param group_name: Name of the group to be removed. Ex - xyz\\\\@abc.com where xyz is
            the group name and abc.com is the domain name
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('remove',
                            {
                            'group_name': group_name,
                            })

    def set(self,
            group_names,
            ):
        """
        Sets the groups in the local sso group. **Warning:** This method is
        available as technical preview. It may be changed in a future release.

        :type  group_names: :class:`set` of :class:`str`
        :param group_names: Names the groups to be in the CloudAdminGroup Ex - xyz\\\\@abc.com
            where xyz is the group name and abc.com is the domain name
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('set',
                            {
                            'group_names': group_names,
                            })

    def get(self):
        """
        Enumerates the set of all the groups in the local sso group.
        **Warning:** This method is available as technical preview. It may be
        changed in a future release.


        :rtype: :class:`set` of :class:`str`
        :return: The :class:`set` of all the groups.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        """
        return self._invoke('get', None)
class _AdministratorsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'group_name': type.StringType(),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/hvc/management/administrators',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for remove operation
        remove_input_type = type.StructType('operation-input', {
            'group_name': type.StringType(),
        })
        remove_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        remove_input_value_validator_list = [
        ]
        remove_output_validator_list = [
        ]
        remove_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/hvc/management/administrators',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'group_names': type.SetType(type.StringType()),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/hvc/management/administrators',
            path_variables={
            },
            query_parameters={
            }
        )

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
            url_template='/hvc/management/administrators',
            path_variables={
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
            'remove': {
                'input_type': remove_input_type,
                'output_type': type.VoidType(),
                'errors': remove_error_dict,
                'input_value_validator_list': remove_input_value_validator_list,
                'output_validator_list': remove_output_validator_list,
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.SetType(type.StringType()),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'add': add_rest_metadata,
            'remove': remove_rest_metadata,
            'set': set_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.hvc.management.administrators',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Administrators': Administrators,
    }

