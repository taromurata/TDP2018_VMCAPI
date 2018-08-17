"""
String Constants used in vAPI runtime
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015-2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


PARAMS = 'params'
SCHEME_ID = 'schemeId'
AUTHN_IDENTITY = 'authnIdentity'
EXECUTION_CONTEXT = 'ctx'
APPLICATION_CONTEXT = 'appCtx'
SECURITY_CONTEXT = 'securityCtx'
PROCESSORS = 'processors'
OPID = 'opId'
SHOW_UNRELEASED_APIS = '$showUnreleasedAPIs'
TASK_OPERATION = '$task'
TASK_ID = '$taskId'
TASK_REST_QUERY_PARAM = 'vmw-task'

# Magic structure names
# Structure name for the StructValues that represent
# map entries in the runtime
MAP_ENTRY = 'map-entry'
# Structure name for the StructValue that represent
# maps when using cleanjson
MAP_STRUCT = 'map-struct'
# Structure name for the StructValues that represent
# operation input in the runtime
OPERATION_INPUT = 'operation-input'

# Structure name for the StructValue that represent
# a dynamic structure in the absence of the the type name
DYNAMIC_STRUCTURE = 'dynamic-structure'

# Constants for REST presentation Layer
JSONRPC = 'jsonrpc'
JSON_CONTENT_TYPE = 'application/json'


class Introspection(object):
    """
    String constants used in introsection service
    """
    PACKAGE = 'com.vmware.vapi.std.introspection'

    # Services
    PROVIDER_SVC = 'com.vmware.vapi.std.introspection.provider'
    SERVICE_SVC = 'com.vmware.vapi.std.introspection.service'
    OPERATION_SVC = 'com.vmware.vapi.std.introspection.operation'

    # Types
    DATA_DEFINITION = \
        'com.vmware.vapi.std.introspection.operation.data_definition'


class RestAnnotations(object):
    """
    String constants used in REST annotations in VMODL definition
    """
    REQUEST_MAPPING = 'RequestMapping'
    PATH_VARIABLE = 'PathVariable'
    METHOD_ELEMENT = 'method'
    VALUE_ELEMENT = 'value'
    ACTION_PARAM = 'action'


class TaskType(object):
    """
    Task types
    """
    NONE = 0
    TASK = 1
    TASK_ONLY = 2
