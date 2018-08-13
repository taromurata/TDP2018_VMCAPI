#!/usr/bin/env python

"""
Unit tests for the double canonicalization
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2015 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import unittest
from decimal import Decimal

from vmware.vapi.lib.jsonlib import canonicalize_double

class TestJsonlib(unittest.TestCase):
    def test_double(self):
        for input_val, expected in [('3.33', '3.33E0'),
                                    ('3.0033', '3.0033E0'),
                                    ('3333.333', '3.333333E3'),
                                    ('3333.333000', '3.333333E3'),
                                    ('3333.0003000', '3.3330003E3'),
                                    ('-3333.333000', '-3.333333E3'),
                                    ('0.3333', '3.333E-1'),
                                    ('0.00333', '3.33E-3'),
                                    ('-0.00333', '-3.33E-3'),
                                    ('0', '0.0E0'),
                                    ('-0', '-0.0E0'),
                                    ('-0.0E-0', '-0.0E0'),
                                    ('+0', '0.0E0'),
                                    ('+0.00', '0.0E0'),
                                    ('-12.34E4', '-1.234E5'),
                                    ('1111111.1111100021e-30', '1.1111111111100021E-24'),
                                    ('0.000234E-10', '2.34E-14'),
                                    ('0.000234E+10', '2.34E6'),
                                   ]:
            actual_output = canonicalize_double(Decimal(input_val))
            self.assertEqual(actual_output, expected)


if __name__ == '__main__':
    unittest.main()
