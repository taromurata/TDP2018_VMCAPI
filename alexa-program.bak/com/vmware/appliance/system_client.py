# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.system.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.system_client`` module provides classes to query the
appliance system information. The module is available starting in vSphere 6.5.

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


class Storage(VapiInterface):
    """
    ``Storage`` class provides methods Appliance storage configuration
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _StorageStub)

    class StorageMapping(VapiStruct):
        """
        The ``Storage.StorageMapping`` class describes the mapping between VCSA
        partitions and the Hard disk numbers visible in the vSphere Web Client.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     disk=None,
                     partition=None,
                     description=None,
                    ):
            """
            :type  disk: :class:`str`
            :param disk: The disk number in the vSphere Web Client.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.system.storage``. When methods return a
                value of this class as a return value, the attribute will be an
                identifier for the resource type:
                ``com.vmware.appliance.system.storage``.
            :type  partition: :class:`str`
            :param partition: Storage partition name.
            :type  description: :class:`com.vmware.vapi.std_client.LocalizableMessage`
            :param description: Description of partition. This attribute was added in vSphere API
                6.7
                This attribute is optional because it was added in a newer version
                than its parent node.
            """
            self.disk = disk
            self.partition = partition
            self.description = description
            VapiStruct.__init__(self)

    StorageMapping._set_binding_type(type.StructType(
        'com.vmware.appliance.system.storage.storage_mapping', {
            'disk': type.IdType(resource_types='com.vmware.appliance.system.storage'),
            'partition': type.StringType(),
            'description': type.OptionalType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        },
        StorageMapping,
        False,
        None))


    class StorageChange(VapiStruct):
        """
        The ``Storage.StorageChange`` class describes the changes in capasity of a
        storage partition. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     old_size=None,
                     new_size=None,
                    ):
            """
            :type  old_size: :class:`long`
            :param old_size: Original size of the partition in MB. This attribute was added in
                vSphere API 6.7
            :type  new_size: :class:`long`
            :param new_size: Nedw size of the partition in MB. This attribute was added in
                vSphere API 6.7
            """
            self.old_size = old_size
            self.new_size = new_size
            VapiStruct.__init__(self)

    StorageChange._set_binding_type(type.StructType(
        'com.vmware.appliance.system.storage.storage_change', {
            'old_size': type.IntegerType(),
            'new_size': type.IntegerType(),
        },
        StorageChange,
        False,
        None))



    def list(self):
        """
        Get disk to partition mapping.


        :rtype: :class:`list` of :class:`Storage.StorageMapping`
        :return: list of mapping items
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('list', None)

    def resize(self):
        """
        Resize all partitions to 100 percent of disk size.


        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('resize', None)

    def resize_ex(self):
        """
        Resize all partitions to 100 percent of disk size. This method was
        added in vSphere API 6.7


        :rtype: :class:`dict` of :class:`str` and :class:`Storage.StorageChange`
        :return: List of the partitions with the size before and after resizing
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('resize_ex', None)
class Uptime(VapiInterface):
    """
    ``Uptime`` class provides methods Get the system uptime.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _UptimeStub)


    def get(self):
        """
        Get the system uptime.


        :rtype: :class:`float`
        :return: system uptime
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Time(VapiInterface):
    """
    ``Time`` class provides methods Gets system time.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _TimeStub)

    class SystemTimeStruct(VapiStruct):
        """
        ``Time.SystemTimeStruct`` class Structure representing the system time.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     seconds_since_epoch=None,
                     date=None,
                     time=None,
                     timezone=None,
                    ):
            """
            :type  seconds_since_epoch: :class:`float`
            :param seconds_since_epoch: seconds since the epoch
            :type  date: :class:`str`
            :param date: date format: Thu 07-31-2014
            :type  time: :class:`str`
            :param time: time format: 18:18:32
            :type  timezone: :class:`str`
            :param timezone: timezone
            """
            self.seconds_since_epoch = seconds_since_epoch
            self.date = date
            self.time = time
            self.timezone = timezone
            VapiStruct.__init__(self)

    SystemTimeStruct._set_binding_type(type.StructType(
        'com.vmware.appliance.system.time.system_time_struct', {
            'seconds_since_epoch': type.DoubleType(),
            'date': type.StringType(),
            'time': type.StringType(),
            'timezone': type.StringType(),
        },
        SystemTimeStruct,
        False,
        None))



    def get(self):
        """
        Get system time.


        :rtype: :class:`Time.SystemTimeStruct`
        :return: System time
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class Version(VapiInterface):
    """
    ``Version`` class provides methods Get the appliance version.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _VersionStub)

    class VersionStruct(VapiStruct):
        """
        ``Version.VersionStruct`` class Structure representing appliance version
        information.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     version=None,
                     product=None,
                     build=None,
                     type=None,
                     summary=None,
                     releasedate=None,
                     install_time=None,
                    ):
            """
            :type  version: :class:`str`
            :param version: Appliance version.
            :type  product: :class:`str`
            :param product: Appliance name.
            :type  build: :class:`str`
            :param build: Appliance build number.
            :type  type: :class:`str`
            :param type: Type of product. Same product can have different deployment
                options, which is represented by type.
            :type  summary: :class:`str`
            :param summary: Summary of patch (empty string, if the appliance has not been
                patched)
            :type  releasedate: :class:`str`
            :param releasedate: Release date of patch (empty string, if the appliance has not been
                patched)
            :type  install_time: :class:`str`
            :param install_time: Display the date and time when this system was first installed.
                Value will not change on subsequent updates.
            """
            self.version = version
            self.product = product
            self.build = build
            self.type = type
            self.summary = summary
            self.releasedate = releasedate
            self.install_time = install_time
            VapiStruct.__init__(self)

    VersionStruct._set_binding_type(type.StructType(
        'com.vmware.appliance.system.version.version_struct', {
            'version': type.StringType(),
            'product': type.StringType(),
            'build': type.StringType(),
            'type': type.StringType(),
            'summary': type.StringType(),
            'releasedate': type.StringType(),
            'install_time': type.StringType(),
        },
        VersionStruct,
        False,
        None))



    def get(self):
        """
        Get the version.


        :rtype: :class:`Version.VersionStruct`
        :return: version information about the appliance
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('get', None)
class _StorageStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/system/storage',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for resize operation
        resize_input_type = type.StructType('operation-input', {})
        resize_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        resize_input_value_validator_list = [
        ]
        resize_output_validator_list = [
        ]
        resize_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/system/storage/resize',
            path_variables={
            },
            query_parameters={
            }
        )

        # properties for resize_ex operation
        resize_ex_input_type = type.StructType('operation-input', {})
        resize_ex_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        resize_ex_input_value_validator_list = [
        ]
        resize_ex_output_validator_list = [
        ]
        resize_ex_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/system/storage?action=resize-ex',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Storage.StorageMapping')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'resize': {
                'input_type': resize_input_type,
                'output_type': type.VoidType(),
                'errors': resize_error_dict,
                'input_value_validator_list': resize_input_value_validator_list,
                'output_validator_list': resize_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'resize_ex': {
                'input_type': resize_ex_input_type,
                'output_type': type.MapType(type.StringType(), type.ReferenceType(__name__, 'Storage.StorageChange')),
                'errors': resize_ex_error_dict,
                'input_value_validator_list': resize_ex_input_value_validator_list,
                'output_validator_list': resize_ex_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'resize': resize_rest_metadata,
            'resize_ex': resize_ex_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.system.storage',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _UptimeStub(ApiInterfaceStub):
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
            url_template='/appliance/system/uptime',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.DoubleType(),
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
            self, iface_name='com.vmware.appliance.system.uptime',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _TimeStub(ApiInterfaceStub):
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
            url_template='/appliance/system/time',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Time.SystemTimeStruct'),
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
            self, iface_name='com.vmware.appliance.system.time',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _VersionStub(ApiInterfaceStub):
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
            url_template='/appliance/system/version',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Version.VersionStruct'),
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
            self, iface_name='com.vmware.appliance.system.version',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Storage': Storage,
        'Uptime': Uptime,
        'Time': Time,
        'Version': Version,
        'time': 'com.vmware.appliance.system.time_client.StubFactory',
    }

