# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.reconciliation.
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


class Job(VapiInterface):
    """
    The ``Job`` class provides methods to create and get the status of
    reconciliation job. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _JobStub)

    class Status(Enum):
        """
        The ``Job.Status`` class defines the status values that can be reported for
        an operation. This enumeration was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NONE = None
        """
        The operation is not running. This class attribute was added in vSphere API
        6.7

        """
        RUNNING = None
        """
        The operation is in progress. This class attribute was added in vSphere API
        6.7

        """
        SUCCEEDED = None
        """
        The operation completed successfully. This class attribute was added in
        vSphere API 6.7

        """
        FAILED = None
        """
        The operation failed. This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('NONE'),
        Status('RUNNING'),
        Status('SUCCEEDED'),
        Status('FAILED'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.reconciliation.job.status',
        Status))


    class CreateSpec(VapiStruct):
        """
        The ``Job.CreateSpec`` class has the fields to request the start of
        reconciliation job. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     sso_admin_user_name=None,
                     sso_admin_user_password=None,
                     ignore_warnings=None,
                    ):
            """
            :type  sso_admin_user_name: :class:`str` or ``None``
            :param sso_admin_user_name: Administrators username for SSO. This attribute was added in
                vSphere API 6.7
                If None SSO authentication will not be used. If the vCenter Server
                is a management node or an embedded node, authentication is
                required.
            :type  sso_admin_user_password: :class:`str` or ``None``
            :param sso_admin_user_password: Password for SSO admin user. This attribute was added in vSphere
                API 6.7
                If None SSO authentication will not be used. If the vCenter Server
                is a management node or an embedded node, authentication is
                required.
            :type  ignore_warnings: :class:`bool` or ``None``
            :param ignore_warnings: Flag indicating whether warnings should be ignored during
                reconciliation. This attribute was added in vSphere API 6.7
                If None, validation warnings will fail the reconciliation
                operation.
            """
            self.sso_admin_user_name = sso_admin_user_name
            self.sso_admin_user_password = sso_admin_user_password
            self.ignore_warnings = ignore_warnings
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.reconciliation.job.create_spec', {
            'sso_admin_user_name': type.OptionalType(type.StringType()),
            'sso_admin_user_password': type.OptionalType(type.SecretType()),
            'ignore_warnings': type.OptionalType(type.BooleanType()),
        },
        CreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Job.Info`` class represents the reconciliation job information. It
        contains information related to current Status, any associated messages and
        progress as percentage. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'status',
                {
                    'FAILED' : [('error', False), ('start_time', True), ('end_time', True)],
                    'RUNNING' : [('start_time', True)],
                    'SUCCEEDED' : [('start_time', True), ('end_time', True)],
                    'NONE' : [],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     service=None,
                     operation=None,
                     parent=None,
                     target=None,
                     status=None,
                     cancelable=None,
                     error=None,
                     start_time=None,
                     end_time=None,
                     messages=None,
                     progress=None,
                    ):
            """
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the operation associated with the task. This
                attribute was added in vSphere API 6.7
            :type  service: :class:`str`
            :param service: Name of the service containing the operation. This attribute was
                added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.reconciliation.job``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.appliance.recovery.reconciliation.job``.
            :type  operation: :class:`str`
            :param operation: Name of the operation associated with the task. This attribute was
                added in vSphere API 6.7
            :type  parent: :class:`str` or ``None``
            :param parent: Parent of the current task. This attribute was added in vSphere API
                6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.reconciliation.job``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.appliance.recovery.reconciliation.job``.
                This attribute will be None if the task has no parent.
            :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
            :param target: Identifier of the target resource the operation modifies. This
                attribute was added in vSphere API 6.7
                This attribute will be None if the task has multiple targets or no
                target.
            :type  status: :class:`Job.Status`
            :param status: Status of the operation associated with the task. This attribute
                was added in vSphere API 6.7
            :type  cancelable: :class:`bool` or ``None``
            :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
                value may change as the operation progresses. This attribute was
                added in vSphere API 6.7
                If None, the operation cannot be canceled.
            :type  error: :class:`Exception` or ``None``
            :param error: Description of the error if the operation status is "FAILED". This
                attribute was added in vSphere API 6.7
                If None the description of why the operation failed will be
                included in the result of the operation (see null).
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the operation is started. This attribute was added in
                vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of :attr:`Job.Status.RUNNING`,
                :attr:`Job.Status.SUCCEEDED`, or :attr:`Job.Status.FAILED`.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the operation is completed. This attribute was added in
                vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of :attr:`Job.Status.SUCCEEDED` or
                :attr:`Job.Status.FAILED`.
            :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param messages: A list of localized messages. This attribute was added in vSphere
                API 6.7
            :type  progress: :class:`long`
            :param progress: The progress of the job as a percentage. This attribute was added
                in vSphere API 6.7
            """
            self.description = description
            self.service = service
            self.operation = operation
            self.parent = parent
            self.target = target
            self.status = status
            self.cancelable = cancelable
            self.error = error
            self.start_time = start_time
            self.end_time = end_time
            self.messages = messages
            self.progress = progress
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.reconciliation.job.info', {
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'service': type.IdType(resource_types='com.vmware.appliance.recovery.reconciliation.job'),
            'operation': type.StringType(),
            'parent': type.OptionalType(type.IdType()),
            'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
            'status': type.ReferenceType(__name__, 'Job.Status'),
            'cancelable': type.OptionalType(type.BooleanType()),
            'error': type.OptionalType(type.AnyErrorType()),
            'start_time': type.OptionalType(type.DateTimeType()),
            'end_time': type.OptionalType(type.DateTimeType()),
            'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
            'progress': type.IntegerType(),
        },
        Info,
        False,
        None))



    def create(self,
               spec,
               ):
        """
        Initiate reconciliation. This method was added in vSphere API 6.7

        :type  spec: :class:`Job.CreateSpec`
        :param spec: CreateSpec Structure
        :rtype: :class:`Job.Info`
        :return: Info Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            A backup or restore is already in progress.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            Reconciliation is allowed only after restore has finished
            successfully.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('create',
                            {
                            'spec': spec,
                            })

    def get(self):
        """
        Get reconciliation job progress/result. This method was added in
        vSphere API 6.7


        :rtype: :class:`Job.Info`
        :return: Info Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if there is no running reconciliation job.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('get', None)
class _JobStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Job.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'FeatureInUse'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/reconciliation/job',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/recovery/reconciliation/job',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.Info'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.reconciliation.job',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Job': Job,
    }

