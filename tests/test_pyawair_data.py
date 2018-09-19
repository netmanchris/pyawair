# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.data module.
"""

from unittest import TestCase
from secret import *
from pyawair.data import *

dev1 = 'Bedroom'

hobbiest = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktSE9CQllJU1QifQ.hzjhIpGljqCZ8vCrOr89POy_ENDPYQXsnzGslP01krI'
small_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktU01BTExfREVWRUxPUEVSIn0.amOu5uy-0UeBDRLd6uhqsbkUEyx13-4QdBrV1S3z2W8'
large_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktTEFSR0VfREVWRUxPUEVSIn0.JmP9a0eGjgYRlmri5BjNj4h1hlAZ-7yFOjcIZjyzypA'
enterprise_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktRU5URVJQUklTRSJ9.bOM9rcABF9HKFHtxzF9kx8h9fv3CfvUIzveLFDRGrXs'

auth = pyawair.auth.AwairAuth(enterprise_dev)

# TODO Remarked out failing tests


class TestGetCurrentAirData(TestCase):
    """
    Test Case for pyawair.data get_current_air_data function
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