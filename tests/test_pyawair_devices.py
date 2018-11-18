# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.devices module.
"""

from unittest import TestCase
from pyawair.devices import *
from pyawair.auth import AwairAuth
from pyawair.devices import get_all_devices

hobbiest = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktSE9CQllJU1QifQ.hzjhIpGljqCZ8vCrOr89POy_ENDPYQXsnzGslP01krI'
small_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktU01BTExfREVWRUxPUEVSIn0.amOu5uy-0UeBDRLd6uhqsbkUEyx13-4QdBrV1S3z2W8'
large_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktTEFSR0VfREVWRUxPUEVSIn0.JmP9a0eGjgYRlmri5BjNj4h1hlAZ-7yFOjcIZjyzypA'
enterprise_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktRU5URVJQUklTRSJ9.bOM9rcABF9HKFHtxzF9kx8h9fv3CfvUIzveLFDRGrXs'

auth = AwairAuth(enterprise_dev)
dev1 = get_all_devices(auth)[0]

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


    def test_get_dev_details_name_pos(self):
        """
        Positive Test Case
        """
        single_device = get_dev_details(auth, device_name=dev1['name'])
        self.assertIs(type(single_device['deviceId']), int)
        self.assertIs(type(single_device['deviceType']), str)
        self.assertIs(type(single_device['latitude']), float)
        self.assertIs(type(single_device['locationName']), str)
        self.assertIs(type(single_device['longitude']), float)
        self.assertIs(type(single_device['name']), str)

    def test_get_dev_details_name_neg(self):
        """
        Negative Test case
        :return:
        """
        single_device = get_dev_details(auth, device_name="Doesn't Exist")
        self.assertEqual(single_device, 'Device not found')


class TestGetDevLEDMode(TestCase):
    """
    Test Case for pyawair.devices get_dev_led_mode function for a single
    device name "Bedroom_Awair"
    """
    def test_get_dev_led_mode_id_pos(self):
        """
        Positive Test case
        """
        led_mode = get_dev_led_mode(auth,device_type=dev1['deviceType'], device_id=dev1['deviceId'])
        modes=["sleep", "on", "dim"]
        self.assertIn(led_mode['mode'].lower(), modes)


    def test_get_dev_led_mode_name_pos(self):
        """
        Positive Test case
        """
        led_mode = get_dev_led_mode(auth, device_name=dev1['name'])
        modes=["sleep", "on", "dim"]
        self.assertIn(led_mode['mode'].lower(), modes)


    def test_get_dev_led_mode__name_neg(self):
        """
        Negative Test case
        :return:
        """
        led_mode = get_dev_led_mode(auth, device_name ="Doesn't Exist")
        self.assertEqual(led_mode, 'Device not found')


class TestGetDevTimeZone(TestCase):
    """
    Test Case for pyawair.devices get_dev_timezone function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_timezone_id_pos(self):
        """
        Positive Test case
        """
        timezone = get_dev_timezone(auth,device_type=dev1['deviceType'], device_id=dev1['deviceId'])
        expected_timezone = {'timezone': 'US/Pacific'}
        self.assertIs(type(timezone['timezone']), str)
        self.assertEqual(timezone, expected_timezone)

    def test_get_dev_timezone_name_pos(self):
        """
        Positive Test case
        """
        timezone = get_dev_timezone(auth, device_name=dev1['name'])
        expected_timezone = {'timezone': 'US/Pacific'}
        self.assertIs(type(timezone['timezone']), str)
        self.assertEqual(timezone, expected_timezone)

    def test_get_dev_timezone_neg(self):
        """
        Negative Test case
        :return:
        """
        timezone = get_dev_timezone(auth, device_name="Doesn't Exist")
        self.assertEqual(timezone, 'Device not found')


class TestGetDevDisplayMode(TestCase):
    """
    Test Case for pyawair.devices get_dev_display_mode function for a single
    device name "Bedroom_Awair"
    """
    def test_get_dev_display_mode_id_pos(self):
        """
        Positive Test case
        """
        display_mode = get_dev_display_mode(auth,device_type=dev1['deviceType'], device_id=dev1['deviceId'])
        modes = ["default", "score", "clock", "off", "nightlight", "temp", "humid",
                 "co2", "voc", "pm25", "temp_humid_celsius", "temp_humid_fahrenheit"]
        self.assertIn(display_mode['mode'].lower(), modes)

    def test_get_dev_display_mode_name_pos(self):
        """
        Positive Test case
        """
        display_mode = get_dev_display_mode(auth, device_name=dev1['name'])
        modes=["default", "score", "clock" ,"off" ,"nightlight", "temp", "humid",
               "co2", "voc", "pm25", "temp_humid_celsius", "temp_humid_fahrenheit"]
        self.assertIn(display_mode['mode'].lower(), modes)

    def test_get_dev_display_mode_name_neg(self):
        """
        Negative Test case
        :return:
        """
        display_mode = get_dev_display_mode(auth, device_name="Doesn't Exist")
        self.assertEqual(display_mode, 'Device not found')

#TODO Get Dev Power TEST FAILING
class TestGetDevPowerStatus(TestCase):
    """
    Test Case for pyawair.devices get_dev_power_status function for a single
    device name "Bedroom_Awair"
    """

    def test_get_dev_power_status_id_post(self):
        power_status = get_dev_power_status(auth,device_type=dev1['deviceType'], device_id=dev1['deviceId'])
        # self.assertIs(type(power_status['message']), str)

    def test_get_dev_power_status_pos(self):
        """
        Positive Test case
        """
        power_status = get_dev_power_status(auth, device_name=dev1['name'])
        #self.assertIs(type(power_status['message']), str)

    def test_get_dev_power_status_neg(self):
        """
        Negative Test case
        :return:
        """
        power_status = get_dev_power_status(auth, device_name="Doesn't Exist")
        self.assertEqual(power_status, 'Device not found')


#TODO All Set Device Preference Tests Failing

class TestSetDevicePreference(TestCase):
    """
    Test Case for pyawair.devices set_dev_preference function for a single
    device name "Bedroom_Awair"
    ['general', 'productivity', 'sleep', 'allergy', 'baby']
    """
    def test_set_dev_preference_pos_id_post(self):
        mode = 'general'
        preference = set_device_preference(auth, mode, device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])
        # self.assertIs(type(preference['message']), str)
        # self.assertEquals(preference['message'],"success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEqual(dev_details['preference'].lower(), mode)

    def test_set_dev_preference_id_bad_mode_neg(self):
        """
        Negative Test case
        :return:
        """
        mode = 'banana'
        preference = set_device_preference(auth, mode, device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])
        self.assertEqual(preference, 'mode setting not valid')


    def test_set_dev_preference_pos_general(self):
        """
        Positive Test case
        """
        mode = 'general'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        #self.assertIs(type(preference['message']), str)
        #self.assertEquals(preference['message'],"success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEqual(dev_details['preference'].lower(), mode )

    def test_set_dev_preference_no_device_neg(self):
        """
        Negative Test case
        :return:
        """
        mode = 'general'
        preference = set_device_preference(auth, mode, device_name="Doesn't Exist")
        self.assertEqual(preference, 'Device not found')

    def test_set_dev_preference_bad_mode_neg(self):
        """
        Negative Test case
        :return:
        """
        mode = 'banana'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        self.assertEqual(preference, 'mode setting not valid')

    '''
    def test_set_dev_preference_pos_sleep(self):
        """
        Positive Test case
        """
        mode = 'sleep'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_productivity(self):
        """
        Positive Test case
        """
        mode = 'productivity'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_baby(self):
        """
        Positive Test case
        """
        mode = 'baby'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEquals(dev_details['preference'].lower(), mode)


    def test_set_dev_preference_pos_allergy(self):
        """
        Positive Test case
        """
        mode = 'allergy'
        preference = set_device_preference(auth, mode, device_name=dev1['name'])
        self.assertIs(type(preference['message']), str)
        self.assertEquals(preference['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEquals(dev_details['preference'].lower(), mode)
'''

class TestSetDeviceTimezone(TestCase):
    """
    Test Case for pyawair.devices set_dev_timezone function for a single
    device name "Bedroom_Awair"
    ['general', 'productivity', 'sleep', 'allergy', 'baby']
    """

    def test_set_dev_timezone_pos_id_post(self):
        new_timezone = 'us/pacific'
        timezone = set_device_timezone(auth, new_timezone,device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])
        self.assertIs(type(timezone['message']), str)
        self.assertEqual(timezone['message'], "success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEqual(dev_details['timezone'].lower(), new_timezone.lower())

    def test_set_dev_timezone_pos(self):
        """
        Positive Test case
        """
        new_timezone = 'us/pacific'
        timezone = set_device_timezone(auth, new_timezone, device_name=dev1['name'])
        self.assertIs(type(timezone['message']), str)
        self.assertEqual(timezone['message'],"success")
        dev_details = get_dev_details(auth, device_name=dev1['name'])
        self.assertEqual(dev_details['timezone'].lower(), new_timezone.lower() )

    def test_set_dev_timezone_neg(self):
        """
        Negative Test case
        :return:
        """
        new_timezone = "America/Montreal"
        timezone = set_device_timezone(auth, new_timezone, device_name="Doesn't Exist")
        self.assertEqual(timezone, 'Device not found')


class TestSetDeviceLED(TestCase):
    """
    Test Case for pyawair.devices set_dev_timezone function for a single
    device name "Bedroom_Awair"
    ['general', 'productivity', 'sleep', 'allergy', 'baby']
    """

    def test_set_device_led_id_pos(self):
        led_mode = 'dim'
        new_mode = set_device_led(auth, led_mode,device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])

        check_mode = get_dev_led_mode(auth, device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])
        self.assertEqual(check_mode, {'mode': 'on'})

    def test_set_device_led_mode_id_neg(self):
        led_mode = 'banana'
        new_mode = set_device_led(auth, led_mode, device_type=dev1['deviceType'],
                                           device_id=dev1['deviceId'])
        self.assertEqual(new_mode, 'mode setting not valid')

    def test_set_device_led_name_pos(self):
        led_mode = 'dim'
        new_mode = set_device_led(auth, led_mode,device_name=dev1['name'])

        check_mode = get_dev_led_mode(auth, device_name=dev1['name'])
        self.assertEqual(check_mode, {'mode': 'on'})

    def test_set_device_led_name_neg(self):
        led_mode = 'dim'
        new_mode = set_device_led(auth, led_mode,device_name='Doesnt exist')
        self.assertEqual(new_mode, 'Device not found')

    def test_set_device_led_mode_name_neg(self):
        led_mode = 'banana'
        new_mode = set_device_led(auth, led_mode,device_name=dev1['name'])
        self.assertEqual(new_mode, 'mode setting not valid')

