# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.storage.policy.
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
    The Compliance class provides methods that return the compliance status of
    virtual machine entities(virtual machine home directory and virtual disks)
    that specify storage policy requirements. This class was added in vSphere
    API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComplianceStub)

    class Status(Enum):
        """
        The ``Compliance.Status`` class defines the storage compliance status of a
        virtual machine and its applicable entities. This enumeration was added in
        vSphere API 6.7

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
        UNKNOWN_COMPLIANCE = None
        """
        Compliance status of the entity is not known. This class attribute was
        added in vSphere API 6.7

        """
        NOT_APPLICABLE = None
        """
        Compliance computation is not applicable for this entity because it does
        not have any storage requirements that apply to the datastore on which it
        is placed. This class attribute was added in vSphere API 6.7

        """
        OUT_OF_DATE = None
        """
        The Compliance status becomes out-of-date when the profile associated with
        the entity is edited but not applied. The compliance status remains
        out-of-date until the edited policy is applied to the entity. This class
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
        'com.vmware.vcenter.vm.storage.policy.compliance.status',
        Status))


    class VmComplianceInfo(VapiStruct):
        """
        The ``Compliance.VmComplianceInfo`` class contains information about
        storage policy compliance associated with a virtual machine. This class was
        added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     check_time=None,
                     policy=None,
                     failure_cause=None,
                    ):
            """
            :type  status: :class:`Compliance.Status`
            :param status: Status of the compliance operation. This attribute was added in
                vSphere API 6.7
            :type  check_time: :class:`datetime.datetime`
            :param check_time: Date and time of the most recent compliance check. This attribute
                was added in vSphere API 6.7
            :type  policy: :class:`str` or ``None``
            :param policy: Identifier of the storage policy associated with the virtual
                machine. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
                If None SPBM is unable to retrieve or determine the associated
                policy, :attr:`Compliance.VmComplianceInfo.failure_cause` is set in
                such casses.
            :type  failure_cause: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param failure_cause: The exception that caused the compliance check to fail. There can
                be more than one cause, since a policy can contain capabilities
                from multiple providers. If empty, it implies no failures while
                retrieving compliance. This attribute was added in vSphere API 6.7
            """
            self.status = status
            self.check_time = check_time
            self.policy = policy
            self.failure_cause = failure_cause
            VapiStruct.__init__(self)

    VmComplianceInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.compliance.vm_compliance_info', {
            'status': type.ReferenceType(__name__, 'Compliance.Status'),
            'check_time': type.DateTimeType(),
            'policy': type.OptionalType(type.IdType()),
            'failure_cause': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        VmComplianceInfo,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Compliance.Info`` class contains information about the storage policy
        compliance of a virtual machine, including information about it's home
        directory and/or it's virtual disks. This class was added in vSphere API
        6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     overall_compliance=None,
                     vm_home=None,
                     disks=None,
                    ):
            """
            :type  overall_compliance: :class:`Compliance.Status`
            :param overall_compliance: The overall compliance status of the virtual machine and all it's
                entities. This attribute was added in vSphere API 6.7
            :type  vm_home: :class:`Compliance.VmComplianceInfo` or ``None``
            :param vm_home: The storage policy compliance information
                :class:`Compliance.VmComplianceInfo` for the virtual machine's home
                directory. This attribute was added in vSphere API 6.7
                If None the virtual machine home directory has no storage policy
                association.
            :type  disks: :class:`dict` of :class:`str` and :class:`Compliance.VmComplianceInfo`
            :param disks: The compliance information :class:`Compliance.VmComplianceInfo` for
                the virtual machine's virtual disks that are currently associated
                with a storage policy. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
            """
            self.overall_compliance = overall_compliance
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.compliance.info', {
            'overall_compliance': type.ReferenceType(__name__, 'Compliance.Status'),
            'vm_home': type.OptionalType(type.ReferenceType(__name__, 'Compliance.VmComplianceInfo')),
            'disks': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Compliance.VmComplianceInfo')),
        },
        Info,
        False,
        None))


    class CheckSpec(VapiStruct):
        """
        The ``Compliance.CheckSpec`` class contains attributes used to specify the
        entities on which the storage policy compliance check is to be invoked.
        This class was added in vSphere API 6.7

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
            :param vm_home: Invoke compliance check on the virtual machine home directory if
                set to true. This attribute was added in vSphere API 6.7
            :type  disks: :class:`set` of :class:`str` or ``None``
            :param disks: Identifiers of the virtual machine's virtual disks for which
                compliance should be checked. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``. When methods return a
                value of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                If None or empty, compliance check is invoked on all the associated
                disks.
            """
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    CheckSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.compliance.check_spec', {
            'vm_home': type.BooleanType(),
            'disks': type.OptionalType(type.SetType(type.IdType())),
        },
        CheckSpec,
        False,
        None))



    def get(self,
            vm,
            ):
        """
        Returns the cached storage policy compliance information of a virtual
        machine. This method was added in vSphere API 6.7

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Compliance.Info` or ``None``
        :return: Virtual machine storage policy compliance Info
            :class:`Compliance.Info`.
            If None, neither the virtual machine home directory nor any of it's
            virtual disks are associated with a storage policy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })

    def check(self,
              vm,
              check_spec=None,
              ):
        """
        Returns the storage policy Compliance :class:`Compliance.Info` of a
        virtual machine after explicitly re-computing compliance check. This
        method was added in vSphere API 6.7

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  check_spec: :class:`Compliance.CheckSpec` or ``None``
        :param check_spec: Parameter specifies the entities on which storage policy compliance
            check is to be invoked. The storage compliance Info
            :class:`Compliance.Info` is returned.
            If None, the behavior is equivalent to a
            :class:`Compliance.CheckSpec` with CheckSpec#vmHome set to true and
            CheckSpec#disks populated with all disks attached to the virtual
            machine.
        :rtype: :class:`Compliance.Info` or ``None``
        :return: Virtual machine storage policy compliance ``Compliance.Info`` class
            .
            If None, neither the virtual machine home directory nor any of it's
            virtual disks are associated with a storage policy.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service necessary to
            complete the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user cannot be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required privileges.
        """
        return self._invoke('check',
                            {
                            'vm': vm,
                            'check_spec': check_spec,
                            })
class _ComplianceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
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
            url_template='/vcenter/vm/{vm}/storage/policy/compliance',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for check operation
        check_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'check_spec': type.OptionalType(type.ReferenceType(__name__, 'Compliance.CheckSpec')),
        })
        check_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        check_input_value_validator_list = [
        ]
        check_output_validator_list = [
        ]
        check_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/vm/{vm}/storage/policy/compliance',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.OptionalType(type.ReferenceType(__name__, 'Compliance.Info')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'check': {
                'input_type': check_input_type,
                'output_type': type.OptionalType(type.ReferenceType(__name__, 'Compliance.Info')),
                'errors': check_error_dict,
                'input_value_validator_list': check_input_value_validator_list,
                'output_validator_list': check_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'check': check_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.storage.policy.compliance',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Compliance': Compliance,
    }

