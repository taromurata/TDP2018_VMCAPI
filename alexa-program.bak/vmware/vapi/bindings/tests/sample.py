"""
Sample type used for testing ReferenceType
"""

from vmware.vapi.bindings.type import StructType, StringType

sample_type = StructType('test', {'echo': StringType()})
