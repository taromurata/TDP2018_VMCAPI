"""
REST Rule generator
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015-2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import collections
import six

from werkzeug.routing import Rule

from com.vmware.vapi.metadata.metamodel_client import Type
from vmware.vapi.lib.constants import RestAnnotations


class MappingRule(object):
    """
    Base class for all the mapping rules. This will contain
    the common helper functions for all the rules.
    """
    def __init__(self, rest_prefix):
        """
        Initialize MappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        self._rest_prefix = rest_prefix

    def _generate_service_base_url(self, service_id):
        """
        Generate base url for a particular service

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service.
        :rtype: :class:`str`
        :return: base url for all the HTTP REST URLs for a given service.
        """
        suffix = service_id.replace('_', '-').replace('.', '/').lower()
        return '%s%s' % (self._rest_prefix, suffix)

    @staticmethod
    def _get_id_suffix(param_info_map):
        """
        Generate suffix using the ID parameters

        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`str` or `None`
        :return: string that can be used in the URL to represent an identifier,
            if there is no identifier, None is returned
        """
        for param_name, param_info in six.iteritems(param_info_map):
            if param_info.type.category == Type.Category.BUILTIN:
                if param_info.type.builtin_type == Type.BuiltinType.ID:
                    # TODO: Handle composite identifiers
                    return '/<string:%s>' % param_name
        # No ID parameter
        return ''


class ListMappingRule(MappingRule):
    """
    Mapping rule that handles 'list' operations in the API
    and generates HTTP GET.

    Operations matched:
    list() -> GET /svc
    """
    def __init__(self, rest_prefix):
        """
        Initialize ListMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    # TODO: All the match methods for default mapping rules need to check if
    # there is a RequestMapping annotation and return False if present
    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'list' else False)

    def url(self, service_id, param_info_map):  # pylint: disable=W0613
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Metamodel metadata paramters for the operation
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        return (service_url, 'GET')


class PostMappingRule(MappingRule):
    """
    Mapping rule that handles 'create' operations in the API
    and generates HTTP POST.

    Operations matched:
    create() -> POST /svc
    create(...) -> POST /svc + body
    """
    def __init__(self, rest_prefix):
        """
        Initialize PostMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'create' else False)

    def url(self, service_id, param_info_map):  # pylint: disable=W0613
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        return (service_url, 'POST')


class DeleteMappingRule(MappingRule):
    """
    Mapping rule that handles 'delete' operations in the API
    and generates HTTP DELETE.

    Operations matched:
    delete(ID id) -> DELETE /svc/<id>
    """
    def __init__(self, rest_prefix):
        """
        Initialize DeleteMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'delete' else False)

    def url(self, service_id, param_info_map):
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        id_suffix = self._get_id_suffix(param_info_map)
        if id_suffix:
            return (service_url + id_suffix, 'DELETE')
        else:
            return (service_url, 'POST')


class GetMappingRule(MappingRule):
    """
    Mapping rule that handles 'get' operations in the API
    and generates HTTP GET.

    Operations matched:
    get(ID id) -> GET /svc/<id>
    """
    def __init__(self, rest_prefix):
        """
        Initialize GetMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'get' else False)

    def url(self, service_id, param_info_map):
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        id_suffix = self._get_id_suffix(param_info_map)
        if id_suffix:
            return (service_url + id_suffix, 'GET')
        else:
            return (service_url, 'POST')


class PatchMappingRule(MappingRule):
    """
    Mapping rule that handles 'update' operations in the API
    and generates HTTP PATCH.

    Operations matched:
    update(ID id) -> PATCH /svc/<id>
    """
    def __init__(self, rest_prefix):
        """
        Initialize PatchMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'update' else False)

    def url(self, service_id, param_info_map):
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        id_suffix = self._get_id_suffix(param_info_map)
        if id_suffix:
            return (service_url + id_suffix, 'PATCH')
        else:
            return (service_url, 'POST')


class PutMappingRule(MappingRule):
    """
    Mapping rule that handles 'set' operations in the API
    and generates HTTP PUT.

    Operations matched:
    set(ID id) -> PUT /svc/<id>
    """
    def __init__(self, rest_prefix):
        """
        Initialize PutMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id == 'set' else False)

    def url(self, service_id, param_info_map):
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        id_suffix = self._get_id_suffix(param_info_map)
        if id_suffix:
            return (service_url + id_suffix, 'PUT')
        else:
            return (service_url, 'POST')


class PostActionMappingRule(MappingRule):
    """
    Mapping rule that handles non-crud operations in the API
    and generates HTTP POST.

    Operations matched:
    custom() -> POST /svc?~action=custom
    custom(ID id) -> POST /svc/<id>?~action=custom
    custom(...) -> POST /svc?~action=custom + body
    custom(ID id, ...) -> POST /svc/<id>?~action=custom + body
    """
    _crud_ops = ['create', 'get', 'list', 'update', 'set', 'delete']

    def __init__(self, rest_prefix):
        """
        Initialize PostActionMappingRule

        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        MappingRule.__init__(self, rest_prefix)

    @staticmethod
    def match(operation_id):
        """
        Check if the given operation matches the criteria for this
        mapping rule.

        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :rtype: :class:`bool`
        :return: True, if the given operation matches the criteria
            for this mapping rule, False, otherwise.
        """
        return (True if operation_id not in PostActionMappingRule._crud_ops
                else False)

    def url(self, service_id, param_info_map):
        """
        Generate the URL for the given operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        service_url = self._generate_service_base_url(service_id)
        id_suffix = self._get_id_suffix(param_info_map)
        return (service_url + id_suffix, 'POST')


class RoutingRuleGenerator(object):
    """
    Generate the routing rules based on vAPI metamodel metadata.
    """
    def __init__(self, metadata, rest_prefix):
        """
        Initialize RoutingRuleGenerator

        :type  metadata: :class:`vmware.vapi.server.rest_handler.MetadataStore`
        :param metadata: Object that contains the relevant metamodel metadata of
            all the services.
        :type  rest_prefix: :class:`str`
        :param rest_prefix: REST URL prefix
        """
        self._metadata = metadata
        self._rest_prefix = rest_prefix
        if not rest_prefix.endswith('/'):
            self._rest_prefix = '%s/' % rest_prefix
        self._mapping_rules = [
            ListMappingRule(self._rest_prefix),
            PostMappingRule(self._rest_prefix),
            DeleteMappingRule(self._rest_prefix),
            GetMappingRule(self._rest_prefix),
            PatchMappingRule(self._rest_prefix),
            PutMappingRule(self._rest_prefix),
            PostActionMappingRule(self._rest_prefix),
        ]

    def _get_default_mapping_rule(self, service_id, op_id, param_info_map):
        """
        Generate default mapping rule for an operation.

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  op_id: :class:`str`
        :param op_id: Operation identifier
        :type  param_info_map: :class:`collections.OrderedDict` of :class:`str`
               and :class:`com.vmware.vapi.metadata.metamodel_client.FieldInfo`
        :param param_info_map: Map of parameter name to its metamodel metadata
        :rtype: :class:`tuple` of :class:`str` and :class:`str`
        :return: Tuple that has URL and the HTTP method for the
            given operation.
        """
        for mapping_rule in self._mapping_rules:
            if mapping_rule.match(op_id):
                service_url, http_method = \
                    mapping_rule.url(service_id, param_info_map)
        return (service_url, http_method)

    #TODO: Delete this method once idl-toolkit does these validations
    @staticmethod
    def _validate_action_param(param, http_method):
        """
        Validate the fixed query parameter in value element of RequestMapping.
        """
        if not http_method == 'POST':
            raise Exception(
                "Fixed query param 'action' is supported only for HTTP " +
                "POST method")
        if not param.startswith(RestAnnotations.ACTION_PARAM) or \
                len(param.split('&')) > 1:
            raise Exception((
                "Illegal fixed param '%s'. " +
                "Only one fixed param is supported - '?%s=<op>'.") %
                (param, RestAnnotations.ACTION_PARAM))
        if len(param.split('=')) != 2:
            raise Exception(
                "Illegal value '%s' for fixed param." % param)
        (_, action_value) = param.split('=')
        if not action_value:
            raise Exception(
                "Illegal value '%s' for fixed param." % param)

    # TODO: Define a class CustomMappingRule and follow the same pattern as
    # other mapping rules
    def _get_custom_mapping_rule(self, request_mapping_element_map):
        """
        Generate the mapping rule for an operation that has RequestMapping
        in the VMODL2 service definition.
        Processing only "value" and "method" elements from the RequestMapping
        annotation

        Operation definition:
        @RequestMapping(value="/svc/{id}?action=custom",
                        method=RequestMethod.POST,
                        contentType="...",
                        accept="...")
        @ResponseStatus(204)
        void custom(@PathVariable("user_id") ID id, ...)

        Generated mapping: POST /svc/{id}?action=custom [+ body]

        :type  request_mapping_element_map:
            :class:`com.vmware.vapi.metadata.metamodel_client.ElementMap`
        :param request_mapping_element_map:
            Metamodel for the RequestMapping annotation on an operation
        :rtype: :class:`tuple` of :class:`str`, :class:`str` and :class:`str`
        :return: Tuple that has URL, HTTP method and value of the fixed query
            param 'action' for the given operation.
        """

        http_method = request_mapping_element_map.elements[
            RestAnnotations.METHOD_ELEMENT].string_value

        custom_url = request_mapping_element_map.elements[
            RestAnnotations.VALUE_ELEMENT].string_value
        custom_url = custom_url.replace('{', '<')
        custom_url = custom_url.replace('}', '>')
        custom_url = '%s%s' % (self._rest_prefix, custom_url[1:])

        # Get value of fixed query parameter 'action' if it exists
        if '?' in custom_url:
            (custom_url, param) = custom_url.split('?')
            (_, action_value) = param.split('=')
            self._validate_action_param(param, http_method)
        else:
            action_value = None

        return (custom_url, http_method, action_value)

    def generate_mapping_rule(
            self, service_id, operation_id, operation_summary):
        """
        Generate HTTP REST rule from operation summary

        :type  service_id: :class:`str`
        :param service_id: Identifier of the service
        :type  operation_id: :class:`str`
        :param operation_id: Identifier of the operation
        :type  operation_summary:
        :class:`vmware.vapi.server.rest_handler.MetadataStore.OperationSummary`
        :param operation_summary: Details of the operation
        :rtype: :class:`tuple` of :class:`str`, :class:`str` and one
            :class:`dict` element
        :return: Tuple that has URL, HTTP method and dispatch info for the given
            operation.

        Dispatch info is a mapping from value of fixed query
        parameter 'action' and corresponding operation_id.
        The possible cases for REST mapping and dispatching are:
        1) Operation with fixed action param:
            @RequestMapping(value="/svc/{id}?action=custom",
                           method=RequestMethod.POST)
            dispatch_info = {<action> : <operation_id>}
            <action> parameter in the query string would be used to obtain the
            operation_id for request dispatching
        2) Operation with @RequestMapping but no fixed param
            @RequestMapping(value="/svc/{id}", method=...)
            dispatch_info = {None: <operation_id>}
            Request can be dispatched to operation_id. Assuming there are no
            conflicting REST mappings
        3) Default REST mapping
            dispatch_info = {None: None}
            Operation ID would be determined based on HTTP method, path params
            and query params
        """
        # Generate custom mapping if there is @RequestMapping on the operation
        if operation_summary.has_request_mapping_metadata():
            service_url, http_method, action = self._get_custom_mapping_rule(
                operation_summary.request_mapping_metadata)
            dispatch_info = {action: operation_id}
        else:
            service_url, http_method = self._get_default_mapping_rule(
                service_id, operation_id, operation_summary.param_info_map)
            dispatch_info = {None: None}
        return (service_url, http_method, dispatch_info)

    @property
    def rest_rules(self):
        """
        HTTP REST rules

        :rtype: :class:` `list` of :class:`werkzeug.routing.Rule`
        :return: List of HTTP REST rules for all the registered services
        """

        rules_dict = collections.defaultdict(dict)

        for service_id, service_info in six.iteritems(
                self._metadata.service_map):
            for operation_id, operation_summary in six.iteritems(service_info):
                (service_url, http_method, dispatch_info) = \
                    self.generate_mapping_rule(service_id,
                                               operation_id,
                                               operation_summary)
                # dispatch_info's for service_url's are aggregated to generate
                # the Werkzeug 'endpoint' which would be used to dispatch the
                # request
                rules_dict[(service_id,
                            service_url,
                            http_method)].update(dispatch_info)

        rules = [Rule(service_url,
                      endpoint=(service_id, tuple(dispatch_info.items())),
                      methods=[http_method])
                 for (service_id, service_url, http_method), dispatch_info in
                 rules_dict.items()]

        return rules
