# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyhpeimc.plat.alarms module.
"""

from unittest import TestCase
from secret import *
from pyawair.data import *

dev1="Bedroom_Awair"   #Modify this variable to test against your own devices



# TODO Remarked out failing tests


class TestGetCurrentAirData(TestCase):
    """
    Test Case for pyawair.devices get_user_data function
    """

    def test_get_current_air(self):
        """
        """
        get_current_air = get_current_air_data(auth, device_name=dev1)
        self.assertIs(type(user_data['dobDay']), int)
        self.assertIs(type(user_data['dobMonth']), int)
        self.assertIs(type(user_data['dobYear']), int)
        self.assertIs(type(user_data['email']), str)
        self.assertIs(type(user_data['firstName']), str)
        self.assertIs(type(user_data['lastName']), str)
        self.assertIs(type(user_data['id']), str)
