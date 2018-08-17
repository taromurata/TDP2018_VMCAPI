# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.vm.storage.
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
    The ``Policy`` class provides methods to configure the storage policies
    associated with the virtual machine home and/or its virtual disks. This
    class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PolicyStub)

    class VmHomePolicySpec(VapiStruct):
        """
        The ``Policy.VmHomePolicySpec`` class provides a specification for the
        storage policy to be associated with the virtual machine home's directory.
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                    'USE_DEFAULT_POLICY' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`Policy.VmHomePolicySpec.PolicyType`
            :param type: Policy type to be used while performing update operation on the
                virtual machine home's directory. This attribute was added in
                vSphere API 6.7
            :type  policy: :class:`str`
            :param policy: Storage Policy identification. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`Policy.VmHomePolicySpec.PolicyType.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class PolicyType(Enum):
            """
            The ``Policy.VmHomePolicySpec.PolicyType`` class defines the choices for
            how to specify the policy to be associated with the virtual machine home's
            directory. This enumeration was added in vSphere API 6.7

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy (see :attr:`Policy.VmHomePolicySpec.policy`). This
            class attribute was added in vSphere API 6.7

            """
            USE_DEFAULT_POLICY = None
            """
            Use the default storage policy of the datastore. This class attribute was
            added in vSphere API 6.7

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`PolicyType` instance.
                """
                Enum.__init__(string)

        PolicyType._set_values([
            PolicyType('USE_SPECIFIED_POLICY'),
            PolicyType('USE_DEFAULT_POLICY'),
        ])
        PolicyType._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm.storage.policy.vm_home_policy_spec.policy_type',
            PolicyType))

    VmHomePolicySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.vm_home_policy_spec', {
            'type': type.ReferenceType(__name__, 'Policy.VmHomePolicySpec.PolicyType'),
            'policy': type.OptionalType(type.IdType()),
        },
        VmHomePolicySpec,
        False,
        None))


    class DiskPolicySpec(VapiStruct):
        """
        The ``Policy.DiskPolicySpec`` class provides a specification for the
        storage policy to be associated with the virtual disks. This class was
        added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'USE_SPECIFIED_POLICY' : [('policy', True)],
                    'USE_DEFAULT_POLICY' : [],
                }
            ),
        ]



        def __init__(self,
                     type=None,
                     policy=None,
                    ):
            """
            :type  type: :class:`Policy.DiskPolicySpec.PolicyType`
            :param type: Policy type to be used while performing update operation on the
                virtual disks. This attribute was added in vSphere API 6.7
            :type  policy: :class:`str`
            :param policy: Storage Policy identification. This attribute was added in vSphere
                API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`Policy.DiskPolicySpec.PolicyType.USE_SPECIFIED_POLICY`.
            """
            self.type = type
            self.policy = policy
            VapiStruct.__init__(self)

        class PolicyType(Enum):
            """
            The ``Policy.DiskPolicySpec`` class defines the choices for how to specify
            the policy to be associated with a virtual disk. This enumeration was added
            in vSphere API 6.7

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            USE_SPECIFIED_POLICY = None
            """
            Use the specified policy (see :attr:`Policy.DiskPolicySpec.policy`). This
            class attribute was added in vSphere API 6.7

            """
            USE_DEFAULT_POLICY = None
            """
            Use the default storage policy of the datastore. This class attribute was
            added in vSphere API 6.7

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`PolicyType` instance.
                """
                Enum.__init__(string)

        PolicyType._set_values([
            PolicyType('USE_SPECIFIED_POLICY'),
            PolicyType('USE_DEFAULT_POLICY'),
        ])
        PolicyType._set_binding_type(type.EnumType(
            'com.vmware.vcenter.vm.storage.policy.disk_policy_spec.policy_type',
            PolicyType))

    DiskPolicySpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.disk_policy_spec', {
            'type': type.ReferenceType(__name__, 'Policy.DiskPolicySpec.PolicyType'),
            'policy': type.OptionalType(type.IdType()),
        },
        DiskPolicySpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Policy.UpdateSpec`` class describes the updates to be made to the
        storage policies associated with the virtual machine home and/or its
        virtual disks. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     vm_home=None,
                     disks=None,
                    ):
            """
            :type  vm_home: :class:`Policy.VmHomePolicySpec` or ``None``
            :param vm_home: Storage policy to be used when reconfiguring the virtual machine
                home. This attribute was added in vSphere API 6.7
                if None the current storage policy is retained.
            :type  disks: (:class:`dict` of :class:`str` and :class:`Policy.DiskPolicySpec`) or ``None``
            :param disks: Storage policy or policies to be used when reconfiguring virtual
                machine diks. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the key in
                the attribute :class:`dict` must be an identifier for the resource
                type: ``com.vmware.vcenter.vm.hardware.Disk``. When methods return
                a value of this class as a return value, the key in the attribute
                :class:`dict` will be an identifier for the resource type:
                ``com.vmware.vcenter.vm.hardware.Disk``.
                if None the current storage policy is retained.
            """
            self.vm_home = vm_home
            self.disks = disks
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.vm.storage.policy.update_spec', {
            'vm_home': type.OptionalType(type.ReferenceType(__name__, 'Policy.VmHomePolicySpec')),
            'disks': type.OptionalType(type.MapType(type.IdType(), type.ReferenceType(__name__, 'Policy.DiskPolicySpec'))),
        },
        UpdateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Policy.Info`` class contains information about the storage policies
        associated with virtual machine's home directory and virtual hard disks.
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
            :type  vm_home: :class:`str` or ``None``
            :param vm_home: Storage Policy associated with virtual machine home. This attribute
                was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``. When methods return a value
                of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.vcenter.StoragePolicy``.
                IfNone, the virtual machine's home directory doesn't have any
                storage policy.
            :type  disks: :class:`dict` of :class:`str` and :class:`str`
            :param disks: Storage policies associated with virtual disks. The values in this
                :class:`dict` are storage policy identifiers. They will be
                identifiers for the resource type:com.vmware.vcenter.StoragePolicy
                If the :class:`dict` is empty, the virtual machine does not have
                any disks or its disks are not associated with a storage policy.
                This attribute was added in vSphere API 6.7
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
        'com.vmware.vcenter.vm.storage.policy.info', {
            'vm_home': type.OptionalType(type.IdType()),
            'disks': type.MapType(type.IdType(), type.StringType()),
        },
        Info,
        False,
        None))



    def update(self,
               vm,
               spec,
               ):
        """
        Updates the storage policy configuration of a virtual machine and/or
        its associated virtual hard disks. This method was added in vSphere API
        6.7

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier.
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :type  spec: :class:`Policy.UpdateSpec`
        :param spec: Storage Policy Specification for updating the virtual machine and
            virtual disks.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required priveleges.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the storage policy specified is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the virtual machine or disk is busy performing another
            operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine or disk's configuration state cannot be
            accessed.
        """
        return self._invoke('update',
                            {
                            'vm': vm,
                            'spec': spec,
                            })

    def get(self,
            vm,
            ):
        """
        Returns Information about Storage Policy associated with a virtual
        machine's home directory and/or its virtual hard disks. This method was
        added in vSphere API 6.7

        :type  vm: :class:`str`
        :param vm: Virtual machine identifier
            The parameter must be an identifier for the resource type:
            ``VirtualMachine``.
        :rtype: :class:`Policy.Info`
        :return: Overview of Storage Policy associated with a virtual machine's home
            directory and/or its associated virtual hard disks.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the virtual machine's configuration state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user does not have the required privileges.
        """
        return self._invoke('get',
                            {
                            'vm': vm,
                            })
class _PolicyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
            'spec': type.ReferenceType(__name__, 'Policy.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/vcenter/vm/{vm}/storage/policy',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'vm': type.IdType(resource_types='VirtualMachine'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
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
            url_template='/vcenter/vm/{vm}/storage/policy',
            path_variables={
                'vm': 'vm',
            },
            query_parameters={
            }
        )

        operations = {
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Policy.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'update': update_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.vm.storage.policy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policy': Policy,
        'policy': 'com.vmware.vcenter.vm.storage.policy_client.StubFactory',
    }

