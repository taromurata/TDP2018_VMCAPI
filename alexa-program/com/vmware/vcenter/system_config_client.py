# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.system_config.
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


class DeploymentType(VapiInterface):
    """
    The ``DeploymentType`` class provides methods to get/set the type of the
    appliance. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DeploymentTypeStub)

    class Info(VapiStruct):
        """
        The ``DeploymentType.Info`` class contains the fields used to get the
        appliance type. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                    ):
            """
            :type  type: :class:`com.vmware.vcenter.deployment_client.ApplianceType`
            :param type: The type of the appliance. This attribute was added in vSphere API
                6.7
            """
            self.type = type
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.info', {
            'type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ApplianceType'),
        },
        Info,
        False,
        None))


    class ReconfigureSpec(VapiStruct):
        """
        The ``DeploymentType.ReconfigureSpec`` class contains the fields used to
        get and set the appliance type. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                     remote_psc=None,
                    ):
            """
            :type  type: :class:`com.vmware.vcenter.deployment_client.ApplianceType`
            :param type: The type of the appliance. This attribute was added in vSphere API
                6.7
            :type  remote_psc: :class:`com.vmware.vcenter.deployment_client.RemotePscSpec` or ``None``
            :param remote_psc: External PSC to register with when reconfiguring a VCSA_EMBEDDED
                appliance to a VCSA_EXTERNAL appliance. This attribute was added in
                vSphere API 6.7
                Only required when reconfiguring an VCSA_EMBEDDED node to a
                VCSA_EXTERNAL.
            """
            self.type = type
            self.remote_psc = remote_psc
            VapiStruct.__init__(self)

    ReconfigureSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.deployment_type.reconfigure_spec', {
            'type': type.ReferenceType('com.vmware.vcenter.deployment_client', 'ApplianceType'),
            'remote_psc': type.OptionalType(type.ReferenceType('com.vmware.vcenter.deployment_client', 'RemotePscSpec')),
        },
        ReconfigureSpec,
        False,
        None))



    def get(self):
        """
        Get the type of the vCenter appliance. This method was added in vSphere
        API 6.7


        :rtype: :class:`DeploymentType.Info`
        :return: The type of the vCenter appliance.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance is not in CONFIGURED state.
        """
        return self._invoke('get', None)

    def reconfigure(self,
                    spec,
                    ):
        """
        Reconfigure the type of the vCenter appliance. This method was added in
        vSphere API 6.7

        :type  spec: :class:`DeploymentType.ReconfigureSpec`
        :param spec: ReconfigureSpec to set the appliance type.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the appliance is in CONFIGURED state and if not changing the
            type form VCSA_EMBEDDED to VCSA_EXTERNAL.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if external PSC credentials are not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is not in INITIALIZED or CONFIGURED state.
        """
        return self._invoke('reconfigure',
                            {
                            'spec': spec,
                            })
class PscRegistration(VapiInterface):
    """
    The ``PscRegistration`` class provides methods to get and set the
    PSC_EXTERNAL appliance a VCSA_EXTERNAL appliance is registered with. This
    class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PscRegistrationStub)

    class Info(VapiStruct):
        """
        The ``PscRegistration.Info`` class has fields to specify information about
        the PSC node. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     https_port=None,
                     sso_domain=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: The IP address or DNS resolvable name of the PSC this appliance is
                registered with. This attribute was added in vSphere API 6.7
            :type  https_port: :class:`long`
            :param https_port: The HTTPs port used by the external PSC. This attribute was added
                in vSphere API 6.7
            :type  sso_domain: :class:`str`
            :param sso_domain: The Single Sign-On domain name of the external PSC. This attribute
                was added in vSphere API 6.7
            """
            self.address = address
            self.https_port = https_port
            self.sso_domain = sso_domain
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.system_config.psc_registration.info', {
            'address': type.StringType(),
            'https_port': type.IntegerType(),
            'sso_domain': type.StringType(),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Get information of the PSC that this appliance is registered with. This
        method was added in vSphere API 6.7


        :rtype: :class:`PscRegistration.Info`
        :return: Info structure containing information about the external PSC node
            this appliance is registered with.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is in NOT_INITIALIZED state.
        """
        return self._invoke('get', None)

    def repoint(self,
                spec,
                ):
        """
        Repoint this vCenter Server appliance to a different external PSC. This
        method was added in vSphere API 6.7

        :type  spec: :class:`com.vmware.vcenter.deployment_client.RemotePscSpec`
        :param spec: RemotePscSpec structure containing information about the external
            PSC node to repoint this vCenter Server appliance to.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the passed external PSC credentials is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the passed external PSC is not a replicating with the current
            PSC this appliance is registered with.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if passed arguments are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the current appliance is not of the type VCSA_EXTERNAL.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the appliance is NOT in CONFIGURED state.
        """
        return self._invoke('repoint',
                            {
                            'spec': spec,
                            })
class _DeploymentTypeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/system-config/deployment-type',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for reconfigure operation
        reconfigure_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'DeploymentType.ReconfigureSpec'),
        })
        reconfigure_error_dict = {
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        reconfigure_input_value_validator_list = [
        ]
        reconfigure_output_validator_list = [
        ]
        reconfigure_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/system-config/deployment-type',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'DeploymentType.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reconfigure': {
                'input_type': reconfigure_input_type,
                'output_type': type.VoidType(),
                'errors': reconfigure_error_dict,
                'input_value_validator_list': reconfigure_input_value_validator_list,
                'output_validator_list': reconfigure_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'reconfigure': reconfigure_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.system_config.deployment_type',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PscRegistrationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/system-config/psc-registration',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for repoint operation
        repoint_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.vcenter.deployment_client', 'RemotePscSpec'),
        })
        repoint_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        repoint_input_value_validator_list = [
        ]
        repoint_output_validator_list = [
        ]
        repoint_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/vcenter/system-config/psc-registration',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'PscRegistration.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'repoint': {
                'input_type': repoint_input_type,
                'output_type': type.VoidType(),
                'errors': repoint_error_dict,
                'input_value_validator_list': repoint_input_value_validator_list,
                'output_validator_list': repoint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'repoint': repoint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.system_config.psc_registration',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DeploymentType': DeploymentType,
        'PscRegistration': PscRegistration,
    }

