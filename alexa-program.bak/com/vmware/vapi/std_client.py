# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.std_client`` module provides standard types that can be
used in the interface specification of any class.

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


class AuthenticationScheme(VapiStruct):
    """
    The :class:`AuthenticationScheme` class defines constants for
    authentication scheme identifiers for authentication mechanisms present in
    the vAPI infrastructure shipped by VMware. 
    
    A third party extension can define and implements it's own authentication
    mechanism and define a constant in a different IDL file.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """
    NO_AUTHENTICATION = "com.vmware.vapi.std.security.no_authentication"
    """
    Indicates that the request doesn't need any authentication.

    """
    SAML_BEARER_TOKEN = "com.vmware.vapi.std.security.saml_bearer_token"
    """
    Indicates that the security context in a request is using a SAML bearer token
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier: com.vmware.vapi.std.security.saml_bearer_token
    * The token itself

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.saml_bearer_token',
    'token': 'the token itself'
    }`` vAPI runtime provide convenient factory methods that take SAML bearer token
    and to create the security context that conforms to the above mentioned format.

    """
    SAML_HOK_TOKEN = "com.vmware.vapi.std.security.saml_hok_token"
    """
    Indicates that the security context in a request is using a SAML holder-of-key
    token based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier: com.vmware.vapi.std.security.saml_hok_token
    * Signature of the request: This includes - algorithm used for signing the
      request, SAML holder of key token and signature digest
    * Request timestamp: This includes the ``created`` and ``expires`` timestamp of
      the request. The timestamp should match the following format -
      YYYY-MM-DDThh:mm:ss.sssZ (e.g. 1878-03-03T19:20:30.451Z).

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.saml_hok_token',
    'signature': {
    'alg': 'RS256',
    'samlToken': ...,
    'value': ...,``, 'timestamp': { 'created': '2012-10-26T12:24:18.941Z',
    'expires': '2012-10-26T12:44:18.941Z', } } } vAPI runtime provide convenient
    factory methods that take SAML holder of key token and private key to create
    the security context that conforms to the above mentioned format.

    """
    SESSION_ID = "com.vmware.vapi.std.security.session_id"
    """
    Indicates that the security context in a request is using a session identifier
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.session_id
    * Valid session identifier - This is usually returned by a login method of a
      session manager interface for a particular vAPI service of this authentication
      scheme

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.session_id',
    'sessionId': ....,
    }`` vAPI runtime provides convenient factory methods that take session
    identifier as input parameter and create a security context that conforms to
    the above format.

    """
    USER_PASSWORD = "com.vmware.vapi.std.security.user_pass"
    """
    Indicates that the security context in a request is using username/password
    based authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.user_pass
    * Username
    * Password

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.user_pass',
    'userName': ....,
    'password': ...
    }`` 
    vAPI runtime provides convenient factory methods that take username and
    password as input parameters and create a security context that conforms to the
    above format.

    """
    OAUTH_ACCESS_TOKEN = "com.vmware.vapi.std.security.oauth"
    """
    Indicates that the security context in a request is using OAuth2 based
    authentication scheme. 

    In this scheme, the following pieces of information has to be passed in the
    SecurityContext structure in the execution context of the request: 

    * The scheme identifier - com.vmware.vapi.std.security.oauth
    * Valid OAuth2 access token - This is usually acquired by OAuth2 Authorization
      Server after successful authentication of the end user.

     

     Sample security context in JSON format that matches the specification: ``{
    'schemeId': 'com.vmware.vapi.std.security.oauth',
    'accesstoken': ....
    }`` 
    vAPI runtime provides convenient factory methods that takes OAuth2 access token
    as input parameter and creates a security context that conforms to the above
    format.

    """




    def __init__(self,
                ):
        """
        """
        VapiStruct.__init__(self)

AuthenticationScheme._set_binding_type(type.StructType(
    'com.vmware.vapi.std.authentication_scheme', {
    },
    AuthenticationScheme,
    False,
    None))



class DynamicID(VapiStruct):
    """
    The ``DynamicID`` class represents an identifier for a resource of an
    arbitrary type.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 type=None,
                 id=None,
                ):
        """
        :type  type: :class:`str`
        :param type: The type of resource being identified (for example
            ``com.acme.Person``). 
            
            Classes that contain methods for creating and deleting resources
            typically contain a class attribute specifying the resource type
            for the resources being created and deleted. The API metamodel
            metadata classes include a class that allows retrieving all the
            known resource types.
        :type  id: :class:`str`
        :param id: The identifier for a resource whose type is specified by
            :attr:`DynamicID.type`.
            When clients pass a value of this class as a parameter, the
            attribute ``type`` must contain the actual resource type. When
            methods return a value of this class as a return value, the
            attribute ``type`` will contain the actual resource type.
        """
        self.type = type
        self.id = id
        VapiStruct.__init__(self)

DynamicID._set_binding_type(type.StructType(
    'com.vmware.vapi.std.dynamic_ID', {
        'type': type.StringType(),
        'id': type.IdType(resource_types=[], resource_type_field_name="type"),
    },
    DynamicID,
    False,
    None))



class LocalizableMessage(VapiStruct):
    """
    The ``LocalizableMessage`` class represents a localizable string or message
    template. Classes include one or more localizable message templates in the
    exceptions they report so that clients can display diagnostic messages in
    the native language of the user. Classes can include localizable strings in
    the data returned from methods to allow clients to display localized status
    information in the native language of the user.

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
        :param id: Unique identifier of the localizable string or message template. 
            
            This identifier is typically used to retrieve a locale-specific
            string or message template from a message catalog.
        :type  default_message: :class:`str`
        :param default_message: The value of this localizable string or message template in the
            ``en_US`` (English) locale. If :attr:`LocalizableMessage.id` refers
            to a message template, the default message will contain the
            substituted arguments. This value can be used by clients that do
            not need to display strings and messages in the native language of
            the user. It could also be used as a fallback if a client is unable
            to access the appropriate message catalog.
        :type  args: :class:`list` of :class:`str`
        :param args: Arguments to be substituted into a message template.
        """
        self.id = id
        self.default_message = default_message
        self.args = args
        VapiStruct.__init__(self)

LocalizableMessage._set_binding_type(type.StructType(
    'com.vmware.vapi.std.localizable_message', {
        'id': type.StringType(),
        'default_message': type.StringType(),
        'args': type.ListType(type.StringType()),
    },
    LocalizableMessage,
    False,
    None))




class StubFactory(StubFactoryBase):
    _attrs = {
        'activation': 'com.vmware.vapi.std.activation_client.StubFactory',
        'errors': 'com.vmware.vapi.std.errors_client.StubFactory',
        'interposition': 'com.vmware.vapi.std.interposition_client.StubFactory',
        'introspection': 'com.vmware.vapi.std.introspection_client.StubFactory',
    }

