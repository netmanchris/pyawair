# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.
"""

from unittest import TestCase
from secret import *
from pyawair.devices import *

dev1="Bedroom Awair"   #Modify this variable to test against your own devices



# TODO Remarked out failing tests


class TestGetUserData(TestCase):
    """
    Test Case for pyawair.devices get_user_data function
    """

    def test_get_user_data(self):
        """
        """
        user_data = get_user_data(auth)
        self.assertIs(type(user_data['dobDay']), int)
        self.assertIs(type(user_data['dobMonth']), int)
        self.assertIs(type(user_data['dobYear']), int)
        self.assertIs(type(user_data['email']), str)
        self.assertIs(type(user_data['firstName']), str)
        self.assertIs(type(user_data['lastName']), str)
        self.assertIs(type(user_data['id']), str)


class TestGetAllDevices(TestCase):
    """
    Test Case for pyawair.devices get_all_devices function
    """

    def test_get_all_devices(self):
        """
        """
        all_devices = get_all_devices(auth)
        self.assertIs(type(all_devices[0]['deviceId']), int)
        self.assertIs(type(all_devices[0]['deviceType']), str)
        self.assertIs(type(all_devices[0]['latitude']), float)
        self.assertIs(type(all_devices[0]['locationName']), str)
        self.assertIs(type(all_devices[0]['longitude']), float)
        self.assertIs(type(all_devices[0]['name']), str)

class TestGetDevDetails(TestCase):
    """
    Test Case for pyawair.devices get_device_details function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_details_pos(self):
        """
        Positive Test Case
        """
        single_device = get_dev_details(auth, device_name=dev1)
        self.assertIs(type(single_device['deviceId']), int)
        self.assertIs(type(single_device['deviceType']), str)
        self.assertIs(type(single_device['latitude']), float)
        self.assertIs(type(single_device['locationName']), str)
        self.assertIs(type(single_device['longitude']), float)
        self.assertIs(type(single_device['name']), str)

    def test_get_dev_details_neg(self):
        """
        Negative Test case
        :return:
        """
        pass


class TestGetDevLEDMode(TestCase):
    """
    Test Case for pyawair.devices get_dev_led_mode function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_led_mode_pos(self):
        """
        Positive Test case
        """
        led_mode = get_dev_led_mode(auth, device_name=dev1)
        modes=["sleep", "on", "dim"]
        self.assertIn(led_mode['mode'].lower(), modes)


class TestGetDevTimeZone(TestCase):
    """
    Test Case for pyawair.devices get_dev_timezone function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_timezone_pos(self):
        """
        Positive Test case
        """
        timezone = get_dev_timezone(auth, device_name=dev1)
        self.assertIs(type(timezone['timezone']), str)


class TestGetDevDisplayMode(TestCase):
    """
    Test Case for pyawair.devices get_dev_display_mode function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_display_mode_pos(self):
        """
        Positive Test case
        """
        display_mode = get_dev_display_mode(auth, device_name=dev1)
        modes=["default", "score", "clock" ,"off" ,"nightlight", "temp", "humid",
               "co2", "voc", "pm25", "temp_humid_celsius", "temp_humid_fahrenheit"]
        self.assertIn(display_mode['mode'].lower(), modes)


class TestGetDevPowerStatus(TestCase):
    """
    Test Case for pyawair.devices get_dev_power_status function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_power_status_pos(self):
        """
        Positive Test case
        """
        power_status = get_dev_power_status(auth, device_name=dev1)
        self.assertIs(type(power_status['message']), str)


class TestSetDevicePreference(TestCase):
    """
    Test Case for pyawair.devices set_dev_preference function for a single
    device name "Bedroom_Awair"
    ['general', 'productivity', 'sleep', 'allergy', 'baby']
    """

    def test_set_dev_preference_pos_general(self):
        """
        Positive Test case
        """
        mode = 'general'
        preference = set_device_preference(auth, mode, device_name=dev1)
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'],"success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['preference'].lower(), mode )

    def test_set_dev_preference_pos_sleep(self):
        """
        Positive Test case
        """
        mode = 'sleep'
        preference = set_device_preference(auth, mode, device_name=dev1)
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_productivity(self):
        """
        Positive Test case
        """
        mode = 'productivity'
        preference = set_device_preference(auth, mode, device_name=dev1)
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_baby(self):
        """
        Positive Test case
        """
        mode = 'baby'
        preference = set_device_preference(auth, mode, device_name=dev1)
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_allergy(self):
        """
        Positive Test case
        """
        mode = 'allergy'
        preference = set_device_preference(auth, mode, device_name=dev1)
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['preference'].lower(), mode)


class TestSetDeviceTimezone(TestCase):
    """
    Test Case for pyawair.devices set_dev_timezone function for a single
    device name "Bedroom_Awair"
    ['general', 'productivity', 'sleep', 'allergy', 'baby']
    """

    def test_set_dev_timezone_pos(self):
        """
        Positive Test case
        """
        new_timezone = "America/Montreal"
        timezone = set_device_timezone(auth, new_timezone, device_name=dev1)
        self.assertIs(type(timezone['message']), str)
        self.assertEquals(timezone['message'],"success")
        dev_details = get_dev_details(auth, device_name=dev1)
        self.assertEquals(dev_details['timezone'].lower(), new_timezone.lower() )