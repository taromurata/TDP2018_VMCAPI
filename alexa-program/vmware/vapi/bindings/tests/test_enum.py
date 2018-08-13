#!/usr/bin/env python
"""
Unit tests for python Enum class
"""

__author__ = 'VMware, Inc.'
__copyright__ = 'Copyright 2016 VMware, Inc.  All rights reserved. -- VMware Confidential'  # pylint: disable=line-too-long

import logging
import unittest

from vmware.vapi.bindings.enum import Enum
from vmware.vapi.bindings.type import EnumType

class PowerState(Enum):
    """
    The ``PowerState`` class defines the valid power states for a virtual
    machine.
    """
    POWERED_OFF = None
    """
    The virtual machine is powered off.

    """
    POWERED_ON = None
    """
    The virtual machine is powered on.

    """
    SUSPENDED = None
    """
    The virtual machine is suspended.

    """

    def __init__(self, string):
        """
        :type  string: :class:`str`
        :param string: String value for the :class:`State` instance.
        """
        Enum.__init__(string)

PowerState._set_values([
    PowerState('POWERED_OFF'),
    PowerState('POWERED_ON'),
    PowerState('SUSPENDED')
    ])
PowerState._set_binding_type(EnumType('vm.power.state', PowerState))


class TestVapiEnum(unittest.TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.INFO)

    def test_get_values(self):
        actual_values = PowerState.get_values()
        expected_values = [PowerState.POWERED_ON, PowerState.POWERED_OFF,
                           PowerState.SUSPENDED]
        self.assertEqual(set(actual_values), set(expected_values))
        expected_values2 = ['POWERED_ON', 'POWERED_OFF', 'SUSPENDED']
        self.assertEqual(set(actual_values), set(expected_values2))

    def test_is_unknown_with_known_val(self):
        val = PowerState.POWERED_ON
        self.assertFalse(val.is_unknown())

    def test_is_unknown_with_unknown_val(self):
        val = PowerState('RANDOM')
        self.assertTrue(val.is_unknown())

if __name__ == '__main__':
    unittest.main()
