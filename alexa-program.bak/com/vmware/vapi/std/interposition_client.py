# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.interposition.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.std.interposition_client`` module provides classes that
TODO.

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


class InvocationRequest(VapiStruct):
    """
    Information about an interposed request for operation invocation. All
    interposers would receive an instance of this structure as an input
    parameter.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 service_id=None,
                 operation_id=None,
                 operation_input=None,
                 user=None,
                 groups=None,
                ):
        """
        :type  service_id: :class:`str`
        :param service_id: Fully qualified name of the service which contains the interposed
            operation. In canonical format. For example org.example.hello.
        :type  operation_id: :class:`str`
        :param operation_id: Name of the interposed operation. In canonical format. For example
            say_hello.
        :type  operation_input: :class:`DataValue`
        :param operation_input: Input of the interposed operation.
        :type  user: :class:`SecurityPrincipal` or ``None``
        :param user: User which started the interposed operation.
            There could be no authentication information. For example when
            methods are invoked anonymously.
        :type  groups: :class:`list` of :class:`SecurityPrincipal`
        :param groups: Groups of the user who started the interposed operation. Would be
            empty if there is no authentication information.
        """
        self.service_id = service_id
        self.operation_id = operation_id
        self.operation_input = operation_input
        self.user = user
        self.groups = groups
        VapiStruct.__init__(self)

InvocationRequest._set_binding_type(type.StructType(
    'com.vmware.vapi.std.interposition.invocation_request', {
        'service_id': type.StringType(),
        'operation_id': type.StringType(),
        'operation_input': type.OpaqueType(),
        'user': type.OptionalType(type.ReferenceType(__name__, 'SecurityPrincipal')),
        'groups': type.ListType(type.ReferenceType(__name__, 'SecurityPrincipal')),
    },
    InvocationRequest,
    False,
    None))



class InvocationResult(VapiStruct):
    """
    Information about the result from an interposed operation invocation. All
    POST interposers will receive an instance of this structure.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _validator_list = [
        UnionValidator(
            'result_type',
            {
                'NORMAL_RESULT' : [('output', True)],
                'ERROR_RESULT' : [('error', True)],
            }
        ),
    ]



    def __init__(self,
                 result_type=None,
                 output=None,
                 error=None,
                ):
        """
        :type  result_type: :class:`InvocationResult.ResultType`
        :param result_type: Type of the invocation result.
        :type  output: :class:`DataValue`
        :param output: Normal result value.
            This attribute is optional and it is only relevant when the value
            of ``resultType`` is
            :attr:`InvocationResult.ResultType.NORMAL_RESULT`.
        :type  error: :class:`vmware.vapi.struct.VapiStruct`
        :param error: Error result value.
            This attribute is optional and it is only relevant when the value
            of ``resultType`` is
            :attr:`InvocationResult.ResultType.ERROR_RESULT`.
        """
        self.result_type = result_type
        self.output = output
        self.error = error
        VapiStruct.__init__(self)

    class ResultType(Enum):
        """
        Type of the invocation result.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NORMAL_RESULT = None
        """
        Normal invocation result.

        """
        ERROR_RESULT = None
        """
        Error invocation result.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`ResultType` instance.
            """
            Enum.__init__(string)

    ResultType._set_values([
        ResultType('NORMAL_RESULT'),
        ResultType('ERROR_RESULT'),
    ])
    ResultType._set_binding_type(type.EnumType(
        'com.vmware.vapi.std.interposition.invocation_result.result_type',
        ResultType))

InvocationResult._set_binding_type(type.StructType(
    'com.vmware.vapi.std.interposition.invocation_result', {
        'result_type': type.ReferenceType(__name__, 'InvocationResult.ResultType'),
        'output': type.OptionalType(type.OpaqueType()),
        'error': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvocationResult,
    False,
    None))



class SecurityPrincipal(VapiStruct):
    """
    VMODL equivalent of com.vmware.vapi.security.PrincipalId.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 name=None,
                 domain=None,
                ):
        """
        :type  name: :class:`str`
        :param name: Principal name.
        :type  domain: :class:`str` or ``None``
        :param domain: Principal domain.
            Domain is optional in ``com.vmware.vapi.security.PrincipalId``
        """
        self.name = name
        self.domain = domain
        VapiStruct.__init__(self)

SecurityPrincipal._set_binding_type(type.StructType(
    'com.vmware.vapi.std.interposition.security_principal', {
        'name': type.StringType(),
        'domain': type.OptionalType(type.StringType()),
    },
    SecurityPrincipal,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

