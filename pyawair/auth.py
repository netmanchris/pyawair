#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-
"""
This module contains functions for authenticating to the Awair Developer API.
For more info on the awair product line, please visit
https://www.getawair.com
"""

# This section imports required libraries
import json

import requests

HEADERS = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json'}


class AwairAuth():
    """
    Object to hold the authentication data for the Awair API
    :return An object of class AwairAuth to be passed into other functions to
    pass the authentication credentials
    """

    def __init__(self, token):
        """
        This class acts as the auth object for the Awair API. The token is available from the
        awair developer website.
        :param token: str object which contains the
        """

        self.token = token
        self.headers = HEADERS = {'Accept': 'application/json', 'Content-Type':
           'application/json', 'Accept-encoding': 'application/json','Authorization': 'Bearer {'
                                                                                      '}'.format(
            self.token)
        }
