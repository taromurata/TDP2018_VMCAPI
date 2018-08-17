# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.cis.task.
#---------------------------------------------------------------------------

"""
The ``com.vmware.cis.task_client`` module provides classes and classes used for
managing tasks.

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

class Status(Enum):
    """
    The ``Status`` class defines the status values that can be reported for an
    operation.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    PENDING = None
    """
    The operation is in pending state.

    """
    RUNNING = None
    """
    The operation is in progress.

    """
    BLOCKED = None
    """
    The operation is blocked.

    """
    SUCCEEDED = None
    """
    The operation completed successfully.

    """
    FAILED = None
    """
    The operation failed.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`Status` instance.
        """
        Enum.__init__(string)

Status._set_values([
    Status('PENDING'),
    Status('RUNNING'),
    Status('BLOCKED'),
    Status('SUCCEEDED'),
    Status('FAILED'),
])
Status._set_binding_type(type.EnumType(
    'com.vmware.cis.task.status',
    Status))




class Progress(VapiStruct):
    """
    The ``Progress`` class contains information describe the progress of an
    operation.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 total=None,
                 completed=None,
                 message=None,
                ):
        """
        :type  total: :class:`long`
        :param total: Total amount of the work for the operation.
        :type  completed: :class:`long`
        :param completed: The amount of work completed for the operation. The value can only
            be incremented.
        :type  message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param message: Message about the work progress.
        """
        self.total = total
        self.completed = completed
        self.message = message
        VapiStruct.__init__(self)

Progress._set_binding_type(type.StructType(
    'com.vmware.cis.task.progress', {
        'total': type.IntegerType(),
        'completed': type.IntegerType(),
        'message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
    },
    Progress,
    False,
    None))



class CommonInfo(VapiStruct):
    """
    The ``CommonInfo`` class contains information common to all tasks.

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
                'BLOCKED' : [('start_time', True)],
                'SUCCEEDED' : [('start_time', True), ('end_time', True)],
                'PENDING' : [],
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
                 user=None,
                ):
        """
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
        :type  status: :class:`Status`
        :param status: Status of the operation associated with the task.
        :type  cancelable: :class:`bool`
        :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
            value may change as the operation progresses.
        :type  error: :class:`Exception` or ``None``
        :param error: Description of the error if the operation status is "FAILED".
            If None the description of why the operation failed will be
            included in the result of the operation (see :attr:`Info.result`).
        :type  start_time: :class:`datetime.datetime`
        :param start_time: Time when the operation is started.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of :attr:`Status.RUNNING`,
            :attr:`Status.BLOCKED`, :attr:`Status.SUCCEEDED`, or
            :attr:`Status.FAILED`.
        :type  end_time: :class:`datetime.datetime`
        :param end_time: Time when the operation is completed.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of :attr:`Status.SUCCEEDED` or
            :attr:`Status.FAILED`.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who performed the operation.
            This attribute will be None if the operation is performed by the
            system.
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
        self.user = user
        VapiStruct.__init__(self)

CommonInfo._set_binding_type(type.StructType(
    'com.vmware.cis.task.common_info', {
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'service': type.IdType(resource_types='com.vmware.vapi.service'),
        'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
        'parent': type.OptionalType(type.IdType()),
        'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        'status': type.ReferenceType(__name__, 'Status'),
        'cancelable': type.BooleanType(),
        'error': type.OptionalType(type.AnyErrorType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'end_time': type.OptionalType(type.DateTimeType()),
        'user': type.OptionalType(type.StringType()),
    },
    CommonInfo,
    False,
    None))



class Info(VapiStruct):
    """
    The ``Info`` class contains information about a task.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'status',
            {
                'RUNNING' : [('progress', True), ('result', False), ('start_time', True)],
                'BLOCKED' : [('progress', True), ('result', False), ('start_time', True)],
                'SUCCEEDED' : [('progress', True), ('result', False), ('start_time', True), ('end_time', True)],
                'FAILED' : [('progress', True), ('result', False), ('error', False), ('start_time', True), ('end_time', True)],
                'PENDING' : [],
            }
        ),
    ]



    def __init__(self,
                 progress=None,
                 result=None,
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
        :type  progress: :class:`Progress`
        :param progress: Progress of the operation.
            This attribute is optional and it is only relevant when the value
            of ``#status`` is one of :attr:`Status.RUNNING`,
            :attr:`Status.BLOCKED`, :attr:`Status.SUCCEEDED`, or
            :attr:`Status.FAILED`.
        :type  result: :class:`DataValue` or ``None``
        :param result: Result of the operation. If an operation reports partial results
            before it completes, this attribute could be :class:`set` before
            the :attr:`CommonInfo.status` has the value
            :attr:`Status.SUCCEEDED`. The value could change as the operation
            progresses.
            This attribute will be None if the operation does not return a
            result or if the result is not available at the current step of the
            operation.
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
        :type  status: :class:`Status`
        :param status: Status of the operation associated with the task.
        :type  cancelable: :class:`bool`
        :param cancelable: Flag to indicate whether or not the operation can be cancelled. The
            value may change as the operation progresses.
        :type  error: :class:`Exception` or ``None``
        :param error: Description of the error if the operation status is "FAILED".
            If None the description of why the operation failed will be
            included in the result of the operation (see :attr:`Info.result`).
        :type  start_time: :class:`datetime.datetime`
        :param start_time: Time when the operation is started.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of :attr:`Status.RUNNING`,
            :attr:`Status.BLOCKED`, :attr:`Status.SUCCEEDED`, or
            :attr:`Status.FAILED`.
        :type  end_time: :class:`datetime.datetime`
        :param end_time: Time when the operation is completed.
            This attribute is optional and it is only relevant when the value
            of ``status`` is one of :attr:`Status.SUCCEEDED` or
            :attr:`Status.FAILED`.
        :type  user: :class:`str` or ``None``
        :param user: Name of the user who performed the operation.
            This attribute will be None if the operation is performed by the
            system.
        """
        self.progress = progress
        self.result = result
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
    'com.vmware.cis.task.info', {
        'progress': type.OptionalType(type.ReferenceType(__name__, 'Progress')),
        'result': type.OptionalType(type.OpaqueType()),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'service': type.IdType(resource_types='com.vmware.vapi.service'),
        'operation': type.IdType(resource_types='com.vmware.vapi.operation'),
        'parent': type.OptionalType(type.IdType()),
        'target': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        'status': type.ReferenceType(__name__, 'Status'),
        'cancelable': type.BooleanType(),
        'error': type.OptionalType(type.AnyErrorType()),
        'start_time': type.OptionalType(type.DateTimeType()),
        'end_time': type.OptionalType(type.DateTimeType()),
        'user': type.OptionalType(type.StringType()),
    },
    Info,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

