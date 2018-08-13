#!/usr/bin/env python

"""
Asyncore http connection
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


# Http stuff
# import Cookie
import asynchat
from collections import deque
import threading
import posixpath
import six

from six.moves import urllib
from six.moves import BaseHTTPServer
from vmware import vapi
from vmware.vapi.lib.log import get_vapi_logger

logger = get_vapi_logger(__name__)

_HTTP_MAX_REQUEST_SIZE = 4 * 1024 * 1024


def find_token(tokens, token_to_find):
    """
    Find token and token value from a comma separated tokens

    :type  tokens: :class:`str`
    :param tokens: comma separated tokens string
    :type  token_to_find: :class:`str`
    :param token_to_find: a string to find in the tokens
    :rtype :class:`tuple` of :class:`str`, :class:`str` if token is found, None otherwise
    :return: tuple of (token_to_find, value)
    """
    # Split token with ,
    for token in tokens.lower().split(','):
        # Split again with ;
        token_and_val = token.split(';', 1)
        if token_and_val[0].strip() == token_to_find:
            if len(token_and_val) > 1:
                val = token_and_val[1].strip()
            else:
                val = ''
            return (token_to_find, val)
    return None


def log_exception(msg, err):
    """
    Handy function to log exception with stack trace

    :type  msg: :class:`str`
    :param msg: error message
    :type  err: :class:`Exception`
    :param err: exception to log
    """
    import traceback
    stack_trace = traceback.format_exc()
    logger.critical('%s: %s: %s', msg, err, stack_trace)


class GzipWriter(object):
    """ Gzip writer """

    def __init__(self, wfile):
        """
        Gzip writer init

        :type  wfile: :class:`file`
        :param wfile: file object to write to
        """
        import gzip
        self.wfile = gzip.GzipFile(fileobj=wfile, mode='wb', compresslevel=5)
        self.org_wfile = wfile

    def write(self, buf):
        """
        write

        :type  buf: :class:`str`
        :param buf: data to write
        """
        if not buf or not self.wfile:
            return
        self.wfile.write(buf)

    def flush(self):
        """ flush """
        if not self.wfile:
            return
        self.wfile.flush()

    def close(self):
        """ close """
        if not self.wfile:
            return

        # No more write
        self.wfile.close()
        self.wfile = None

        self.org_wfile.close()
        self.org_wfile = None

    def __del__(self):
        self.close()


class DeflateWriter(object):
    """ Deflate (zlib) writer """
    def __init__(self, wfile, compresslevel=5):
        """
        Deflate (zlib) writer init

        :type  wfile: :class:`file`
        :param wfile: file object to write to
        """
        import zlib
        self.wfile = wfile
        self.compress = zlib.compressobj(compresslevel,
                                         zlib.DEFLATED,
                                         zlib.MAX_WBITS)
        self.flush_flag = zlib.Z_SYNC_FLUSH
        self.close_flush_flag = zlib.Z_FINISH

    def write(self, buf):
        """
        write

        :type  buf: :class:`str`
        :param buf: data to write
        """
        if not buf or not self.wfile:
            return

        self.wfile.write(self.compress.compress(buf))

    def flush(self):
        """ flush """
        if not self.wfile:
            return

        self.wfile.write(self.compress.flush(self.flush_flag))
        self.wfile.flush()

    def close(self):
        """ close """
        if not self.wfile:
            return

        self.wfile.write(self.compress.flush(self.close_flush_flag))
        self.wfile.close()

        # No more write
        self.wfile = None
        self.compress = None

    def __del__(self):
        self.close()


class AsyncChatWriteAdapter(object):
    """ Async chat write adapter """

    def __init__(self, chat_obj):
        """
        Async chat write adapter init

        :type  chat_obj: :class:`asynchat.async_chat`
        :param chat_obj: async chat object
        """
        self.chat_obj = chat_obj

    def write(self, buf):
        """
        write

        :type  buf: :class:`str`
        :param buf: data to write
        """
        if not self.chat_obj:
            return

        self.chat_obj.push(buf)

    def flush(self):
        """ flush """
        if not self.chat_obj:
            return

        self.chat_obj.initiate_send()

    def close(self):
        """ close """
        if not self.chat_obj:
            return

        self.chat_obj.close_when_done()
        self.flush()

        self.chat_obj = None

    def __del__(self):
        self.close()


class ChunkedMessageBodyWriter(object):
    """ Chunked message writer """
    def __init__(self, wfile, chunk_size=4096):
        """
        Chunked message writer init

        :type  wfile: :class:`file`
        :param wfile: file object to write to
        :type  chunk_size: :class:`int`
        :param chunk_size: max write chunk size
        """
        self.wfile = wfile
        self.chunk_size = chunk_size

        self.curr_chunk_size = 0
        self.chunks = deque()

    def _write_chunk(self):
        """ write a chunk """
        if not self.wfile:
            return

        if self.curr_chunk_size > self.chunk_size:
            chunk_size = self.chunk_size
            leftover_bytes = self.curr_chunk_size - self.chunk_size
        else:
            chunk_size = self.curr_chunk_size
            leftover_bytes = 0

        # Write chunk header
        chunk_header = '%x\r\n' % chunk_size
        if six.PY3:
            chunk_header = chunk_header.encode('utf-8')
        self.wfile.write(chunk_header)

        chunks = self.chunks
        if leftover_bytes > 0:
            # Split the last chunk
            last_chunk = chunks.pop()
            chunks.append(last_chunk[:-leftover_bytes])
            leftover_chunks = [last_chunk[-leftover_bytes:]]
        else:
            leftover_chunks = deque()

        # Write chunks
        for chunk in chunks:
            self.wfile.write(chunk)
        self.wfile.write(b'\r\n')

        # Reset state
        self.curr_chunk_size = leftover_bytes
        self.chunks = leftover_chunks

    def write(self, buf):
        """
        write

        :type  buf: :class:`str`
        :param buf: data to write
        """
        if not buf or not self.wfile:
            return

        size = len(buf)
        self.curr_chunk_size += size
        self.chunks.append(buf)
        while self.curr_chunk_size >= self.chunk_size:
            self._write_chunk()

    def close(self):
        """ close """
        if not self.wfile:
            return

        # Flush chunks
        self.flush()

        # Write ending zero bytes chunk
        self._write_chunk()
        self.wfile.close()
        self.wfile = None

    def __del__(self):
        self.close()

    def flush(self):
        """ flush """
        # Flush buffer
        if self.curr_chunk_size:
            self._write_chunk()
            if self.wfile:
                self.wfile.flush()


class DataHandler(object):
    """ Async chat data handler """

    def __init__(self, channel):
        """
        Async chat data handler init

        :type  channel: :class:`HttpRequestHandler`
        :param channel: http request handler
        """
        self.channel = channel
        self.max_data_size = 0
        self.data = None
        self.data_size = 0
        self.clear_data()

    def clear_data(self):
        """ Clear self.data """
        self.data = deque()
        self.data_size = 0

    def set_handlers(self,
                     found_term_handler, terminator,
                     collect_in_data_handler, max_data_size):
        """
        Set asynchat handlers

        :type  found_term_handler: :class:`function`
        :param found_term_handler: terminator found handler
        :type  terminator: :class:`str`
        :param terminator: terminator string
        :type  collect_in_data_handler: :class:`function`
        :param collect_in_data_handler: collect incoming data handler
        :type  max_data_size: :class:`int`
        :param max_data_size: max data size before abort
        """
        self.channel.set_handlers(found_term_handler, terminator, collect_in_data_handler)
        self.max_data_size = max_data_size

    def append_data_collect_incoming_data(self, data):
        """
        Generic incoming data handler: Append data to self.data

        :type  data: :class:`str`
        :param data: incoming data
        """
        data_size = self.data_size + len(data)
        if data_size > self.max_data_size:
            self.channel.request_too_large(data_size, self.max_data_size)
            return

        # Append data
        self.data.append(data)
        self.data_size = data_size


class HttpHeadersHandler(DataHandler):
    """ Async chat http header handler """

    def __init__(self, channel):
        """
        Async chat http headers handler init

        :type  channel: :class:`HttpRequestHandler`
        :param channel: http request handler
        """
        DataHandler.__init__(self, channel)
        self.set_handlers(self.http_headers_found_terminator, b'\r\n\r\n',
                          self.append_data_collect_incoming_data, 4096)

    def http_headers_found_terminator(self):
        """ Found terminator handler """
        self.channel.http_headers_end(b''.join(self.data))


class HttpBodyHandler(DataHandler):
    """ Async chat http body handler """

    def __init__(self, channel):
        """
        Async chat http body handler init

        :type  channel: :class:`HttpRequestHandler`
        :param channel: http request handler
        """
        DataHandler.__init__(self, channel)
        # Max request len is 4 M
        self.request_size = 0
        self.max_request_size = _HTTP_MAX_REQUEST_SIZE

    def http_body_collect_incoming_data(self, data):
        """
        incoming data handler

        :type  data: :class:`str`
        :param data: incoming data
        """
        data_size = self.request_size + len(data)
        if data_size > self.max_request_size:
            self.channel.request_too_large(data_size, self.max_request_size)
            return

        self.channel.http_body_continue(data)
        self.request_size = data_size

    def http_body_found_terminator(self):
        """ Found terminator handler """
        self.channel.http_body_end()


class ChunkedHandler(HttpBodyHandler):
    """ Async chat http chunked handler """

    def __init__(self, channel):
        """
        Async chat http chunked handler init

        :type  channel: :class:`HttpRequestHandler`
        :param channel: http request handler
        """
        HttpBodyHandler.__init__(self, channel)
        self.set_handlers(self.chunked_size_found_terminator, b'\r\n',
                          self.append_data_collect_incoming_data, 128)

    def chunked_size_found_terminator(self):
        """ Found chunked size handler """
        line = ''.join(self.data)
        self.clear_data()
        try:
            chunk_size = int(line.split(';', 1)[0], 16)
        except Exception:
            logger.error('400: Bad chunk size: %s', line)
            self.channel.send_error_(400, 'Bad chunk size (%s)' % line)
            return

        if chunk_size == 0:
            # Last chunk. Remove trailer
            self.set_handlers(
                self.chunked_trailer_found_terminator, b'\r\n',
                self.append_data_collect_incoming_data, 4096)
        else:
            self.set_handlers(
                lambda: self.channel.setup_chunked_handler(), chunk_size + 2,  # pylint: disable=W0108
                    self.chunked_data_collect_incoming_data, self.max_request_size)

    def chunked_trailer_found_terminator(self):
        """ Found chunked trailer terminator handler """
        if len(self.data) and self.data[-1] == b'\r\n':
            # End of chunked trailer
            self.http_body_found_terminator()

    def chunked_data_collect_incoming_data(self, data):
        """
        incoming data handler

        :type  data: :class:`str`
        :param data: incoming data
        """
        self.http_body_collect_incoming_data(data)


class MessageHandler(HttpBodyHandler):
    """ Async chat http message handler """

    def __init__(self, channel, content_len=None):
        """
        Async chat http message handler init

        :type  channel: :class:`HttpRequestHandler`
        :param channel: http request handler
        :type  content_len: :class:`int` or None
        :param content_len: http content length
        """
        HttpBodyHandler.__init__(self, channel)

        if content_len is None:
            # Read until eof
            content_len = self.max_request_size
        elif content_len < 0 or content_len > self.max_request_size:
            self.channel.request_too_large(content_len, self.max_request_size)
            return

        if content_len == 0:
            self.message_body_found_terminator()
        else:
            self.set_handlers(self.message_body_found_terminator, content_len,
                              self.message_body_collect_incoming_data, self.max_request_size)

    def message_body_found_terminator(self):
        """ Found http message terminator handler """
        self.http_body_found_terminator()

    def message_body_collect_incoming_data(self, data):
        """
        incoming data handler

        :type  data: :class:`str`
        :param data: incoming data
        """
        self.http_body_collect_incoming_data(data)


class HeadOfLineWriter(object):
    """ Head of line writer """

    class Writer:
        """ Chile writer """
        def __init__(self, parent):
            """
            Chile writer init

            :type  parent: :class:`HeadOfLineWriter`
            :param parent: Parent writer
            """
            self.reply = None   # Used by parent to buffer pending reply
            self.parent = parent

        def write(self, data):
            """
            write

            :type  data: :class:`str`
            :param data: data to write
            """
            if self.parent:
                self.parent.write(self, data)

        def close(self):
            """ close """
            if self.parent:
                self.parent.close(self)
                self.parent = None

        def __del__(self):
            self.close()

        def flush(self):
            """ flush """
            if self.parent:
                self.parent.flush(self)

        def is_closed(self):
            """
            is writer closed

            :rtype:  :class:`bool`
            :return: True if closed, False otherwise
            """
            return self.parent is None

    def __init__(self, wfile):
        """
        Head of line writer init

        :type  wfile: :class:`file`
        :param wfile: file object to write to
        """
        self.wfile = wfile
        self.lock = threading.RLock()   # Protecting writers_q
        self.writers_q = deque()

    def new_writer(self):
        """
        Create a new child writer

        :rtype:  :class:`Writer`
        :return: A new writer
        """
        writer = self.Writer(self)
        with self.lock:
            self.writers_q.append(writer)
        return writer

    def write(self, writer, data):
        """
        Write to child writer

        :type  writer: :class:`Writer`
        :param writer: child writer
        :type  data: :class:`str`
        :param data: data to write
        """
        if writer.is_closed():
            # Connection already closed
            return

        with self.lock:
            head_conn = self.writers_q[0]
            # TODO: Release global lock, acquire writer lock
            if writer != head_conn:
                if not writer.reply:
                    writer.reply = deque()
                writer.reply.append(data)
            else:
                self.flush_pending_reply(writer)
                try:
                    # logger.debug('write len %d %s', len(data), self.wfile)
                    self.wfile.write(data)
                except Exception as err:
                    logger.error('write: Failed to write %s', (str(err)))

    def close(self, writer):
        """
        Close a child writer

        :type  writer: :class:`Writer`
        :param writer: child writer
        """
        # close will modify writers_q. Must NOT call this while iterating
        # thru writers_q
        with self.lock:
            if len(self.writers_q) > 0 and writer == self.writers_q[0]:
                self.writers_q.popleft()
                while len(self.writers_q) > 0 and self.writers_q[0].is_closed():
                    head_writer = self.writers_q.popleft()
                    self.flush_pending_reply(head_writer)
                self.wfile.flush()

    def flush_pending_reply(self, writer):
        """
        Flush pending reply

        :type  writer: :class:`Writer`
        :param writer: child writer
        """
        if writer.reply:
            pending_reply = writer.reply
            writer.reply = None
            try:
                data = ''.join(pending_reply)
                # logger.debug('write len %d %s', len(data), self.wfile)
                self.wfile.write(data)
            except Exception as err:
                logger.error('flush_pending_reply: Failed to write %s', (str(err)))

    def flush(self, writer):  # pylint: disable=W0613
        """
        flush a child writer (only possible for head of line writer)

        :type  writer: :class:`Writer`
        :param writer: child writer
        """
        # TODO: Only flush head of line writer
        self.wfile.flush()

    def __del__(self):
        with self.lock:
            while len(self.writers_q) > 0:
                head_writer = self.writers_q.popleft()
                try:
                    self.flush_pending_reply(head_writer)
                    head_writer.close()
                except Exception:
                    pass

            logger.debug('close %s', self.wfile)
            self.wfile.close()
            self.wfile = None


class HttpRequestHandler(object):
    """ Http request handler """

    def __init__(self, http_conn, wfile, content_type, protocol_handler):
        """
        Http request handler init

        :type  http_conn: :class:`AsyncoreHttpConnection`
        :param http_conn: http connection
        :type  wfile: :class:`file`
        :param wfile: file object to write to
        :type  content_type: :class:`str`
        :param content_type: request content type
        :type  protocol_handler: :class:`vmware.vapi.protocol.server.transport.\
                                            async_protocol_handler.AsyncProtocolHandler`
        :param protocol_handler: async protocol handler
        """
        # Extract info from http_conn
        self.http_conn = http_conn
        self.wfile = wfile
        self.content_type = content_type
        self.protocol_handler = protocol_handler

        self.http_version = http_conn.http_version
        headers = http_conn.headers

        # Set static response headers
        # NYI: Cookies
        # cookies = Cookie.SimpleCookie(headers.get('cookie'))
        self.response_headers = {
            'cache-control': 'no-cache',
        }
        if self.content_type:
            self.response_headers['content-type'] = self.content_type

        self.gzip_response = False
        self.deflate_response = False
        self.resp_chunking = False
        self.force_close = False   # force_close_when_done
        if self.http_version >= 1.1:
            # Accept-Encoding
            accept_encoding = headers.get('accept-encoding', '')
            # Support gzip only for now
            self.gzip_response = \
                (find_token(accept_encoding, 'gzip') is not None)
            if not self.gzip_response:
                self.deflate_response = \
                    (find_token(accept_encoding, 'deflate') is not None)

            # Response chunking
            te = headers.get('TE', 'chunked')
            self.resp_chunking = (find_token(te, 'chunked') is not None)

            self.force_close = headers.get('connection', '') == 'close'

            # Set static response headers
            if self.resp_chunking:
                self.response_headers['transfer-encoding'] = 'chunked'

            if self.gzip_response:
                self.response_headers['content-encoding'] = 'gzip'
            elif self.deflate_response:
                self.response_headers['content-encoding'] = 'deflate'
        elif self.http_version == 1.0:
            if headers.get('connection', '') != 'keep-alive':
                self.force_close = True
        else:
            self.force_close = True

        self.data_handler = \
            protocol_handler.get_data_handler(self) if protocol_handler else None
        self._response_started = False

    def request_continue(self, data):
        """
        request data continue

        :type  data: :class:`str`
        :param data: request data
        """
        self.data_handler.data_ready(data)

    def request_end(self):
        """ request data ended """
        self.data_handler.data_end()

    def write(self, data):
        """
        write

        :type  data: :class:`str`
        :param data: data to write
        """
        if not self._response_started:
            self._response_started = True
            self.send_response_headers(200)
        self.response_continue(data)

    def close(self):
        """ close """
        self.response_end()
        self.http_conn = None

    def __del__(self):
        self.close()

    def close_http_conn_when_done(self):
        """ close the connection after all data written """
        if self.http_conn:
            self.http_conn.close_when_done()

    def send_response_headers(self, response_code):
        """
        send response headers

        :type  response_code: :class:`int`
        :param response_code: http response code
        """

        try:
            close_connection = self.force_close

            # Char encoding
            # encoding = 'utf-8'

            # Send response code
            http_conn = self.http_conn
            http_conn.send_response(response_code)

            # NYI: cookies
            #for cookie in cookies:
            #    header_value = cookies[cookie].output(header='')
            #    http_conn.send_header('set-cookie', header_value)

            if not self.resp_chunking:
                close_connection = True

            if self.http_version >= 1.1:
                # Close connection?
                if close_connection:
                    self.response_headers['connection'] = 'close'
                    self.close_http_conn_when_done()
            else:
                if close_connection:
                    self.close_http_conn_when_done()

            # Send headers
            for key, value in six.iteritems(self.response_headers):
                http_conn.send_header(key, value)

            # End headers
            http_conn.end_headers()

            wfile = self.wfile
            chunk_size = 4096

            # Handle chunking
            if self.resp_chunking:
                wfile = ChunkedMessageBodyWriter(wfile, chunk_size)

            # Handle compression
            if self.gzip_response:
                wfile = GzipWriter(wfile=wfile)
            elif self.deflate_response:
                wfile = DeflateWriter(wfile=wfile)

            self.wfile = wfile
        except Exception as err:
            log_exception('Error: Send response exception', err)
            self.close_http_conn_when_done()

    def response_continue(self, response):
        """
        response data continue

        :type  response: :class:`str`
        :param response: http response data
        """

        try:
            # Send response
            if response and self.wfile:
                wfile = self.wfile
                is_str_response = (
                    isinstance(response, six.string_types) or
                    isinstance(response, six.binary_type))
                if is_str_response:
                    wfile.write(response)
                else:
                    # In theory, this should be async too...
                    while True:
                        chunk = response.read(4096)
                        if not chunk:
                            break
                        wfile.write(chunk)

                if not is_str_response:
                    response.close()
        except Exception as err:
            log_exception('Error: Send response exception', err)
            self.close_http_conn_when_done()

    def response_end(self):
        """ response data end """
        try:
            if self.wfile:
                self.wfile.close()
                self.wfile = None
        except Exception as err:
            log_exception('Error: Send response exception', err)
            self.close_http_conn_when_done()


class AsyncoreHttpConnection(asynchat.async_chat, BaseHTTPServer.BaseHTTPRequestHandler):  # pylint: disable=W0223
    """ Async Http connection with async chat """

    _HTTP_VERSION = 1.1

    # Override base class's protocol_version
    # Note: need to include accurate 'Content-Length' in send_header()
    protocol_version = 'HTTP/' + str(_HTTP_VERSION)

    # XXX: Get around a nasty async_chat bug
    asynchat.async_chat.ac_in_buffer_size = _HTTP_MAX_REQUEST_SIZE

    def __init__(self, server, sock_map, sock, from_addr, protocol_factory):
        """
        Async Http connection with async chat

        :type  server: :class:`vmware.vapi.server.asyncore_server.AsyncoreTcpListener`
        :type  server: asyncore server
        :type  sock_map: :class:`dict`
        :param sock_map: Global socket map
        :type  sock: :class:`socket.socket`
        :param sock: http connection socket
        :type  from_addr: :class:`tuple`
        :param from_addr: remote address bound to the socket
        :type  protocol_factory: :class:`HttpFactory`
        :param protocol_factory: protocol factory
        """
        try:
            self.accept_read = False
            asynchat.async_chat.__init__(self, sock, map=sock_map)
            BaseHTTPServer.BaseHTTPRequestHandler.__init__(self, sock,
                                                           from_addr, server)
            self.server = server

            # Http headers handler
            self.close_connection = 0
            self.setup_http_headers_handler()

            # Setup rfile / wfile
            self.rfile = None
            self.wfile = vapi.server.asyncore_server.SyncWriteToAsyncWriteAdapter(self)
            self.head_of_line_writer = HeadOfLineWriter(self.wfile)

            self.protocol_factory = protocol_factory
            self.request_handler = None

            # Shutup pylint
            self.http_version = self._HTTP_VERSION
            self.request_size = 0
        except Exception:
            self.cleanup()
            raise

    def cleanup(self):
        """ connection cleanup """
        # Need to cleanup from sock_map
        try:
            self.del_channel()
        except Exception:
            pass
        self.server = None
        self.close_connection = 1
        self.rfile = None
        self.wfile = None
        self.head_of_line_writer = None
        self.protocol_factory = None
        self.request_handler = None

    ## Begin BaseHTTPServer.BaseHTTPRequestHandler interface
    #
    def setup(self):
        """ setup: Not used """
        pass

    def handle(self):
        """ handle: Not used """
        pass

    def finish(self):
        """ finish: Not used """
        pass

    ## Handle HTTP POST
    #
    def do_POST(self):
        """ Handle HTTP Post """
        logger.debug('In do_POST: %s', self.client_address)
        self.http_body_begin()
        logger.debug('Done do_POST: %s', self.client_address)

    ## End BaseHTTPServer.BaseHTTPRequestHandler interface

    ## Begin async_chat interface
    #
    # def collect_incoming_data(): pass
    # def found_terminator(): pass

    def setup_http_headers_handler(self):
        """ setup asynchat http headers handlers """
        self.accept_read = True
        HttpHeadersHandler(self)
        self.server.loop_controller.intr()   # Wake up server

    def setup_chunked_handler(self):
        """ setup asynchat http chunked handlers """
        ChunkedHandler(self)

    def setup_message_handler(self, content_len):
        """ setup asynchat http message body handlers """
        MessageHandler(self, content_len)

    def set_handlers(self, found_term_handler, terminator, collect_in_data_handler):
        """
        setup asynchat handlers

        :type  found_term_handler: :class:`function`
        :param found_term_handler: terminator found handler
        :type  terminator: :class:`str`
        :param terminator: terminator string
        :type  collect_in_data_handler: :class:`function`
        :param collect_in_data_handler: collect incoming data handler
        """
        self.found_terminator = found_term_handler
        self.set_terminator(terminator)
        self.collect_incoming_data = collect_in_data_handler

    def http_headers_end(self, headers):
        """
        http headers end callback

        :type  headers: :class:`str`
        :param headers: http headers string
        """
        self.rfile = six.BytesIO(headers)
        self.handle_one_request()
        if self.close_connection:
            self.close_when_done()

    def http_body_begin(self):
        """ request body begin """
        self.http_version = float(self.request_version.split('/')[1])

        # Get protocol handler
        path = self.path.split('?', 1)[0]
        path = path.split('#', 1)[0]
        path = urllib.parse.unquote(path)

        header_content_type = self.headers.get('content-type', '')
        tokens = header_content_type.split(';', 1)
        if len(tokens) > 1:
            content_type, _ = tokens
        else:
            content_type = tokens[0]

        protocol_handler = self.protocol_factory.get_handler(path, content_type)
        if protocol_handler is None:
            self.send_error_(404, 'Path not found: %s' % path)
            # TODO: close connection?
            return

        assert(self.request_handler is None)
        wfile = self.head_of_line_writer.new_writer()
        self.request_handler = HttpRequestHandler(self, wfile, content_type, protocol_handler)

        # Look for non-identity transfer-encoding before content-length
        req_chunking = False
        if self.http_version >= 1.1:
            # Request chunking
            xfer_encoding = self.headers.get('transfer-encoding', '')
            req_chunking = (find_token(xfer_encoding, 'chunked') is not None)

        self.request_size = 0
        if req_chunking:
            # Setup chunked message body handler
            self.setup_chunked_handler()
        else:
            # Get content length from header
            content_length = self.headers.get('content-length')
            if content_length:
                try:
                    content_len = int(content_length)
                except Exception:
                    logger.error('400: Bad content-length: %s', content_length)
                    self.send_error_(400, 'Bad content-length (%s)' % content_length)
                    return
            else:
                content_len = None

            # Setup message body handler
            self.setup_message_handler(content_len)

    def http_body_continue(self, data):
        """ request body continue """
        if self.request_handler:
            self.request_handler.request_continue(data)

    def readable(self):
        """
        Can read more data?

        :rtype  :class:`bool`
        :return True if this can handle more data
        """
        return self.accept_read and asynchat.async_chat.readable(self)

    def http_body_end(self):
        """ request body ended """
        # To stop pipeline request, set accept_read to False until the server
        # can serve another request
        # self.accept_read = False

        if self.request_handler:
            self.request_handler.request_end()
            self.request_handler = None

        # Back to http header reader
        self.setup_http_headers_handler()

    def send_error_(self, response_code, response_txt):
        """
        Send http error

        :type  response_code: :class:`int`
        :param response_code: http response code
        :type  response_txt: :class:`str`
        :param response_txt: http response text
        """
        try:
            self.send_error(response_code, response_txt)
        except Exception:
            pass
        self.close_when_done()

    def request_too_large(self, data_size, max_data_size):
        """
        Send request too large error

        :type  data_size: :class:`int`
        :param data_size: request data size
        :type  max_data_size: :class:`int`
        :param max_data_size: max request data size allowed
        """
        msg = 'Request too large (%d bytes). Max allowed is %d' % (data_size, max_data_size)
        self.send_error_(413, msg)   # 413: Request Entity Too Large

    def log_message(self, format, *args):  # pylint: disable=W0622
        """
        Override the BaseHTTPServer.BaseHTTPRequestHandler method to send the
        log message to the log file instead of stderr.

        :type  format: :class:`str`
        :param format string
        :type  args: :class:`tuple`
        :param args: format argument(s)
        """
        logger.debug('%s - - %s', self.client_address, format % args)

    # Apparently asynchat write is not multi-thread safe. Use our own
    def handle_write(self):
        """ handle write """
        if self.wfile:
            self.wfile.write_ready()

    def writable(self):
        """
        Have something to write to http connection?

        :rtype  :class:`bool`
        :return True if data is ready to write
        """
        if self.wfile:
            return self.wfile.writable()
        else:
            return False

    def close_when_done(self):
        """ close the connection after all data written """
        if self.wfile:
            self.wfile.close_when_done()
        self.close_connection = 1

    def handle_error(self):
        """ handle error callback """
        self.cleanup()

    def handle_expt(self):
        """ handle exception callback """
        self.cleanup()


class HttpFactory(object):
    """ Http factory """
    HTTP_CONTENT_MAPPING = {'json': 'application/json',
                            'xml': 'text/xml'}

    def __init__(self):
        """ Http factory init """
        self.path_map = {}

    @staticmethod
    def abspath(path):
        """
        Get posix absolute path

        :type  path: :class:`str`
        :param path: url path
        :rtype: :class:`str`
        :return: posix style abs path
        """
        abspath = posixpath.abspath(path)
        # Strange. posixpath returns '//' for '//' but '/' for '///' (or
        # other variants). Explicitly check for this
        if abspath == '//':
            abspath = '/'
        logger.debug('abspath %s -> %s', path, abspath)
        return abspath

    def add_handler(self, path, msg_type, protocol_handler):
        """
        add handler associated with url path and transport message

        :type  path: :class:`str`
        :param path: url path
        :type  msg_type: :class:`str`
        :param msg_type: message type
        :type  protocol_handler: :class:`vmware.vapi.protocol.server.transport.\
                                            async_protocol_handler.AsyncProtocolHandler`
        :param protocol_handler: async protocol handler
        """
        content_type = self.HTTP_CONTENT_MAPPING.get(msg_type)
        if not content_type:
            logger.error('Unsupported msg type: %s', msg_type)
            return False

        path = self.abspath(path)
        handlers = self.path_map.get(path)
        if not handlers:
            logger.debug('add_handler %s: %s', content_type, path)
            self.path_map = {path: {content_type: protocol_handler}}
        else:
            handler = handlers.get(content_type)
            if handler and handler != protocol_handler:
                logger.error('Cannot re-register resource @ %s', path)
                return False

            logger.debug('add_handler %s: %s', content_type, path)
            handlers[content_type] = protocol_handler

    def get_path_handlers(self, path):
        """
        get handlers for a particular url path

        :type  path: :class:`str`
        :param path: url path
        :rtype: :class:`dict` of :class:`tuple` of (:class:`str`,
                 :class:`vmware.vapi.protocol.server.transport.async_protocol_handler.AsyncProtocolHandler`)
        :return: a dict of content type to protocol handler mapping
        """
        path = self.abspath(path)
        return self.path_map.get(path)

    def get_handler(self, path, content_type):
        """
        get handler for a particular url path and content type

        :type  path: :class:`str`
        :param path: url path
        :type  content_type: :class:`str`
        :param content_type: http content-type
        :rtype:  :class:`vmware.vapi.protocol.server.transport.async_protocol_handler.AsyncProtocolHandler`
        :return: protocol handler
        """
        path = self.abspath(path)
        handlers = self.path_map.get(path)
        if handlers:
            handler = handlers.get(content_type)
        else:
            handler = None
        return handler

    def handle_accept(self, server, sock_map, sock, from_addr):
        """
        handle newly accepted socket connection

        :type  server: :class:`vmware.vapi.server.asyncore_server.AsyncoreTcpListener`
        :type  server: asyncore server
        :type  sock_map: :class:`dict`
        :param sock_map: Global socket map
        :type  sock: :class:`socket.socket`
        :param sock: accepted socket
        :type  from_addr: :class:`tuple`
        :param from_addr: remote address bound to the socket
        """
        AsyncoreHttpConnection(server, sock_map, sock, from_addr, self)
