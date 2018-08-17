#!/usr/bin/env python

"""
Unit tests for the data validators
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import sys

from vmware.vapi.bindings.common import raise_core_exception
from vmware.vapi.bindings.type import *
from vmware.vapi.bindings.struct import VapiStruct
from vmware.vapi.data.validator import *
from vmware.vapi.data.value import *
from vmware.vapi.exception import CoreException

class NestedProperties(VapiStruct):
    def __init__(self, int_val=None):
        self.int_val = int_val
        VapiStruct.__init__(self)

NestedProperties._set_binding_type(StructType(
    'nested_properties', {
        'int_val': IntegerType(),
    }, NestedProperties))

class Properties(VapiStruct):
    def __init__(self, int_val=None, str_val=None, bool_val=None,
                 opt_int_val=None, list_val=None, nested_val=None):
        self.int_val = int_val
        self.str_val = str_val
        self.bool_val = bool_val
        self.opt_int_val = opt_int_val
        self.list_val = list_val
        self.nested_val = nested_val
        VapiStruct.__init__(self)

Properties._set_binding_type(StructType(
    'properties', {
        'int_val': IntegerType(),
        'str_val': StringType(),
        'bool_val': BooleanType(),
        'opt_int_val': OptionalType(IntegerType()),
        'list_val': ListType(IntegerType()),
        'nested_val': ReferenceType(__name__, 'NestedProperties')
    }, Properties))

dynamic_struct_binding_type = DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [ReferenceType(__name__, 'Properties')])

class NestedProperties2(VapiStruct):
    def __init__(self, int_val=None):
        self.int_val = int_val
        VapiStruct.__init__(self)

NestedProperties2._set_binding_type(StructType(
    'nested_properties2', {
        'opt_int_val': OptionalType(IntegerType()),
    }, NestedProperties2))

class Properties2(VapiStruct):
    def __init__(self, int_val=None, str_val=None, bool_val=None,
                 opt_int_val=None, list_val=None, nested_val=None):
        self.list_val = list_val
        self.nested_val = nested_val
        VapiStruct.__init__(self)

Properties2._set_binding_type(StructType(
    'properties2', {
        'list_val': ListType(OptionalType(IntegerType())),
        'nested_val': ReferenceType(__name__, 'NestedProperties2')
    }, Properties2))

dynamic_struct_binding_type2 = DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct, [ReferenceType(__name__, 'Properties2')])

class TestHasFieldsOfValidator(unittest.TestCase):
    def setUp(self):
        self.has_fields_of_validator = HasFieldsOfValidator()

    def test_has_fields_of_positive1(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=11,
                          list_val=[10],
                          nested_val=NestedProperties(int_val=100)
                          )
        msg_list = self.has_fields_of_validator.validate(prop.get_struct_value(), dynamic_struct_binding_type)
        raise_core_exception(msg_list)

    def test_has_fields_of_positive2(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=11,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        msg_list = self.has_fields_of_validator.validate(prop.get_struct_value(), dynamic_struct_binding_type)
        raise_core_exception(msg_list)

    def test_has_fields_of_positive3(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=None,
                          list_val=[10],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k not in ['opt_int_val']:
                values[k] = v
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        raise_core_exception(msg_list)

    def test_has_fields_of_negative1(self):
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values={}), dynamic_struct_binding_type)
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_has_fields_of_negative2(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=None,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k not in ['str_val']:
                values[k] = v
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_has_fields_of_negative3(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=None,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k not in ['nested_val']:
                values[k] = v
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_has_fields_of_negative4(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=None,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k != 'nested_val':
                values[k] = v
            else:
                values[k] = StructValue(name='NestedProperties', values={})
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        self.assertRaises(CoreException, raise_core_exception, msg_list)

class TestHasFieldsOfValidatorWithCleanJSONDataValue(unittest.TestCase):
    def setUp(self):
        self.has_fields_of_validator = HasFieldsOfValidator()

    def test_has_fields_of_positive1(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=11,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k == 'opt_int_val':
                values[k] = v.value
            else:
                values[k] = v
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        raise_core_exception(msg_list)

    def test_has_fields_of_positive2(self):
        prop = Properties(int_val=10,
                          str_val='STRING_PROP',
                          bool_val=True,
                          opt_int_val=11,
                          list_val=[],
                          nested_val=NestedProperties(int_val=100)
                          )
        values = {}
        for k,v in prop.get_struct_value().get_fields():
            if k != 'opt_int_val':
                values[k] = v
        msg_list = self.has_fields_of_validator.validate(StructValue(name='Properties', values=values), dynamic_struct_binding_type)
        raise_core_exception(msg_list)

    def test_has_fields_of_positive3(self):
        struct_value = StructValue(
            name='Properties2',
            values={
                'list_val': ListValue(),
                'nested_val': StructValue('NestedProperties2')
                })
        msg_list = self.has_fields_of_validator.validate(struct_value, dynamic_struct_binding_type2)
        raise_core_exception(msg_list)

    def test_has_fields_of_positive4(self):
        struct_value = StructValue(
            name='Properties2',
            values={
                'list_val': ListValue([IntegerValue(10), IntegerValue(20)]),
                'nested_val': StructValue('NestedProperties2', values={
                    'opt_int_val': IntegerValue(10)
                    })
                })
        msg_list = self.has_fields_of_validator.validate(struct_value, dynamic_struct_binding_type2)
        raise_core_exception(msg_list)

class TestUnionValidator(unittest.TestCase):
    def test_union_validator_positive1(self):
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': OptionalValue(IntegerValue(100))
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'long_val': OptionalValue()
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative1(self):
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'string_val': OptionalValue(StringValue('STRING_VAL'))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'string_val': OptionalValue(StringValue('STRING_VAL'))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_union_validator_positive2(self):
        # Test Optional union tags
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(StringValue('LONG')),
                            'long_val': OptionalValue(IntegerValue(100))
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(StringValue('NONE')),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(),
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative2(self):
        # Test Optional union tags
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(StringValue('LONG')),
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(StringValue('NONE')),
                            'long_val': OptionalValue(IntegerValue(100))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': OptionalValue(),
                            'long_val': OptionalValue(IntegerValue(100))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_union_validator_positive3(self):
        # Test Optional union cases
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True), ('opt_long_val', False)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': OptionalValue(IntegerValue(100)),
                            'opt_long_val': OptionalValue(IntegerValue(120))
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': OptionalValue(IntegerValue(100)),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative3(self):
        # Test Optional union cases
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True), ('opt_long_val', False)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'opt_long_val': OptionalValue(IntegerValue(120))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('STRING'),
                            'opt_long_val': OptionalValue(IntegerValue(120))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'opt_long_val': OptionalValue(IntegerValue(120))
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)


class TestUnionValidatorForCleanJSONDataValue(unittest.TestCase):
    def test_union_validator_positive1(self):
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': IntegerValue(100)
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative1(self):
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'string_val': StringValue('STRING_VAL')
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'string_val': StringValue('STRING_VAL')
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_union_validator_positive2(self):
        # Test Optional union tags
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': IntegerValue(100)
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative2(self):
        # Test Optional union tags
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'long_val': IntegerValue(100)
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'long_val': IntegerValue(100)
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)

    def test_union_validator_positive3(self):
        # Test Optional union cases
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True), ('opt_long_val', False)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': IntegerValue(100),
                            'opt_long_val': IntegerValue(120)
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'long_val': IntegerValue(100),
                        }))
        raise_core_exception(msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                        }))
        raise_core_exception(msg_list)

    def test_union_validator_negative3(self):
        # Test Optional union cases
        union_validator = UnionValidator('test_enum',
                                         {
                                             'LONG' : [('long_val', True), ('opt_long_val', False)],
                                             'STRING' : [('string_val', True)],
                                             'NONE' : [],
                                         }
                                        )
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('LONG'),
                            'opt_long_val': IntegerValue(120)
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('STRING'),
                            'opt_long_val': IntegerValue(120)
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)
        msg_list = union_validator.validate(
            StructValue(name='TestStruct',
                        values={
                            'test_enum': StringValue('NONE'),
                            'opt_long_val': IntegerValue(120)
                        }))
        self.assertRaises(CoreException, raise_core_exception, msg_list)

class TestValidator(unittest.TestCase):
    def test_abstract_validator(self):
        self.assertRaises(TypeError, Validator)

if __name__ == "__main__":
    unittest.main()
