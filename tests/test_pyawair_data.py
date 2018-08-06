# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.
"""

from unittest import TestCase
from secret import *
from pyawair.data import *

#dev1="Bedroom Awair"   #Modify this variable to test against your own devices
dev1="Bedroom Glow"


# TODO Remarked out failing tests


class TestGetCurrentAirData(TestCase):
    """
    Test Case for pyawair.devices get_current_air_data function
    """

    def test_get_current_air(self):
        """
        """
        get_current_air = get_current_air_data(auth, device_name=dev1)
        self.assertIs(type(get_current_air[0]), dict)
        self.assertIs(type(get_current_air[0]['timestamp']), str)
        self.assertIs(type(get_current_air[0]['indices']), list)
        self.assertIs(type(get_current_air[0]['score']), float)
        self.assertIs(type(get_current_air[0]['sensors']), list)

class TestGet5MinAverage(TestCase):
    """
    Test Case for pyawair.devices get_5_min_average function
    """

    def test_get_5Min_air(self):
        """
        """
        get_5min_air = get_5_min_average(auth, device_name=dev1)
        self.assertIs(type(get_5min_air[0]), dict)
        self.assertIs(type(get_5min_air[0]['timestamp']), str)
        self.assertIs(type(get_5min_air[0]['indices']), list)
        self.assertIs(type(get_5min_air[0]['score']), float)
        self.assertIs(type(get_5min_air[0]['sensors']), list)


class TestGet15MinAverage(TestCase):
    """
    Test Case for pyawair.devices get_15_min_average function
    """

    def test_get_15Min_air(self):
        """
        """
        get_15min_air = get_15_min_average(auth, device_name=dev1)
        self.assertIs(type(get_15min_air[0]), dict)
        self.assertIs(type(get_15min_air[0]['timestamp']), str)
        self.assertIs(type(get_15min_air[0]['indices']), list)
        self.assertIs(type(get_15min_air[0]['score']), float)
        self.assertIs(type(get_15min_air[0]['sensors']), list)


class TestGetRawData(TestCase):
    """
    Test Case for pyawair.devices get_raw_data function
    """

    def test_get_raw_air(self):
        """
        """
        get_raw_air = get_raw_data(auth, device_name=dev1)
        self.assertIs(type(get_raw_air[0]), dict)
        self.assertIs(type(get_raw_air[0]['timestamp']), str)
        self.assertIs(type(get_raw_air[0]['indices']), list)
        self.assertIs(type(get_raw_air[0]['score']), float)
        self.assertIs(type(get_raw_air[0]['sensors']), list)