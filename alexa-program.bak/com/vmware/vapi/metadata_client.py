# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.
#---------------------------------------------------------------------------

"""
The :mod:`com.vmware.vapi.metadata_client` module provides metadata classes.
These are classes that provide different facets of API information. Clients can
use these classes to: 

* Discover APIs available in the infrastructure.
* Fetch metadata that can be used to build presentation layers like CLI, REST,
  etc.
* Fetch authentication and authorization metadata.

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

class SourceType(Enum):
    """
    The ``SourceType`` class defines the types of sources for API metadata. You
    specify the type of source when adding a metadata source to a metadata
    service.

    .. note::
        This class represents an enumerated type in the interface language
        definition. The class contains class attributes which represent the
        values in the current version of the enumerated type. Newer versions of
        the enumerated type may contain new values. To use new values of the
        enumerated type in communication with a server that supports the newer
        version of the API, you instantiate this class. See :ref:`enumerated
        type description page <enumeration_description>`.
    """
    FILE = None
    """
    Indicates the metadata source is a JSON file.

    """
    REMOTE = None
    """
    Indicates the metadata source is a remote server.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`SourceType` instance.
        """
        Enum.__init__(string)

SourceType._set_values([
    SourceType('FILE'),
    SourceType('REMOTE'),
])
SourceType._set_binding_type(type.EnumType(
    'com.vmware.vapi.metadata.source_type',
    SourceType))




class SourceCreateSpec(VapiStruct):
    """
    The ``SourceCreateSpec`` class contains the registration information for a
    metadata source.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'type',
            {
                'FILE' : [('filepath', True)],
                'REMOTE' : [('address', True)],
            }
        ),
    ]



    def __init__(self,
                 description=None,
                 type=None,
                 filepath=None,
                 address=None,
                ):
        """
        :type  description: :class:`str`
        :param description: English language human readable description of the source.
        :type  type: :class:`SourceType`
        :param type: Type of the metadata source.
        :type  filepath: :class:`str`
        :param filepath: Absolute file path of the metamodel metadata file that has the
            metamodel information about one component element.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`SourceType.FILE`.
        :type  address: :class:`str`
        :param address: Connection information of the remote server. This should be of the
            format http(s)://IP:port/namespace. 
            
            The remote server should contain the classes in
            :mod:`com.vmware.vapi.metadata.metamodel_client` module. It could
            expose metamodel information of one or more components.
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`SourceType.REMOTE`.
        """
        self.description = description
        self.type = type
        self.filepath = filepath
        self.address = address
        VapiStruct.__init__(self)

SourceCreateSpec._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.source_create_spec', {
        'description': type.StringType(),
        'type': type.ReferenceType(__name__, 'SourceType'),
        'filepath': type.OptionalType(type.StringType()),
        'address': type.OptionalType(type.URIType()),
    },
    SourceCreateSpec,
    False,
    None))



class SourceInfo(VapiStruct):
    """
    Metadata source info

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'type',
            {
                'FILE' : [('file_name', True)],
                'REMOTE' : [('remote_addr', True), ('msg_protocol', True)],
            }
        ),
    ]



    def __init__(self,
                 type=None,
                 file_name=None,
                 remote_addr=None,
                 msg_protocol=None,
                ):
        """
        :type  type: :class:`SourceType`
        :param type: Type of the metadata source
        :type  file_name: :class:`str`
        :param file_name: Name of the metadata source file
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`SourceType.FILE`.
        :type  remote_addr: :class:`str`
        :param remote_addr: Address of the remote metadata source
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`SourceType.REMOTE`.
        :type  msg_protocol: :class:`str`
        :param msg_protocol: Message protocol to be used
            This attribute is optional and it is only relevant when the value
            of ``type`` is :attr:`SourceType.REMOTE`.
        """
        self.type = type
        self.file_name = file_name
        self.remote_addr = remote_addr
        self.msg_protocol = msg_protocol
        VapiStruct.__init__(self)

SourceInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.source_info', {
        'type': type.ReferenceType(__name__, 'SourceType'),
        'file_name': type.OptionalType(type.StringType()),
        'remote_addr': type.OptionalType(type.StringType()),
        'msg_protocol': type.OptionalType(type.StringType()),
    },
    SourceInfo,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'authentication': 'com.vmware.vapi.metadata.authentication_client.StubFactory',
        'cli': 'com.vmware.vapi.metadata.cli_client.StubFactory',
        'metamodel': 'com.vmware.vapi.metadata.metamodel_client.StubFactory',
        'privilege': 'com.vmware.vapi.metadata.privilege_client.StubFactory',
        'routing': 'com.vmware.vapi.metadata.routing_client.StubFactory',
    }

