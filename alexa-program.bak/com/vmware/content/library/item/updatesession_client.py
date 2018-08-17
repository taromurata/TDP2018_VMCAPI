# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.library.item.updatesession.
#---------------------------------------------------------------------------

"""
The Content Library Item Update Session module provides classes and classes for
updating files in a session.

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


class File(VapiInterface):
    """
    The ``File`` class provides methods for accessing files within an update
    session. 
    
    After an update session is created against a library item, the ``File``
    class can be used to make changes to the underlying library item metadata
    as well as the content of the files. The following changes can be made: 
    
    * deleting an existing file within the library item. This deletes both the
      metadata and the content.
    * updating an existing file with new content.
    * adding a new file to the library item.
    
     
    
    The above changes are not applied or visible until the session is
    completed. See
    :class:`com.vmware.content.library.item_client.UpdateSession`.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FileStub)

    class SourceType(Enum):
        """
        The ``File.SourceType`` class defines how the file content is retrieved.

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
        No source type has been requested.

        """
        PUSH = None
        """
        The client is uploading content using HTTP(S) PUT requests.

        """
        PULL = None
        """
        The server is pulling content from a URL. The URL scheme can be ``http``,
        ``https``, ``file``, or ``ds``.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`SourceType` instance.
            """
            Enum.__init__(string)

    SourceType._set_values([
        SourceType('NONE'),
        SourceType('PUSH'),
        SourceType('PULL'),
    ])
    SourceType._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.updatesession.file.source_type',
        SourceType))


    class AddSpec(VapiStruct):
        """
        The ``File.AddSpec`` class describes the properties of the file to be
        uploaded.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'source_type',
                {
                    'PULL' : [('source_endpoint', True)],
                    'NONE' : [],
                    'PUSH' : [],
                }
            ),
        ]



        def __init__(self,
                     name=None,
                     source_type=None,
                     source_endpoint=None,
                     size=None,
                     checksum_info=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the file being uploaded.
            :type  source_type: :class:`File.SourceType`
            :param source_type: The source type (NONE, PUSH, PULL) from which the file content will
                be retrieved.
            :type  source_endpoint: :class:`com.vmware.content.library.item_client.TransferEndpoint`
            :param source_endpoint: Location from which the Content Library Service will fetch the
                file, rather than requiring a client to upload the file.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`File.SourceType.PULL`.
            :type  size: :class:`long` or ``None``
            :param size: The file size, in bytes.
                If specified the server will verify it received the correct size.
            :type  checksum_info: :class:`com.vmware.content.library.item_client.File.ChecksumInfo` or ``None``
            :param checksum_info: The checksum of the file. If specified, the server will verify the
                checksum once the file is received. If there is a mismatch, the
                upload will fail.
                If not specified the server does not verify the checksum.
            """
            self.name = name
            self.source_type = source_type
            self.source_endpoint = source_endpoint
            self.size = size
            self.checksum_info = checksum_info
            VapiStruct.__init__(self)

    AddSpec._set_binding_type(type.StructType(
        'com.vmware.content.library.item.updatesession.file.add_spec', {
            'name': type.StringType(),
            'source_type': type.ReferenceType(__name__, 'File.SourceType'),
            'source_endpoint': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'TransferEndpoint')),
            'size': type.OptionalType(type.IntegerType()),
            'checksum_info': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'File.ChecksumInfo')),
        },
        AddSpec,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``File.Info`` class defines the uploaded file.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'source_type',
                {
                    'PULL' : [('source_endpoint', True)],
                    'PUSH' : [('upload_endpoint', True)],
                    'NONE' : [],
                }
            ),
        ]



        def __init__(self,
                     name=None,
                     source_type=None,
                     size=None,
                     checksum_info=None,
                     source_endpoint=None,
                     upload_endpoint=None,
                     bytes_transferred=None,
                     status=None,
                     error_message=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the file.
            :type  source_type: :class:`File.SourceType`
            :param source_type: The source type (NONE, PUSH, PULL) from which the file is being
                retrieved. This may be :attr:`File.SourceType.NONE` if the file is
                not being changed.
            :type  size: :class:`long` or ``None``
            :param size: The file size, in bytes as received by the server. This attribute
                is guaranteed to be set when the server has completely received the
                file.
                This attribute won't be set until the file status is
                :attr:`com.vmware.content.library.item_client.TransferStatus.READY`.
            :type  checksum_info: :class:`com.vmware.content.library.item_client.File.ChecksumInfo` or ``None``
            :param checksum_info: The checksum information of the file received by the server.
                If not specified the server does not verify the checksum.
            :type  source_endpoint: :class:`com.vmware.content.library.item_client.TransferEndpoint`
            :param source_endpoint: A source endpoint from which to retrieve the file.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`File.SourceType.PULL`.
            :type  upload_endpoint: :class:`com.vmware.content.library.item_client.TransferEndpoint`
            :param upload_endpoint: An upload endpoint to which the client can push the content.
                This attribute is optional and it is only relevant when the value
                of ``sourceType`` is :attr:`File.SourceType.PUSH`.
            :type  bytes_transferred: :class:`long`
            :param bytes_transferred: The number of bytes of this file that have been received by the
                server.
            :type  status: :class:`com.vmware.content.library.item_client.TransferStatus`
            :param status: The transfer status (WAITING_FOR_TRANSFER, TRANSFERRING, READY,
                VALIDATING, ERROR) of this file.
            :type  error_message: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param error_message: Details about the transfer error.
                An error message is set if the status is
                :attr:`com.vmware.content.library.item_client.TransferStatus.ERROR`.
            """
            self.name = name
            self.source_type = source_type
            self.size = size
            self.checksum_info = checksum_info
            self.source_endpoint = source_endpoint
            self.upload_endpoint = upload_endpoint
            self.bytes_transferred = bytes_transferred
            self.status = status
            self.error_message = error_message
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.content.library.item.updatesession.file.info', {
            'name': type.StringType(),
            'source_type': type.ReferenceType(__name__, 'File.SourceType'),
            'size': type.OptionalType(type.IntegerType()),
            'checksum_info': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'File.ChecksumInfo')),
            'source_endpoint': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'TransferEndpoint')),
            'upload_endpoint': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'TransferEndpoint')),
            'bytes_transferred': type.IntegerType(),
            'status': type.ReferenceType('com.vmware.content.library.item_client', 'TransferStatus'),
            'error_message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Info,
        False,
        None))


    class ValidationError(VapiStruct):
        """
        The ``File.ValidationError`` class defines the validation error of a file
        in the session.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     error_message=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the file.
            :type  error_message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param error_message: A message indicating why the file was considered invalid.
            """
            self.name = name
            self.error_message = error_message
            VapiStruct.__init__(self)

    ValidationError._set_binding_type(type.StructType(
        'com.vmware.content.library.item.updatesession.file.validation_error', {
            'name': type.StringType(),
            'error_message': type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage'),
        },
        ValidationError,
        False,
        None))


    class ValidationResult(VapiStruct):
        """
        The ``File.ValidationResult`` class defines the result of validating the
        files in the session.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     has_errors=None,
                     missing_files=None,
                     invalid_files=None,
                    ):
            """
            :type  has_errors: :class:`bool`
            :param has_errors: Whether the validation was succesful or not. In case of errors, the
                :attr:`File.ValidationResult.missing_files` and
                :attr:`File.ValidationResult.invalid_files` will contain at least
                one entry.
            :type  missing_files: :class:`set` of :class:`str`
            :param missing_files: A :class:`set` containing the names of the files that are required
                but the client hasn't added.
            :type  invalid_files: :class:`list` of :class:`File.ValidationError`
            :param invalid_files: A :class:`list` containing the files that have been identified as
                invalid and details about the error.
            """
            self.has_errors = has_errors
            self.missing_files = missing_files
            self.invalid_files = invalid_files
            VapiStruct.__init__(self)

    ValidationResult._set_binding_type(type.StructType(
        'com.vmware.content.library.item.updatesession.file.validation_result', {
            'has_errors': type.BooleanType(),
            'missing_files': type.SetType(type.StringType()),
            'invalid_files': type.ListType(type.ReferenceType(__name__, 'File.ValidationError')),
        },
        ValidationResult,
        False,
        None))



    def validate(self,
                 update_session_id,
                 ):
        """
        Validates the files in the update session with the referenced
        identifier and ensures all necessary files are received. In the case
        where a file is missing, this method will return its name in the
        :attr:`File.ValidationResult.missing_files` set. The user can add the
        missing files and try re-validating. For other type of errors,
        :attr:`File.ValidationResult.invalid_files` will contain the list of
        invalid files.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session to validate.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :rtype: :class:`File.ValidationResult`
        :return: A validation result containing missing files or invalid files and
            the reason why they are invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no update session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is not in the
            :attr:`com.vmware.content.library.item_client.UpdateSessionModel.State.ACTIVE`
            state, or if some of the files that will be uploaded by the client
            aren't received correctly.
        """
        return self._invoke('validate',
                            {
                            'update_session_id': update_session_id,
                            })

    def add(self,
            update_session_id,
            file_spec,
            ):
        """
        Requests file content to be changed (either created, or updated).
        Depending on the source type of the file, this method will either
        return an upload endpoint where the client can push the content, or the
        server will pull from the provided source endpoint. If a file with the
        same name already exists in this session, this method will be used to
        update the content of the existing file. 
        
        When importing a file directly from storage, where the source endpoint
        is a file or datastore URI, you will need to have the
        ContentLibrary.ReadStorage privilege on the library item. If the file
        is located in the same directory as the library storage backing folder,
        the server will move the file instead of copying it, thereby allowing
        instantaneous import of files for efficient backup and restore
        scenarios. In all other cases, a copy is performed rather than a move.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session to be modified.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :type  file_spec: :class:`File.AddSpec`
        :param file_spec: Specification for the file that needs to be added or updated. This
            includes whether the client wants to push the content or have the
            server pull it.
        :rtype: :class:`File.Info`
        :return: An :class:`File.Info` class containing upload links as well as
            server side state tracking the transfer of the file.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``file_spec`` is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session doesn't exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the caller doesn't have ContentLibrary.ReadStorage privilege on
            the library item of the update session and source type
            :attr:`File.SourceType.PULL` is requested for a file or datastore
            source endpoint (that is, not HTTP or HTTPs based endpoint).
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the library item associated with the update
            session has been deleted from the storage backings (see null)
            associated with it.
        """
        return self._invoke('add',
                            {
                            'update_session_id': update_session_id,
                            'file_spec': file_spec,
                            })

    def remove(self,
               update_session_id,
               file_name,
               ):
        """
        Requests a file to be removed. The file will only be effectively
        removed when the update session is completed.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :type  file_name: :class:`str`
        :param file_name:  Name of the file to be removed.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session doesn't exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the file doesn't exist in the library item associated with the
            update session.
        """
        return self._invoke('remove',
                            {
                            'update_session_id': update_session_id,
                            'file_name': file_name,
                            })

    def list(self,
             update_session_id,
             ):
        """
        Lists all files in the library item associated with the update session.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :rtype: :class:`list` of :class:`File.Info`
        :return: The :class:`list` of the files in the library item associated with
            the update session. This :class:`list` may be empty if the caller
            has removed all the files as part of this session (in which case
            completing the update session will result in an empty library
            item).
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session doesn't exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``libraryItemId`` requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'update_session_id': update_session_id,
                            })

    def get(self,
            update_session_id,
            file_name,
            ):
        """
        Retrieves information about a specific file in the snapshot of the
        library item at the time when the update session was created.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :type  file_name: :class:`str`
        :param file_name:  Name of the file.
        :rtype: :class:`File.Info`
        :return: Information about the file.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session doesn't exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the file doesn't exist in the library item associated with the
            update session.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``libraryItemId`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'update_session_id': update_session_id,
                            'file_name': file_name,
                            })
class _FileStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for validate operation
        validate_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        validate_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        validate_input_value_validator_list = [
        ]
        validate_output_validator_list = [
        ]
        validate_rest_metadata = None

        # properties for add operation
        add_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
            'file_spec': type.ReferenceType(__name__, 'File.AddSpec'),
        })
        add_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        add_input_value_validator_list = [
        ]
        add_output_validator_list = [
        ]
        add_rest_metadata = None

        # properties for remove operation
        remove_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
            'file_name': type.StringType(),
        })
        remove_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        remove_input_value_validator_list = [
        ]
        remove_output_validator_list = [
        ]
        remove_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
            'file_name': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'validate': {
                'input_type': validate_input_type,
                'output_type': type.ReferenceType(__name__, 'File.ValidationResult'),
                'errors': validate_error_dict,
                'input_value_validator_list': validate_input_value_validator_list,
                'output_validator_list': validate_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'add': {
                'input_type': add_input_type,
                'output_type': type.ReferenceType(__name__, 'File.Info'),
                'errors': add_error_dict,
                'input_value_validator_list': add_input_value_validator_list,
                'output_validator_list': add_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'remove': {
                'input_type': remove_input_type,
                'output_type': type.VoidType(),
                'errors': remove_error_dict,
                'input_value_validator_list': remove_input_value_validator_list,
                'output_validator_list': remove_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'File.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'File.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'validate': validate_rest_metadata,
            'add': add_rest_metadata,
            'remove': remove_rest_metadata,
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.updatesession.file',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'File': File,
    }

