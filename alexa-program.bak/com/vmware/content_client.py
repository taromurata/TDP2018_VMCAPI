# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.content.
#---------------------------------------------------------------------------

"""
The Content module provides classes and classes for configuring global settings
and permissions, and for managing libraries in the Content Library Service.

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


class ConfigurationModel(VapiStruct):
    """
    The ``ConfigurationModel`` class defines the global settings of the Content
    Library Service.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 automatic_sync_enabled=None,
                 automatic_sync_start_hour=None,
                 automatic_sync_stop_hour=None,
                 maximum_concurrent_item_syncs=None,
                ):
        """
        :type  automatic_sync_enabled: :class:`bool`
        :param automatic_sync_enabled: Whether automatic synchronization is enabled. 
            
            When automatic synchronization is enabled, the Content Library
            Service will automatically synchronize all subscribed libraries on
            a daily basis. Subscribed libraries with the
            :attr:`com.vmware.content.library_client.SubscriptionInfo.automatic_sync_enabled`
            flag turned on will be synchronized every hour between
            :attr:`ConfigurationModel.automatic_sync_start_hour` and
            :attr:`ConfigurationModel.automatic_sync_stop_hour`.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  automatic_sync_start_hour: :class:`long`
        :param automatic_sync_start_hour: The hour at which the automatic synchronization will start. This
            value is between 0 (midnight) and 23 inclusive.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  automatic_sync_stop_hour: :class:`long`
        :param automatic_sync_stop_hour: The hour at which the automatic synchronization will stop. Any
            active synchronization operation will continue to run, however no
            new synchronization operations will be triggered after the stop
            hour. This value is between 0 (midnight) and 23 inclusive.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  maximum_concurrent_item_syncs: :class:`long`
        :param maximum_concurrent_item_syncs: The maximum allowed number of library items to synchronize
            concurrently from remote libraries. This must be a positive number.
            The service may not be able to guarantee the requested concurrency
            if there is no available capacity. 
            
             This setting is global across all subscribed libraries.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        """
        self.automatic_sync_enabled = automatic_sync_enabled
        self.automatic_sync_start_hour = automatic_sync_start_hour
        self.automatic_sync_stop_hour = automatic_sync_stop_hour
        self.maximum_concurrent_item_syncs = maximum_concurrent_item_syncs
        VapiStruct.__init__(self)

ConfigurationModel._set_binding_type(type.StructType(
    'com.vmware.content.configuration_model', {
        'automatic_sync_enabled': type.OptionalType(type.BooleanType()),
        'automatic_sync_start_hour': type.OptionalType(type.IntegerType()),
        'automatic_sync_stop_hour': type.OptionalType(type.IntegerType()),
        'maximum_concurrent_item_syncs': type.OptionalType(type.IntegerType()),
    },
    ConfigurationModel,
    False,
    None))



class LibraryModel(VapiStruct):
    """
    The :class:`LibraryModel` class represents a Content Library resource
    model. 
    
    A ``LibraryModel`` is a container for a set of items which represent a
    usable set of files. The Content Library Service allows for multiple
    libraries to be created with separate authorization and sharing policies. 
    
    Each ``LibraryModel`` is a container for a set of
    :class:`com.vmware.content.library_client.ItemModel` instances. Each item
    is a logical object in a library, which may have multiple files. 
    
    A ``LibraryModel`` may be local or subscribed. A local library has its
    source of truth about items within this Content Library Service. Items may
    be added to or removed from the library. A local library may also be
    private or published. When published, the library is exposed by a network
    endpoint and can be used by another Content Library Service for
    synchronization. A private local library cannot be used for
    synchronization. 
    
    A subscribed library is a library which gets its source of truth from
    another library that may be across a network in another Content Library
    Service. A subscribed library may have a different name and metadata from
    the library to which it subscribes, but the set of library items is always
    the same as those in the source library. Library items cannot be manually
    added to a subscribed library -- they can only be added by adding new items
    to the source library.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 creation_time=None,
                 description=None,
                 last_modified_time=None,
                 last_sync_time=None,
                 name=None,
                 storage_backings=None,
                 type=None,
                 optimization_info=None,
                 version=None,
                 publish_info=None,
                 subscription_info=None,
                 server_guid=None,
                ):
        """
        :type  id: :class:`str`
        :param id: An identifier which uniquely identifies this ``LibraryModel``.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.content.Library``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.content.Library``.
            This attribute is not used for the ``create`` method. It will not
            be present in the return value of the ``get`` or ``list`` methods.
            It is not used for the ``update`` method.
        :type  creation_time: :class:`datetime.datetime`
        :param creation_time: The date and time when this library was created.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  description: :class:`str`
        :param description: A human-readable description for this library.
            This attribute is optional for the ``create`` method. Leaving it
            None during creation will result in an empty string value. It will
            always be present in the result of a ``get`` or ``list`` method. It
            is optional for the ``update`` method. Leaving it None during
            update indicates that the description should be left unchanged.
        :type  last_modified_time: :class:`datetime.datetime`
        :param last_modified_time: The date and time when this library was last updated. 
            
            This attribute is updated automatically when the library properties
            are changed. This attribute is not affected by adding, removing, or
            modifying a library item or its content within the library. Tagging
            the library or syncing the subscribed library does not alter this
            attribute.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  last_sync_time: :class:`datetime.datetime`
        :param last_sync_time: The date and time when this library was last synchronized. 
            
            This attribute applies only to subscribed libraries. It is updated
            every time a synchronization is triggered on the library. The value
            is None for a local library.
            This attribute is not used for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is not used for the ``update`` method.
        :type  name: :class:`str`
        :param name: The name of the library. 
            
            A Library is identified by a human-readable name. Library names
            cannot be undefined or an empty string. Names do not have to be
            unique.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is optional for the ``update`` method.
        :type  storage_backings: :class:`list` of :class:`com.vmware.content.library_client.StorageBacking`
        :param storage_backings: The list of default storage backings which are available for this
            library. 
            
            A :class:`com.vmware.content.library_client.StorageBacking` defines
            a default storage location which can be used to store files for
            library items in this library. Some library items, for instance,
            virtual machine template items, support files that may be
            distributed across various storage backings. One or more item files
            may or may not be located on the default storage backing. 
            
            Multiple default storage locations are not currently supported but
            may become supported in future releases.
            This attribute must be provided for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  type: :class:`LibraryModel.LibraryType`
        :param type: The type (LOCAL, SUBSCRIBED) of this library. 
            
            This value can be used to determine what additional services and
            information can be available for this library. This attribute is
            not used for the ``create`` and ``update`` methods. It will always
            be present in the result of a ``get`` method.
            This attribute is not used for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        :type  optimization_info: :class:`com.vmware.content.library_client.OptimizationInfo`
        :param optimization_info: Defines various optimizations and optimization parameters applied
            to this library.
            This attribute is optional for the ``create`` method. It is
            optional in the return value of the ``get`` or ``list`` methods. It
            is optional for the ``update`` method.
        :type  version: :class:`str`
        :param version: A version number which is updated on metadata changes. This value
            allows clients to detect concurrent updates and prevent accidental
            clobbering of data. 
            
            This value represents a number which is incremented every time
            library properties, such as name or description, are changed. It is
            not incremented by changes to a library item within the library,
            including adding or removing items. It is also not affected by
            tagging the library.
            This attribute is not used for the ``create`` method. It will
            always be present in the result of a ``get`` or ``list`` method. It
            is optional for the ``update`` method. Leaving it None during
            update indicates that you do not need to detect concurrent updates.
        :type  publish_info: :class:`com.vmware.content.library_client.PublishInfo`
        :param publish_info: Defines how this library is published so that it can be subscribed
            to by a remote subscribed library. 
            
            The :class:`com.vmware.content.library_client.PublishInfo` defines
            where and how the metadata for this local library is accessible. A
            local library is only published publically if
            :attr:`com.vmware.content.library_client.PublishInfo.published` is
            ``true``.
            This attribute is optional for the ``create`` and ``update``
            methods. If not specified during creation, the default is for the
            library to not be published. If not specified during update, the
            attribute is left unchanged.
        :type  subscription_info: :class:`com.vmware.content.library_client.SubscriptionInfo`
        :param subscription_info: Defines the subscription behavior for this Library. 
            
            The :class:`com.vmware.content.library_client.SubscriptionInfo`
            defines how this subscribed library synchronizes to a remote
            source. Setting the value will determine the remote source to which
            the library synchronizes, and how. Changing the subscription will
            result in synchronizing to a new source. If the new source differs
            from the old one, the old library items and data will be lost.
            Setting
            :attr:`com.vmware.content.library_client.SubscriptionInfo.automatic_sync_enabled`
            to false will halt subscription but will not remove existing cached
            data.
            This attribute is optional for the ``create`` and ``update``
            methods. If not specified during creation, a default will be
            created without an active subscription. If not specified during
            update, the attribute is left unchanged.
        :type  server_guid: :class:`str`
        :param server_guid: The unique identifier of the vCenter server where the library
            exists.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vcenter.VCenter``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vcenter.VCenter``.
            This attribute is optional for the ``create`` method. It will
            always be present in the return value of the ``get`` or ``list``
            methods. It is not used for the ``update`` method.
        """
        self.id = id
        self.creation_time = creation_time
        self.description = description
        self.last_modified_time = last_modified_time
        self.last_sync_time = last_sync_time
        self.name = name
        self.storage_backings = storage_backings
        self.type = type
        self.optimization_info = optimization_info
        self.version = version
        self.publish_info = publish_info
        self.subscription_info = subscription_info
        self.server_guid = server_guid
        VapiStruct.__init__(self)

    class LibraryType(Enum):
        """
        The ``LibraryModel.LibraryType`` class defines the type of a
        :class:`LibraryModel`. 
        
        The type of a library can be used to determine which additional services
        can be performed with a library.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        LOCAL = None
        """
        The library contents are defined and stored by the local Content Library
        Service installation. 
        
        A local library can be retrieved and managed via the :class:`LocalLibrary`.

        """
        SUBSCRIBED = None
        """
        The library synchronizes its items and content from another published
        library. 
        
        A subscribed library can be retrieved and managed via the
        :class:`SubscribedLibrary`.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`LibraryType` instance.
            """
            Enum.__init__(string)

    LibraryType._set_values([
        LibraryType('LOCAL'),
        LibraryType('SUBSCRIBED'),
    ])
    LibraryType._set_binding_type(type.EnumType(
        'com.vmware.content.library_model.library_type',
        LibraryType))

LibraryModel._set_binding_type(type.StructType(
    'com.vmware.content.library_model', {
        'id': type.OptionalType(type.IdType()),
        'creation_time': type.OptionalType(type.DateTimeType()),
        'description': type.OptionalType(type.StringType()),
        'last_modified_time': type.OptionalType(type.DateTimeType()),
        'last_sync_time': type.OptionalType(type.DateTimeType()),
        'name': type.OptionalType(type.StringType()),
        'storage_backings': type.OptionalType(type.ListType(type.ReferenceType('com.vmware.content.library_client', 'StorageBacking'))),
        'type': type.OptionalType(type.ReferenceType(__name__, 'LibraryModel.LibraryType')),
        'optimization_info': type.OptionalType(type.ReferenceType('com.vmware.content.library_client', 'OptimizationInfo')),
        'version': type.OptionalType(type.StringType()),
        'publish_info': type.OptionalType(type.ReferenceType('com.vmware.content.library_client', 'PublishInfo')),
        'subscription_info': type.OptionalType(type.ReferenceType('com.vmware.content.library_client', 'SubscriptionInfo')),
        'server_guid': type.OptionalType(type.IdType()),
    },
    LibraryModel,
    True,
    ["id"]))



class Configuration(VapiInterface):
    """
    The ``Configuration`` class provides methods to configure the global
    settings of the Content Library Service. 
    
    The configuration settings are used by the Content Library Service to
    control the behavior of various operations.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ConfigurationStub)


    def update(self,
               model,
               ):
        """
        Updates the configuration. The update is incremental. Any attribute in
        the :class:`ConfigurationModel` class that is None will not be
        modified. Note that this update method doesn't guarantee an atomic
        change of all the properties. In the case of a system crash or failure,
        some of the properties could be left unchanged while others may be
        updated.

        :type  model: :class:`ConfigurationModel`
        :param model:  The :class:`ConfigurationModel` specifying the settings to update.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if one of the configuration properties is not within the proper
            range.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ContentLibrary.UpdateConfiguration``.
        """
        return self._invoke('update',
                            {
                            'model': model,
                            })

    def get(self):
        """
        Retrieves the current configuration values.


        :rtype: :class:`ConfigurationModel`
        :return: The :class:`ConfigurationModel` instance representing the
            configuration of the Content Library Service.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ContentLibrary.GetConfiguration``.
        """
        return self._invoke('get', None)
class Library(VapiInterface):
    """
    The ``Library`` class provides methods to manage and find
    :class:`LibraryModel` entities. 
    
    The ``Library`` class provides support for generic functionality which can
    be applied equally to all types of libraries. The functionality provided by
    this class will not affect the properties specific to the type of library.
    See also :class:`LocalLibrary` and :class:`SubscribedLibrary`.
    """
    RESOURCE_TYPE = "com.vmware.content.Library"
    """
    Resource type for library.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LibraryStub)

    class FindSpec(VapiStruct):
        """
        Specifies the properties that can be used as a filter to find libraries.
        When multiple attributes are specified, all properties of the library must
        match the specification.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     type=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: Name of the library to search. The name is case-insensitive. See
                :attr:`LibraryModel.name`.
                If not specified any name will be searched.
            :type  type: :class:`LibraryModel.LibraryType` or ``None``
            :param type: Library type to search. See :attr:`LibraryModel.type`.
                If not specified any library type will be searched.
            """
            self.name = name
            self.type = type
            VapiStruct.__init__(self)

    FindSpec._set_binding_type(type.StructType(
        'com.vmware.content.library.find_spec', {
            'name': type.OptionalType(type.StringType()),
            'type': type.OptionalType(type.ReferenceType(__name__, 'LibraryModel.LibraryType')),
        },
        FindSpec,
        False,
        None))



    def get(self,
            library_id,
            ):
        """
        Returns a given :class:`LibraryModel`.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the library to return.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :rtype: :class:`LibraryModel`
        :return: The :class:`LibraryModel` instance with the specified
            ``library_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the specified library does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'library_id': library_id,
                            })

    def list(self):
        """
        Returns the identifiers of all libraries of any type in the Content
        Library.


        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of all identifiers of all libraries in the
            Content Library.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def find(self,
             spec,
             ):
        """
        Returns a list of all the visible (as determined by authorization
        policy) libraries matching the requested :class:`Library.FindSpec`.

        :type  spec: :class:`Library.FindSpec`
        :param spec:  Specification describing what properties to filter on.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all the visible libraries
            matching the given ``spec``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if no properties are specified in the ``spec``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('find',
                            {
                            'spec': spec,
                            })

    def update(self,
               library_id,
               update_spec,
               ):
        """
        Updates the properties of a library. 
        
        This is an incremental update to the library. Any attribute in the
        :class:`LibraryModel` class that is None will not be modified. 
        
        This method will only update the common properties for all library
        types. This will not, for example, update the
        :attr:`LibraryModel.publish_info` of a local library, nor the
        :attr:`LibraryModel.subscription_info` of a subscribed library.
        Specific properties are updated in :func:`LocalLibrary.update` and
        :func:`SubscribedLibrary.update`.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the library to update.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :type  update_spec: :class:`LibraryModel`
        :param update_spec:  Specification of the new property values to set on the library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library associated with ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``update_spec`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the :attr:`LibraryModel.version` of ``update_spec`` is not equal
            to the current version of the library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``ContentLibrary.UpdateLibrary``.
        """
        return self._invoke('update',
                            {
                            'library_id': library_id,
                            'update_spec': update_spec,
                            })
class LocalLibrary(VapiInterface):
    """
    The ``LocalLibrary`` class manages local libraries. 
    
    The ``LocalLibrary`` class provides support for creating and maintaining
    local library instances. A local library may also use the :class:`Library`
    class to manage general library functionality.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LocalLibraryStub)


    def create(self,
               create_spec,
               client_token=None,
               ):
        """
        Creates a new local library.

        :type  client_token: :class:`str` or ``None``
        :param client_token: A unique token generated on the client for each creation request.
            The token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent creation.
            If not specified creation is not idempotent.
        :type  create_spec: :class:`LibraryModel`
        :param create_spec:  Specification for the new local library.
        :rtype: :class:`str`
        :return: Identifier of the newly created :class:`LibraryModel`.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``create_spec`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``client_token`` does not conform to the UUID format.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
             if using multiple storage backings.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ContentLibrary.CreateLocalLibrary``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'create_spec': create_spec,
                            })

    def delete(self,
               library_id,
               ):
        """
        Deletes the specified local library. 
        
        Deleting a local library will remove the entry immediately and begin an
        asynchronous task to remove all cached content for the library. If the
        asynchronous task fails, file content may remain on the storage
        backing. This content will require manual removal.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the local library to delete.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
             if the library specified by ``library_id`` is not a local library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires
              ``ContentLibrary.DeleteLocalLibrary``.
        """
        return self._invoke('delete',
                            {
                            'library_id': library_id,
                            })

    def get(self,
            library_id,
            ):
        """
        Returns a given local library.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the local library to return.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :rtype: :class:`LibraryModel`
        :return: The :class:`LibraryModel` instance associated with ``library_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
             if the library specified by ``library_id`` is not a local library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'library_id': library_id,
                            })

    def list(self):
        """
        Returns the identifiers of all local libraries in the Content Library.


        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all local libraries in the
            Content Library.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def update(self,
               library_id,
               update_spec,
               ):
        """
        Updates the properties of a local library. 
        
        This is an incremental update to the local library. Attributes that are
        None in the update specification will be left unchanged.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the local library to update.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :type  update_spec: :class:`LibraryModel`
        :param update_spec: Specification of the new property values to set on the local
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the library specified by ``library_id`` is a published library
            with JSON persistence enabled (see
            :attr:`com.vmware.content.library_client.PublishInfo.persist_json_enabled`)
            and the content of the library has been deleted from the storage
            backings (see :attr:`LibraryModel.storage_backings`) associated
            with it.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
             if the library specified by ``library_id`` is not a local library.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``update_spec`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the
            :attr:`com.vmware.content.library_client.PublishInfo.current_password`
            in the ``update_spec`` does not match the existing password of the
            published library.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the :attr:`LibraryModel.version` of ``update_spec`` is None and
            the library is being concurrently updated by another user.
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
            if the :attr:`LibraryModel.version` of ``update_spec`` is not equal
            to the current version of the library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires
              ``ContentLibrary.UpdateLocalLibrary``.
        """
        return self._invoke('update',
                            {
                            'library_id': library_id,
                            'update_spec': update_spec,
                            })
class SubscribedLibrary(VapiInterface):
    """
    
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SubscribedLibraryStub)

    class ProbeResult(VapiStruct):
        """
        The ``SubscribedLibrary.ProbeResult`` class defines the subscription
        information probe result. This describes whether using a given subscription
        URL is successful or if there are access problems, such as SSL errors.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     ssl_thumbprint=None,
                     error_messages=None,
                    ):
            """
            :type  status: :class:`SubscribedLibrary.ProbeResult.Status`
            :param status: The status of probe result. This will be one of SUCCESS,
                INVALID_URL, TIMED_OUT, HOST_NOT_FOUND, RESOURCE_NOT_FOUND,
                INVALID_CREDENTIALS, CERTIFICATE_ERROR, UNKNOWN_ERROR.
            :type  ssl_thumbprint: :class:`str` or ``None``
            :param ssl_thumbprint: The SSL thumbprint for the remote endpoint.
                An SSL thumbprint is only returned if the host is secured with
                SSL/TLS.
            :type  error_messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param error_messages: If the probe result is in an error status, this attribute will
                contain the detailed error messages.
            """
            self.status = status
            self.ssl_thumbprint = ssl_thumbprint
            self.error_messages = error_messages
            VapiStruct.__init__(self)

        class Status(Enum):
            """
            The ``SubscribedLibrary.ProbeResult.Status`` class defines the error status
            constants for the probe result.

            .. note::
                This class represents an enumerated type in the interface language
                definition. The class contains class attributes which represent the
                values in the current version of the enumerated type. Newer versions of
                the enumerated type may contain new values. To use new values of the
                enumerated type in communication with a server that supports the newer
                version of the API, you instantiate this class. See :ref:`enumerated
                type description page <enumeration_description>`.
            """
            SUCCESS = None
            """
            Indicates that the probe was successful.

            """
            INVALID_URL = None
            """
            Indicates that the supplied URL was not valid.

            """
            TIMED_OUT = None
            """
            Indicates that the probe timed out while attempting to connect to the URL.

            """
            HOST_NOT_FOUND = None
            """
            Indicates that the host in the URL could not be found.

            """
            RESOURCE_NOT_FOUND = None
            """
            Indicates that the given resource at the URL was not found.

            """
            INVALID_CREDENTIALS = None
            """
            Indicates that the connection was rejected due to invalid credentials.

            """
            CERTIFICATE_ERROR = None
            """
            Indicates that the provided server certificate thumbprint in
            :attr:`com.vmware.content.library_client.SubscriptionInfo.ssl_thumbprint`
            is invalid. In this case, the returned null should be set in
            :attr:`com.vmware.content.library_client.SubscriptionInfo.ssl_thumbprint`.

            """
            UNKNOWN_ERROR = None
            """
            Indicates an unspecified error different from the other error cases defined
            in :class:`SubscribedLibrary.ProbeResult.Status`.

            """

            def __init__(self, string):
                """
                :type  string: :class:`str`
                :param string: String value for the :class:`Status` instance.
                """
                Enum.__init__(string)

        Status._set_values([
            Status('SUCCESS'),
            Status('INVALID_URL'),
            Status('TIMED_OUT'),
            Status('HOST_NOT_FOUND'),
            Status('RESOURCE_NOT_FOUND'),
            Status('INVALID_CREDENTIALS'),
            Status('CERTIFICATE_ERROR'),
            Status('UNKNOWN_ERROR'),
        ])
        Status._set_binding_type(type.EnumType(
            'com.vmware.content.subscribed_library.probe_result.status',
            Status))

    ProbeResult._set_binding_type(type.StructType(
        'com.vmware.content.subscribed_library.probe_result', {
            'status': type.ReferenceType(__name__, 'SubscribedLibrary.ProbeResult.Status'),
            'ssl_thumbprint': type.OptionalType(type.StringType()),
            'error_messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        ProbeResult,
        False,
        None))



    def create(self,
               create_spec,
               client_token=None,
               ):
        """
        Creates a new subscribed library. 
        
        Once created, the subscribed library will be empty. If the
        :attr:`LibraryModel.subscription_info` property is set, the Content
        Library Service will attempt to synchronize to the remote source. This
        is an asynchronous operation so the content of the published library
        may not immediately appear.

        :type  client_token: :class:`str` or ``None``
        :param client_token: Unique token generated on the client for each creation request. The
            token should be a universally unique identifier (UUID), for
            example: ``b8a2a2e3-2314-43cd-a871-6ede0f429751``. This token can
            be used to guarantee idempotent creation.
            If not specified creation is not idempotent.
        :type  create_spec: :class:`LibraryModel`
        :param create_spec:  Specification for the new subscribed library.
        :rtype: :class:`str`
        :return: Identifier of the newly created subscribed library.
            The return value will be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``create_spec`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``client_token`` does not conform to the UUID format.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unsupported` 
             if using multiple storage backings.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
             if subscribing to a published library which cannot be accessed.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires
              ``ContentLibrary.CreateSubscribedLibrary``.
        """
        return self._invoke('create',
                            {
                            'client_token': client_token,
                            'create_spec': create_spec,
                            })

    def delete(self,
               library_id,
               ):
        """
        Deletes the specified subscribed library. 
        
        Deleting a subscribed library will remove the entry immediately and
        begin an asynchronous task to remove all cached content for the
        library. If the asynchronous task fails, file content may remain on the
        storage backing. This content will require manual removal.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the subscribed library to delete.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library referenced by ``library_id`` is not a subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library referenced by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires
              ``ContentLibrary.DeleteSubscribedLibrary``.
        """
        return self._invoke('delete',
                            {
                            'library_id': library_id,
                            })

    def evict(self,
              library_id,
              ):
        """
        Evicts the cached content of an on-demand subscribed library. 
        
        This method allows the cached content of a subscribed library to be
        removed to free up storage capacity. This method will only work when a
        subscribed library is synchronized on-demand.

        :type  library_id: :class:`str`
        :param library_id: Identifier of the subscribed library whose content should be
            evicted.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library specified by ``library_id`` is not a subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the library specified by ``library_id`` does not synchronize
            on-demand, or if the content of the library specified by
            ``library_id`` has been deleted from the storage backings (see
            :attr:`LibraryModel.storage_backings`) associated with it. 
            
            For instance, this {\\\\@term error) is reported on evicting an
            on-demand subscribed library that was restored from backup, and the
            library was deleted after the backup was taken, thus resulting in
            its content being deleted from the associated storage backings. In
            this scenario, the metadata of the library is present on a restore,
            while its content has been deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires
              ``ContentLibrary.EvictSubscribedLibrary``.
        """
        return self._invoke('evict',
                            {
                            'library_id': library_id,
                            })

    def get(self,
            library_id,
            ):
        """
        Returns a given subscribed library.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the subscribed library to return.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :rtype: :class:`LibraryModel`
        :return: The :class:`LibraryModel` instance that corresponds to
            ``library_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library associated with ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library associated with ``library_id`` is not a subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``System.Read``.
        """
        return self._invoke('get',
                            {
                            'library_id': library_id,
                            })

    def list(self):
        """
        Returns the identifiers of all subscribed libraries in the Content
        Library.


        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of identifiers of all subscribed libraries in the
            Content Library.
            The return value will contain identifiers for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
        """
        return self._invoke('list', None)

    def sync(self,
             library_id,
             ):
        """
        Forces the synchronization of the subscribed library. 
        
        Synchronizing a subscribed library forcefully with this method will
        perform the same synchronization behavior as would run periodically for
        the library. The
        :attr:`com.vmware.content.library_client.SubscriptionInfo.on_demand`
        setting is respected. Calling this method on a library that is already
        in the process of synchronizing will have no effect.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the subscribed library to synchronize.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library specified by ``library_id`` is not a subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the content of the library specified by ``library_id`` has been
            deleted from the storage backings (see
            :attr:`LibraryModel.storage_backings`) associated with it. 
            
            For instance, this {\\\\@term error) is reported on synchronizing a
            subscribed library that was restored from backup, and the library
            was deleted after the backup was taken, thus resulting in its
            content being deleted from the associated storage backings. In this
            scenario, the metadata of the library is present on a restore,
            while its content has been deleted.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if some parameter in the subscribed library subscription info is
            invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
             if the published library cannot be contacted or found.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires ``ContentLibrary.SyncLibrary``.
        """
        return self._invoke('sync',
                            {
                            'library_id': library_id,
                            })

    def update(self,
               library_id,
               update_spec,
               ):
        """
        Updates the properties of a subscribed library. 
        
        This is an incremental update to the subscribed library. Attributes
        that are None in the update specification will be left unchanged.

        :type  library_id: :class:`str`
        :param library_id:  Identifier of the subscribed library to update.
            The parameter must be an identifier for the resource type:
            ``com.vmware.content.Library``.
        :type  update_spec: :class:`LibraryModel`
        :param update_spec: Specification of the new property values to set on the subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the library specified by ``library_id`` does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotAllowedInCurrentState` 
            if the ``update_spec`` updates the subscription URL (see
            :attr:`com.vmware.content.library_client.SubscriptionInfo.subscription_url`)
            and the content of the library specified by ``library_id`` has been
            deleted from the storage backings (see
            :attr:`LibraryModel.storage_backings`) associated with it.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidElementType` 
            if the library specified by ``library_id`` is not a subscribed
            library.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if the ``update_spec`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceInaccessible` 
            if the subscription info is being updated but the published library
            cannot be contacted or found.
        :raise: :class:`com.vmware.vapi.std.errors_client.ResourceBusy` 
            if the :attr:`LibraryModel.version` of ``update_spec`` is None and
            the library is being concurrently updated by another user.
        :raise: :class:`com.vmware.vapi.std.errors_client.ConcurrentChange` 
            if the :attr:`LibraryModel.version` of ``update_spec`` is not equal
            to the current version of the library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * The resource ``com.vmware.content.Library`` referenced by the
              parameter ``library_id`` requires
              ``ContentLibrary.UpdateSubscribedLibrary``.
        """
        return self._invoke('update',
                            {
                            'library_id': library_id,
                            'update_spec': update_spec,
                            })

    def probe(self,
              subscription_info,
              ):
        """
        Probes remote library subscription information, including URL, SSL
        certificate and password. The resulting
        :class:`SubscribedLibrary.ProbeResult` class describes whether or not
        the subscription configuration is successful.

        :type  subscription_info: :class:`com.vmware.content.library_client.SubscriptionInfo`
        :param subscription_info:  The subscription info to be probed.
        :rtype: :class:`SubscribedLibrary.ProbeResult`
        :return: The subscription info probe result.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ContentLibrary.ProbeSubscription``.
        """
        return self._invoke('probe',
                            {
                            'subscription_info': subscription_info,
                            })
class Type(VapiInterface):
    """
    The ``Type`` class exposes the
    :class:`com.vmware.content.library_client.ItemModel` types that this
    Content Library Service supports. 
    
    A library item has an optional type which can be specified with the
    :attr:`com.vmware.content.library_client.ItemModel.type` attribute. For
    items with a type that is supported by a plugin, the Content Library
    Service may understand the files which are part of the library item and can
    produce metadata for the item. 
    
    In other cases, uploads may require a process in which one upload implies
    subsequent uploads. For example, an Open Virtualization Format (OVF)
    package is composed of an OVF descriptor file and the associated virtual
    disk files. Uploading an OVF descriptor can enable the Content Library
    Service to understand that the complete OVF package requires additional
    disk files, and it can set up the transfers for the disks automatically by
    adding the file entries for the disks when the OVF descriptor is uploaded. 
    
    When a type is not supported by a plugin, or the type is not specified, the
    Content Library Service can handle a library item in a default way, without
    adding metadata to the item or guiding the upload process.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TypeStub)

    class Info(VapiStruct):
        """
        The ``Type.Info`` class describes support for a specific type of data in an
        :class:`com.vmware.content.library_client.ItemModel`. The ``Type.Info`` can
        be queried through the :class:`Type` class. Type support describes plugins
        in the Content Library which can provide metadata on library items and help
        manage the transfer process by adding dependent files when a current file
        is added.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     description=None,
                     name=None,
                     type=None,
                     vendor=None,
                     version=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: A description of the type support offered by the plugin.
            :type  name: :class:`str`
            :param name: The name of the plugin which provides the type support.
            :type  type: :class:`str`
            :param type: The type which the plugin supports. 
                
                To upload a library item of the type supported by the plugin, the
                :attr:`com.vmware.content.library_client.ItemModel.type` attribute
                of the item should be set to this value.
            :type  vendor: :class:`str`
            :param vendor: The name of the vendor who created the type support plugin.
            :type  version: :class:`str`
            :param version: The version number of the type support plugin.
            """
            self.description = description
            self.name = name
            self.type = type
            self.vendor = vendor
            self.version = version
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.content.type.info', {
            'description': type.StringType(),
            'name': type.StringType(),
            'type': type.StringType(),
            'vendor': type.StringType(),
            'version': type.StringType(),
        },
        Info,
        False,
        None))



    def list(self):
        """
        Returns a :class:`list` of :class:`Type.Info` instances which describe
        the type support plugins in this Content Library.


        :rtype: :class:`list` of :class:`Type.Info`
        :return: The :class:`list` of :class:`Type.Info` instances which describe
            the type support plugins in this Content Library.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``ContentLibrary.TypeIntrospection``.
        """
        return self._invoke('list', None)
class _ConfigurationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'model': type.ReferenceType(__name__, 'ConfigurationModel'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {}
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        operations = {
            'update': {
                'input_type': update_input_type,
                'output_type': type.VoidType(),
                'errors': update_error_dict,
                'input_value_validator_list': update_input_value_validator_list,
                'output_validator_list': update_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ConfigurationModel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'update': update_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.configuration',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LibraryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
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
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for find operation
        find_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Library.FindSpec'),
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
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
            'update_spec': type.ReferenceType(__name__, 'LibraryModel'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'LibraryModel'),
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
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'find': find_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.library',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LocalLibraryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'create_spec': type.ReferenceType(__name__, 'LibraryModel'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
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
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
            'update_spec': type.ReferenceType(__name__, 'LibraryModel'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.Library'),
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
                'output_type': type.ReferenceType(__name__, 'LibraryModel'),
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
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'update': update_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.local_library',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SubscribedLibraryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'client_token': type.OptionalType(type.StringType()),
            'create_spec': type.ReferenceType(__name__, 'LibraryModel'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unsupported':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unsupported'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
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

        # properties for evict operation
        evict_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
        })
        evict_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),

        }
        evict_input_value_validator_list = [
        ]
        evict_output_validator_list = [
        ]
        evict_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for sync operation
        sync_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
        })
        sync_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),

        }
        sync_input_value_validator_list = [
        ]
        sync_output_validator_list = [
        ]
        sync_rest_metadata = None

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'library_id': type.IdType(resource_types='com.vmware.content.Library'),
            'update_spec': type.ReferenceType(__name__, 'LibraryModel'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.not_allowed_in_current_state':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotAllowedInCurrentState'),
            'com.vmware.vapi.std.errors.invalid_element_type':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidElementType'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.resource_inaccessible':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceInaccessible'),
            'com.vmware.vapi.std.errors.resource_busy':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ResourceBusy'),
            'com.vmware.vapi.std.errors.concurrent_change':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'ConcurrentChange'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        # properties for probe operation
        probe_input_type = type.StructType('operation-input', {
            'subscription_info': type.ReferenceType('com.vmware.content.library_client', 'SubscriptionInfo'),
        })
        probe_error_dict = {}
        probe_input_value_validator_list = [
        ]
        probe_output_validator_list = [
        ]
        probe_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.content.Library'),
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
            'evict': {
                'input_type': evict_input_type,
                'output_type': type.VoidType(),
                'errors': evict_error_dict,
                'input_value_validator_list': evict_input_value_validator_list,
                'output_validator_list': evict_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'LibraryModel'),
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
            'sync': {
                'input_type': sync_input_type,
                'output_type': type.VoidType(),
                'errors': sync_error_dict,
                'input_value_validator_list': sync_input_value_validator_list,
                'output_validator_list': sync_output_validator_list,
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
            'probe': {
                'input_type': probe_input_type,
                'output_type': type.ReferenceType(__name__, 'SubscribedLibrary.ProbeResult'),
                'errors': probe_error_dict,
                'input_value_validator_list': probe_input_value_validator_list,
                'output_validator_list': probe_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'evict': evict_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'sync': sync_rest_metadata,
            'update': update_rest_metadata,
            'probe': probe_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.content.subscribed_library',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TypeStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Type.Info')),
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
            self, iface_name='com.vmware.content.type',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Configuration': Configuration,
        'Library': Library,
        'LocalLibrary': LocalLibrary,
        'SubscribedLibrary': SubscribedLibrary,
        'Type': Type,
        'library': 'com.vmware.content.library_client.StubFactory',
    }

