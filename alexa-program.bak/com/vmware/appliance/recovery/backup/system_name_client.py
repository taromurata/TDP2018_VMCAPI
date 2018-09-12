# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.backup.system_name.
#---------------------------------------------------------------------------

"""


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


class Archive(VapiInterface):
    """
    The ``Archive`` class provides methods to get the backup information. This
    class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ArchiveStub)

    class Info(VapiStruct):
        """
        The ``Archive.Info`` class represents backup archive information. This
        class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     timestamp=None,
                     location=None,
                     parts=None,
                     version=None,
                     system_name=None,
                     comment=None,
                    ):
            """
            :type  timestamp: :class:`datetime.datetime`
            :param timestamp: Time when this backup was completed. This attribute was added in
                vSphere API 6.7
            :type  location: :class:`str`
            :param location: Backup location URL. This attribute was added in vSphere API 6.7
            :type  parts: :class:`list` of :class:`str`
            :param parts: List of parts included in the backup. This attribute was added in
                vSphere API 6.7
            :type  version: :class:`str`
            :param version: The version of the appliance represented by the backup. This
                attribute was added in vSphere API 6.7
            :type  system_name: :class:`str`
            :param system_name: The system name identifier of the appliance represented by the
                backup. This attribute was added in vSphere API 6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.system_name``. When methods
                return a value of this class as a return value, the attribute will
                be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.system_name``.
            :type  comment: :class:`str`
            :param comment: Custom comment added by the user for this backup. This attribute
                was added in vSphere API 6.7
            """
            self.timestamp = timestamp
            self.location = location
            self.parts = parts
            self.version = version
            self.system_name = system_name
            self.comment = comment
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.system_name.archive.info', {
            'timestamp': type.DateTimeType(),
            'location': type.URIType(),
            'parts': type.ListType(type.StringType()),
            'version': type.StringType(),
            'system_name': type.IdType(resource_types='com.vmware.appliance.recovery.backup.system_name'),
            'comment': type.StringType(),
        },
        Info,
        False,
        None))


    class Summary(VapiStruct):
        """
        The ``Archive.Summary`` class contains commonly used information about a
        backup archive. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     archive=None,
                     timestamp=None,
                     version=None,
                     comment=None,
                    ):
            """
            :type  archive: :class:`str`
            :param archive: Backup archive identifier. This attribute was added in vSphere API
                6.7
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.system_name.archive``. When
                methods return a value of this class as a return value, the
                attribute will be an identifier for the resource type:
                ``com.vmware.appliance.recovery.backup.system_name.archive``.
            :type  timestamp: :class:`datetime.datetime`
            :param timestamp: Time when this backup was started. This attribute was added in
                vSphere API 6.7
            :type  version: :class:`str`
            :param version: The version of the appliance represented by the backup archive.
                This attribute was added in vSphere API 6.7
            :type  comment: :class:`str`
            :param comment: Custom comment added by the user for this backup. This attribute
                was added in vSphere API 6.7
            """
            self.archive = archive
            self.timestamp = timestamp
            self.version = version
            self.comment = comment
            VapiStruct.__init__(self)

    Summary._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.system_name.archive.summary', {
            'archive': type.IdType(resource_types='com.vmware.appliance.recovery.backup.system_name.archive'),
            'timestamp': type.DateTimeType(),
            'version': type.StringType(),
            'comment': type.StringType(),
        },
        Summary,
        False,
        None))


    class FilterSpec(VapiStruct):
        """
        The ``Archive.FilterSpec`` class contains attributes used to filter the
        results when listing backup archives (see :func:`Archive.list`). If
        multiple attributes are specified, only backup archives matching all of the
        attributes match the filter. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     start_timestamp=None,
                     end_timestamp=None,
                     comment_substring=None,
                     max_results=None,
                    ):
            """
            :type  start_timestamp: :class:`datetime.datetime` or ``None``
            :param start_timestamp: Backup must have been taken on or after this time to match the
                filter. This attribute was added in vSphere API 6.7
                If None the filter will match oldest backups.
            :type  end_timestamp: :class:`datetime.datetime` or ``None``
            :param end_timestamp: Backup must have been taken on or before this time to match the
                filter. This attribute was added in vSphere API 6.7
                If None the filter will match most recent backups.
            :type  comment_substring: :class:`str` or ``None``
            :param comment_substring: Backup comment must contain this :class:`str` to match the filter.
                This attribute was added in vSphere API 6.7
                If None the filter will match backups with any comment.
            :type  max_results: :class:`long` or ``None``
            :param max_results: Limit result to a max count of most recent backups. This attribute
                was added in vSphere API 6.7
                If None it defaults to 128.
            """
            self.start_timestamp = start_timestamp
            self.end_timestamp = end_timestamp
            self.comment_substring = comment_substring
            self.max_results = max_results
            VapiStruct.__init__(self)

    FilterSpec._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.system_name.archive.filter_spec', {
            'start_timestamp': type.OptionalType(type.DateTimeType()),
            'end_timestamp': type.OptionalType(type.DateTimeType()),
            'comment_substring': type.OptionalType(type.StringType()),
            'max_results': type.OptionalType(type.IntegerType()),
        },
        FilterSpec,
        False,
        None))



    def get(self,
            spec,
            system_name,
            archive,
            ):
        """
        Returns the information for backup corresponding to given backup
        location and system name. This method was added in vSphere API 6.7

        :type  spec: :class:`com.vmware.appliance.recovery.backup_client.LocationSpec`
        :param spec: LocationSpec Structure.
        :type  system_name: :class:`str`
        :param system_name: System name identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.system_name``.
        :type  archive: :class:`str`
        :param archive: Archive identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.system_name.archive``.
        :rtype: :class:`Archive.Info`
        :return: Info Structure.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if backup does not exist.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('get',
                            {
                            'spec': spec,
                            'system_name': system_name,
                            'archive': archive,
                            })

    def list(self,
             loc_spec,
             system_name,
             filter_spec,
             ):
        """
        Returns information about backup archives corresponding to given backup
        location and system name, which match the :class:`Archive.FilterSpec`.
        This method was added in vSphere API 6.7

        :type  loc_spec: :class:`com.vmware.appliance.recovery.backup_client.LocationSpec`
        :param loc_spec: LocationSpec Structure.
        :type  system_name: :class:`str`
        :param system_name: System name identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.appliance.recovery.backup.system_name``.
        :type  filter_spec: :class:`Archive.FilterSpec`
        :param filter_spec: Specification of matching backups for which information should be
            returned.
        :rtype: :class:`list` of :class:`Archive.Summary`
        :return: Commonly used information about the backup archives.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if combination of ``loc_spec`` and system name does not refer to an
            existing location on the backup server.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            if any error occurs during the execution of the operation.
        """
        return self._invoke('list',
                            {
                            'loc_spec': loc_spec,
                            'system_name': system_name,
                            'filter_spec': filter_spec,
                            })
class _ArchiveStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType('com.vmware.appliance.recovery.backup_client', 'LocationSpec'),
            'system_name': type.IdType(resource_types='com.vmware.appliance.recovery.backup.system_name'),
            'archive': type.IdType(resource_types='com.vmware.appliance.recovery.backup.system_name.archive'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/recovery/backup/system-name/{systemName}/archives/{archive}',
            path_variables={
                'system_name': 'systemName',
                'archive': 'archive',
            },
            query_parameters={
            }
        )

        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'loc_spec': type.ReferenceType('com.vmware.appliance.recovery.backup_client', 'LocationSpec'),
            'system_name': type.IdType(resource_types='com.vmware.appliance.recovery.backup.system_name'),
            'filter_spec': type.ReferenceType(__name__, 'Archive.FilterSpec'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/appliance/recovery/backup/system-name/{systemName}/archives',
            path_variables={
                'system_name': 'systemName',
            },
            query_parameters={
            }
        )

        operations = {
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Archive.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Archive.Summary')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'get': get_rest_metadata,
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.backup.system_name.archive',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Archive': Archive,
    }

