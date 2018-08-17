# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.storage.
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


class Policies(VapiInterface):
    """
    The ``Policies`` class provides methods for managing the storage policies.
    This class was added in vSphere API 6.7
    """
    RESOURCE_TYPE = "com.vmware.vcenter.StoragePolicy"
    """
    Resource type for vAPI metadata policy. This class attribute was added in
    vSphere API 6.7

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PoliciesStub)

    class FilterSpec(VapiStruct):
        """
        The ``Policies.FilterSpec`` class contains attributes used to filter the
        results when listing the storage policies (see :func:`Policies.list`). This
        class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policies=None,
                    ):
            """
            :type  policies: :class:`set` of :class:`str` or ``None``
            :param policies: Identifiers of storage policies that can match the filter. This
                attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
                If None or empty, storage policies with any identifiers match the
                filter.
            """
            self.policies = policies
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.filter_spec', {
            'policies': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Policies.Summary`` class contains commonly used information about a
        storage policy. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     policy=None,
                     name=None,
                     description=None,
                    ):
            """
            :type  policy: :class:`str`
            :param policy: Identifier of the storage policy. This attribute was added in
                vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
            :type  name: :class:`str`
            :param name: Name of the storage policy. This attribute was added in vSphere API
                6.7
            :type  description: :class:`str`
            :param description: Description of the storage policy. This attribute was added in
                vSphere API 6.7
            """
            self.policy = policy
            self.name = name
            self.description = description
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.summary', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.StoragePolicy'),
            'name': type.StringType(),
            'description': type.StringType(),
        },
        Summary,
        False,
        None))


    class CompatibleDatastoreInfo(VapiStruct):
        """
        The ``Policies.CompatibleDatastoreInfo`` class contains compatible
        datastore's information. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     datastore=None,
                    ):
            """
            :type  datastore: :class:`str`
            :param datastore: Identifier of the datastore. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``Datastore``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``Datastore``.
            """
            self.datastore = datastore
            VapiStruct.__init__(self)

    CompatibleDatastoreInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compatible_datastore_info', {
            'datastore': type.IdType(resource_types='Datastore'),
        },
        CompatibleDatastoreInfo,
        False,
        None))


    class CompatibilityInfo(VapiStruct):
        """
        The ``Policies.CompatibilityInfo`` class contains info about a list of
        datastores compatible with a specific storage policy. This class was added
        in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     compatible_datastores=None,
                    ):
            """
            :type  compatible_datastores: :class:`list` of :class:`Policies.CompatibleDatastoreInfo`
            :param compatible_datastores: Info about a list of datastores compatible with a specific storage
                policy. This attribute was added in vSphere API 6.7
            """
            self.compatible_datastores = compatible_datastores
            VapiStruct.__init__(self)

    CompatibilityInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compatibility_info', {
            'compatible_datastores': type.ListType(type.ReferenceType(__name__, 'Policies.CompatibleDatastoreInfo')),
        },
        CompatibilityInfo,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns information about at most 1024 visible (subject to permission
        checks) storage solicies availabe in vCenter. These storage policies
        can be used for provisioning virtual machines or disks. This method was
        added in vSphere API 6.7

        :type  filter: :class:`Policies.FilterSpec` or ``None``
        :param filter: Specification of matching storage policies for which information
            should be returned.
            If None, the behavior is equivalent to a
            :class:`Policies.FilterSpec` with all attributes None which means
            all storage policies match the filter
        :rtype: :class:`list` of :class:`Policies.Summary`
        :return: Commonly used Information about the storage policies.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :class:`Policies.FilterSpec` contains a value that is not
            supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1024 storage policies exist.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })

    def check_compatibility(self,
                            policy,
                            datastores,
                            ):
        """
        Returns datastore compatibility summary about a specific storage
        policy. This method was added in vSphere API 6.7

        :type  policy: :class:`str`
        :param policy: The storage policy identifier
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.StoragePolicy``.
        :type  datastores: :class:`set` of :class:`str`
        :param datastores: Datastores used to check compatibility against a storage policy.
            The number of datastores is limited to 1024.
            The parameter must contain identifiers for the resource type:
            ``Datastore``.
        :rtype: :class:`Policies.CompatibilityInfo`
        :return: datastore compatibility summary about a specific storage policy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the storage policy specified does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if input more than 1024 datastores.
        """
        return self._invoke('check_compatibility',
                            {
                            'policy': policy,
                            'datastores': datastores,
                            })
class _PoliciesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Policies.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/storage/policies',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for check_compatibility operation
        check_compatibility_input_type = type.StructType('operation-input', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.StoragePolicy'),
            'datastores': type.SetType(type.IdType()),
        })
        check_compatibility_error_dict = {
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
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),

        }
        check_compatibility_input_value_validator_list = [
        ]
        check_compatibility_output_validator_list = [
        ]
        check_compatibility_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/storage/policies/{policy}',
            path_variables={
                'policy': 'policy',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Policies.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'check_compatibility': {
                'input_type': check_compatibility_input_type,
                'output_type': type.ReferenceType(__name__, 'Policies.CompatibilityInfo'),
                'errors': check_compatibility_error_dict,
                'input_value_validator_list': check_compatibility_input_value_validator_list,
                'output_validator_list': check_compatibility_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'check_compatibility': check_compatibility_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.storage.policies',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policies': Policies,
        'policies': 'com.vmware.vcenter.storage.policies_client.StubFactory',
    }

