"""
Unit tests for Introspection data conversion
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest

from vmware.vapi.data.definition import (
    IntegerDefinition, DoubleDefinition, BooleanDefinition, StringDefinition,
    BlobDefinition, ListDefinition, StructDefinition, OptionalDefinition,
    VoidDefinition, OpaqueDefinition, SecretDefinition, ErrorDefinition,
    StructRefDefinition, DynamicStructDefinition, AnyErrorDefinition
)
from vmware.vapi.data.value import (
    StructValue, StringValue, OptionalValue, ListValue)
from vmware.vapi.data.serializers.introspection import (
    convert_data_def_to_data_value, convert_data_value_to_data_def)
from vmware.vapi.lib.constants import (Introspection, MAP_ENTRY)


class IntrospectionConversion(unittest.TestCase):

    def generate_primitive_value(self, typ):
        output = StructValue(Introspection.DATA_DEFINITION)
        output.set_field('type', StringValue(typ))
        output.set_field('fields', OptionalValue())
        output.set_field('name', OptionalValue())
        output.set_field('element_definition', OptionalValue())
        return output

    # Convert from data definition to Introspection VMODL2 type
    def test_primitive_def_to_value(self):
        for typ_def_class, typ in [(VoidDefinition, 'VOID'),
                                   (IntegerDefinition, 'LONG'),
                                   (DoubleDefinition, 'DOUBLE'),
                                   (BooleanDefinition, 'BOOLEAN'),
                                   (StringDefinition, 'STRING'),
                                   (BlobDefinition, 'BINARY'),
                                   (OpaqueDefinition, 'OPAQUE'),
                                   (SecretDefinition, 'SECRET'),
                                   (DynamicStructDefinition, 'DYNAMIC_STRUCTURE'),
                                   (AnyErrorDefinition, 'ANY_ERROR')]:
            actual_output = convert_data_def_to_data_value(typ_def_class())
            expected_output = self.generate_primitive_value(typ)
            self.assertEqual(actual_output, expected_output)

    def test_generic_def_to_value(self):
        for typ_def, typ in [(OptionalDefinition, 'OPTIONAL'),
                             (ListDefinition, 'LIST')]:
            typ_def = typ_def(StringDefinition())
            actual_output = convert_data_def_to_data_value(typ_def)
            expected_output = StructValue(Introspection.DATA_DEFINITION)
            element_value = self.generate_primitive_value('STRING')
            expected_output.set_field('type', StringValue(typ))
            expected_output.set_field('fields', OptionalValue())
            expected_output.set_field('name', OptionalValue())
            expected_output.set_field('element_definition',
                                      OptionalValue(element_value))
            self.assertEqual(actual_output, expected_output)

    def test_struct_ref_to_value(self):
        actual_output = convert_data_def_to_data_value(
            StructRefDefinition('mock'))
        expected_output = StructValue(Introspection.DATA_DEFINITION)
        expected_output.set_field('type',
                                  StringValue('STRUCTURE_REF'))
        expected_output.set_field('fields', OptionalValue())
        expected_output.set_field('name', OptionalValue(StringValue('mock')))
        expected_output.set_field('element_definition', OptionalValue())
        self.assertEqual(actual_output, expected_output)

    def test_struct_to_value(self):
        struct_def = StructDefinition('mock', [('field1', StringDefinition())])
        actual_output = convert_data_def_to_data_value(struct_def)
        expected_output = StructValue(Introspection.DATA_DEFINITION)
        expected_output.set_field('type', StringValue('STRUCTURE'))
        expected_output.set_field('name', OptionalValue(StringValue('mock')))
        expected_output.set_field('element_definition', OptionalValue())
        field_value = self.generate_primitive_value('STRING')
        field_entry = StructValue(MAP_ENTRY)
        field_entry.set_field('key', StringValue('field1'))
        field_entry.set_field('value', field_value)
        field_values = ListValue()
        field_values.add(field_entry)
        expected_output.set_field('fields', OptionalValue(field_values))
        self.assertEqual(actual_output, expected_output)

    def test_error_to_value(self):
        struct_def = ErrorDefinition('mock', [('field1', StringDefinition())])
        actual_output = convert_data_def_to_data_value(struct_def)
        expected_output = StructValue(Introspection.DATA_DEFINITION)
        expected_output.set_field('type', StringValue('ERROR'))
        expected_output.set_field('name', OptionalValue(StringValue('mock')))
        expected_output.set_field('element_definition', OptionalValue())
        field_value = self.generate_primitive_value('STRING')
        field_entry = StructValue(MAP_ENTRY)
        field_entry.set_field('key', StringValue('field1'))
        field_entry.set_field('value', field_value)
        field_values = ListValue()
        field_values.add(field_entry)
        expected_output.set_field('fields', OptionalValue(field_values))
        self.assertEqual(actual_output, expected_output)

    # Convert from Introspection VMODL2 type to data definition
    def test_value_to_primitive_def(self):
        for typ_def_class, typ in [(VoidDefinition, 'VOID'),
                                   (IntegerDefinition, 'LONG'),
                                   (DoubleDefinition, 'DOUBLE'),
                                   (BooleanDefinition, 'BOOLEAN'),
                                   (StringDefinition, 'STRING'),
                                   (BlobDefinition, 'BINARY'),
                                   (OpaqueDefinition, 'OPAQUE'),
                                   (SecretDefinition, 'SECRET'),
                                   (DynamicStructDefinition, 'DYNAMIC_STRUCTURE'),
                                   (AnyErrorDefinition, 'ANY_ERROR')]:
            data_value = self.generate_primitive_value(typ)
            actual_output = convert_data_value_to_data_def(data_value)
            expected_output = typ_def_class()
            self.assertEqual(actual_output, expected_output)

    def test_value_to_generic_def(self):
        for typ_def_class, typ in [(OptionalDefinition, 'OPTIONAL'),
                                   (ListDefinition, 'LIST')]:
            expected_output = typ_def_class(StringDefinition())
            element_value = self.generate_primitive_value('STRING')
            generic_value = StructValue(Introspection.DATA_DEFINITION)
            generic_value.set_field('type', StringValue(typ))
            generic_value.set_field('fields', OptionalValue())
            generic_value.set_field('name', OptionalValue())
            generic_value.set_field('element_definition',
                                    OptionalValue(element_value))
            actual_output = convert_data_value_to_data_def(generic_value)
            self.assertEqual(actual_output, expected_output)

    def test_value_to_struct(self):
        struct_value = StructValue(Introspection.DATA_DEFINITION)
        struct_value.set_field('type', StringValue('STRUCTURE'))
        struct_value.set_field('name', OptionalValue(StringValue('mock')))
        struct_value.set_field('element_definition', OptionalValue())
        field_value = self.generate_primitive_value('STRING')
        field_entry = StructValue(MAP_ENTRY)
        field_entry.set_field('key', StringValue('field1'))
        field_entry.set_field('value', field_value)
        field_values = ListValue()
        field_values.add(field_entry)
        struct_value.set_field('fields', OptionalValue(field_values))
        actual_output = convert_data_value_to_data_def(struct_value)
        expected_output = StructDefinition(
                'mock', [('field1', StringDefinition())])
        self.assertEqual(actual_output, expected_output)

    def test_value_to_struct_ref_def(self):
        struct_value = StructValue(Introspection.DATA_DEFINITION)
        struct_value.set_field('type', StringValue('STRUCTURE'))
        struct_value.set_field('name', OptionalValue(StringValue('mock')))
        struct_value.set_field('element_definition', OptionalValue())
        field_value = self.generate_primitive_value('STRUCTURE_REF')
        field_value.set_field('name', OptionalValue(StringValue('mock')))
        field_entry = StructValue(MAP_ENTRY)
        field_entry.set_field('key', StringValue('field1'))
        field_entry.set_field('value', field_value)
        field_values = ListValue()
        field_values.add(field_entry)
        struct_value.set_field('fields', OptionalValue(field_values))
        actual_output = convert_data_value_to_data_def(struct_value)
        expected_output = StructDefinition(
                'mock', [('field1', StructRefDefinition('mock'))])
        self.assertEqual(actual_output, expected_output)
        # Check the circular reference as well
        self.assertEqual(actual_output.get_field('field1').target, expected_output)

    def test_value_to_error(self):
        struct_value = StructValue(Introspection.DATA_DEFINITION)
        struct_value.set_field('type', StringValue('ERROR'))
        struct_value.set_field('name', OptionalValue(StringValue('mock')))
        struct_value.set_field('element_definition', OptionalValue())
        field_value = self.generate_primitive_value('STRING')
        field_entry = StructValue(MAP_ENTRY)
        field_entry.set_field('key', StringValue('field1'))
        field_entry.set_field('value', field_value)
        field_values = ListValue()
        field_values.add(field_entry)
        struct_value.set_field('fields', OptionalValue(field_values))
        actual_output = convert_data_value_to_data_def(struct_value)
        expected_output = ErrorDefinition(
                'mock', [('field1', StringDefinition())])
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

