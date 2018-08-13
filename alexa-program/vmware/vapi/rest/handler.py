# -*- coding: utf-8 -*-
"""
REST Handler for WSGI application
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015-2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import base64
import collections
import decimal
import json
import six
import werkzeug

from com.vmware.vapi.metadata.metamodel_client import (
    Component, Structure, Type, Enumeration, GenericInstantiation)
from vmware.vapi.bindings.task_helper import get_task_operation_name
from vmware.vapi.common.context import set_context, clear_context
from vmware.vapi.core import ExecutionContext
from vmware.vapi.data.serializers.cleanjson import DataValueConverter
from vmware.vapi.data.type import Type as DataType
from vmware.vapi.data.value import (
    data_value_factory, ListValue, StructValue,
    StringValue, OptionalValue, VoidValue, SecretValue)
from vmware.vapi.lib.constants import (
    MAP_ENTRY, OPERATION_INPUT, RestAnnotations, TASK_REST_QUERY_PARAM)
from vmware.vapi.lib.context import create_default_application_context
from vmware.vapi.lib.load import dynamic_import_list
from vmware.vapi.lib.log import get_vapi_logger
from vmware.vapi.protocol.client.local_connector import get_local_connector
from vmware.vapi.security.session import (
    REST_SESSION_ID_KEY, REQUIRE_HEADER_AUTHN)
from vmware.vapi.stdlib.client.factories import StubConfigurationFactory

from .lib import vapi_to_http_error_map
from .rules import RoutingRuleGenerator

logger = get_vapi_logger(__name__)

# Mapping from HTTP method to operation name. The actual
# operation name might change based on ID parameters in the URL.
# Since GET is mapped to both list() and get(<>) operations,
# this map will return list as operation name and if the HTTP
# request has identifier arguments, then 'get' operation
# identifier should be used instead of 'list'.
http_method_map = {
    'GET': 'list',
    'PATCH': 'update',
    'DELETE': 'delete',
    'POST': 'create',
    'PUT': 'set',
    'HEAD': 'get'
}

# Mapping from vAPI operation identifier to HTTP method
vapi_method_map = dict((v, k) for k, v in six.iteritems(http_method_map))


class MetadataStore(object):
    """
    Helper class to process the metamodel metadata and
    provide a convenient way to access the data.
    """

    class OperationSummary(object):
        """
        Helper class to contain only useful metamodel metadata of an operation
        """
        def __init__(self, param_info_map, path_variables_map=None,
                     request_mapping_metadata=None):
            """
            :type  param_info_map:
                :class:`collections.OrderedDict` of :class:`str` and
                :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
            :param param_info_map: Map of parameter name to its metamodel
                metadata
            :type  path_variables_map: :class:`dict` of :class:`str` and
                :class:`str`
            :param path_variables_map: Map of path variable name to canonical
                name of the parameters that have the PathVariable annotation
            :type  request_mapping_metadata:
                :class:`com.vmware.vapi.metadata.metamodel_provider.ElementMap`
            :param request_mapping_metadata: Metamodel metadata of
                RequestMapping annotation on the operation
            """
            self.param_info_map = param_info_map
            self.path_variables_map = path_variables_map
            self.request_mapping_metadata = request_mapping_metadata

        def has_request_mapping_metadata(self):
            """
            Tells whether this operation has RequestMapping annotation
            """
            return self.request_mapping_metadata is not None

    def __init__(self, api_provider):
        """
        Initialize MetadataStore

        :type  api_provider: :class:`vmware.vapi.core.ApiProvider`
        :param api_provider: ApiProvider to get the metadata
        """
        self.structure_map = {}
        self.enumeration_map = {}
        self.service_map = {}
        self._build(api_provider)

    def _build(self, api_provider):
        """
        Get the metamodel metadata and process it

        :type  api_provider: :class:`vmware.vapi.core.ApiProvider`
        :param api_provider: ApiProvider to get the metadata
        """
        local_connector = get_local_connector(api_provider)
        stub_config = StubConfigurationFactory.new_std_configuration(
            local_connector)
        component_svc = Component(stub_config)
        components = component_svc.list()
        for component_id in components:
            component_data = component_svc.get(component_id)
            self._process_component_info(component_data.info)

    def _process_component_info(self, component_info):
        """
        Process the metamodel component information. Scan the packages
        for services, structures and enumerations and store into dictionaries
        for fast lookup.

        :type  component_info:
               :class:`com.vmware.vapi.metadata.metamodel_client.ComponentInfo`
        :param component_info: Metamodel component information to be processed
        """
        for package_info in six.itervalues(component_info.packages):
            for structure_id, structure_info in six.iteritems(
                                                package_info.structures):
                self._process_structure_info(structure_id, structure_info)
            for service_id, service_info in six.iteritems(
                                            package_info.services):
                self._process_service_info(service_id, service_info)
            for enumeration_id, enumeration_info in six.iteritems(
                                                    package_info.enumerations):
                self.enumeration_map[enumeration_id] = enumeration_info

    def _create_operation_summary(self, operation_info):
        """
        Generate a summary of the metamodel operation information.

        :type  component_info:
               :class:`com.vmware.vapi.metadata.metamodel_client.OperationInfo`
        :param component_info: Metamodel metadata of an operation
        :rtype: :class:`vmware.vapi.server.rest_handler.MetadataStore.\
            OperationSummary`
        :return: Class containing parameters metadata and annotations in dicts
        """
        param_list = [(param_info.name, param_info)
                      for param_info in operation_info.params]
        param_info_map = collections.OrderedDict(param_list)

        if RestAnnotations.REQUEST_MAPPING in operation_info.metadata.keys():
            # Create a map of value in PathVariable annotation to
            # canonical name of the parameter
            path_variables_map = {
                param_info.metadata[RestAnnotations.PATH_VARIABLE].elements[
                    RestAnnotations.VALUE_ELEMENT].string_value: param_name
                for param_name, param_info in six.iteritems(param_info_map)
                if RestAnnotations.PATH_VARIABLE in param_info.metadata
            }
            # pylint: disable=E0602
            return self.OperationSummary(
                param_info_map,
                path_variables_map,
                operation_info.metadata[RestAnnotations.REQUEST_MAPPING])

        return self.OperationSummary(param_info_map)  # pylint: disable=E0602

    def _process_service_info(self, service_id, service_info):
        """
        Process the metamodel service information. Scan the services
        for operations, structures and enumerations and store into dictionaries
        for fast lookup.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service.
        :type  service_info:
               :class:`com.vmware.vapi.metadata.metamodel_client.ServiceInfo`
        :param service_info: Metamodel service information to be processed
        """
        for structure_id, structure_info in six.iteritems(
                                            service_info.structures):
            self._process_structure_info(structure_id, structure_info)

        for enumeration_id, enumeration_info in six.iteritems(
                                                service_info.enumerations):
            self.enumeration_map[enumeration_id] = enumeration_info

        self.service_map[service_id] = {
            operation_id: self._create_operation_summary(operation_info)
            for operation_id, operation_info in six.iteritems(
                                                service_info.operations)}

    def _process_structure_info(self, structure_id, structure_info):
        """
        Process the metamodel structure information. Scan the structures for
        for fields and enumerations and store into dictionaries
        for fast lookup.

        :type  structure_id: :class:`str`
        :param structure_id: Identifier of the structure.
        :type  structure_info:
               :class:`com.vmware.vapi.metadata.metamodel_client.StructureInfo`
        :param structure_info: Metamodel structure information to be processed
        """
        field_map = {}
        for field_info in structure_info.fields:
            field_map[field_info.name] = field_info
        self.structure_map[structure_id] = field_map

        for enumeration_id, enumeration_info in six.iteritems(
                                                structure_info.enumerations):
            self.enumeration_map[enumeration_id] = enumeration_info


class URLValueDeserializer(object):
    """
    Deserialize the parameters provided in the HTTP query string
    into a dictionary.

    For example:
        /rest/vmodl/test/uber/rest/filter?
            struct.string_field=string&
            struct.boolean_field=True&
            struct.long_field=10&
            struct.struct_field.string_field=string&
            struct.struct_field.long_field=10&
            struct.optional_string=string&
            struct.list_string.1=string1&
            struct.list_string.2=string2&
            struct.list_list_long.1.1=11&
            struct.list_list_long.1.2=12&
            struct.list_list_long.2.1=21&
            struct.list_list_long.2.2=22&
            struct.map_simple.1.key=stringkey&
            struct.map_simple.1.value=stringvalue&
            struct.map_struct.1.key=stringkey&
            struct.map_struct.1.value.string_field=string&
            struct.map_struct.1.value.long_field=10

    1. Top level members of the request complex type are referenced by their
       name.
    2. Referencing nested complex structures will use "." and concatenation of
       names.
    3. Whenever arrays of given type are required we will use param.n notation
       to identify the instance number n of the object.

    Deserialized version of this query string will be:
    {
        "struct": {
            "string_field": "string",
            "boolean_field": True,
            "long_field": 10,
            "struct_field": {
                "long_field": 10,
                "string_field": "string"
            },
            "optional_string": "string",
            "list_string": [
                "string1",
                "string2"
            ],
            "list_list_long": [
                [
                    11,
                    12
                ],
                [
                    21,
                    22
                ]
            ],
            "map_simple": [
                {
                    "key": "stringkey",
                    "value": "stringvalue"
                }
            ],
            "map_struct": [
                {
                    "key": "stringkey",
                    "value": {
                        "long_field": 10,
                        "string_field": "string"
                    }
                }
            ]
        }
    }

    """
    @staticmethod
    def deserialize(query_string):
        """
        Deserialize the given query string into a python dictionary.

        :type  query_string: :class:`str`
        :param query_string: HTTP query string containing parameters.
        :rtype: :class:`dict` of :class:`str` and :class:`object`
        :return: Python dictionary deserialized from query string.
        """
        query_string_dict = {}

        query_string = query_string.decode()
        for item in query_string.split('&'):
            # Parse only the query parameters
            if '=' not in item:
                continue

            k, v = item.split('=')
            tokens = k.split('.')

            #
            # The core idea here is to split the tokens in
            # a.b.c.d type of string and go from left to right.
            # At each step, the next token will be either put
            # at a key in the dictionary or element in a list if
            # the token is a digit.
            #
            # So, at each token, we should look ahead the next token,
            # and if the next token is a digit, then create an empty
            # list or return an existing list where it should be added
            # as element. If the next token is a non-digit, then create
            # a new dictionary or return an existing dictionary where
            # the token should be added as a key.
            #

            current_value = query_string_dict
            tokens_length = len(tokens)
            for i, token in enumerate(tokens):

                # Lookahead the next token
                next_token = None
                if i + 1 < tokens_length:
                    next_token = tokens[i + 1]

                # Next token is the last token
                if next_token is None:
                    if isinstance(current_value, list):
                        current_value.append(v)  # pylint: disable=E1101
                    elif isinstance(current_value, dict):
                        current_value[token] = v
                # Next token is not the last token
                else:
                    #
                    # If next token is a digit, create array as placeholder
                    # otherwise a dictionary
                    next_token_type = [] if next_token.isdigit() else {}

                    if isinstance(current_value, list):
                        index = int(token)
                        if index > len(current_value) + 1:
                            msg = (
                                'Element with index %d is expected,'
                                ' but got %d' % (len(current_value) + 1, index))
                            logger.error(msg)
                            raise werkzeug.exceptions.BadRequest(msg)
                        elif index == len(current_value) + 1:
                            # pylint: disable=E1101
                            current_value.append(next_token_type)
                        next_value = current_value[index - 1]
                    elif isinstance(current_value, dict):
                        next_value = current_value.setdefault(
                            token, next_token_type)
                    current_value = next_value

        return query_string_dict


class DataValueDeserializer(object):
    """
    Convert from Python dictionary deserialized from a JSON object
    (or) from HTTP URL query string to DataValue.
    """
    _builtin_type_map = {
        Type.BuiltinType.VOID: DataType.VOID,
        Type.BuiltinType.BOOLEAN: DataType.BOOLEAN,
        Type.BuiltinType.LONG: DataType.INTEGER,
        Type.BuiltinType.DOUBLE: DataType.DOUBLE,
        Type.BuiltinType.STRING: DataType.STRING,
        Type.BuiltinType.BINARY: DataType.BLOB,
        Type.BuiltinType.SECRET: DataType.SECRET,
        Type.BuiltinType.DATE_TIME: DataType.STRING,
        Type.BuiltinType.ID: DataType.STRING,
        Type.BuiltinType.URI: DataType.STRING,
        Type.BuiltinType.ANY_ERROR: DataType.ANY_ERROR,
        Type.BuiltinType.DYNAMIC_STRUCTURE: DataType.DYNAMIC_STRUCTURE,
    }
    _builtin_native_type_map = {
        Type.BuiltinType.BOOLEAN: bool,
        Type.BuiltinType.LONG: int,
        Type.BuiltinType.DOUBLE: decimal.Decimal,
        Type.BuiltinType.STRING: six.text_type,
        Type.BuiltinType.BINARY: six.text_type,
        Type.BuiltinType.SECRET: six.text_type,
        Type.BuiltinType.DATE_TIME: six.text_type,
        Type.BuiltinType.ID: six.text_type,
        Type.BuiltinType.URI: six.text_type,
    }

    def __init__(self, metadata):
        """
        Initialize DataValueDeserializer

        :type  metadata: :class:`vmware.vapi.server.rest_handler.MetadataStore`
        :param metadata: Object that contains the metamodel metadata of
            all the services.
        """
        self._metadata = metadata
        self._category_map = {
            Type.Category.BUILTIN: self.visit_builtin,
            Type.Category.USER_DEFINED: self.visit_user_defined,
            Type.Category.GENERIC: self.visit_generic
        }
        self._generic_map = {
            GenericInstantiation.GenericType.OPTIONAL: self.visit_optional,
            GenericInstantiation.GenericType.LIST: self.visit_list,
            GenericInstantiation.GenericType.SET: self.visit_list,
            GenericInstantiation.GenericType.MAP: self.visit_map,
        }

    def visit_builtin(self, type_info, json_value):
        """
        Deserialize a primitive value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.DataValue`
        :return: DataValue created using the input
        """
        try:
            native_type = self._builtin_native_type_map[type_info.builtin_type]
            if native_type == six.text_type:
                if type_info.builtin_type == Type.BuiltinType.BINARY:
                    # For Binary types, we need to convert unicode to bytes
                    base64_encoded_value = json_value.encode()
                    native_value = base64.b64decode(base64_encoded_value)
                else:
                    native_value = json_value
            elif native_type == int:
                native_value = int(json_value)
            elif native_type == decimal.Decimal:
                native_value = decimal.Decimal(json_value)
            elif native_type == bool:
                if isinstance(json_value, bool):
                    native_value = json_value
                elif json_value.lower() == 'true':
                    native_value = True
                elif json_value.lower() == 'false':
                    native_value = False
                else:
                    msg = 'Expected boolean value, but got %s' % json_value
                    logger.error(msg)
                    raise werkzeug.exceptions.BadRequest(msg)
            data_type = self._builtin_type_map[type_info.builtin_type]
            return data_value_factory(data_type, native_value)
        except KeyError:
            msg = ('Could not process the request, '
                   'builtin type %s is not supported' % type_info.builtin_type)
            logger.exception(msg)
            raise werkzeug.exceptions.InternalServerError(msg)

    def visit_user_defined(self, type_info, json_value):
        """
        Deserialize a user defined value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.StructValue` or
            :class:`vmware.vapi.data.value.StringValue`
        :return: DataValue created using the input
        """
        user_defined_type_info = type_info.user_defined_type
        if user_defined_type_info.resource_type == Enumeration.RESOURCE_TYPE:
            return StringValue(json_value)
        elif user_defined_type_info.resource_type == Structure.RESOURCE_TYPE:
            structure_info = self._metadata.structure_map[
                user_defined_type_info.resource_id]
            struct_value = StructValue(
                name=user_defined_type_info.resource_id)
            for field_name, field_value in six.iteritems(json_value):
                try:
                    field_info = structure_info[str(field_name)]
                    field_data_value = self.visit(field_info.type, field_value)
                    struct_value.set_field(field_name, field_data_value)
                except KeyError:
                    msg = 'Unexpected field \'%s\' in request' % field_name
                    logger.error(msg)
                    raise werkzeug.exceptions.BadRequest(msg)
            return struct_value
        else:
            msg = ('Could not process the request,'
                   'user defined type %s is not supported' %
                   user_defined_type_info.resource_type)
            logger.error(msg)
            raise werkzeug.exceptions.InternalServerError(msg)

    def visit_optional(self, type_info, json_value):
        """
        Deserialize an optional value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.OptionalValue`
        :return: DataValue created using the input
        """
        if json_value is not None:
            element_value = self.visit(type_info.element_type, json_value)
            return OptionalValue(element_value)
        else:
            return OptionalValue()

    def visit_list(self, type_info, json_value):
        """
        Deserialize a list value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.ListValue`
        :return: DataValue created using the input
        """
        if not isinstance(json_value, list):
            msg = 'Excepted list, but got %s' % type(json_value).__name__
            logger.error(msg)
            raise werkzeug.exceptions.BadRequest(msg)
        return ListValue([
            self.visit(type_info.element_type, value) for value in json_value])

    def visit_map(self, type_info, json_value):
        """
        Deserialize a map value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.StructValue`
        :return: DataValue created using the input
        """
        if not isinstance(json_value, list):
            msg = 'Excepted list, but got %s' % type(json_value).__name__
            logger.error(msg)
            raise werkzeug.exceptions.BadRequest(msg)
        try:
            return ListValue(
                [StructValue(
                    name=MAP_ENTRY,
                    values={
                        'key': self.visit(
                            type_info.map_key_type, value['key']),
                        'value': self.visit(
                            type_info.map_value_type, value['value'])
                    })
                 for value in json_value])
        except KeyError as e:
            msg = 'Invalid Map input, missing %s' % e
            logger.error(msg)
            raise werkzeug.exceptions.BadRequest(msg)

    def visit_generic(self, type_info, json_value):
        """
        Deserialize a list/optional/map value

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.OptionalValue` or
            :class:`vmware.vapi.data.value.ListValue` or
            :class:`vmware.vapi.data.value.StructValue`
        :return: DataValue created using the input
        """
        try:
            generic_type_info = type_info.generic_instantiation
            generic_convert_method = \
                self._generic_map[generic_type_info.generic_type]
            return generic_convert_method(generic_type_info, json_value)
        except KeyError:
            msg = ('Could not process the request, generic type '
                   '%s is not supported' % generic_type_info.generic_type)
            logger.exception(msg)
            raise werkzeug.exceptions.InternalServerError(msg)

    def visit(self, type_info, json_value):
        """
        Deserialize the given input using the metamodel type information

        :type  type_info:
            :class:`com.vmware.vapi.metadata.metamodel_client.Type`
        :param type_info: Metamodel type information
        :type  json_value: :class:`object`
        :param json_value: Value to be visited
        :rtype: :class:`vmware.vapi.data.value.DataValue`
        :return: DataValue created using the input
        """
        convert_method = self._category_map[type_info.category]
        return convert_method(type_info, json_value)

    def generate_operation_input(self, service_id, operation_id, input_data):
        """
        This method generates a StructValue corresponding to the Python dict
        (deserialized from JSON) suitable as an input value for the specified
        operation.

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service to be invoked.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation to be invoked.
        :type  input_data: :class:`dict`
        :param input_data: Dictionary object that represents the deserialized
            json input.
        :rtype: :class:`vmware.vapi.data.value.DataValue` or
        :return: DataValue created using the input
        """

        param_info_map = \
            self._metadata.service_map[service_id][operation_id].param_info_map

        try:
            fields = {
                param_name: self.visit(param_info_map[str(param_name)].type,
                                       param_value)
                for param_name, param_value in six.iteritems(input_data)}
        except KeyError as e:
            msg = 'Unexpected parameter %s in JSON body' % e
            logger.exception(msg)
            raise werkzeug.exceptions.BadRequest(msg)

        return StructValue(name=OPERATION_INPUT, values=fields)

    def map_uri_params(self, uri_parameters, service_id, operation_id):
        """
        If RequestMapping annotation is present, map URI parameters to
        respective parameter names. When request mapping is provided, it is
        possible that the uri parameter name is different from the canonical
        name of the parameter.

        :type  uri_parameters: :class:`dict` of :class:`str` and :class:`object`
        :param uri_parameters: Arguments parsed from the HTTP URL
        :type  service_id: :class:`str`
        :param service_id: Identifier of the service to be invoked
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation to be invoked
        :rtype: :class:`dict` of :class:`str` and :class:`object`
        :return: Arguments parsed from the HTTP URL - path_variable name
                 replaced with the canonical name of the parameter
        """

        if not self._metadata.service_map[
               service_id][operation_id].has_request_mapping_metadata():
            return uri_parameters

        path_variables_map = \
            self._metadata.service_map[service_id][operation_id].\
            path_variables_map

        # Update keys in uri_parameters from path variable name to canonical
        # name of the parameter
        return {path_variables_map[name]: value
                for name, value in six.iteritems(uri_parameters)}


class SecurityContextBuilder(object):
    """
    Helper class to build the appropriate security context based
    on the authentication information present in the request context.
    """
    def __init__(self, parsers):
        """
        Initialize SecurityContextBuilder

        :type  parsers: :class:`list` of :class:`str`
        :param parsers: List of names of Security Parsers
        """
        #
        # The order in the variable determines the order in which
        # the security parsers parse the request. The first parser
        # that can create a security context is used.
        #
        # If the request contains more than one kind of security
        # related information, the first one that gets parsed is used.
        # And if that information is invalid, 401 UNAUTHORIZED
        # is returned to the client. The other security information
        # that is not parsed is not taken into consideration.
        #
        # The user has to remove the invalid security context and invoke
        # the operation again.
        #
        self._parsers = [parser_class()
                         for parser_class in dynamic_import_list(parsers)]

    def build(self, request):
        """
        Build the security context based on the authentication information
        in the request context

        :type  request: :class:`werkzeug.wrappers.Request`
        :param request: Request object
        :rtype: :class:`vmware.vapi.core.SecurityContext`
        :return: Security context
        """
        for parser in self._parsers:
            security_context = parser.build(request)
            if security_context:
                return security_context


class ResponseCookieBuilder(object):
    """
    Helper class to build the appropriate cookies to be set
    in the response.
    """
    def __init__(self, session_methods):
        """
        Initialize ResponseCookieBuilder

        :type  session_methods: :class:`list` of :class:`str`
        :param session_methods: List of names of session login methods
        """
        self._session_methods = session_methods

    def build(self, service_id, operation_id, method_result):
        """
        Build the response cookie for the request

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service to be invoked.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation to be invoked.
        :type  method_result: :class:`vmware.vapi.core.MethodResult`
        :param method_result: MethodResult object to be serialized
        :rtype: :class:`dict` of :class:`str` and :class:`str`
        :return: Dictionary containing cookies that need to be set in the
            response.
        """
        session_method = '%s.%s' % (service_id, operation_id)
        if session_method in self._session_methods:
            if (isinstance(method_result.output, StringValue) or
                    isinstance(method_result.output, SecretValue)):
                session_id = method_result.output.value
            return {REST_SESSION_ID_KEY: session_id}


class RESTHandler(object):
    """
    Request handler that accept REST API calls and invoke the corresponding
    call on ApiProvider interface.
    """
    def __init__(self, api_provider, allow_cookies=True, provider_config=None):
        """
        Initialize RESTHandler

        :type  api_provider: :class:`vmware.vapi.core.ApiProvider`
        :param api_provider: ApiProvider to be used to invoke the vAPI requests
        :type  allow_cookies: :class:`bool`
        :param allow_cookies: Whether cookie support should be enabled
        :type  provider_config:
            :class:`vmware.vapi.settings.config.ProviderConfig` or :class:`None`
        :param provider_config: ApiProvider to be used to invoke the vAPI
            requests
        """
        self._api_provider = api_provider
        metadata = MetadataStore(api_provider)
        self.rest_rules = RoutingRuleGenerator(
            metadata, provider_config.get_rest_prefix()).rest_rules
        self.data_value_deserializer = DataValueDeserializer(metadata)
        self.security_context_builder = SecurityContextBuilder(
            provider_config.get_rest_security_parsers())
        self.response_cookie_builder = ResponseCookieBuilder(
            provider_config.get_rest_session_methods()) \
            if allow_cookies else None

    @staticmethod
    def _get_default_mapping_operation_id(
            http_method,
            query_params, uri_params):
        """
        Figure out the operation identifier based on the HTTP method,
        the identifier arguments in the URL and the query string.

        :type  http_method: :class:`str`
        :param http_method: HTTP request method
        :type  query_params: :class:`dict` of :class:`str` and :class:`object`
        :param query_params: Decoded dictionary from the query string
        :type  uri_params: :class:`dict` of :class:`str` and :class:`object`
        :param uri_params: Arguments parsed from the HTTP URL
        :rtype: :class:`str`
        :return: Identifier of the operation to be invoked
        """
        operation_id = http_method_map[http_method]
        # If ID is in the URI parameter then, operation_id is get instead of
        # list
        if uri_params and operation_id == 'list':
            ## TODO: Handle composite identifier case
            operation_id = 'get'
        action = query_params.get('~action')
        if action:
            operation_id = action.replace('-', '_')
        return operation_id

    @staticmethod
    def _get_action_operation_id(dispatch_info, query_params):
        """
        Figure out the operation identifier based on the action parameter
        in the query string and dispatch info provided

        :type  dispatch_info: :class:`tuple` of :class:`tuple`s of
            :class:`str` and :class:`str`
        :param dispatch_info: Tuple of tuples of (action, operation_id)
        :type  query_params: :class:`dict` of :class:`str` and :class:`object`
        :param query_params: Decoded dictionary from the query string
        :rtype: :class:`str`
        :return: Identifier of the operation to be invoked
        """
        actions = dict(dispatch_info)
        action_requested = query_params.get(RestAnnotations.ACTION_PARAM)
        if action_requested not in actions:
            if action_requested:
                msg = 'No matching method available for the requested ' + \
                    'action \'%s\' on the URL' % action_requested
            else:
                msg = 'No matching method available for the requested ' + \
                    'URL and HTTP method'
            logger.error(msg)
            raise werkzeug.exceptions.NotFound(msg)
        return actions[action_requested]

    def _get_input_value(self, service_id, operation_id, input_data):
        """
        Generate the input DataValue for the given operation

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service to be invoked.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation to be invoked.
        :type  input_data: :class:`dict`
        :param input_data: Dictionary object that represents the deserialized
            json input.
        """
        try:
            return self.data_value_deserializer.generate_operation_input(
                service_id, operation_id, input_data)
        except werkzeug.exceptions.BadRequest as e:
            raise e
        except Exception as e:
            msg = 'Cannot process request: %s' % e
            logger.exception(msg)
            raise werkzeug.exceptions.InternalServerError(msg)

    def _serialize_output(
            self, request, service_id, operation_id, method_result,
            use_cookies):
        """
        Serialize the MethodResult object

        :type  request: :class:`werkzeug.wrappers.Request`
        :param request: Request object
        :type  service_id: :class:`str`
        :param service_id: Identifier of the service to be invoked.
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation to be invoked.
        :type  method_result: :class:`vmware.vapi.core.MethodResult`
        :param method_result: MethodResult object to be serialized
        :type  use_cookies: :class:`bool`
        :param use_cookies: Whether cookies are to be sent in response
        :rtype: :class:`tuple` of :class:`int`, :class:`str`, :class:`dict`
        :return: HTTP status code, serialized json output of the operation and
            a dictionary of response cookies.
        """
        if method_result.success():
            if self.response_cookie_builder is None or not use_cookies:
                cookies = None
            else:
                cookies = self.response_cookie_builder.build(
                    service_id, operation_id, method_result)
            output = method_result.output
            json_output = None
            if not isinstance(output, VoidValue):
                if not isinstance(output, StructValue):
                    # If the output is not a struct or error value,
                    # box it with {'value':..} to make it a
                    # good json output
                    output = StructValue(name='output', values={
                        'value': output
                    })
                json_output = DataValueConverter.convert_to_json(output)
            status = 204 if request.method == 'DELETE' else 200
        else:
            cookies = None
            error = method_result.error
            json_output = DataValueConverter.convert_to_json(error)
            status = vapi_to_http_error_map.get(error.name, 500)
        return (status, json_output, cookies)

    def invoke(self, request, endpoint, uri_parameters):
        """
        Handle the REST API invocation

        :type  request: :class:`werkzeug.wrappers.Request`
        :param request: Request object
        :type  endpoint: :class:`tuple` of :class:`tuple` of :class:`str` and
        :class:`str`
        :param endpoint: Tuple of service ID and dispatch_info is a tuples of
        tuples of (action, operation_id)
        :type  uri_parameters: :class:`dict` of :class:`str` and :class:`object`
        :param uri_parameters: Arguments parsed from the HTTP URL
        :rtype: :class:`tuple` of :class:`int`, :class:`str`, :class:`dict`
        :return: HTTP status code, serialized json output of the operation and
            response cookies.
        """
        # Operation input is contributed by:
        # 1. URI parameters: Arguments parsed from HTTP URL
        # 2. Query parameters: Arguments parsed from the query string in the
        #               HTTP URL
        # 3. Request body: Arguments present in request body
        #
        # There is a definitive place for each argument, a particular argument
        # can be passed only using one of the above ways.
        #
        # Typically, main object identifiers are present in the base HTTP URL.
        # For GET operations, additional parameters can be provided in the query
        # string. For POST, PUT, PATCH, parameters can only be provided using
        # the body

        query_string_flat_dict = werkzeug.urls.url_decode(
            request.query_string)
        (service_id, dispatch_info) = endpoint

        # When dispatch_info is ((None, operation_id),) or ((None, None),)
        if len(dispatch_info) == 1 and dispatch_info[0][0] is None:
            operation_id = dispatch_info[0][1]
            if operation_id is None:
                operation_id = self._get_default_mapping_operation_id(
                    request.method, query_string_flat_dict, uri_parameters)
        else:
            operation_id = self._get_action_operation_id(
                dispatch_info, query_string_flat_dict)
            # Fixed query param 'action' is supported only for
            # HTTP POST method
            # Delete 'action' from query string if:
            # 1) We start supporting 'action' for GET or,
            # 2) We start accepting query parameters for POST
            # Only in those cases, the 'action' parameter in query string
            # would cause an unexpected keyword argument error

        input_data = self.data_value_deserializer.map_uri_params(
            uri_parameters, service_id, operation_id)

        if request.method == 'GET':
            query_string_parameters = URLValueDeserializer.deserialize(
                request.query_string)
            # Currently we put all query params for GET requests in request
            # body, don't do that for TASK_REST_QUERY_PARAM
            input_data.update({key: query_string_parameters[key]
                               for key in query_string_parameters.keys()
                               if key != TASK_REST_QUERY_PARAM})

        if request.method in ['PUT', 'PATCH', 'POST']:
            request_body_string = request.get_data()
            if request_body_string:
                try:
                    if isinstance(request_body_string, six.string_types):
                        input_data.update(
                            json.loads(request_body_string,
                                       parse_float=decimal.Decimal))
                    elif isinstance(request_body_string, six.binary_type):
                        input_data.update(
                            json.loads(request_body_string.decode('utf-8'),
                                       parse_float=decimal.Decimal))
                except ValueError as e:
                    msg = 'Invalid JSON in request body: %s' % e
                    logger.error(msg)
                    raise werkzeug.exceptions.BadRequest(msg)

        # Create request context
        security_context = self.security_context_builder.build(request)
        application_context = create_default_application_context()
        ctx = ExecutionContext(
            application_context=application_context,
            security_context=security_context)

        # Set application context for the current operation/thread
        set_context(ctx)

        input_value = self._get_input_value(
            service_id, operation_id, input_data)

        # Check if it's a task invocation
        is_task = query_string_flat_dict.get(TASK_REST_QUERY_PARAM)
        if is_task is not None:
            if is_task.lower() == 'true':
                operation_id = get_task_operation_name(operation_id)
            else:
                msg = 'Invalid value for "%s" query param' % (
                            TASK_REST_QUERY_PARAM)
                logger.error(msg)
                raise werkzeug.exceptions.BadRequest(msg)

        method_result = self._api_provider.invoke(
            service_id, operation_id, input_value, ctx)

        # Clear application context from the current operation/thread
        clear_context()

        use_cookies = False if REQUIRE_HEADER_AUTHN in request.headers else True
        return self._serialize_output(
            request, service_id, operation_id, method_result, use_cookies)
