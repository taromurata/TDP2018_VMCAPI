# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.update.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.update_client`` module provides classes for updating
the software in the appliance. The module is available starting in vSphere 6.5.

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


class ServiceInfo(VapiStruct):
    """
    The ``ServiceInfo`` class describes a service to be stopped and started
    during the update installation.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 service=None,
                 description=None,
                ):
        """
        :type  service: :class:`str`
        :param service: Service ID
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.appliance.service``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.appliance.service``.
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Service description
        """
        self.service = service
        self.description = description
        VapiStruct.__init__(self)

ServiceInfo._set_binding_type(type.StructType(
    'com.vmware.appliance.update.service_info', {
        'service': type.IdType(resource_types='com.vmware.appliance.service'),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
    },
    ServiceInfo,
    False,
    None))



class CommonInfo(VapiStruct):
    """
    The ``CommonInfo`` class defines common update information

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 description=None,
                 priority=None,
                 severity=None,
                 update_type=None,
                 release_date=None,
                 reboot_required=None,
                 size=None,
                ):
        """
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Description of the update. The short information what this update
            is. E.g. "Update2 for vCenter Server Appliance 6.5"
        :type  priority: :class:`CommonInfo.Priority`
        :param priority: Update priority
        :type  severity: :class:`CommonInfo.Severity`
        :param severity: Update severity
        :type  update_type: :class:`CommonInfo.Category`
        :param update_type: Update category
        :type  release_date: :class:`datetime.datetime`
        :param release_date: Update release date.
        :type  reboot_required: :class:`bool`
        :param reboot_required: Flag indicating whether reboot is required after update.
        :type  size: :class:`long`
        :param size: Download Size of update in Megabytes.
        """
        self.description = description
        self.priority = priority
        self.severity = severity
        self.update_type = update_type
        self.release_date = release_date
        self.reboot_required = reboot_required
        self.size = size
        VapiStruct.__init__(self)

    class Priority(Enum):
        """
        The ``CommonInfo.Priority`` class defines the update installation priority
        recommendations.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        HIGH = None
        """
        Install ASAP

        """
        MEDIUM = None
        """
        Install at the earliest convenience

        """
        LOW = None
        """
        Install at your discretion

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Priority` instance.
            """
            Enum.__init__(string)

    Priority._set_values([
        Priority('HIGH'),
        Priority('MEDIUM'),
        Priority('LOW'),
    ])
    Priority._set_binding_type(type.EnumType(
        'com.vmware.appliance.update.common_info.priority',
        Priority))

    class Severity(Enum):
        """
        The ``CommonInfo.Severity`` class defines the severity of the issues fixed
        in the update.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        CRITICAL = None
        """
        Vulnerabilities that can be exploited by an unauthenticated attacker from
        the Internet or those that break the guest/host Operating System isolation.
        The exploitation results in the complete compromise of confidentiality,
        integrity, and availability of user data and/or processing resources
        without user interaction. Exploitation could be leveraged to propagate an
        Internet worm or execute arbitrary code between Virtual Machines and/or the
        Host Operating System.

        """
        IMPORTANT = None
        """
        Vulnerabilities that are not rated critical but whose exploitation results
        in the complete compromise of confidentiality and/or integrity of user data
        and/or processing resources through user assistance or by authenticated
        attackers. This rating also applies to those vulnerabilities which could
        lead to the complete compromise of availability when exploitation is by a
        remote unauthenticated attacker from the Internet or through a breach of
        virtual machine isolation.

        """
        MODERATE = None
        """
        Vulnerabilities where the ability to exploit is mitigated to a significant
        degree by configuration or difficulty of exploitation, but in certain
        deployment scenarios could still lead to the compromise of confidentiality,
        integrity, or availability of user data and/or processing resources.

        """
        LOW = None
        """
        All other issues that have a security impact. Vulnerabilities where
        exploitation is believed to be extremely difficult, or where successful
        exploitation would have minimal impact

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Severity` instance.
            """
            Enum.__init__(string)

    Severity._set_values([
        Severity('CRITICAL'),
        Severity('IMPORTANT'),
        Severity('MODERATE'),
        Severity('LOW'),
    ])
    Severity._set_binding_type(type.EnumType(
        'com.vmware.appliance.update.common_info.severity',
        Severity))

    class Category(Enum):
        """
        The ``CommonInfo.Category`` class defines update type

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SECURITY = None
        """
        Fixes vulnerabilities, doesn't change functionality

        """
        FIX = None
        """
        Fixes bugs/vulnerabilities, doesn't change functionality

        """
        UPDATE = None
        """
        Changes product functionality

        """
        UPGRADE = None
        """
        Introduces new features, significantly changes product functionality

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Category` instance.
            """
            Enum.__init__(string)

    Category._set_values([
        Category('SECURITY'),
        Category('FIX'),
        Category('UPDATE'),
        Category('UPGRADE'),
    ])
    Category._set_binding_type(type.EnumType(
        'com.vmware.appliance.update.common_info.category',
        Category))

CommonInfo._set_binding_type(type.StructType(
    'com.vmware.appliance.update.common_info', {
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'priority': type.ReferenceType(__name__, 'CommonInfo.Priority'),
        'severity': type.ReferenceType(__name__, 'CommonInfo.Severity'),
        'update_type': type.ReferenceType(__name__, 'CommonInfo.Category'),
        'release_date': type.DateTimeType(),
        'reboot_required': type.BooleanType(),
        'size': type.IntegerType(),
    },
    CommonInfo,
    False,
    None))



class Summary(VapiStruct):
    """
    The ``Summary`` class contains the essential information about the update

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 description=None,
                 priority=None,
                 severity=None,
                 update_type=None,
                 release_date=None,
                 reboot_required=None,
                 size=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version in form of X.Y.Z.P. e.g. 6.5.1.5400
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``. When methods return a
            value of this class as a return value, the attribute will be an
            identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param description: Description of the update. The short information what this update
            is. E.g. "Update2 for vCenter Server Appliance 6.5"
        :type  priority: :class:`CommonInfo.Priority`
        :param priority: Update priority
        :type  severity: :class:`CommonInfo.Severity`
        :param severity: Update severity
        :type  update_type: :class:`CommonInfo.Category`
        :param update_type: Update category
        :type  release_date: :class:`datetime.datetime`
        :param release_date: Update release date.
        :type  reboot_required: :class:`bool`
        :param reboot_required: Flag indicating whether reboot is required after update.
        :type  size: :class:`long`
        :param size: Download Size of update in Megabytes.
        """
        self.version = version
        self.description = description
        self.priority = priority
        self.severity = severity
        self.update_type = update_type
        self.release_date = release_date
        self.reboot_required = reboot_required
        self.size = size
        VapiStruct.__init__(self)

Summary._set_binding_type(type.StructType(
    'com.vmware.appliance.update.summary', {
        'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
        'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        'priority': type.ReferenceType(__name__, 'CommonInfo.Priority'),
        'severity': type.ReferenceType(__name__, 'CommonInfo.Severity'),
        'update_type': type.ReferenceType(__name__, 'CommonInfo.Category'),
        'release_date': type.DateTimeType(),
        'reboot_required': type.BooleanType(),
        'size': type.IntegerType(),
    },
    Summary,
    False,
    None))



class Policy(VapiInterface):
    """
    The ``Policy`` class provides methods to set/get background check for the
    new updates.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PolicyStub)

    class DayOfWeek(Enum):
        """
        The ``Policy.DayOfWeek`` class defines the set of days

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
        Monday

        """
        TUESDAY = None
        """
        Tuesday

        """
        WEDNESDAY = None
        """
        Wednesday

        """
        THURSDAY = None
        """
        Thursday

        """
        FRIDAY = None
        """
        Friday

        """
        SATURDAY = None
        """
        Saturday

        """
        SUNDAY = None
        """
        Sunday

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
        'com.vmware.appliance.update.policy.day_of_week',
        DayOfWeek))


    class Time(VapiStruct):
        """
        The ``Policy.Time`` class defines weekday and time the automatic check for
        new updates will be run

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     day=None,
                     hour=None,
                     minute=None,
                    ):
            """
            :type  day: :class:`Policy.DayOfWeek`
            :param day: weekday to check for updates.
            :type  hour: :class:`long`
            :param hour: Hour: 0-24
            :type  minute: :class:`long`
            :param minute: Minute: 0-59
            """
            self.day = day
            self.hour = hour
            self.minute = minute
            VapiStruct.__init__(self)

    Time._set_binding_type(type.StructType(
        'com.vmware.appliance.update.policy.time', {
            'day': type.ReferenceType(__name__, 'Policy.DayOfWeek'),
            'hour': type.IntegerType(),
            'minute': type.IntegerType(),
        },
        Time,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Policy.Info`` class defines automatic update checking and staging
        policy.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'custom_URL': 'custom_url',
                                'default_URL': 'default_url',
                                }

        def __init__(self,
                     custom_url=None,
                     default_url=None,
                     username=None,
                     check_schedule=None,
                     auto_stage=None,
                     auto_update=None,
                     manual_control=None,
                    ):
            """
            :type  custom_url: :class:`str` or ``None``
            :param custom_url: Current appliance update custom repository URL.
                If None update is checked at defaut URL.
            :type  default_url: :class:`str`
            :param default_url: Current appliance update default repository URL.
            :type  username: :class:`str` or ``None``
            :param username: Username for the update repository
                If None username will not be used to login
            :type  check_schedule: :class:`list` of :class:`Policy.Time`
            :param check_schedule: Schedule when the automatic check will be run.
            :type  auto_stage: :class:`bool`
            :param auto_stage: Automatically stage the latest update if available.
            :type  auto_update: :class:`bool`
            :param auto_update: Is the appliance updated automatically. If :class:`set` the
                appliance may ignore the check schedule or auto-stage settings.
            :type  manual_control: :class:`bool`
            :param manual_control: Whether API client should allow the user to start update manually
            """
            self.custom_url = custom_url
            self.default_url = default_url
            self.username = username
            self.check_schedule = check_schedule
            self.auto_stage = auto_stage
            self.auto_update = auto_update
            self.manual_control = manual_control
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.update.policy.info', {
            'custom_URL': type.OptionalType(type.StringType()),
            'default_URL': type.StringType(),
            'username': type.OptionalType(type.StringType()),
            'check_schedule': type.ListType(type.ReferenceType(__name__, 'Policy.Time')),
            'auto_stage': type.BooleanType(),
            'auto_update': type.BooleanType(),
            'manual_control': type.BooleanType(),
        },
        Info,
        False,
        None))


    class Config(VapiStruct):
        """
        The ``Policy.Config`` class defines automatic update checking and staging
        policy.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """



        _canonical_to_pep_names = {
                                'custom_URL': 'custom_url',
                                }

        def __init__(self,
                     custom_url=None,
                     username=None,
                     password=None,
                     check_schedule=None,
                     auto_stage=None,
                    ):
            """
            :type  custom_url: :class:`str` or ``None``
            :param custom_url: Current appliance update repository URL.
                If None then default URL is assumed
            :type  username: :class:`str` or ``None``
            :param username: Username for the update repository
                If None username will not be used to login
            :type  password: :class:`str` or ``None``
            :param password: Password for the update repository
                password If None password will not be used to login
            :type  check_schedule: :class:`list` of :class:`Policy.Time`
            :param check_schedule: Schedule when the automatic check will be run.
            :type  auto_stage: :class:`bool`
            :param auto_stage: Automatically stage the latest update if available.
            """
            self.custom_url = custom_url
            self.username = username
            self.password = password
            self.check_schedule = check_schedule
            self.auto_stage = auto_stage
            VapiStruct.__init__(self)

    Config._set_binding_type(type.StructType(
        'com.vmware.appliance.update.policy.config', {
            'custom_URL': type.OptionalType(type.StringType()),
            'username': type.OptionalType(type.StringType()),
            'password': type.OptionalType(type.SecretType()),
            'check_schedule': type.ListType(type.ReferenceType(__name__, 'Policy.Time')),
            'auto_stage': type.BooleanType(),
        },
        Config,
        False,
        None))



    def get(self):
        """
        Gets the automatic update checking and staging policy.


        :rtype: :class:`Policy.Info`
        :return: Structure containing the policy for the appliance update.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        """
        return self._invoke('get', None)

    def set(self,
            policy,
            ):
        """
        Sets the automatic update checking and staging policy.

        :type  policy: :class:`Policy.Config`
        :param policy: Info structure containing the policy for the appliance update.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        """
        return self._invoke('set',
                            {
                            'policy': policy,
                            })
class Pending(VapiInterface):
    """
    The ``Pending`` class provides methods to manipulate pending updates.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PendingStub)

    class SourceType(Enum):
        """
        The ``Pending.SourceType`` class defines the supported types of sources of
        updates.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        LAST_CHECK = None
        """
        Do not perform a new check, return the previous result

        """
        LOCAL = None
        """
        Check the local sources, ISO devices, staged area

        """
        LOCAL_AND_ONLINE = None
        """
        Check the local sources, ISO devices, staged area, then online repository
        as stated in update policy

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SourceType` instance.
            """
            Enum.__init__(string)

    SourceType._set_values([
        SourceType('LAST_CHECK'),
        SourceType('LOCAL'),
        SourceType('LOCAL_AND_ONLINE'),
    ])
    SourceType._set_binding_type(type.EnumType(
        'com.vmware.appliance.update.pending.source_type',
        SourceType))


    class Info(VapiStruct):
        """
        The ``Pending.Info`` class contains the extended information about the
        update

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     contents=None,
                     services_will_be_stopped=None,
                     eulas=None,
                     staged=None,
                     description=None,
                     priority=None,
                     severity=None,
                     update_type=None,
                     release_date=None,
                     reboot_required=None,
                     size=None,
                    ):
            """
            :type  contents: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param contents: List of the 1. issues addressed since previous/current version 2.
                new features/improvements
            :type  services_will_be_stopped: :class:`list` of :class:`ServiceInfo`
            :param services_will_be_stopped: List of the services that will be stopped and restarted during the
                update installation.
            :type  eulas: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param eulas: List of EULAs. This list has multiple entries and can be dynamic
                based on what we are actually installing.
            :type  staged: :class:`bool`
            :param staged: Is the update staged
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the update. The short information what this update
                is. E.g. "Update2 for vCenter Server Appliance 6.5"
            :type  priority: :class:`CommonInfo.Priority`
            :param priority: Update priority
            :type  severity: :class:`CommonInfo.Severity`
            :param severity: Update severity
            :type  update_type: :class:`CommonInfo.Category`
            :param update_type: Update category
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Update release date.
            :type  reboot_required: :class:`bool`
            :param reboot_required: Flag indicating whether reboot is required after update.
            :type  size: :class:`long`
            :param size: Download Size of update in Megabytes.
            """
            self.contents = contents
            self.services_will_be_stopped = services_will_be_stopped
            self.eulas = eulas
            self.staged = staged
            self.description = description
            self.priority = priority
            self.severity = severity
            self.update_type = update_type
            self.release_date = release_date
            self.reboot_required = reboot_required
            self.size = size
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.update.pending.info', {
            'contents': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
            'services_will_be_stopped': type.ListType(type.ReferenceType(__name__, 'ServiceInfo')),
            'eulas': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
            'staged': type.BooleanType(),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'priority': type.ReferenceType(__name__, 'CommonInfo.Priority'),
            'severity': type.ReferenceType(__name__, 'CommonInfo.Severity'),
            'update_type': type.ReferenceType(__name__, 'CommonInfo.Category'),
            'release_date': type.DateTimeType(),
            'reboot_required': type.BooleanType(),
            'size': type.IntegerType(),
        },
        Info,
        False,
        None))


    class Question(VapiStruct):
        """
        The ``Pending.Question`` class describes a item of information that must be
        provided by the user in order to install the update.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'PLAIN_TEXT' : [('allowed_values', False), ('regexp', False), ('default_answer', False)],
                    'BOOLEAN' : [],
                    'PASSWORD' : [],
                }
            ),
        ]



        def __init__(self,
                     data_item=None,
                     text=None,
                     description=None,
                     type=None,
                     allowed_values=None,
                     regexp=None,
                     default_answer=None,
                    ):
            """
            :type  data_item: :class:`str`
            :param data_item: ID of the data item
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.applicance.update.pending.dataitem``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.applicance.update.pending.dataitem``.
            :type  text: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param text: Label for the item to be used in GUI/CLI
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the item
            :type  type: :class:`Pending.Question.InputType`
            :param type: How this field shoudl be represented in GUI or CLI
            :type  allowed_values: :class:`list` of :class:`str` or ``None``
            :param allowed_values: List of allowed values
                allowedValues If None any value is valid.
            :type  regexp: :class:`str` or ``None``
            :param regexp: Regexp to validate the input
                regexp If None no validation will be performed.
            :type  default_answer: :class:`str` or ``None``
            :param default_answer: Default answer
                defaultAnswer If None then there is no default answer, so an
                explicit answer must be provided
            """
            self.data_item = data_item
            self.text = text
            self.description = description
            self.type = type
            self.allowed_values = allowed_values
            self.regexp = regexp
            self.default_answer = default_answer
            VapiStruct.__init__(self)

        class InputType(Enum):
            """
            The ``Pending.Question.InputType`` class defines representation of field
            fields in GUI or CLI

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            PLAIN_TEXT = None
            """
            plain text answer

            """
            BOOLEAN = None
            """
            Yes/No,On/Off,Checkbox answer

            """
            PASSWORD = None
            """
            Password (masked) answer

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`InputType` instance.
                """
                Enum.__init__(string)

        InputType._set_values([
            InputType('PLAIN_TEXT'),
            InputType('BOOLEAN'),
            InputType('PASSWORD'),
        ])
        InputType._set_binding_type(type.EnumType(
            'com.vmware.appliance.update.pending.question.input_type',
            InputType))

    Question._set_binding_type(type.StructType(
        'com.vmware.appliance.update.pending.question', {
            'data_item': type.IdType(resource_types='com.vmware.applicance.update.pending.dataitem'),
            'text': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'type': type.ReferenceType(__name__, 'Pending.Question.InputType'),
            'allowed_values': type.OptionalType(type.ListType(type.StringType())),
            'regexp': type.OptionalType(type.StringType()),
            'default_answer': type.OptionalType(type.StringType()),
        },
        Question,
        False,
        None))


    class PrecheckResult(VapiStruct):
        """
        The ``Pending.PrecheckResult`` class contains estimates of how long it will
        take install and rollback an update as well as a list of possible warnings
        and problems with installing the update.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     check_time=None,
                     estimated_time_to_install=None,
                     estimated_time_to_rollback=None,
                     reboot_required=None,
                     issues=None,
                     questions=None,
                    ):
            """
            :type  check_time: :class:`datetime.datetime`
            :param check_time: Time when this precheck was run
            :type  estimated_time_to_install: :class:`long` or ``None``
            :param estimated_time_to_install: Rough estimate of time to install the update (minutes).
                estimatedTimeToInstall If None N/A
            :type  estimated_time_to_rollback: :class:`long` or ``None``
            :param estimated_time_to_rollback: Rough estimate of time to rollback the update (minutes).
                estimatedTimeToRollback If None N/A
            :type  reboot_required: :class:`bool`
            :param reboot_required: Is reboot required to install the update.
            :type  issues: :class:`com.vmware.appliance_client.Notifications` or ``None``
            :param issues: Lists of the issues and warnings
                issues If None N/A
            :type  questions: :class:`list` of :class:`Pending.Question`
            :param questions: List of questions that must be answered to install the update.
            """
            self.check_time = check_time
            self.estimated_time_to_install = estimated_time_to_install
            self.estimated_time_to_rollback = estimated_time_to_rollback
            self.reboot_required = reboot_required
            self.issues = issues
            self.questions = questions
            VapiStruct.__init__(self)

    PrecheckResult._set_binding_type(type.StructType(
        'com.vmware.appliance.update.pending.precheck_result', {
            'check_time': type.DateTimeType(),
            'estimated_time_to_install': type.OptionalType(type.IntegerType()),
            'estimated_time_to_rollback': type.OptionalType(type.IntegerType()),
            'reboot_required': type.BooleanType(),
            'issues': type.OptionalType(type.ReferenceType('com.vmware.appliance_client', 'Notifications')),
            'questions': type.ListType(type.ReferenceType(__name__, 'Pending.Question')),
        },
        PrecheckResult,
        False,
        None))



    def list(self,
             source_type,
             url=None,
             ):
        """
        Checks if new updates are available.

        :type  source_type: :class:`Pending.SourceType`
        :param source_type: type of the source
        :type  url: :class:`str` or ``None``
        :param url: specific URL to check at
            If None then URL is taken from the policy settings
        :rtype: :class:`list` of :class:`Summary`
        :return: List of the update summaries
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            source is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        """
        return self._invoke('list',
                            {
                            'source_type': source_type,
                            'url': url,
                            })

    def get(self,
            version,
            ):
        """
        Gets update information

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :rtype: :class:`Pending.Info`
        :return: Update
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the update of this version is already installed
        """
        return self._invoke('get',
                            {
                            'version': version,
                            })

    def precheck(self,
                 version,
                 ):
        """
        Runs update precheck

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :rtype: :class:`Pending.PrecheckResult`
        :return: PrecheckResult
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if this version is already installed
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if another operation is in progress
        """
        return self._invoke('precheck',
                            {
                            'version': version,
                            })

    def stage(self,
              version,
              ):
        """
        Starts staging the appliance update. The updates are searched for in
        the following order: staged, CDROM, URL

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the update of this version is already installed
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            the update is already staged
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance update state prevents staging
        """
        return self._invoke('stage',
                            {
                            'version': version,
                            })

    def validate(self,
                 version,
                 user_data,
                 ):
        """
        Validates the user provided data before the update installation.

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :type  user_data: :class:`dict` of :class:`str` and :class:`str`
        :param user_data: map of user provided data with IDs
            The key in the parameter :class:`dict` must be an identifier for
            the resource type:
            ``com.vmware.applicance.update.pending.dataitem``.
        :rtype: :class:`com.vmware.appliance_client.Notifications`
        :return: Issues struct with the issues found during the validation
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the update of this version is already installed
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance update state prevents running an check
        """
        return self._invoke('validate',
                            {
                            'version': version,
                            'user_data': user_data,
                            })

    def install(self,
                version,
                user_data,
                ):
        """
        Starts operation of installing the appliance update. Will fail is the
        update is not staged

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :type  user_data: :class:`dict` of :class:`str` and :class:`str`
        :param user_data: map of user provided data with IDs
            The key in the parameter :class:`dict` must be an identifier for
            the resource type:
            ``com.vmware.applicance.update.pending.dataitem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the update of this version is already installed
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance update state prevents running an update or not staged
        """
        return self._invoke('install',
                            {
                            'version': version,
                            'user_data': user_data,
                            })

    def stage_and_install(self,
                          version,
                          user_data,
                          ):
        """
        Starts operation of installing the appliance update. Will stage update
        if not already staged The updates are searched for in the following
        order: staged, CDROM, URL

        :type  version: :class:`str`
        :param version: Update version
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.update.pending``.
        :type  user_data: :class:`dict` of :class:`str` and :class:`str`
        :param user_data: map of user provided data with IDs
            The key in the parameter :class:`dict` must be an identifier for
            the resource type:
            ``com.vmware.applicance.update.pending.dataitem``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the update is not found
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyInDesiredState` 
            if the update of this version is already installed
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if appliance update state prevents running an update
        """
        return self._invoke('stage_and_install',
                            {
                            'version': version,
                            'user_data': user_data,
                            })
class Staged(VapiInterface):
    """
    The ``Staged`` class provides methods to get the status of the staged
    update.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StagedStub)

    class Info(VapiStruct):
        """
        The ``Staged.Info`` class contains information about the staged update

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     staging_complete=None,
                     version=None,
                     description=None,
                     priority=None,
                     severity=None,
                     update_type=None,
                     release_date=None,
                     reboot_required=None,
                     size=None,
                    ):
            """
            :type  staging_complete: :class:`bool`
            :param staging_complete: Is staging complete
            :type  version: :class:`str`
            :param version: Version in form of X.Y.Z.P. e.g. 6.5.1.5400
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.update.pending``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.appliance.update.pending``.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of the update. The short information what this update
                is. E.g. "Update2 for vCenter Server Appliance 6.5"
            :type  priority: :class:`CommonInfo.Priority`
            :param priority: Update priority
            :type  severity: :class:`CommonInfo.Severity`
            :param severity: Update severity
            :type  update_type: :class:`CommonInfo.Category`
            :param update_type: Update category
            :type  release_date: :class:`datetime.datetime`
            :param release_date: Update release date.
            :type  reboot_required: :class:`bool`
            :param reboot_required: Flag indicating whether reboot is required after update.
            :type  size: :class:`long`
            :param size: Download Size of update in Megabytes.
            """
            self.staging_complete = staging_complete
            self.version = version
            self.description = description
            self.priority = priority
            self.severity = severity
            self.update_type = update_type
            self.release_date = release_date
            self.reboot_required = reboot_required
            self.size = size
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.update.staged.info', {
            'staging_complete': type.BooleanType(),
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
            'description': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
            'priority': type.ReferenceType(__name__, 'CommonInfo.Priority'),
            'severity': type.ReferenceType(__name__, 'CommonInfo.Severity'),
            'update_type': type.ReferenceType(__name__, 'CommonInfo.Category'),
            'release_date': type.DateTimeType(),
            'reboot_required': type.BooleanType(),
            'size': type.IntegerType(),
        },
        Info,
        False,
        None))



    def get(self):
        """
        Gets the current status of the staged update


        :rtype: :class:`Staged.Info`
        :return: Info structure with information about staged update
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if nothing is staged
        """
        return self._invoke('get', None)

    def delete(self):
        """
        Deletes the staged update


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            session is not authenticated
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            session is not authorized to perform this operation
        """
        return self._invoke('delete', None)
class _PolicyStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
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
            url_template='/appliance/update/policy',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for set operation
        set_input_type = type.StructType('operation-input', {
            'policy': type.ReferenceType(__name__, 'Policy.Config'),
        })
        set_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        set_input_value_validator_list = [
        ]
        set_output_validator_list = [
        ]
        set_rest_metadata = OperationRestMetadata(
            http_method='PUT',
            url_template='/appliance/update/policy',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Policy.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'set': {
                'input_type': set_input_type,
                'output_type': type.VoidType(),
                'errors': set_error_dict,
                'input_value_validator_list': set_input_value_validator_list,
                'output_validator_list': set_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'set': set_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.update.policy',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PendingStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'source_type': type.ReferenceType(__name__, 'Pending.SourceType'),
            'url': type.OptionalType(type.StringType()),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/appliance/update/pending',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/update/pending/{version}',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        # properties for precheck operation
        precheck_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
        })
        precheck_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        precheck_input_value_validator_list = [
        ]
        precheck_output_validator_list = [
        ]
        precheck_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/update/pending/{version}?action=precheck',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        # properties for stage operation
        stage_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
        })
        stage_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        stage_input_value_validator_list = [
        ]
        stage_output_validator_list = [
        ]
        stage_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/update/pending/{version}?action=stage',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        # properties for validate operation
        validate_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
            'user_data': type.MapType(type.IdType(), type.StringType()),
        })
        validate_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        validate_input_value_validator_list = [
        ]
        validate_output_validator_list = [
        ]
        validate_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/update/pending/{version}?action=validate',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        # properties for install operation
        install_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
            'user_data': type.MapType(type.IdType(), type.StringType()),
        })
        install_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        install_input_value_validator_list = [
        ]
        install_output_validator_list = [
        ]
        install_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/update/pending/{version}?action=install',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        # properties for stage_and_install operation
        stage_and_install_input_type = type.StructType('operation-input', {
            'version': type.IdType(resource_types='com.vmware.appliance.update.pending'),
            'user_data': type.MapType(type.IdType(), type.StringType()),
        })
        stage_and_install_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.already_in_desired_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyInDesiredState'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        stage_and_install_input_value_validator_list = [
        ]
        stage_and_install_output_validator_list = [
        ]
        stage_and_install_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/update/pending/{version}?action=stage-and-install',
            path_variables={
                'version': 'version',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Pending.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'precheck': {
                'input_type': precheck_input_type,
                'output_type': type.ReferenceType(__name__, 'Pending.PrecheckResult'),
                'errors': precheck_error_dict,
                'input_value_validator_list': precheck_input_value_validator_list,
                'output_validator_list': precheck_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'stage': {
                'input_type': stage_input_type,
                'output_type': type.VoidType(),
                'errors': stage_error_dict,
                'input_value_validator_list': stage_input_value_validator_list,
                'output_validator_list': stage_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'validate': {
                'input_type': validate_input_type,
                'output_type': type.ReferenceType('com.vmware.appliance_client', 'Notifications'),
                'errors': validate_error_dict,
                'input_value_validator_list': validate_input_value_validator_list,
                'output_validator_list': validate_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'install': {
                'input_type': install_input_type,
                'output_type': type.VoidType(),
                'errors': install_error_dict,
                'input_value_validator_list': install_input_value_validator_list,
                'output_validator_list': install_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'stage_and_install': {
                'input_type': stage_and_install_input_type,
                'output_type': type.VoidType(),
                'errors': stage_and_install_error_dict,
                'input_value_validator_list': stage_and_install_input_value_validator_list,
                'output_validator_list': stage_and_install_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'precheck': precheck_rest_metadata,
            'stage': stage_rest_metadata,
            'validate': validate_rest_metadata,
            'install': install_rest_metadata,
            'stage_and_install': stage_and_install_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.update.pending',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _StagedStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/update/staged',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {})
        delete_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = OperationRestMetadata(
            http_method='DELETE',
            url_template='/appliance/update/staged',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Staged.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
            'get': get_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.update.staged',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Policy': Policy,
        'Pending': Pending,
        'Staged': Staged,
    }

