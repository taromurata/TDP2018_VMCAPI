# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.backup.
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


class LocationSpec(VapiStruct):
    """
    The ``LocationSpec`` class has fields to represent a location on the backup
    server. This class was added in vSphere API 6.7

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 location=None,
                 location_user=None,
                 location_password=None,
                ):
        """
        :type  location: :class:`str`
        :param location: Backup location URL. This attribute was added in vSphere API 6.7
        :type  location_user: :class:`str` or ``None``
        :param location_user: Username for the given location. This attribute was added in
            vSphere API 6.7
            If None authentication will not be used.
        :type  location_password: :class:`str` or ``None``
        :param location_password: Password for the given location. This attribute was added in
            vSphere API 6.7
            If None authentication will not be used.
        """
        self.location = location
        self.location_user = location_user
        self.location_password = location_password
        VapiStruct.__init__(self)

LocationSpec._set_binding_type(type.StructType(
    'com.vmware.appliance.recovery.backup.location_spec', {
        'location': type.URIType(),
        'location_user': type.OptionalType(type.StringType()),
        'location_password': type.OptionalType(type.SecretType()),
    },
    LocationSpec,
    False,
    None))



class Job(VapiInterface):
    """
    The ``Job`` class provides methods to be performed on a backup job.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _JobStub)

    class ReturnStatus(Enum):
        """
        The ``Job.ReturnStatus`` class defines the return type for the cancel
        operation. You specify the return status when you return the result of
        cancel job. See :class:`Job.ReturnResult`.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FAIL = None
        """
        Cancel operation failed.

        """
        WARNING = None
        """
        Cancel operation passed with warnings.

        """
        OK = None
        """
        Cancel operation succeeded.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ReturnStatus` instance.
            """
            Enum.__init__(string)

    ReturnStatus._set_values([
        ReturnStatus('FAIL'),
        ReturnStatus('WARNING'),
        ReturnStatus('OK'),
    ])
    ReturnStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.job.return_status',
        ReturnStatus))


    class LocationType(Enum):
        """
        The ``Job.LocationType`` class defines the type of destination location for
        backup/restore. You specify the location type when you create a backup job.
        See :class:`Job.BackupRequest`.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FTP = None
        """
        Destination is FTP server.

        """
        HTTP = None
        """
        Destination is HTTP server.

        """
        FTPS = None
        """
        Destination is FTPS server.

        """
        HTTPS = None
        """
        Destination is HTTPS server.

        """
        SCP = None
        """
        Destination is SSH server.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`LocationType` instance.
            """
            Enum.__init__(string)

    LocationType._set_values([
        LocationType('FTP'),
        LocationType('HTTP'),
        LocationType('FTPS'),
        LocationType('HTTPS'),
        LocationType('SCP'),
    ])
    LocationType._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.job.location_type',
        LocationType))


    class BackupRestoreProcessState(Enum):
        """
        The ``Job.BackupRestoreProcessState`` class defines the possible states of
        a backup/restore process.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FAILED = None
        """
        Backup/Restore job failed.

        """
        INPROGRESS = None
        """
        Backup/Restore job is in progress.

        """
        NONE = None
        """
        Backup/Restore job is not started.

        """
        SUCCEEDED = None
        """
        Backup/Restore job completed successfully.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BackupRestoreProcessState` instance.
            """
            Enum.__init__(string)

    BackupRestoreProcessState._set_values([
        BackupRestoreProcessState('FAILED'),
        BackupRestoreProcessState('INPROGRESS'),
        BackupRestoreProcessState('NONE'),
        BackupRestoreProcessState('SUCCEEDED'),
    ])
    BackupRestoreProcessState._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.job.backup_restore_process_state',
        BackupRestoreProcessState))


    class LocalizableMessage(VapiStruct):
        """
        The ``Job.LocalizableMessage`` class represents a localizable message.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     default_message=None,
                     args=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: Id in message bundle.
            :type  default_message: :class:`str`
            :param default_message: Text in english.
            :type  args: :class:`list` of :class:`str`
            :param args: Nested data.
            """
            self.id = id
            self.default_message = default_message
            self.args = args
            VapiStruct.__init__(self)

    LocalizableMessage._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class ReturnResult(VapiStruct):
        """
        The ``Job.ReturnResult`` class contains the result information for the
        cancel operation.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Job.ReturnStatus`
            :param status: Status of the cancel operation.
            :type  messages: :class:`list` of :class:`Job.LocalizableMessage`
            :param messages: List of messages.
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    ReturnResult._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.return_result', {
            'status': type.ReferenceType(__name__, 'Job.ReturnStatus'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Job.LocalizableMessage')),
        },
        ReturnResult,
        False,
        None))


    class BackupRequest(VapiStruct):
        """
        The ``Job.BackupRequest`` class represents a requested backup piece.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     parts=None,
                     backup_password=None,
                     location_type=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     comment=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str`
            :param parts: List of optional parts that will be included in the backup. Use the
                :func:`Parts.list` method to get information about the supported
                parts.
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: Password for a backup piece. The backupPassword must adhere to the
                following password requirements: At least 8 characters, cannot be
                more than 20 characters in length. At least 1 uppercase letter. At
                least 1 lowercase letter. At least 1 numeric digit. At least 1
                special character (i.e. any character not in [0-9,a-z,A-Z]). Only
                visible ASCII characters (for example, no space).
                backupPassword If no password then the piece will not be encrypted
            :type  location_type: :class:`Job.LocationType`
            :param location_type: Type of backup location.
            :type  location: :class:`str`
            :param location: Path or URL of the backup location.
            :type  location_user: :class:`str` or ``None``
            :param location_user: Username for the given location.
                If None authentication will not be used for the specified location.
            :type  location_password: :class:`str` or ``None``
            :param location_password: Password for the given location.
                If None authentication will not be used for the specified location.
            :type  comment: :class:`str` or ``None``
            :param comment: Custom comment provided by the user.
                If None comment will be empty.
            """
            self.parts = parts
            self.backup_password = backup_password
            self.location_type = location_type
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.comment = comment
            VapiStruct.__init__(self)

    BackupRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.backup_request', {
            'parts': type.ListType(type.StringType()),
            'backup_password': type.OptionalType(type.SecretType()),
            'location_type': type.ReferenceType(__name__, 'Job.LocationType'),
            'location': type.StringType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'comment': type.OptionalType(type.StringType()),
        },
        BackupRequest,
        False,
        None))


    class BackupJobStatus(VapiStruct):
        """
        The ``Job.BackupJobStatus`` class represents the status of a backup/restore
        job.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     state=None,
                     messages=None,
                     progress=None,
                     start_time=None,
                     end_time=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: TimeStamp based ID.
            :type  state: :class:`Job.BackupRestoreProcessState`
            :param state: The state of the backup job.
            :type  messages: :class:`list` of :class:`Job.LocalizableMessage`
            :param messages: List of messages.
            :type  progress: :class:`long`
            :param progress: Progress of the job in percentage.
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time when the backup was started.
            :type  end_time: :class:`datetime.datetime` or ``None``
            :param end_time: Time when the backup was finished.
                If None end time is None until backup is finished.
            """
            self.id = id
            self.state = state
            self.messages = messages
            self.progress = progress
            self.start_time = start_time
            self.end_time = end_time
            VapiStruct.__init__(self)

    BackupJobStatus._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.job.backup_job_status', {
            'id': type.StringType(),
            'state': type.ReferenceType(__name__, 'Job.BackupRestoreProcessState'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Job.LocalizableMessage')),
            'progress': type.IntegerType(),
            'start_time': type.DateTimeType(),
            'end_time': type.OptionalType(type.DateTimeType()),
        },
        BackupJobStatus,
        False,
        None))



    def cancel(self,
               id,
               ):
        """
        Cancel the backup job.

        :type  id: :class:`str`
        :param id: ID (ID of job)
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :rtype: :class:`Job.ReturnResult`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if backup associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('cancel',
                            {
                            'id': id,
                            })

    def create(self,
               piece,
               ):
        """
        Initiate backup.

        :type  piece: :class:`Job.BackupRequest`
        :param piece: BackupRequest Structure
        :rtype: :class:`Job.BackupJobStatus`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            A backup or restore is already in progress.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('create',
                            {
                            'piece': piece,
                            })

    def list(self):
        """
        Get list of backup jobs


        :rtype: :class:`list` of :class:`str`
        :return: list of BackupJob IDs
            The return value will contain identifiers for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list', None)

    def get(self,
            id,
            ):
        """
        See backup job progress/result.

        :type  id: :class:`str`
        :param id: ID (ID of job)
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.job``.
        :rtype: :class:`Job.BackupJobStatus`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if backup associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('get',
                            {
                            'id': id,
                            })
class Parts(VapiInterface):
    """
    ``Parts`` class provides methods Provides list of parts optional for the
    backup
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PartsStub)

    class LocalizableMessage(VapiStruct):
        """
        ``Parts.LocalizableMessage`` class Structure representing message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     default_message=None,
                     args=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: id in message bundle
            :type  default_message: :class:`str`
            :param default_message: text in english
            :type  args: :class:`list` of :class:`str`
            :param args: nested data
            """
            self.id = id
            self.default_message = default_message
            self.args = args
            VapiStruct.__init__(self)

    LocalizableMessage._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.parts.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class Part(VapiStruct):
        """
        ``Parts.Part`` class Structure representing backup restore part

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     name=None,
                     description=None,
                     selected_by_default=None,
                     optional=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: part ID
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.parts``. When methods return
                a value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.parts``.
            :type  name: :class:`Parts.LocalizableMessage`
            :param name: part name id in message bundle
            :type  description: :class:`Parts.LocalizableMessage`
            :param description: part description id in message bundle
            :type  selected_by_default: :class:`bool`
            :param selected_by_default: Is this part selected by default in the user interface.
            :type  optional: :class:`bool`
            :param optional: Is this part optional.
            """
            self.id = id
            self.name = name
            self.description = description
            self.selected_by_default = selected_by_default
            self.optional = optional
            VapiStruct.__init__(self)

    Part._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.parts.part', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.parts'),
            'name': type.ReferenceType(__name__, 'Parts.LocalizableMessage'),
            'description': type.ReferenceType(__name__, 'Parts.LocalizableMessage'),
            'selected_by_default': type.BooleanType(),
            'optional': type.BooleanType(),
        },
        Part,
        False,
        None))



    def list(self):
        """
        Gets a list of the backup parts.


        :rtype: :class:`list` of :class:`Parts.Part`
        :return: Information about each of the backup parts.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list', None)

    def get(self,
            id,
            ):
        """
        Gets the size (in MB) of the part.

        :type  id: :class:`str`
        :param id: Identifier of the part.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.parts``.
        :rtype: :class:`long`
        :return: long Size of the part in megabytes.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('get',
                            {
                            'id': id,
                            })
class Schedules(VapiInterface):
    """
    The ``Schedules`` class provides methods to be performed to manage backup
    schedules. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SchedulesStub)

    class DayOfWeek(Enum):
        """
        The ``Schedules.DayOfWeek`` class defines the set of days when backup can
        be scheduled. The days can be specified as a list of individual days. You
        specify the days when you set the recurrence for a schedule. See
        :attr:`Schedules.RecurrenceInfo.days`. This enumeration was added in
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
        MONDAY = None
        """
        Monday. This class attribute was added in vSphere API 6.7

        """
        TUESDAY = None
        """
        Tuesday. This class attribute was added in vSphere API 6.7

        """
        WEDNESDAY = None
        """
        Wednesday. This class attribute was added in vSphere API 6.7

        """
        THURSDAY = None
        """
        Thursday. This class attribute was added in vSphere API 6.7

        """
        FRIDAY = None
        """
        Friday. This class attribute was added in vSphere API 6.7

        """
        SATURDAY = None
        """
        Saturday. This class attribute was added in vSphere API 6.7

        """
        SUNDAY = None
        """
        Sunday. This class attribute was added in vSphere API 6.7

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`DayOfWeek` instance.
            """
            Enum.__init__(string)

    DayOfWeek._set_values([
        DayOfWeek('MONDAY'),
        DayOfWeek('TUESDAY'),
        DayOfWeek('WEDNESDAY'),
        DayOfWeek('THURSDAY'),
        DayOfWeek('FRIDAY'),
        DayOfWeek('SATURDAY'),
        DayOfWeek('SUNDAY'),
    ])
    DayOfWeek._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.schedules.day_of_week',
        DayOfWeek))


    class RetentionInfo(VapiStruct):
        """
        The ``Schedules.RetentionInfo`` class contains retention information
        associated with a schedule. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     max_count=None,
                    ):
            """
            :type  max_count: :class:`long`
            :param max_count: Number of backups which should be retained. If retention is not
                set, all the backups will be retained forever. This attribute was
                added in vSphere API 6.7
            """
            self.max_count = max_count
            VapiStruct.__init__(self)

    RetentionInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.schedules.retention_info', {
            'max_count': type.IntegerType(),
        },
        RetentionInfo,
        False,
        None))


    class RecurrenceInfo(VapiStruct):
        """
        The ``Schedules.RecurrenceInfo`` class contains the recurrence information
        associated with a schedule. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     minute=None,
                     hour=None,
                     days=None,
                    ):
            """
            :type  minute: :class:`long`
            :param minute: Minute when backup should run. This attribute was added in vSphere
                API 6.7
            :type  hour: :class:`long`
            :param hour: Hour when backup should run. The hour should be specified in
                24-hour clock format. This attribute was added in vSphere API 6.7
            :type  days: :class:`list` of :class:`Schedules.DayOfWeek` or ``None``
            :param days: Day of week when the backup should be run. Days can be specified as
                list of days. This attribute was added in vSphere API 6.7
                If None the backup will be run everyday.
            """
            self.minute = minute
            self.hour = hour
            self.days = days
            VapiStruct.__init__(self)

    RecurrenceInfo._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.schedules.recurrence_info', {
            'minute': type.IntegerType(),
            'hour': type.IntegerType(),
            'days': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'Schedules.DayOfWeek'))),
        },
        RecurrenceInfo,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Schedules.CreateSpec`` class contains fields to be specified for
        creating a new schedule. The structure includes parts, location
        information, encryption password and enable flag. This class was added in
        vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     parts=None,
                     backup_password=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     enable=None,
                     recurrence_info=None,
                     retention_info=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str` or ``None``
            :param parts: List of optional parts to be backed up. Use the :func:`Parts.list`
                method to get information about the supported parts. This attribute
                was added in vSphere API 6.7
                If None all the optional parts will not be backed up.
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: Password for a backup piece. The backupPassword must adhere to the
                following password requirements: At least 8 characters, cannot be
                more than 20 characters in length. At least 1 uppercase letter. At
                least 1 lowercase letter. At least 1 numeric digit. At least 1
                special character (i.e. any character not in [0-9,a-z,A-Z]). Only
                visible ASCII characters (for example, no space). This attribute
                was added in vSphere API 6.7
                If None the backup piece will not be encrypted.
            :type  location: :class:`str`
            :param location: URL of the backup location. This attribute was added in vSphere API
                6.7
            :type  location_user: :class:`str` or ``None``
            :param location_user: Username for the given location. This attribute was added in
                vSphere API 6.7
                If None authentication will not be used for the specified location.
            :type  location_password: :class:`str` or ``None``
            :param location_password: Password for the given location. This attribute was added in
                vSphere API 6.7
                If None authentication will not be used for the specified location.
            :type  enable: :class:`bool` or ``None``
            :param enable: Enable or disable a schedule. This attribute was added in vSphere
                API 6.7
                If None the schedule will be enabled.
            :type  recurrence_info: :class:`Schedules.RecurrenceInfo` or ``None``
            :param recurrence_info: Recurrence information for the schedule. This attribute was added
                in vSphere API 6.7
                If None backup job will not be scheduled. See
                :class:`Schedules.RecurrenceInfo`
            :type  retention_info: :class:`Schedules.RetentionInfo` or ``None``
            :param retention_info: Retention information for the schedule. This attribute was added in
                vSphere API 6.7
                If None all the completed backup jobs will be retained forever. See
                :class:`Schedules.RetentionInfo`
            """
            self.parts = parts
            self.backup_password = backup_password
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.enable = enable
            self.recurrence_info = recurrence_info
            self.retention_info = retention_info
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.schedules.create_spec', {
            'parts': type.OptionalType(type.ListType(type.StringType())),
            'backup_password': type.OptionalType(type.SecretType()),
            'location': type.URIType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'enable': type.OptionalType(type.BooleanType()),
            'recurrence_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RecurrenceInfo')),
            'retention_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RetentionInfo')),
        },
        CreateSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Schedules.Info`` class contains information about an existing
        schedule. The structure includes Schedule ID, parts, location information,
        encryption password, enable flag, recurrence and retention information.
        This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     parts=None,
                     location=None,
                     location_user=None,
                     enable=None,
                     recurrence_info=None,
                     retention_info=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str`
            :param parts: List of optional parts that will be included in backups based on
                this schedule details. Use the :func:`Parts.list` method to get
                information about the supported parts. This attribute was added in
                vSphere API 6.7
            :type  location: :class:`str`
            :param location: URL of the backup location. This attribute was added in vSphere API
                6.7
            :type  location_user: :class:`str` or ``None``
            :param location_user: Username for the given location. This attribute was added in
                vSphere API 6.7
                If None location user will not be used.
            :type  enable: :class:`bool`
            :param enable: Enable or disable a schedule, by default when created a schedule
                will be enabled. This attribute was added in vSphere API 6.7
            :type  recurrence_info: :class:`Schedules.RecurrenceInfo` or ``None``
            :param recurrence_info: Recurrence information for the schedule. This attribute was added
                in vSphere API 6.7
                If None backup job is not scheduled. See
                :class:`Schedules.RecurrenceInfo`
            :type  retention_info: :class:`Schedules.RetentionInfo` or ``None``
            :param retention_info: Retention information for the schedule. This attribute was added in
                vSphere API 6.7
                If None all the completed backup jobs are retained forever. See
                :class:`Schedules.RetentionInfo`
            """
            self.parts = parts
            self.location = location
            self.location_user = location_user
            self.enable = enable
            self.recurrence_info = recurrence_info
            self.retention_info = retention_info
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.schedules.info', {
            'parts': type.ListType(type.StringType()),
            'location': type.URIType(),
            'location_user': type.OptionalType(type.StringType()),
            'enable': type.BooleanType(),
            'recurrence_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RecurrenceInfo')),
            'retention_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RetentionInfo')),
        },
        Info,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Schedules.UpdateSpec`` class contains the fields of the existing
        schedule which can be updated. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     parts=None,
                     backup_password=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     enable=None,
                     recurrence_info=None,
                     retention_info=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str` or ``None``
            :param parts: List of optional parts. Use the :func:`Parts.list` method to get
                information about the supported parts. This attribute was added in
                vSphere API 6.7
                If None the value will not be changed.
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: Password for a backup piece. The backupPassword must adhere to the
                following password requirements: At least 8 characters, cannot be
                more than 20 characters in length. At least 1 uppercase letter. At
                least 1 lowercase letter. At least 1 numeric digit. At least 1
                special character (i.e. any character not in [0-9,a-z,A-Z]). Only
                visible ASCII characters (for example, no space). This attribute
                was added in vSphere API 6.7
                If None the value will not be changed.
            :type  location: :class:`str` or ``None``
            :param location: URL of the backup location. This attribute was added in vSphere API
                6.7
                If None the value will not be changed.
            :type  location_user: :class:`str` or ``None``
            :param location_user: Username for the given location. This attribute was added in
                vSphere API 6.7
                If None the value will not be changed.
            :type  location_password: :class:`str` or ``None``
            :param location_password: Password for the given location. This attribute was added in
                vSphere API 6.7
                If None the value will not be changed.
            :type  enable: :class:`bool` or ``None``
            :param enable: Enable or disable a schedule. This attribute was added in vSphere
                API 6.7
                If None the value will not be changed.
            :type  recurrence_info: :class:`Schedules.RecurrenceInfo` or ``None``
            :param recurrence_info: Recurrence information for the schedule. This attribute was added
                in vSphere API 6.7
                If None the infomration will not be changed. See
                :class:`Schedules.RecurrenceInfo`
            :type  retention_info: :class:`Schedules.RetentionInfo` or ``None``
            :param retention_info: Retention information for the schedule. This attribute was added in
                vSphere API 6.7
                If None the information will not be changed. See
                :class:`Schedules.RetentionInfo`
            """
            self.parts = parts
            self.backup_password = backup_password
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.enable = enable
            self.recurrence_info = recurrence_info
            self.retention_info = retention_info
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.schedules.update_spec', {
            'parts': type.OptionalType(type.ListType(type.StringType())),
            'backup_password': type.OptionalType(type.SecretType()),
            'location': type.OptionalType(type.URIType()),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'enable': type.OptionalType(type.BooleanType()),
            'recurrence_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RecurrenceInfo')),
            'retention_info': type.OptionalType(type.ReferenceType(__name__, 'Schedules.RetentionInfo')),
        },
        UpdateSpec,
        False,
        None))



    def list(self):
        """
        Returns a list of existing schedules with details. This method was
        added in vSphere API 6.7


        :rtype: :class:`dict` of :class:`str` and :class:`Schedules.Info`
        :return: Map of schedule id to Info Structure
            The key in the return value :class:`dict` will be an identifier for
            the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list', None)

    def run(self,
            schedule,
            comment=None,
            ):
        """
        Initiate backup with the specified schedule. This method was added in
        vSphere API 6.7

        :type  schedule: :class:`str`
        :param schedule: Identifier of the schedule
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :type  comment: :class:`str` or ``None``
        :param comment: field that specifies the description for the backup.
            If None the backup will have an empty comment.
        :rtype: :class:`Job.BackupJobStatus`
        :return: BackupJobStatus Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            if a backup or restore is already in progress.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if schedule associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('run',
                            {
                            'schedule': schedule,
                            'comment': comment,
                            })

    def get(self,
            schedule,
            ):
        """
        Returns an existing schedule information based on id. This method was
        added in vSphere API 6.7

        :type  schedule: :class:`str`
        :param schedule: Identifier of the schedule
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :rtype: :class:`Schedules.Info`
        :return: Info Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if schedule associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('get',
                            {
                            'schedule': schedule,
                            })

    def create(self,
               schedule,
               spec,
               ):
        """
        Creates a schedule. This method was added in vSphere API 6.7

        :type  schedule: :class:`str`
        :param schedule: Identifier of the schedule
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :type  spec: :class:`Schedules.CreateSpec`
        :param spec: CreateSpec Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if provided with invalid schedule specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the schedule with the given id already exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('create',
                            {
                            'schedule': schedule,
                            'spec': spec,
                            })

    def update(self,
               schedule,
               spec,
               ):
        """
        Updates a schedule. This method was added in vSphere API 6.7

        :type  schedule: :class:`str`
        :param schedule: Identifier of the schedule
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :type  spec: :class:`Schedules.UpdateSpec`
        :param spec: UpdateSpec Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if provided with invalid schedule specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if schedule associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('update',
                            {
                            'schedule': schedule,
                            'spec': spec,
                            })

    def delete(self,
               schedule,
               ):
        """
        Deletes an existing schedule. This method was added in vSphere API 6.7

        :type  schedule: :class:`str`
        :param schedule: Identifier of the schedule
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.schedule``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if schedule associated with id does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('delete',
                            {
                            'schedule': schedule,
                            })
class SystemName(VapiInterface):
    """
    The ``SystemName`` class provides methods to enumerate system names of
    appliance backups. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SystemNameStub)


    def list(self,
             loc_spec,
             ):
        """
        Returns a list of system names for which backup archives exist under
        ``loc_spec``. This method was added in vSphere API 6.7

        :type  loc_spec: :class:`LocationSpec`
        :param loc_spec: LocationSpec Structure
        :rtype: :class:`list` of :class:`str`
        :return: list of system names
            The return value will contain identifiers for the resource type:
            ``com.vmware.appliance.recovery.backup.system_name``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``loc_spec`` doesn't refer to an existing location on the backup
            server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list',
                            {
                            'loc_spec': loc_spec,
                            })
class _JobStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.job'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/backup/job/{id}/cancel',
            path_variables={
                'id': 'id',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'piece': type.ReferenceType(__name__, 'Job.BackupRequest'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'FeatureInUse'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/backup/job',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/appliance/recovery/backup/job',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.job'),
        })
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
            url_template='/appliance/recovery/backup/job/{id}',
            path_variables={
                'id': 'id',
            },
            query_parameters={
            }
        )

        operations = {
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.ReturnResult'),
                'errors': cancel_error_dict,
                'input_value_validator_list': cancel_input_value_validator_list,
                'output_validator_list': cancel_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.BackupJobStatus'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.BackupJobStatus'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'cancel': cancel_rest_metadata,
            'create': create_rest_metadata,
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.backup.job',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PartsStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/appliance/recovery/backup/parts',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'id': type.IdType(resource_types='com.vmware.appliance.recovery.backup.parts'),
        })
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
            url_template='/appliance/recovery/backup/parts/{id}',
            path_variables={
                'id': 'id',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Parts.Part')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.IntegerType(),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.backup.parts',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SchedulesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
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
            url_template='/appliance/recovery/backup/schedules',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for run operation
        run_input_type = type.StructType('operation-input', {
            'schedule': type.IdType(resource_types='com.vmware.appliance.recovery.backup.schedule'),
            'comment': type.OptionalType(type.StringType()),
        })
        run_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'FeatureInUse'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        run_input_value_validator_list = [
        ]
        run_output_validator_list = [
        ]
        run_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/backup/schedules/{schedule}?action=run',
            path_variables={
                'schedule': 'schedule',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'schedule': type.IdType(resource_types='com.vmware.appliance.recovery.backup.schedule'),
        })
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
            url_template='/appliance/recovery/backup/schedules/{schedule}',
            path_variables={
                'schedule': 'schedule',
            },
            query_parameters={
            }
        )

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'schedule': type.IdType(resource_types='com.vmware.appliance.recovery.backup.schedule'),
            'spec': type.ReferenceType(__name__, 'Schedules.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/backup/schedules/{schedule}',
            path_variables={
                'schedule': 'schedule',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'schedule': type.IdType(resource_types='com.vmware.appliance.recovery.backup.schedule'),
            'spec': type.ReferenceType(__name__, 'Schedules.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/recovery/backup/schedules/update/{schedule}',
            path_variables={
                'schedule': 'schedule',
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'schedule': type.IdType(resource_types='com.vmware.appliance.recovery.backup.schedule'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/appliance/recovery/backup/schedules/{schedule}',
            path_variables={
                'schedule': 'schedule',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Schedules.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'run': {
                'input_type': run_input_type,
                'output_type': type.ReferenceType(__name__, 'Job.BackupJobStatus'),
                'errors': run_error_dict,
                'input_value_validator_list': run_input_value_validator_list,
                'output_validator_list': run_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Schedules.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'run': run_rest_metadata,
            'get': get_rest_metadata,
            'create': create_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.backup.schedules',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SystemNameStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'loc_spec': type.ReferenceType(__name__, 'LocationSpec'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/recovery/backup/system-name',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
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
            self, iface_name='com.vmware.appliance.recovery.backup.system_name',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Job': Job,
        'Parts': Parts,
        'Schedules': Schedules,
        'SystemName': SystemName,
        'job': 'com.vmware.appliance.recovery.backup.job_client.StubFactory',
        'system_name': 'com.vmware.appliance.recovery.backup.system_name_client.StubFactory',
    }

