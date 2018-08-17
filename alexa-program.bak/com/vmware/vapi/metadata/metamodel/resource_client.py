# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.metamodel.resource.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.metamodel.resource_client`` module provides
classes to retrieve metamodel information for resource types.

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


class Model(VapiInterface):
    """
    The ``Model`` class provides methods to retrieve information about models. 
    
    A structure is used as a model if it is used for persisting data about an
    entity. Some of the fields in the model structure are also used for
    creating indexes for querying. 
    
    One or more services can operate on the same resource type. One or more
    services can provide the model structure for an entity of this resource
    type. Using ``Model`` class you can retrieve the list of all the structure
    elements that are model structures for a given resource type.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ModelStub)


    def list(self,
             resource_id,
             ):
        """
        Returns the set of identifiers for the structure elements that are
        models for the resource type corresponding to ``resource_id``. 
        
        The :class:`com.vmware.vapi.metadata.metamodel_client.Structure` class
        provides methods to retrieve more details about the structure elements
        corresponding to the identifiers returned by this method.

        :type  resource_id: :class:`str`
        :param resource_id: Identifier of the resource type.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.resource``.
        :rtype: :class:`set` of :class:`str`
        :return: The set of identifiers for the models that are associated with the
            resource type in ``resource_id``.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.structure``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if the resource type associated with ``resource_id`` does not
            exist.
        """
        return self._invoke('list',
                            {
                            'resource_id': resource_id,
                            })
class _ModelStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'resource_id': type.IdType(resource_types='com.vmware.vapi.resource'),
        })
        list_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.SetType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.metamodel.resource.model',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Model': Model,
    }

