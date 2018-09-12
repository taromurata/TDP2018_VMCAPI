# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.backup.job.
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


class Details(VapiInterface):
    """
    The ``Details`` class provides methods to get the details about backup
    jobs. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DetailsStub)

    class Type(Enum):
        """
        The ``Details.Type`` class defines the type of backup job. This enumeration
        was added in vSphere API 6.7

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SCHEDULED = None
        """
        Job type is Scheduled. This class attribute was added in vSphere API 6.7

        """
        MANUAL = None
        """
        Job type is Manual. This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('SCHEDULED'),
        Type('MANUAL'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.job.details.type',
        Type))


    class Info(VapiStruct):
        """
        The ``Details.Info`` class contains information about a backup job. This
        class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'status',
                {
                    'SUCCEEDED' : [('duration', True), ('size', True), ('progress', True), ('start_time', True), ('end_time', True)],
                    'FAILED' : [('duration', True), ('size', True), ('progress', True), ('error', False), ('start_time', True), ('end_time', True)],
                    'RUNNING' : [('duration', True), ('size', True), ('progress', True), ('start_time', True)],
                    'BLOCKED' : [('start_time', True)],
                    'PENDING' : [],
                }
            ),
        ]



        def __init__(self,
                     location=None,
                     duration=None,
                     size=None,
                     progress=None,
                     location_user=None,
                     type=None,
                     messages=None,
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
                     user=None,
                    ):
            """
            :type  location: :class:`str`
            :param location: URL of the backup location. This attribute was added in vSphere API
                6.7
            :type  duration: :class:`long`
            :param duration: Time in seconds since the backup job was started or the time it
                took to complete the backup job. This attribute was added in
                vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``#status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`,
                :attr:`com.vmware.cis.task_client.Status.FAILED`, or
                :attr:`com.vmware.cis.task_client.Status.RUNNING`.
            :type  size: :class:`long`
            :param size: Size of the backup data transferred to remote location. This
                attribute was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``#status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`,
                :attr:`com.vmware.cis.task_client.Status.FAILED`, or
                :attr:`com.vmware.cis.task_client.Status.RUNNING`.
            :type  progress: :class:`com.vmware.cis.task_client.Progress`
            :param progress: Progress of the job. This attribute was added in vSphere API 6.7
                This attribute is optional and it is only relevant when the value
                of ``#status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`,
                :attr:`com.vmware.cis.task_client.Status.FAILED`, or
                :attr:`com.vmware.cis.task_client.Status.RUNNING`.
            :type  location_user: :class:`str`
            :param location_user: The username for the remote backup location. This attribute was
                added in vSphere API 6.7
            :type  type: :class:`Details.Type`
            :param type: Type of the backup job. Indicates whether the backup was started
                manually or as a scheduled backup. This attribute was added in
                vSphere API 6.7
            :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param messages: List of any info/warning/error messages returned by the backup job.
                This attribute was added in vSphere API 6.7
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the operation associated with the task.
            :type  service: :class:`str`
            :param service: Name of the service containing the operation.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.service``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.service``.
            :type  operation: :class:`str`
            :param operation: Name of the operation associated with the task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.operation``.
            :type  parent: :class:`str` or ``None``
            :param parent: Parent of the current task.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.task``. When methods return a value of this class
                as a return value, the attribute will be an identifier for the
                resource type: ``com.vmware.cis.task``.
                This attribute will be None if the task has no parent.
            :type  target: :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
            :param target: Identifier of the target created by the operation or an existing
                one the operation performed on.
                This attribute will be None if the operation has no target or
                multiple targets.
            :type  status: :class:`com.vmware.cis.task_client.Status`
            :param status: Status of the operation associated with the task.
            :type  cancelable: :class:`bool`
            :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
                value may change as the operation progresses.
            :type  error: :class:`Exception` or ``None``
            :param error: Description of the error if the operation status is "FAILED".
                If None the description of why the operation failed will be
                included in the result of the operation (see
                :attr:`com.vmware.cis.task_client.Info.result`).
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the operation is started.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.RUNNING`,
                :attr:`com.vmware.cis.task_client.Status.BLOCKED`,
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED`, or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  end_time: :class:`datetime.datetime`
            :param end_time: Time when the operation is completed.
                This attribute is optional and it is only relevant when the value
                of ``status`` is one of
                :attr:`com.vmware.cis.task_client.Status.SUCCEEDED` or
                :attr:`com.vmware.cis.task_client.Status.FAILED`.
            :type  user: :class:`str` or ``None``
            :param user: Name of the user who performed the operation.
                This attribute will be None if the operation is performed by the
                system.
            """
            self.location = location
            self.duration = duration
            self.size = size
            self.progress = progress
            self.location_user = location_user
            self.type = type
            self.messages = messages
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
            self.user = user
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.details.info', {
            'location': type.URIType(),
            'duration': type.OptionalType(type.IntegerType()),
            'size': type.OptionalType(type.IntegerType()),
            'progress': type.OptionalType(type.ReferenceType('com.vmware.cis.task_client', 'Progress')),
            'location_user': type.StringType(),
            'type': type.ReferenceType(__name__, 'Details.Type'),
            'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'service': type.IdType(resource_types='com.vmware.vapi.service'),
            'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
            'parent': type.OptionalType(type.IdType()),
            'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
            'status': type.ReferenceType('com.vmware.cis.task_client', 'Status'),
            'cancelable': type.BooleanType(),
            'error': type.OptionalType(type.AnyErrorType()),
            'start_time': type.OptionalType(type.DateTimeType()),
            'end_time': type.OptionalType(type.DateTimeType()),
            'user': type.OptionalType(type.StringType()),
        },
        Info,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Details.FilterSpec`` class contains attributes used to filter the
        results when listing backup jobs details (see :func:`Details.list`). This
        class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     jobs=None,
                    ):
            """
            :type  jobs: :class:`set` of :class:`str` or ``None``
            :param jobs: Identifiers of backup jobs that can match the filter. This
                attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.appliance.recovery.backup.job``. When methods return a
                value of this class as a return value, the attribute will contain
                identifiers for the resource type:
                ``com.vmware.appliance.recovery.backup.job``.
                If None the filter will match all the backup jobs.
            """
            self.jobs = jobs
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.details.filter_spec', {
            'jobs': type.OptionalType(type.SetType(type.IdType())),
        },
        FilterSpec,
        False,
        None))



    def list(self,
             filter=None,
             ):
        """
        Returns detailed information about the current and historical backup
        jobs. This method was added in vSphere API 6.7

        :type  filter: :class:`Details.FilterSpec` or ``None``
        :param filter: Specification of matching backup jobs for which information should
            be returned.
            If None, the behavior is equivalent to :class:`Details.FilterSpec`
            with all attributes None which means all the backup jobs match the
            filter.
        :rtype: :class:`dict` of :class:`str` and :class:`Details.Info`
        :return: Map of backup job identifier to Info Structure.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.appliance.recovery.backup.job``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list',
                            {
                            'filter': filter,
                            })
class _DetailsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter': type.OptionalType(type.ReferenceType(__name__, 'Details.FilterSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/recovery/backup/job/details',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Details.Info')),
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
            self, iface_name='com.vmware.appliance.recovery.backup.job.details',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Details': Details,
    }

