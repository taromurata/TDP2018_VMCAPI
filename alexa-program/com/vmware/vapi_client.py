# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi_client`` component provides API infrastructure classes
and standard types that can be used in the interface specification of any
class.

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


class ComponentInfo(VapiStruct):
    """
    The ``ComponentInfo`` class holds component metadata of the different
    metadata types for an API component. The class allows any combination of
    metadata types to be aggregated into one instance.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 metamodel=None,
                 cli=None,
                 authentication=None,
                 routing=None,
                 privilege=None,
                ):
        """
        :type  metamodel: :class:`com.vmware.vapi.metadata.metamodel_client.ComponentInfo`
        :param metamodel: The metamodel component data
        :type  cli: :class:`com.vmware.vapi.metadata.cli_client.ComponentInfo` or ``None``
        :param cli: The CLI component data
            could be None because CLI metadata might not be present for the
            component
        :type  authentication: :class:`com.vmware.vapi.metadata.authentication_client.ComponentInfo` or ``None``
        :param authentication: The authentication component data
            could be None because authentication metadata might not be present
            for the component
        :type  routing: :class:`com.vmware.vapi.metadata.routing_client.ComponentInfo` or ``None``
        :param routing: The routing component data
            could be None because routing metadata might not be present for the
            component
        :type  privilege: :class:`com.vmware.vapi.metadata.privilege_client.ComponentInfo` or ``None``
        :param privilege: The privilege component data
            could be None because privilege metadata might not be present for
            the component
        """
        self.metamodel = metamodel
        self.cli = cli
        self.authentication = authentication
        self.routing = routing
        self.privilege = privilege
        VapiStruct.__init__(self)

ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.component_info', {
        'metamodel': type.ReferenceType('com.vmware.vapi.metadata.metamodel_client', 'ComponentInfo'),
        'cli': type.OptionalType(type.ReferenceType('com.vmware.vapi.metadata.cli_client', 'ComponentInfo')),
        'authentication': type.OptionalType(type.ReferenceType('com.vmware.vapi.metadata.authentication_client', 'ComponentInfo')),
        'routing': type.OptionalType(type.ReferenceType('com.vmware.vapi.metadata.routing_client', 'ComponentInfo')),
        'privilege': type.OptionalType(type.ReferenceType('com.vmware.vapi.metadata.privilege_client', 'ComponentInfo')),
    },
    ComponentInfo,
    False,
    None))



class MetadataInfo(VapiStruct):
    """
    The ``MetadataInfo`` is a class which holds a map of the available metadata
    aggregated in a :class:`ComponentInfo` class.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 version=None,
                 metadata=None,
                ):
        """
        :type  version: :class:`str`
        :param version: Version of the current ``MetadataInfo`` class. Property value
            changes when the content of the ``MetadataInfo`` or referenced
            classes changes. This enables class processing adjustments.
        :type  metadata: :class:`dict` of :class:`str` and :class:`ComponentInfo`
        :param metadata: Component information of all available components. The key in the
            :class:`dict` is the identifier of the component and the value is
            the aggregated :class:`ComponentInfo`.
            When clients pass a value of this class as a parameter, the key in
            the attribute :class:`dict` must be an identifier for the resource
            type: ``com.vmware.vapi.component``. When methods return a value of
            this class as a return value, the key in the attribute
            :class:`dict` will be an identifier for the resource type:
            ``com.vmware.vapi.component``.
        """
        self.version = version
        self.metadata = metadata
        VapiStruct.__init__(self)

MetadataInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata_info', {
        'version': type.StringType(),
        'metadata': type.MapType(type.IdType(), type.ReferenceType(__name__, 'ComponentInfo')),
    },
    MetadataInfo,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'metadata': 'com.vmware.vapi.metadata_client.StubFactory',
        'std': 'com.vmware.vapi.std_client.StubFactory',
    }

