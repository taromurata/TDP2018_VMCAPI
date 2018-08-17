# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.cis.tagging.
#---------------------------------------------------------------------------

"""
The ``com.vmware.cis.tagging_client`` component provides methods and classes to
attach metadata, by means of tags, to vSphere objects to make these objects
more sortable and searchable. You can use it to create, manage, and enumerate
tags and their categories (the group a tag belongs to). You can also query the
attached tags and attached objects.

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


class CategoryModel(VapiStruct):
    """
    The ``CategoryModel`` class defines a category that is used to group one or
    more tags.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 name=None,
                 description=None,
                 cardinality=None,
                 associable_types=None,
                 used_by=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The unique identifier of the category.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.cis.tagging.Category``.
        :type  name: :class:`str`
        :param name: The display name of the category.
        :type  description: :class:`str`
        :param description: The description of the category.
        :type  cardinality: :class:`CategoryModel.Cardinality`
        :param cardinality: The associated cardinality (SINGLE, MULTIPLE) of the category.
        :type  associable_types: :class:`set` of :class:`str`
        :param associable_types: The types of objects that the tags in this category can be attached
            to. If the :class:`set` is empty, then tags can be attached to all
            types of objects. This field works only for objects that reside in
            Inventory Service (IS). For non IS objects, this check is not
            performed today and hence a tag can be attached to any non IS
            object.
        :type  used_by: :class:`set` of :class:`str`
        :param used_by: The :class:`set` of users that can use this category. To add users
            to this, you need to have the edit privilege on the category.
            Similarly, to unsubscribe from this category, you need the edit
            privilege on the category. You should not modify other users
            subscription from this :class:`set`.
        """
        self.id = id
        self.name = name
        self.description = description
        self.cardinality = cardinality
        self.associable_types = associable_types
        self.used_by = used_by
        VapiStruct.__init__(self)

    class Cardinality(Enum):
        """
        The ``CategoryModel.Cardinality`` class defines the number of tags in a
        category that can be assigned to an object.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SINGLE = None
        """
        An object can only be assigned one of the tags in this category. For
        example, if a category is "Operating System", then different tags of this
        category would be "Windows", "Linux", and so on. In this case a VM object
        can be assigned only one of these tags and hence the cardinality of the
        associated category here is single.

        """
        MULTIPLE = None
        """
        An object can be assigned several of the tags in this category. For
        example, if a category is "Server", then different tags of this category
        would be "AppServer", "DatabaseServer" and so on. In this case a VM object
        can be assigned more than one of the above tags and hence the cardinality
        of the associated category here is multiple.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Cardinality` instance.
            """
            Enum.__init__(string)

    Cardinality._set_values([
        Cardinality('SINGLE'),
        Cardinality('MULTIPLE'),
    ])
    Cardinality._set_binding_type(type.EnumType(
        'com.vmware.cis.tagging.category_model.cardinality',
        Cardinality))

CategoryModel._set_binding_type(type.StructType(
    'com.vmware.cis.tagging.category_model', {
        'id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        'name': type.StringType(),
        'description': type.StringType(),
        'cardinality': type.ReferenceType(__name__, 'CategoryModel.Cardinality'),
        'associable_types': type.SetType(type.StringType()),
        'used_by': type.SetType(type.StringType()),
    },
    CategoryModel,
    True,
    ["id"]))



class TagModel(VapiStruct):
    """
    The ``TagModel`` class defines a tag that can be attached to vSphere
    objects.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 id=None,
                 category_id=None,
                 name=None,
                 description=None,
                 used_by=None,
                ):
        """
        :type  id: :class:`str`
        :param id: The unique identifier of the tag.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.cis.tagging.Tag``.
        :type  category_id: :class:`str`
        :param category_id: The identifier of the parent category in which this tag will be
            created.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``. When methods return a value of
            this class as a return value, the attribute will be an identifier
            for the resource type: ``com.vmware.cis.tagging.Category``.
        :type  name: :class:`str`
        :param name: The display name of the tag.
        :type  description: :class:`str`
        :param description: The description of the tag.
        :type  used_by: :class:`set` of :class:`str`
        :param used_by: The :class:`set` of users that can use this tag. To add users to
            this, you need to have the edit privilege on the tag. Similarly, to
            unsubscribe from this tag, you need the edit privilege on the tag.
            You should not modify other users subscription from this
            :class:`set`.
        """
        self.id = id
        self.category_id = category_id
        self.name = name
        self.description = description
        self.used_by = used_by
        VapiStruct.__init__(self)

TagModel._set_binding_type(type.StructType(
    'com.vmware.cis.tagging.tag_model', {
        'id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
        'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        'name': type.StringType(),
        'description': type.StringType(),
        'used_by': type.SetType(type.StringType()),
    },
    TagModel,
    True,
    ["id"]))



class Category(VapiInterface):
    """
    The ``Category`` class provides methods to create, read, update, delete,
    and enumerate categories.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CategoryStub)

    class CreateSpec(VapiStruct):
        """
        The ``Category.CreateSpec`` class is used to create a category. 
        
        Use the :func:`Category.create` method to create a category defined by the
        create specification.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     cardinality=None,
                     associable_types=None,
                     category_id=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The display name of the category.
            :type  description: :class:`str`
            :param description: The description of the category.
            :type  cardinality: :class:`CategoryModel.Cardinality`
            :param cardinality: The associated cardinality (SINGLE, MULTIPLE) of the category.
            :type  associable_types: :class:`set` of :class:`str`
            :param associable_types: Object types to which this category's tags can be attached.
            :type  category_id: :class:`str` or ``None``
            :param category_id: This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.tagging.Category``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.cis.tagging.Category``.
                If None an identifier will be generated by the server
            """
            self.name = name
            self.description = description
            self.cardinality = cardinality
            self.associable_types = associable_types
            self.category_id = category_id
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.category.create_spec', {
            'name': type.StringType(),
            'description': type.StringType(),
            'cardinality': type.ReferenceType(__name__, 'CategoryModel.Cardinality'),
            'associable_types': type.SetType(type.StringType()),
            'category_id': type.OptionalType(type.IdType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Category.UpdateSpec`` class describes the updates to be made to an
        existing category. 
        
        Use the :func:`Category.update` method to modify a category. When you call
        the method, specify the category identifier. You obtain the category
        identifier when you call the :func:`Category.create` method. You can also
        retrieve an identifier by using the :func:`Category.list` method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     cardinality=None,
                     associable_types=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: The display name of the category.
                If None the name will not be modified.
            :type  description: :class:`str` or ``None``
            :param description: The description of the category.
                If None the description will not be modified.
            :type  cardinality: :class:`CategoryModel.Cardinality` or ``None``
            :param cardinality: The associated cardinality (SINGLE, MULTIPLE) of the category.
                If None the cardinality will not be modified.
            :type  associable_types: :class:`set` of :class:`str` or ``None``
            :param associable_types: Object types to which this category's tags can be attached. 
                
                The :class:`set` of associable types cannot be updated
                incrementally. For example, if
                :attr:`Category.UpdateSpec.associable_types` originally contains
                {A,B,C} and you want to add D, then you need to pass {A,B,C,D} in
                your update specification. You also cannot remove any item from
                this :class:`set`. For example, if you have {A,B,C}, then you
                cannot remove say {A} from it. Similarly, if you start with an
                empty :class:`set`, then that implies that you can tag any object
                and hence you cannot later pass say {A}, because that would be
                restricting the type of objects you want to tag. Thus, associable
                types can only grow and not shrink.
                If None the associable types will not be modified.
            """
            self.name = name
            self.description = description
            self.cardinality = cardinality
            self.associable_types = associable_types
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.category.update_spec', {
            'name': type.OptionalType(type.StringType()),
            'description': type.OptionalType(type.StringType()),
            'cardinality': type.OptionalType(type.ReferenceType(__name__, 'CategoryModel.Cardinality')),
            'associable_types': type.OptionalType(type.SetType(type.StringType())),
        },
        UpdateSpec,
        False,
        None))



    def create(self,
               create_spec,
               ):
        """
        Creates a category. To invoke this method, you need the create category
        privilege.

        :type  create_spec: :class:`Category.CreateSpec`
        :param create_spec:  Specification for the new category to be created.
        :rtype: :class:`str`
        :return: The identifier of the created category.
            The return value will be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the :attr:`Category.CreateSpec.name` provided in the
            ``create_spec`` is the name of an already existing category.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if any of the information in the ``create_spec`` is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to create a category.
        """
        return self._invoke('create',
                            {
                            'create_spec': create_spec,
                            })

    def get(self,
            category_id,
            ):
        """
        Fetches the category information for the given category identifier. In
        order to view the category information, you need the read privilege on
        the category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the input category.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :rtype: :class:`CategoryModel`
        :return: The :class:`CategoryModel` that corresponds to ``category_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the category.
        """
        return self._invoke('get',
                            {
                            'category_id': category_id,
                            })

    def update(self,
               category_id,
               update_spec,
               ):
        """
        Updates an existing category. To invoke this method, you need the edit
        privilege on the category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the category to be updated.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :type  update_spec: :class:`Category.UpdateSpec`
        :param update_spec:  Specification to update the category.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the :attr:`Category.UpdateSpec.name` provided in the
            ``update_spec`` is the name of an already existing category.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if any of the information in the ``update_spec`` is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to update the category.
        """
        return self._invoke('update',
                            {
                            'category_id': category_id,
                            'update_spec': update_spec,
                            })

    def delete(self,
               category_id,
               ):
        """
        Deletes an existing category. To invoke this method, you need the
        delete privilege on the category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of category to be deleted.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to delete the category.
        """
        return self._invoke('delete',
                            {
                            'category_id': category_id,
                            })

    def list(self):
        """
        Enumerates the categories in the system. To invoke this method, you
        need the read privilege on the individual categories. The :class:`list`
        will only contain those categories for which you have read privileges.


        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of resource identifiers for the categories in the
            system.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Category``.
        """
        return self._invoke('list', None)

    def list_used_categories(self,
                             used_by_entity,
                             ):
        """
        Enumerates all categories for which the ``used_by_entity`` is part of
        the :attr:`CategoryModel.used_by` subscribers :class:`set`. To invoke
        this method, you need the read privilege on the individual categories.

        :type  used_by_entity: :class:`str`
        :param used_by_entity:  The field on which the results will be filtered.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of resource identifiers for the categories in the
            system that are used by ``used_by_entity``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Category``.
        """
        return self._invoke('list_used_categories',
                            {
                            'used_by_entity': used_by_entity,
                            })

    def add_to_used_by(self,
                       category_id,
                       used_by_entity,
                       ):
        """
        Adds the ``used_by_entity`` to the :attr:`CategoryModel.used_by`
        subscribers :class:`set` for the specified category. If the
        ``used_by_entity`` is already in the :class:`set`, then this becomes an
        idempotent no-op. To invoke this method, you need the modify
        :attr:`CategoryModel.used_by` privilege on the category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the input category.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :type  used_by_entity: :class:`str`
        :param used_by_entity: The name of the user to be added to the
            :attr:`CategoryModel.used_by` :class:`set`.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to add an entity to the
            :attr:`CategoryModel.used_by` field.
        """
        return self._invoke('add_to_used_by',
                            {
                            'category_id': category_id,
                            'used_by_entity': used_by_entity,
                            })

    def remove_from_used_by(self,
                            category_id,
                            used_by_entity,
                            ):
        """
        Removes the ``used_by_entity`` from the :attr:`CategoryModel.used_by`
        subscribers :class:`set`. If the ``used_by_entity`` is not using this
        category, then this becomes a no-op. To invoke this method, you need
        the modify :attr:`CategoryModel.used_by` privilege on the category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the input category.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :type  used_by_entity: :class:`str`
        :param used_by_entity: The name of the user to be removed from the
            :attr:`CategoryModel.used_by` :class:`set`.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to remove an entity from the
            :attr:`CategoryModel.used_by` field.
        """
        return self._invoke('remove_from_used_by',
                            {
                            'category_id': category_id,
                            'used_by_entity': used_by_entity,
                            })

    def revoke_propagating_permissions(self,
                                       category_id,
                                       ):
        """
        Revokes all propagating permissions on the given category. You should
        then attach a direct permission with tagging privileges on the given
        category. To invoke this method, you need category related privileges
        (direct or propagating) on the concerned category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the input category.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to revoke propagating permissions
            on the category.
        """
        return self._invoke('revoke_propagating_permissions',
                            {
                            'category_id': category_id,
                            })
class Tag(VapiInterface):
    """
    The ``Tag`` class provides methods to create, read, update, delete, and
    enumerate tags.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TagStub)

    class CreateSpec(VapiStruct):
        """
        The ``Tag.CreateSpec`` class describes a tag. 
        
        Use the :func:`Tag.create` method to create a tag defined by the create
        specification.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                     category_id=None,
                     tag_id=None,
                    ):
            """
            :type  name: :class:`str`
            :param name: The display name of the tag. The name must be unique within its
                category.
            :type  description: :class:`str`
            :param description: The description of the tag.
            :type  category_id: :class:`str`
            :param category_id: The unique identifier of the parent category in which this tag will
                be created.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.tagging.Category``. When methods return a value of
                this class as a return value, the attribute will be an identifier
                for the resource type: ``com.vmware.cis.tagging.Category``.
            :type  tag_id: :class:`str` or ``None``
            :param tag_id: This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.tagging.Tag``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.cis.tagging.Tag``.
                If None an identifier will be generated by the server
            """
            self.name = name
            self.description = description
            self.category_id = category_id
            self.tag_id = tag_id
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.tag.create_spec', {
            'name': type.StringType(),
            'description': type.StringType(),
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
            'tag_id': type.OptionalType(type.IdType()),
        },
        CreateSpec,
        False,
        None))


    class UpdateSpec(VapiStruct):
        """
        The ``Tag.UpdateSpec`` class describes the updates to be made to an
        existing tag. 
        
        Use the :func:`Tag.update` method to modify a tag. When you call the
        method, you specify the tag identifier. You obtain the tag identifier when
        you call the :func:`Tag.create` method. You can also retrieve an identifier
        by using the :func:`Tag.list` method.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     name=None,
                     description=None,
                    ):
            """
            :type  name: :class:`str` or ``None``
            :param name: The display name of the tag.
                If None the name will not be modified.
            :type  description: :class:`str` or ``None``
            :param description: The description of the tag.
                If None the description will not be modified.
            """
            self.name = name
            self.description = description
            VapiStruct.__init__(self)

    UpdateSpec._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.tag.update_spec', {
            'name': type.OptionalType(type.StringType()),
            'description': type.OptionalType(type.StringType()),
        },
        UpdateSpec,
        False,
        None))



    def create(self,
               create_spec,
               ):
        """
        Creates a tag. To invoke this method, you need the create tag privilege
        on the input category.

        :type  create_spec: :class:`Tag.CreateSpec`
        :param create_spec:  Specification for the new tag to be created.
        :rtype: :class:`str`
        :return: The identifier of the created tag.
            The return value will be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the :attr:`Tag.CreateSpec.name` provided in the ``create_spec``
            is the name of an already existing tag in the input category.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if any of the input information in the ``create_spec`` is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for in the given ``create_spec`` does not exist in
            the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to create tag.
        """
        return self._invoke('create',
                            {
                            'create_spec': create_spec,
                            })

    def get(self,
            tag_id,
            ):
        """
        Fetches the tag information for the given tag identifier. To invoke
        this method, you need the read privilege on the tag in order to view
        the tag info.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :rtype: :class:`TagModel`
        :return: The :class:`TagModel` that corresponds to ``tag_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if the user does not have the privilege to read the tag.
        """
        return self._invoke('get',
                            {
                            'tag_id': tag_id,
                            })

    def update(self,
               tag_id,
               update_spec,
               ):
        """
        Updates an existing tag. To invoke this method, you need the edit
        privilege on the tag.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  update_spec: :class:`Tag.UpdateSpec`
        :param update_spec:  Specification to update the tag.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the :attr:`Tag.UpdateSpec.name` provided in the ``update_spec``
            is the name of an already existing tag in the same category.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
             if any of the input information in the ``update_spec`` is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to update the tag.
        """
        return self._invoke('update',
                            {
                            'tag_id': tag_id,
                            'update_spec': update_spec,
                            })

    def delete(self,
               tag_id,
               ):
        """
        Deletes an existing tag. To invoke this method, you need the delete
        privilege on the tag.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to delete the tag.
        """
        return self._invoke('delete',
                            {
                            'tag_id': tag_id,
                            })

    def list(self):
        """
        Enumerates the tags in the system. To invoke this method, you need read
        privilege on the individual tags. The :class:`list` will only contain
        tags for which you have read privileges.


        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of resource identifiers for the tags in the
            system.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        """
        return self._invoke('list', None)

    def list_used_tags(self,
                       used_by_entity,
                       ):
        """
        Enumerates all tags for which the ``used_by_entity`` is part of the
        :attr:`TagModel.used_by` subscribers :class:`set`. To invoke this
        method, you need the read privilege on the individual tags.

        :type  used_by_entity: :class:`str`
        :param used_by_entity:  The field on which the results will be filtered.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of resource identifiers for the tags in the
            system that are used by ``used_by_entity``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        """
        return self._invoke('list_used_tags',
                            {
                            'used_by_entity': used_by_entity,
                            })

    def list_tags_for_category(self,
                               category_id,
                               ):
        """
        Enumerates all tags for the given category. To invoke this method, you
        need the read privilege on the given category and the individual tags
        in that category.

        :type  category_id: :class:`str`
        :param category_id:  The identifier of the input category.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Category``.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of resource identifiers for the tags in the given
            input category.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the category for the given ``category_id`` does not exist in the
            system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the category.
        """
        return self._invoke('list_tags_for_category',
                            {
                            'category_id': category_id,
                            })

    def add_to_used_by(self,
                       tag_id,
                       used_by_entity,
                       ):
        """
        Adds the ``used_by_entity`` to the :attr:`TagModel.used_by` subscribers
        :class:`set`. If the ``used_by_entity`` is already in the :class:`set`,
        then this becomes a no-op. To invoke this method, you need the modify
        :attr:`TagModel.used_by` privilege on the tag.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  used_by_entity: :class:`str`
        :param used_by_entity: The name of the user to be added to the :attr:`TagModel.used_by`
            :class:`set`.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to add an entity to the
            :attr:`TagModel.used_by` field.
        """
        return self._invoke('add_to_used_by',
                            {
                            'tag_id': tag_id,
                            'used_by_entity': used_by_entity,
                            })

    def remove_from_used_by(self,
                            tag_id,
                            used_by_entity,
                            ):
        """
        Removes the ``used_by_entity`` from the :attr:`TagModel.used_by`
        subscribers set. If the ``used_by_entity`` is not using this tag, then
        this becomes a no-op. To invoke this method, you need modify
        :attr:`TagModel.used_by` privilege on the tag.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  used_by_entity: :class:`str`
        :param used_by_entity: The name of the user to be removed from the
            :attr:`TagModel.used_by` :class:`set`.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to remove an entity from the
            :attr:`TagModel.used_by` field.
        """
        return self._invoke('remove_from_used_by',
                            {
                            'tag_id': tag_id,
                            'used_by_entity': used_by_entity,
                            })

    def revoke_propagating_permissions(self,
                                       tag_id,
                                       ):
        """
        Revokes all propagating permissions on the given tag. You should then
        attach a direct permission with tagging privileges on the given tag. To
        invoke this method, you need tag related privileges (direct or
        propagating) on the concerned tag.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to revoke propagating permissions
            on the tag.
        """
        return self._invoke('revoke_propagating_permissions',
                            {
                            'tag_id': tag_id,
                            })
class TagAssociation(VapiInterface):
    """
    The ``TagAssociation`` class provides methods to attach, detach, and query
    tags.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TagAssociationStub)

    class BatchResult(VapiStruct):
        """
        The ``TagAssociation.BatchResult`` class describes the result of performing
        the same method on several tags or objects in a single invocation. This
        class was added in vSphere API 6.5

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     success=None,
                     error_messages=None,
                    ):
            """
            :type  success: :class:`bool`
            :param success: This is true if the batch method completed without any errors.
                Otherwise it is false and all or some methods have failed. This
                attribute was added in vSphere API 6.5
            :type  error_messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param error_messages: The :class:`list` of error messages. This attribute was added in
                vSphere API 6.5
            """
            self.success = success
            self.error_messages = error_messages
            VapiStruct.__init__(self)

    BatchResult._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.tag_association.batch_result', {
            'success': type.BooleanType(),
            'error_messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        BatchResult,
        False,
        None))


    class TagToObjects(VapiStruct):
        """
        The ``TagAssociation.TagToObjects`` class describes a tag and its related
        objects. Use the :func:`TagAssociation.list_attached_objects_on_tags`
        method to retrieve a :class:`list` with each element containing a tag and
        the objects to which it is attached. This class was added in vSphere API
        6.5

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     tag_id=None,
                     object_ids=None,
                    ):
            """
            :type  tag_id: :class:`str`
            :param tag_id: The identifier of the tag. This attribute was added in vSphere API
                6.5
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.cis.tagging.Tag``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.cis.tagging.Tag``.
            :type  object_ids: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID`
            :param object_ids: The identifiers of the related objects. This attribute was added in
                vSphere API 6.5
            """
            self.tag_id = tag_id
            self.object_ids = object_ids
            VapiStruct.__init__(self)

    TagToObjects._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.tag_association.tag_to_objects', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'object_ids': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        },
        TagToObjects,
        False,
        None))


    class ObjectToTags(VapiStruct):
        """
        The ``TagAssociation.ObjectToTags`` class describes an object and its
        related tags. Use the :func:`TagAssociation.list_attached_tags_on_objects`
        method to retrieve a :class:`list` with each element containing an object
        and the tags attached to it. This class was added in vSphere API 6.5

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     object_id=None,
                     tag_ids=None,
                    ):
            """
            :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
            :param object_id: The identifier of the object. This attribute was added in vSphere
                API 6.5
            :type  tag_ids: :class:`list` of :class:`str`
            :param tag_ids: The identifiers of the related tags. This attribute was added in
                vSphere API 6.5
                When clients pass a value of this class as a parameter, the
                attribute must contain identifiers for the resource type:
                ``com.vmware.cis.tagging.Tag``. When methods return a value of this
                class as a return value, the attribute will contain identifiers for
                the resource type: ``com.vmware.cis.tagging.Tag``.
            """
            self.object_id = object_id
            self.tag_ids = tag_ids
            VapiStruct.__init__(self)

    ObjectToTags._set_binding_type(type.StructType(
        'com.vmware.cis.tagging.tag_association.object_to_tags', {
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
            'tag_ids': type.ListType(type.IdType()),
        },
        ObjectToTags,
        False,
        None))



    def attach(self,
               tag_id,
               object_id,
               ):
        """
        Attaches the given tag to the input object. The tag needs to meet the
        cardinality (:attr:`CategoryModel.cardinality`) and associability
        (:attr:`CategoryModel.associable_types`) criteria in order to be
        eligible for attachment. If the tag is already attached to the object,
        then this method is a no-op and an error will not be thrown. To invoke
        this method, you need the attach tag privilege on the tag and the read
        privilege on the object.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the input tag is not eligible to be attached to this object or
            if the ``object_id`` is not valid.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to attach the tag or do not have
            the privilege to read the object.
        """
        return self._invoke('attach',
                            {
                            'tag_id': tag_id,
                            'object_id': object_id,
                            })

    def attach_multiple_tags_to_object(self,
                                       object_id,
                                       tag_ids,
                                       ):
        """
        Attaches the given tags to the input object. If a tag is already
        attached to the object, then the individual method is a no-op and an
        error will not be added to
        :attr:`TagAssociation.BatchResult.error_messages`. To invoke this
        method, you need the read privilege on the object and the attach tag
        privilege on each tag. This method was added in vSphere API 6.5

        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :type  tag_ids: :class:`list` of :class:`str`
        :param tag_ids:  The identifiers of the input tags.
            The parameter must contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :rtype: :class:`TagAssociation.BatchResult`
        :return: The outcome of the batch method and the :class:`list` of error
            messages (:attr:`TagAssociation.BatchResult.error_messages`)
            describing attachment failures.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the object.
        """
        return self._invoke('attach_multiple_tags_to_object',
                            {
                            'object_id': object_id,
                            'tag_ids': tag_ids,
                            })

    def attach_tag_to_multiple_objects(self,
                                       tag_id,
                                       object_ids,
                                       ):
        """
        Attaches the given tag to the input objects. If a tag is already
        attached to the object, then the individual method is a no-op and an
        error will not be added to
        :attr:`TagAssociation.BatchResult.error_messages`. To invoke this
        method, you need the attach tag privilege on the tag and the read
        privilege on each object. This method was added in vSphere API 6.5

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  object_ids: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_ids:  The identifiers of the input objects.
        :rtype: :class:`TagAssociation.BatchResult`
        :return: The outcome of the batch method and the :class:`list` of error
            messages (:attr:`TagAssociation.BatchResult.error_messages`)
            describing attachment failures.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the attach tag privilege on the tag.
        """
        return self._invoke('attach_tag_to_multiple_objects',
                            {
                            'tag_id': tag_id,
                            'object_ids': object_ids,
                            })

    def detach(self,
               tag_id,
               object_id,
               ):
        """
        Detaches the tag from the given object. If the tag is already removed
        from the object, then this method is a no-op and an error will not be
        thrown. To invoke this method, you need the attach tag privilege on the
        tag and the read privilege on the object.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
            if you do not have the privilege to detach the tag or do not have
            the privilege to read the given object.
        """
        return self._invoke('detach',
                            {
                            'tag_id': tag_id,
                            'object_id': object_id,
                            })

    def detach_multiple_tags_from_object(self,
                                         object_id,
                                         tag_ids,
                                         ):
        """
        Detaches the given tags from the input object. If a tag is already
        removed from the object, then the individual method is a no-op and an
        error will not be added to
        :attr:`TagAssociation.BatchResult.error_messages`. To invoke this
        method, you need the read privilege on the object and the attach tag
        privilege each tag. This method was added in vSphere API 6.5

        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :type  tag_ids: :class:`list` of :class:`str`
        :param tag_ids:  The identifiers of the input tags.
            The parameter must contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :rtype: :class:`TagAssociation.BatchResult`
        :return: The outcome of the batch method and the :class:`list` of error
            messages (:attr:`TagAssociation.BatchResult.error_messages`)
            describing detachment failures.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the object.
        """
        return self._invoke('detach_multiple_tags_from_object',
                            {
                            'object_id': object_id,
                            'tag_ids': tag_ids,
                            })

    def detach_tag_from_multiple_objects(self,
                                         tag_id,
                                         object_ids,
                                         ):
        """
        Detaches the given tag from the input objects. If a tag is already
        removed from the object, then the individual method is a no-op and an
        error will not be added to
        :attr:`TagAssociation.BatchResult.error_messages`. To invoke this
        method, you need the attach tag privilege on the tag and the read
        privilege on each object. This method was added in vSphere API 6.5

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :type  object_ids: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_ids:  The identifiers of the input objects.
        :rtype: :class:`TagAssociation.BatchResult`
        :return: The outcome of the batch method and the :class:`list` of error
            messages (:attr:`TagAssociation.BatchResult.error_messages`)
            describing detachment failures.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given tag does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the attach tag privilege on the tag.
        """
        return self._invoke('detach_tag_from_multiple_objects',
                            {
                            'tag_id': tag_id,
                            'object_ids': object_ids,
                            })

    def list_attached_objects(self,
                              tag_id,
                              ):
        """
        Fetches the :class:`list` of attached objects for the given tag. To
        invoke this method, you need the read privilege on the input tag. Only
        those objects for which you have the read privilege will be returned.

        :type  tag_id: :class:`str`
        :param tag_id:  The identifier of the input tag.
            The parameter must be an identifier for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :rtype: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID`
        :return: The :class:`list` of attached object identifiers.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
             if the tag for the given ``tag_id`` does not exist in the system.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the tag.
        """
        return self._invoke('list_attached_objects',
                            {
                            'tag_id': tag_id,
                            })

    def list_attached_objects_on_tags(self,
                                      tag_ids,
                                      ):
        """
        Fetches the :class:`list` of :class:`TagAssociation.TagToObjects`
        describing the input tag identifiers and the objects they are attached
        to. To invoke this method, you need the read privilege on each input
        tag. The :attr:`TagAssociation.TagToObjects.object_ids` will only
        contain those objects for which you have the read privilege. This
        method was added in vSphere API 6.5

        :type  tag_ids: :class:`list` of :class:`str`
        :param tag_ids:  The identifiers of the input tags.
            The parameter must contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :rtype: :class:`list` of :class:`TagAssociation.TagToObjects`
        :return: The :class:`list` of the tag identifiers to all object identifiers
            that each tag is attached to.
        """
        return self._invoke('list_attached_objects_on_tags',
                            {
                            'tag_ids': tag_ids,
                            })

    def list_attached_tags(self,
                           object_id,
                           ):
        """
        Fetches the :class:`list` of tags attached to the given object. To
        invoke this method, you need the read privilege on the input object.
        The :class:`list` will only contain those tags for which you have the
        read privileges.

        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of all tag identifiers that correspond to the
            tags attached to the given object.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the object.
        """
        return self._invoke('list_attached_tags',
                            {
                            'object_id': object_id,
                            })

    def list_attached_tags_on_objects(self,
                                      object_ids,
                                      ):
        """
        Fetches the :class:`list` of :class:`TagAssociation.ObjectToTags`
        describing the input object identifiers and the tags attached to each
        object. To invoke this method, you need the read privilege on each
        input object. The :attr:`TagAssociation.ObjectToTags.tag_ids` will only
        contain those tags for which you have the read privilege. This method
        was added in vSphere API 6.5

        :type  object_ids: :class:`list` of :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_ids:  The identifiers of the input objects.
        :rtype: :class:`list` of :class:`TagAssociation.ObjectToTags`
        :return: The :class:`list` of the object identifiers to all tag identifiers
            that are attached to that object.
        """
        return self._invoke('list_attached_tags_on_objects',
                            {
                            'object_ids': object_ids,
                            })

    def list_attachable_tags(self,
                             object_id,
                             ):
        """
        Fetches the :class:`list` of attachable tags for the given object,
        omitting the tags that have already been attached. Criteria for
        attachability is calculated based on tagging cardinality
        (:attr:`CategoryModel.cardinality`) and associability
        (:attr:`CategoryModel.associable_types`) constructs. To invoke this
        method, you need the read privilege on the input object. The
        :class:`list` will only contain those tags for which you have read
        privileges.

        :type  object_id: :class:`com.vmware.vapi.std_client.DynamicID`
        :param object_id:  The identifier of the input object.
        :rtype: :class:`list` of :class:`str`
        :return: The :class:`list` of tag identifiers that are eligible to be
            attached to the given object.
            The return value will contain identifiers for the resource type:
            ``com.vmware.cis.tagging.Tag``.
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized` 
             if you do not have the privilege to read the object.
        """
        return self._invoke('list_attachable_tags',
                            {
                            'object_id': object_id,
                            })
class _CategoryStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'create_spec': type.ReferenceType(__name__, 'Category.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
            'update_spec': type.ReferenceType(__name__, 'Category.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for list_used_categories operation
        list_used_categories_input_type = type.StructType('operation-input', {
            'used_by_entity': type.StringType(),
        })
        list_used_categories_error_dict = {}
        list_used_categories_input_value_validator_list = [
        ]
        list_used_categories_output_validator_list = [
        ]
        list_used_categories_rest_metadata = None

        # properties for add_to_used_by operation
        add_to_used_by_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
            'used_by_entity': type.StringType(),
        })
        add_to_used_by_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        add_to_used_by_input_value_validator_list = [
        ]
        add_to_used_by_output_validator_list = [
        ]
        add_to_used_by_rest_metadata = None

        # properties for remove_from_used_by operation
        remove_from_used_by_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
            'used_by_entity': type.StringType(),
        })
        remove_from_used_by_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        remove_from_used_by_input_value_validator_list = [
        ]
        remove_from_used_by_output_validator_list = [
        ]
        remove_from_used_by_rest_metadata = None

        # properties for revoke_propagating_permissions operation
        revoke_propagating_permissions_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        })
        revoke_propagating_permissions_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        revoke_propagating_permissions_input_value_validator_list = [
        ]
        revoke_propagating_permissions_output_validator_list = [
        ]
        revoke_propagating_permissions_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'CategoryModel'),
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
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
            'list_used_categories': {
                'input_type': list_used_categories_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_used_categories_error_dict,
                'input_value_validator_list': list_used_categories_input_value_validator_list,
                'output_validator_list': list_used_categories_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'add_to_used_by': {
                'input_type': add_to_used_by_input_type,
                'output_type': type.VoidType(),
                'errors': add_to_used_by_error_dict,
                'input_value_validator_list': add_to_used_by_input_value_validator_list,
                'output_validator_list': add_to_used_by_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'remove_from_used_by': {
                'input_type': remove_from_used_by_input_type,
                'output_type': type.VoidType(),
                'errors': remove_from_used_by_error_dict,
                'input_value_validator_list': remove_from_used_by_input_value_validator_list,
                'output_validator_list': remove_from_used_by_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revoke_propagating_permissions': {
                'input_type': revoke_propagating_permissions_input_type,
                'output_type': type.VoidType(),
                'errors': revoke_propagating_permissions_error_dict,
                'input_value_validator_list': revoke_propagating_permissions_input_value_validator_list,
                'output_validator_list': revoke_propagating_permissions_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
            'list_used_categories': list_used_categories_rest_metadata,
            'add_to_used_by': add_to_used_by_rest_metadata,
            'remove_from_used_by': remove_from_used_by_rest_metadata,
            'revoke_propagating_permissions': revoke_propagating_permissions_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.tagging.category',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TagStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'create_spec': type.ReferenceType(__name__, 'Tag.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for update operation
        update_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'update_spec': type.ReferenceType(__name__, 'Tag.UpdateSpec'),
        })
        update_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        update_input_value_validator_list = [
        ]
        update_output_validator_list = [
        ]
        update_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for list_used_tags operation
        list_used_tags_input_type = type.StructType('operation-input', {
            'used_by_entity': type.StringType(),
        })
        list_used_tags_error_dict = {}
        list_used_tags_input_value_validator_list = [
        ]
        list_used_tags_output_validator_list = [
        ]
        list_used_tags_rest_metadata = None

        # properties for list_tags_for_category operation
        list_tags_for_category_input_type = type.StructType('operation-input', {
            'category_id': type.IdType(resource_types='com.vmware.cis.tagging.Category'),
        })
        list_tags_for_category_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_tags_for_category_input_value_validator_list = [
        ]
        list_tags_for_category_output_validator_list = [
        ]
        list_tags_for_category_rest_metadata = None

        # properties for add_to_used_by operation
        add_to_used_by_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'used_by_entity': type.StringType(),
        })
        add_to_used_by_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        add_to_used_by_input_value_validator_list = [
        ]
        add_to_used_by_output_validator_list = [
        ]
        add_to_used_by_rest_metadata = None

        # properties for remove_from_used_by operation
        remove_from_used_by_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'used_by_entity': type.StringType(),
        })
        remove_from_used_by_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        remove_from_used_by_input_value_validator_list = [
        ]
        remove_from_used_by_output_validator_list = [
        ]
        remove_from_used_by_rest_metadata = None

        # properties for revoke_propagating_permissions operation
        revoke_propagating_permissions_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
        })
        revoke_propagating_permissions_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        revoke_propagating_permissions_input_value_validator_list = [
        ]
        revoke_propagating_permissions_output_validator_list = [
        ]
        revoke_propagating_permissions_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'TagModel'),
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
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
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
            'list_used_tags': {
                'input_type': list_used_tags_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_used_tags_error_dict,
                'input_value_validator_list': list_used_tags_input_value_validator_list,
                'output_validator_list': list_used_tags_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_tags_for_category': {
                'input_type': list_tags_for_category_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_tags_for_category_error_dict,
                'input_value_validator_list': list_tags_for_category_input_value_validator_list,
                'output_validator_list': list_tags_for_category_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'add_to_used_by': {
                'input_type': add_to_used_by_input_type,
                'output_type': type.VoidType(),
                'errors': add_to_used_by_error_dict,
                'input_value_validator_list': add_to_used_by_input_value_validator_list,
                'output_validator_list': add_to_used_by_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'remove_from_used_by': {
                'input_type': remove_from_used_by_input_type,
                'output_type': type.VoidType(),
                'errors': remove_from_used_by_error_dict,
                'input_value_validator_list': remove_from_used_by_input_value_validator_list,
                'output_validator_list': remove_from_used_by_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'revoke_propagating_permissions': {
                'input_type': revoke_propagating_permissions_input_type,
                'output_type': type.VoidType(),
                'errors': revoke_propagating_permissions_error_dict,
                'input_value_validator_list': revoke_propagating_permissions_input_value_validator_list,
                'output_validator_list': revoke_propagating_permissions_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'get': get_rest_metadata,
            'update': update_rest_metadata,
            'delete': delete_rest_metadata,
            'list': list_rest_metadata,
            'list_used_tags': list_used_tags_rest_metadata,
            'list_tags_for_category': list_tags_for_category_rest_metadata,
            'add_to_used_by': add_to_used_by_rest_metadata,
            'remove_from_used_by': remove_from_used_by_rest_metadata,
            'revoke_propagating_permissions': revoke_propagating_permissions_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.tagging.tag',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TagAssociationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for attach operation
        attach_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
        })
        attach_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        attach_input_value_validator_list = [
        ]
        attach_output_validator_list = [
        ]
        attach_rest_metadata = None

        # properties for attach_multiple_tags_to_object operation
        attach_multiple_tags_to_object_input_type = type.StructType('operation-input', {
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
            'tag_ids': type.ListType(type.IdType()),
        })
        attach_multiple_tags_to_object_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        attach_multiple_tags_to_object_input_value_validator_list = [
        ]
        attach_multiple_tags_to_object_output_validator_list = [
        ]
        attach_multiple_tags_to_object_rest_metadata = None

        # properties for attach_tag_to_multiple_objects operation
        attach_tag_to_multiple_objects_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'object_ids': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        })
        attach_tag_to_multiple_objects_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        attach_tag_to_multiple_objects_input_value_validator_list = [
        ]
        attach_tag_to_multiple_objects_output_validator_list = [
        ]
        attach_tag_to_multiple_objects_rest_metadata = None

        # properties for detach operation
        detach_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
        })
        detach_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        detach_input_value_validator_list = [
        ]
        detach_output_validator_list = [
        ]
        detach_rest_metadata = None

        # properties for detach_multiple_tags_from_object operation
        detach_multiple_tags_from_object_input_type = type.StructType('operation-input', {
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
            'tag_ids': type.ListType(type.IdType()),
        })
        detach_multiple_tags_from_object_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        detach_multiple_tags_from_object_input_value_validator_list = [
        ]
        detach_multiple_tags_from_object_output_validator_list = [
        ]
        detach_multiple_tags_from_object_rest_metadata = None

        # properties for detach_tag_from_multiple_objects operation
        detach_tag_from_multiple_objects_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
            'object_ids': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        })
        detach_tag_from_multiple_objects_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        detach_tag_from_multiple_objects_input_value_validator_list = [
        ]
        detach_tag_from_multiple_objects_output_validator_list = [
        ]
        detach_tag_from_multiple_objects_rest_metadata = None

        # properties for list_attached_objects operation
        list_attached_objects_input_type = type.StructType('operation-input', {
            'tag_id': type.IdType(resource_types='com.vmware.cis.tagging.Tag'),
        })
        list_attached_objects_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_attached_objects_input_value_validator_list = [
        ]
        list_attached_objects_output_validator_list = [
        ]
        list_attached_objects_rest_metadata = None

        # properties for list_attached_objects_on_tags operation
        list_attached_objects_on_tags_input_type = type.StructType('operation-input', {
            'tag_ids': type.ListType(type.IdType()),
        })
        list_attached_objects_on_tags_error_dict = {}
        list_attached_objects_on_tags_input_value_validator_list = [
        ]
        list_attached_objects_on_tags_output_validator_list = [
        ]
        list_attached_objects_on_tags_rest_metadata = None

        # properties for list_attached_tags operation
        list_attached_tags_input_type = type.StructType('operation-input', {
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
        })
        list_attached_tags_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_attached_tags_input_value_validator_list = [
        ]
        list_attached_tags_output_validator_list = [
        ]
        list_attached_tags_rest_metadata = None

        # properties for list_attached_tags_on_objects operation
        list_attached_tags_on_objects_input_type = type.StructType('operation-input', {
            'object_ids': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
        })
        list_attached_tags_on_objects_error_dict = {}
        list_attached_tags_on_objects_input_value_validator_list = [
        ]
        list_attached_tags_on_objects_output_validator_list = [
        ]
        list_attached_tags_on_objects_rest_metadata = None

        # properties for list_attachable_tags operation
        list_attachable_tags_input_type = type.StructType('operation-input', {
            'object_id': type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID'),
        })
        list_attachable_tags_error_dict = {
            'com.vmware.vapi.std.errors.unauthorized':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthorized'),

        }
        list_attachable_tags_input_value_validator_list = [
        ]
        list_attachable_tags_output_validator_list = [
        ]
        list_attachable_tags_rest_metadata = None

        operations = {
            'attach': {
                'input_type': attach_input_type,
                'output_type': type.VoidType(),
                'errors': attach_error_dict,
                'input_value_validator_list': attach_input_value_validator_list,
                'output_validator_list': attach_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'attach_multiple_tags_to_object': {
                'input_type': attach_multiple_tags_to_object_input_type,
                'output_type': type.ReferenceType(__name__, 'TagAssociation.BatchResult'),
                'errors': attach_multiple_tags_to_object_error_dict,
                'input_value_validator_list': attach_multiple_tags_to_object_input_value_validator_list,
                'output_validator_list': attach_multiple_tags_to_object_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'attach_tag_to_multiple_objects': {
                'input_type': attach_tag_to_multiple_objects_input_type,
                'output_type': type.ReferenceType(__name__, 'TagAssociation.BatchResult'),
                'errors': attach_tag_to_multiple_objects_error_dict,
                'input_value_validator_list': attach_tag_to_multiple_objects_input_value_validator_list,
                'output_validator_list': attach_tag_to_multiple_objects_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'detach': {
                'input_type': detach_input_type,
                'output_type': type.VoidType(),
                'errors': detach_error_dict,
                'input_value_validator_list': detach_input_value_validator_list,
                'output_validator_list': detach_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'detach_multiple_tags_from_object': {
                'input_type': detach_multiple_tags_from_object_input_type,
                'output_type': type.ReferenceType(__name__, 'TagAssociation.BatchResult'),
                'errors': detach_multiple_tags_from_object_error_dict,
                'input_value_validator_list': detach_multiple_tags_from_object_input_value_validator_list,
                'output_validator_list': detach_multiple_tags_from_object_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'detach_tag_from_multiple_objects': {
                'input_type': detach_tag_from_multiple_objects_input_type,
                'output_type': type.ReferenceType(__name__, 'TagAssociation.BatchResult'),
                'errors': detach_tag_from_multiple_objects_error_dict,
                'input_value_validator_list': detach_tag_from_multiple_objects_input_value_validator_list,
                'output_validator_list': detach_tag_from_multiple_objects_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_attached_objects': {
                'input_type': list_attached_objects_input_type,
                'output_type': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'DynamicID')),
                'errors': list_attached_objects_error_dict,
                'input_value_validator_list': list_attached_objects_input_value_validator_list,
                'output_validator_list': list_attached_objects_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_attached_objects_on_tags': {
                'input_type': list_attached_objects_on_tags_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'TagAssociation.TagToObjects')),
                'errors': list_attached_objects_on_tags_error_dict,
                'input_value_validator_list': list_attached_objects_on_tags_input_value_validator_list,
                'output_validator_list': list_attached_objects_on_tags_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_attached_tags': {
                'input_type': list_attached_tags_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_attached_tags_error_dict,
                'input_value_validator_list': list_attached_tags_input_value_validator_list,
                'output_validator_list': list_attached_tags_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_attached_tags_on_objects': {
                'input_type': list_attached_tags_on_objects_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'TagAssociation.ObjectToTags')),
                'errors': list_attached_tags_on_objects_error_dict,
                'input_value_validator_list': list_attached_tags_on_objects_input_value_validator_list,
                'output_validator_list': list_attached_tags_on_objects_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list_attachable_tags': {
                'input_type': list_attachable_tags_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_attachable_tags_error_dict,
                'input_value_validator_list': list_attachable_tags_input_value_validator_list,
                'output_validator_list': list_attachable_tags_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'attach': attach_rest_metadata,
            'attach_multiple_tags_to_object': attach_multiple_tags_to_object_rest_metadata,
            'attach_tag_to_multiple_objects': attach_tag_to_multiple_objects_rest_metadata,
            'detach': detach_rest_metadata,
            'detach_multiple_tags_from_object': detach_multiple_tags_from_object_rest_metadata,
            'detach_tag_from_multiple_objects': detach_tag_from_multiple_objects_rest_metadata,
            'list_attached_objects': list_attached_objects_rest_metadata,
            'list_attached_objects_on_tags': list_attached_objects_on_tags_rest_metadata,
            'list_attached_tags': list_attached_tags_rest_metadata,
            'list_attached_tags_on_objects': list_attached_tags_on_objects_rest_metadata,
            'list_attachable_tags': list_attachable_tags_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.cis.tagging.tag_association',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Category': Category,
        'Tag': Tag,
        'TagAssociation': TagAssociation,
    }

