# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.health.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.health_client`` module provides classes for
reporting the health of the various subsystems of the the appliance. The module
is available starting in vSphere 6.5.

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


class Applmgmt(VapiInterface):
    """
    ``Applmgmt`` class provides methods Get health status of applmgmt services.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ApplmgmtStub)


    def get(self):
        """
        Get health status of applmgmt services.


        :rtype: :class:`str`
        :return: health status
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Databasestorage(VapiInterface):
    """
    ``Databasestorage`` class provides methods Get database storage health.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DatabasestorageStub)

    class HealthLevel(Enum):
        """
        ``Databasestorage.HealthLevel`` class Defines service health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        The service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy but experiencing some problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.databasestorage.health_level',
        HealthLevel))



    def get(self):
        """
        Get database storage health.


        :rtype: :class:`Databasestorage.HealthLevel`
        :return: Database storage health
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Load(VapiInterface):
    """
    ``Load`` class provides methods Get load health.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _LoadStub)

    class HealthLevel(Enum):
        """
        ``Load.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.load.health_level',
        HealthLevel))



    def get(self):
        """
        Get load health.


        :rtype: :class:`Load.HealthLevel`
        :return: Load health.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Mem(VapiInterface):
    """
    ``Mem`` class provides methods Get memory health.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _MemStub)

    class HealthLevel(Enum):
        """
        ``Mem.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.mem.health_level',
        HealthLevel))



    def get(self):
        """
        Get memory health.


        :rtype: :class:`Mem.HealthLevel`
        :return: Memory health.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Softwarepackages(VapiInterface):
    """
    ``Softwarepackages`` class provides methods Get information on available
    software updates available in remote VUM repository.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SoftwarepackagesStub)

    class HealthLevel(Enum):
        """
        ``Softwarepackages.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.softwarepackages.health_level',
        HealthLevel))



    def get(self):
        """
        Get information on available software updates available in the remote
        vSphere Update Manager repository. Red indicates that security updates
        are available. Orange indicates that non-security updates are
        available. Green indicates that there are no updates available. Gray
        indicates that there was an error retreiving information on software
        updates.


        :rtype: :class:`Softwarepackages.HealthLevel`
        :return: software updates available.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Storage(VapiInterface):
    """
    ``Storage`` class provides methods Get storage health.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StorageStub)

    class HealthLevel(Enum):
        """
        ``Storage.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.storage.health_level',
        HealthLevel))



    def get(self):
        """
        Get storage health.


        :rtype: :class:`Storage.HealthLevel`
        :return: Storage health.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Swap(VapiInterface):
    """
    ``Swap`` class provides methods Get swap health.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SwapStub)

    class HealthLevel(Enum):
        """
        ``Swap.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.swap.health_level',
        HealthLevel))



    def get(self):
        """
        Get swap health.


        :rtype: :class:`Swap.HealthLevel`
        :return: Swap health
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class System(VapiInterface):
    """
    ``System`` class provides methods Get overall health of the system.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SystemStub)

    class HealthLevel(Enum):
        """
        ``System.HealthLevel`` class Defines health levels.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        orange = None
        """
        The service health is degraded. The service might have serious problems.

        """
        gray = None
        """
        No health data is available for this service.

        """
        green = None
        """
        Service is healthy.

        """
        red = None
        """
        The service is unavaiable, not functioning properly, or will stop
        functioning soon.

        """
        yellow = None
        """
        The service is healthy state, but experiencing some levels of problems.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`HealthLevel` instance.
            """
            Enum.__init__(string)

    HealthLevel._set_values([
        HealthLevel('orange'),
        HealthLevel('gray'),
        HealthLevel('green'),
        HealthLevel('red'),
        HealthLevel('yellow'),
    ])
    HealthLevel._set_binding_type(type.EnumType(
        'com.vmware.appliance.health.system.health_level',
        HealthLevel))



    def lastcheck(self):
        """
        Get last check timestamp of the health of the system.


        :rtype: :class:`datetime.datetime`
        :return: System health last check timestamp
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('lastcheck', None)

    def get(self):
        """
        Get overall health of system.


        :rtype: :class:`System.HealthLevel`
        :return: System health
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class _ApplmgmtStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/applmgmt',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.StringType(),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.applmgmt',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _DatabasestorageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/database-storage',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Databasestorage.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.databasestorage',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _LoadStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/load',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Load.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.load',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _MemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/mem',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Mem.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.mem',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SoftwarepackagesStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/software-packages',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Softwarepackages.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.softwarepackages',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _StorageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/storage',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Storage.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.storage',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SwapStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/swap',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Swap.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.swap',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SystemStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for lastcheck operation
        lastcheck_input_type = type.StructType('operation-input', {})
        lastcheck_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        lastcheck_input_value_validator_list = [
        ]
        lastcheck_output_validator_list = [
        ]
        lastcheck_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/system/lastcheck',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for get operation
        get_input_type = type.StructType('operation-input', {})
        get_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/health/system',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'lastcheck': {
                'input_type': lastcheck_input_type,
                'output_type': type.DateTimeType(),
                'errors': lastcheck_error_dict,
                'input_value_validator_list': lastcheck_input_value_validator_list,
                'output_validator_list': lastcheck_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'System.HealthLevel'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'lastcheck': lastcheck_rest_metadata,
            'get': get_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.health.system',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Applmgmt': Applmgmt,
        'Databasestorage': Databasestorage,
        'Load': Load,
        'Mem': Mem,
        'Softwarepackages': Softwarepackages,
        'Storage': Storage,
        'Swap': Swap,
        'System': System,
    }

