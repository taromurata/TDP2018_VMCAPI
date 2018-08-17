# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.library.
#---------------------------------------------------------------------------

"""
The Content Library module provides classes and classes for defining and
managing the library's items, subscription, publication, and storage.

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


class ItemModel(VapiStruct):
    """
    The ``ItemModel`` class represents a library item that has been stored in a
    library. 
    
    A ``ItemModel`` represents a single logical unit to be managed within a
    :class:`com.vmware.content_client.LibraryModel`. Items contain the actual
    content of a library, and their placement within a library determines
    policies that affect that content such as publishing. 
    
    A library item can have a specified type, indicated with the
    :attr:`ItemModel.type` attribute. This property is associated with a
    Content Library Service plugin that supports specific types and provides
    additional services. The types available in a specific Content Library
    Service can be queried using the :class:`com.vmware.content_client.Type`
    class. Items of an unknown or unspecified type are treated generically.
    Because subscribed library catalogs are synchronized as is, subscribing to
    a remote Content Library Service effectively gives you a library with the
    functionality of the remote service's type adapter plugins, even if they
    are not installed locally. 
    
    Items can be managed using the :class:`Item` class and, for items in
    subscribed libraries, the :class:`SubscribedItem` class.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 library_id=None,
                 content_version=None,
                 creation_time=None,
                 description=None,
                 last_modified_time=None,
                 last_sync_time=None,
                 metadata_version=None,
                 name=None,
                 cached=None,
                 size=None,
                 type=None,
                 version=None,
                 source_id=None,
                ):
        """
        :type  id: :class:`str`
        :param id: A unique identifier for this library item.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.Item``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.content.library.Item``.
            This attribute is not used for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is not used for the ``update`` method.
        :type  library_id: :class:`str`
        :param library_id: The identifier of the
            :class:`com.vmware.content_client.LibraryModel` to which this item
            belongs.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.Library``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.content.Library``.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  content_version: :class:`str`
        :param content_version: The version of the file content list of this library item.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  creation_time: :class:`datetime.datetime`
        :param creation_time: The date and time when this library item was created.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  description: :class:`str`
        :param description: A human-readable description for this library item.
            This attribute is optional for the ``create`` method. Leaving it
            None during creation will result in an empty string value. It will
            always be present in the result of a ``get`` or ``list`` method. It
            is optional for the ``update`` method. Leaving it None during
            update indicates that the description remains unchanged.
        :type  last_modified_time: :class:`datetime.datetime`
        :param last_modified_time: The date and time when the metadata for this library item was last
            changed. 
            
            This attribute is affected by changes to the properties or file
            content of this item. It is not modified by changes to the tags of
            the item, or by changes to the library which owns this item.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  last_sync_time: :class:`datetime.datetime`
        :param last_sync_time: The date and time when this library item was last synchronized. 
            
            This attribute is updated every time a synchronization is triggered
            on the library item, including when a synchronization is triggered
            on the library to which this item belongs. The value is None for a
            library item that belongs to a local library.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        :type  metadata_version: :class:`str`
        :param metadata_version: A version number for the metadata of this library item. 
            
            This value is incremented with each change to the metadata of this
            item. Changes to name, description, and so on will increment this
            value. The value is not incremented by changes to the content or
            tags of the item or the library which owns it.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  name: :class:`str`
        :param name: A human-readable name for this library item. 
            
            The name may not be None or an empty string. The name does not have
            to be unique, even within the same library.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  cached: :class:`bool`
        :param cached: The status that indicates whether the library item is on disk or
            not. The library item is cached when all its files are on disk.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  size: :class:`long`
        :param size: The library item size, in bytes. The size is the sum of the size
            used on the storage backing for all the files in the item. When the
            library item is not cached, the size is 0.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        :type  type: :class:`str`
        :param type: An optional type identifier which indicates the type adapter plugin
            to use. 
            
            This attribute may be set to a non-empty string value that
            corresponds to an identifier supported by a type adapter plugin
            present in the Content Library Service. A type adapter plugin, if
            present for the specified type, can provide additional information
            and services around the item content. A type adapter can guide the
            upload process by creating file entries that are in need of being
            uploaded to complete an item. 
            
            The types and plugins supported by the Content Library Service can
            be queried using the :class:`com.vmware.content_client.Type` class.
            This attribute is optional for the ``create`` and ``update``
            methods. During creation, if the type is left unspecified, or if
            the type is specified but does not have a corresponding type
            support plugin, then the type of the library item is considered to
            be generic and all data is treated as generic files. During update,
            if the type is not specified, then it is not updated.
        :type  version: :class:`str`
        :param version: A version number that is updated on metadata changes. This value is
            used to validate update requests to provide optimistic concurrency
            of changes. 
            
            This value represents a number that is incremented every time
            library item properties, such as name or description, are changed.
            It is not incremented by changes to the file content of the library
            item, including adding or removing files. It is also not affected
            by tagging the library item.
            This attribute is not used for the ``create`` method. It will
            always be present in the result of a ``get`` or ``list`` method. It
            is optional for the ``update`` method. Leaving it None during
            update indicates that you do not need to detect concurrent updates.
        :type  source_id: :class:`str`
        :param source_id: The identifier of the :class:`ItemModel` to which this item is
            synchronized to if the item belongs to a subscribed library. The
            value is None for a library item that belongs to a local library.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.library.Item``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.content.library.Item``.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        """
        self.id = id
        self.library_id = library_id
        self.content_version = content_version
        self.creation_time = creation_time
        self.description = description
        self.last_modified_time = last_modified_time
        self.last_sync_time = last_sync_time
        self.metadata_version = metadata_version
        self.name = name
        self.cached = cached
        self.size = size
        self.type = type
        self.version = version
        self.source_id = source_id
        VapiStruct.__init__(self)

ItemModel._set_binding_type(type.StructType(
    'com.vmware.content.library.item_model', {
        'id': type.OptionalType(type.IdType()),
        'library_id': type.OptionalType(type.IdType()),
        'content_version': type.OptionalType(type.StringType()),
        'creation_time': type.OptionalType(type.DateTimeType()),
        'description': type.OptionalType(type.StringType()),
        'last_modified_time': type.OptionalType(type.DateTimeType()),
        'last_sync_time': type.OptionalType(type.DateTimeType()),
        'metadata_version': type.OptionalType(type.StringType()),
        'name': type.OptionalType(type.StringType()),
        'cached': type.OptionalType(type.BooleanType()),
        'size': type.OptionalType(type.IntegerType()),
        'type': type.OptionalType(type.StringType()),
        'version': type.OptionalType(type.StringType()),
        'source_id': type.OptionalType(type.IdType()),
    },
    ItemModel,
    True,
    ["id"]))



class OptimizationInfo(VapiStruct):
    """
    The ``OptimizationInfo`` class defines different optimizations and
    optimization parameters applied to particular library.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 optimize_remote_publishing=None,
                ):
        """
        :type  optimize_remote_publishing: :class:`bool`
        :param optimize_remote_publishing: If set to ``true`` then library would be optimized for remote
            publishing. 
            
            Turn it on if remote publishing is dominant use case for this
            library. Remote publishing means here that publisher and
            subscribers are not the part of the same ``Vcenter`` SSO domain. 
            
            Any optimizations could be done as result of turning on this
            optimization during library creation. For example, library content
            could be stored in different format but optimizations are not
            limited to just storage format. 
            
            Note, that value of this toggle could be set only during creation
            of the library and you would need to migrate your library in case
            you need to change this value (optimize the library for different
            use case).
            This attribute is optional for the ``create`` method. If not
            specified for the ``create``, the default is for the library to not
            be optmized for specific use case. It is not used for the
            ``update`` method.
        """
        self.optimize_remote_publishing = optimize_remote_publishing
        VapiStruct.__init__(self)

OptimizationInfo._set_binding_type(type.StructType(
    'com.vmware.content.library.optimization_info', {
        'optimize_remote_publishing': type.OptionalType(type.BooleanType()),
    },
    OptimizationInfo,
    False,
    None))



class PublishInfo(VapiStruct):
    """
    The ``PublishInfo`` class defines how a local library is published publicly
    for synchronization to other libraries.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 authentication_method=None,
                 published=None,
                 publish_url=None,
                 user_name=None,
                 password=None,
                 current_password=None,
                 persist_json_enabled=None,
                ):
        """
        :type  authentication_method: :class:`PublishInfo.AuthenticationMethod`
        :param authentication_method: Indicates how a subscribed library should authenticate (BASIC,
            NONE) to the published library endpoint.
            This attribute is required for the
            :func:`com.vmware.content_client.LocalLibrary.create` method. It is
            optional for the
            :func:`com.vmware.content_client.LocalLibrary.update` operation,
            and if None the value will not be changed. When the existing
            authentication method is
            :attr:`PublishInfo.AuthenticationMethod.BASIC` and authentication
            is being turned off by updating this attribute to
            :attr:`PublishInfo.AuthenticationMethod.NONE`, then the
            :attr:`PublishInfo.current_password` attribute is required. This
            attribute will always be present in the results of the
            :func:`com.vmware.content_client.LocalLibrary.get` method.
        :type  published: :class:`bool`
        :param published: Whether the local library is published.
            This attribute is required for the
            :func:`com.vmware.content_client.LocalLibrary.create` method. It is
            optional for the
            :func:`com.vmware.content_client.LocalLibrary.update` operation,
            and if None the value will not be changed. When the existing
            authentication method is
            :attr:`PublishInfo.AuthenticationMethod.BASIC` and the local
            library is published, the :attr:`PublishInfo.current_password`
            attribute is required before turning off publishing. This attribute
            will always be present in the results of the
            :func:`com.vmware.content_client.LocalLibrary.get` method.
        :type  publish_url: :class:`str`
        :param publish_url: The URL to which the library metadata is published by the Content
            Library Service. 
            
            This value can be used to set the
            :attr:`SubscriptionInfo.subscription_url` property when creating a
            subscribed library.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  user_name: :class:`str`
        :param user_name: The username to require for authentication.
            This attribute is optional for the
            :func:`com.vmware.content_client.LocalLibrary.create` and
            :func:`com.vmware.content_client.LocalLibrary.update` methods. When
            the authentication method is
            :attr:`PublishInfo.AuthenticationMethod.NONE`, the username can be
            left None. When the authentication method is
            :attr:`PublishInfo.AuthenticationMethod.BASIC`, the username is
            ignored in the current release. It defaults to "vcsp". It is
            preferable to leave this None. If specified, it must be set to
            "vcsp".
        :type  password: :class:`str`
        :param password: The new password to require for authentication.
            This attribute is optional for the
            :func:`com.vmware.content_client.LocalLibrary.create` method. When
            the authentication method is
            :attr:`PublishInfo.AuthenticationMethod.NONE`, the password can be
            left None. When the authentication method is
            :attr:`PublishInfo.AuthenticationMethod.BASIC`, the password should
            be a non-empty string. This attribute is optional for the
            :func:`com.vmware.content_client.LocalLibrary.update` method.
            Leaving it None during update indicates that the password is not
            changed. When the password is changed, the
            :attr:`PublishInfo.current_password` attribute is required. This
            attribute is not used for the
            :func:`com.vmware.content_client.LocalLibrary.get` method.
        :type  current_password: :class:`str`
        :param current_password: The current password to verify. This attribute is available
            starting in vSphere 6.7.
            This attribute is unused for the
            :func:`com.vmware.content_client.LocalLibrary.create` method. This
            attribute is optional for the
            :func:`com.vmware.content_client.LocalLibrary.update` method. When
            the existing authentication method is
            :attr:`PublishInfo.AuthenticationMethod.NONE`, the current password
            can be left None. When the existing authentication method is
            :attr:`PublishInfo.AuthenticationMethod.BASIC`, the current
            password is verified before applying the new
            :attr:`PublishInfo.password`, turning off authentication, or
            unpublishing the library. This attribute is not used for the
            :func:`com.vmware.content_client.LocalLibrary.get` method.
        :type  persist_json_enabled: :class:`bool`
        :param persist_json_enabled: Whether library and library item metadata are persisted in the
            storage backing as JSON files. This flag only applies if the local
            library is published. 
            
            Enabling JSON persistence allows you to synchronize a subscribed
            library manually instead of over HTTP. You copy the local library
            content and metadata to another storage backing manually and then
            create a subscribed library referencing the location of the library
            JSON file in the :attr:`SubscriptionInfo.subscription_url`. When
            the subscribed library's storage backing matches the subscription
            URL, files do not need to be copied to the subscribed library. 
            
            For a library backed by a datastore, the library JSON file will be
            stored at the path contentlib-{library_id}/lib.json on the
            datastore. 
            
            For a library backed by a remote file system, the library JSON file
            will be stored at {library_id}/lib.json in the remote file system
            path.
            This attribute is optional for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        """
        self.authentication_method = authentication_method
        self.published = published
        self.publish_url = publish_url
        self.user_name = user_name
        self.password = password
        self.current_password = current_password
        self.persist_json_enabled = persist_json_enabled
        VapiStruct.__init__(self)

    class AuthenticationMethod(Enum):
        """
        The ``PublishInfo.AuthenticationMethod`` class indicates how a subscribed
        library should authenticate to the published library endpoint.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BASIC = None
        """
        Require HTTP Basic authentication matching a specified username and
        password.

        """
        NONE = None
        """
        Require no authentication.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`AuthenticationMethod` instance.
            """
            Enum.__init__(string)

    AuthenticationMethod._set_values([
        AuthenticationMethod('BASIC'),
        AuthenticationMethod('NONE'),
    ])
    AuthenticationMethod._set_binding_type(type.EnumType(
        'com.vmware.content.library.publish_info.authentication_method',
        AuthenticationMethod))

PublishInfo._set_binding_type(type.StructType(
    'com.vmware.content.library.publish_info', {
        'authentication_method': type.OptionalType(type.ReferenceType(__name__, 'PublishInfo.AuthenticationMethod')),
        'published': type.OptionalType(type.BooleanType()),
        'publish_url': type.OptionalType(type.URIType()),
        'user_name': type.OptionalType(type.StringType()),
        'password': type.OptionalType(type.SecretType()),
        'current_password': type.OptionalType(type.SecretType()),
        'persist_json_enabled': type.OptionalType(type.BooleanType()),
    },
    PublishInfo,
    False,
    None))



class StorageBacking(VapiStruct):
    """
    The ``StorageBacking`` class defines a storage location where content in a
    library will be stored. The storage location can either be a Datastore or
    Other type.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'type',
            {
                'DATASTORE' : [('datastore_id', False)],
                'OTHER' : [('storage_uri', False)],
            }
        ),
    ]



    def __init__(self,
                 type=None,
                 datastore_id=None,
                 storage_uri=None,
                ):
        """
        :type  type: :class:`StorageBacking.Type`
        :param type: Type (DATASTORE, OTHER) of :class:`StorageBacking`.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  datastore_id: :class:`str`
        :param datastore_id: Identifier of the datastore used to store the content in the
            library.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``Datastore``. When methods return a value of this class as a
            return value, the attribute will be an identifier for the resource
            type: ``Datastore``.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`StorageBacking.Type.DATASTORE`.
        :type  storage_uri: :class:`str`
        :param storage_uri: URI identifying the location used to store the content in the
            library. 
            
             The following URI formats are supported: 
            
             vSphere 6.5 
            
            * nfs://server/path?version=4 (for vCenter Server Appliance only) -
              Specifies an NFS Version 4 server.
            * nfs://server/path (for vCenter Server Appliance only) - Specifies
              an NFS Version 3 server. The nfs://server:/path format is also
              supported.
            * smb://server/path - Specifies an SMB server or Windows share.
            
             
            
             vSphere 6.0 Update 1 
            
            * nfs://server:/path (for vCenter Server Appliance only)
            * file://unc-server/path (for vCenter Server for Windows only)
            * file:///mount/point (for vCenter Server Appliance only) - Local
              file URIs are supported only when the path is a local mount point
              for an NFS file system. Use of file URIs is strongly discouraged.
              Instead, use an NFS URI to specify the remote file system.
            
             
            
             vSphere 6.0 
            
            * nfs://server:/path (for vCenter Server Appliance only)
            * file://unc-server/path (for vCenter Server for Windows only)
            * file:///path - Local file URIs are supported but strongly
              discouraged because it may interfere with the performance of
              vCenter Server.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`StorageBacking.Type.OTHER`.
        """
        self.type = type
        self.datastore_id = datastore_id
        self.storage_uri = storage_uri
        VapiStruct.__init__(self)

    class Type(Enum):
        """
        The ``StorageBacking.Type`` class specifies the type of the
        :class:`StorageBacking`.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        DATASTORE = None
        """
        The content of the library will be stored on a datastore. 
        
        These are vCenter Server managed datastores, and are logical containers
        that hide specifics of each storage device. Depending on the type of
        storage you use, datastores can be backed by the following file system
        formats: 
        
        * Virtual Machine File System (VMFS)
        * Network File System (NFS)
        
         

        """
        OTHER = None
        """
        The content of the library will be stored on a remote file system. 
        
         Supports the following remote file systems: 
        
        * NFS (on vCenter Server Appliance)
        * SMB (on vCenter Server Appliance and vCenter Server for Windows)
        
         

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('DATASTORE'),
        Type('OTHER'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.content.library.storage_backing.type',
        Type))

StorageBacking._set_binding_type(type.StructType(
    'com.vmware.content.library.storage_backing', {
        'type': type.OptionalType(type.ReferenceType(__name__, 'StorageBacking.Type')),
        'datastore_id': type.OptionalType(type.IdType()),
        'storage_uri': type.OptionalType(type.URIType()),
    },
    StorageBacking,
    False,
    None))



class SubscriptionInfo(VapiStruct):
    """
    The ``SubscriptionInfo`` class defines the subscription behavior for a
    subscribed library.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 authentication_method=None,
                 automatic_sync_enabled=None,
                 on_demand=None,
                 password=None,
                 ssl_thumbprint=None,
                 subscription_url=None,
                 user_name=None,
                ):
        """
        :type  authentication_method: :class:`SubscriptionInfo.AuthenticationMethod`
        :param authentication_method: Indicate how the subscribed library should authenticate (BASIC,
            NONE) with the published library endpoint.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  automatic_sync_enabled: :class:`bool`
        :param automatic_sync_enabled: Whether the library should participate in automatic library
            synchronization. In order for automatic synchronization to happen,
            the global
            :attr:`com.vmware.content_client.ConfigurationModel.automatic_sync_enabled`
            option must also be true. The subscription is still active even
            when automatic synchronization is turned off, but synchronization
            is only activated with an explicit call to
            :func:`com.vmware.content_client.SubscribedLibrary.sync` or
            :func:`SubscribedItem.sync`. In other words, manual synchronization
            is still available even when automatic synchronization is disabled.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  on_demand: :class:`bool`
        :param on_demand: Indicates whether a library item's content will be synchronized
            only on demand. 
            
            If this is set to ``true``, then the library item's metadata will
            be synchronized but the item's content (its files) will not be
            synchronized. The Content Library Service will synchronize the
            content upon request only. This can cause the first use of the
            content to have a noticeable delay. 
            
            Items without synchronized content can be forcefully synchronized
            in advance using the :func:`SubscribedItem.sync` call with
            ``forceSyncContent`` set to true. Once content has been
            synchronized, the content can removed with the
            :func:`SubscribedItem.evict` call. 
            
            If this value is set to ``false``, all content will be synchronized
            in advance.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  password: :class:`str`
        :param password: The password to use when authenticating. 
            
            The password must be set when using a password-based authentication
            method; empty strings are not allowed.
            This attribute is optional for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is optional for the ``update`` method.
        :type  ssl_thumbprint: :class:`str`
        :param ssl_thumbprint: An optional SHA-1 hash of the SSL certificate for the remote
            endpoint. 
            
            If this value is defined the SSL certificate will be verified by
            comparing it to the SSL thumbprint. The SSL certificate must verify
            against the thumbprint. When specified, the standard certificate
            chain validation behavior is not used. The certificate chain is
            validated normally if this value is None.
            This attribute is optional for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is optional for the ``update`` method.
        :type  subscription_url: :class:`str`
        :param subscription_url: The URL of the endpoint where the metadata for the remotely
            published library is being served. 
            
            This URL can be the :attr:`PublishInfo.publish_url` of the
            published library (for example, https://server/path/lib.json). 
            
            If the source content comes from a published library with
            :attr:`PublishInfo.persist_json_enabled`, the subscription URL can
            be a URL pointing to the library JSON file on a datastore or remote
            file system. The supported formats are: 
            
             vSphere 6.5 
            
            * ds:///vmfs/volumes/{uuid}/mylibrary/lib.json (for datastore)
            * nfs://server/path/mylibrary/lib.json (for NFSv3 server on vCenter
              Server Appliance)
            * nfs://server/path/mylibrary/lib.json?version=4 (for NFSv4 server
              on vCenter Server Appliance)
            * smb://server/path/mylibrary/lib.json (for SMB server)
            
             
            
             vSphere 6.0 
            
            * file://server/mylibrary/lib.json (for UNC server on vCenter
              Server for Windows)
            * file:///path/mylibrary/lib.json (for local file system)
            
             
            
            When you specify a DS subscription URL, the datastore must be on
            the same vCenter Server as the subscribed library. When you specify
            an NFS or SMB subscription URL, the
            :attr:`StorageBacking.storage_uri` of the subscribed library must
            be on the same remote file server and should share a common parent
            path with the subscription URL.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  user_name: :class:`str`
        :param user_name: The username to use when authenticating. 
            
            The username must be set when using a password-based authentication
            method. Empty strings are allowed for usernames.
            This attribute is optional for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is optional for the ``update`` method.
        """
        self.authentication_method = authentication_method
        self.automatic_sync_enabled = automatic_sync_enabled
        self.on_demand = on_demand
        self.password = password
        self.ssl_thumbprint = ssl_thumbprint
        self.subscription_url = subscription_url
        self.user_name = user_name
        VapiStruct.__init__(self)

    class AuthenticationMethod(Enum):
        """
        Indicate how the subscribed library should authenticate with the published
        library endpoint.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BASIC = None
        """
        Require HTTP Basic authentication matching a specified username and
        password.

        """
        NONE = None
        """
        Require no authentication.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`AuthenticationMethod` instance.
            """
            Enum.__init__(string)

    AuthenticationMethod._set_values([
        AuthenticationMethod('BASIC'),
        AuthenticationMethod('NONE'),
    ])
    AuthenticationMethod._set_binding_type(type.EnumType(
        'com.vmware.content.library.subscription_info.authentication_method',
        AuthenticationMethod))

SubscriptionInfo._set_binding_type(type.StructType(
    'com.vmware.content.library.subscription_info', {
        'authentication_method': type.OptionalType(type.ReferenceType(__name__, 'SubscriptionInfo.AuthenticationMethod')),
        'automatic_sync_enabled': type.OptionalType(type.BooleanType()),
        'on_demand': type.OptionalType(type.BooleanType()),
        'password': type.OptionalType(type.SecretType()),
        'ssl_thumbprint': type.OptionalType(type.StringType()),
        'subscription_url': type.OptionalType(type.URIType()),
        'user_name': type.OptionalType(type.StringType()),
    },
    SubscriptionInfo,
    False,
    None))



class Item(VapiInterface):
    """
    The ``Item`` class provides methods for managing library items.
    """
    RESOURCE_TYPE = "com.vmware.content.library.Item"
    """
    Resource type for item.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ItemStub)

    class FindSpec(VapiStruct):
        """
        The ``Item.FindSpec`` class specifies the properties that can be used as a
        filter to find library items. When multiple attributes are specified, all
        properties of the item must match the specification.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     library_id=None,
                     source_id=None,
                     type=None,
                     cached=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: The name of the library item. The name is case-insensitive. See
                :attr:`ItemModel.name`.
                If not specified all library item names are searched.
            :type  library_id: :class:`str` or ``None``
            :param library_id: The identifier of the library containing the item. See
                :attr:`ItemModel.library_id`.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.Library``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.content.Library``.
                If not specified all libraries are searched.
            :type  source_id: :class:`str` or ``None``
            :param source_id: The identifier of the library item as reported by the publisher.
                See :attr:`ItemModel.source_id`.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.content.library.Item``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.content.library.Item``.
                If not specified all library items are searched.
            :type  type: :class:`str` or ``None``
            :param type: The type of the library item. The type is case-insensitive. See
                :attr:`ItemModel.type`.
                If not specified all types are searched.
            :type  cached: :class:`bool` or ``None``
            :param cached: Whether the item is cached. Possible values are 'true' or 'false'.
                See :attr:`ItemModel.cached`.
                If not specified all library items are searched.
            """
            self.name = name
            self.library_id = library_id
            self.source_id = source_id
            self.type = type
            self.cached = cached
            VapiStruct.__init__(self)

    FindSpec._set_binding_type(type.StructType(
        'com.vmware.content.library.item.find_spec', {
            'name': type.OptionalType(type.StringType()),
            'library_id': type.OptionalType(type.IdType()),
            'source_id': type.OptionalType(type.IdType()),
            'type': type.OptionalType(type.StringType()),
            'cached': type.OptionalType(type.BooleanType()),
        },
        FindSpec,
        False,
        None))



    def copy(self,
             source_library_item_id,
             destination_create_spec,
             client_token=None,
             ):
        """
        Copies a library item. 
        
        Copying a library item allows a duplicate to be made within the same or
        different library. The copy occurs by first creating a new library
        item, whose identifier is returned. The content of the library item is
        then copied asynchronously. This copy can be tracked as a task. 
        
        If the copy fails, Content Library Service will roll back the copy by
        deleting any content that was already copied, and removing the new
        library item. A failure during rollback may require manual cleanup by
        an administrator. 
        
         A library item cannot be copied into a subscribed library.

        :type  client_token: :class:`str` or ``None``
        :param client_token: A unique token generated on the client for each copy request. The
            token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent copy.
            If not specified copy is not idempotent.
        :type  source_library_item_id: :class:`str`
        :param source_library_item_id: Identifier of the existing library item from which the content will
            be copied.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  destination_create_spec: :class:`ItemModel`
        :param destination_create_spec:  Specification for the new library item to be created.
        :rtype: :class:`str`
        :return: The identifier of the new library item into which the content is
            being copied.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item with ``source_library_item_id`` does not exist,
            or if the library referenced by the :attr:`ItemModel.library_id`
            property of ``destination_create_spec`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if one of the following is true for the new library item: 
            
            * name is empty
            * name exceeds 80 characters
            * description exceeds 1024 characters
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``client_token`` does not conform to the UUID format.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the :attr:`ItemModel.library_id` property of
            ``destination_create_spec`` refers to a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the copy operation failed because the source or destination
            library item is not accessible.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the source library item specified by
            ``source_library_item_id``, or the content of the target library
            specified by the library ID (see :attr:`ItemModel.library_id`)
            property of ``destination_create_spec`` has been deleted from the
            storage backings (see null) associated with it.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``source_library_item_id`` requires ``System.Read``.
            * The resource ``com.vmware.content.Library`` referenced by the
              attribute :attr:`ItemModel.library_id` requires
              ``ContentLibrary.AddLibraryItem``.
        """
        return self._invoke('copy',
                            {
                            'client_token': client_token,
                            'source_library_item_id': source_library_item_id,
                            'destination_create_spec': destination_create_spec,
                            })

    def create(self,
               create_spec,
               client_token=None,
               ):
        """
        Creates a new library item. 
        
        A new library item is created without any content. After creation,
        content can be added through the
        :class:`com.vmware.content.library.item_client.UpdateSession` and
        :class:`com.vmware.content.library.item.updatesession_client.File`
        classes. 
        
         A library item cannot be created in a subscribed library.

        :type  client_token: :class:`str` or ``None``
        :param client_token: A unique token generated on the client for each creation request.
            The token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent creation.
            If not specified creation is not idempotent.
        :type  create_spec: :class:`ItemModel`
        :param create_spec:  Specification that defines the properties of the new library item.
        :rtype: :class:`str`
        :return: Identifier of the new library item.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the :attr:`ItemModel.library_id` property of ``create_spec``
            refers to a library that does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if one of the following is true for the new library item: 
            
            * name is empty
            * name exceeds 80 characters
            * description exceeds 1024 characters
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``client_token`` does not conform to the UUID format.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the :attr:`ItemModel.library_id` property of
            ``destinationCreateSpec`` refers to a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the library specified by the library ID (see
            :attr:`ItemModel.library_id`) property of ``create_spec`` has been
            deleted from the storage backings (see null) associated with it.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              attribute :attr:`ItemModel.library_id` requires
              ``ContentLibrary.AddLibraryItem``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'create_spec': create_spec,
                            })

    def delete(self,
               library_item_id,
               ):
        """
        Deletes a library item. 
        
        This method will immediately remove the item from the library that owns
        it. The content of the item will be asynchronously removed from the
        storage backings. The content deletion can be tracked with a task. In
        the event that the task fails, an administrator may need to manually
        remove the files from the storage backing. 
        
        This method cannot be used to delete a library item that is a member of
        a subscribed library. Removing an item from a subscribed library
        requires deleting the item from the original published local library
        and syncing the subscribed library.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item to delete.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library item with the given ``library_item_id`` is a member
            of a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item with the specified ``library_item_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.DeleteLibraryItem``.
        """
        return self._invoke('delete',
                            {
                            'library_item_id': library_item_id,
                            })

    def get(self,
            library_item_id,
            ):
        """
        Returns the :class:`ItemModel` with the given identifier.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item to return.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :rtype: :class:`ItemModel`
        :return: The :class:`ItemModel` instance with the given ``library_item_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if no item with the given ``library_item_id`` exists.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'library_item_id': library_item_id,
                            })

    def list(self,
             library_id,
             ):
        """
        Returns the identifiers of all items in the given library.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the library whose items should be returned.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of the items in the library
            specified by ``library_id``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library associated with ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``System.Read``.
        """
        return self._invoke('list',
                            {
                            'library_id': library_id,
                            })

    def find(self,
             spec,
             ):
        """
        Returns identifiers of all the visible (as determined by authorization
        policy) library items matching the requested :class:`Item.FindSpec`.

        :type  spec: :class:`Item.FindSpec`
        :param spec:  Specification describing what properties to filter on.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all the visible library items
            matching the given ``spec``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if no properties are specified in the ``spec``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``com.vmware.content.Library`` referenced by the
              attribute :attr:`Item.FindSpec.library_id` requires
              ``System.Read``.
        """
        return self._invoke('find',
                            {
                            'spec': spec,
                            })

    def update(self,
               library_item_id,
               update_spec,
               ):
        """
        Updates the specified properties of a library item. 
        
        This is an incremental update to the library item. Attributes that are
        None in the update specification are left unchanged. 
        
        This method cannot update a library item that is a member of a
        subscribed library. Those items must be updated in the source published
        library and synchronized to the subscribed library.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item to update.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  update_spec: :class:`ItemModel`
        :param update_spec:  Specification of the properties to set.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``library_item_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library item corresponding to ``library_item_id`` is a
            member of a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if one of the following is true for the ``update_spec``: 
            
            * name is empty
            * name exceeds 80 characters
            * description exceeds 1024 characters
            * version is not equal to the current version of the library item
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the library item belongs to a published library with JSON
            persistence enabled (see :attr:`PublishInfo.persist_json_enabled`)
            and the content of the library item specified by
            ``library_item_id`` has been deleted from the storage backings (see
            null) associated with it.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.UpdateLibraryItem``.
        """
        return self._invoke('update',
                            {
                            'library_item_id': library_item_id,
                            'update_spec': update_spec,
                            })
class SubscribedItem(VapiInterface):
    """
    The ``SubscribedItem`` class manages the unique features of library items
    that are members of a subscribed library.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SubscribedItemStub)


    def evict(self,
              library_item_id,
              ):
        """
        Evicts the cached content of a library item in a subscribed library. 
        
        This method allows the cached content of a library item to be removed
        to free up storage capacity. This method will only work when a library
        item is synchronized on-demand. When a library is not synchronized
        on-demand, it always attempts to keep its cache up-to-date with the
        published source. Evicting the library item will set
        :attr:`ItemModel.cached` to false.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item whose content should be evicted.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``library_item_id`` does not
            exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library item specified by ``library_item_id`` is not a
            member of a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementConfiguration` 
            if the library item specified by ``library_item_id`` is a member of
            a subscribed library that does not synchronize on-demand.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the library item specified by ``library_item_id``
            has been deleted from the storage backings (see null) associated
            with it. 
            
            For instance, this {\\\\@term error) is reported on evicting a
            library item in an on-demand subscribed library that was restored
            from backup, and the library item was deleted after backup, thus
            resulting in its content being deleted from the associated storage
            backings. In this scenario, the metadata of the library item is
            present on a restore, while its content has been deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.EvictLibraryItem``.
        """
        return self._invoke('evict',
                            {
                            'library_item_id': library_item_id,
                            })

    def sync(self,
             library_item_id,
             force_sync_content,
             ):
        """
        Forces the synchronization of an individual library item in a
        subscribed library. 
        
        Synchronizing an individual item will update that item's metadata from
        the remote source. If the source library item on the remote library has
        been deleted, this method will delete the library item from the
        subscribed library as well. 
        
        The default behavior of the synchronization is determined by the
        :class:`SubscriptionInfo` of the library which owns the library item. 
        
        * If :attr:`SubscriptionInfo.on_demand` is true, then the file content
          is not synchronized by default. In this case, only the library item
          metadata is synchronized. The file content may still be forcefully
          synchronized by passing true for the ``force_sync_content`` parameter.
        * If :attr:`SubscriptionInfo.on_demand` is false, then this call will
          always synchronize the file content. The ``force_sync_content``
          parameter is ignored when the subscription is not on-demand.
        
        When the file content has been synchronized, the
        :attr:`ItemModel.cached` attribute will be true. 
        
        This method will return immediately and create an asynchronous task to
        perform the synchronization.

        :type  library_item_id: :class:`str`
        :param library_item_id:  Identifier of the library item to synchronize.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.library.Item``.
        :type  force_sync_content: :class:`bool`
        :param force_sync_content: Whether to synchronize file content as well as metadata. This
            parameter applies only if the subscription is on-demand.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the library item specified by ``library_item_id`` could not be
            found.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library item specified by ``library_item_id`` is not a
            member of a subscribed library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the library item specified by ``library_item_id``
            has been deleted from the storage backings (see null) associated
            with it. 
            
            For instance, this {\\\\@term error) is reported on synchronizing a
            library item in a subscribed library that was restored from backup,
            and the library item was deleted after backup, thus resulting in
            its content being deleted from the associated storage backings. In
            this scenario, the metadata of the library item is present on a
            restore, while its content has been deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.library.Item`` referenced by
              the parameter ``library_item_id`` requires
              ``ContentLibrary.SyncLibraryItem``.
        """
        return self._invoke('sync',
                            {
                            'library_item_id': library_item_id,
                            'force_sync_content': force_sync_content,
                            })
class _ItemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for copy operation
        copy_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'source_library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'destination_create_spec': type.ReferenceType(__name__, 'ItemModel'),
        })
        copy_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        copy_input_value_validator_list = [
        ]
        copy_output_validator_list = [
        ]
        copy_rest_metadata = None

        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'create_spec': type.ReferenceType(__name__, 'ItemModel'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
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
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
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

        # properties for find operation
        find_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Item.FindSpec'),
        })
        find_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        find_input_value_validator_list = [
        ]
        find_output_validator_list = [
        ]
        find_rest_metadata = None

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'update_spec': type.ReferenceType(__name__, 'ItemModel'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        operations = {
            'copy': {
                'input_type': copy_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.library.Item'),
                'errors': copy_error_dict,
                'input_value_validator_list': copy_input_value_validator_list,
                'output_validator_list': copy_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.library.Item'),
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
                'output_type': type.ReferenceType(__name__, 'ItemModel'),
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
            'find': {
                'input_type': find_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': find_error_dict,
                'input_value_validator_list': find_input_value_validator_list,
                'output_validator_list': find_output_validator_list,
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
        }
        rest_metadata = {
            'copy': copy_rest_metadata,
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'find': find_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.item',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SubscribedItemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for evict operation
        evict_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
        })
        evict_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.invalid_element_configuration':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementConfiguration'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        evict_input_value_validator_list = [
        ]
        evict_output_validator_list = [
        ]
        evict_rest_metadata = None

        # properties for sync operation
        sync_input_type = type.StructType('operation-input', {
            'library_item_id': type.IdType(resource_types='com.vmware.content.library.Item'),
            'force_sync_content': type.BooleanType(),
        })
        sync_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        sync_input_value_validator_list = [
        ]
        sync_output_validator_list = [
        ]
        sync_rest_metadata = None

        operations = {
            'evict': {
                'input_type': evict_input_type,
                'output_type': type.VoidType(),
                'errors': evict_error_dict,
                'input_value_validator_list': evict_input_value_validator_list,
                'output_validator_list': evict_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'sync': {
                'input_type': sync_input_type,
                'output_type': type.VoidType(),
                'errors': sync_error_dict,
                'input_value_validator_list': sync_input_value_validator_list,
                'output_validator_list': sync_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'evict': evict_rest_metadata,
            'sync': sync_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library.subscribed_item',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Item': Item,
        'SubscribedItem': SubscribedItem,
        'item': 'com.vmware.content.library.item_client.StubFactory',
    }

