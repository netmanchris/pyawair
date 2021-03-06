# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.objects module.
"""

from unittest import TestCase
from unittest import mock
from pyawair.objects import *
from pyawair.auth import AwairAuth
from pyawair.devices import get_all_devices

hobbiest = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktSE9CQllJU1QifQ.hzjhIpGljqCZ8vCrOr89POy_ENDPYQXsnzGslP01krI'
small_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktU01BTExfREVWRUxPUEVSIn0.amOu5uy-0UeBDRLd6uhqsbkUEyx13-4QdBrV1S3z2W8'
large_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktTEFSR0VfREVWRUxPUEVSIn0.JmP9a0eGjgYRlmri5BjNj4h1hlAZ-7yFOjcIZjyzypA'
enterprise_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktRU5URVJQUklTRSJ9.bOM9rcABF9HKFHtxzF9kx8h9fv3CfvUIzveLFDRGrXs'

auth = AwairAuth(enterprise_dev)
dev1 = get_all_devices(auth)[0]

class TestGetCurrentAirData(TestCase):
    """
    Test Case for pyawair.objects AwairDev class
    """


    def test_create_AwairDev_pos(self):
        """
        """
        new_device = AwairDev(dev1['name'], auth)
        self.assertEqual(new_device._type, 'awair')
        self.assertEqual(new_device._id, 0)
        self.assertEqual(new_device._device_name, dev1['name'])


    def test_get_state_method(self):
        new_device = AwairDev(dev1['name'], auth)
        score = new_device.get_state('score')
        self.assertEqual(score, 90.0)
        score = new_device.get_state('temp')
        self.assertEqual(score, 69.45)
        score = new_device.get_state('humid')
        self.assertEqual(score, 49.92)
        score = new_device.get_state('co2')
        self.assertEqual(score, 419.0)
        score = new_device.get_state('voc')
        self.assertEqual(score, 399.0)
        score = new_device.get_state('dust')
        self.assertEqual(score, 56.8)
        #score = new_device.get_state('pm10')
        #self.assertEqual(score, 100.0)


    def test_get_name_method(self):
        new_device = AwairDev(dev1['name'], auth)
        name = new_device.name()
        self.assertEqual(name, dev1['name'])


    def test_get_type_method(self):
        new_device = AwairDev(dev1['name'], auth)
        dev_type = new_device.type()
        self.assertEqual(dev_type, dev1['deviceType'])


    def test_get_id_method(self):
        new_device = AwairDev(dev1['name'], auth)
        dev_id = new_device.id()
        self.assertEqual(dev_id, dev1['deviceId'])


    def test_aggregate_type_default_pos(self):
        new_device = AwairDev(dev1['name'], auth)
        self.assertEqual(new_device._aggregate_type, '15-minute')


    def test_aggregate_type_current_pos(self):
        new_device = AwairDev(dev1['name'], auth, aggregate_type='current')
        self.assertEqual(new_device._aggregate_type, 'current')


    def test_aggregate_type_5min_pos(self):
        new_device = AwairDev(dev1['name'], auth, aggregate_type='5-minute')
        self.assertEqual(new_device._aggregate_type, '5-minute')


    def test_aggregate_type_invalid(self):
        with self.assertRaises(ValueError):
            new_device = AwairDev(dev1['name'], auth, aggregate_type='10-minute')


    def test_device_name_invalid(self):
        with self.assertRaises(ValueError):
            new_device = AwairDev('banana', auth)


    def test_refresh_type_default_pos(self):
        new_device = AwairDev(dev1['name'], auth)
        new_device.refresh()
        self.assertEqual(new_device._data['score'], 90.0)


    def test_refresh_type_current_pos(self):
        new_device = AwairDev(dev1['name'], auth, aggregate_type='current')
        new_device.refresh()
        self.assertEqual(new_device._data['score'], 90.0)


    def test_refresh_type_5min_pos(self):
        new_device = AwairDev(dev1['name'], auth, aggregate_type='5-minute')
        new_device.refresh()
        self.assertEqual(new_device._data['score'], 90.0)





