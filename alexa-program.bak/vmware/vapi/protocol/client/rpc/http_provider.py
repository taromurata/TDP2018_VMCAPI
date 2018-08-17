"""
Http protocol rpc provider
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015-2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long


import threading
import socket
import sys
import time
import six
from six.moves import urllib

from six.moves import http_client
try:
    from select import poll, POLLIN
except ImportError:
    poll = False
    try:
        from select import select
    except ImportError:
        select = False

from vmware.vapi.protocol.client.http_lib import HTTPResponse
from vmware.vapi.protocol.client.rpc.provider import HTTPProvider
from vmware.vapi.lib.addr_url_parser import parse_addr_url
from vmware.vapi.lib.log import get_vapi_logger

# Mostly reusing from pyVmomi/SoapAdapter. No point to reinvent so many wheel
# for http
# NYI: Use httplib2
logger = get_vapi_logger(__name__)


#
# Temporary workaround for Bug 1222549
#
# When client and server are using HTTP 1.1 with chunked encoding. Once server
# sends all the data, it should sent a zero length chunk to indicate to the
# client that server has sent all the data. In this case, if server closes the
# session without sending a zero length chunk, client throws IncompleteRead
# error.
#
# However, the issue is intermittent and is not reproducable.
#
# A possible fix has been suggested here:
# http://bobrochel.blogspot.com/2010/11/bad-servers-chunked-encoding-and.html
# i.e. Read the partial data and don't complain if we don't receive the zero
# length chunk.
#
#
def patch_http_response_read(func):
    """
    Wrapper function to patch the http read method to return the partial data
    when the server doesn't send a zero length chunk
    """
    def inner(*args):
        """
        Function that implements the patch
        """
        try:
            return func(*args)
        except http_client.IncompleteRead as e:
            logger.exception('Did not receive zero length chunk from the server')
            return e.partial
    return inner


http_client.HTTPResponse.read = patch_http_response_read(http_client.HTTPResponse.read)


class UnixSocketConnection(http_client.HTTPConnection):
    """
    Variant of http_client.HTTPConnection that supports HTTP
    connections over Unix domain sockets.
    """

    def __init__(self, path):
        """
        Initialize a Unix domain socket HTTP connection

        The HTTPConnection __init__ method expects a single argument,
        which it interprets as the host to connect to.  For this
        class, we instead interpret the parameter as the filesystem
        path of the Unix domain socket.

        :type    path: :class:`str`
        :param   path: Unix domain socket path
        """

        # Pass '' as the host to HTTPConnection; it doesn't really matter
        # what we pass (since we've overridden the connect method) as long
        # as it's a valid string.
        http_client.HTTPConnection.__init__(self, '')
        self.path = path
        self.sock = None

    def connect(self):
        """
        Override the HTTPConnection connect method to connect to a
        Unix domain socket.  Obey the same contract as HTTPConnection.connect
        which puts the socket in self.sock.
        """

        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        self.sock = sock


class _SslSocketWrapper(object):
    """
    The http_client module requires its sockets to have a
    makefile() method to provide a file-like interface (or rather
    file-in-Python-like) to the socket. PyOpenSSL doesn't implement
    makefile() as the semantics require files to call dup(2) on the
    underlying file descriptors, something not easily done on SSL sockets.

     # TODO: This wrapper breaks when the server requests a renegotiation
    """
    def __init__(self, sock):
        """
        Initializes this class.
        """
        self._sock = sock

    def __getattr__(self, name):
        """
        Forward everything to underlying socket.
        """
        return getattr(self._sock, name)

    def makefile(self, mode, bufsize=0):
        """
        Fake makefile method.

        makefile() on normal file descriptors uses dup2(2), which doesn't work with
        SSL sockets and therefore is not implemented by pyOpenSSL. This fake method
        works with the http_client module, but might not work for other modules.
        """
        # pylint: disable-msg=W0212
        return socket._fileobject(self._sock, mode, bufsize)


class HttpsConnection(http_client.HTTPSConnection):
    """
    Internal version of https connection
    """

    def __init__(self, *args, **kwargs):
        """
        Internal version of https connection init

        :type    args: :class:`tuple`
        :param   args: position parameters to :class:`http_client.HTTPSConnection`
        :type    kwargs: :class:`dict`
        :param   kwargs: key parameters to :class:`http_client.HTTPSConnection`
        """
        self.host = None
        self.port = None
        self.sock = None
        self._ssl_context = kwargs.pop('ssl_context')
        if self._ssl_context is None:
            # Only if the client requires SSL depend on SSL support
            from vmware.vapi.lib.ssl import DefaultClientContextFactory
            self._ssl_context = DefaultClientContextFactory().get_context()
        http_client.HTTPSConnection.__init__(self, *args, **kwargs)

    ## Override connect to allow us to use PyOpenSSL sockets
    def connect(self):
        """ connect """
        if self._ssl_context:
            # Only if client requires SSL depend on SSL import
            from OpenSSL import SSL
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ssl_sock = SSL.Connection(self._ssl_context, sock)
            ssl_sock.connect((self.host, self.port))
            ssl_sock.do_handshake()
            # Verify the python version
            if sys.hexversion < 0x2060000:
                self.sock = http_client.FakeSocket(sock, ssl_sock)
            elif six.PY2:
                self.sock = _SslSocketWrapper(ssl_sock)
            else:
                self.sock = sock
        else:
            http_client.HTTPSConnection.connect(self)


class GzipReader(object):
    """ Gzip reader """
    GZIP = 1
    DEFLATE = 2

    def __init__(self, rfile, encoding=GZIP, read_chunk_size=512):
        """
        Gzip reader init

        :type  rfile: :class:`file`
        :param rfile: file object to read from
        :type  encoding: :class:`int` (``GzipReader.GZIP`` or ``GzipReader.DEFLATE``)
        :param encoding: Zip stream encoding enum
        :type  read_chunk_size: :class:`int`
        :param read_chunk_size: Read chunk size
        """
        self.rfile = rfile
        self.chunks = []
        self.buf_size = 0    # Remaining buffer
        assert(encoding in (GzipReader.GZIP, GzipReader.DEFLATE))
        self.encoding = encoding
        self.unzip = None
        self.read_chunk_size = read_chunk_size

    def _create_unzip(self, first_chunk):
        """
        create unzip

        :type  first_chunk: :class:`str`
        :param first_chunk: First chunk of read stream data
        :rtype: :class:`str`
        :return: Decompressed data
        """
        import zlib
        if self.encoding == GzipReader.GZIP:
            wbits = zlib.MAX_WBITS + 16
        elif self.encoding == GzipReader.DEFLATE:
            # Sniff out real deflate format
            chunk_len = len(first_chunk)
            # Assume raw deflate
            wbits = -zlib.MAX_WBITS
            if first_chunk[:3] == ['\x1f', '\x8b', '\x08']:
                # gzip: Apache mod_deflate will send gzip. Yurk!
                wbits = zlib.MAX_WBITS + 16
            elif chunk_len >= 2:
                byte0 = ord(first_chunk[0])
                byte1 = ord(first_chunk[1])
                if (byte0 & 0xf) == 8 and (((byte0 * 256 + byte1)) % 31) == 0:
                    # zlib deflate
                    wbits = min(((byte0 & 0xf0) >> 4) + 8, zlib.MAX_WBITS)
        else:
            assert(False)
        self.unzip = zlib.decompressobj(wbits)
        return self.unzip

    def read(self, num_bytes=-1):
        """
        read

        :type  num_bytes: :class:`int`
        :param num_bytes: Number of decompressed bytes to read
        :rtype: :class:`bytes`
        :return: Decompressed data (len up to num_bytes)
        """
        chunks = self.chunks
        buf_size = self.buf_size

        while buf_size < num_bytes or num_bytes == -1:
            # Read and decompress
            chunk = self.rfile.read(self.read_chunk_size)

            if self.unzip is None:
                self._create_unzip(chunk)

            if chunk:
                inflated_chunk = self.unzip.decompress(chunk)
                buf_size += len(inflated_chunk)
                chunks.append(inflated_chunk)
            else:
                # Returns whatever we have
                break

        if buf_size <= num_bytes or num_bytes == -1:
            leftover_bytes = 0
            leftover_chunks = []
        else:
            leftover_bytes = buf_size - num_bytes
            # Adjust last chunk to hold only the left over bytes
            last_chunk = chunks.pop()
            chunks.append(last_chunk[:-leftover_bytes])
            leftover_chunks = [last_chunk[-leftover_bytes:]]

        self.chunks = leftover_chunks
        self.buf_size = leftover_bytes

        buf = b''.join(chunks)
        return buf


class HttpRpcProvider(HTTPProvider):
    """ http rpc provider """

    def __init__(self, ssl_args, url):
        """
        http rpc provider init

        :type  ssl_args: :class:`dict`
        :param ssl_args: ssl arguments
        :type  url: :class:`str`
        :param url: url to connected to
        """
        HTTPProvider.__init__(self)
        self.lock = threading.RLock()
        self.ssl_enabled = False
        self.ssl_args = ssl_args

        scheme, host, port, user, password, path, _ = parse_addr_url(url)
        assert(scheme == 'http' or scheme == 'https')
        if scheme == 'https':
            self.ssl_enabled = True
        assert(user is None and password is None)    # NYI
        if host.startswith('!'):
            # Unix domain socket: hostname is '!' followed by
            # the URL-encoded socket path
            self.host = None
            self.uds = urllib.parse.unquote(host[1:]).parse
            # SSL currently not supported for Unix domain sockets
            if self.ssl_enabled:
                raise Exception('SSL not supported on Unix domain sockets')
        else:
            self.host = host
            if port:
                self.host += ':%d' % port
            self.uds = None
        self.path = path
        self.cookie = ''
        self.accept_compress_response = True

        self.pool = []
        self.pool_size = 8
        self.connection_pool_timeout = 8 * 60    # 8 minutes

    def __del__(self):
        """ http rpc provider on delete """
        self.disconnect()

    def connect(self):
        """
        connect

        :rtype: :class:`vmware.vapi.protocol.client.rpc.provider.RpcProvider`
        :return: http rpc provider
        """
        return self

    def disconnect(self):
        """ disconnect """
        pass

    def _get_connection(self):
        """
        get connection from pool

        :rtype: :class:`http_client.HTTPConnection` (or)
            :class:`HttpsConnection` (or)
            :class:`UnixSocketConnection`
        :return: http(s) connection or unix socket connection
        """
        conn = None
        with self.lock:
            idle_connections = self._close_idle_connections()
            if self.pool:
                conn, _ = self.pool.pop(0)
        self._close_connections(idle_connections)

        if not conn:
            if self.ssl_enabled:
                conn = HttpsConnection(self.host, **self.ssl_args)
            elif self.uds:
                conn = UnixSocketConnection(self.uds)
            else:
                conn = http_client.HTTPConnection(self.host)

            # Disable Nagle
            self.disable_nagle(conn)
        else:
            # If we got an existing connection, verify the state
            # of the socket
            if self.is_connection_dropped(conn):
                conn.close()

        return conn

    ## Clean up connection pool to throw away idle timed-out connections
    #  SoapStubAdapter lock must be acquired before this method is called.
    def _close_idle_connections(self):
        """
        close all idle connections

        :rtype: :class:`http_client.HTTPConnection`
        :return: list of idle http connections
        """
        idle_connections = []
        if self.connection_pool_timeout >= 0:
            current_time = time.time()
            for idx, (_, last_access_time) in enumerate(self.pool):
                idle_time = current_time - last_access_time
                if idle_time >= self.connection_pool_timeout:
                    idle_connections = self.pool[idx:]
                    self.pool = self.pool[:idx]
                    break
        return idle_connections

    def _return_connection(self, conn):
        """
        return a connection to pool

        :type  conn: :class:`http_client.HTTPConnection`
        :param conn: http connection
        """
        with self.lock:
            if len(self.pool) < self.pool_size:
                self.pool.insert(0, (conn, time.time()))
                conn = None

        if conn:
            conn.close()

    def _drop_connections(self):
        """ drop all connections """
        with self.lock:
            connections = self.pool
            self.pool = []
        self._close_connections(connections)

    @staticmethod
    def is_connection_dropped(conn):
        """
        Returns True if the connection is dropped and should be closed.

        :type  conn: :class:`http_client.HTTPConnection`
        :param conn: HTTP connection object
        :rtype: :class:`bool`
        :return: True if the connection is dropped, False otherwise
        """
        sock = getattr(conn, 'sock', False)
        if not sock:
            return False

        if poll:
            # This version is better on platforms that support it.
            poll_obj = poll()
            poll_obj.register(sock, POLLIN)
            for (fno, _) in poll_obj.poll(0.0):
                if fno == sock.fileno():
                    # Either data is buffered (bad), or the connection is
                    # dropped.
                    return True
        elif select:
            try:
                # The return value is a triple of lists of objects that are
                # ready. If there is a socket error, then the return list
                # would be empty lists
                ready_objects = select([sock], [], [], 0.0)[0]
                return True if ready_objects else False

            except socket.error:
                return True

        return False

    @staticmethod
    def _close_connections(connections):
        """
        close a list of connections

        :type  connections: :class:`list` of :class:`http_client.HTTPConnection`
        :param connections: a list of http connections
        """
        for conn, _ in connections:
            conn.close()

    @staticmethod
    def disable_nagle(conn):
        """
        disable nagle algorithm for a connection

        :type  conn: :class:`http_client.HTTPConnection`
        :param conn: http connection
        """

        # Always disable NAGLE algorithm, but not for python 2.7
        # See pyVmomi/SoapAdapter.py for details
        if sys.version_info[:2] < (2, 7):
            return

        if not getattr(conn, 'connect'):
            return

        org_connect = conn.connect

        def connect_disable_nagle(*args, **kwargs):
            """ connect replacement with disable nagle """
            org_connect(*args, **kwargs)
            sock = getattr(conn, 'sock')
            if sock:
                try:
                    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                except Exception:
                    pass
        conn.connect = connect_disable_nagle

    def do_request(self, http_request):
        """
        Send an HTTP request

        :type  http_request: :class:`vmware.vapi.protocol.client.http_lib.HTTPRequest`
        :param http_request: The http request to be sent
        :rtype: :class:`vmware.vapi.protocol.client.http_lib.HTTPResponse`
        :return: The http response received
        """
        # pylint can't detect request, getresponse and close methods from
        # Http(s)Connection/UnixSocketConnection
        # pylint: disable=E1103
        request_ctx = http_request.headers
        request = http_request.body
        content_type = request_ctx.get('Content-Type')
        if not content_type:
            # For http, content-type must be set
            raise Exception('do_request: request_ctx content-type not set')

        response_ctx, response = {'Content-Type': content_type}, None
        if request:
            request_length = len(request)
            # Send request
            headers = {'Cookie': self.cookie,
                       'Content-Type': content_type}
            if self.accept_compress_response:
                headers['Accept-Encoding'] = 'gzip, deflate'

            try:
                conn = self._get_connection()
                logger.debug('do_request: request_len %d', request_length)

                conn.request('POST', self.path, request, headers)
                resp = conn.getresponse()
            except (socket.error, http_client.HTTPException):
                raise

            # Debug
            # logger.debug('do_request: response headers', resp.getheaders())

            cookie = resp.getheader('Set-Cookie')
            if cookie:
                self.cookie = cookie

            status = resp.status
            if status == 200 or status == 500:
                try:
                    encoding = resp.getheader('Content-Encoding', 'identity').lower()
                    if encoding == 'gzip':
                        resp_reader = GzipReader(resp, encoding=GzipReader.GZIP)
                    elif encoding == 'deflate':
                        resp_reader = GzipReader(resp, encoding=GzipReader.DEFLATE)
                    else:
                        resp_reader = resp
                    response = resp_reader.read()

                    logger.debug('do_request: response len %d', len(response))
                except:
                    conn.close()
                    raise
                else:
                    if resp_reader:
                        resp_reader.read()
                    self._return_connection(conn)

                content_type = resp.getheader('Content-Type')
                if content_type:
                    response_ctx['Content-Type'] = content_type
            else:
                conn.close()
                raise http_client.HTTPException('%d %s' % (resp.status, resp.reason))

            if self.cookie:
                response_ctx['Cookie'] = self.cookie
        return HTTPResponse(status=status, headers=response_ctx, body=response)
