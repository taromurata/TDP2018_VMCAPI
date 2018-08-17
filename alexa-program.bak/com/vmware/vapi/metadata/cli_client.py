# -*- coding: utf-8 -*-
#---------------------------------------------------------------------------
# Copyright 2018 VMware, Inc.  All rights reserved.

# AUTO GENERATED FILE -- DO NOT MODIFY!
#
# vAPI stub file for package com.vmware.vapi.metadata.cli.
#---------------------------------------------------------------------------

"""
The ``com.vmware.vapi.metadata.cli_client`` module provides classes that expose
all the information required to display namespace or command help, execute a
command and display it's result.

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
    The ``ComponentInfo`` is an aggregated class for CLI commands and
    namespaces information.

    .. tip::
        The arguments are used to initialize data attributes with the same
        names.
    """




    def __init__(self,
                 namespaces=None,
                 commands=None,
                ):
        """
        :type  namespaces: :class:`list` of :class:`Namespace.Info`
        :param namespaces: Information for all CLI namespaces of a component
        :type  commands: :class:`list` of :class:`Command.Info`
        :param commands: Information for all CLI commands of a component
        """
        self.namespaces = namespaces
        self.commands = commands
        VapiStruct.__init__(self)

ComponentInfo._set_binding_type(type.StructType(
    'com.vmware.vapi.metadata.cli.component_info', {
        'namespaces': type.ListType(type.ReferenceType(__name__, 'Namespace.Info')),
        'commands': type.ListType(type.ReferenceType(__name__, 'Command.Info')),
    },
    ComponentInfo,
    False,
    None))



class Command(VapiInterface):
    """
    The ``Command`` class provides methods to get information about command
    line interface (CLI) commands.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _CommandStub)

    class FormatterType(Enum):
        """
        The ``Command.FormatterType`` class defines supported CLI output formatter
        types. See :attr:`Command.Info.formatter`.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        SIMPLE = None
        """
        Displays command output as it is.

        """
        TABLE = None
        """
        Displays command output in table format.

        """
        JSON = None
        """
        Displays command output in JSON format.

        """
        XML = None
        """
        Displays command output in XML format.

        """
        CSV = None
        """
        Displays command output in CSV format.

        """
        HTML = None
        """
        Displays command output in HTML format.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`FormatterType` instance.
            """
            Enum.__init__(string)

    FormatterType._set_values([
        FormatterType('SIMPLE'),
        FormatterType('TABLE'),
        FormatterType('JSON'),
        FormatterType('XML'),
        FormatterType('CSV'),
        FormatterType('HTML'),
    ])
    FormatterType._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.cli.command.formatter_type',
        FormatterType))


    class GenericType(Enum):
        """
        The ``Command.GenericType`` class defines generic types supported by
        ``Command`` class. See :attr:`Command.OptionInfo.generic`.

        .. note::
            This class represents an enumerated type in the interface language
            definition. The class contains class attributes which represent the
            values in the current version of the enumerated type. Newer versions of
            the enumerated type may contain new values. To use new values of the
            enumerated type in communication with a server that supports the newer
            version of the API, you instantiate this class. See :ref:`enumerated
            type description page <enumeration_description>`.
        """
        NONE = None
        """
        Default case.

        """
        OPTIONAL = None
        """
        Input parameter is an optional.

        """
        LIST = None
        """
        Input parameter is a list.

        """
        OPTIONAL_LIST = None
        """
        Input parameter is an optional of type list.

        """
        LIST_OPTIONAL = None
        """
        Input parameter is a list of optionals.

        """

        def __init__(self, string):
            """
            :type  string: :class:`str`
            :param string: String value for the :class:`GenericType` instance.
            """
            Enum.__init__(string)

    GenericType._set_values([
        GenericType('NONE'),
        GenericType('OPTIONAL'),
        GenericType('LIST'),
        GenericType('OPTIONAL_LIST'),
        GenericType('LIST_OPTIONAL'),
    ])
    GenericType._set_binding_type(type.EnumType(
        'com.vmware.vapi.metadata.cli.command.generic_type',
        GenericType))


    class OutputFieldInfo(VapiStruct):
        """
        The ``Command.OutputFieldInfo`` class describes the name used by the CLI to
        display a single attribute of a class element in the interface definition
        language.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     field_name=None,
                     display_name=None,
                    ):
            """
            :type  field_name: :class:`str`
            :param field_name: Name of the attribute.
            :type  display_name: :class:`str`
            :param display_name: Name used by the CLI to display the attribute.
            """
            self.field_name = field_name
            self.display_name = display_name
            VapiStruct.__init__(self)

    OutputFieldInfo._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.command.output_field_info', {
            'field_name': type.StringType(),
            'display_name': type.StringType(),
        },
        OutputFieldInfo,
        False,
        None))


    class OutputInfo(VapiStruct):
        """
        The ``Command.OutputInfo`` class describes the names used by the CLI to
        display the attributes of a class element in the interface definition
        language as well as the order in which the attributes will be displayed.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     structure_id=None,
                     output_fields=None,
                    ):
            """
            :type  structure_id: :class:`str`
            :param structure_id: Name of the class.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.structure``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.structure``.
            :type  output_fields: :class:`list` of :class:`Command.OutputFieldInfo`
            :param output_fields: The order in which the attributes of the class will be displayed by
                the CLI as well as the names used to display the attributes.
            """
            self.structure_id = structure_id
            self.output_fields = output_fields
            VapiStruct.__init__(self)

    OutputInfo._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.command.output_info', {
            'structure_id': type.IdType(resource_types='com.vmware.vapi.structure'),
            'output_fields': type.ListType(type.ReferenceType(__name__, 'Command.OutputFieldInfo')),
        },
        OutputInfo,
        False,
        None))


    class OptionInfo(VapiStruct):
        """
        The ``Command.OptionInfo`` class describes information about a specific
        input option of a command.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     long_option=None,
                     short_option=None,
                     field_name=None,
                     description=None,
                     type=None,
                     generic=None,
                    ):
            """
            :type  long_option: :class:`str`
            :param long_option: The long option name of the parameter as used by the user.
            :type  short_option: :class:`str` or ``None``
            :param short_option: The single character value option name.
                If not present, there's no single character option for the
                parameter.
            :type  field_name: :class:`str`
            :param field_name: The fully qualified name of the option referred to by the operation
                element in :attr:`Command.Info.operation_id`.
            :type  description: :class:`str`
            :param description: The description of the option to be displayed to the user when they
                request usage information for a CLI command.
            :type  type: :class:`str`
            :param type: The type of option. This is used to display information about what
                kind of data is expected (string, number, boolean, etc.) for the
                option when they request usage information for a CLI command. For
                class this stores the fully qualified class id.
            :type  generic: :class:`Command.GenericType`
            :param generic: This is used to tell the user whether the option is required or
                optional, or whether they can specify the option multiple times.
            """
            self.long_option = long_option
            self.short_option = short_option
            self.field_name = field_name
            self.description = description
            self.type = type
            self.generic = generic
            VapiStruct.__init__(self)

    OptionInfo._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.command.option_info', {
            'long_option': type.StringType(),
            'short_option': type.OptionalType(type.StringType()),
            'field_name': type.StringType(),
            'description': type.StringType(),
            'type': type.StringType(),
            'generic': type.ReferenceType(__name__, 'Command.GenericType'),
        },
        OptionInfo,
        False,
        None))


    class Identity(VapiStruct):
        """
        The ``Command.Identity`` class uniquely identifies a command in the CLI
        commands tree.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     path=None,
                     name=None,
                    ):
            """
            :type  path: :class:`str`
            :param path: The dot-separated path of the namespace containing the command in
                the CLI command tree.
            :type  name: :class:`str`
            :param name: Name of the command.
            """
            self.path = path
            self.name = name
            VapiStruct.__init__(self)

    Identity._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.command.identity', {
            'path': type.StringType(),
            'name': type.StringType(),
        },
        Identity,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Command.Info`` class contains information about a command. It
        includes the identity of the command, a description, information about the
        class and method that implement the command, and CLI-specific information
        for the command.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     identity=None,
                     description=None,
                     service_id=None,
                     operation_id=None,
                     options=None,
                     formatter=None,
                     output_field_list=None,
                    ):
            """
            :type  identity: :class:`Command.Identity`
            :param identity: Basic command identity.
            :type  description: :class:`str`
            :param description: The text description displayed to the user in help output.
            :type  service_id: :class:`str`
            :param service_id: The service identifier that contains the operations for this CLI
                command.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.service``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.service``.
            :type  operation_id: :class:`str`
            :param operation_id: The operation identifier corresponding to this CLI command.
                When clients pass a value of this class as a parameter, the
                attribute must be an identifier for the resource type:
                ``com.vmware.vapi.operation``. When methods return a value of this
                class as a return value, the attribute will be an identifier for
                the resource type: ``com.vmware.vapi.operation``.
            :type  options: :class:`list` of :class:`Command.OptionInfo`
            :param options: The input for this command.
            :type  formatter: :class:`Command.FormatterType` or ``None``
            :param formatter: The formatter to use when displaying the output of this command.
                If not present, client can choose a default output formatter.
            :type  output_field_list: :class:`list` of :class:`Command.OutputInfo`
            :param output_field_list: List of output structure name and output field info.
            """
            self.identity = identity
            self.description = description
            self.service_id = service_id
            self.operation_id = operation_id
            self.options = options
            self.formatter = formatter
            self.output_field_list = output_field_list
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.command.info', {
            'identity': type.ReferenceType(__name__, 'Command.Identity'),
            'description': type.StringType(),
            'service_id': type.IdType(resource_types='com.vmware.vapi.service'),
            'operation_id': type.IdType(resource_types='com.vmware.vapi.operation'),
            'options': type.ListType(type.ReferenceType(__name__, 'Command.OptionInfo')),
            'formatter': type.OptionalType(type.ReferenceType(__name__, 'Command.FormatterType')),
            'output_field_list': type.ListType(type.ReferenceType(__name__, 'Command.OutputInfo')),
        },
        Info,
        False,
        None))



    def list(self,
             path=None,
             ):
        """
        Returns the identifiers of all commands, or commands in a specific
        namespace.

        :type  path: :class:`str` or ``None``
        :param path: The dot-separated path of the namespace for which command
            identifiers should be returned.
            If None identifiers of all commands registered with the
            infrastructure will be returned.
        :rtype: :class:`list` of :class:`Command.Identity`
        :return: Identifiers of the requested commands.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a namespace corresponding to ``path`` doesn't exist.
        """
        return self._invoke('list',
                            {
                            'path': path,
                            })

    def get(self,
            identity,
            ):
        """
        Retrieves information about a command including information about how
        to execute that command.

        :type  identity: :class:`Command.Identity`
        :param identity: Identifier of the command for which to retreive information.
        :rtype: :class:`Command.Info`
        :return: Information about the command including information about how to
            execute that command.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a command corresponding to ``identity`` doesn't exist.
        """
        return self._invoke('get',
                            {
                            'identity': identity,
                            })

    def fingerprint(self):
        """
        Returns the aggregate fingerprint of all the command metadata from all
        the metadata sources. 
        
        The fingerprint provides clients an efficient way to check if the
        metadata for commands has been modified on the server.


        :rtype: :class:`str`
        :return: Fingerprint of all the command metadata present on the server.
        """
        return self._invoke('fingerprint', None)
class Namespace(VapiInterface):
    """
    The ``Namespace`` class provides methods to get information about command
    line interface (CLI) namespaces.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _NamespaceStub)

    class Identity(VapiStruct):
        """
        The ``Namespace.Identity`` class uniquely identifies a namespace in the CLI
        namespace tree.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     path=None,
                     name=None,
                    ):
            """
            :type  path: :class:`str`
            :param path: The dot-separated path of the namespace containing the namespace in
                the CLI node tree. For top-level namespace this will be empty.
            :type  name: :class:`str`
            :param name: The name displayed to the user for this namespace.
            """
            self.path = path
            self.name = name
            VapiStruct.__init__(self)

    Identity._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.namespace.identity', {
            'path': type.StringType(),
            'name': type.StringType(),
        },
        Identity,
        False,
        None))


    class Info(VapiStruct):
        """
        The ``Namespace.Info`` class contains information about a namespace. It
        includes the identity of the namespace, a description, information children
        namespaces.

        .. tip::
            The arguments are used to initialize data attributes with the same
            names.
        """




        def __init__(self,
                     identity=None,
                     description=None,
                     children=None,
                    ):
            """
            :type  identity: :class:`Namespace.Identity`
            :param identity: Basic namespace identity.
            :type  description: :class:`str`
            :param description: The text description displayed to the user in help output.
            :type  children: :class:`list` of :class:`Namespace.Identity`
            :param children: The children of this namespace in the tree of CLI namespaces.
            """
            self.identity = identity
            self.description = description
            self.children = children
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.namespace.info', {
            'identity': type.ReferenceType(__name__, 'Namespace.Identity'),
            'description': type.StringType(),
            'children': type.ListType(type.ReferenceType(__name__, 'Namespace.Identity')),
        },
        Info,
        False,
        None))



    def list(self):
        """
        Returns the identifiers of all namespaces registered with the
        infrastructure.


        :rtype: :class:`list` of :class:`Namespace.Identity`
        :return: Identifiers of all the namespaces.
        """
        return self._invoke('list', None)

    def get(self,
            identity,
            ):
        """
        Retreives information about a namespace including information about
        children of that namespace.

        :type  identity: :class:`Namespace.Identity`
        :param identity: Identifier of the namespace for which to retreive information.
        :rtype: :class:`Namespace.Info`
        :return: Information about the namespace including information about child
            of that namespace.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            if a namespace corresponding to ``identity`` doesn't exist.
        """
        return self._invoke('get',
                            {
                            'identity': identity,
                            })

    def fingerprint(self):
        """
        Returns the aggregate fingerprint of all the namespace metadata from
        all the metadata sources. 
        
        The fingerprint provides clients an efficient way to check if the
        metadata for namespaces has been modified on the server.


        :rtype: :class:`str`
        :return: Fingerprint of all the namespace metadata present on the server.
        """
        return self._invoke('fingerprint', None)
class Source(VapiInterface):
    """
    The ``Source`` class provides methods to manage the sources of command line
    interface (CLI) metadata information. 
    
    The interface definition language infrastructure provides tools to generate
    various kinds of metadata in JSON format from the interface definition
    files and additional properties files. One of the generated files contains
    CLI information. 
    
    A CLI metadata file contains information about one component element. When
    a CLI metadata file is added as a source, each source contributes only one
    component element's metadata. 
    
    CLI metadata can also be discovered from a remote server that supports the
    CLI metadata services (see :mod:`com.vmware.vapi.metadata.cli_client`)
    module. Since multiple components can be registered with a single metadata
    server, when a remote server is registered as a source, that source can
    contribute more than one component.
    """


    def __init__(self, config):
        """
        :type  config: :class:`vmware.vapi.bindings.stub.StubConfiguration`
        :param config: Configuration to be used for creating the stub.
        """
        VapiInterface.__init__(self, config, _SourceStub)

    class Info(VapiStruct):
        """
        The ``Source.Info`` class contains the metadata source information.

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
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: The type (FILE, REMOTE) of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the CLI metadata file that has the CLI
                information about one component. The ``filepath`` is the path to
                the file in the server's filesystem.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information for the remote server. This should be in the
                format http(s)://IP:port/namespace. 
                
                The remote server must contain the classes in the
                :mod:`com.vmware.vapi.metadata.cli_client` module. It must expose
                CLI information of one or more components.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    Info._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.source.info', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        Info,
        False,
        None))


    class CreateSpec(VapiStruct):
        """
        The ``Source.CreateSpec`` class contains the registration information of a
        CLI source.

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
            :type  type: :class:`com.vmware.vapi.metadata_client.SourceType`
            :param type: Type of the metadata source.
            :type  filepath: :class:`str`
            :param filepath: Absolute file path of the metamodel metadata file that has the
                metamodel information about one component element.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.FILE`.
            :type  address: :class:`str`
            :param address: Connection information of the remote server. This should be of the
                format http(s)://IP:port/namespace. 
                
                The remote server should contain the classes in
                :mod:`com.vmware.vapi.metadata.metamodel_client` module. It could
                expose metamodel information of one or more components.
                This attribute is optional and it is only relevant when the value
                of ``type`` is
                :attr:`com.vmware.vapi.metadata_client.SourceType.REMOTE`.
            """
            self.description = description
            self.type = type
            self.filepath = filepath
            self.address = address
            VapiStruct.__init__(self)

    CreateSpec._set_binding_type(type.StructType(
        'com.vmware.vapi.metadata.cli.source.create_spec', {
            'description': type.StringType(),
            'type': type.ReferenceType('com.vmware.vapi.metadata_client', 'SourceType'),
            'filepath': type.OptionalType(type.StringType()),
            'address': type.OptionalType(type.URIType()),
        },
        CreateSpec,
        False,
        None))



    def create(self,
               source_id,
               spec,
               ):
        """
        Creates a new metadata source. Once the server validates the
        registration information of the metadata source, the CLI metadata is
        retrieved from the source. This populates elements in all the classes
        defined in :mod:`com.vmware.vapi.metadata.cli_client` module.

        :type  source_id: :class:`str`
        :param source_id: metadata source identifier.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :type  spec: :class:`Source.CreateSpec`
        :param spec: create specification.
        :raise: :class:`com.vmware.vapi.std.errors_client.AlreadyExists` 
            If the metadata source identifier is already registered with the
            infrastructure.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If type of the source specified in null is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the file specified in null is not a valid JSON file or if the
            format of the CLI metadata in the JSON file is invalid.
        :raise: :class:`com.vmware.vapi.std.errors_client.InvalidArgument` 
            If the URI specified in null is unreachable or if there is a
            transport protocol or message protocol mismatch between the client
            and the server or if the remote server do not have classes present
            in :mod:`com.vmware.vapi.metadata.cli_client` module.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the file specified in null does not exist.
        """
        return self._invoke('create',
                            {
                            'source_id': source_id,
                            'spec': spec,
                            })

    def delete(self,
               source_id,
               ):
        """
        Deletes an existing CLI metadata source from the infrastructure.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the metadata source identifier is not found.
        """
        return self._invoke('delete',
                            {
                            'source_id': source_id,
                            })

    def get(self,
            source_id,
            ):
        """
        Retrieves information about the metadata source corresponding to
        ``source_id``.

        :type  source_id: :class:`str`
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
        :rtype: :class:`Source.Info`
        :return: The :class:`Source.Info` instance that corresponds to ``source_id``
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the metadata source identifier is not found.
        """
        return self._invoke('get',
                            {
                            'source_id': source_id,
                            })

    def list(self):
        """
        Returns the identifiers of the metadata sources currently registered
        with the infrastructure.


        :rtype: :class:`list` of :class:`str`
        :return: The list of identifiers for metadata sources currently registered.
            The return value will contain identifiers for the resource type:
            ``com.vmware.vapi.metadata.source``.
        """
        return self._invoke('list', None)

    def reload(self,
               source_id=None,
               ):
        """
        Reloads the CLI metadata from all the metadata sources or of a
        particular metadata source if ``source_id`` is specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
            If unspecified, all the metadata sources are reloaded.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the metadata source identifier is not found.
        """
        return self._invoke('reload',
                            {
                            'source_id': source_id,
                            })

    def fingerprint(self,
                    source_id=None,
                    ):
        """
        Returns the aggregate fingerprint of metadata from all the metadata
        sources or from a particular metadata source if ``source_id`` is
        specified.

        :type  source_id: :class:`str` or ``None``
        :param source_id: Identifier of the metadata source.
            The parameter must be an identifier for the resource type:
            ``com.vmware.vapi.metadata.source``.
            If unspecified, the fingerprint of all the metadata sources is
            returned.
        :rtype: :class:`str`
        :return: Aggregate fingerprint of all the metadata sources or of a
            particular metadata source.
        :raise: :class:`com.vmware.vapi.std.errors_client.NotFound` 
            If the metadata source identifier is not found.
        """
        return self._invoke('fingerprint',
                            {
                            'source_id': source_id,
                            })
class _CommandStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {
            'path': type.OptionalType(type.StringType()),
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

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'identity': type.ReferenceType(__name__, 'Command.Identity'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {})
        fingerprint_error_dict = {}
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Command.Identity')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Command.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.cli.command',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _NamespaceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'identity': type.ReferenceType(__name__, 'Namespace.Identity'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {})
        fingerprint_error_dict = {}
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.ReferenceType(__name__, 'Namespace.Identity')),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Namespace.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'list': list_rest_metadata,
            'get': get_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.cli.namespace',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)

class _SourceStub(ApiInterfaceStub):
    def __init__(self, config):
        # properties for create operation
        create_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
            'spec': type.ReferenceType(__name__, 'Source.CreateSpec'),
        })
        create_error_dict = {
            'com.vmware.vapi.std.errors.already_exists':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'AlreadyExists'),
            'com.vmware.vapi.std.errors.invalid_argument':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'InvalidArgument'),
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        create_input_value_validator_list = [
        ]
        create_output_validator_list = [
        ]
        create_rest_metadata = None

        # properties for delete operation
        delete_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
        })
        delete_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        delete_input_value_validator_list = [
        ]
        delete_output_validator_list = [
        ]
        delete_rest_metadata = None

        # properties for get operation
        get_input_type = type.StructType('operation-input', {
            'source_id': type.IdType(resource_types='com.vmware.vapi.metadata.source'),
        })
        get_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        get_input_value_validator_list = [
        ]
        get_output_validator_list = [
        ]
        get_rest_metadata = None

        # properties for list operation
        list_input_type = type.StructType('operation-input', {})
        list_error_dict = {}
        list_input_value_validator_list = [
        ]
        list_output_validator_list = [
        ]
        list_rest_metadata = None

        # properties for reload operation
        reload_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        reload_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        reload_input_value_validator_list = [
        ]
        reload_output_validator_list = [
        ]
        reload_rest_metadata = None

        # properties for fingerprint operation
        fingerprint_input_type = type.StructType('operation-input', {
            'source_id': type.OptionalType(type.IdType()),
        })
        fingerprint_error_dict = {
            'com.vmware.vapi.std.errors.not_found':
                type.ReferenceType('com.vmware.vapi.std.errors_client', 'NotFound'),

        }
        fingerprint_input_value_validator_list = [
        ]
        fingerprint_output_validator_list = [
        ]
        fingerprint_rest_metadata = None

        operations = {
            'create': {
                'input_type': create_input_type,
                'output_type': type.VoidType(),
                'errors': create_error_dict,
                'input_value_validator_list': create_input_value_validator_list,
                'output_validator_list': create_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'delete': {
                'input_type': delete_input_type,
                'output_type': type.VoidType(),
                'errors': delete_error_dict,
                'input_value_validator_list': delete_input_value_validator_list,
                'output_validator_list': delete_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'get': {
                'input_type': get_input_type,
                'output_type': type.ReferenceType(__name__, 'Source.Info'),
                'errors': get_error_dict,
                'input_value_validator_list': get_input_value_validator_list,
                'output_validator_list': get_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'list': {
                'input_type': list_input_type,
                'output_type': type.ListType(type.IdType()),
                'errors': list_error_dict,
                'input_value_validator_list': list_input_value_validator_list,
                'output_validator_list': list_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'reload': {
                'input_type': reload_input_type,
                'output_type': type.VoidType(),
                'errors': reload_error_dict,
                'input_value_validator_list': reload_input_value_validator_list,
                'output_validator_list': reload_output_validator_list,
                'task_type': TaskType.NONE,
            },
            'fingerprint': {
                'input_type': fingerprint_input_type,
                'output_type': type.StringType(),
                'errors': fingerprint_error_dict,
                'input_value_validator_list': fingerprint_input_value_validator_list,
                'output_validator_list': fingerprint_output_validator_list,
                'task_type': TaskType.NONE,
            },
        }
        rest_metadata = {
            'create': create_rest_metadata,
            'delete': delete_rest_metadata,
            'get': get_rest_metadata,
            'list': list_rest_metadata,
            'reload': reload_rest_metadata,
            'fingerprint': fingerprint_rest_metadata,
        }
        ApiInterfaceStub.__init__(
            self, iface_name='com.vmware.vapi.metadata.cli.source',
            config=config, operations=operations, rest_metadata=rest_metadata,
            is_vapi_rest=True)


class StubFactory(StubFactoryBase):
    _attrs = {
        'Command': Command,
        'Namespace': Namespace,
        'Source': Source,
    }

