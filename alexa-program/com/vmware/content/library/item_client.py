# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.library.item.
#---------------------------------------------------------------------------

"""
The Content Library Item module provides classes and classes for managing files
in a library item.

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

class TransferStatus(Enum):
    """
    The ``TransferStatus`` class defines the transfer state of a file.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    WAITING_FOR_TRANSFER = None
    """
    Indicates that a file has been defined for a library item and its content
    needs to be uploaded.

    """
    TRANSFERRING = None
    """
    Indicates that data is being transferred to the file.

    """
    READY = None
    """
    Indicates that the file has been fully transferred and is ready to be used.

    """
    VALIDATING = None
    """
    Indicates that the file is being validated (checksum, type adapters).

    """
    ERROR = None
    """
    Indicates that there was an error transferring or validating the file.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`TransferStatus` instance.
        """
        Enum.__init__(string)

TransferStatus._set_values([
    TransferStatus('WAITING_FOR_TRANSFER'),
    TransferStatus('TRANSFERRING'),
    TransferStatus('READY'),
    TransferStatus('VALIDATING'),
    TransferStatus('ERROR'),
])
TransferStatus._set_binding_type(type.EnumType(
    'com.vmware.content.library.item.transfer_status',
    TransferStatus))




class DownloadSessionModel(VapiStruct):
    """
    The ``DownloadSessionModel`` class provides information on an active
    :class:`DownloadSession` resource.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 library_item_id=None,
                 library_item_content_version=None,
                 error_message=None,
                 client_progress=None,
                 state=None,
                 expiration_time=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of this download session.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
            This attribute is not used for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is not used for the ``update`` method.
        :type  library_item_id: :class:`str`
        :param library_item_id: The identifier of the library item whose content is being
            downloaded.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.Item``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.content.library.Item``.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  library_item_content_version: :class:`str`
        :param library_item_content_version: The content version of the library item whose content is being
            downloaded. This value is the
            :attr:`com.vmware.content.library_client.ItemModel.content_version`
            at the time when the session is created for the library item.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  error_message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param error_message: If the session is in the :attr:`DownloadSessionModel.State.ERROR`
            status this property will have more details about the error.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        :type  client_progress: :class:`long`
        :param client_progress: The progress that has been made with the download. This property is
            to be updated by the client during the download process to indicate
            the progress of its work in completing the download. The initial
            progress is 0 until updated by the client. The maximum value is
            100, which indicates that the download is complete.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  state: :class:`DownloadSessionModel.State`
        :param state: The current state (ACTIVE, CANCELED, ERROR) of the download
            session.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  expiration_time: :class:`datetime.datetime`
        :param expiration_time: Indicates the time after which the session will expire. The session
            is guaranteed not to expire before this time.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        """
        self.id = id
        self.library_item_id = library_item_id
        self.library_item_content_version = library_item_content_version
        self.error_message = error_message
        self.client_progress = client_progress
        self.state = state
        self.expiration_time = expiration_time
        VapiStruct.__init__(self)

    class State(Enum):
        """
        The state of the download session.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ACTIVE = None
        """
        The session is active. Individual files may be in the process of being
        transferred and may become ready for download at different times.

        """
        CANCELED = None
        """
        The session has been canceled. On-going downloads may fail. The session
        will stay in this state until it is either deleted by the user or
        automatically cleaned up by the Content Library Service.

        """
        ERROR = None
        """
        Indicates there was an error during the session lifecycle.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`State` instance.
            """
            Enum.__init__(string)

    State._set_values([
        State('ACTIVE'),
        State('CANCELED'),
        State('ERROR'),
    ])
    State._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.download_session_model.state',
        State))

DownloadSessionModel._set_binding_type(type.StructType(
    'com.vmware.content.library.item.download_session_model', {
        'id': type.OptionalType(type.IdType()),
        'library_item_id': type.OptionalType(type.IdType()),
        'library_item_content_version': type.OptionalType(type.StringType()),
        'error_message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'client_progress': type.OptionalType(type.IntegerType()),
        'state': type.OptionalType(type.ReferenceType(__name__, 'DownloadSessionModel.State')),
        'expiration_time': type.OptionalType(type.DateTimeType()),
    },
    DownloadSessionModel,
    True,
    ["id"]))



class TransferEndpoint(VapiStruct):
    """
    The ``TransferEndpoint`` class encapsulates a URI along with extra
    information about it.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 uri=None,
                 ssl_certificate_thumbprint=None,
                ):
        """
        :type  uri: :class:`str`
        :param uri: Transfer endpoint URI. The supported URI schemes are: ``http``,
            ``https``, ``file``, and ``ds``. 
            
            An endpoint URI with the ``ds`` scheme specifies the location of
            the file on the datastore. The format of the datastore URI is: 
            
            * ds:///vmfs/volumes/uuid/path
            
             
            
             Some examples of valid file URI formats are: 
            
            * file:///path
            * file:///C:/path
            * file://unc-server/path
            
             
            
            When the transfer endpoint is a file or datastore location, the
            server can import the file directly from the storage backing
            without the overhead of streaming over HTTP.
        :type  ssl_certificate_thumbprint: :class:`str` or ``None``
        :param ssl_certificate_thumbprint: Thumbprint of the expected SSL certificate for this endpoint. Only
            used for HTTPS connections. The thumbprint is the SHA-1 hash of the
            DER encoding of the remote endpoint's SSL certificate. If set, the
            remote endpoint's SSL certificate is only accepted if it matches
            this thumbprint, and no other certificate validation is performed.
            If not specified, standard certificate validation is performed.
        """
        self.uri = uri
        self.ssl_certificate_thumbprint = ssl_certificate_thumbprint
        VapiStruct.__init__(self)

TransferEndpoint._set_binding_type(type.StructType(
    'com.vmware.content.library.item.transfer_endpoint', {
        'uri': type.URIType(),
        'ssl_certificate_thumbprint': type.OptionalType(type.StringType()),
    },
    TransferEndpoint,
    False,
    None))



class UpdateSessionModel(VapiStruct):
    """
    The ``UpdateSessionModel`` class provides information on an active
    :class:`UpdateSession` resource.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 library_item_id=None,
                 library_item_content_version=None,
                 error_message=None,
                 client_progress=None,
                 state=None,
                 expiration_time=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The identifier of this update session.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``. When methods
            return a value of this class as a return value, the attribute will
            be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
            This attribute is not used for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is not used for the ``update`` method.
        :type  library_item_id: :class:`str`
        :param library_item_id: The identifier of the library item to which content will be
            uploaded or removed.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.Item``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.content.library.Item``.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  library_item_content_version: :class:`str`
        :param library_item_content_version: The content version of the library item whose content is being
            modified. This value is the
            :attr:`com.vmware.content.library_client.ItemModel.content_version`
            at the time when the session is created for the library item.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  error_message: :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param error_message: If the session is in the :attr:`UpdateSessionModel.State.ERROR`
            status this property will have more details about the error.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        :type  client_progress: :class:`long`
        :param client_progress: The progress that has been made with the upload. This property is
            to be updated by the client during the upload process to indicate
            the progress of its work in completing the upload. The initial
            progress is 0 until updated by the client. The maximum value is
            100, which indicates that the update is complete.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  state: :class:`UpdateSessionModel.State`
        :param state: The current state (ACTIVE, DONE, ERROR, CANCELED) of the update
            session.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  expiration_time: :class:`datetime.datetime`
        :param expiration_time: Indicates the time after which the session will expire. The session
            is guaranteed not to expire earlier than this time.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        """
        self.id = id
        self.library_item_id = library_item_id
        self.library_item_content_version = library_item_content_version
        self.error_message = error_message
        self.client_progress = client_progress
        self.state = state
        self.expiration_time = expiration_time
        VapiStruct.__init__(self)

    class State(Enum):
        """
        The state of an update session.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        ACTIVE = None
        """
        The session is currently active. This is the initial state when the session
        is created. Files may be uploaded by the client or pulled by the Content
        Library Service at this stage.

        """
        DONE = None
        """
        The session is done and all its effects are now visible.

        """
        ERROR = None
        """
        There was an error during the session.

        """
        CANCELED = None
        """
        The session has been canceled.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`State` instance.
            """
            Enum.__init__(string)

    State._set_values([
        State('ACTIVE'),
        State('DONE'),
        State('ERROR'),
        State('CANCELED'),
    ])
    State._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.update_session_model.state',
        State))

UpdateSessionModel._set_binding_type(type.StructType(
    'com.vmware.content.library.item.update_session_model', {
        'id': type.OptionalType(type.IdType()),
        'library_item_id': type.OptionalType(type.IdType()),
        'library_item_content_version': type.OptionalType(type.StringType()),
        'error_message': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'client_progress': type.OptionalType(type.IntegerType()),
        'state': type.OptionalType(type.ReferenceType(__name__, 'UpdateSessionModel.State')),
        'expiration_time': type.OptionalType(type.DateTimeType()),
    },
    UpdateSessionModel,
    True,
    ["id"]))



class DownloadSession(VapiInterface):
    """
    The ``DownloadSession`` class manipulates download sessions, which are used
    to download content from the Content Library Service. 
    
    A download session is an object that tracks the download of content (that
    is, downloading content from the Content Library Service) and acts as a
    lease to keep the download links available. 
    
    The :class:`com.vmware.content.library.item.downloadsession_client.File`
    class provides access to the download links.
    """
    RESOURCE_TYPE = "com.vmware.content.library.item.DownloadSession"
    """
    Resource type for a download session.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DownloadSessionStub)


    def create(self,
               create_spec,
               client_token=None,
               ):
        """
        Creates a new download session.

        :type  client_token: :class:`str` or ``None``
        :param client_token: A unique token generated by the client for each creation request.
            The token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent creation.
            If not specified creation is not idempotent.
        :type  create_spec: :class:`DownloadSessionModel`
        :param create_spec:  Specification for the new download session to be created.
        :rtype: :class:`str`
        :return: Identifier of the new download session being created.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the session specification is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             format.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library item targeted by the download does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the attribute :attr:`DownloadSessionModel.library_item_id` requires
              ``ContentLibrary.DownloadSession``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'create_spec': create_spec,
                            })

    def get(self,
            download_session_id,
            ):
        """
        Gets the download session with the specified identifier, including the
        most up-to-date status information for the session.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session to retrieve.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :rtype: :class:`DownloadSessionModel`
        :return: The :class:`DownloadSessionModel` instance with the given
            ``download_session_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if no download session with the given ``download_session_id``
            exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('get',
                            {
                            'download_session_id': download_session_id,
                            })

    def list(self,
             library_item_id=None,
             ):
        """
        Lists the identifiers of the download sessions created by the calling
        user. Optionally may filter by library item.

        :type  library_item_id: :class:`str` or ``None``
        :param library_item_id:  Library item identifier on which to filter results.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
            If not specified all download session identifiers are listed.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all download sessions created
            by the calling user.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a library item identifier is given for an item which does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.item.DownloadSession``
              referenced by the parameter ``library_item_id`` requires
              ``ContentLibrary.DownloadSession``.
        """
        return self._invoke('list',
                            {
                            'library_item_id': library_item_id,
                            })

    def keep_alive(self,
                   download_session_id,
                   progress=None,
                   ):
        """
        Keeps a download session alive. This operation is allowed only if the
        session is in the :attr:`DownloadSessionModel.State.ACTIVE` state. 
        
        If there is no activity for a download session for a certain period of
        time, the download session will expire. The download session expiration
        timeout is configurable in the Content Library Service system
        configuration. The default is five minutes. Invoking this method
        enables a client to specifically extend the lifetime of an active
        download session.

        :type  download_session_id: :class:`str`
        :param download_session_id: Identifier of the download session whose lifetime should be
            extended.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :type  progress: :class:`long` or ``None``
        :param progress: Optional update to the progress property of the session. If
            specified, the new progress should be greater then the current
            progress. See :attr:`DownloadSessionModel.client_progress`.
            If not specified the progress is not updated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no download session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the download session is not in the
            :attr:`DownloadSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('keep_alive',
                            {
                            'download_session_id': download_session_id,
                            'progress': progress,
                            })

    def cancel(self,
               download_session_id,
               ):
        """
        Cancels the download session. This method will abort any ongoing
        transfers and invalidate transfer urls that the client may be
        downloading from.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifer of the download session that should be canceled.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no download session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the download session is not in the
            :attr:`DownloadSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('cancel',
                            {
                            'download_session_id': download_session_id,
                            })

    def delete(self,
               download_session_id,
               ):
        """
        Deletes a download session. This removes the session and all
        information associated with it. 
        
        Removing a download session leaves any current transfers for that
        session in an indeterminate state (there is no guarantee that the
        transfers will be able to complete). However there will no longer be a
        means of inspecting the status of those downloads except by seeing the
        effect on the library item. 
        
        Download sessions for which there is no download activity or which are
        complete will automatically be expired and then deleted after a period
        of time.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session to be deleted.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the download session does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('delete',
                            {
                            'download_session_id': download_session_id,
                            })

    def fail(self,
             download_session_id,
             client_error_message,
             ):
        """
        Terminates the download session with a client specified error message. 
        
        This is useful in transmitting client side failures (for example, not
        being able to download a file) to the server side.

        :type  download_session_id: :class:`str`
        :param download_session_id:  Identifier of the download session to fail.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.DownloadSession``.
        :type  client_error_message: :class:`str`
        :param client_error_message: Client side error message. This can be useful in providing some
            extra details about the client side failure. Note that the message
            won't be translated to the user's locale.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the download session does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the download session is not in the
            :attr:`DownloadSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('fail',
                            {
                            'download_session_id': download_session_id,
                            'client_error_message': client_error_message,
                            })
class File(VapiInterface):
    """
    The ``File`` class can be used to query for information on the files within
    a library item. Files are objects which are added to a library item through
    the :class:`UpdateSession` and
    :class:`com.vmware.content.library.item.updatesession_client.File` classes.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _FileStub)

    class ChecksumAlgorithm(Enum):
        """
        The ``File.ChecksumAlgorithm`` class defines the valid checksum algorithms.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SHA1 = None
        """
        Checksum algorithm: SHA-1

        """
        MD5 = None
        """
        Checksum algorithm: MD5

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ChecksumAlgorithm` instance.
            """
            Enum.__init__(string)

    ChecksumAlgorithm._set_values([
        ChecksumAlgorithm('SHA1'),
        ChecksumAlgorithm('MD5'),
    ])
    ChecksumAlgorithm._set_binding_type(type.EnumType(
        'com.vmware.content.library.item.file.checksum_algorithm',
        ChecksumAlgorithm))


    class ChecksumInfo(VapiStruct):
        """
        Provides checksums for a :class:`File.Info` object.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     algorithm=None,
                     checksum=None,
                    ):
            """
            :type  algorithm: :class:`File.ChecksumAlgorithm` or ``None``
            :param algorithm: The checksum algorithm (SHA1, MD5) used to calculate the checksum.
                If not specified the default checksum algorithm is
                :attr:`File.ChecksumAlgorithm.SHA1`.
            :type  checksum: :class:`str`
            :param checksum: The checksum value calculated with
                :attr:`File.ChecksumInfo.algorithm`.
            """
            self.algorithm = algorithm
            self.checksum = checksum
            VapiStruct.__init__(self)

    ChecksumInfo._set_binding_type(type.StructType(
        'com.vmware.content.library.item.file.checksum_info', {
            'algorithm': type.OptionalType(type.ReferenceType(__name__, 'File.ChecksumAlgorithm')),
            'checksum': type.StringType(),
        },
        ChecksumInfo,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``File.Info`` class provides information about a file in Content
        Library Service storage. 
        
        A file is an actual stored object for a library item. An item will have
        zero files initially, but one or more can be uploaded to the item.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     checksum_info=None,
                     name=None,
                     size=None,
                     cached=None,
                     version=None,
                    ):
            """
            :type  checksum_info: :class:`File.ChecksumInfo` or ``None``
            :param checksum_info: A checksum for validating the content of the file. 
                
                This value can be used to verify that a transfer was completed
                without errors.
                A checksum cannot always be calculated, and the value will be None
                if the file does not have content.
            :type  name: :class:`str`
            :param name: The name of the file. 
                
                This value will be unique within the library item for each file. It
                cannot be an empty string.
            :type  size: :class:`long`
            :param size: The file size, in bytes. The file size is the storage used and not
                the uploaded or provisioned size. For example, when uploading a
                disk to a datastore, the amount of storage that the disk consumes
                may be different from the disk file size. When the file is not
                cached, the size is 0.
            :type  cached: :class:`bool`
            :param cached: Indicates whether the file is on disk or not.
            :type  version: :class:`str`
            :param version: The version of this file; incremented when a new copy of the file
                is uploaded.
            """
            self.checksum_info = checksum_info
            self.name = name
            self.size = size
            self.cached = cached
            self.version = version
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.content.library.item.file.info', {
            'checksum_info': type.OptionalType(type.ReferenceType(__name__, 'File.ChecksumInfo')),
            'name': type.StringType(),
            'size': type.IntegerType(),
            'cached': type.BooleanType(),
            'version': type.StringType(),
        },
        Info,
        False,
        None))



    def get(self,
            library_item_id,
            name,
            ):
        """
        Retrieves the information for a single file in a library item by its
        name.

        :type  library_item_id: :class:`str`
        :param library_item_id: Identifier of the library item whose file information should be
            returned.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  name: :class:`str`
        :param name: Name of the file in the library item whose information should be
            returned.
        :rtype: :class:`File.Info`
        :return: The :class:`File.Info` object with information on the specified
            file.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``library_item_id`` refers to a library item that does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``name`` refers to a file that does not exist in the library
            item.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'library_item_id': library_item_id,
                            'name': name,
                            })

    def list(self,
             library_item_id,
             ):
        """
        Lists all of the files that are stored within a given library item.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item whose files should be listed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :rtype: :class:`list` of :class:`File.Info`
        :return: The :class:`list` of all of the files that are stored within the
            given library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if ``library_item_id`` refers to a library item that does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'library_item_id': library_item_id,
                            })
class Storage(VapiInterface):
    """
    ``Storage`` is a resource that represents a specific instance of a file
    stored on a storage backing. Unlike :class:`File`, which is abstract,
    storage represents concrete files on the various storage backings. A file
    is only represented once in :class:`File`, but will be represented multiple
    times (once for each storage backing) in ``Storage``. The ``Storage`` class
    provides information on the storage backing and the specific location of
    the file in that backing to privileged users who want direct access to the
    file on the storage medium.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StorageStub)

    class Info(VapiStruct):
        """
        The ``Storage.Info`` class is the expanded form of :class:`File.Info` that
        includes details about the storage backing for a file in a library item.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     storage_backing=None,
                     storage_uris=None,
                     checksum_info=None,
                     name=None,
                     size=None,
                     cached=None,
                     version=None,
                    ):
            """
            :type  storage_backing: :class:`com.vmware.content.library_client.StorageBacking`
            :param storage_backing: The storage backing on which this object resides. This might not be
                the same as the default storage backing associated with the
                library.
            :type  storage_uris: :class:`list` of :class:`str`
            :param storage_uris: URIs that identify the file on the storage backing. 
                
                These URIs may be specific to the backing and may need
                interpretation by the client. A client that understands a URI
                scheme in this list may use that URI to directly access the file on
                the storage backing. This can provide high-performance support for
                file manipulation.
            :type  checksum_info: :class:`File.ChecksumInfo` or ``None``
            :param checksum_info: A checksum for validating the content of the file. 
                
                This value can be used to verify that a transfer was completed
                without errors.
                A checksum cannot always be calculated, and the value will be None
                if the file does not have content.
            :type  name: :class:`str`
            :param name: The name of the file. 
                
                This value will be unique within the library item for each file. It
                cannot be an empty string.
            :type  size: :class:`long`
            :param size: The file size, in bytes. The file size is the storage used and not
                the uploaded or provisioned size. For example, when uploading a
                disk to a datastore, the amount of storage that the disk consumes
                may be different from the disk file size. When the file is not
                cached, the size is 0.
            :type  cached: :class:`bool`
            :param cached: Indicates whether the file is on disk or not.
            :type  version: :class:`str`
            :param version: The version of this file; incremented when a new copy of the file
                is uploaded.
            """
            self.storage_backing = storage_backing
            self.storage_uris = storage_uris
            self.checksum_info = checksum_info
            self.name = name
            self.size = size
            self.cached = cached
            self.version = version
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.content.library.item.storage.info', {
            'storage_backing': type.ReferenceType('com.vmware.content.library_client', 'StorageBacking'),
            'storage_uris': type.ListType(type.URIType()),
            'checksum_info': type.OptionalType(type.ReferenceType(__name__, 'File.ChecksumInfo')),
            'name': type.StringType(),
            'size': type.IntegerType(),
            'cached': type.BooleanType(),
            'version': type.StringType(),
        },
        Info,
        False,
        None))



    def get(self,
            library_item_id,
            file_name,
            ):
        """
        Retrieves the storage information for a specific file in a library
        item.

        :type  library_item_id: :class:`str`
        :param library_item_id: Identifier of the library item whose storage information should be
            retrieved.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  file_name: :class:`str`
        :param file_name: Name of the file for which the storage information should be
            listed.
        :rtype: :class:`list` of :class:`Storage.Info`
        :return: The :class:`list` of all the storage items for the given file
            within the given library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the specified library item does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the specified file does not exist in the given library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.ReadStorage``.
        """
        return self._invoke('get',
                            {
                            'library_item_id': library_item_id,
                            'file_name': file_name,
                            })

    def list(self,
             library_item_id,
             ):
        """
        Lists all storage items for a given library item.

        :type  library_item_id: :class:`str`
        :param library_item_id: Identifier of the library item whose storage information should be
            listed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :rtype: :class:`list` of :class:`Storage.Info`
        :return: The :class:`list` of all storage items for a given library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the specified library item does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.ReadStorage``.
        """
        return self._invoke('list',
                            {
                            'library_item_id': library_item_id,
                            })
class UpdateSession(VapiInterface):
    """
    The ``UpdateSession`` class manipulates sessions that are used to upload
    content into the Content Library Service, and/or to remove files from a
    library item. 
    
    An update session is a resource which tracks changes to content. An update
    session is created with a set of files that are intended to be uploaded to
    a specific :class:`com.vmware.content.library_client.ItemModel`, or removed
    from an item. The session object can be used to track the uploads and
    inspect the changes that are being made to the item by that upload. It can
    also serve as a channel to check on the result of the upload, and status
    messages such as errors and warnings for the upload. 
    
    Modifications are not visible to other clients unless the session is
    completed and all necessary files have been received. 
    
    The management of the files within the session is done through the
    :class:`com.vmware.content.library.item.updatesession_client.File` class.
    """
    RESOURCE_TYPE = "com.vmware.content.library.item.UpdateSession"
    """
    Resource type for an update session.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UpdateSessionStub)


    def create(self,
               create_spec,
               client_token=None,
               ):
        """
        Creates a new update session. An update session is used to make
        modifications to a library item. Modifications are not visible to other
        clients unless the session is completed and all necessary files have
        been received. 
        
        Content Library Service allows only one single update session to be
        active for a specific library item.

        :type  client_token: :class:`str` or ``None``
        :param client_token: Unique token generated by the client for each creation request. The
            token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent creation.
            If not specified creation is not idempotent.
        :type  create_spec: :class:`UpdateSessionModel`
        :param create_spec:  Specification for the new update session to be created.
        :rtype: :class:`str`
        :return: Identifier of the new update session being created.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the session specification is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``client_token`` does not conform to the UUID format.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the update session is being created on a subscribed library
            item.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the item targeted for update does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
             if there is another update session on the same library item.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the attribute :attr:`UpdateSessionModel.library_item_id` requires
              ``ContentLibrary.UpdateSession``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'create_spec': create_spec,
                            })

    def get(self,
            update_session_id,
            ):
        """
        Gets the update session with the specified identifier, including the
        most up-to-date status information for the session.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session to retrieve.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :rtype: :class:`UpdateSessionModel`
        :return: The :class:`UpdateSessionModel` instance with the given
            ``update_session_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no update session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('get',
                            {
                            'update_session_id': update_session_id,
                            })

    def list(self,
             library_item_id=None,
             ):
        """
        Lists the identifiers of the update session created by the calling
        user. Optionally may filter by library item.

        :type  library_item_id: :class:`str` or ``None``
        :param library_item_id:  Optional library item identifier on which to filter results.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
            If not specified the results are not filtered.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all update sessions created by
            the calling user.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a library item identifier is given for an item which does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.item.UpdateSession``
              referenced by the parameter ``library_item_id`` requires
              ``ContentLibrary.UpdateSession``.
        """
        return self._invoke('list',
                            {
                            'library_item_id': library_item_id,
                            })

    def complete(self,
                 update_session_id,
                 ):
        """
        Completes the update session. This indicates that the client has
        finished making all the changes required to the underlying library
        item. If the client is pushing the content to the server, the library
        item will be updated once this call returns. If the server is pulling
        the content, the call may return before the changes become visible. In
        that case, the client can track the session to know when the server is
        done. 
        
        This method requires the session to be in the
        :attr:`UpdateSessionModel.State.ACTIVE` state. 
        
        Depending on the type of the library item associated with this session,
        a type adapter may be invoked to verify the validity of the files
        uploaded. The user can explicitly validate the session before
        completing the session by using the
        :func:`com.vmware.content.library.item.updatesession_client.File.validate`
        method. 
        
        Modifications are not visible to other clients unless the session is
        completed and all necessary files have been received.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session that should be completed.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no update session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is not in the
            :attr:`UpdateSessionModel.State.ACTIVE` state, or if some of the
            files that will be uploaded by the client aren't received
            correctly.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('complete',
                            {
                            'update_session_id': update_session_id,
                            })

    def keep_alive(self,
                   update_session_id,
                   client_progress=None,
                   ):
        """
        Keeps an update session alive. 
        
        If there is no activity for an update session after a period of time,
        the update session will expire, then be deleted. The update session
        expiration timeout is configurable in the Content Library Service
        system configuration. The default is five minutes. Invoking this method
        enables a client to specifically extend the lifetime of the update
        session.

        :type  update_session_id: :class:`str`
        :param update_session_id: Identifier of the update session whose lifetime should be extended.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :type  client_progress: :class:`long` or ``None``
        :param client_progress: Optional update to the progress property of the session. If
            specified, the new progress should be greater then the current
            progress. See :attr:`UpdateSessionModel.client_progress`.
            If not specified the progress is not updated.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no update session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is not in the
            :attr:`UpdateSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('keep_alive',
                            {
                            'update_session_id': update_session_id,
                            'client_progress': client_progress,
                            })

    def cancel(self,
               update_session_id,
               ):
        """
        Cancels the update session and sets its state to
        :attr:`UpdateSessionModel.State.CANCELED`. This method will free up any
        temporary resources currently associated with the session. 
        
         This method is not allowed if the session has been already completed. 
        
        Cancelling an update session will cancel any in progress transfers
        (either uploaded by the client or pulled by the server). Any content
        that has been already received will be scheduled for deletion.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session that should be canceled.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no update session with the given identifier exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is not in the
            :attr:`UpdateSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('cancel',
                            {
                            'update_session_id': update_session_id,
                            })

    def fail(self,
             update_session_id,
             client_error_message,
             ):
        """
        Terminates the update session with a client specified error message. 
        
        This is useful in transmitting client side failures (for example, not
        being able to access a file) to the server side.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifier of the update session to fail.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :type  client_error_message: :class:`str`
        :param client_error_message: Client side error message. This can be useful in providing some
            extra details about the client side failure. Note that the message
            won't be translated to the user's locale.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is not in the
            :attr:`UpdateSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('fail',
                            {
                            'update_session_id': update_session_id,
                            'client_error_message': client_error_message,
                            })

    def delete(self,
               update_session_id,
               ):
        """
        Deletes an update session. This removes the session and all information
        associated with it. 
        
        Removing an update session leaves any current transfers for that
        session in an indeterminate state (there is no guarantee that the
        server will terminate the transfers, or that the transfers can be
        completed). However there will no longer be a means of inspecting the
        status of those uploads except by seeing the effect on the library
        item. 
        
        Update sessions for which there is no upload activity or which are
        complete will automatically be deleted after a period of time.

        :type  update_session_id: :class:`str`
        :param update_session_id:  Identifer of the update session to delete.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.item.UpdateSession``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the update session does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the update session is in the
            :attr:`UpdateSessionModel.State.ACTIVE` state.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Anonymous``.
        """
        return self._invoke('delete',
                            {
                            'update_session_id': update_session_id,
                            })
class _DownloadSessionStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'create_spec': type.ReferenceType(__name__, 'DownloadSessionModel'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'library_item_id': type.OptionalType(type.IdType()),
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

        # properties for keep_alive operation
        keep_alive_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
            'progress': type.OptionalType(type.IntegerType()),
        })
        keep_alive_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        keep_alive_input_value_validator_list = [
        ]
        keep_alive_output_validator_list = [
        ]
        keep_alive_rest_metadata = None

        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for fail operation
        fail_input_type = type.StructType('operation-input', {
            'download_session_id': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
            'client_error_message': type.StringType(),
        })
        fail_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        fail_input_value_validator_list = [
        ]
        fail_output_validator_list = [
        ]
        fail_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.library.item.DownloadSession'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'DownloadSessionModel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
            'keep_alive': {
                'input_type': keep_alive_input_type,
                'output_type': type.VoidType(),
                'errors': keep_alive_error_dict,
                'input_value_validator_list': keep_alive_input_value_validator_list,
                'output_validator_list': keep_alive_output_validator_list,
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fail': {
                'input_type': fail_input_type,
                'output_type': type.VoidType(),
                'errors': fail_error_dict,
                'input_value_validator_list': fail_input_value_validator_list,
                'output_validator_list': fail_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'keep_alive': keep_alive_rest_metadata,
            'cancel': cancel_rest_metadata,
            'delete': delete_rest_metadata,
            'fail': fail_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.download_session',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _FileStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'name': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
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

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'File.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.file',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _StorageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'file_name': type.StringType(),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
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

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Storage.Info')),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Storage.Info')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.storage',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _UpdateSessionStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'create_spec': type.ReferenceType(__name__, 'UpdateSessionModel'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'library_item_id': type.OptionalType(type.IdType()),
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

        # properties for complete operation
        complete_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        complete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        complete_input_value_validator_list = [
        ]
        complete_output_validator_list = [
        ]
        complete_rest_metadata = None

        # properties for keep_alive operation
        keep_alive_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
            'client_progress': type.OptionalType(type.IntegerType()),
        })
        keep_alive_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        keep_alive_input_value_validator_list = [
        ]
        keep_alive_output_validator_list = [
        ]
        keep_alive_rest_metadata = None

        # properties for cancel operation
        cancel_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        cancel_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        cancel_input_value_validator_list = [
        ]
        cancel_output_validator_list = [
        ]
        cancel_rest_metadata = None

        # properties for fail operation
        fail_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
            'client_error_message': type.StringType(),
        })
        fail_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        fail_input_value_validator_list = [
        ]
        fail_output_validator_list = [
        ]
        fail_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'update_session_id': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.library.item.UpdateSession'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'UpdateSessionModel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
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
            'complete': {
                'input_type': complete_input_type,
                'output_type': type.VoidType(),
                'errors': complete_error_dict,
                'input_value_validator_list': complete_input_value_validator_list,
                'output_validator_list': complete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'keep_alive': {
                'input_type': keep_alive_input_type,
                'output_type': type.VoidType(),
                'errors': keep_alive_error_dict,
                'input_value_validator_list': keep_alive_input_value_validator_list,
                'output_validator_list': keep_alive_output_validator_list,
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
            'fail': {
                'input_type': fail_input_type,
                'output_type': type.VoidType(),
                'errors': fail_error_dict,
                'input_value_validator_list': fail_input_value_validator_list,
                'output_validator_list': fail_output_validator_list,
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
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'complete': complete_rest_metadata,
            'keep_alive': keep_alive_rest_metadata,
            'cancel': cancel_rest_metadata,
            'fail': fail_rest_metadata,
            'delete': delete_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item.update_session',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'DownloadSession': DownloadSession,
        'File': File,
        'Storage': Storage,
        'UpdateSession': UpdateSession,
        'downloadsession': 'com.vmware.content.library.item.downloadsession_client.StubFactory',
        'updatesession': 'com.vmware.content.library.item.updatesession_client.StubFactory',
    }

