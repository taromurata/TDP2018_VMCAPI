# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.hvc.links.sync.
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


class Providers(VapiInterface):
    """
    The ``Providers`` class provides methods to create a sync session, get
    information on Sync. **Warning:** This class is available as technical
    preview. It may be changed in a future release.
    """
    RESOURCE_TYPE = "com.vmware.vcenter.hvc.links.sync.Providers"
    """
    Resource type for Sync Providers. **Warning:** This class attribute is
    available as technical preview. It may be changed in a future release.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ProvidersStub)

    class Status(Enum):
        """
        The ``Providers.Status`` class defines valid sync status. **Warning:** This
        enumeration is available as technical preview. It may be changed in a
        future release.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SUCCEEDED = None
        """
        If Sync was successful. **Warning:** This class attribute is available as
        technical preview. It may be changed in a future release.

        """
        FAILED = None
        """
        If Sync failed. **Warning:** This class attribute is available as technical
        preview. It may be changed in a future release.

        """
        NO_SYNC_FOUND = None
        """
        If Sync has not been triggered. **Warning:** This class attribute is
        available as technical preview. It may be changed in a future release.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Status` instance.
            """
            Enum.__init__(string)

    Status._set_values([
        Status('SUCCEEDED'),
        Status('FAILED'),
        Status('NO_SYNC_FOUND'),
    ])
    Status._set_binding_type(type.EnumType(
        'com.vmware.vcenter.hvc.links.sync.providers.status',
        Status))


    class Info(VapiStruct):
        """
        The ``Providers.Info`` class contains information about sync for a
        provider. **Warning:** This class is available as technical preview. It may
        be changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'status',
                {
                    'FAILED' : [('status_message', True)],
                    'SUCCEEDED' : [],
                    'NO_SYNC_FOUND' : [],
                }
            ),
        ]



        def __init__(self,
                     last_sync_time=None,
                     status=None,
                     polling_interval_in_seconds=None,
                     current_session_info=None,
                     status_message=None,
                    ):
            """
            :type  last_sync_time: :class:`datetime.datetime` or ``None``
            :param last_sync_time: Last sync time for the provider. This indicates the last time that
                either a background sync or a force sync was started for the
                provider. **Warning:** This attribute is available as technical
                preview. It may be changed in a future release.
                If None no sync was found for the provider.
            :type  status: :class:`Providers.Status`
            :param status: Last Sync status for the provider. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  polling_interval_in_seconds: :class:`long`
            :param polling_interval_in_seconds: Sync Polling interval between local and remote replicas for the
                provider. **Warning:** This attribute is available as technical
                preview. It may be changed in a future release.
            :type  current_session_info: :class:`Providers.SessionInfo` or ``None``
            :param current_session_info: Returns information on the forced sync for the provider.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                If None there is no outstanding sync session created for this
                provider
            :type  status_message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param status_message: Localizable messages associated with sync status. **Warning:** This
                attribute is available as technical preview. It may be changed in a
                future release.
                This attribute is optional and it is only relevant when the value
                of ``status`` is :attr:`Providers.Status.FAILED`.
            """
            self.last_sync_time = last_sync_time
            self.status = status
            self.polling_interval_in_seconds = polling_interval_in_seconds
            self.current_session_info = current_session_info
            self.status_message = status_message
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.sync.providers.info', {
            'last_sync_time': type.OptionalType(type.DateTimeType()),
            'status': type.ReferenceType(__name__, 'Providers.Status'),
            'polling_interval_in_seconds': type.IntegerType(),
            'current_session_info': type.OptionalType(type.ReferenceType(__name__, 'Providers.SessionInfo')),
            'status_message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Info,
        False,
        None))


    class SessionInfo(VapiStruct):
        """
        The ``Providers.SessionInfo`` class contains sync session information.
        **Warning:** This class is available as technical preview. It may be
        changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'stage',
                {
                    'FAILED' : [('completion_time', True), ('exception', True)],
                    'COMPLETED' : [('completion_time', True)],
                    'CHANGE_DETECTION' : [],
                    'CHANGE_ENUMERATION' : [],
                    'CHANGE_APPLICATION' : [],
                    'WAITING' : [],
                }
            ),
        ]



        def __init__(self,
                     stage=None,
                     completed_work=None,
                     total_work=None,
                     completion_time=None,
                     start_time=None,
                     exception=None,
                    ):
            """
            :type  stage: :class:`Providers.SessionInfo.Stage`
            :param stage: Sync stage for the session. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  completed_work: :class:`long`
            :param completed_work: Completed work for the session. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  total_work: :class:`long`
            :param total_work: Total work for the session. **Warning:** This attribute is
                available as technical preview. It may be changed in a future
                release.
            :type  completion_time: :class:`datetime.datetime`
            :param completion_time: Time at which forced sync session was completed. **Warning:** This
                attribute is available as technical preview. It may be changed in a
                future release.
                If None there is an ongoing sync that has not completed
            :type  start_time: :class:`datetime.datetime`
            :param start_time: Time at which force sync was initiated. **Warning:** This attribute
                is available as technical preview. It may be changed in a future
                release.
            :type  exception: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param exception: Exception message if there is a sync failure on forced sync.
                **Warning:** This attribute is available as technical preview. It
                may be changed in a future release.
                This attribute is optional and it is only relevant when the value
                of ``stage`` is :attr:`Providers.SessionInfo.Stage.FAILED`.
            """
            self.stage = stage
            self.completed_work = completed_work
            self.total_work = total_work
            self.completion_time = completion_time
            self.start_time = start_time
            self.exception = exception
            VapiStruct.__init__(self)

        class Stage(Enum):
            """
            The ``Providers.SessionInfo.Stage`` class defines the different stages of
            Sync. **Warning:** This enumeration is available as technical preview. It
            may be changed in a future release.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            CHANGE_DETECTION = None
            """
            Changes are being detected on the source replica. **Warning:** This class
            attribute is available as technical preview. It may be changed in a future
            release.

            """
            CHANGE_ENUMERATION = None
            """
            Changes from the source replica are being enumerated. **Warning:** This
            class attribute is available as technical preview. It may be changed in a
            future release.

            """
            CHANGE_APPLICATION = None
            """
            Changes are being applied to the destination replica. **Warning:** This
            class attribute is available as technical preview. It may be changed in a
            future release.

            """
            COMPLETED = None
            """
            Sync has completed. **Warning:** This class attribute is available as
            technical preview. It may be changed in a future release.

            """
            FAILED = None
            """
            Sync failed. **Warning:** This class attribute is available as technical
            preview. It may be changed in a future release.

            """
            WAITING = None
            """
            Session is waiting for progress to be set. **Warning:** This class
            attribute is available as technical preview. It may be changed in a future
            release.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Stage` instance.
                """
                Enum.__init__(string)

        Stage._set_values([
            Stage('CHANGE_DETECTION'),
            Stage('CHANGE_ENUMERATION'),
            Stage('CHANGE_APPLICATION'),
            Stage('COMPLETED'),
            Stage('FAILED'),
            Stage('WAITING'),
        ])
        Stage._set_binding_type(type.EnumType(
            'com.vmware.vcenter.hvc.links.sync.providers.session_info.stage',
            Stage))

    SessionInfo._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.sync.providers.session_info', {
            'stage': type.ReferenceType(__name__, 'Providers.SessionInfo.Stage'),
            'completed_work': type.IntegerType(),
            'total_work': type.IntegerType(),
            'completion_time': type.OptionalType(type.DateTimeType()),
            'start_time': type.DateTimeType(),
            'exception': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        SessionInfo,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Providers.Summary`` class contains information about a provider.
        **Warning:** This class is available as technical preview. It may be
        changed in a future release.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     provider=None,
                    ):
            """
            :type  provider: :class:`str`
            :param provider: Sync provider id. **Warning:** This attribute is available as
                technical preview. It may be changed in a future release.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vcenter.hvc.links.sync.Providers``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.vcenter.hvc.links.sync.Providers``.
            """
            self.provider = provider
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.vcenter.hvc.links.sync.providers.summary', {
            'provider': type.IdType(resource_types='com.vmware.vcenter.hvc.links.sync.Providers'),
        },
        Summary,
        False,
        None))



    def list(self,
             link,
             ):
        """
        Enumerates the sync providers. **Warning:** This method is available as
        technical preview. It may be changed in a future release.

        :type  link: :class:`str`
        :param link: Unique identifier of the link
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :rtype: :class:`list` of :class:`Providers.Summary`
        :return: The :class:`list` of sync provider information.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            If list fails.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            If the user is not authorized to perform this operation.
        """
        return self._invoke('list',
                            {
                            'link': link,
                            })

    def get(self,
            link,
            provider,
            ):
        """
        Gets Sync information for a sync provider. **Warning:** This method is
        available as technical preview. It may be changed in a future release.

        :type  link: :class:`str`
        :param link: Unique identifier of the link
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :type  provider: :class:`str`
        :param provider: Unique identifier of the sync provider.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.sync.Providers``.
        :rtype: :class:`Providers.Info`
        :return: The Info of sync information for the provider.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the sync provider associated with ``provider`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user is not authorized to perform this operation.
        """
        return self._invoke('get',
                            {
                            'link': link,
                            'provider': provider,
                            })

    def start(self,
              link,
              provider,
              ):
        """
        Initiates synchronization between the local and remote replicas for the
        sync provider. **Warning:** This method is available as technical
        preview. It may be changed in a future release.

        :type  link: :class:`str`
        :param link: Unique identifier of the link
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.Links``.
        :type  provider: :class:`str`
        :param provider: Unique identifier representing the sync provider
            The parameter must be an identifier for the resource type:
            ``com.vmware.vcenter.hvc.sync.Providers``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the link associated with ``link`` does not exist if the provider
            associated with ``provider`` is not registered for sync
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user is not authorized to perform this operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if a sync is already running.
        """
        return self._invoke('start',
                            {
                            'link': link,
                            'provider': provider,
                            })
class _ProvidersStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
        })
        list_error_dict = {
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
            url_template='/hvc/links/{link_id}/sync/providers',
            path_variables={
                'link': 'link_id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
            'provider': type.IdType(resource_types='com.vmware.vcenter.hvc.sync.Providers'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/hvc/links/{link_id}/sync/providers/{provider_id}',
            path_variables={
                'link': 'link_id',
                'provider': 'provider_id',
            },
            query_parameters={
            }
        )

        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'link': type.IdType(resource_types='com.vmware.vcenter.hvc.Links'),
            'provider': type.IdType(resource_types='com.vmware.vcenter.hvc.sync.Providers'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/hvc/links/{link_id}/sync/providers/{provider_id}?action=start',
            path_variables={
                'link': 'link_id',
                'provider': 'provider_id',
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Providers.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Providers.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'start': {
                'input_type': start_input_type,
                'output_type': type.VoidType(),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': start_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'start': start_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.hvc.links.sync.providers',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Providers': Providers,
    }

