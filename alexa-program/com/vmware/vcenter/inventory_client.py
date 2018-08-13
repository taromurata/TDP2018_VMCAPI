# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.inventory.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vcenter.inventory_client`` component provides methods and
classes for retrieving vCenter datastore and network information for a given
:class:`list` of identifiers.

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


class Datastore(VapiInterface):
    """
    The ``Datastore`` class provides methods to retrieve information about
    datastores.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _DatastoreStub)

    class Info(VapiStruct):
        """
        The ``Datastore.Info`` class contains information about a datastore.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                    ):
            """
            :type  type: :class:`str`
            :param type: Type of the datastore.
                When clients pass a value of this class as a parameter, the
                attribute must be one of ``Datastore`` or ``StoragePod``. When
                methods return a value of this class as a return value, the
                attribute will be one of ``Datastore`` or ``StoragePod``.
            """
            self.type = type
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.inventory.datastore.info', {
            'type': type.StringType(),
        },
        Info,
        False,
        None))



    def find(self,
             datastores,
             ):
        """
        Returns datastore information for the specified datastores. The key in
        the return value :class:`dict` is the datastore identifier and the
        value in the :class:`dict` is the datastore information.

        :type  datastores: :class:`list` of :class:`str`
        :param datastores: Identifiers of the datastores for which information will be
            returned.
            The parameter must contain identifiers for the resource type:
            ``Datastore``.
        :rtype: :class:`dict` of :class:`str` and (:class:`Datastore.Info` or ``None``)
        :return: Datastore information for the specified datastores. The key in the
            return value :class:`dict` is the datastore identifier and the
            value in the :class:`dict` is the datastore information.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``Datastore``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if no datastore can be found for one or more of the datastore
            identifiers in ``datastores``
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``Datastore`` referenced by the parameter
              ``datastores`` requires ``System.Read``.
        """
        return self._invoke('find',
                            {
                            'datastores': datastores,
                            })
class Network(VapiInterface):
    """
    The ``Network`` class provides methods to retrieve information about
    vCenter Server networks.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NetworkStub)

    class Info(VapiStruct):
        """
        The ``Network.Info`` class contains information about a vCenter Server
        network.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     type=None,
                    ):
            """
            :type  type: :class:`str`
            :param type: Type of the vCenter Server network.
                When clients pass a value of this class as a parameter, the
                attribute must be one of ``Network``,
                ``DistributedVirtualPortgroup``, or ``OpaqueNetwork``. When methods
                return a value of this class as a return value, the attribute will
                be one of ``Network``, ``DistributedVirtualPortgroup``, or
                ``OpaqueNetwork``.
            """
            self.type = type
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vcenter.inventory.network.info', {
            'type': type.StringType(),
        },
        Info,
        False,
        None))



    def find(self,
             networks,
             ):
        """
        Returns network information for the specified vCenter Server networks.
        The key in the return value :class:`dict` is the network identifier and
        the value in the :class:`dict` is the network information.

        :type  networks: :class:`list` of :class:`str`
        :param networks: Identifiers of the vCenter Server networks for which information
            will be returned.
            The parameter must contain identifiers for the resource type:
            ``Network``.
        :rtype: :class:`dict` of :class:`str` and (:class:`Network.Info` or ``None``)
        :return: Network information for the specified vCenter Server networks. The
            key in the return value :class:`dict` is the network identifier and
            the value in the :class:`dict` is the network information.
            The key in the return value :class:`dict` will be an identifier for
            the resource type: ``Network``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if no datastore can be found for one or more of the vCenter Server
            network identifiers in ``networks``
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthorized`
            if you do not have all of the privileges described as follows: 
            
            * Method execution requires ``System.Read``.
            * The resource ``Network`` referenced by the parameter ``networks``
              requires ``System.Read``.
        """
        return self._invoke('find',
                            {
                            'networks': networks,
                            })
class _DatastoreStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for find operation
        find_input_type = type.StructType('operation-input', {
            'datastores': type.ListType(type.IdType()),
        })
        find_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        find_input_value_validator_list = [
        ]
        find_output_validator_list = [
        ]
        find_rest_metadata = None

        operations = {
            'find': {
                'input_type': find_input_type,
                'output_type': type.MapType(type.IdType(), type.OptionalType(type.ReferenceType(__name__, 'Datastore.Info'))),
                'errors': find_error_dict,
                'input_value_validator_list': find_input_value_validator_list,
                'output_validator_list': find_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'find': find_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.inventory.datastore',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NetworkStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for find operation
        find_input_type = type.StructType('operation-input', {
            'networks': type.ListType(type.IdType()),
        })
        find_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        find_input_value_validator_list = [
        ]
        find_output_validator_list = [
        ]
        find_rest_metadata = None

        operations = {
            'find': {
                'input_type': find_input_type,
                'output_type': type.MapType(type.IdType(), type.OptionalType(type.ReferenceType(__name__, 'Network.Info'))),
                'errors': find_error_dict,
                'input_value_validator_list': find_input_value_validator_list,
                'output_validator_list': find_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'find': find_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vcenter.inventory.network',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Datastore': Datastore,
        'Network': Network,
    }

