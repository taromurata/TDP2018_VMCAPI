#!/usr/bin/env python
"""
Unit tests for DataValue <-> Python native value (de)serialization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import base64
import decimal
import logging
import six
import sys
import unittest

from vmware.vapi.bindings.type import (IntegerType, DoubleType,
    BooleanType, StringType, BlobType, VoidType, OpaqueType, IdType,
    ListType, StructType, ErrorType, OptionalType, SecretType, EnumType,
    AnyErrorType, DynamicStructType, MapType, SetType, ReferenceType)
from vmware.vapi.data.value import (IntegerValue, DoubleValue, \
    BooleanValue, StringValue, BlobValue, VoidValue,
    ListValue, OptionalValue, SecretValue)
from vmware.vapi.data.value import StructValue
from vmware.vapi.bindings.converter import RestConverter, TypeConverter
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.bindings.error import (VapiError, UnresolvedError)
from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.common import NameToTypeResolver
from vmware.vapi.exception import CoreException
from vmware.vapi.lib.std import (
    make_std_error_def, make_error_value_from_msg_id)
from com.vmware.vapi.std_client import LocalizableMessage
from com.vmware.vapi.std.errors_client import (Error, TimedOut)

'''
The classes below in the test code represent simulated binding classes for the
following VMODL:

class Properties {
    long intVal;
    String strVal;
    boolean boolVal;
    Optional<Long> optVal;
    List<Long> listVal;
}

class CopyOfProperties {
    long intVal;
    String strVal;
    boolean boolVal;
    Optional<Long> optVal;
    List<Long> listVal;
}

class PropertiesWithDynamicStructure {
    long intVal;
    DynamicStructure dynStrVal;
}

class OuterStructure {
    Properties structVal;
}

class StructureHavingFieldWithDifferentCanonicalName {
    @CanonicalName("size_MiB")
    long sizeMiB;
    @CanonicalName("_def")
    String def; //python reserved word
}
'''

class Properties(VapiStruct):
    def __init__(self, **kwargs):
        self.int_val = kwargs.get('int_val')
        self.str_val = kwargs.get('str_val')
        self.bool_val = kwargs.get('bool_val')
        self.opt_val = kwargs.get('opt_val')
        self.list_val = kwargs.get('list_val')
        VapiStruct.__init__(self)

Properties._set_binding_type(StructType(
    'properties', {
        'int_val': IntegerType(),
        'str_val': StringType(),
        'bool_val': BooleanType(),
        'opt_val': OptionalType(IntegerType()),
        'list_val': ListType(IntegerType()),
    }, Properties))

class CopyOfProperties(Properties):
    pass

CopyOfProperties._set_binding_type(StructType(
    'copy_of_properties', {
        'int_val': IntegerType(),
        'str_val': StringType(),
        'bool_val': BooleanType(),
        'opt_val': OptionalType(IntegerType()),
        'list_val': ListType(IntegerType()),
    }, CopyOfProperties))

class PropertiesWithDynamicStructure(VapiStruct):
    def __init__(self, int_val, dyn_str_val):
        self.int_val = int_val
        self.dyn_str_val = dyn_str_val
        VapiStruct.__init__(self)

PropertiesWithDynamicStructure._set_binding_type(StructType(
    'properties_with_dynamic_structure', {
        'int_val': IntegerType(),
        'dyn_str_val': DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct),
    }, PropertiesWithDynamicStructure))

class OuterStructure(VapiStruct):
    def __init__(self, **kwargs):
        self.struct_val = kwargs.get('struct_val')
        VapiStruct.__init__(self)

OuterStructure._set_binding_type(StructType(
    'outer_structure', {
        'struct_val': ReferenceType(__name__, 'Properties'),
    }, OuterStructure))

class StructureHavingFieldWithDifferentCanonicalName(VapiStruct):
    _canonical_to_pep_names = {
        'size_MiB': 'size_mib',
        '_def': 'def_',
    }
    def __init__(self, size_mib, def_):
        self.size_mib = size_mib
        self.def_ = def_
        VapiStruct.__init__(self)

StructureHavingFieldWithDifferentCanonicalName._set_binding_type(StructType(
    'structure_having_field_with_different_canonical_name', {
        'size_MiB': IntegerType(),
        '_def': StringType()
    }, StructureHavingFieldWithDifferentCanonicalName))

class TestBindingTypeConverter(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_void(self):
        # Void Conversion
        data_def = VoidType()
        data_val = TypeConverter.convert_to_vapi(None, data_def)
        self.assertEqual(data_val, VoidValue())
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, None)

    def test_invalid_value_to_void(self):
        data_def = VoidType()
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          1, data_def)

    def test_integer(self):
        # Integer Conversion
        data_def = IntegerType()
        data_val = TypeConverter.convert_to_vapi(10, data_def)
        self.assertEqual(data_val, IntegerValue(10))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, 10)
            self.assertTrue(isinstance(py_val, six.integer_types))

    def test_double(self):
        # Double Conversion
        data_def = DoubleType()
        data_val = TypeConverter.convert_to_vapi(11.11, data_def)
        self.assertEqual(data_val, DoubleValue(11.11))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, decimal.Decimal('11.11'))
            self.assertTrue(isinstance(py_val, decimal.Decimal))

        decimal_val = decimal.Decimal('1E-130')
        data_val = TypeConverter.convert_to_vapi(decimal_val,
                                                 data_def)
        self.assertEqual(data_val, DoubleValue(decimal_val))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, decimal_val)
            self.assertTrue(isinstance(py_val, decimal.Decimal))

    def test_string(self):
        # String Conversion
        data_def = StringType()
        data_val = TypeConverter.convert_to_vapi('test', data_def)
        self.assertEqual(data_val, StringValue('test'))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, 'test')
            self.assertTrue(isinstance(py_val, str))

    def test_unicode_string(self):
        data_type = StringType()
        actual_val = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        data_val = TypeConverter.convert_to_vapi(actual_val, data_type)
        self.assertEqual(data_val, StringValue(actual_val))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_type,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, actual_val)
            self.assertTrue(isinstance(py_val, six.string_types))

    def test_big_unicode_string(self):
        data_type = StringType()
        actual_val = u'\U0001d120'
        data_val = TypeConverter.convert_to_vapi(actual_val, data_type)
        self.assertEqual(data_val, StringValue(actual_val))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_type,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, actual_val)
            self.assertTrue(isinstance(py_val, six.string_types))

    def test_secret(self):
        # Secret Conversion
        data_def = SecretType()
        data_val = TypeConverter.convert_to_vapi('test', data_def)
        self.assertEqual(data_val, SecretValue('test'))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, 'test')
            self.assertTrue(isinstance(py_val, str))

    def test_id(self):
        id_value = 'id'
        data_def = IdType()
        data_val = TypeConverter.convert_to_vapi(id_value, data_def)
        self.assertEqual(data_val, StringValue(id_value))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, id_value)
            self.assertTrue(isinstance(py_val, str))

    def test_blob(self):
        # Blob Conversion
        data_def = BlobType()
        data_val = TypeConverter.convert_to_vapi(b'test', data_def)
        self.assertEqual(data_val, BlobValue(b'test'))
        for rest_converter_mode in [None]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, b'test')
            self.assertTrue(isinstance(py_val, six.binary_type))

    def test_boolean(self):
        # Boolean Conversion
        data_def = BooleanType()
        data_val = TypeConverter.convert_to_vapi(True, data_def)
        self.assertEqual(data_val, BooleanValue(True))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, True)
            self.assertTrue(isinstance(py_val, bool))
        data_def = BooleanType()
        data_val = TypeConverter.convert_to_vapi(False, data_def)
        self.assertEqual(data_val, BooleanValue(False))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, False)
            self.assertTrue(isinstance(py_val, bool))

    def test_opaque_primitive(self):
        data_def = OpaqueType()
        data_val = IntegerValue(10)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, data_val)
        py_val2 = TypeConverter.convert_to_vapi(data_val, data_def)
        self.assertEqual(py_val2, data_val)

    def test_opaque_generic(self):
        data_def = OpaqueType()
        data_val = ListValue()
        data_val.add(IntegerValue(10))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, data_val)
        py_val2 = TypeConverter.convert_to_vapi(data_val, data_def)
        self.assertEqual(py_val2, data_val)

    def test_opaque_invalid(self):
        data_def = OpaqueType()
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          10, data_def)

    def test_optional(self):
        data_def = OptionalType(IntegerType())
        data_val = TypeConverter.convert_to_vapi(10, data_def)
        self.assertEqual(data_val, OptionalValue(value=IntegerValue(10)))
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, 10)
            self.assertIsInstance(py_val, six.integer_types)

        data_val = TypeConverter.convert_to_vapi(None, data_def)
        self.assertEqual(data_val, OptionalValue())
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val = TypeConverter.convert_to_python(data_val, data_def,
                                                     rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, None)

    def test_dynamic_structure(self):
        binding_type = PropertiesWithDynamicStructure.get_binding_type()
        py_val = PropertiesWithDynamicStructure(
            int_val=10,
            dyn_str_val=VapiStruct(struct_value=StructValue(name='test')))
        actual_val = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_def = binding_type.definition
        expected_val = data_def.new_value()
        expected_val.set_field('int_val', IntegerValue(10))
        expected_val.set_field('dyn_str_val', StructValue(name='test'))
        self.assertEqual(expected_val, actual_val)

        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_actual_val = TypeConverter.convert_to_python(actual_val, binding_type,
                                                            rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_actual_val)

    def test_structure(self):
        fields = {'int_val': IntegerType(),
                  'str_val': StringType(),
                  'bool_val': BooleanType(),
                  'opt_val': OptionalType(IntegerType()),
                  'list_val': ListType(IntegerType()),
                 }
        binding_type = StructType('properties', fields, Properties)
        data_def = binding_type.definition

        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30])
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(data_valc, data_val)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_valc, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

            self.assertEqual(py_valc.get_struct_value(), data_val)

    def test_structure_with_unset_optional_fields(self):
        binding_type = Properties.get_binding_type()
        data_def = binding_type.definition

        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            list_val=[10, 20, 30])
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue())
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(data_valc, data_val)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_valc, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)
            self.assertEqual(py_valc.get_struct_value(), data_val)

    def test_structure_with_missing_optional_value_wrappers(self):
        binding_type = Properties.get_binding_type()
        data_def = binding_type.definition

        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30])
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', IntegerValue(10))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertRaises(CoreException, TypeConverter.convert_to_python,
                          data_val, binding_type, rest_converter_mode=None)

    def test_struct_with_extra_fields(self):
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10])
        py_val._set_extra_fields(extra_fields={
            'extra_str_val': StringValue('extra')})
        binding_type = Properties.get_binding_type()
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = binding_type.definition.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        data_val.set_field('list_val', list_val)
        data_val.set_field('extra_str_val', StringValue('extra'))
        self.assertEqual(data_valc, data_val)
        py_valc = TypeConverter.convert_to_python(data_valc, binding_type)
        self.assertEqual(py_val, py_valc)
        self.assertEqual(py_valc.get_struct_value(), data_val)

    def test_nested_struct_with_extra_fields(self):
        py_prop_val = Properties(int_val=10,
                                 str_val='testing',
                                 bool_val=True,
                                 opt_val=10,
                                 list_val=[10])
        py_prop_val._set_extra_fields(extra_fields={
            'nested_extra_str_val': StringValue('nested_extra')})
        py_val = OuterStructure(struct_val=py_prop_val)
        py_val._set_extra_fields(extra_fields={
            'extra_str_val': StringValue('outer_extra')})
        binding_type = OuterStructure.get_binding_type()
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        prop_val = Properties.get_binding_type().definition.new_value()
        prop_val.set_field('int_val', IntegerValue(10))
        prop_val.set_field('str_val', StringValue('testing'))
        prop_val.set_field('bool_val', BooleanValue(True))
        prop_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        prop_val.set_field('list_val', list_val)
        prop_val.set_field('nested_extra_str_val', StringValue('nested_extra'))
        data_val = binding_type.definition.new_value()
        data_val.set_field('struct_val', prop_val)
        data_val.set_field('extra_str_val', StringValue('outer_extra'))
        self.assertEqual(data_valc, data_val)
        py_valc = TypeConverter.convert_to_python(data_valc, binding_type)
        self.assertEqual(py_val, py_valc)
        self.assertEqual(py_valc.get_struct_value(), data_val)

    def test_struct_with_field_with_different_canonical_name(self):
        py_val = StructureHavingFieldWithDifferentCanonicalName(size_mib=10, def_='HELLO')
        binding_type = StructureHavingFieldWithDifferentCanonicalName.get_binding_type()
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = binding_type.definition.new_value()
        data_val.set_field('size_MiB', IntegerValue(10))
        data_val.set_field('_def', StringValue('HELLO'))
        self.assertEqual(data_valc, data_val)
        py_valc = TypeConverter.convert_to_python(data_valc, binding_type)
        self.assertEqual(py_val, py_valc)
        self.assertEqual(py_valc.get_struct_value(), data_val)

    def test_dict(self):
        fields = {'int_val': IntegerType(),
                  'str_val': StringType(),
                  'bool_val': BooleanType(),
                  'opt_val': OptionalType(IntegerType()),
                  'list_val': ListType(IntegerType()),
                 }
        binding_type = StructType('Properties', fields)
        data_def = binding_type.definition
        py_val = {'int_val': 10, 'str_val': 'testing', 'bool_val': True,
                  'opt_val': 10, 'list_val': [10, 20, 30]}
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(data_valc, data_val)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_valc, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

    def test_dict_for_struct_with_different_canonical_pep_names(self):
        binding_type = StructureHavingFieldWithDifferentCanonicalName.get_binding_type()
        data_def = binding_type.definition
        py_val = {'size_mib': 10, 'def_': 'testing'}
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        expected_data_val = data_def.new_value()
        expected_data_val.set_field('size_MiB', IntegerValue(10))
        expected_data_val.set_field('_def', StringValue('testing'))
        self.assertEqual(data_valc, expected_data_val)
        expected_py_val = StructureHavingFieldWithDifferentCanonicalName(
            size_mib=10, def_='testing')
        for rest_converter_mode in [
                None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(
                data_valc, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(expected_py_val, py_valc)

    def test_dict_for_struct_with_different_canonical_pep_names_invalid(self):
        binding_type = StructureHavingFieldWithDifferentCanonicalName.get_binding_type()
        data_def = binding_type.definition
        py_val = {'size_MiB': 10, 'def_': 'testing'}
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

    def test_invalid_value_type(self):
        binding_type = StructType('Properties', {})
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          10, binding_type)

    def test_invalid_struct_class(self):
        py_val = CopyOfProperties(int_val=10,
                                  str_val='testing',
                                  bool_val=True,
                                  opt_val=10,
                                  list_val=[10, 20, 30])
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, Properties.get_binding_type())

    def test_invalid_struct_field(self):
        fields = {'int_val': IntegerType(),
                  'str_val': StringType(),
                  'bool_val': BooleanType(),
                  'opt_val': OptionalType(IntegerType()),
                  'list_val': ListType(IntegerType()),
                 }
        binding_type = StructType('Properties', fields)
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10)
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

        py_val = {'int_val': 10, 'str_val': 'testing', 'bool_val': True,
                  'opt_val': 10}
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

    class TestEnum(Enum):
        """
        """
        def __init__(self, s=''):
            Enum.__init__(s)

    TestEnum.ONE = TestEnum('ONE')
    TestEnum.TWO = TestEnum('TWO')
    TestEnum.THREE = TestEnum('THREE')
    TestEnum._set_binding_type(EnumType(
        'test_enum',
        TestEnum))

    def test_enum(self):
        binding_type = TestBindingTypeConverter.TestEnum.get_binding_type()
        data_def = binding_type.definition
        py_val = TestBindingTypeConverter.TestEnum.ONE
        enum_value_str = 'ONE'
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value(enum_value_str)
        self.assertEqual(data_val, data_valc)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

    def test_enum_with_string_value(self):
        binding_type = TestBindingTypeConverter.TestEnum.get_binding_type()
        data_def = binding_type.definition
        py_val = TestBindingTypeConverter.TestEnum.ONE
        enum_value_str = 'ONE'
        data_valc = TypeConverter.convert_to_vapi(enum_value_str, binding_type)
        data_val = data_def.new_value(enum_value_str)
        self.assertEqual(data_val, data_valc)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

    def test_enum_with_unicode_value(self):
        binding_type = TestBindingTypeConverter.TestEnum.get_binding_type()
        data_def = binding_type.definition
        py_val = TestBindingTypeConverter.TestEnum.ONE
        enum_value_str = u'ONE'
        data_valc = TypeConverter.convert_to_vapi(enum_value_str, binding_type)
        data_val = data_def.new_value(enum_value_str)
        self.assertEqual(data_val, data_valc)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)


    def test_enum_future(self):
        # In enums, a user can add new enum values in later versions.
        # We want to provide the ability for old clients to use enum
        # values from the later version of the API, so even if they pass
        # an enum value which is not known, we should not complain and pass
        # it to the server as server might be a newer version and have that
        # enum value
        binding_type = TestBindingTypeConverter.TestEnum.get_binding_type()
        data_def = binding_type.definition
        py_val = TestBindingTypeConverter.TestEnum('FOUR')
        enum_value_str = 'FOUR'

        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value(enum_value_str)
        self.assertEqual(data_val, data_valc)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

        data_valc = TypeConverter.convert_to_vapi(enum_value_str, binding_type)
        data_val = data_def.new_value(enum_value_str)
        self.assertEqual(data_val, data_valc)
        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                      rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_valc)

    class AnotherTestEnum(Enum):
        """
        """
        def __init__(self, s=''):
            Enum.__init__(s)

    AnotherTestEnum.ONE = AnotherTestEnum('ONE')
    AnotherTestEnum._set_binding_type(EnumType(
        'another_test_enum',
        TestEnum))

    def test_invalid_enum_type(self):
        binding_type = TestBindingTypeConverter.TestEnum.get_binding_type()
        py_val = TestBindingTypeConverter.AnotherTestEnum.ONE
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

    def test_set_with_primitive(self):
        binding_type = SetType(StringType())
        data_def = binding_type.definition
        py_val = set(['a', 'b', 'c'])

        data_val_actual = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val_expected = data_def.new_value(
            [StringValue('a'),
             StringValue('b'),
             StringValue('c')])
        self.assertEqual(len(data_val_actual), len(data_val_expected))
        for element in data_val_actual:
            self.assertTrue(element in data_val_expected)

        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(len(py_val_actual), len(py_val))
            for element in py_val_actual:
                self.assertTrue(element in py_val)

    def test_set_with_enum(self):
        binding_type = SetType(TestBindingTypeConverter.TestEnum.get_binding_type())
        data_def = binding_type.definition
        py_val = set([TestBindingTypeConverter.TestEnum.ONE,
                      TestBindingTypeConverter.TestEnum.THREE,
                      TestBindingTypeConverter.TestEnum.TWO])

        data_val_actual = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val_expected = data_def.new_value(['ONE', 'TWO', 'THREE'])
        for value in data_val_expected:
            self.assertTrue(value in py_val)

        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_val_actual)

    def test_set_with_enum2(self):
        binding_type = SetType(TestBindingTypeConverter.TestEnum.get_binding_type())
        data_def = binding_type.definition
        py_val = set([TestBindingTypeConverter.TestEnum.ONE,
                      TestBindingTypeConverter.TestEnum.ONE,
                      TestBindingTypeConverter.TestEnum.TWO])

        data_val_actual = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val_expected = data_def.new_value(
            [StringValue('ONE'), StringValue('TWO')])
        self.assertEqual(len(data_val_actual), 2)
        for value in data_val_actual:
            self.assertTrue(value in data_val_expected)

        for rest_converter_mode in [None, RestConverter.VAPI_REST, RestConverter.SWAGGER_REST]:
            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_val_actual)

    def test_map(self):
        binding_type = MapType(StringType(), StringType())
        data_def = binding_type.definition
        py_val = {'a': 'a', 'b': 'b'}
        for rest_converter_mode in [None, RestConverter.VAPI_REST]:
            data_val_actual = TypeConverter.convert_to_vapi(
                py_val, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(len(data_val_actual), 2)

            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_val_actual)

    def test_map_with_enum_keys(self):
        binding_type = MapType(
            TestBindingTypeConverter.TestEnum.get_binding_type(),
            StringType())
        data_def = binding_type.definition
        py_val = {TestBindingTypeConverter.TestEnum.ONE: 'a',
                  TestBindingTypeConverter.TestEnum.TWO: 'b'}
        element_val1 = data_def.element_type.new_value()
        element_val1.set_field('key', StringValue('ONE'))
        element_val1.set_field('value', StringValue('a'))
        element_val2 = data_def.element_type.new_value()
        element_val2.set_field('key', StringValue('TWO'))
        element_val2.set_field('value', StringValue('b'))
        for rest_converter_mode in [None, RestConverter.VAPI_REST]:
            data_val_actual = TypeConverter.convert_to_vapi(
                py_val, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(len(data_val_actual), 2)

            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_val_actual)

    def test_map_with_enum_keys_2(self):
        binding_type = MapType(
            TestBindingTypeConverter.TestEnum.get_binding_type(),
            StringType())
        data_def = binding_type.definition
        py_val = {TestBindingTypeConverter.TestEnum.ONE: 'a',
                  TestBindingTypeConverter.TestEnum.ONE: 'b'}
        element_val1 = data_def.element_type.new_value()
        element_val1.set_field('key', StringValue('ONE'))
        element_val1.set_field('value', StringValue('b'))
        for rest_converter_mode in [None, RestConverter.VAPI_REST]:
            data_val_actual = TypeConverter.convert_to_vapi(
                py_val, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(len(data_val_actual), 1)

            py_val_actual = TypeConverter.convert_to_python(
                data_val_actual, binding_type, rest_converter_mode=rest_converter_mode)
            self.assertEqual(py_val, py_val_actual)

    def test_reference(self):
        PropertiesReferenceType = Properties.get_binding_type()
        # Using reference type to convert from python native value to data value
        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30])
        actual_data_val = TypeConverter.convert_to_vapi(py_val,
                                                        PropertiesReferenceType)

        data_def = PropertiesReferenceType.definition
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(actual_data_val, data_val)

        # Using reference type to convert from data value to python native value
        actual_py_val = TypeConverter.convert_to_python(actual_data_val,
                                                  PropertiesReferenceType)
        self.assertEqual(py_val, actual_py_val)


class TestVapiRestBindingTypeConverter(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_structure_with_missing_optional_value_wrappers(self):
        binding_type = Properties.get_binding_type()
        data_def = binding_type.definition

        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30])
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', IntegerValue(10))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                  rest_converter_mode=RestConverter.VAPI_REST)
        self.assertEqual(py_val, py_valc)

    def test_blob(self):
        # Blob Conversion
        byte_str = b'test'
        data_def = BlobType()
        data_val = TypeConverter.convert_to_vapi(
            byte_str, data_def, RestConverter.VAPI_REST)
        self.assertEqual(data_val, BlobValue(byte_str))
        unicode_str = base64.b64encode(byte_str).decode('utf-8')
        data_val = StringValue(unicode_str)
        py_val = TypeConverter.convert_to_python(
            data_val, data_def, rest_converter_mode=RestConverter.VAPI_REST)
        self.assertEqual(py_val, byte_str)


class TestSwaggerRestBindingTypeConverter(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_structure_with_missing_optional_value_wrappers(self):
        binding_type = Properties.get_binding_type()
        data_def = binding_type.definition

        py_val = Properties(int_val=10,
                            str_val='testing',
                            bool_val=True,
                            opt_val=10,
                            list_val=[10, 20, 30])
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', IntegerValue(10))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        py_valc = TypeConverter.convert_to_python(data_val, binding_type,
                                                  rest_converter_mode=RestConverter.SWAGGER_REST)
        self.assertEqual(py_val, py_valc)

    def test_map(self):
        binding_type = MapType(StringType(), StringType())
        data_def = binding_type.definition
        py_val = {'a': 'a', 'b': 'b'}
        data_val_actual = TypeConverter.convert_to_vapi(py_val, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        data_val = StructValue('map-struct')
        data_val.set_field('a', StringValue('a'))
        data_val.set_field('b', StringValue('b'))
        self.assertEqual(data_val, data_val_actual)

        py_val_actual = TypeConverter.convert_to_python(
            data_val_actual, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        self.assertEqual(py_val, py_val_actual)

    def test_map_with_enum_keys(self):
        binding_type = MapType(
            TestBindingTypeConverter.TestEnum.get_binding_type(),
            StringType())
        data_def = binding_type.definition
        py_val = {TestBindingTypeConverter.TestEnum.ONE: 'a',
                  TestBindingTypeConverter.TestEnum.TWO: 'b'}
        data_val_actual = TypeConverter.convert_to_vapi(
            py_val, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        data_val = StructValue('map-struct')
        data_val.set_field(TestBindingTypeConverter.TestEnum.ONE, StringValue('a'))
        data_val.set_field(TestBindingTypeConverter.TestEnum.TWO, StringValue('b'))
        self.assertEqual(data_val, data_val_actual)

        py_val_actual = TypeConverter.convert_to_python(
            data_val_actual, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        self.assertEqual(py_val, py_val_actual)

    def test_map_with_enum_keys_2(self):
        binding_type = MapType(
            TestBindingTypeConverter.TestEnum.get_binding_type(),
            StringType())
        data_def = binding_type.definition
        py_val = {TestBindingTypeConverter.TestEnum.ONE: 'a',
                  TestBindingTypeConverter.TestEnum.ONE: 'b'}
        data_val_actual = TypeConverter.convert_to_vapi(
            py_val, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        data_val = StructValue('map-struct')
        data_val.set_field(TestBindingTypeConverter.TestEnum.ONE, StringValue('b'))
        self.assertEqual(data_val, data_val_actual)

        py_val_actual = TypeConverter.convert_to_python(
            data_val_actual, binding_type, rest_converter_mode=RestConverter.SWAGGER_REST)
        self.assertEqual(py_val, py_val_actual)

    def test_blob(self):
        # Blob Conversion
        byte_str = b'test'
        data_def = BlobType()
        data_val = TypeConverter.convert_to_vapi(
            byte_str, data_def, RestConverter.SWAGGER_REST)
        self.assertEqual(data_val, BlobValue(byte_str))
        unicode_str = base64.b64encode(byte_str).decode('utf-8')
        data_val = StringValue(unicode_str)
        py_val = TypeConverter.convert_to_python(
            data_val, data_def, rest_converter_mode=RestConverter.SWAGGER_REST)
        self.assertEqual(py_val, byte_str)


class TestBindingErrorConverter(unittest.TestCase):
    _msg_binding = LocalizableMessage('msg.id.test', 'test message', [])
    _timed_out_def = make_std_error_def('com.vmware.vapi.std.errors.timed_out')
    _std_error_def = make_std_error_def('com.vmware.vapi.std.errors.error')
    _not_found_def = make_std_error_def('com.vmware.vapi.std.errors.not_found')
    _timed_out_value = make_error_value_from_msg_id(
        _timed_out_def, 'vapi.connection', 'localhost')
    _std_error_value = make_error_value_from_msg_id(
        _std_error_def, 'vapi.connection', 'localhost')
    _not_found_value = make_error_value_from_msg_id(
        _not_found_def, 'vapi.connection', 'localhost')
    _timed_out_binding = TimedOut(
            messages=[LocalizableMessage(
                id='vapi.connection',
                default_message='Could not connect to localhost',
                args=['localhost'])])
    _std_error_binding = Error(
            messages=[LocalizableMessage(
                id='vapi.connection',
                default_message='Could not connect to localhost',
                args=['localhost'])])
    _resolver = NameToTypeResolver(
        {'com.vmware.vapi.std.errors.timed_out': TimedOut.get_binding_type(),
         'com.vmware.vapi.std.errors.error': Error.get_binding_type()})

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    class Error(VapiError):
        _canonical_to_pep_names = {
            'strVal' : 'str_val',
            'boolVal' : 'bool_val',
            'intVal' : 'int_val',
            'optVal' : 'opt_val',
            'listVal' : 'list_val'
        }
        def __init__(self, int_val=None, str_val=None, bool_val=None,
                     opt_val=None, list_val=None):
            self.int_val = int_val
            self.str_val = str_val
            self.bool_val = bool_val
            self.opt_val = opt_val
            self.list_val = list_val
            VapiError.__init__(self)

    Error._set_binding_type(
        ErrorType('Error',
                  {'int_val': IntegerType(),
                   'str_val': StringType(),
                   'bool_val': BooleanType(),
                   'opt_val': OptionalType(IntegerType()),
                   'list_val': ListType(IntegerType()),
                  },
                  Error))

    def test_error(self):
        binding_type = TestBindingErrorConverter.Error.get_binding_type()
        data_def = binding_type.definition

        py_val = TestBindingErrorConverter.Error(10, 'testing', True,
                                                     10, [10, 20, 30])
        data_valc = TypeConverter.convert_to_vapi(py_val, binding_type)
        data_val = data_def.new_value()
        data_val.set_field('int_val', IntegerValue(10))
        data_val.set_field('str_val', StringValue('testing'))
        data_val.set_field('bool_val', BooleanValue(True))
        data_val.set_field('opt_val', OptionalValue(value=IntegerValue(10)))
        list_val = ListValue()
        list_val.add(IntegerValue(10))
        list_val.add(IntegerValue(20))
        list_val.add(IntegerValue(30))
        data_val.set_field('list_val', list_val)
        self.assertEqual(data_valc, data_val)
        py_valc = TypeConverter.convert_to_python(data_valc, binding_type)
        self.assertEqual(py_val, py_valc)

    def test_invalid_error_class(self):
        binding_type = ErrorType('Error', {})
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          10, binding_type)


    def test_invalid_error_field(self):
        fields = {'int_val': IntegerType(),
                  'str_val': StringType(),
                  'bool_val': BooleanType(),
                  'opt_val': OptionalType(IntegerType()),
                  'list_val': ListType(IntegerType()),
                 }
        binding_type = ErrorType('Error', fields)
        py_val = TestBindingErrorConverter.Error(10, 'testing', True,
                                                     10)
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

        py_val = {'int_val': 10, 'str_val': 'testing', 'bool_val': True,
                  'opt_val': 10}
        self.assertRaises(CoreException,
                          TypeConverter.convert_to_vapi,
                          py_val, binding_type)

    #
    # AnyError tests
    #

    def test_any_error(self):
        binding_type = AnyErrorType()
        actual_value = TypeConverter.convert_to_python(
            self._timed_out_value, binding_type, self._resolver)
        self.assertEqual(self._timed_out_binding, actual_value)

    def test_std_base_error_to_binding(self):
        binding_type = AnyErrorType()
        actual_value = TypeConverter.convert_to_python(
            self._std_error_value, binding_type, self._resolver)
        self.assertEqual(self._std_error_binding, actual_value)

    def test_unresolved_error_binding(self):
        binding_type = AnyErrorType()
        actual_value = TypeConverter.convert_to_python(
            self._not_found_value, binding_type, self._resolver)
        self.assertEqual(UnresolvedError(self._not_found_value),
                         actual_value)

    def test_unresolved_error_to_value(self):
        actual_value = TypeConverter.convert_to_vapi(
            UnresolvedError(error_value=self._timed_out_value), AnyErrorType())
        expected_value = self._timed_out_value
        self.assertEqual(expected_value, actual_value)

    def test_std_error_to_value(self):
        actual_value = TypeConverter.convert_to_vapi(
            self._timed_out_binding, AnyErrorType())
        expected_value = self._timed_out_value
        self.assertEqual(expected_value, actual_value)

    def test_std_base_error_to_value(self):
        actual_value = TypeConverter.convert_to_vapi(
            self._std_error_binding, AnyErrorType())
        expected_value = self._std_error_value
        self.assertEqual(expected_value, actual_value)

    def custom_error_to_binding(self):
        py_val = TestBindingErrorConverter.Error(10, 'testing', True, 10, [10,20])
        data_val_actual = TypeConverter.convert_to_vapi(py_val, AnyErrorType())
        data_val_expected = py_val.get_error_value()
        self.assertEqual(data_val_actual, data_val_expected)
        py_val_actual = TypeConverter.convert_to_python(data_val_expected,
                                                        AnyErrorType())
        py_val_expected = VapiError(data_val_expected)
        self.assertEqual(py_val_actual, py_val_expected)


if __name__ == '__main__':
   unittest.main()
