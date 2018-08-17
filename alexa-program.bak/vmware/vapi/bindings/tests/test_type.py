#!/usr/bin/env python

"""
Unit tests for the type system
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import sys
import unittest

from vmware.vapi.bindings.type import (IntegerType, DoubleType, ReferenceType,
    BooleanType, StringType, BlobType, VoidType, OpaqueType, URIType,
    ListType, StructType, OptionalType, SecretType, DateTimeType, EnumType, IdType,
    AnyErrorType, MapType, SetType)
from vmware.vapi.data.definition import (IntegerDefinition, DoubleDefinition,
    BooleanDefinition, StringDefinition, BlobDefinition, VoidDefinition,
    OpaqueDefinition, ListDefinition, StructDefinition, OptionalDefinition,
    SecretDefinition, StructRefDefinition, AnyErrorDefinition)
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.lib.constants import MAP_ENTRY

class TopLevelStruct(VapiStruct):
    def __init__(self, **kwargs):
        self.dbl1 = kwargs.get('dbl1')
        VapiStruct.__init__(self)

    class NestedStruct(VapiStruct):
        def __init__(self, **kwargs):
            self.str1 = kwargs.get('str1')
            VapiStruct.__init__(self)
    NestedStruct._set_binding_type(StructType(
        'nested_struct', {
            'str1': StringType(),
        },
        NestedStruct))

TopLevelStruct._set_binding_type(StructType(
    'top_level_struct', {
        'dbl1': DoubleType(),
    }, TopLevelStruct))


class TopLevelStruct2(VapiStruct):
    def __init__(self, **kwargs):
        self.field1 = kwargs.get('field1')
        self.field2 = kwargs.get('field2')
        VapiStruct.__init__(self)

TopLevelStruct2._set_binding_type(StructType(
    'top_level_struct_2', {
        'field1': ReferenceType(__name__, 'TopLevelStruct'),
        'field2': ReferenceType(__name__, 'TopLevelStruct.NestedStruct'),
    }, TopLevelStruct2))


class ModelStruct(VapiStruct):
    def __init__(self, **kwargs):
        self.model_key = kwargs.get('model_key')
        VapiStruct.__init__(self)

ModelStruct._set_binding_type(StructType(
    'model_struct', {
        'model_key': IdType("model"),
    }, ModelStruct, is_model=True, model_keys=["model_key"]))

class TestEnum(Enum):
    TWO = None
    THREE = None
    FOUR = None

    def __init__(self, s=''):
        Enum.__init__(s)

TestEnum.TWO = TestEnum('TWO')
TestEnum.THREE = TestEnum('THREE')
TestEnum.FOUR = TestEnum('FOUR')
TestEnum._set_binding_type(EnumType(
    'test_enum',
    TestEnum))


class ReferenceLocalRecursive(VapiStruct):
    # class LinkedList {
    #     String data;
    #     Optional<LinkedList> nextNode;
    # }
    def __init__(self, **kwargs):
        self.data = kwargs.get('data')
        self.next_node = kwargs.get('next_node')

ReferenceLocalRecursive._set_binding_type(StructType(
    'linked_list', {
        'data': StringType(),
        'next_node': ReferenceType(__name__, 'ReferenceLocalRecursive')
    }))

class MultipleStructReferences(VapiStruct):
    # class MultipleStructReferences {
    #     String string_field;
    #     TopLevelStruct structure_field1;
    #      TopLevelStruct structure_field2;
    # }
    def __init__(self, **kwargs):
        self.name = kwargs.get('string_field')
        self.structure_field1 = kwargs.get('structure_field1')
        self.structure_field2 = kwargs.get('structure_field2')

MultipleStructReferences._set_binding_type(StructType(
    'multiple_struct_references', {
        'string_field': StringType(),
        'structure_field1': ReferenceType(__name__, 'TopLevelStruct'),
        'structure_field2': ReferenceType(__name__, 'TopLevelStruct')
    }))

class TestType(unittest.TestCase):

    def setUp(self):
        pass

    def test_void_type(self):
        void_type = VoidType()
        self.assertNotEqual(void_type, None)
        self.assertEqual(void_type.definition, VoidDefinition())

    def test_integer_type(self):
        int_type = IntegerType()
        self.assertNotEqual(int_type, None)
        self.assertEqual(int_type.definition, IntegerDefinition())

    def test_double_type(self):
        d_type = DoubleType()
        self.assertNotEqual(d_type, None)
        self.assertEqual(d_type.definition, DoubleDefinition())

    def test_string_type(self):
        s_type = StringType()
        self.assertNotEqual(s_type, None)
        self.assertEqual(s_type.definition, StringDefinition())

    def test_secret_type(self):
        s_type = SecretType()
        self.assertNotEqual(s_type, None)
        self.assertEqual(s_type.definition, SecretDefinition())

    def test_boolean_type(self):
        b_type = BooleanType()
        self.assertNotEqual(b_type, None)
        self.assertEqual(b_type.definition, BooleanDefinition())

    def test_blob_type(self):
        blob_type = BlobType()
        self.assertNotEqual(blob_type, None)
        self.assertEqual(blob_type.definition, BlobDefinition())

    def test_opaque_type(self):
        opaque_type = OpaqueType()
        self.assertNotEqual(opaque_type, None)
        self.assertEqual(opaque_type.definition, OpaqueDefinition())

    def test_any_error_type(self):
        any_error_type = AnyErrorType()
        self.assertNotEqual(any_error_type, None)
        self.assertEqual(any_error_type.definition, AnyErrorDefinition())

    def test_optional_type(self):
        opt_type = OptionalType(IntegerType())
        self.assertNotEqual(opt_type, None)
        self.assertEqual(opt_type.definition,
                         OptionalDefinition(IntegerDefinition()))
        self.assertEqual(opt_type.element_type.definition,
                         IntegerDefinition())

    def test_invalid_optional_type(self):
        self.assertRaises(TypeError, OptionalType, None)
        self.assertRaises(TypeError, OptionalType, IntegerDefinition())

    def test_list_type(self):
        list_type = ListType(IntegerType())
        self.assertNotEqual(list_type, None)
        self.assertEqual(list_type.definition,
                         ListDefinition(IntegerDefinition()))
        self.assertEqual(list_type.element_type.definition,
                         IntegerDefinition())

    def test_invalid_list_type(self):
        self.assertRaises(TypeError, ListType, None)
        self.assertRaises(TypeError, ListType, IntegerDefinition())

    def test_struct_type(self):
        fields = {
            'name': StringType(),
            'age': IntegerType(),
            'address': OptionalType(StringType()),
        }
        struct_type = StructType('test', fields)

        fields_def = [
            ('name', StringDefinition()),
            ('age', IntegerDefinition()),
            ('address', OptionalDefinition(StringDefinition())),
        ]
        struct_def = StructDefinition('test', fields_def)

        self.assertNotEqual(struct_type, None)
        self.assertEqual(struct_type.definition, struct_def)
        self.assertEqual(struct_type.name, 'test')
        self.assertEqual(sorted(struct_type.get_field_names()),
                         sorted(struct_def.get_field_names()))
        for field in struct_type.get_field_names():
            self.assertEqual(struct_type.get_field(field).definition,
                             struct_def.get_field(field))

    def test_invalid_struct_type(self):
        self.assertRaises(TypeError, StructType, 'test', [])
        self.assertRaises(TypeError, StructType, 10, {})
        self.assertRaises(TypeError, StructType, 'test',
                          {'name': StringDefinition()})

    def test_datetime_type(self):
        dt_type = DateTimeType()
        self.assertNotEqual(dt_type, None)
        self.assertEqual(dt_type.definition, StringDefinition())

    def test_uri_type(self):
        uri_type = URIType()
        self.assertNotEqual(uri_type, None)
        self.assertEqual(uri_type.definition, StringDefinition())

    def test_enum_type(self):
        enum_name = 'test_enum'
        enum_type = TestEnum.get_binding_type()
        self.assertNotEqual(enum_type, None)
        self.assertEqual(enum_type.name, enum_name)
        self.assertEqual(enum_type.definition, StringDefinition())

    def test_map_type(self):
        map_type = MapType(StringType(), StringType())
        self.assertNotEqual(map_type, None)
        self.assertEqual(map_type.definition,
                         ListDefinition(
                            StructDefinition(
                                MAP_ENTRY,
                                [('key', StringDefinition()),
                                 ('value', StringDefinition())]
                            )
                         ))
        self.assertRaises(TypeError,
                          MapType, 'bogus', StringType())
        self.assertRaises(TypeError,
                          MapType, StringType(), 'bogus')

    def test_set_type(self):
        set_type = SetType(StringType())
        self.assertNotEqual(set_type, None)
        self.assertEqual(set_type.definition,
                         ListDefinition(StringDefinition()))
        self.assertRaises(TypeError, SetType, 'bogus')

    def test_id_type(self):
        # Static id
        id_type = IdType(resource_types="id1")
        self.assertNotEqual(id_type, None)
        self.assertEqual(id_type.resource_types, "id1")
        self.assertEqual(id_type.resource_type_field_name, None)

        # Polymorphic id
        id_type = IdType(resource_types=["id1", "id2"],
                         resource_type_field_name="id_type")
        self.assertNotEqual(id_type, None)
        self.assertEqual(id_type.resource_types, ["id1", "id2"])
        self.assertEqual(id_type.resource_type_field_name, "id_type")

        # Polymorphic any id
        id_type = IdType(resource_type_field_name="id_type")
        self.assertNotEqual(id_type, None)
        self.assertEqual(id_type.resource_types, None)
        self.assertEqual(id_type.resource_type_field_name, "id_type")

    def test_reference_type_locals(self):
        struct_type = TopLevelStruct.get_binding_type()
        reference_type = TopLevelStruct2.get_binding_type().get_field('field1')
        self.assertNotEqual(reference_type, None)
        self.assertEqual(reference_type.resolved_type.name,
                         struct_type.name)
        self.assertEqual(reference_type.resolved_type.get_field_names(),
                         struct_type.get_field_names())
        self.assertEqual(reference_type.resolved_type.get_field('db1'),
                         struct_type.get_field('db1'))
        self.assertEqual(reference_type.resolved_type.definition,
                         struct_type.definition)

    def test_reference_type_nested(self):
        struct_type = TopLevelStruct.NestedStruct.get_binding_type()
        reference_type = TopLevelStruct2.get_binding_type().get_field('field2')
        self.assertNotEqual(reference_type, None)
        self.assertEqual(reference_type.resolved_type.name,
                         struct_type.name)
        self.assertEqual(reference_type.resolved_type.get_field_names(),
                         struct_type.get_field_names())
        self.assertEqual(reference_type.resolved_type.get_field('str1'),
                         struct_type.get_field('str1'))
        self.assertEqual(reference_type.resolved_type.definition,
                         struct_type.definition)

    def test_invalid_reference_type(self):
        self.assertRaises(TypeError, ReferenceType, None, None)
        self.assertRaises(TypeError, ReferenceType, sys.modules[__name__], '')
        self.assertRaises(TypeError, ReferenceType, sys.modules[__name__], TopLevelStruct)
        self.assertRaises(TypeError, ReferenceType, __name__, TopLevelStruct)

    def test_recursive_structure(self):
        linked_list_type = ReferenceLocalRecursive.get_binding_type()
        expected_definition = StructDefinition(
            'linked_list', [('data', StringDefinition()),
                            ('next_node', StructRefDefinition('linked_list'))])
        self.assertEqual(linked_list_type.definition,
                         expected_definition)

    def test_model_struct(self):
        model_type = ModelStruct.get_binding_type()
        self.assertTrue(model_type.is_model)
        self.assertEqual(model_type.model_keys, ["model_key"])

    def test_multiple_struct_references(self):
        top_level_struct_type = TopLevelStruct.get_binding_type()
        multiple_struct_references_type = MultipleStructReferences.get_binding_type()
        expected_definition = StructDefinition(
            'multiple_struct_references',
            [('string_field', StringDefinition()),
             ('structure_field1', top_level_struct_type.definition),
             ('structure_field2', top_level_struct_type.definition)])
        self.assertEqual(multiple_struct_references_type.definition,
                         expected_definition)

    def test_equals_operation_on_struct(self):
        model1 = ModelStruct(model_key='model1')
        model2 = None
        self.assertNotEqual(model1, model2)
        model2 = ModelStruct(model_key='model1')
        self.assertEqual(model1, model2)

if __name__ == "__main__":
    unittest.main()
