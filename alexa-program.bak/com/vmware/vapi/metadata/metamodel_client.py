# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.metamodel.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.metamodel_client`` module provides classes that
expose all the information present in the interface definition language (IDL)
specification. 

Metamodel metadata is organized into an hierarchy of elements. The main
elements are: 

* Enumeration: An enumeration element that has a list of enumeration value
  elements.
* Constant: A constant element has a name and a value.
* Structure: A structure element can have field elements, constant elements and
  enumeration elements.
* Operation: An operation has a list of parameter elements, result element and
  error elements.
* Service: A service is a collection of operation elements, structure elements,
  enumerated elements and constant elements.
* Package: A package is a collection of service elements, structure elements
  and enumeration elements.
* Component: A component is a collection of package elements.

The ``com.vmware.vapi.metadata.metamodel_client`` module has classes that
enables two styles of client applications: 

* A client can retrieve the exact pieces of information it requires using the
  various granularities the API supports (that is :class:`Component`,
  :class:`Package`, :class:`Service`, :class:`Structure`, :class:`Enumeration`
  and :class:`com.vmware.vapi.metadata.metamodel.service_client.Operation`). In
  this case, it doesn't cache any information locally and always invokes methods
  to get the metamodel information it requires.
* A client can retrieve all the metamodel information in fewer method
  invocations using the :class:`Component` class and cache the output locally. It
  can then poll on the fingerprint information exposed by the :class:`Component`
  class to monitor changes in API definition.

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


class ComponentData(VapiStruct):
    """
    The ``ComponentData`` class contains the metamodel metadata information of
    a component element along with its fingerprint.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 info=None,
                 fingerprint=None,
                ):
        """
        :type  info: :class:`ComponentInfo`
        :param info: Metamodel information of the component element. This includes
            information about all the package elements contained in this
            component element. 
            
            The metamodel information about a component could be quite large if
            there are a lot of package elements contained in this component.
        :type  fingerprint: :class:`str`
        :param fingerprint: Fingerprint of the metamodel metadata of the component component. 
            
            Metamodel information could change when there is an infrastructure
            update and new functionality is added to an existing component. 
            
            Since the data present in :attr:`ComponentData.info` could be quite
            large, ``fingerprint`` provides a convenient way to check if the
            data for a particular component is updated. 
            
            You should store the fingerprint associated with a component. After
            an update, by invoking the :func:`Component.fingerprint` method,
            you can retrieve the new fingerprint for the component. If the new
            fingerprint and the previously stored fingerprint do not match,
            clients can use the :func:`Component.get` to retrieve the new
            metamodel information for the component.
        """
        self.info = info
        self.fingerprint = fingerprint
        VapiStruct.__init__(self)

ComponentData._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.component_data', {
        'info': type.ReferenceType(__name__, 'ComponentInfo'),
        'fingerprint': type.StringType(),
    },
    ComponentData,
    False,
    None))



class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class contains metamodel metadata information about a
    component element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 packages=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Dot separated name of the component element. The segments in the
            name reflect the organization of the APIs. The format of each
            segment is lower case with underscores. Each underscore represents
            a word boundary. If there are acronyms in the word, the
            capitalization is preserved. This format makes it easy to translate
            the segment into a different naming convention.
        :type  packages: :class:`dict` of :class:`str` and :class:`PackageInfo`
        :param packages: Metamodel metadata information of all the package elements
            contained in the component element. The key in the :class:`dict` is
            the identifier of the package element and the value in the
            :class:`dict` is the metamodel information of the package element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.package``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata for the component element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for a component. It can contain HTML
            markup and documentation tags (similar to Javadoc tags). The first
            sentence of the package documentation is a complete sentence that
            identifies the component by name and summarizes the purpose of the
            component.
        """
        self.name = name
        self.packages = packages
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.component_info', {
        'name': type.StringType(),
        'packages': type.MapType(type.IdType(), type.ReferenceType(__name__, 'PackageInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    ComponentInfo,
    False,
    None))



class ConstantInfo(VapiStruct):
    """
    The ``ConstantInfo`` class contains metamodel information of the constant
    elements.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                 value=None,
                 documentation=None,
                ):
        """
        :type  type: :class:`Type`
        :param type: Type of the constant element.
        :type  value: :class:`ConstantValue`
        :param value: Value of the constant element.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for the constant element. It can
            contain HTML markup and documentation tags (similar to Javadoc
            tags).
        """
        self.type = type
        self.value = value
        self.documentation = documentation
        VapiStruct.__init__(self)

ConstantInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.constant_info', {
        'type': type.ReferenceType(__name__, 'Type'),
        'value': type.ReferenceType(__name__, 'ConstantValue'),
        'documentation': type.StringType(),
    },
    ConstantInfo,
    False,
    None))



class ConstantValue(VapiStruct):
    """
    The ``ConstantValue`` class contains the metamodel information of the
    constant element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'category',
            {
                'PRIMITIVE' : [('primitive_value', True)],
                'LIST' : [('list_value', True)],
            }
        ),
    ]



    def __init__(self,
                 category=None,
                 primitive_value=None,
                 list_value=None,
                ):
        """
        :type  category: :class:`ConstantValue.Category`
        :param category: Category of the type of constant value.
        :type  primitive_value: :class:`PrimitiveValue`
        :param primitive_value: Primitive value of the constant element.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`ConstantValue.Category.PRIMITIVE`.
        :type  list_value: :class:`list` of :class:`PrimitiveValue`
        :param list_value: List value of the constant element.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`ConstantValue.Category.LIST`.
        """
        self.category = category
        self.primitive_value = primitive_value
        self.list_value = list_value
        VapiStruct.__init__(self)

    class Category(Enum):
        """
        The ``ConstantValue.Category`` class defines class attributes for the valid
        kinds of values.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        PRIMITIVE = None
        """
        Indicates the type of constant value is primitive.

        """
        LIST = None
        """
        Indicates the type of constant value is a list.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Category` instance.
            """
            Enum.__init__(string)

    Category._set_values([
        Category('PRIMITIVE'),
        Category('LIST'),
    ])
    Category._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.constant_value.category',
        Category))

ConstantValue._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.constant_value', {
        'category': type.ReferenceType(__name__, 'ConstantValue.Category'),
        'primitive_value': type.OptionalType(type.ReferenceType(__name__, 'PrimitiveValue')),
        'list_value': type.OptionalType(type.ListType(type.ReferenceType(__name__, 'PrimitiveValue'))),
    },
    ConstantValue,
    False,
    None))



class ElementMap(VapiStruct):
    """
    The ``ElementMap`` class contains the metadata elements. 
    
    One of the sources for metadata is the annotations present in the interface
    definition language. When an annotation is represented in the
    ``ElementMap``, ``ElementMap`` describes the data specified in the
    arguments for the annotation. 
    
    For example, in ``\\\\@UnionCase(tag="tag", value="SELECT")``, ElementMap
    describes the keyword arguments tag and value.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 elements=None,
                ):
        """
        :type  elements: :class:`dict` of :class:`str` and :class:`ElementValue`
        :param elements: Metamodel information of the metadata elements. The key parameter
            of the :class:`dict` is the identifier for the element and the
            value corresponds to the element value.
        """
        self.elements = elements
        VapiStruct.__init__(self)

ElementMap._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.element_map', {
        'elements': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementValue')),
    },
    ElementMap,
    False,
    None))



class ElementValue(VapiStruct):
    """
    The ``ElementValue`` class describes the value of the metadata element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'type',
            {
                'LONG' : [('long_value', True)],
                'STRING' : [('string_value', True)],
                'STRING_LIST' : [('list_value', True)],
                'STRUCTURE_REFERENCE' : [('structure_id', True)],
                'STRUCTURE_REFERENCE_LIST' : [('structure_ids', True)],
            }
        ),
    ]



    def __init__(self,
                 type=None,
                 long_value=None,
                 string_value=None,
                 list_value=None,
                 structure_id=None,
                 structure_ids=None,
                ):
        """
        :type  type: :class:`ElementValue.Type`
        :param type: Type of the value.
        :type  long_value: :class:`long`
        :param long_value: Long value of the metadata element.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`ElementValue.Type.LONG`.
        :type  string_value: :class:`str`
        :param string_value: String value of the metadata element.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`ElementValue.Type.STRING`.
        :type  list_value: :class:`list` of :class:`str`
        :param list_value: List of strings value of the metadata element.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`ElementValue.Type.STRING_LIST`.
        :type  structure_id: :class:`str`
        :param structure_id: Identifier of the structure element.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.structure``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.structure``.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`ElementValue.Type.STRUCTURE_REFERENCE`.
        :type  structure_ids: :class:`list` of :class:`str`
        :param structure_ids: List of identifiers of the structure elements.
            When clients pass a value of this class as a parameter, the
            attribute must contain identifiers for the resource type:
            ``com.vmware.vapi.structure``. When methods return a value of this
            class as a return value, the attribute will contain identifiers for
            the resource type: ``com.vmware.vapi.structure``.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`ElementValue.Type.STRUCTURE_REFERENCE_LIST`.
        """
        self.type = type
        self.long_value = long_value
        self.string_value = string_value
        self.list_value = list_value
        self.structure_id = structure_id
        self.structure_ids = structure_ids
        VapiStruct.__init__(self)

    class Type(Enum):
        """
        The ``ElementValue.Type`` class defines the valid types for values in
        metadata elements.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        LONG = None
        """
        Indicates the type of the value is a long (64 bit signed integer).

        """
        STRING = None
        """
        Indicates the type of the value is a string (a variable length sequence of
        characters). The encoding is UTF-8.

        """
        STRING_LIST = None
        """
        Indicates the type of the value is a list of strings.

        """
        STRUCTURE_REFERENCE = None
        """
        Indicates the type of the value is an identifier for a structure element.

        """
        STRUCTURE_REFERENCE_LIST = None
        """
        Indicates the type of the value is a list of identifiers for a structure
        element.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('LONG'),
        Type('STRING'),
        Type('STRING_LIST'),
        Type('STRUCTURE_REFERENCE'),
        Type('STRUCTURE_REFERENCE_LIST'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.element_value.type',
        Type))

ElementValue._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.element_value', {
        'type': type.ReferenceType(__name__, 'ElementValue.Type'),
        'long_value': type.OptionalType(type.IntegerType()),
        'string_value': type.OptionalType(type.StringType()),
        'list_value': type.OptionalType(type.ListType(type.StringType())),
        'structure_id': type.OptionalType(type.IdType()),
        'structure_ids': type.OptionalType(type.ListType(type.IdType())),
    },
    ElementValue,
    False,
    None))



class EnumerationInfo(VapiStruct):
    """
    The ``EnumerationInfo`` class contains the metamodel information of an
    enumeration element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 values=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Dot separated name of the enumeration element. The segments in the
            name reflect the organization of the APIs. The format of each
            segment is lower case with underscores. Each underscore represents
            a word boundary. If there are acronyms in the word, the
            capitalization is preserved. This format makes it easy to translate
            the segment into a different naming convention.
        :type  values: :class:`list` of :class:`EnumerationValueInfo`
        :param values: Metamodel information of all the enumeration value elements
            contained in this enumeration element. The order of the enumeration
            value elements in the list is same as the order in which they are
            defined in the interface definition file.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for an enumeration element. The key in
            the :class:`dict` is the name of the metadata element and the value
            is the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for an enumeration element. It can
            contain HTML markup and Javadoc tags. The first sentence of the
            enumeration documentation is a complete sentence that identifies
            the enumeration by name and summarizes the purpose of the
            enumeration. The documentation describes the context in which the
            enumeration is used. 
            
            The documentation also contains references to the context in which
            the enumeration is used. But if the enumeration is used in many
            contexts, the references may not be present.
        """
        self.name = name
        self.values = values
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

EnumerationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.enumeration_info', {
        'name': type.StringType(),
        'values': type.ListType(type.ReferenceType(__name__, 'EnumerationValueInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    EnumerationInfo,
    False,
    None))



class EnumerationValueInfo(VapiStruct):
    """
    The ``EnumerationValueInfo`` class describes the class attribute in the
    class.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 value=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  value: :class:`str`
        :param value: Value in the enumerated type. All the characters in the string are
            capitalized.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Additional metadata for enumeration value in the enumerated type.
            The key in the :class:`dict` is the name of the metadata element
            and the value is the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for an enumeration value. It can
            contain HTML markup and documentation tags (similar to Javadoc
            tags). The first statement will be a noun or verb phrase that
            describes the purpose of the enumeration value.
        """
        self.value = value
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

EnumerationValueInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.enumeration_value_info', {
        'value': type.StringType(),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    EnumerationValueInfo,
    False,
    None))



class ErrorInfo(VapiStruct):
    """
    The ``ErrorInfo`` class contains the metadata information about the error
    elements contained in an operation element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 structure_id=None,
                 documentation=None,
                ):
        """
        :type  structure_id: :class:`str`
        :param structure_id: Identifier for the structure element corresponding to the error
            that is being reported by the operation.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for the resource type:
            ``com.vmware.vapi.structure``. When methods return a value of this
            class as a return value, the attribute will be an identifier for
            the resource type: ``com.vmware.vapi.structure``.
        :type  documentation: :class:`str`
        :param documentation: The English language documentation for the service element. It can
            contain HTML markup and Javadoc tags.
        """
        self.structure_id = structure_id
        self.documentation = documentation
        VapiStruct.__init__(self)

ErrorInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.error_info', {
        'structure_id': type.IdType(resource_types='com.vmware.vapi.structure'),
        'documentation': type.StringType(),
    },
    ErrorInfo,
    False,
    None))



class FieldInfo(VapiStruct):
    """
    The ``FieldInfo`` class contains metamodel information of a field element
    contained in a structure element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 type=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the field element in a canonical format. The format is
            lower case with underscores. Each underscore represents a word
            boundary. If there are acronyms in the word, the capitalization is
            preserved. This format makes it easy to translate the segment into
            a different naming convention.
        :type  type: :class:`Type`
        :param type: Type information.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the field element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for the service element. It can
            contain HTML markup and Javadoc tags.
        """
        self.name = name
        self.type = type
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

FieldInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.field_info', {
        'name': type.StringType(),
        'type': type.ReferenceType(__name__, 'Type'),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    FieldInfo,
    False,
    None))



class GenericInstantiation(VapiStruct):
    """
    The ``GenericInstantiation`` class describes the type information of a
    typed element when the type is an instantiation of one of the generic types
    provided by the infrastructure.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'generic_type',
            {
                'LIST' : [('element_type', True)],
                'OPTIONAL' : [('element_type', True)],
                'SET' : [('element_type', True)],
                'MAP' : [('map_key_type', True), ('map_value_type', True)],
            }
        ),
    ]



    def __init__(self,
                 generic_type=None,
                 element_type=None,
                 map_key_type=None,
                 map_value_type=None,
                ):
        """
        :type  generic_type: :class:`GenericInstantiation.GenericType`
        :param generic_type: The generic type that is being instantiated.
        :type  element_type: :class:`Type`
        :param element_type: Type of the element parameter if the generic type instantiation is
            a :attr:`GenericInstantiation.GenericType.LIST`,
            :attr:`GenericInstantiation.GenericType.OPTIONAL` or
            :attr:`GenericInstantiation.GenericType.SET`.
            This attribute is optional and it is only relevant when the value
            of ``genericType`` is one of
            :attr:`GenericInstantiation.GenericType.LIST`,
            :attr:`GenericInstantiation.GenericType.OPTIONAL`, or
            :attr:`GenericInstantiation.GenericType.SET`.
        :type  map_key_type: :class:`Type`
        :param map_key_type: Type of the key parameter of the map generic type instantiation.
            The map generic type has a key parameter and value parameter. The
            type of the value parameter is described by
            :attr:`GenericInstantiation.map_value_type`..
            This attribute is optional and it is only relevant when the value
            of ``genericType`` is :attr:`GenericInstantiation.GenericType.MAP`.
        :type  map_value_type: :class:`Type`
        :param map_value_type: Type of the value parameter of the map generic type instantiation.
            The map generic type has a key parameter and value parameter. The
            type of the key parameter is described by
            :attr:`GenericInstantiation.map_key_type`..
            This attribute is optional and it is only relevant when the value
            of ``genericType`` is :attr:`GenericInstantiation.GenericType.MAP`.
        """
        self.generic_type = generic_type
        self.element_type = element_type
        self.map_key_type = map_key_type
        self.map_value_type = map_value_type
        VapiStruct.__init__(self)

    class GenericType(Enum):
        """
        The ``GenericInstantiation.GenericType`` class provides class attributes
        for each of the generic types provided by the infrastructure.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        LIST = None
        """
        Indicates the generic type is a list.

        """
        MAP = None
        """
        Indicates the generic type is a map.

        """
        OPTIONAL = None
        """
        Indicates the generic type is an optional.

        """
        SET = None
        """
        Indicates the generic type is a set.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`GenericType` instance.
            """
            Enum.__init__(string)

    GenericType._set_values([
        GenericType('LIST'),
        GenericType('MAP'),
        GenericType('OPTIONAL'),
        GenericType('SET'),
    ])
    GenericType._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.generic_instantiation.generic_type',
        GenericType))

GenericInstantiation._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.generic_instantiation', {
        'generic_type': type.ReferenceType(__name__, 'GenericInstantiation.GenericType'),
        'element_type': type.OptionalType(type.ReferenceType(__name__, 'Type')),
        'map_key_type': type.OptionalType(type.ReferenceType(__name__, 'Type')),
        'map_value_type': type.OptionalType(type.ReferenceType(__name__, 'Type')),
    },
    GenericInstantiation,
    False,
    None))



class OperationInfo(VapiStruct):
    """
    The ``OperationInfo`` class contains metamodel information of an operation
    element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 params=None,
                 output=None,
                 errors=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Name of the operation element in a canonical format. The format is
            lower case with underscores. Each underscore represents a word
            boundary. If there are acronyms in the word, the capitalization is
            preserved. This format makes it easy to translate the segment into
            a different naming convention.
        :type  params: :class:`list` of :class:`FieldInfo`
        :param params: Metamodel information for the parameter elements. The order of the
            parameters elements in the list is same as the order of the
            parameters declared in the interface definition file.
        :type  output: :class:`OperationResultInfo`
        :param output: Metamodel type for the output element.
        :type  errors: :class:`list` of :class:`ErrorInfo`
        :param errors: List of error elements that might be reported by the operation
            element. If the operation reports the same error for more than one
            reason, the list contains the error element associated with the
            error more than once with different documentation elements.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the operation element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            key in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for the service element. It can
            contain HTML markup and Javadoc tags.
        """
        self.name = name
        self.params = params
        self.output = output
        self.errors = errors
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

OperationInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.operation_info', {
        'name': type.StringType(),
        'params': type.ListType(type.ReferenceType(__name__, 'FieldInfo')),
        'output': type.ReferenceType(__name__, 'OperationResultInfo'),
        'errors': type.ListType(type.ReferenceType(__name__, 'ErrorInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    OperationInfo,
    False,
    None))



class OperationResultInfo(VapiStruct):
    """
    The ``OperationResultInfo`` class contains the metamodel information of an
    operation result element. 
    
    An operation accepts a list of parameters and returns a result or an error.
    The ``OperationResultInfo`` describes the result element of an operation.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  type: :class:`Type`
        :param type: Type information of the operation result element.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the service element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for the operation result element. It
            can contain HTML markup and Javadoc tags.
        """
        self.type = type
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

OperationResultInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.operation_result_info', {
        'type': type.ReferenceType(__name__, 'Type'),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    OperationResultInfo,
    False,
    None))



class PackageInfo(VapiStruct):
    """
    The ``PackageInfo`` class contains the metamodel information of all the
    service elements, structure elements and enumeration elements contained in
    the package element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 structures=None,
                 enumerations=None,
                 services=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Dot separated name of the package element. The segments in the name
            reflect the organization of the APIs. The format of each segment is
            lower case with underscores. Each underscore represents a word
            boundary. If there are acronyms in the word, the capitalization is
            preserved. This format makes it easy to translate the segment into
            a different naming convention.
        :type  structures: :class:`dict` of :class:`str` and :class:`StructureInfo`
        :param structures: Metamodel information of all the structure elements contained in
            the package element. The key in the :class:`dict` is the identifier
            of the structure element and the value in the :class:`dict` is the
            metamodel information for the structure element. 
            
            This does not include the structure elements contained in the
            service elements that are contained in this package element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.structure``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.structure``.
        :type  enumerations: :class:`dict` of :class:`str` and :class:`EnumerationInfo`
        :param enumerations: Metamodel information of all the enumeration elements contained in
            the package element. The key in the :class:`dict` is the identifier
            of the enumeration element and the value in the :class:`dict` is
            the metamodel information for the enumeration element. 
            
            This does not include the enumeration elements that are contained
            in the service elements of this package element or structure
            elements of this package element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.enumeration``. When methods return a value
            of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.enumeration``.
        :type  services: :class:`dict` of :class:`str` and :class:`ServiceInfo`
        :param services: Metamodel information of all the service elements contained in the
            package element. The key in the :class:`dict` is the identifier of
            the service element and the value in the :class:`dict` is the
            metamodel information for the service element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.service``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the package element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for a package. It can contain HTML
            markup and Javadoc tags. The first sentence of the package
            documentation is a complete sentence that identifies the package by
            name and summarizes the purpose of the package. 
            
            The primary purpose of a package documentation is to provide
            high-level context that will provide a framework in which the users
            can put the detail about the package contents.
        """
        self.name = name
        self.structures = structures
        self.enumerations = enumerations
        self.services = services
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

PackageInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.package_info', {
        'name': type.StringType(),
        'structures': type.MapType(type.IdType(), type.ReferenceType(__name__, 'StructureInfo')),
        'enumerations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'EnumerationInfo')),
        'services': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ServiceInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    PackageInfo,
    False,
    None))



class PrimitiveValue(VapiStruct):
    """
    The ``PrimitiveValue`` class contains value of the constant element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'type',
            {
                'BOOLEAN' : [('boolean_value', True)],
                'DOUBLE' : [('double_value', True)],
                'LONG' : [('long_value', True)],
                'STRING' : [('string_value', True)],
            }
        ),
    ]



    def __init__(self,
                 type=None,
                 boolean_value=None,
                 double_value=None,
                 long_value=None,
                 string_value=None,
                ):
        """
        :type  type: :class:`PrimitiveValue.Type`
        :param type: Type of the constant value.
        :type  boolean_value: :class:`bool`
        :param boolean_value: Boolean value of the constant.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`PrimitiveValue.Type.BOOLEAN`.
        :type  double_value: :class:`float`
        :param double_value: Double value of the constant.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`PrimitiveValue.Type.DOUBLE`.
        :type  long_value: :class:`long`
        :param long_value: Long value of the constant.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`PrimitiveValue.Type.LONG`.
        :type  string_value: :class:`str`
        :param string_value: String value of the constant.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`PrimitiveValue.Type.STRING`.
        """
        self.type = type
        self.boolean_value = boolean_value
        self.double_value = double_value
        self.long_value = long_value
        self.string_value = string_value
        VapiStruct.__init__(self)

    class Type(Enum):
        """
        The ``PrimitiveValue.Type`` class defines the valid types for values in
        constant elements.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BOOLEAN = None
        """
        Indicates the value is a boolean (true or false).

        """
        DOUBLE = None
        """
        Indicates the value is a double (64 bit floating number).

        """
        LONG = None
        """
        Indicates the value is a long (64 bit signed integer).

        """
        STRING = None
        """
        Indicates the value is a string (a variable length sequence of characters).
        The encoding is UTF8.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('BOOLEAN'),
        Type('DOUBLE'),
        Type('LONG'),
        Type('STRING'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.primitive_value.type',
        Type))

PrimitiveValue._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.primitive_value', {
        'type': type.ReferenceType(__name__, 'PrimitiveValue.Type'),
        'boolean_value': type.OptionalType(type.BooleanType()),
        'double_value': type.OptionalType(type.DoubleType()),
        'long_value': type.OptionalType(type.IntegerType()),
        'string_value': type.OptionalType(type.StringType()),
    },
    PrimitiveValue,
    False,
    None))



class ServiceInfo(VapiStruct):
    """
    The ``ServiceInfo`` class contains the metamodel information of all the
    operation elements, structure elements and enumeration elements containted
    in a service element.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 operations=None,
                 structures=None,
                 enumerations=None,
                 constants=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Dot separated name of the service element. The segments in the name
            reflect the organization of the APIs. The format of each segment is
            lower case with underscores. Each underscore represents a word
            boundary. If there are acronyms in the word, the capitalization is
            preserved. This format makes it easy to translate the segment into
            a different naming convention.
        :type  operations: :class:`dict` of :class:`str` and :class:`OperationInfo`
        :param operations: Metamodel information of all the operation elements contained in
            the service element. The key in the :class:`dict` is the identifier
            of the operation element and the value in the :class:`dict` is the
            metamodel information for the operation element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.operation``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.operation``.
        :type  structures: :class:`dict` of :class:`str` and :class:`StructureInfo`
        :param structures: Metamodel information of all the structure elements contained in
            the service element. The key in the :class:`dict` is the identifier
            of the structure element and the value in the :class:`dict` is the
            metamodel information for the structure element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.structure``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.structure``.
        :type  enumerations: :class:`dict` of :class:`str` and :class:`EnumerationInfo`
        :param enumerations: Metamodel information of all the enumeration elements contained in
            the service element. The key in the :class:`dict` is the identifier
            of the enumeration element and the value in the :class:`dict` is
            the metamodel information for the enumeration element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.enumeration``. When methods return a value
            of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.enumeration``.
        :type  constants: :class:`dict` of :class:`str` and :class:`ConstantInfo`
        :param constants: Metamodel information of all the constant elements contained in the
            service element. The key in the :class:`dict` is the name of the
            constant element and the value in the :class:`dict` is the
            metamodel information for the contant element.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the service element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for the service element. It can
            contain HTML markup and Javadoc tags. The first sentence of the
            service documentation is a complete sentence that identifies the
            service by name and summarizes the purpose of the service. The
            remaining part of the documentation provides a summary of how to
            use the operations defined in the service.
        """
        self.name = name
        self.operations = operations
        self.structures = structures
        self.enumerations = enumerations
        self.constants = constants
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

ServiceInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.service_info', {
        'name': type.StringType(),
        'operations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'OperationInfo')),
        'structures': type.MapType(type.IdType(), type.ReferenceType(__name__, 'StructureInfo')),
        'enumerations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'EnumerationInfo')),
        'constants': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ConstantInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    ServiceInfo,
    False,
    None))



class StructureInfo(VapiStruct):
    """
    The ``StructureInfo`` class contains the metamodel information of all the
    field elements, constant elements and enumeration elements contained in the
    structure element. 
    
    In the interface definition language, API designers have the ability to
    include all the fields from one structure to another structure. This is
    done by using an annotation ``\\\\@Include`` on the structure in which we
    want to add the fields. If this annotation is present, the list of fields
    in the ``StructureInfo`` will also contain the fields that are being
    included. The annotation information is also retained in the
    :attr:`StructureInfo.metadata` element as well.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 type=None,
                 enumerations=None,
                 constants=None,
                 fields=None,
                 metadata=None,
                 documentation=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Dot separated name of the structure element. The segments in the
            name reflect the organization of the APIs. The format of each
            segment is lower case with underscores. Each underscore represents
            a word boundary. If there are acronyms in the word, the
            capitalization is preserved. This format makes it easy to translate
            the segment into a different naming convention.
        :type  type: :class:`StructureInfo.Type`
        :param type: Type of the structure.
        :type  enumerations: :class:`dict` of :class:`str` and :class:`EnumerationInfo`
        :param enumerations: Metamodel information of all the enumeration elements contained in
            the structure element. The key in the :class:`dict` is the
            identifier of the enumeration element and the value is the
            metamodel information of the enumeration element.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.enumeration``. When methods return a value
            of this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.enumeration``.
        :type  constants: :class:`dict` of :class:`str` and :class:`ConstantInfo`
        :param constants: Metamodel information of all the constant elements contained in the
            structure element. The key in the :class:`dict` is the name of the
            constant element and the value in the :class:`dict` is the
            metamodel information for the constant element.
        :type  fields: :class:`list` of :class:`FieldInfo`
        :param fields: Metamodel information of all the field elements. The order of the
            field elements in the list matches the order in which the fields
            are defined in the service.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ElementMap`
        :param metadata: Generic metadata elements for the structure element. The key in the
            :class:`dict` is the name of the metadata element and the value is
            the data associated with that metadata element. 
            
            The :class:`MetadataIdentifier` contains possible string values for
            keys in the :class:`dict`.
        :type  documentation: :class:`str`
        :param documentation: English language documentation for a structure element. It can
            contain HTML markup and Javadoc tags. The first sentence of the
            structure documentation is a complete sentence that identifies the
            structure by name and summarizes the purpose of the structure.
        """
        self.name = name
        self.type = type
        self.enumerations = enumerations
        self.constants = constants
        self.fields = fields
        self.metadata = metadata
        self.documentation = documentation
        VapiStruct.__init__(self)

    class Type(Enum):
        """
        The ``StructureInfo.Type`` class defines the kind of this structure
        element. In the interface definition language, structure element and error
        element have similar characteristics. The difference is that only error
        elements can be used to describe the exceptions of an operation element.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        STRUCTURE = None
        """
        If the type is a structure element.

        """
        ERROR = None
        """
        If the type is an error element.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Type` instance.
            """
            Enum.__init__(string)

    Type._set_values([
        Type('STRUCTURE'),
        Type('ERROR'),
    ])
    Type._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.structure_info.type',
        Type))

StructureInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.structure_info', {
        'name': type.StringType(),
        'type': type.ReferenceType(__name__, 'StructureInfo.Type'),
        'enumerations': type.MapType(type.IdType(), type.ReferenceType(__name__, 'EnumerationInfo')),
        'constants': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ConstantInfo')),
        'fields': type.ListType(type.ReferenceType(__name__, 'FieldInfo')),
        'metadata': type.MapType(type.StringType(), type.ReferenceType(__name__, 'ElementMap')),
        'documentation': type.StringType(),
    },
    StructureInfo,
    False,
    None))



class Type(VapiStruct):
    """
    The ``Type`` class describes the type information of a typed element in the
    interface definiton language. The following elements in the metamodel are
    typed: 
    
    * Field element in a structure element. See :attr:`StructureInfo.fields`
    * Parameter element in an operation element. See
      :attr:`OperationInfo.params`
    * Result element in an operation element. See :attr:`OperationInfo.output`
    
     The type could be one of the three following categories: 
    
    * Built-in types: These are types present in the interface definition
      language type system. They are provided by the infrastructure.
    * User defined named type: API designers can create custom types and use
      them for the typed elements. These types have a unique identifier.
    * Generic type instantiation: The language infrastructure also provides
      generic types such as list, map, set and so on. An instantiation of one of
      these generic types could also be used for the typed elements.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'category',
            {
                'BUILTIN' : [('builtin_type', True)],
                'USER_DEFINED' : [('user_defined_type', True)],
                'GENERIC' : [('generic_instantiation', True)],
            }
        ),
    ]



    def __init__(self,
                 category=None,
                 builtin_type=None,
                 user_defined_type=None,
                 generic_instantiation=None,
                ):
        """
        :type  category: :class:`Type.Category`
        :param category: Category of this type.
        :type  builtin_type: :class:`Type.BuiltinType`
        :param builtin_type: Category of the built-in type.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`Type.Category.BUILTIN`.
        :type  user_defined_type: :class:`UserDefinedType`
        :param user_defined_type: Identifier and type of the user defined type.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`Type.Category.USER_DEFINED`.
        :type  generic_instantiation: :class:`GenericInstantiation`
        :param generic_instantiation: Instantiation of one of the generic types available in the
            interface definition language.
            This attribute is optional and it is only relevant when the value
            of ``category`` is :attr:`Type.Category.GENERIC`.
        """
        self.category = category
        self.builtin_type = builtin_type
        self.user_defined_type = user_defined_type
        self.generic_instantiation = generic_instantiation
        VapiStruct.__init__(self)

    class Category(Enum):
        """
        The ``Type.Category`` class provides class attribute for each category of
        the type.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        BUILTIN = None
        """
        The type is one of the built-in types specified in
        :class:`Type.BuiltinType`

        """
        USER_DEFINED = None
        """
        The type is one of the user defined named types.

        """
        GENERIC = None
        """
        The type is an instantiation of one of the generic types.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`Category` instance.
            """
            Enum.__init__(string)

    Category._set_values([
        Category('BUILTIN'),
        Category('USER_DEFINED'),
        Category('GENERIC'),
    ])
    Category._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.type.category',
        Category))

    class BuiltinType(Enum):
        """
        The ``Type.BuiltinType`` class provides class attribute for each of the
        built-in types present in the interface definition language type system.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        VOID = None
        """
        The built-in type is a void. The value is None.

        """
        BOOLEAN = None
        """
        The built-in type is a boolean. The value is true or false.

        """
        LONG = None
        """
        The built-in type is a long. The value is a 64 bit signed integer.

        """
        DOUBLE = None
        """
        The built-in type is a double. The value is a 64 bit floating point number.

        """
        STRING = None
        """
        The built-in type is a string. The value is a variable-length sequence of
        zero or more unicode characters.

        """
        BINARY = None
        """
        The built-in type is a binary. The value is a variable-length sequence of
        zero or more bytes.

        """
        SECRET = None
        """
        The built-in type is a secret. The value is a variable-length sequence of
        zero or more unicode characters. The value contains sensitive data that
        should not be printed or displayed anywhere.

        """
        DATE_TIME = None
        """
        The built-in type is a datetime. The value should be in the UTC timezone
        and the precision is milliseconds.

        """
        ID = None
        """
        The built-in type is an ID. The value represents an identifier for a
        resource.

        """
        URI = None
        """
        The built-in type is an URI. The value follows the IRI specification in RFC
        3987.

        """
        ANY_ERROR = None
        """
        The built-in type is an arbitrary exception type. This is used if the value
        of a typed element can be one of any user defined named type which is an
        exception.

        """
        DYNAMIC_STRUCTURE = None
        """
        The built-in type is a dynamic structure. This is used if the value of a
        typed element can be one of any user defined named type.

        """
        OPAQUE = None
        """
        The built-in type is an opaque. This is used if the value of a typed
        element could be of any type and the actual type will be known only during
        the execution of the API. This is mostly used in infrastructure classes.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`BuiltinType` instance.
            """
            Enum.__init__(string)

    BuiltinType._set_values([
        BuiltinType('VOID'),
        BuiltinType('BOOLEAN'),
        BuiltinType('LONG'),
        BuiltinType('DOUBLE'),
        BuiltinType('STRING'),
        BuiltinType('BINARY'),
        BuiltinType('SECRET'),
        BuiltinType('DATE_TIME'),
        BuiltinType('ID'),
        BuiltinType('URI'),
        BuiltinType('ANY_ERROR'),
        BuiltinType('DYNAMIC_STRUCTURE'),
        BuiltinType('OPAQUE'),
    ])
    BuiltinType._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.metamodel.type.builtin_type',
        BuiltinType))

Type._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.type', {
        'category': type.ReferenceType(__name__, 'Type.Category'),
        'builtin_type': type.OptionalType(type.ReferenceType(__name__, 'Type.BuiltinType')),
        'user_defined_type': type.OptionalType(type.ReferenceType(__name__, 'UserDefinedType')),
        'generic_instantiation': type.OptionalType(type.ReferenceType(__name__, 'GenericInstantiation')),
    },
    Type,
    False,
    None))



class UserDefinedType(VapiStruct):
    """
    The ``UserDefinedType`` class contains the metamodel type information of a
    typed element whose type is a user defined named type.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 resource_type=None,
                 resource_id=None,
                ):
        """
        :type  resource_type: :class:`str`
        :param resource_type: Category of the user defined named type. The named type could be a
            structure element or an enumeration element.
            When clients pass a value of this class as a parameter, the
            attribute must be one of ``com.vmware.vapi.structure`` or
            ``com.vmware.vapi.enumeration``. When methods return a value of
            this class as a return value, the attribute will be one of
            ``com.vmware.vapi.structure`` or ``com.vmware.vapi.enumeration``.
        :type  resource_id: :class:`str`
        :param resource_id: Identifier of the user defined named type.
            When clients pass a value of this class as a parameter, the
            attribute must be an identifier for one of these resource types:
            ``com.vmware.vapi.structure`` or ``com.vmware.vapi.enumeration``.
            When methods return a value of this class as a return value, the
            attribute will be an identifier for one of these resource types:
            ``com.vmware.vapi.structure`` or ``com.vmware.vapi.enumeration``.
        """
        self.resource_type = resource_type
        self.resource_id = resource_id
        VapiStruct.__init__(self)

UserDefinedType._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.metamodel.user_defined_type', {
        'resource_type': type.StringType(),
        'resource_id': type.IdType(resource_types=["com.vmware.vapi.structure", "com.vmware.vapi.enumeration"], resource_type_field_name="resource_type"),
    },
    UserDefinedType,
    False,
    None))



class Component(VapiInterface):
    """
    The ``Component`` class providers methods to retrieve metamodel information
    of a component element. 
    
    A component defines a set of functionality that is deployed together and
    versioned together. For example, all the classes that belong to VMware
    Content Library are part of a single component. A component element
    describes a component. A component element contains one or more package
    elements. 
    
     The methods for package elements are provided by class :class:`Package`.
    """
    RESOURCE_TYPE = "com.vmware.vapi.component"
    """
    Resource type for component.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ComponentStub)


    def list(self):
        """
        Returns the identifiers for the component elements that are registered
        with the infrastructure.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the component elements that are
            registered with the infrastructure.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.component``.
        """
        return self._invoke('list', None)

    def get(self,
            component_id,
            ):
        """
        Retrieves metamodel information about the component element
        corresponding to ``component_id``. 
        
        The :class:`ComponentData` contains the metamodel information about the
        component and it's fingerprint. It contains information about all the
        package elements that are contained in this component element.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`ComponentData`
        :return: The :class:`ComponentData` instance that corresponds to
            ``component_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` is not
            registered with the infrastructure.
        """
        return self._invoke('get',
                            {
                            'component_id': component_id,
                            })

    def fingerprint(self,
                    component_id,
                    ):
        """
        Retrieves the fingerprint computed from the metamodel metadata of the
        component element corresponding to ``component_id``. 
        
        The fingerprint provides clients an efficient way to check if the
        metadata for a particular component element has been modified on the
        server. The client can do this by comparing the result of this
        operation with the fingerprint returned in the result of
        :func:`Component.get`.

        :type  component_id: :class:`str`
        :param component_id: Identifier of the component element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        :rtype: :class:`str`
        :return: The fingerprint computed from the metamodel metadata of the
            component element.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the component element associated with ``component_id`` is not
            registered with the infrastructure.
        """
        return self._invoke('fingerprint',
                            {
                            'component_id': component_id,
                            })
class Enumeration(VapiInterface):
    """
    The ``Enumeration`` class provides methods to retrieve metamodel
    information about an enumeration element in the interface definition
    language. 
    
     The ``Enumeration`` has a list of enumeration value elements.
    """
    RESOURCE_TYPE = "com.vmware.vapi.enumeration"
    """
    Resource type for enumeration.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _EnumerationStub)


    def list(self):
        """
        Returns the identifiers for the enumeration elements that are contained
        in all the package elements, service elements and structure elements.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the enumeration elements.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.enumeration``.
        """
        return self._invoke('list', None)

    def get(self,
            enumeration_id,
            ):
        """
        Retrieves information about the enumeration element corresponding to
        ``enumeration_id``. 
        
        The :class:`EnumerationInfo` contains the metamodel information about
        the enumeration value element contained in the enumeration element.

        :type  enumeration_id: :class:`str`
        :param enumeration_id: Identifier of the enumeration element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.enumeration``.
        :rtype: :class:`EnumerationInfo`
        :return: The :class:`EnumerationInfo` instance that corresponds to
            ``enumeration_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the enumeration element associated with ``enumeration_id`` is
            not contained in any of the package elements, service elements and
            structure elements.
        """
        return self._invoke('get',
                            {
                            'enumeration_id': enumeration_id,
                            })
class MetadataIdentifier(VapiInterface):
    """
    The ``MetadataIdentifier`` class provides string constants that can be used
    as identifiers for the metadata elements. 
    
    Most of the types in :mod:`com.vmware.vapi.metadata.metamodel_client`
    package has a metadata field whose type is ``Map<String, ElementMap>``.
    :class:`MetadataIdentifier` contains the identifiers used in the keys of
    the above Map type.
    """
    CANONICAL_NAME = "CanonicalName"
    """
    Identifier representing the CanonicalName metadata.

    """
    COMPONENT = "Component"
    """
    Identifier representing the Component metadata.

    """
    CREATE = "Create"
    """
    Identifier representing the Create metadata.

    """
    CRUD = "Crud"
    """
    Identifier representing the Crud metadata.

    """
    HAS_FIELDS_OF = "HasFieldsOf"
    """
    Identifier representing the HasFieldsOf metadata.

    """
    INCLUDABLE = "Includable"
    """
    Identifier representing the Includable metadata.

    """
    INCLUDE = "Include"
    """
    Identifier representing the Include metadata.

    """
    IS_ONE_OF = "IsOneOf"
    """
    Identifier representing the IsOneOf metadata.

    """
    MODEL = "Model"
    """
    Identifier representing the Model metadata.

    """
    READ = "Read"
    """
    Identifier representing the Read metadata.

    """
    RESOURCE = "Resource"
    """
    Identifier representing the Resource metadata.

    """
    UNION_CASE = "UnionCase"
    """
    Identifier representing the UnionCase metadata.

    """
    UNION_TAG = "UnionTag"
    """
    Identifier representing the UnionTag metadata.

    """
    UPDATE = "Update"
    """
    Identifier representing the Update metadata.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MetadataIdentifierStub)

class Package(VapiInterface):
    """
    The ``Package`` class provides methods to retrieve metamodel information
    about a package element in the interface definition language. 
    
    A package is a logical grouping of services, structures and enumerations. A
    package element describes the package. It contains the service elements,
    structure elements and enumeration elements that are grouped together.
    """
    RESOURCE_TYPE = "com.vmware.vapi.package"
    """
    Resource type for package.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _PackageStub)


    def list(self):
        """
        Returns the identifiers for the packages elements that are contained in
        all the registered component elements.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the package elements that are contained
            in all the registered component elements.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.package``.
        """
        return self._invoke('list', None)

    def get(self,
            package_id,
            ):
        """
        Retrieves information about the package element corresponding to
        ``package_id``.

        :type  package_id: :class:`str`
        :param package_id: Identifier of the package element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.package``.
        :rtype: :class:`PackageInfo`
        :return: The :class:`PackageInfo` instance that corresponds to
            ``package_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the package element associated with ``package_id`` does not
            exist.
        """
        return self._invoke('get',
                            {
                            'package_id': package_id,
                            })
class Resource(VapiInterface):
    """
    The :class:`Resource` class provides methods to retrieve information about
    resource types. 
    
    A service is a logical grouping of operations that operate on an entity.
    Each entity is identifier by a namespace (or resource type) and an unique
    identifier.
    """
    RESOURCE_TYPE = "com.vmware.vapi.resource"
    """
    Resource type for resource.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ResourceStub)


    def list(self):
        """
        Returns the set of resource types present across all the service
        elements contained in all the package elements.


        :rtype: :class:`set` of :class:`str`
        :return: Set of resource types
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.resource``.
        """
        return self._invoke('list', None)
class Service(VapiInterface):
    """
    The ``Service`` class provides methods to retrieve metamodel information
    about a service element in the interface definition language. 
    
    A service is a logical grouping of operations that operate on some entity.
    A service element describes a service. It contains operation elements that
    describe the operations grouped in the service. It also contains structure
    elements and enumeration elements corresponding to the structures and
    enumerations defined in the service.
    """
    RESOURCE_TYPE = "com.vmware.vapi.service"
    """
    Resource type for service.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ServiceStub)


    def list(self):
        """
        Returns the identifiers for the service elements that are currently
        registered with the infrastructure. 
        
        The list of service elements is an aggregate list of all the service
        elements contained in all the package elements.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the service elements that are currently
            registered with the infrastructure.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.service``.
        """
        return self._invoke('list', None)

    def get(self,
            service_id,
            ):
        """
        Retrieves information about the service element corresponding to
        ``service_id``. 
        
        The :class:`ServiceInfo` contains the metamodel information for the
        operation elements, structure elements and enumeration elements
        contained in the service element.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.service``.
        :rtype: :class:`ServiceInfo`
        :return: The :class:`ServiceInfo` instance that corresponds to
            ``service_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the service element associated with ``service_id`` is not
            registered with the infrastructure.
        """
        return self._invoke('get',
                            {
                            'service_id': service_id,
                            })
class Source(VapiInterface):
    """
    The ``Source`` class provides methods to manage the sources of metamodel
    metadata information. 
    
    The interface definition language infrastructure provides tools to generate
    various kinds of metadata in JSON format from the interface definition
    files and additional properties files. One of the generated files contains
    metamodel information. The generated file can be registered as a source of
    metadata. 
    
    The metamodel file contains all the data present in the interface
    definition files. Each metamodel file contains data about one component
    element. When a metamodel file is added as a source, each source
    contributes only one component element's metadata. 
    
    Metamodel metadata can also be discovered from a remote server that
    supports the metamodel metadata classes (see
    :mod:`com.vmware.vapi.metadata.metamodel_client`). Since multiple
    components can be registered with a single metadata server, when a remote
    server is registered as a source, that source can contribute more than one
    component.
    """
    RESOURCE_TYPE = "com.vmware.vapi.metadata.metamodel.source"
    """
    Resource type for metadata source.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SourceStub)

    class Info(VapiStruct):
        """
        The ``Source.Info`` class contains the metadata source information.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('filepath', True)],
                    'REMOTE' : [('address', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     type=None,
                     filepath=None,
                     address=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: English language human readable description of the source.
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: Type of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the metamodel metadata file that has the
                metamodel information about one component element. The ``filePath``
                is the path to the file in the server's filesystem.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information for the remote server. This must be in the
                format http(s)://IP:port/namespace. 
                
                The remote server must support the classes in the
                :mod:`com.vmware.vapi.metadata.metamodel_client` module. It must
                expose metamodel information of one or more components.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.metamodel.source.info', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Source.CreateSpec`` class contains the registration information of a
        metamodel source.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """

        _validator_list = [
            UnionValidator(
                'type',
                {
                    'FILE' : [('filepath', True)],
                    'REMOTE' : [('address', True)],
                }
            ),
        ]



        def __init__(self,
                     description=None,
                     type=None,
                     filepath=None,
                     address=None,
                    ):
            """
            :type  description: :class:`str`
            :param description: English language human readable description of the source.
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: Type of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the metamodel metadata file that has the
                metamodel information about one component element.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information of the remote server. This should be of the
                format http(s)://IP:port/namespace. 
                
                The remote server should contain the classes in
                :mod:`com.vmware.vapi.metadata.metamodel_client` module. It could
                expose metamodel information of one or more components.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.metamodel.source.create_spec', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        CreateSpec,
        False,
        None))



    def create(self,
               source_id,
               spec,
               ):
        """
        Creates a new metadata source. Once the server validates the
        registration information of the metadata source, the metamodel metadata
        is retrieved from the source. This populates elements in all the
        classes defined in :mod:`com.vmware.vapi.metadata.metamodel_client`
        module.

        :type  source_id: :class:`str`
        :param source_id: metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
        :type  spec: :class:`Source.CreateSpec`
        :param spec: create specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            if the metadata source identifier is already registered with the
            infrastructure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the type of the source specified in null is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the file specified in null is not a valid JSON file or if the
            format of the metamodel metadata in the JSON file is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            if the URI specified in null is unreachable or if there is a
            transport protocol or message protocol mismatch between the client
            and the server or if the remote server do not have classes present
            in :mod:`com.vmware.vapi.metadata.metamodel_client` module.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the file specified in null does not exist.
        """
        return self._invoke('create',
                            {
                            'source_id': source_id,
                            'spec': spec,
                            })

    def delete(self,
               source_id,
               ):
        """
        Deletes an existing metamodel metadata source from the infrastructure.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('delete',
                            {
                            'source_id': source_id,
                            })

    def get(self,
            source_id,
            ):
        """
        Retrieves information about the metadata source corresponding to
        ``source_id``.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
        :rtype: :class:`Source.Info`
        :return: The :class:`Source.Info` instance that corresponds to ``source_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('get',
                            {
                            'source_id': source_id,
                            })

    def list(self):
        """
        Returns the identifiers of the metadata sources currently registered
        with the infrastructure.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for metadata sources currently registered.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
        """
        return self._invoke('list', None)

    def reload(self,
               source_id=None,
               ):
        """
        Reloads the metamodel metadata from all the metadata sources or of a
        particular metadata source if ``source_id`` is specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
            If unspecified, all the metadata sources are reloaded.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('reload',
                            {
                            'source_id': source_id,
                            })

    def fingerprint(self,
                    source_id=None,
                    ):
        """
        Returns the aggregate fingerprint of metadata from all the metadata
        sources or from a particular metadata source if ``source_id`` is
        specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.metamodel.source``.
            If unspecified, the fingerprint of all the metadata sources is
            returned.
        :rtype: :class:`str`
        :return: Aggregate fingerprint of all the metadata sources or of a
            particular metadata source.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the metadata source associated with ``source_id`` is not found.
        """
        return self._invoke('fingerprint',
                            {
                            'source_id': source_id,
                            })
class Structure(VapiInterface):
    """
    The ``Structure`` class providers methods to retrieve metamodel information
    about a structure element in the interface definition language.
    """
    RESOURCE_TYPE = "com.vmware.vapi.structure"
    """
    Resource type for structure.

    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StructureStub)


    def list(self):
        """
        Returns the identifiers for the structure elements that are contained
        in all the package elements and service elements.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for the structure elements.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.structure``.
        """
        return self._invoke('list', None)

    def get(self,
            structure_id,
            ):
        """
        Retrieves information about the structure element corresponding to
        ``structure_id``. 
        
        The :class:`StructureInfo` contains the metamodel information about the
        structure element. It contains information about all the field elements
        and enumeration elements contained in this structure element.

        :type  structure_id: :class:`str`
        :param structure_id: Identifier of the structure element.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.structure``.
        :rtype: :class:`StructureInfo`
        :return: The :class:`StructureInfo` instance that corresponds to
            ``structure_id``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the structure element associated with ``structure_id`` is not
            contained in any of the package elements or service elements.
        """
        return self._invoke('get',
                            {
                            'structure_id': structure_id,
                            })
class _ComponentStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
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

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'component_id': type.IdType(resource_types='com.vmware.vapi.component'),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ComponentData'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.component',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _EnumerationStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'enumeration_id': type.IdType(resource_types='com.vmware.vapi.enumeration'),
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

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'EnumerationInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.enumeration',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _MetadataIdentifierStub(ApiInterfaceStub):
    def __init__(self, config):
        operations = {
        }
        rest_metadata = {
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.metadata_identifier',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _PackageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'package_id': type.IdType(resource_types='com.vmware.vapi.package'),
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

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'PackageInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.package',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ResourceStub(ApiInterfaceStub):
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
                'output_type': type.SetType(type.IdType()),
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
            self, iface_name='com.vmware.vapi.metadata.metamodel.resource',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _ServiceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
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

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'ServiceInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.service',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SourceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.metamodel.source'),
            'spec': type.ReferenceType(__name__, 'Source.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
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

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.metamodel.source'),
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.metamodel.source'),
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

        # properties for reload operation
        reload_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        reload_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reload_input_value_validator_list = [
        ]
        reload_output_validator_list = [
        ]
        reload_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
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
                'output_type': type.ReferenceType(__name__, 'Source.Info'),
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
            'reload': {
                'input_type': reload_input_type,
                'output_type': type.VoidType(),
                'errors': reload_error_dict,
                'input_value_validator_list': reload_input_value_validator_list,
                'output_validator_list': reload_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'reload': reload_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.source',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _StructureStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'structure_id': type.IdType(resource_types='com.vmware.vapi.structure'),
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

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'StructureInfo'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.structure',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Component': Component,
        'Enumeration': Enumeration,
        'MetadataIdentifier': MetadataIdentifier,
        'Package': Package,
        'Resource': Resource,
        'Service': Service,
        'Source': Source,
        'Structure': Structure,
        'resource': 'com.vmware.vapi.metadata.metamodel.resource_client.StubFactory',
        'service': 'com.vmware.vapi.metadata.metamodel.service_client.StubFactory',
    }

