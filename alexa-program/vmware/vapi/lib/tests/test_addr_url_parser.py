"""
Unit tests for addr_url_parser
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import six
import unittest

from vmware.vapi.lib.addr_url_parser import parse_addr_url

urls = [
   # url: scheme, host, port, user, password, path, query_dict
   (None, [None, None, None, None, None, None, None]),
   ('', [None, None, None, None, None, None, None]),

   # Not sure if the expected result is ok, but for invalid input, any reasonable result is ok
   ('?', ['', None, None, None, None, None, None]),
   ('@', ['', None, None, None, None, '@', None]),
   ('://', ['', None, None, None, None, '://', None]),

   ('${scheme}', ['', None, None, None, None, '${scheme}', None]),
   ('${scheme}:', ['${scheme}', None, None, None, None, None, None]),
   ('${scheme}://', ['${scheme}', None, None, None, None, None, None]),
   ('${scheme}:///', ['${scheme}', None, None, None, None, '/', None]),
   # This will fail for http on 2.6.1. Ignore this for now
   # ('${scheme}:////', ['${scheme}', None, None, None, None, '//', None]),
   ('${scheme}://${host}', ['${scheme}', '${host}', None, None, None, None, None]),
   ('${scheme}://user@${host}', ['${scheme}', '${host}', None, 'user', None, None, None]),
   ('${scheme}://user:@${host}', ['${scheme}', '${host}', None, 'user', '', None, None]),
   ('${scheme}://user:pass@${host}', ['${scheme}', '${host}', None, 'user', 'pass', None, None]),
   ('${scheme}://${host}:80', ['${scheme}', '${host}', 80, None, None, None, None]),
   ('${scheme}://user@${host}:80', ['${scheme}', '${host}', 80, 'user', None, None, None]),
   ('${scheme}://user:@${host}:80', ['${scheme}', '${host}', 80, 'user', '', None, None]),
   ('${scheme}://user:pass@${host}:80', ['${scheme}', '${host}', 80, 'user', 'pass', None, None]),
   ('${scheme}://${host}:80/', ['${scheme}', '${host}', 80, None, None, '/', None]),
   ('${scheme}://user@${host}:80/', ['${scheme}', '${host}', 80, 'user', None, '/', None]),
   ('${scheme}://user:@${host}:80/', ['${scheme}', '${host}', 80, 'user', '', '/', None]),
   ('${scheme}://user:pass@${host}:80/', ['${scheme}', '${host}', 80, 'user', 'pass', '/', None]),
   ('${scheme}://${host}:80/vapi', ['${scheme}', '${host}', 80, None, None, '/vapi', None]),
   ('${scheme}://user@${host}:80/vapi', ['${scheme}', '${host}', 80, 'user', None, '/vapi', None]),
   ('${scheme}://user:@${host}:80/vapi', ['${scheme}', '${host}', 80, 'user', '', '/vapi', None]),
   ('${scheme}://user:pass@${host}:80/vapi', ['${scheme}', '${host}', 80, 'user', 'pass', '/vapi', None]),
   ('${scheme}://${host}:80/vapi/', ['${scheme}', '${host}', 80, None, None, '/vapi/', None]),
   ('${scheme}://${host}:80/vapi/v0', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', None]),
   ('${scheme}://${host}:80/vapi/v0/', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', None]),

   # Query
   ('${scheme}://${host}:80/vapi/v0?', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', None]),
   ('${scheme}://${host}:80/vapi/v0?query_0', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', {}]),
   ('${scheme}://${host}:80/vapi/v0?query_0=', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', {}]),
   ('${scheme}://${host}:80/vapi/v0?query_0=0', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', {'query_0' : ['0']}]),
   ('${scheme}://${host}:80/vapi/v0?query_0=0&query_1=1', ['${scheme}', '${host}', 80, None, None, '/vapi/v0', {'query_0' : ['0'], 'query_1' : ['1']}]),

   ('${scheme}://${host}:80/vapi/v0/?', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', None]),
   ('${scheme}://${host}:80/vapi/v0/?query_0', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', {}]),
   ('${scheme}://${host}:80/vapi/v0/?query_0=', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', {}]),
   ('${scheme}://${host}:80/vapi/v0/?query_0=0', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', {'query_0' : ['0']}]),
   ('${scheme}://${host}:80/vapi/v0/?query_0=0&query_1=1', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', {'query_0' : ['0'], 'query_1' : ['1']}]),
   ('${scheme}://${host}:80/vapi/v0/?query_0=0&query_1=1&query_0=2', ['${scheme}', '${host}', 80, None, None, '/vapi/v0/', {'query_0' : ['0', '2'], 'query_1' : ['1']}]),

   ('${scheme}://user:pass@${host}:80/vapi/v0/?query_0=0&query_1=1&query_0=2', ['${scheme}', '${host}', 80, 'user', 'pass', '/vapi/v0/', {'query_0' : ['0', '2'], 'query_1' : ['1']}]),

   # Example from http://www.rabbitmq.com/uri-spec.html, not covered above
   # parse_addr_url don't unescape url
   # ('${scheme}://user%61:%61pass@ho%61st:10000/v%2fhost', ['${scheme}', 'hosta', 10000, 'usera', 'apass', 'v/host', None]),
   ('${scheme}://:@/', ['${scheme}', None, None, '', '', '/', None]),
   ('${scheme}://user@', ['${scheme}', None, None, 'user', None, None, None]),
   ('${scheme}://user:pass@', ['${scheme}', None, None, 'user', 'pass', None, None]),
   ('${scheme}://:80', ['${scheme}', None, 80, None, None, None, None]),
   ('${scheme}:///vhost', ['${scheme}', None, None, None, None, '/vhost', None]),

   # Proposed encoding for HTTP over Unix domain sockets: '!'
   # followed by URL-encoded socket path as the hostname.  See
   # http://lists.w3.org/Archives/Public/uri/2008Oct/0000.html
   ('${scheme}://!%2fvar%2frun%2fsock', ['${scheme}', '!%2fvar%2frun%2fsock', None, None, None, None, None]),
]

class TestAddrUrlParser(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

        global urls
        self.urls = urls
        self.schemes = ('amqp', 'http', 'vmware')
        self.hosts = ('[::1]', '[::]', '[2001:db8:1234::]',
                      '[::ffff:192.0.2.128]',
                      '[2001:db8:85a3::8a2e:370:7334]',
                      'localhost', '127.0.0.1')

    def sub_vars(self, input, vars):
        result = input
        if result and isinstance(result, six.string_types):
            for key, val in six.iteritems(vars):
                result = result.replace(key, val)
        return result

    def test_urls(self):
        for scheme in self.schemes:
            for host in self.hosts:
                substitution_vars = {'${scheme}': scheme, '${host}': host}
                for url, answer in self.urls:
                    test_url = self.sub_vars(url, substitution_vars)
                    expected_answer = [self.sub_vars(token, substitution_vars)
                                                           for token in answer]

                    test_answer = parse_addr_url(test_url)
                    if list(test_answer) != expected_answer:
                        logging.info('url: %s' % test_url)
                        logging.info('got     : %s' % list(test_answer))
                        logging.info('expected: %s' % expected_answer)
                        self.assertTrue(False)
