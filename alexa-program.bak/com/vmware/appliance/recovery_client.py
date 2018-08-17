# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.appliance.recovery.
#---------------------------------------------------------------------------

"""
The ``com.vmware.appliance.recovery_client`` module provides classes for backin
up and restoring vCenter Appliance configuration. The module is available
starting in vSphere 6.7.

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


class Backup(VapiInterface):
    """
    ``Backup`` class provides methods Performs backup restore operations
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _BackupStub)

    class ReturnStatus(Enum):
        """
        ``Backup.ReturnStatus`` class Defines the state of precheck

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FAIL = None
        """
        Check failed

        """
        WARNING = None
        """
        Passed with warnings

        """
        OK = None
        """
        Check passed

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ReturnStatus` instance.
            """
            Enum.__init__(string)

    ReturnStatus._set_values([
        ReturnStatus('FAIL'),
        ReturnStatus('WARNING'),
        ReturnStatus('OK'),
    ])
    ReturnStatus._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.return_status',
        ReturnStatus))


    class LocationType(Enum):
        """
        ``Backup.LocationType`` class Defines type of all locations for
        backup/restore

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FTP = None
        """
        Destination is FTP server

        """
        HTTP = None
        """
        Destination is HTTP server

        """
        FTPS = None
        """
        Destination is FTPS server

        """
        HTTPS = None
        """
        Destination is HTTPS server

        """
        SCP = None
        """
        Destination is SSH server

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`LocationType` instance.
            """
            Enum.__init__(string)

    LocationType._set_values([
        LocationType('FTP'),
        LocationType('HTTP'),
        LocationType('FTPS'),
        LocationType('HTTPS'),
        LocationType('SCP'),
    ])
    LocationType._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.backup.location_type',
        LocationType))


    class LocalizableMessage(VapiStruct):
        """
        ``Backup.LocalizableMessage`` class Structure representing message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     default_message=None,
                     args=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: id in message bundle
            :type  default_message: :class:`str`
            :param default_message: text in english
            :type  args: :class:`list` of :class:`str`
            :param args: nested data
            """
            self.id = id
            self.default_message = default_message
            self.args = args
            VapiStruct.__init__(self)

    LocalizableMessage._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class ReturnResult(VapiStruct):
        """
        ``Backup.ReturnResult`` class Structure representing precheck result

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     status=None,
                     messages=None,
                    ):
            """
            :type  status: :class:`Backup.ReturnStatus`
            :param status: Check status
            :type  messages: :class:`list` of :class:`Backup.LocalizableMessage`
            :param messages: List of messages
            """
            self.status = status
            self.messages = messages
            VapiStruct.__init__(self)

    ReturnResult._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.return_result', {
            'status': type.ReferenceType(__name__, 'Backup.ReturnStatus'),
            'messages': type.ListType(type.ReferenceType(__name__, 'Backup.LocalizableMessage')),
        },
        ReturnResult,
        False,
        None))


    class BackupRequest(VapiStruct):
        """
        ``Backup.BackupRequest`` class Structure representing requested backup
        piece

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     parts=None,
                     backup_password=None,
                     location_type=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     comment=None,
                    ):
            """
            :type  parts: :class:`list` of :class:`str`
            :param parts: a list of optional parts. Run backup parts APIs to get list of
                optional parts and description
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: a password for a backup piece The backupPassword must adhere to the
                following password requirements: At least 8 characters, cannot be
                more than 20 characters in length. At least 1 uppercase letter. At
                least 1 lowercase letter. At least 1 numeric digit. At least 1
                special character (i.e. any character not in [0-9,a-z,A-Z]). Only
                visible ASCII characters (for example, no space).
                backupPassword If no password then the piece will not be encrypted
            :type  location_type: :class:`Backup.LocationType`
            :param location_type: a type of location
            :type  location: :class:`str`
            :param location: path or url
            :type  location_user: :class:`str` or ``None``
            :param location_user: username for location
                locationUser User name for this location if login is required.
            :type  location_password: :class:`str` or ``None``
            :param location_password: password for location
                locationPassword Password for the specified user if login is
                required at this location.
            :type  comment: :class:`str` or ``None``
            :param comment: Custom comment
                comment an optional comment
            """
            self.parts = parts
            self.backup_password = backup_password
            self.location_type = location_type
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.comment = comment
            VapiStruct.__init__(self)

    BackupRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.backup.backup_request', {
            'parts': type.ListType(type.StringType()),
            'backup_password': type.OptionalType(type.SecretType()),
            'location_type': type.ReferenceType(__name__, 'Backup.LocationType'),
            'location': type.StringType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'comment': type.OptionalType(type.StringType()),
        },
        BackupRequest,
        False,
        None))



    def validate(self,
                 piece,
                 ):
        """
        Check for backup errors without starting backup.

        :type  piece: :class:`Backup.BackupRequest`
        :param piece: BackupRequest Structure
        :rtype: :class:`Backup.ReturnResult`
        :return: ReturnResult Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.FeatureInUse` 
            A backup or restore is already in progress
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('validate',
                            {
                            'piece': piece,
                            })
class Restore(VapiInterface):
    """
    ``Restore`` class provides methods Performs restore operations
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _RestoreStub)

    class LocationType(Enum):
        """
        ``Restore.LocationType`` class Defines type of all locations for
        backup/restore

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        FTP = None
        """
        Destination is FTP server

        """
        HTTP = None
        """
        Destination is HTTP server

        """
        FTPS = None
        """
        Destination is FTPS server

        """
        HTTPS = None
        """
        Destination is HTTPS server

        """
        SCP = None
        """
        Destination is SSH server

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`LocationType` instance.
            """
            Enum.__init__(string)

    LocationType._set_values([
        LocationType('FTP'),
        LocationType('HTTP'),
        LocationType('FTPS'),
        LocationType('HTTPS'),
        LocationType('SCP'),
    ])
    LocationType._set_binding_type(type.EnumType(
        'com.vmware.appliance.recovery.restore.location_type',
        LocationType))


    class RestoreRequest(VapiStruct):
        """
        ``Restore.RestoreRequest`` class Structure representing requested restore
        piece

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     backup_password=None,
                     location_type=None,
                     location=None,
                     location_user=None,
                     location_password=None,
                     sso_admin_user_name=None,
                     sso_admin_user_password=None,
                    ):
            """
            :type  backup_password: :class:`str` or ``None``
            :param backup_password: a password for a backup piece
                backupPassword If no password then the piece will not be decrypted
            :type  location_type: :class:`Restore.LocationType`
            :param location_type: a type of location
            :type  location: :class:`str`
            :param location: path or url
            :type  location_user: :class:`str` or ``None``
            :param location_user: username for location
                locationUser User name for this location if login is required.
            :type  location_password: :class:`str` or ``None``
            :param location_password: password for location
                locationPassword Password for the specified user if login is
                required at this location.
            :type  sso_admin_user_name: :class:`str` or ``None``
            :param sso_admin_user_name: Administrators username for SSO. This attribute was added in
                vSphere API 6.7
                If None SSO authentication will not be used. If the vCenter Server
                is a management node or an embedded node, authentication is
                required.
            :type  sso_admin_user_password: :class:`str` or ``None``
            :param sso_admin_user_password: The password for SSO admin user. This attribute was added in
                vSphere API 6.7
                If None SSO authentication will not be used. If the vCenter Server
                is a management node or an embedded node, authentication is
                required.
            """
            self.backup_password = backup_password
            self.location_type = location_type
            self.location = location
            self.location_user = location_user
            self.location_password = location_password
            self.sso_admin_user_name = sso_admin_user_name
            self.sso_admin_user_password = sso_admin_user_password
            VapiStruct.__init__(self)

    RestoreRequest._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.restore_request', {
            'backup_password': type.OptionalType(type.SecretType()),
            'location_type': type.ReferenceType(__name__, 'Restore.LocationType'),
            'location': type.StringType(),
            'location_user': type.OptionalType(type.StringType()),
            'location_password': type.OptionalType(type.SecretType()),
            'sso_admin_user_name': type.OptionalType(type.StringType()),
            'sso_admin_user_password': type.OptionalType(type.SecretType()),
        },
        RestoreRequest,
        False,
        None))


    class LocalizableMessage(VapiStruct):
        """
        ``Restore.LocalizableMessage`` class Structure representing message

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     id=None,
                     default_message=None,
                     args=None,
                    ):
            """
            :type  id: :class:`str`
            :param id: id in message bundle
            :type  default_message: :class:`str`
            :param default_message: text in english
            :type  args: :class:`list` of :class:`str`
            :param args: nested data
            """
            self.id = id
            self.default_message = default_message
            self.args = args
            VapiStruct.__init__(self)

    LocalizableMessage._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.localizable_message', {
            'id': type.StringType(),
            'default_message': type.StringType(),
            'args': type.ListType(type.StringType()),
        },
        LocalizableMessage,
        False,
        None))


    class Metadata(VapiStruct):
        """
        ``Restore.Metadata`` class Structure representing metadata

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     timestamp=None,
                     parts=None,
                     version=None,
                     boxname=None,
                     sso_login_required=None,
                     comment=None,
                     applicable=None,
                     messages=None,
                    ):
            """
            :type  timestamp: :class:`datetime.datetime`
            :param timestamp: Time when this backup was completed.
            :type  parts: :class:`list` of :class:`str`
            :param parts: List of parts included in the backup.
            :type  version: :class:`str`
            :param version: VCSA version
            :type  boxname: :class:`str`
            :param boxname: Box name is PNID/ FQDN etc
            :type  sso_login_required: :class:`bool`
            :param sso_login_required: Is SSO login required for the vCenter server. This attribute was
                added in vSphere API 6.7
                This attribute is optional because it was added in a newer version
                than its parent node.
            :type  comment: :class:`str`
            :param comment: Custom comment
            :type  applicable: :class:`bool`
            :param applicable: Does the VCSA match the deployment type, network properties and
                version of backed up VC
            :type  messages: :class:`list` of :class:`Restore.LocalizableMessage`
            :param messages: Any messages if the backup is not aplicable
            """
            self.timestamp = timestamp
            self.parts = parts
            self.version = version
            self.boxname = boxname
            self.sso_login_required = sso_login_required
            self.comment = comment
            self.applicable = applicable
            self.messages = messages
            VapiStruct.__init__(self)

    Metadata._set_binding_type(type.StructType(
        'com.vmware.appliance.recovery.restore.metadata', {
            'timestamp': type.DateTimeType(),
            'parts': type.ListType(type.StringType()),
            'version': type.StringType(),
            'boxname': type.StringType(),
            'sso_login_required': type.OptionalType(type.BooleanType()),
            'comment': type.StringType(),
            'applicable': type.BooleanType(),
            'messages': type.ListType(type.ReferenceType(__name__, 'Restore.LocalizableMessage')),
        },
        Metadata,
        False,
        None))



    def validate(self,
                 piece,
                 ):
        """
        Get metadata before restore

        :type  piece: :class:`Restore.RestoreRequest`
        :param piece: RestoreRequest Structure
        :rtype: :class:`Restore.Metadata`
        :return: Metadata Structure
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            Generic error
        """
        return self._invoke('validate',
                            {
                            'piece': piece,
                            })
class _BackupStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for validate operation
        validate_input_type = type.StructType('operation-input', {
            'piece': type.ReferenceType(__name__, 'Backup.BackupRequest'),
        })
        validate_error_dict = {
            'com.vmware.vapi.std.errors.feature_in_use':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'FeatureInUse'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        validate_input_value_validator_list = [
        ]
        validate_output_validator_list = [
        ]
        validate_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/backup/validate',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'validate': {
                'input_type': validate_input_type,
                'output_type': type.ReferenceType(__name__, 'Backup.ReturnResult'),
                'errors': validate_error_dict,
                'input_value_validator_list': validate_input_value_validator_list,
                'output_validator_list': validate_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'validate': validate_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.backup',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _RestoreStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for validate operation
        validate_input_type = type.StructType('operation-input', {
            'piece': type.ReferenceType(__name__, 'Restore.RestoreRequest'),
        })
        validate_error_dict = {
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        validate_input_value_validator_list = [
        ]
        validate_output_validator_list = [
        ]
        validate_rest_metadata = OperationRestMetadata(
            http_method='POST',
            url_template='/appliance/recovery/restore/validate',
            path_variables={
            },
            query_parameters={
            }
        )

        operations = {
            'validate': {
                'input_type': validate_input_type,
                'output_type': type.ReferenceType(__name__, 'Restore.Metadata'),
                'errors': validate_error_dict,
                'input_value_validator_list': validate_input_value_validator_list,
                'output_validator_list': validate_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'validate': validate_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.appliance.recovery.restore',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Backup': Backup,
        'Restore': Restore,
        'backup': 'com.vmware.appliance.recovery.backup_client.StubFactory',
        'reconciliation': 'com.vmware.appliance.recovery.reconciliation_client.StubFactory',
        'restore': 'com.vmware.appliance.recovery.restore_client.StubFactory',
    }

