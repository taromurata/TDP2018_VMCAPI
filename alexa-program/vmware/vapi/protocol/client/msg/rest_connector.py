"""
Rest client handler
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


from vmware.vapi.core import ApiProvider
from vmware.vapi.data.serializers.rest import RestSerializer
from vmware.vapi.lib.load import dynamic_import
from vmware.vapi.lib.log import get_client_wire_logger, get_vapi_logger
from vmware.vapi.protocol.client.http_lib import HTTPMethod, HTTPRequest
from vmware.vapi.protocol.client.msg.generic_connector import GenericConnector

logger = get_vapi_logger(__name__)
request_logger = get_client_wire_logger()


class RestClientProvider(ApiProvider):
    """ Rest rpc client provider """

    def __init__(
            self, http_provider, post_processors, rest_metadata_map=None,
            is_vapi_rest=True):
        """
        Rest rpc client provider init

        :type  http_provider:
            :class:`vmware.vapi.protocol.client.rpc.provider.HTTPProvider`
        :param http_provider: rpc provider object
        :type  post_processors: :class:`list` of :class:`str`
        :param post_processors: List of post processor class names
        :type  rest_metadata_map: :class:`dict` of (:class:`str`, :class:`str`)
            and :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata_map: Rest metadata for all operations
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        """

        ApiProvider.__init__(self)
        self._http_provider = http_provider
        self._rest_metadata_map = rest_metadata_map or {}
        self._is_vapi_rest = is_vapi_rest

        # Load all the post processors
        self.post_processors = [dynamic_import(p)() for p in post_processors]

    def add_rest_metadata(self, service_id, operation_id, rest_metadata):
        """
        Add rest metadata for an operation

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest metadata for the operation
        """
        self._rest_metadata_map[(service_id, operation_id)] = rest_metadata

    def set_rest_format(self, is_vapi_rest):
        """
        Set whether the rest format is VAPI or Swagger REST

        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the rest format is VAPI REST or not
        """
        self._is_vapi_rest = is_vapi_rest

    def invoke(self, service_id, operation_id, input_value, ctx):
        """
        Invokes the specified method using the input value and the
        the execution context provided

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :type  input_value: :class:`vmware.vapi.data.value.DataValue`
        :param input_value: method input parameters
        :type  ctx: :class:`vmware.vapi.core.ExecutionContext`
        :param ctx: execution context object
        :rtype: :class:`vmware.vapi.core.MethodResult`
        :return: method result object
        """
        operation_rest_metadata = None
        if self._rest_metadata_map is not None and \
                (service_id, operation_id) in self._rest_metadata_map:
            operation_rest_metadata = \
                self._rest_metadata_map[(service_id, operation_id)]
        return self._invoke(service_id, operation_id, input_value, ctx,
                            operation_rest_metadata, self._is_vapi_rest)

    def _invoke(self, service_id, operation_id, input_value, ctx, rest_metadata,  # pylint: disable=W0613
                is_vapi_rest):
        """
        Invokes the specified method using the input value, execution context
        and rest metadata provided

        :type  service_id: :class:`str`
        :param service_id: Service identifier
        :type  operation_id: :class:`str`
        :param operation_id: Operation identifier
        :type  input_value: :class:`vmware.vapi.data.value.DataValue`
        :param input_value: method input parameters
        :type  ctx: :class:`vmware.vapi.core.ExecutionContext`
        :param ctx: execution context object
        :type  rest_metadata:
            :class:`vmware.vapi.lib.rest.OperationRestMetadata`
        :param rest_metadata: Rest metadata for the operation
        :type  is_vapi_rest: :class:`bool`
        :param is_vapi_rest: Whether the Rest json message format is VAPI Rest
            or not
        :rtype: :class:`vmware.vapi.core.MethodResult`
        :return: method result object
        """
        http_method = rest_metadata.http_method
        (url_path, auth_headers, request_body_str, cookies) = \
            RestSerializer.serialize_request(input_value, ctx, rest_metadata,
                                             is_vapi_rest)
        # Add headers
        # Accept header is needed because any operation can report an error and
        # hence could have a body.
        headers = {
            'Accept': 'application/json',
        }
        if http_method not in [HTTPMethod.GET, HTTPMethod.HEAD]:
            # TODO Maybe add this as part of REST metadata
            headers['Content-Type'] = 'application/json'
        if auth_headers is not None:
            headers.update(auth_headers)
        request_logger.debug('_invoke: request url: %s', url_path)
        request_logger.debug('_invoke: request http method: %s', http_method)
        request_logger.debug('_invoke: request headers: %s', headers)
        request_logger.debug('_invoke: request body: %s', request_body_str)
        http_request = HTTPRequest(method=http_method, url_path=url_path,
                                   headers=headers, body=request_body_str,
                                   cookies=cookies)

        # TODO Add post processors
        #for processor in self.post_processors:
        #    request_msg = processor.process(request_msg)
        http_response = self._http_provider.do_request(http_request)
        request_logger.debug(
            '_invoke: response status: %s', http_response.status)
        request_logger.debug('_invoke: response body: %s', http_response.body)
        method_result = RestSerializer.deserialize_response(
            http_response.status, http_response.body, is_vapi_rest)
        return method_result


def get_protocol_connector(
        http_provider, post_processors=None, provider_filter_chain=None):
    """
    Get protocol connector

    :type  http_provider:
        :class:`vmware.vapi.protocol.client.rpc.provider.HTTPProvider`
    :param http_provider: rpc provider object
    :type  post_processors: :class:`list` of :class:`str`
    :param post_processors: List of post processor class names
    :type  provider_filter_chain: :class:`list` of
        :class:`vmware.vapi.provider.filter.ApiProviderFilter`
    :param provider_filter_chain: List of API filters in order they are to be
        chained
    :rtype: :class:`vmware.vapi.protocol.client.connector.Connector`
    :return: json rpc connector object
    """
    if not post_processors:
        post_processors = []
    api_provider = RestClientProvider(http_provider, post_processors)
    connector = GenericConnector(
        http_provider, api_provider, provider_filter_chain)
    return connector
