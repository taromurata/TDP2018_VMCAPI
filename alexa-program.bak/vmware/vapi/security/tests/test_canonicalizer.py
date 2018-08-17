"""
Unit tests for JSON canonicalization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
import os

from vmware.vapi.security.sso import JSONCanonicalizer

DATA_DIR =  os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources')


class TestCanonicalizer(unittest.TestCase):

    def setUp(self):
        self._inputs = []
        self._outputs = []
        file_data = None
        with open(os.path.join(DATA_DIR, 'json-canonicalizer.data'), 'r') as fp:
            file_data = fp.read()

        file_data = file_data.split('Input:')
        self._num_tests = int(file_data[0].strip())
        for data in file_data[1:]:
            input_data, output_data = data.split('Canonical form:')
            input_data, output_data = input_data.strip(), output_data.strip()
            self._inputs.append(input_data)
            self._outputs.append(output_data)

    def test_canonical(self):
        for num in range(self._num_tests):
            self.assertEqual(JSONCanonicalizer.canonicalize(self._inputs[num]),
                             self._outputs[num])

if __name__ == '__main__':
    unittest.main()
