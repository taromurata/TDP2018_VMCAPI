#!/usr/bin/env python
"""
Asyncore server
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015, 2017 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import asyncore
import six
import socket
import ssl

from six.moves import urllib
from six.moves import queue
from vmware.vapi.server.server_interface import ServerInterface
from vmware.vapi.lib.addr_url_parser import parse_addr_url
from vmware.vapi.lib.log import get_vapi_logger
from vmware.vapi.server.asyncore_http import HttpFactory


logger = get_vapi_logger(__name__)


class SyncWriteToAsyncWriteAdapter(object):
    """ Sync write to async write adapter """

    def __init__(self, async_socket):
        """
        Sync write to async write adapter init

        :type  async_socket: :class:`socket.socket`
        :param async_socket: async socket
        """
        self.buf = None
        self.async_socket = async_socket
        self.is_closed = False
        self.queue = queue.Queue()

        # Test if TCP_CORK is available on this socket
        try:
            self.tcp_cork(0)
            self.use_cork = True
        except socket.error:
            self.use_cork = False

    def tcp_cork(self, enable):
        """
        tcp cork

        Python failed to merge small send into big packet, which is
        very inefficient. Use TCP_CORK to queue partial packets to bigger
        packet before sending it. Alternatively we should use writev, but
        it is not available on standard python socket lib.

        :type  enable: :class:`int`
        :param enable: 1 => turn TCP_CORK on, 0 => off
        :raise: :class:`socket.error` if TCP_CORK is not supported on this
            socket
        """
        self.async_socket.setsockopt(
            socket.IPPROTO_TCP, socket.TCP_CORK, enable)

    def write_ready(self):
        """ write ready callback """
        if not self.async_socket:
            return

        if self.use_cork:
            self.tcp_cork(1)

        while True:
            if self.buf:
                data = self.buf
                self.buf = None
            else:
                try:
                    data = self.queue.get(block=False)
                except queue.Empty:
                    break
                self.queue.task_done()
                if not data:
                    self.async_socket.close()
                    self.async_socket = None
                    return

            data_len = len(data)
            bytes_send = self.async_socket.send(data)
            if bytes_send < data_len:
                self.buf = data[bytes_send:]   # Save the leftover
                break

        if self.use_cork:
            self.tcp_cork(0)

    def write(self, data):
        """
        Write the given bytes

        :type  data: :class:`bytes`
        :param data: data to write
        """
        if not self.is_closed and data:
            # NYI: Make it more efficient: e.g. direct write if marked writable
            # NYI: Possible to block if running out of buffer
            self.queue.put(data)

    def writable(self):
        """
        Have something to write to http connection?

        :rtype  :class:`bool`
        :return True if data is ready to write
        """
        return (self.buf or (not self.queue.empty()))

    def close(self):
        """ close """
        self.close_when_done()

        # Flush chunks
        self.flush()

    def close_when_done(self):
        """ close when all data written """
        if not self.is_closed:
            # No more write
            self.is_closed = True
            self.queue.put(None)   # None in queue => close eventually

    def flush(self):
        """ flush """
        if self.writable():
            # Interrupt loop to indicate write ready
            try:
                # Flush could be called after async_socket is None. Ignore error
                self.async_socket.server.loop_controller.intr()
            except Exception:
                pass

    def __del__(self):
        """ on delete """
        self.close()

    def __enter__(self):
        """ with statement enter """
        return self

    def __exit__(self, typ, val, traceback):
        """ with statement exit """
        self.close()


class AsyncoreSslConnection(asyncore.dispatcher):
    """ Asyncore ssl connection """

    def __init__(self, server, sock_map, sock, from_addr, protocol_factory):
        """
        Asyncore ssl connection init

        :type  server:
            :class:`vmware.vapi.server.asyncore_server.AsyncoreTcpListener`
        :param server: asyncore server
        :type  sock_map: :class:`dict`
        :param sock_map: Global socket map
        :type  sock: :class:`socket.socket`
        :param sock: connection socket
        :type  from_addr: :class:`tuple`
        :param from_addr: remote address bound to the socket
        :type  protocol_factory: :class:`object` with method handle_accept
        :param protocol_factory: protocol factory
        """
        try:
            asyncore.dispatcher.__init__(self, sock, map=sock_map)
            self.server = server
            self.sock_map = sock_map
            self.sock = sock
            self.from_addr = from_addr
            self.is_read_ready = True
            self.is_write_ready = False

            self.protocol_factory = protocol_factory
        except Exception:
            self.cleanup()
            raise

    def cleanup(self, close_socket=False):
        """
        connection cleanup

        :type  close_socket: :class:`bool`
        :param close_socket: close internal socket (or not)
        """
        try:
            self.del_channel()
        except Exception:
            pass
        self.server = None
        self.sock_map = None
        self.from_addr = None
        if close_socket:
            if self.sock is not None:
                self.sock.close()
                self.sock = None
        self.is_read_ready = False
        self.is_write_ready = False

        self.protocol_factory = None

    def do_handshake_continue(self):
        """ ssl do handshake continue """
        try:
            self.sock.do_handshake()
            # No exception. Hand shake done

            # Remove ssl handler from sock map
            self.del_channel()

            # Pass control to protocol factory
            self.protocol_factory.handle_accept(self.server, self.sock_map,
                                                self.sock, self.from_addr)

            # Unref ssl handler
            self.cleanup()
        except ssl.SSLError as err:
            if err.args[0] == ssl.SSL_ERROR_WANT_READ:
                self.is_read_ready = True
            elif err.args[0] == ssl.SSL_ERROR_WANT_WRITE:
                self.is_write_ready = True
                # Write ready
                self.server.loop_controller.intr()
            else:
                # SSL exception
                self.cleanup(close_socket=True)
                raise

    def handle_read(self):
        """ read data available callback """
        if self.is_read_ready:
            self.is_read_ready = False
            self.do_handshake_continue()

    def handle_write(self):
        """ write ready callback """
        if self.is_write_ready:
            self.is_write_ready = False
            self.do_handshake_continue()

    def readable(self):
        """
        Can read more data?

        :rtype  :class:`bool`
        :return True if this can handle more data
        """
        return self.is_read_ready

    def writable(self):
        """
        Have something to write to ssl connection?

        :rtype  :class:`bool`
        :return True if data is ready to write
        """
        return self.is_write_ready

    def handle_close(self):
        """ handle close callback """
        self.cleanup(close_socket=True)

    def handle_error(self):
        """ handle error callback """
        self.cleanup(close_socket=True)

    def handle_expt(self):
        """ handle exception callback """
        self.cleanup(close_socket=True)


class AsyncoreTcpListener(asyncore.dispatcher):
    """ Asyncore tcp listener """

    def __init__(
            self, loop_controller, sock_map, addr, ssl_args, protocol_factory):
        """
        Asyncore tcp listener init

        :type  loop_controller: :class:`AsyncoreLoopController`
        :param loop_controller: loop controller
        :type  sock_map: :class:`dict`
        :param sock_map: Global socket map
        :type  addr: :class:`tuple` of :class:`str`, :class:`int`
        :param addr: tcp addr and port
        :type  ssl_args: :class:`dict`
        :param ssl_args: ssl arguments
        :type  protocol_factory: :class:`object` with method handle_accept
        :param protocol_factory: protocol factory
        """
        self.loop_controller = loop_controller
        self.sock_map = sock_map
        asyncore.dispatcher.__init__(self, map=self.sock_map)

        # Init ssl
        self.ssl_args = None
        self.ssl_wrap_socket = None
        self.init_ssl(ssl_args)

        # Setup server
        if addr[0].startswith('!'):
            # Unix domain socket: hostname is '!' followed by the URL-encoded
            # socket path; socket.bind expects the path as a string argument.
            addr = urllib.parse.unquote(addr[0][1:])
            sock_family = socket.AF_UNIX
        else:
            sock_family = socket.AF_INET
        self.create_socket(sock_family, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(addr)
        self.listen(5)

        assert(protocol_factory)
        self.protocol_factory = protocol_factory

    def init_ssl(self, ssl_args):
        """
        Setup SSL arguments

        :type  ssl_args: :class:`dict`
        :param ssl_args: ssl arguments
        """

        self.ssl_args = None
        try:
            _ssl_args = {}

            # Override ssl arguments
            if ssl_args:
                for key, val in six.iteritems(ssl_args):
                    # func_code dose exist for callable object
                    # pylint: disable=E1101
                    if key in six.get_function_code(
                            ssl.wrap_socket).co_varnames:
                        _ssl_args.setdefault(key, val)

            if len(_ssl_args) > 0:
                # server_side is always True
                _ssl_args.setdefault('server_side', True)
                # Async handshake
                _ssl_args.setdefault('do_handshake_on_connect', False)
                self.ssl_args = _ssl_args

            self.ssl_wrap_socket = ssl.wrap_socket
        except ImportError:
            pass

    def handle_accept(self):
        """ accept connection callback """

        new_socket = None
        try:
            new_socket, from_addr = self.accept()

            if not new_socket:
                logger.debug('Accept failed. Client closed?')
                return

            logger.debug('Connection from: %s', from_addr)

            # Disable nagle
            # NYI: In theory don't need this, but response is slower without
            #      setting TCP_NODELAY. Bug in python 2.6 httplib?
            try:
                new_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
            except Exception as e:
                logger.error('Error disabling nagle: %s', e)

            if self.ssl_args is not None:
                new_socket = self.ssl_wrap_socket(new_socket, **self.ssl_args)
                AsyncoreSslConnection(self, self.sock_map, new_socket,
                                      from_addr, self.protocol_factory)
            else:
                self.protocol_factory.handle_accept(self, self.sock_map,
                                                    new_socket, from_addr)
        except Exception as e:
            logger.error('Error accepting connection: %s', e)
            # Cleanup
            if new_socket:
                new_socket.shutdown(socket.SHUT_RDWR)
                new_socket.close()
                new_socket = None

    def writable(self):
        """
        Have something to write to this connection?

        :rtype  :class:`bool`
        :return True if data is ready to write
        """
        return False

    def handle_close(self):
        """ handle close callback """
        self.close()

    def handle_error(self):
        """ handle error callback """
        # Handle exception
        pass

    def handle_expt(self):
        """ handle exception callback """
        logger.debug('Accept failed. Client closed?')

    ## End asyncore.dispatcher interface


class AsyncoreLoopController(asyncore.dispatcher):
    """ Asyncore loop controller """

    def __init__(self, sock_map):
        """
        Asyncore loop controller init

        :type  sock_map: :class:`dict`
        :param sock_map: Global socket map
        """
        # Create our own contol channel
        sck = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sck.bind(('localhost', 0))
        sck.connect(sck.getsockname())
        asyncore.dispatcher.__init__(self, sck, sock_map)

    def intr(self):
        """ Interrupt the asyncore loop """
        try:
            self.send(b'i')
        except socket.error:
            self.handle_error()

    ## Begin asyncore.dispatcher interface

    def readable(self):
        """
        Can accept more data?

        :rtype  :class:`bool`
        :return True if this can handle more data
        """
        return True

    def writable(self):
        """
        Have something to write to this connection?

        :rtype  :class:`bool`
        :return True if data is ready to write
        """
        return False

    def handle_read(self):
        """ read data available callback """
        try:
            _ = self.recv(1024)
        except socket.error:
            self.handle_error()

    def handle_close(self):
        """ handle close callback """
        self.close()

    def handle_error(self):
        """ handle error callback """
        pass

    def handle_expt(self):
        """ handle exception callback """
        pass

    ## End asyncore.dispatcher interface


class AsyncoreTcpServer(ServerInterface):
    """ Asyncore tcp server """

    SUPPORTED_SCHEMES = ('http', 'https')

    def __init__(self):
        """ Asyncore tcp server init """
        ServerInterface.__init__(self)
        self.handlers_map = {}
        self.sock_map = {}

        self.protocol_factories = {}

    def register_handler(self, addr, msg_type, protocol_handler, ssl_args=None):
        """
        Register protocol handler

        :type  addr: :class:`str`
        :param addr: addr url
        :type  msg_type: :class:`str`
        :param msg_type: protocol message type
        :type  protocol_handler: :class:`vmware.vapi.protocol.server.transport.\
            async_protocol_handler.AsyncProtocolHandler`
        :param protocol_handler: protocol handler for this addr
        :type  ssl_args: :class:`dict`
        :param ssl_args: ssl arguments
        """

        logger.info("register_handler: msg: %s addr: %s", msg_type, addr)

        # addr is in the form of url
        scheme, host, port, _, _, path, _ = parse_addr_url(addr)
        if host is None:
            host = ''

        if scheme not in self.SUPPORTED_SCHEMES:
            logger.error('Unsupported url scheme: %s', addr)
            return

        if not protocol_handler:
            logger.error('No protocol handler: %s', addr)
            return

        if scheme not in ('https'):
            ssl_args = None

        if scheme in ('http', 'https'):
            protocol_factory = self.protocol_factories.get(('http', port))
            if not protocol_factory:
                protocol_factory = HttpFactory()
                self.protocol_factories[('http', port)] = protocol_factory
            protocol_factory.add_handler(path, msg_type, protocol_handler)

        self.handlers_map[(host, port)] = (protocol_factory, ssl_args)

    def serve_forever(self):
        """ Server loop """
        # Add contol channel
        loop_controller = AsyncoreLoopController(self.sock_map)

        for addr, (protocol_factory, ssl_args) \
                in six.iteritems(self.handlers_map):
            logger.info('Listening on: %s %s', addr, ssl_args)
            AsyncoreTcpListener(loop_controller, self.sock_map, addr,
                                ssl_args, protocol_factory)
        try:
            asyncore.loop(timeout=-1, use_poll=True, map=self.sock_map)
        except KeyboardInterrupt:
            pass
        self.shutdown()

    def shutdown(self):
        """ Server shutdown """

        if self.sock_map:
            asyncore.close_all(map=self.sock_map)
            self.sock_map = None


def get_server():
    """
    Get asyncore server

    :rtype: :class:`vmware.vapi.server.server_interface.ServerInterface`
    :return: subclass of ServerInterface
    """

    # Returns server with ServerInterface
    args = tuple()
    kwargs = {}

    # NYI: Singleton
    server = AsyncoreTcpServer(*args, **kwargs)
    return server
