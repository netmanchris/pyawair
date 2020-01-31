# -*- coding: utf-8 -*-
"""
This module is used for testing the functions within the pyawair.objects module.
"""

from unittest import TestCase
from unittest import mock
import pyawair.auth
from pyawair.conn import *

hobbiest = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktSE9CQllJU1QifQ.hzjhIpGljqCZ8vCrOr89POy_ENDPYQXsnzGslP01krI'
small_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktU01BTExfREVWRUxPUEVSIn0.amOu5uy-0UeBDRLd6uhqsbkUEyx13-4QdBrV1S3z2W8'
large_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktTEFSR0VfREVWRUxPUEVSIn0.JmP9a0eGjgYRlmri5BjNj4h1hlAZ-7yFOjcIZjyzypA'
enterprise_dev = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoiRFVNTVktRU5URVJQUklTRSJ9.bOM9rcABF9HKFHtxzF9kx8h9fv3CfvUIzveLFDRGrXs'

auth = pyawair.auth.AwairAuth(enterprise_dev)


class TestCheckResponse(TestCase):
    """
    Test Case for pyawair.objects AwairDev class
    """

    def test_check_response_pos(self):
        """
        """
        response = requests.get("https://developer-apis.awair.is/v1/users/self/devices",
                                headers=auth.headers)
        good_response = check_response(response)
        self.assertEqual(good_response, None)

