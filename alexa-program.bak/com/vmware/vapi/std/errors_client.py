# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.std.errors.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.std.errors_client`` module provides the standard
exceptions that can be included in the list of exceptions in the specification
of methods to indicate that the method might report those exceptions. It also
provides some classes intended to be used as payload to provide additional
information about those exceptions.

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


class ArgumentLocations(VapiStruct):
    """
    The ``ArgumentLocations`` class describes which part(s) of the input to the
    method caused the exception. 
    
    Some types of exceptions are caused by the value of one of the inputs to
    the method, possibly due to an interaction with other inputs to the method.
    This class is intended to be used as the payload to identify those inputs
    when the method reports exceptions like :class:`InvalidArgument` or
    :class:`NotFound`. See :attr:`Error.data`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 primary=None,
                 secondary=None,
                ):
        """
        :type  primary: :class:`str`
        :param primary: String describing the location of the input that triggered the
            exception.
        :type  secondary: :class:`list` of :class:`str`
        :param secondary: :class:`list` (possibly empty) of strings describing the locations
            of other inputs that caused the the primary input to trigger the
            exception.
        """
        self.primary = primary
        self.secondary = secondary
        VapiStruct.__init__(self)

ArgumentLocations._set_binding_type(type.StructType(
    'com.vmware.vapi.std.errors.argument_locations', {
        'primary': type.StringType(),
        'secondary': type.ListType(type.StringType()),
    },
    ArgumentLocations,
    False,
    None))



class FileLocations(VapiStruct):
    """
    The ``FileLocations`` class identifies the file(s) that caused the method
    to report the exception. 
    
    Some types of exceptions are caused by a problem with one or more files.
    This class is intended to be used as the payload to identify those files
    when the method reports exceptions like :class:`NotFound`. See
    :attr:`Error.data`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 primary=None,
                 secondary=None,
                ):
        """
        :type  primary: :class:`str`
        :param primary: String identifying the file that triggered the exception.
        :type  secondary: :class:`list` of :class:`str`
        :param secondary: :class:`list` (possibly empty) of strings identifying other files
            that caused the primary file to trigger the exception.
        """
        self.primary = primary
        self.secondary = secondary
        VapiStruct.__init__(self)

FileLocations._set_binding_type(type.StructType(
    'com.vmware.vapi.std.errors.file_locations', {
        'primary': type.StringType(),
        'secondary': type.ListType(type.StringType()),
    },
    FileLocations,
    False,
    None))



class TransientIndication(VapiStruct):
    """
    The ``TransientIndication`` class indicates whether or not the exception is
    transient. 
    
    Some types of exceptions are transient in certain situtations and not
    transient in other situtations. This exception payload can be used to
    indicate to clients whether a particular exception is transient. See
    :attr:`Error.data`.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 is_transient=None,
                ):
        """
        :type  is_transient: :class:`bool`
        :param is_transient: Indicates that the exception this class is attached to is
            transient.
        """
        self.is_transient = is_transient
        VapiStruct.__init__(self)

TransientIndication._set_binding_type(type.StructType(
    'com.vmware.vapi.std.errors.transient_indication', {
        'is_transient': type.BooleanType(),
    },
    TransientIndication,
    False,
    None))



class Error(VapiError):
    """
    The ``Error`` exception describes theattributes common to all standard
    exceptions. 
    
     This exception serves two purposes: 
    
    #. It is the exception that clients in many programming languages can catch
       to handle all standard exceptions. Typically those clients will display one
       or more of the localizable messages from :attr:`Error.messages` to a human.
    #. It is the exception that methods can report when they need to report
       some exception, but the exception doesn't fit into any other standard
       exception, and in fact the only reasonable way for a client to react to the
       exception is to display the message(s) to a human.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Error'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        self.messages = messages
        self.data = data
        VapiError.__init__(self)

Error._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.error', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Error))



class Unsupported(Error):
    """
    The ``Unsupported`` exception indicates that the method is not supported by
    the class. 
    
     Examples: 
    
    * Trying to hot-plug a CPU when the current configuration of the VM does
      not support hot-plugging of CPUs.
    * Trying to change the memory size to a value that is not within the
      acceptable guest memory bounds supported by the virtual machine's host.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Unsupported'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

Unsupported._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.unsupported', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Unsupported))



class UnexpectedInput(Error):
    """
    The ``UnexpectedInput`` exception indicates that the request contained a
    parameter or attribute whose name is not known by the server. 
    
    Every method expects parameters with known names. Some of those parameters
    may be (or contain) classes, and the method expects those classes to
    contain attributes with known names. If the method receives parameters or
    attributes with names that is does not expect, this exception may be
    reported. 
    
    This exception can be reported by the API infrastructure for any method,
    but it is specific to the API infrastructure, and should never be reported
    by the implementation of any method. 
    
     Examples: 
    
    * A client using stubs generated from the interface specification for
      version2 of a class invokes the method passing one or more parameters that
      were added in version2, but they are communicating with a server that only
      supports version1 of the class.
    * A client provides an unexpected parameter or attribute name when invoking
      the method using a dynamic interface (for example REST).

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'UnexpectedInput'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

UnexpectedInput._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.unexpected_input', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    UnexpectedInput))



class Unauthorized(Error):
    """
    The ``Unauthorized`` exception indicates that the user is not authorized to
    perform the method. 
    
    API requests may include a security context containing user credentials.
    For example, the user credentials could be a SAML token, a user name and
    password, or the session identifier for a previously established session.
    Invoking the method may require that the user identified by those
    credentials has particular privileges on the method or on one or more
    resource identifiers passed to the method. 
    
     Examples: 
    
    * The method requires that the user have one or more privileges on the
      method, but the user identified by the credentials in the security context
      does not have the required privileges.
    * The method requires that the user have one or more privileges on a
      resource identifier passed to the method, but the user identified by the
      credentials in the security context does not have the required privileges.
    
     
    
     
    
     Counterexamples: 
    
    * The SAML token in the request's security context has expired. A
      :class:`Unauthenticated` exception would be used instead.
    * The user name and password in the request's security context are invalid.
      The :class:`Unauthenticated` exception would be used instead.
    * The session identifier in the request's security context identifies a
      session that has expired. The :class:`Unauthenticated` exception would be
      used instead.
    
     
    
    For security reasons, the :attr:`Error.data` attribute in this exception is
    None, and the :attr:`Error.messages` attribute in this exception does not
    disclose why the user is not authorized to perform the method. For example
    the messages would not disclose which privilege the user did not have or
    which resource identifier the user did not have the required privilege to
    access. The API documentation should indicate what privileges are required.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Unauthorized'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

Unauthorized._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.unauthorized', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Unauthorized))



class Unauthenticated(Error):
    """
    The ``Unauthenticated`` exception indicates that the method requires
    authentication and the user is not authenticated. 
    
    API requests may include a security context containing user credentials.
    For example, the user credentials could be a SAML token, a user name and
    password, or the session identifier for a previously established session. 
    
     Examples: 
    
    * The SAML token in the request's security context has expired.
    * The user name and password in the request's security context are invalid.
    * The session identifier in the request's security context identifies a
      session that has expired.
    
     Counterexamples: 
    
    * The user is authenticated but isn't authorized to perform the requested
      method. The :class:`Unauthorized` exception would be used instead.
    
     
    
    For security reasons, the :attr:`Error.data` attribute in this exception is
    None, and the :attr:`Error.messages` attribute in this exception does not
    disclose which part of the security context is correct or incorrect. For
    example the messages would not disclose whether a username or a password is
    valid or invalid, but only that a combination of username and password is
    invalid.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Unauthenticated'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

Unauthenticated._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.unauthenticated', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Unauthenticated))



class UnableToAllocateResource(Error):
    """
    The ``UnableToAllocateResource`` exception indicates that the method failed
    because it was unable to allocate or acquire a required resource. 
    
     Examples: 
    
    * Trying to power on a virtual machine when there are not enough licenses
      to do so.
    * Trying to power on a virtual machine that would violate a resource usage
      policy.
    
     
    
     Counterexamples: 
    
    * Trying to power off a virtual machine that is in the process of being
      powered on. A :class:`ResourceBusy` exception would be used instead.
    * Trying to remove a VMFS datastore when the is a virtual machine
      registered on any host attached to the datastore. The
      :class:`ResourceInUse` exception would be used instead.
    * Trying to add a virtual switch if the physical network adapter being
      bridged is already in use. The :class:`ResourceInUse` exception would be
      used instead.
    * Attempt to invoke some method on a virtual machine when the virtual
      machine's configuration file is not accessible (for example due to a
      storage APD condition). The :class:`ResourceInaccessible` exception would
      be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'UnableToAllocateResource'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

UnableToAllocateResource._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.unable_to_allocate_resource', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    UnableToAllocateResource))



class TimedOut(Error):
    """
    The ``TimedOut`` exception indicates that the method did not complete
    within the allowed amount of time. The allowed amount of time might be: 
    
    * provided by the client as an input parameter.
    * a fixed limit of the class implementation that is a documented part of
      the contract of the class.
    * a configurable limit used by the implementation of the class.
    * a dynamic limit computed by the implementation of the class.
    
    The method may or may not complete after the ``TimedOut`` exception was
    reported. 
    
     Examples: 
    
    * The method was unable to complete within the timeout duration specified
      by a parameter of the method.
    
     
    
     Counterexamples: 
    
    * A server implementation that puts requests into a queue before
      dispatching them might delete a request from the queue if it doesn't get
      dispatched within *n* minutes. The :class:`ServiceUnavailable` exception
      would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'TimedOut'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

TimedOut._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.timed_out', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    TimedOut))



class ServiceUnavailable(Error):
    """
    The ``ServiceUnavailable`` exception indicates that the class is
    unavailable. 
    
     Examples: 
    
    * Attempt to invoke a method when the server is too busy.
    * Attempt to invoke a method when the server is undergoing maintenance.
    * An method fails to contact VMware Tools running inside the virtual
      machine.
    
     
    
     Counterexamples: 
    
    * A client provides an invalid service or operation identifier when
      invoking the method using a dynamic interface (for example REST). The
      :class:`OperationNotFound` exception would be used instead.
    * A client invokes the method from the class, but that class has not been
      installed. The :class:`OperationNotFound` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'ServiceUnavailable'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

ServiceUnavailable._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.service_unavailable', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ServiceUnavailable))



class ResourceInaccessible(Error):
    """
    The ``ResourceInaccessible`` exception indicates that the method could not
    be completed because an entity is not accessible. 
    
     Examples: 
    
    * Attempt to invoke some method on a virtual machine when the virtual
      machine's configuration file is not accessible (for example due to a
      storage APD condition).
    
     
    
     Counterexamples: 
    
    * Attempt to invoke some method when the server is too busy. The
      :class:`ServiceUnavailable` exception would be used instead.
    * Attempt to invoke some method when the server is undergoing maintenance.
      The :class:`ServiceUnavailable` exception would be used instead.
    * Some method fails to contact VMware Tools running inside the virtual
      machine. The :class:`ServiceUnavailable` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'ResourceInaccessible'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

ResourceInaccessible._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.resource_inaccessible', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ResourceInaccessible))



class ResourceInUse(Error):
    """
    The ``ResourceInUse`` exception indicates that the method could not be
    completed because a resource is in use. 
    
     Examples: 
    
    * Trying to remove a VMFS datastore when the is a virtual machine
      registered on any host attached to the datastore.
    * Trying to add a virtual switch if the physical network adapter being
      bridged is already in use.
    
     
    
     Counterexamples: 
    
    * Trying to power off a virtual machine that is in the process of being
      powered on. The :class:`ResourceBusy` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'ResourceInUse'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

ResourceInUse._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.resource_in_use', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ResourceInUse))



class ResourceBusy(Error):
    """
    The ``ResourceBusy`` exception indicates that the method could not be
    completed because a resource it needs is busy. 
    
     Examples: 
    
    * Trying to power off a virtual machine that is in the process of being
      powered on.
    
     
    
     Counterexamples: 
    
    * Trying to remove a VMFS datastore when there is a virtual machine
      registered on any host attached to the datastore. The
      :class:`ResourceInUse` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'ResourceBusy'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

ResourceBusy._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.resource_busy', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ResourceBusy))



class OperationNotFound(Error):
    """
    The ``OperationNotFound`` exception indicates that the method specified in
    the request could not be found. 
    
    Every API request specifies a service identifier and an operation
    identifier along with the parameters. If the API infrastructure is unable
    to find the requested class or method it reports this exception. 
    
    This exception can be reported by the API infrastructure for any method,
    but it is specific to the API infrastructure, and should never be reported
    by the implementation of any method. 
    
     Examples: 
    
    * A client provides an invalid service or operation identifier when
      invoking the method using a dynamic interface (for example REST).
    * A client invokes the method from a class, but that class has not been
      installed.
    
     
    
     Counterexamples: 
    
    * A client invokes a task scheduling method, but provides an invalid
      service identifier or operation identifier. The :class:`NotFound` exception
      would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'OperationNotFound'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

OperationNotFound._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.operation_not_found', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    OperationNotFound))



class NotFound(Error):
    """
    The ``NotFound`` exception indicates that a specified element could not be
    found. 
    
     Examples: 
    
    * Invoke the method to retrieve information about a virtual machine,
      passing an id that does not identify an existing virtual machine.
    * Invoke the method to modify the configuration of a virtual nic, passing
      an id that does not identify an existing virtual nic in the specified
      virtual machine.
    * Invoke the method to remove a vswitch, passing an id that does not
      identify an existing vswitch.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'NotFound'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

NotFound._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.not_found', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    NotFound))



class NotAllowedInCurrentState(Error):
    """
    The ``NotAllowedInCurrentState`` exception indicates that the requested
    method is not allowed with a resource or service in its current state. This
    could be because the method is performing a configuration change that is
    not allowed in the current state or because method itself is not allowed in
    the current state. 
    
     Examples: 
    
    * Trying to add a virtual device that cannot be hot plugged to a running
      virtual machine.
    * Trying to upgrade the virtual hardware version for a suspended virtual
      machine.
    * Trying to power off, reset, or suspend a virtual machine that is not
      powered on.
    
     
    
     Counterexamples: 
    
    * Trying to power off a virtual machine that is in the process of being
      powered on. The :class:`ResourceBusy` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'NotAllowedInCurrentState'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

NotAllowedInCurrentState._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.not_allowed_in_current_state', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    NotAllowedInCurrentState))



class InvalidRequest(Error):
    """
    The ``InvalidRequest`` exception indicates that the request is malformed in
    such a way that the server is unable to process it. 
    
     Examples: 
    
    * The XML in a SOAP request is not well-formed so the server cannot parse
      the request.
    * The XML in a SOAP request is well-formed but does not match the structure
      required by the SOAP specification.
    * A JSON-RPC request is not valid JSON.
    * The JSON sent in a JSON-RPC request is not a valid JSON-RPC Request
      object.
    * The Request object from a JSON-RPC request does not match the structure
      required by the API infrastructure.
    
     
    
     Counterexamples: 
    
    * The parameter has a value that is not with the required range. The
      :class:`InvalidArgument` exception would be used instead.
    * The name of the method specified in the request doesn't not match any
      known method. The :class:`NotFound` exception would be used instead.
    
     
    
    Some transport protocols (for example JSON-RPC) include their own mechanism
    for reporting these kinds of errors, and the API infrastructure for a
    programming language may expose the errors using a language specific
    mechanism, so this exception might not be used.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidRequest'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidRequest._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.invalid_request', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidRequest))



class InvalidElementType(Error):
    """
    The ``InvalidElementType`` exception indicates that the server was unable
    to fulfil the request because an element of a specific type cannot be a
    member of particular group. 
    
    This exception could be reported, for example, if an attempt is made to put
    an element into the wrong type of container. 
    
     Examples: 
    
    * Attempt to put a virtual machine into a folder that can only contain
      hosts.
    * Attempt to attach a SCSI virtual disk to an IDE port.
    
     Counterexamples: 
    
    * A parameter has a value that is not of the expected type. The
      :class:`InvalidArgument` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidElementType'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidElementType._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.invalid_element_type', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidElementType))



class InvalidElementConfiguration(Error):
    """
    The ``InvalidElementConfiguration`` exception indicates that an attempt to
    modify the configuration of an element or a group containing the element
    failed due to the configuraton of the element. A typical case is when the
    method is am attempt to change the group membership of the element fails,
    in which case a configuration change on the element may allow the group
    membership change to succeed. 
    
     Examples: 
    
    * Attempt to move a host with a fault tolerant virtual machine out of a
      cluster (i.e. make the host a standalone host).
    * Attempt to remove a host from a DRS cluster without putting the host into
      maintenance mode.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidElementConfiguration'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidElementConfiguration._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.invalid_element_configuration', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidElementConfiguration))



class InvalidArgument(Error):
    """
    The ``InvalidArgument`` exception indicates that the values received for
    one or more parameters are not acceptable. 
    
    This exception is reported by the API infrastructure, so it could occur in
    response to the invocation of any method. It may also be reported as the
    result of method-specific validation. 
    
     Examples: 
    
    * A parameter has a value that is not of the expected type.
    * A parameter has a value that is not in the required range.
    * A parameter has a value that is not one of the specifically allowed
      strings.
    * One attribute of a class is the tag for a tagged union, and has a
      specific value but another attribute of the class that is required to be
      specified when the tag has that value is not specified, or another
      attribute of the class that is required to be unspecified when the tag has
      that value is specified.
    
     
    
     Counterexamples: 
    
    * Trying to create a new tag in tag category when a tag with the specified
      name already exists the tag category. The :class:`AlreadyExists` exception
      would be used instead.
    * Invoke the method to retrieve information about a virtual machine,
      passing an id that does not identify an existing virtual machine. The
      :class:`NotFound` exception would be used instead.
    * Attempt to put a virtual machine into a folder that can only contain
      hosts. The :class:`InvalidElementType` exception would be used instead.
    * Attempt to attach a SCSI virtual disk to an IDE port. The
      :class:`InvalidElementType` exception would be used instead.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InvalidArgument'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InvalidArgument._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.invalid_argument', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InvalidArgument))



class InternalServerError(Error):
    """
    The ``InternalServerError`` exception indicates that the server encounters
    an unexpected condition that prevented it from fulfilling the request. 
    
    This exception is reported by the API infrastructure, so it could occur in
    response to the invocation of any method. 
    
     Examples: 
    
    * The method returns a value whose type doesn't match the type type the
      method says it should return.
    * The method reports an exception that is not included in the list of
      exceptions the method says that it can report.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'InternalServerError'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

InternalServerError._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.internal_server_error', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    InternalServerError))



class FeatureInUse(Error):
    """
    The ``FeatureInUse`` exception indicates that an action cannot be completed
    because a feature is in use. 
    
     Examples: 
    
    * Trying to disable snapshots on a virtual machine which has a snapshot.
    * Trying to downgrade a license that has licensed features that are in use.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'FeatureInUse'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

FeatureInUse._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.feature_in_use', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    FeatureInUse))



class ConcurrentChange(Error):
    """
    The ``ConcurrentChange`` exception indicates that a data structure, entity,
    or resource has been modified since some earlier point in time. Typically
    this happens when the client is doing the *write* portion of a
    read-modify-write sequence and indicates that it wants the server to notify
    it if the data in the server has changed after it did the *read*, so that
    it can avoid overwriting that change inadvertantly.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'ConcurrentChange'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

ConcurrentChange._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.concurrent_change', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    ConcurrentChange))



class Canceled(Error):
    """
    The ``Canceled`` exception indicates that the method canceled itself in
    response to an explicit request to do so. Methods being "canceled" for
    other reasons (for example the client connection was closed, a time out
    occured, or due to excessive resource consumption) should not report this
    exception. 
    
     Examples: 
    
    * A user is monitoring the progress of the method in a GUI and sees that it
      is likely to take longer than he is willing to wait and clicks the cancel
      button.
    * A user invokes the method using a command-line tool and decides that she
      didn't really want to invoke that method, and presses CTRL-c.
    
     
    
     Counterexamples: 
    
    * The client's connection to the server was closed. Reporting an exception
      is pointless since the client will not receive the error response because
      the connection has been closed.
    * The request is taking longer than some amount of time. The
      :class:`TimedOut` exception would be reported if the time was specified as
      part of the input or is documented in the API contract.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'Canceled'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

Canceled._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.canceled', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    Canceled))



class AlreadyInDesiredState(Error):
    """
    The ``AlreadyInDesiredState`` exception indicates that an attempt to change
    the state of a resource or service had no effect because the resource or
    service is already in the desired state. 
    
     Examples: 
    
    * Trying to power on a virtual machine that is already powered on.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'AlreadyInDesiredState'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

AlreadyInDesiredState._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.already_in_desired_state', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    AlreadyInDesiredState))



class AlreadyExists(Error):
    """
    The ``AlreadyExists`` exception indicates that an attempt was made to
    create an entity but the entity already exists. Typically the entity has a
    name or identifier that is required to be unique in some context, but there
    is already an entity with that name or identifier in that context. 
    
     Examples: 
    
    * Trying to create a new tag category when a tag category with the
      specified name already exists.
    * Trying to create a new tag in tag category when a tag with the specified
      name already exists the tag category.
    * Trying to create a LUN with a specific UUID on a node (for replication
      purposes) when a LUN with that UUID already exists on the node.
    * Trying to create a file in a directory or move or copy a file to a
      directory when a file with that name already exists in the directory.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """

    _qualname = 'AlreadyExists'

    def __init__(self,
                 messages=None,
                 data=None,
                ):
        """
        :type  messages: :class:`list` of :class:`com.vmware.vapi.std_client.LocalizableMessage`
        :param messages: Stack of one or more localizable messages for human exception
            consumers. 
            
            The message at the top of the stack (first in the list) describes
            the exception from the perspective of the method the client
            invoked. Each subsequent message in the stack describes the "cause"
            of the prior message.
        :type  data: :class:`vmware.vapi.struct.VapiStruct` or ``None``
        :param data: Data to facilitate clients responding to the method reporting a
            standard exception to indicating that it was unable to complete
            successfully. 
            
            Methods may provide data that clients can use when responding to
            exceptions. Since the data that clients need may be specific to the
            context of the method reporting the exception, different methods
            that report the same exception may provide different data in the
            exception. The documentation for each each method will describe
            what, if any, data it provides for each exception it reports. The
            :class:`ArgumentLocations`, :class:`FileLocations`, and
            :class:`TransientIndication` classes are intended as possible
            values for this attribute.
            :class:`com.vmware.vapi.std_client.DynamicID` may also be useful as
            a value for this attribute (although that is not its primary
            purpose). Some classes may provide their own specific classes for
            use as the value of this attribute when reporting exceptions from
            their methods.
            Some methods will not set this attribute when reporting exceptions.
        """

        Error.__init__(
            self,
            messages=messages,
            data=data,
        )

AlreadyExists._set_binding_type(type.ErrorType(
    'com.vmware.vapi.std.errors.already_exists', {
        'messages': type.ListType(type.ReferenceType('com.vmware.vapi.std_client', 'LocalizableMessage')),
        'data': type.OptionalType(type.DynamicStructType('vmware.vapi.dynamic_struct', {}, VapiStruct)),
    },
    AlreadyExists))




class StubFactory(StubFactoryBase):
    _attrs = {
    }

