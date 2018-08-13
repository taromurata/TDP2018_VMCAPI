# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vcenter.deployment.install.initial_config.remote_psc.
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


class Thumbprint(VapiInterface):
    """
    The ``Thumbprint`` class provides methods to get the thumbprint of the
    remote PSC. This class was added in vSphere API 6.7
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _ThumbprintStub)

    class RemoteSpec(VapiStruct):
        """
        The ``Thumbprint.RemoteSpec`` class contains the information used to
        connect to the remote PSC. This class was added in vSphere API 6.7

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     address=None,
                     https_port=None,
                    ):
            """
            :type  address: :class:`str`
            :param address: The IP address or DNS resolvable name of the remote PSC. This
                attribute was added in vSphere API 6.7
            :type  https_port: :class:`long` or ``None``
            :param https_port: The HTTPS port of the remote PSC. This attribute was added in
                vSphere API 6.7
                If None, port 443 will be used.
            """
            self.address = address
            self.https_port = https_port
            VapiStruct.__init__(self)

    RemoteSpec._set_binding_type(type.StructType(
        'com.vmware.vcenter.deployment.install.initial_config.remote_psc.thumbprint.remote_spec', {
            'address': type.StringType(),
            'https_port': type.OptionalType(type.IntegerType()),
        },
        RemoteSpec,
        False,
        None))



    def get(self,
            spec,
            ):
        """
        Gets the SHA1 thumbprint of the remote PSC. This method was added in
        vSphere API 6.7

        :type  spec: :class:`Thumbprint.RemoteSpec`
        :param spec: Information used to connect to the remote PSC.
        :rtype: :class:`str`
        :return: The thumbprint of the specified remote PSC
        :raise: :class:`com.vmware.vapi.std.errors_client.Unauthenticated` 
            if the caller is not authenticated.
        :raise: :class:`com.vmware.vapi.std.errors_client.Error` 
            on exception.
        """
        return self._invoke('get',
                            {
                            'spec': spec,
                            })
class _ThumbprintStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'spec': type.ReferenceType(__name__, 'Thumbprint.RemoteSpec'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.unauthenticated':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Unauthenticated'),
            'com.vmware.vapi.std.errors.error':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'Error'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = OperationRestMetadata(
            http_method='GET',
            url_template='/vcenter/deployment/install/initial-config/remote-psc/thumbprint',
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
            self, iface_name='com.vmware.vcenter.deployment.install.initial_config.remote_psc.thumbprint',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Thumbprint': Thumbprint,
    }

