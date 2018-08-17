# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.vmon.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.vmon_client`` module provides classes to manage a
set of services that are part of the vCenter Server.

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


class Service(VapiInterface):
    """
    The ``Service`` class provides methods to manage a single/set of services
    that are managed by vMon.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)

    class StartupType(Enum):
        """
        The ``Service.StartupType`` class defines valid Startup Type for services
        managed by vMon.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        MANUAL = None
        """
        Service Startup type is Manual, thus issuing an explicit start on the
        service will start it.

        """
        AUTOMATIC = None
        """
        Service Startup type is Automatic, thus during starting all services or
        issuing explicit start on the service will start it.

        """
        DISABLED = None
        """
        Service Startup type is Disabled, thus it will not start unless the startup
        type changes to manual or automatic.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`StartupType` instance.
            """
            Enum.__init__(string)

    StartupType._set_values([
        StartupType('MANUAL'),
        StartupType('AUTOMATIC'),
        StartupType('DISABLED'),
    ])
    StartupType._set_binding_type(type.EnumType(
        'com.vmware.appliance.vmon.service.startup_type',
        StartupType))


    class State(Enum):
        """
        The ``Service.State`` class defines valid Run State for services.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        STARTING = None
        """
        Service Run State is Starting, it is still not functional

        """
        STOPPING = None
        """
        Service Run State is Stopping, it is not functional

        """
        STARTED = None
        """
        Service Run State is Started, it is fully functional

        """
        STOPPED = None
        """
        Service Run State is Stopped

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`State` instance.
            """
            Enum.__init__(string)

    State._set_values([
        State('STARTING'),
        State('STOPPING'),
        State('STARTED'),
        State('STOPPED'),
    ])
    State._set_binding_type(type.EnumType(
        'com.vmware.appliance.vmon.service.state',
        State))


    class Health(Enum):
        """
        The ``Service.Health`` class defines the possible values for health of a
        service.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DEGRADED = None
        """
        Service is in degraded state, it is not functional.

        """
        HEALTHY = None
        """
        Service is in a healthy state and is fully functional.

        """
        HEALTHY_WITH_WARNINGS = None
        """
        Service is healthy with warnings.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Health` instance.
            """
            Enum.__init__(string)

    Health._set_values([
        Health('DEGRADED'),
        Health('HEALTHY'),
        Health('HEALTHY_WITH_WARNINGS'),
    ])
    Health._set_binding_type(type.EnumType(
        'com.vmware.appliance.vmon.service.health',
        Health))


    class Info(VapiStruct):
        """
        The ``Service.Info`` class contains information about a service.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'state',
                {
                    'STARTED' : [('health', True), ('health_messages', True)],
                    'STARTING' : [],
                    'STOPPING' : [],
                    'STOPPED' : [],
                }
            ),
        ]



        def __init__(self,
                     name_key=None,
                     description_key=None,
                     startup_type=None,
                     state=None,
                     health=None,
                     health_messages=None,
                    ):
            """
            :type  name_key: :class:`str`
            :param name_key: Service name key. Can be used to lookup resource bundle
            :type  description_key: :class:`str`
            :param description_key: Service description key. Can be used to lookup resource bundle
            :type  startup_type: :class:`Service.StartupType`
            :param startup_type: Startup Type.
            :type  state: :class:`Service.State`
            :param state: Running State.
            :type  health: :class:`Service.Health`
            :param health: Health of service.
                This attribute is optional and it is only relevant when the value
                of ``state`` is :attr:`Service.State.STARTED`.
            :type  health_messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param health_messages: Localizable messages associated with the health of the service
                This attribute is optional and it is only relevant when the value
                of ``state`` is :attr:`Service.State.STARTED`.
            """
            self.name_key = name_key
            self.description_key = description_key
            self.startup_type = startup_type
            self.state = state
            self.health = health
            self.health_messages = health_messages
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.vmon.service.info', {
            'name_key': type.StringType(),
            'description_key': type.StringType(),
            'startup_type': type.ReferenceType(__name__, 'Service.StartupType'),
            'state': type.ReferenceType(__name__, 'Service.State'),
            'health': type.OptionalType(type.ReferenceType(__name__, 'Service.Health')),
            'health_messages': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'))),
        },
        Info,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Service.UpdateSpec`` class describes the changes to be made to the
        configuration of the service.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     startup_type=None,
                    ):
            """
            :type  startup_type: :class:`Service.StartupType` or ``None``
            :param startup_type: Startup Type
                If unspecified, leaves value unchanged.
            """
            self.startup_type = startup_type
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.vmon.service.update_spec', {
            'startup_type': type.OptionalType(type.ReferenceType(__name__, 'Service.StartupType')),
        },
        UpdateSpec,
        False,
        None))



    def start(self,
              service,
              ):
        """
        Starts a service

        :type  service: :class:`str`
        :param service: identifier of the service to start
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.vmon.Service``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service associated with ``service`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation is denied in the current state of the service. If
            a stop or restart operation is in progress, the start operation
            will not be allowed.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if start operation is issued on a service which has startup type
            :attr:`Service.StartupType.DISABLED`.
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
            if any timeout occurs during the execution of the start operation.
            Timeout occurs when the service takes longer than StartTimeout to
            start.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any other error occurs during the execution of the operation.
        """
        return self._invoke('start',
                            {
                            'service': service,
                            })

    def stop(self,
             service,
             ):
        """
        Stops a service

        :type  service: :class:`str`
        :param service: identifier of the service to stop
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.vmon.Service``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service associated with ``service`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any other error occurs during the execution of the operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation is denied in the current state of the service. If
            a stop operation is in progress, issuing another stop operation
            will lead to this error.
        """
        return self._invoke('stop',
                            {
                            'service': service,
                            })

    def restart(self,
                service,
                ):
        """
        Restarts a service

        :type  service: :class:`str`
        :param service: identifier of the service to restart
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.vmon.Service``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service associated with ``service`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.TimedOut` 
            if any timeout occurs during the execution of the restart
            operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation is denied in the current state of the service. If
            a stop or start operation is in progress, issuing a restart
            operation will lead to this error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if a restart operation is issued on a service which has startup
            type :attr:`Service.StartupType.DISABLED`
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any other error occurs during the execution of the operation.
        """
        return self._invoke('restart',
                            {
                            'service': service,
                            })

    def get(self,
            service,
            ):
        """
        Returns the state of a service.

        :type  service: :class:`str`
        :param service: identifier of the service whose state is being queried.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.vmon.Service``.
        :rtype: :class:`Service.Info`
        :return: Service Info structure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service associated with ``service`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any other error occurs during the execution of the operation.
        """
        return self._invoke('get',
                            {
                            'service': service,
                            })

    def update(self,
               service,
               spec,
               ):
        """
        Updates the properties of a service.

        :type  service: :class:`str`
        :param service: identifier of the service whose properties are being updated.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.vmon.Service``.
        :type  spec: :class:`Service.UpdateSpec`
        :param spec: Service Update specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service associated with ``service`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any other error occurs during the execution of the operation.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the operation is denied in the current state of the service. If
            a start, stop or restart operation is in progress, update operation
            will fail with this error.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if a request to set the :attr:`Service.UpdateSpec.startup_type`
            attribute of ``spec`` to :attr:`Service.StartupType.DISABLED` comes
            in for a service that is not in :attr:`Service.State.STOPPED`
            state.
        """
        return self._invoke('update',
                            {
                            'service': service,
                            'spec': spec,
                            })

    def list_details(self):
        """
        Lists details of services managed by vMon.


        :rtype: :class:`dict` of :class:`str` and :class:`Service.Info`
        :return: Map of service identifiers to service Info structures.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.appliance.vmon.Service``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list_details', None)
class _ServiceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for start operation
        start_input_type = type.StructType('operation-input', {
            'service': type.IdType(resource_types='com.vmware.appliance.vmon.Service'),
        })
        start_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        start_input_value_validator_list = [
        ]
        start_output_validator_list = [
        ]
        start_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/vmon/service/{id}/start',
            path_variables={
                'service': 'id',
            },
            query_parameters={
            }
        )

        # properties for stop operation
        stop_input_type = type.StructType('operation-input', {
            'service': type.IdType(resource_types='com.vmware.appliance.vmon.Service'),
        })
        stop_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        stop_input_value_validator_list = [
        ]
        stop_output_validator_list = [
        ]
        stop_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/vmon/service/{id}/stop',
            path_variables={
                'service': 'id',
            },
            query_parameters={
            }
        )

        # properties for restart operation
        restart_input_type = type.StructType('operation-input', {
            'service': type.IdType(resource_types='com.vmware.appliance.vmon.Service'),
        })
        restart_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.timed_out':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'TimedOut'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        restart_input_value_validator_list = [
        ]
        restart_output_validator_list = [
        ]
        restart_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/vmon/service/{id}/restart',
            path_variables={
                'service': 'id',
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service': type.IdType(resource_types='com.vmware.appliance.vmon.Service'),
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
            url_template='/appliance/vmon/service/{id}',
            path_variables={
                'service': 'id',
            },
            query_parameters={
            }
        )

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'service': type.IdType(resource_types='com.vmware.appliance.vmon.Service'),
            'spec': type.ReferenceType(__name__, 'Service.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = OperationRestMetadata(
            http_method='PATCH',
            url_template='/appliance/vmon/service/{id}',
            path_variables={
                'service': 'id',
            },
            query_parameters={
            }
        )

        # properties for list_details operation
        list_details_input_type = type.StructType('operation-input', {})
        list_details_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_details_input_value_validator_list = [
        ]
        list_details_output_validator_list = [
        ]
        list_details_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/vmon/service',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'start': {
                'input_type': start_input_type,
                'output_type': type.VoidType(),
                'errors': start_error_dict,
                'input_value_validator_list': start_input_value_validator_list,
                'output_validator_list': start_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'stop': {
                'input_type': stop_input_type,
                'output_type': type.VoidType(),
                'errors': stop_error_dict,
                'input_value_validator_list': stop_input_value_validator_list,
                'output_validator_list': stop_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'restart': {
                'input_type': restart_input_type,
                'output_type': type.VoidType(),
                'errors': restart_error_dict,
                'input_value_validator_list': restart_input_value_validator_list,
                'output_validator_list': restart_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Service.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
            'list_details': {
                'input_type': list_details_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType(__name__, 'Service.Info')),
                'errors': list_details_error_dict,
                'input_value_validator_list': list_details_input_value_validator_list,
                'output_validator_list': list_details_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'start': start_rest_metadata,
            'stop': stop_rest_metadata,
            'restart': restart_rest_metadata,
            'get': get_rest_metadata,
            'update': update_rest_metadata,
            'list_details': list_details_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.vmon.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Service': Service,
    }

