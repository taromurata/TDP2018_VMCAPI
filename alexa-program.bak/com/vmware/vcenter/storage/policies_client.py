# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.storage.policies.
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


class Compliance(VapiInterface):
    """
    The Compliance class provides methods related to all the associated
    entities of given compliance statuses. This class was added in vSphere API
    6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComplianceStub)

    class Status(Enum):
        """
        This enumeration defines the set of status values for a compliance
        operation. This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        COMPLIANT = None
        """
        Entity is in compliance. This class attribute was added in vSphere API 6.7

        """
        NON_COMPLIANT = None
        """
        Entity is out of compliance. This class attribute was added in vSphere API
        6.7

        """
        UNKNOWN = None
        """
        Compliance status of the entity is not known. This class attribute was
        added in vSphere API 6.7

        """
        NOT_APPLICABLE = None
        """
        Compliance computation is not applicable for this entity because it does
        not have any storage requirement that apply to the object-based datastore
        on which the entity is placed. This class attribute was added in vSphere
        API 6.7

        """
        OUT_OF_DATE = None
        """
        Compliance status becomes out of date when the profile associated with the
        entity is edited and not applied. The compliance status will remain out of
        date until the latest policy is applied to the entity. This class attribute
        was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('COMPLIANT'),
        Status('NON_COMPLIANT'),
        Status('UNKNOWN'),
        Status('NOT_APPLICABLE'),
        Status('OUT_OF_DATE'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.vcenter.storage.policies.compliance.status',
        Status))


    class Summary(VapiStruct):
        """
        Provides the details of a virtual machine and its associated entities which
        match the given compliance statuses. This class was added in vSphere API
        6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm=None,
                     vm_home=None,
                     disks=None,
                    ):
            """
            :type  vm: :class:`str`
            :param vm: Identifier of virtual machine. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will be an identifier for the resource
                type: ``VirtualMachine``.
            :type  vm_home: :class:`Compliance.Status` or ``None``
            :param vm_home: Compliance status of the virtual machine home. This attribute was
                added in vSphere API 6.7
                If None or empty, vmHome is not associated with a storage policy.
            :type  disks: (:class:`dict` of :class:`str` and :class:`Compliance.Status`) or ``None``
            :param disks: List of the virtual hard disk. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If None or empty, virtual machine entity does not have any disks or
                its disks are not associated with a storage policy.
            """
            self.vm = vm
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compliance.summary', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'vm_home': type.OptionalType(type.ReferenceType(__name__, 'Compliance.Status')),
            'disks': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'Compliance.Status'))),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Compliance.FilterSpec`` class contains complianceStatus used to
        filter the results when listing entities (see :func:`Compliance.list`).
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                    ):
            """
            :type  status: :class:`set` of :class:`Compliance.Status`
            :param status: Compliance Status that a virtual machine must have to match the
                filter. This attribute was added in vSphere API 6.7
            """
            self.status = status
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compliance.filter_spec', {
            'status': type.SetType(type.ReferenceType(__name__, 'Compliance.Status')),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter,
             ):
        """
        Returns compliance information about entities matching the filter
        :class:`Compliance.FilterSpec`. Entities without storage policy
        association are not returned. This method was added in vSphere API 6.7

        :type  filter: :class:`Compliance.FilterSpec`
        :param filter: compliance status of matching entities for which information should
            be returned.
        :rtype: :class:`list` of :class:`Compliance.Summary`
        :return: compliance information about entities matching the filter
            :class:`Compliance.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`Compliance.FilterSpec.status` attribute contains a
            value that is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class VM(VapiInterface):
    """
    The ``VM`` class provides methods managing the storage policy association
    for a virtual machine and its virtual disks. This class was added in
    vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VMStub)

    class Info(VapiStruct):
        """
        The ``VM.Info`` class contains information about a virtual machine and its
        virtual disks that are associated with the given storage policy. This class
        was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm_home=None,
                     disks=None,
                    ):
            """
            :type  vm_home: :class:`bool`
            :param vm_home: Flag to indicate whether or not the virtual machine home is
                associated with the given storage policy. This attribute was added
                in vSphere API 6.7
            :type  disks: :class:`list` of :class:`str`
            :param disks: List of the virtual disks that are associated with the given
                storage policy. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            """
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.VM.info', {
            'vm_home': type.BooleanType(),
            'disks': type.ListType(type.IdType()),
        },
        Info,
        False,
        None))



    def list(self,
             policy,
             ):
        """
        Returns information about the virtual machines and/or their virtual
        disks that are associated with the given storage policy. This method
        was added in vSphere API 6.7

        :type  policy: :class:`str`
        :param policy: storage policy identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.StoragePolicy``.
        :rtype: :class:`dict` of :class:`str` and :class:`VM.Info`
        :return: Information about the virtual machines and/or their virtual disks
            that are associated with the given storage policy.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no policy associated with ``policy`` in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            if more than 1000 virtual machines are associated with the
            specified policy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service necessary to
            complete the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the backend server encounters some an error while processing the
            request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required priveleges.
        """
        return self._invoke('list',
                            {
                            'policy': policy,
                            })
class _ComplianceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.ReferenceType(__name__, 'Compliance.FilterSpec'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/storage/policies/entities/compliance',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Compliance.Summary')),
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
            self, iface_name='com.vmware.vcenter.storage.policies.compliance',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _VMStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'policy': type.IdType(resource_types='com.vmware.vcenter.StoragePolicy'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/storage/policies/{policy}/vm',
            path_variables={
                'policy': 'policy',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'VM.Info')),
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
            self, iface_name='com.vmware.vcenter.storage.policies.VM',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Compliance': Compliance,
        'VM': VM,
        'compliance': 'com.vmware.vcenter.storage.policies.compliance_client.StubFactory',
    }

