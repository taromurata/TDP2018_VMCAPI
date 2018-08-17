# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.cis.
#---------------------------------------------------------------------------

"""
The ``com.vmware.cis_client`` module provides VMware common infrastructure
classes.

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


class Session(VapiInterface):
    """
    The ``Session`` class allows API clients to manage session tokens including
    creating, deleting and obtaining information about sessions. 
    
     
    
    * The :func:`Session.create` method creates session token in exchange for
      another authentication token.
    * The :func:`Session.delete` method invalidates a session token.
    * The :func:`Session.get` retrieves information about a session token.
    
     
    
    The call to the :func:`Session.create` method is part of the overall
    authentication process for API clients. For example, the sequence of steps
    for establishing a session with SAML token is: 
    
    * Connect to lookup service.
    * Discover the secure token service (STS) endpoint URL.
    * Connect to the secure token service to obtain a SAML token.
    * Authenticate to the lookup service using the obtained SAML token.
    * Discover the API endpoint URL from lookup service.
    * Call the :func:`Session.create` method. The :func:`Session.create` call
      must include the SAML token.
    
     
    
    See the programming guide and samples for additional information about
    establishing API sessions. 
    
     **Execution Context and Security Context** 
    
    To use session based authentication a client should supply the session
    token obtained through the :func:`Session.create` method. The client should
    add the session token in the security context when using SDK classes.
    Clients using the REST API should supply the session token as a HTTP
    header. 
    
     **Session Lifetime** 
    
    A session begins with call to the :func:`Session.create` method to exchange
    a SAML token for a API session token. A session ends under the following
    circumstances: 
    
    * Call to the :func:`Session.delete` method.
    * The session expires. Session expiration may be caused by one of the
      following situations: 
    
    * Client inactivity - For a particular session identified by client
      requests that specify the associated session ID, the lapsed time since the
      last request exceeds the maximum interval between requests.
    * Unconditional or absolute session expiration time: At the beginning of
      the session, the session logic uses the SAML token and the system
      configuration to calculate absolute expiration time.
    
     
    
    When a session ends, the authentication logic will reject any subsequent
    client requests that specify that session. Any operations in progress will
    continue to completion. 
    
     **Error Handling** 
    
     The :class:`Session` returns the following exceptions: 
    
    * :class:`com.vmware.vapi.std.errors_client.Unauthenticated` exception for
      any exceptions related to the request.
    * :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` exception
      for all exceptions caused by internal service failure.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SessionStub)

    class Info(VapiStruct):
        """
        Represents data associated with an API session.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     user=None,
                     created_time=None,
                     last_accessed_time=None,
                    ):
            """
            :type  user: :class:`str`
            :param user: Fully qualified name of the end user that created the session, for
                example Administrator\\\\@vsphere.local. A typical use case for
                this information is in Graphical User Interfaces (GUI) or logging
                systems to visualize the identity of the current user.
            :type  created_time: :class:`datetime.datetime`
            :param created_time: Time when the session was created.
            :type  last_accessed_time: :class:`datetime.datetime`
            :param last_accessed_time: Last time this session was used by passing the session key for
                invoking an API.
            """
            self.user = user
            self.created_time = created_time
            self.last_accessed_time = last_accessed_time
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.cis.session.info', {
            'user': type.StringType(),
            'created_time': type.DateTimeType(),
            'last_accessed_time': type.DateTimeType(),
        },
        Info,
        False,
        None))



    def create(self):
        """
        Creates a session with the API. This is the equivalent of login. This
        method exchanges user credentials supplied in the security context for
        a session identifier that is to be used for authenticating subsequent
        calls. To authenticate subsequent calls clients are expected to include
        the session key.


        :rtype: :class:`str`
        :return: Newly created session identifier to be used for authenticating
            further requests.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session creation fails due to request specific issues. Due
            to the security nature of the API the details of the error are not
            disclosed. 
            
            Please check the following preconditions if using a SAML token to
            authenticate: 
            
            * the supplied token is delegate-able.
            * the time of client and server system are synchronized.
            * the token supplied is valid.
            * if bearer tokens are used check that system configuration allows
              the API endpoint to accept such tokens.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session creation fails due to server specific issues, for
            example connection to a back end component is failing. Due to the
            security nature of this API further details will not be disclosed
            in the exception. Please refer to component health information,
            administrative logs and product specific documentation for possible
            causes.
        """
        return self._invoke('create', None)

    def delete(self):
        """
        Terminates the validity of a session token. This is the equivalent of
        log out. 
        
         A session identifier is expected as part of the request. 


        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session id is missing from the request or the corresponding
            session object cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session deletion fails due to server specific issues, for
            example connection to a back end component is failing. Due to the
            security nature of this API further details will not be disclosed
            in the exception. Please refer to component health information,
            administrative logs and product specific documentation for possible
            causes.
        """
        return self._invoke('delete', None)

    def get(self):
        """
        Returns information about the current session. This method expects a
        valid session identifier to be supplied. 
        
        A side effect of invoking this method may be a change to the session's
        last accessed time to the current time if this is supported by the
        session implementation. Invoking any other method in the API will also
        update the session's last accessed time. 
        
        This API is meant to serve the needs of various front end projects that
        may want to display the name of the user. Examples of this include
        various web based user interfaces and logging facilities.


        :rtype: :class:`Session.Info`
        :return: Information about the session.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the session id is missing from the request or the corresponding
            session object cannot be found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if session retrieval fails due to server specific issues e.g.
            connection to back end component is failing. Due to the security
            nature of this API further details will not be disclosed in the
            error. Please refer to component health information, administrative
            logs and product specific documentation for possible causes.
        """
        return self._invoke('get', None)
class Tasks(VapiInterface):
    """
    The ``Tasks`` class provides methods for managing the task related to a
    long running operation. **Warning:** This class is part of a new feature in
    development. It may be changed at any time and may not have all supported
    functionality implemented.
    """
    RESOURCE_TYPE = "com.vmware.cis.task"
    """
    Resource type for task. **Warning:** This class attribute is part of a new
    feature in development. It may be changed at any time and may not have all
    supported functionality implemented.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TasksStub)

    class GetSpec(VapiStruct):
        """
        The ``Tasks.GetSpec`` class describes what data should be included when
        retrieving information about a task. **Warning:** This class is part of a
        new feature in development. It may be changed at any time and may not have
        all supported functionality implemented.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     return_all=None,
                     exclude_result=None,
                    ):
            """
            :type  return_all: :class:`bool` or ``None``
            :param return_all: If true, all data, including operation-specific data, will be
                returned, otherwise only the data described in
                :class:`com.vmware.cis.task_client.Info` will be returned.
                **Warning:** This attribute is part of a new feature in
                development. It may be changed at any time and may not have all
                supported functionality implemented.
                If None, only the data described in
                :class:`com.vmware.cis.task_client.Info` will be returned.
            :type  exclude_result: :class:`bool` or ``None``
            :param exclude_result: If true, the result will not be included in the task information,
                otherwise it will be included. **Warning:** This attribute is part
                of a new feature in development. It may be changed at any time and
                may not have all supported functionality implemented.
                If None, the result of the operation will be included in the task
                information.
            """
            self.return_all = return_all
            self.exclude_result = exclude_result
            VapiStruct.__init__(self)

    GetSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tasks.get_spec', {
            'return_all': type.OptionalType(type.BooleanType()),
            'exclude_result': type.OptionalType(type.BooleanType()),
        },
        GetSpec,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Tasks.FilterSpec`` class contains attributes used to filter the
        results when listing tasks (see :func:`Tasks.list`). If multiple attributes
        are specified, only tasks matching all of the attributes match the filter.
        **Warning:** This class is part of a new feature in development. It may be
        changed at any time and may not have all supported functionality
        implemented.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     tasks=None,
                     status=None,
                     targets=None,
                     users=None,
                    ):
            """
            :type  tasks: :class:`set` of :class:`str` or ``None``
            :param tasks: Identifiers of tasks that can match the filter. **Warning:** This
                attribute is part of a new feature in development. It may be
                changed at any time and may not have all supported functionality
                implemented.
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.cis.task``. When methods return a value of this class
                as a return value, the attribute will contain identifiers for the
                resource type: ``com.vmware.cis.task``.
                This attribute is currently required and must contain at least one
                task identifier. In the future, if this attribute is None or empty,
                tasks with any identifier will match the filter.
            :type  status: :class:`set` of :class:`com.vmware.cis.task_client.Status` or ``None``
            :param status: Status that a task must have to match the filter (see
                :attr:`com.vmware.cis.task_client.CommonInfo.status`). **Warning:**
                This attribute is part of a new feature in development. It may be
                changed at any time and may not have all supported functionality
                implemented.
                If None or empty, tasks with any status match the filter.
            :type  targets: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID` or ``None``
            :param targets: Identifiers of the targets the operation for the associated task
                created or was performed on (see
                :attr:`com.vmware.cis.task_client.CommonInfo.target`). **Warning:**
                This attribute is part of a new feature in development. It may be
                changed at any time and may not have all supported functionality
                implemented.
                If None or empty, tasks associated with operations on any target
                match the filter.
            :type  users: :class:`set` of :class:`str` or ``None``
            :param users: Users who must have initiated the operation for the associated task
                to match the filter (see
                :attr:`com.vmware.cis.task_client.CommonInfo.user`). **Warning:**
                This attribute is part of a new feature in development. It may be
                changed at any time and may not have all supported functionality
                implemented.
                If None or empty, tasks associated with operations initiated by any
                user match the filter.
            """
            self.tasks = tasks
            self.status = status
            self.targets = targets
            self.users = users
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tasks.filter_spec', {
            'tasks': type.OptionalType(type.SetType(type.IdType())),
            'status': type.OptionalType(type.SetType(type.ReferenceType('com.vmware.cis.task_client', 'Status'))),
            'targets': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'))),
            'users': type.OptionalType(type.SetType(type.StringType())),
        },
        FilterSpec,
        False,
        None))



    def get(self,
            task,
            spec=None,
            ):
        """
        Returns information about a task. **Warning:** This method is part of a
        new feature in development. It may be changed at any time and may not
        have all supported functionality implemented.

        :type  task: :class:`str`
        :param task: Task identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.task``.
        :type  spec: :class:`Tasks.GetSpec` or ``None``
        :param spec: Specification on what to get for a task.
            If None, the behavior is equivalent to a :class:`Tasks.GetSpec`
            with all attributes None which means only the data described in
            :class:`com.vmware.cis.task_client.Info` will be returned and the
            result of the operation will be return.
        :rtype: :class:`com.vmware.cis.task_client.Info`
        :return: Information about the specified task.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the task is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the task's state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('get',
                            {
                            'task': task,
                            'spec': spec,
                            })

    def list(self,
             filter_spec=None,
             result_spec=None,
             ):
        """
        Returns information about at most 1000 visible (subject to permission
        checks) tasks matching the :class:`Tasks.FilterSpec`. All tasks must be
        in the same provider. **Warning:** This method is part of a new feature
        in development. It may be changed at any time and may not have all
        supported functionality implemented.

        :type  filter_spec: :class:`Tasks.FilterSpec` or ``None``
        :param filter_spec: Specification of matching tasks.
            This is currently required. In the future, if it is None, the
            behavior is equivalent to a :class:`Tasks.FilterSpec` with all
            attributes None which means all tasks match the filter.
        :type  result_spec: :class:`Tasks.GetSpec` or ``None``
        :param result_spec: Specification of what to return for a task.
            If None, the behavior is equivalent to a :class:`Tasks.GetSpec`
            with all attributes None which means only the data describe in
            :class:`com.vmware.cis.task_client.Info` will be returned and the
            result of the operation will be return.
        :rtype: :class:`dict` of :class:`str` and :class:`com.vmware.cis.task_client.Info`
        :return: Map of task identifier to information about the task.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``com.vmware.cis.task``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if any of the specified parameters are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if a task's state cannot be accessed or over 1000 tasks matching
            the :class:`Tasks.FilterSpec`.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        """
        return self._invoke('list',
                            {
                            'filter_spec': filter_spec,
                            'result_spec': result_spec,
                            })

    def cancel(self,
               task,
               ):
        """
        Cancel a running task. This is the best effort attempt. Task may not be
        cancelled anymore once it reaches certain stage. **Warning:** This
        method is part of a new feature in development. It may be changed at
        any time and may not have all supported functionality implemented.

        :type  task: :class:`str`
        :param task: Task identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.task``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if the system reports an error while responding to the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the task is already canceled or completed.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the task is not found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the task's state cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.ServiceUnavailable` 
            if the system is unable to communicate with a service to complete
            the request.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the user can not be authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the user doesn't have the required privileges.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
            if the task is not cancelable.
        """
        return self._invoke('cancel',
                            {
                            'task': task,
                            })
class _SessionStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {})
        create_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {})
        delete_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.SecretType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
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
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Session.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.session',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TasksStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'task': type.IdType(resource_types='com.vmware.cis.task'),
            'spec': type.OptionalType(type.ReferenceType(__name__, 'Tasks.GetSpec')),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
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
            url_template='/cis/tasks/{task}',
            path_variables={
                'task': 'task',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'filter_spec': type.OptionalType(type.ReferenceType(__name__, 'Tasks.FilterSpec')),
            'result_spec': type.OptionalType(type.ReferenceType(__name__, 'Tasks.GetSpec')),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
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
            url_template='/cis/tasks',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'task': type.IdType(resource_types='com.vmware.cis.task'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.service_unavailable':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ServiceUnavailable'),
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/cis/tasks/{task}',
            path_variables={
                'task': 'task',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType('com.vmware.cis.task_client', 'Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.MapType(type.IdType(), type.ReferenceType('com.vmware.cis.task_client', 'Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'cancel': {
                'input_type': cancel_input_type,
                'output_type': type.VoidType(),
                'errors': cancel_error_dict,
                'input_value_validator_list': cancel_input_value_validator_list,
                'output_validator_list': cancel_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'cancel': cancel_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.tasks',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Session': Session,
        'Tasks': Tasks,
        'task': 'com.vmware.cis.task_client.StubFactory',
    }

