# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.storage.policies.compliance.
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


class VM(VapiInterface):
    """
    The ``VM`` class provides methods related to query virtual machines of
    given compliance statuses. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VMStub)

    class Status(Enum):
        """
        The {\\\\@Status} class defines he valid compliance status values for a
        virtual machine or virtual disk. This enumeration was added in vSphere API
        6.7

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
        The virtual machine or virtual disk is in compliance. This class attribute
        was added in vSphere API 6.7

        """
        NON_COMPLIANT = None
        """
        The virtual machine or virtual disk is in not in compliance. This class
        attribute was added in vSphere API 6.7

        """
        UNKNOWN_COMPLIANCE = None
        """
        Compliance status of the virtual machine or virtual disk is not known. This
        class attribute was added in vSphere API 6.7

        """
        NOT_APPLICABLE = None
        """
        Compliance computation is not applicable for this virtual machine or disk
        because it does not have any storage requirement that apply to the
        object-based datastore on which the entity is placed. This class attribute
        was added in vSphere API 6.7

        """
        OUT_OF_DATE = None
        """
        Compliance status becomes out of date when the profile associated with the
        virtual machine or disk is edited and not applied. The compliance status
        will remain out of date until the latest policy is applied. This class
        attribute was added in vSphere API 6.7

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
        Status('UNKNOWN_COMPLIANCE'),
        Status('NOT_APPLICABLE'),
        Status('OUT_OF_DATE'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.vcenter.storage.policies.compliance.VM.status',
        Status))


    class Info(VapiStruct):
        """
        Provides the compliance details of a virtual machine and its associated
        entities which match the given compliance statuses. This class was added in
        vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm_home=None,
                     disks=None,
                    ):
            """
            :type  vm_home: :class:`VM.Status` or ``None``
            :param vm_home: Compliance status of the virtual machine home. This attribute was
                added in vSphere API 6.7
                If None or empty, virtual machine home is not associated with a
                storage policy.
            :type  disks: :class:`dict` of :class:`str` and :class:`VM.Status`
            :param disks: A Map of virtual disks and their compliance status If empty, the
                virtual machine does not have any disks or its disks are not
                associated with a storage policy. This attribute was added in
                vSphere API 6.7
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            """
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compliance.VM.info', {
            'vm_home': type.OptionalType(type.ReferenceType(__name__, 'VM.Status')),
            'disks': type.MapType(type.IdType(), type.ReferenceType(__name__, 'VM.Status')),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``VM.FilterSpec`` class contains Status used to filter the results when
        listing virtual machines (see :func:`VM.list`). This class was added in
        vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     vms=None,
                    ):
            """
            :type  status: :class:`set` of :class:`VM.Status`
            :param status: Compliance Status that a virtual machine must have to match the
                filter. Atleast one status must be specified. This attribute was
                added in vSphere API 6.7
            :type  vms: :class:`set` of :class:`str` or ``None``
            :param vms: Identifiers of virtual machines that can match the filter. This
                attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``VirtualMachine``. When methods return a value of this class as a
                return value, the attribute will contain identifiers for the
                resource type: ``VirtualMachine``.
                If None or empty, virtual machines with any identifier matches the
                filter
            """
            self.status = status
            self.vms = vms
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.storage.policies.compliance.VM.filter_spec', {
            'status': type.SetType(type.ReferenceType(__name__, 'VM.Status')),
            'vms': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter,
             ):
        """
        Returns compliance information about at most 1000 virtual machines
        matching the filter :class:`VM.FilterSpec`. If there are no virtual
        machines matching the :class:`VM.FilterSpec` an empty List is returned.
        Virtual machines without storage policy association are not returned.
        This method was added in vSphere API 6.7

        :type  filter: :class:`VM.FilterSpec`
        :param filter: compliance status of matching virtual machines for which
            information should be returned.
        :rtype: :class:`dict` of :class:`str` and :class:`VM.Info`
        :return: compliance information about virtual machines matching the filter
            :class:`VM.FilterSpec`.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``VirtualMachine``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`VM.FilterSpec.status` attribute contains a value that
            is not supported by the server.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the API is invoked against vCenter Server version is less than
            6.5
        :raise: :class:`com.vmware.vapi.std.errors_client.UnableToAllocateResource` 
            If more than 1000 results match the :class:`VM.FilterSpec`
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class _VMStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.ReferenceType(__name__, 'VM.FilterSpec'),
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
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.unable_to_allocate_resource':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'UnableToAllocateResource'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/storage/policies/compliance/vm',
            path_variables={
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
            self, iface_name='com.vmware.vcenter.storage.policies.compliance.VM',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'VM': VM,
    }

