# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.library.item.downloadsession.
#---------------------------------------------------------------------------

"""
The Content Library Item Download Session module provides classes and classes
for downloading files in a session.

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
    The ``File`` class provides methods for accessing files within a download
    session. 
    
    After a download session is created against a library item, the ``File``
    class can be used to retrieve all downloadable content within the library
    item. Since the content may not be available immediately in a downloadable
    form on the server side, the client will have to prepare the file and wait
    for the file status to become :attr:`File.PrepareStatus.PREPARED`. 
    
     See :class:`com.vmware.content.library.item_client.DownloadSession`.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FileStub)

    class PrepareStatus(Enum):
        """
        The ``File.PrepareStatus`` class defines the state of the file in
        preparation for download.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        UNPREPARED = None
        """
        The file hasn't been requested for preparation.

        """
        PREPARE_REQUESTED = None
        """
        A prepare has been requested, however the server hasn't started the
        preparation yet.

        """
        PREPARING = None
        """
        A prepare has been requested and the file is in the process of being
        prepared.

        """
        PREPARED = None
        """
        Prepare succeeded. The file is ready for download.

        """
        ERROR = None
        """
        Prepare failed.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`PrepareStatus` instance.
            """
            Enum.__init__(string)

    PrepareStatus._set_values([
        PrepareStatus('UNPREPARED'),
        PrepareStatus('PREPARE_REQUESTED'),
        PrepareStatus('PREPARING'),
        PrepareStatus('PREPARED'),
        PrepareStatus('ERROR'),
    ])
    PrepareStatus._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.downloadsession.file.prepare_status',
        PrepareStatus))


    class EndpointType(Enum):
        """
        The ``File.EndpointType`` class defines the types of endpoints used to
        download the file.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        HTTPS = None
        """
        An https download endpoint.

        """
        DIRECT = None
        """
        A direct download endpoint indicating the location of the file on storage.
        The caller is responsible for retrieving the file from the storage location
        directly.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`EndpointType` instance.
            """
            Enum.__init__(string)

    EndpointType._set_values([
        EndpointType('HTTPS'),
        EndpointType('DIRECT'),
    ])
    EndpointType._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.downloadsession.file.endpoint_type',
        EndpointType))


    class Info(VapiStruct):
        """
        The ``File.Info`` class defines the downloaded file.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     size=None,
                     bytes_transferred=None,
                     status=None,
                     download_endpoint=None,
                     checksum_info=None,
                     error_message=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The name of the file.
            :type  size: :class:`long` or ``None``
            :param size: The file size, in bytes.
                This attribute may not be available immediately. It is guaranteed
                to be set when the client finishes downloading the file.
            :type  bytes_transferred: :class:`long`
            :param bytes_transferred: The number of bytes that have been transferred by the server so far
                for making this file prepared for download. This value may stay at
                zero till the client starts downloading the file.
            :type  status: :class:`File.PrepareStatus`
            :param status: The preparation status (UNPREPARED, PREPARE_REQUESTED, PREPARING,
                PREPARED, ERROR) of the file.
            :type  download_endpoint: :class:`com.vmware.content.library.item_client.TransferEndpoint` or ``None``
            :param download_endpoint: Endpoint at which the file is available for download. The value is
                valid only when the :attr:`File.Info.status` is
                :attr:`File.PrepareStatus.PREPARED`.
                This attribute won't be set until the file status is
                :attr:`File.PrepareStatus.PREPARED`.
            :type  checksum_info: :class:`com.vmware.content.library.item_client.File.ChecksumInfo` or ``None``
            :param checksum_info: The checksum information of the file. When the download is
                complete, you can retrieve the checksum from the :func:`File.get`
                method to verify the checksum for the downloaded file.
                The checksum is always calculated for the downloaded file, but this
                attribute won't be set until the download is complete.
            :type  error_message: :class:`com.vmware.vapi.std_client.LocalizableMessage` or ``None``
            :param error_message: Error message for a failed preparation when the prepare status is
                :attr:`File.PrepareStatus.ERROR`.
                This attribute won't be set unless there was an error with the file
                transfer.
            """
            self.name = name
            self.size = size
            self.bytes_transferred = bytes_transferred
            self.status = status
            self.download_endpoint = download_endpoint
            self.checksum_info = checksum_info
            self.error_message = error_message
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.content.library.item.downloadsession.file.info', {
            'name': type.StringType(),
            'size': type.OptionalType(type.IntegerType()),
            'bytes_transferred': type.IntegerType(),
            'status': type.ReferenceType(__name__, 'File.PrepareStatus'),
            'download_endpoint': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'TransferEndpoint')),
            'checksum_info': type.OptionalType(type.ReferenceType('com.vmware.content.library.item_client', 'File.ChecksumInfo')),
            'error_message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        Info,
        False,
        None))



    def list(self,
             download_session_id,
             ):
        """
        Lists the information of all the files in the library item associated
        with the download session.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :rtype: :class:`list` of :class:`File.Info`
        :return: The :class:`list` of :class:`File.Info` instances.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the download session associated with ``download_session_id``
            doesn't exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``libraryItemId`` requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'download_session_id': download_session_id,
                            })

    def prepare(self,
                download_session_id,
                file_name,
                endpoint_type=None,
                ):
        """
        Requests a file to be prepared for download.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :type  file_name: :class:`str`
        :param file_name:  Name of the file requested for download.
        :type  endpoint_type: :class:`File.EndpointType` or ``None``
        :param endpoint_type: Endpoint type request, one of HTTPS, DIRECT. This will determine
            the type of the :attr:`File.Info.download_endpoint` that is
            generated when the file is prepared. The
            :attr:`File.EndpointType.DIRECT` is only available to users who
            have the ContentLibrary.ReadStorage privilege.
            If not specified the default is :attr:`File.EndpointType.HTTPS`.
        :rtype: :class:`File.Info`
        :return: File information containing the status of the request and the
            download link to the file.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the download session does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if there is no file with the specified ``file_name``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if the the download session wasn't created with the
            ContentLibrary.ReadStorage privilege and the caller requested a
            :attr:`File.EndpointType.DIRECT` endpoint type.
        """
        return self._invoke('prepare',
                            {
                            'download_session_id': download_session_id,
                            'file_name': file_name,
                            'endpoint_type': endpoint_type,
                            })

    def get(self,
            download_session_id,
            file_name,
            ):
        """
        Retrieves file download information for a specific file.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :type  file_name: :class:`str`
        :param file_name:  Name of the file requested.
        :rtype: :class:`File.Info`
        :return: The :class:`File.Info` instance containing the status of the file
            and its download link if available.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the download session associated with ``download_session_id``
            does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if there is no file with the specified ``file_name``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``libraryItemId`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'download_session_id': download_session_id,
                            'file_name': file_name,
                            })
class _FileStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
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

        # properties for prepare operation
        prepare_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
            'file_name': type.StringType(),
            'endpoint_type': type.OptionalType(type.ReferenceType(__name__, 'File.EndpointType')),
        })
        prepare_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        prepare_input_value_validator_list = [
        ]
        prepare_output_validator_list = [
        ]
        prepare_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
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
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'File.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'prepare': {
                'input_type': prepare_input_type,
                'output_type': type.ReferenceType(__name__, 'File.Info'),
                'errors': prepare_error_dict,
                'input_value_validator_list': prepare_input_value_validator_list,
                'output_validator_list': prepare_output_validator_list,
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
            'list': list_rest_metadata,
            'prepare': prepare_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.downloadsession.file',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'File': File,
    }

