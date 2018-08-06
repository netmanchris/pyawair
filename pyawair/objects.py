
#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-

from pyawair.data import get_current_air_data
from pyawair.data import get_all_devices

class AwairDev:
    def __init__(self, device_name, auth):
        self._auth = auth
        self.device_name = device_name
        devices = get_all_devices(self._auth)
        self._type = next((item for item in devices if item["name"] == device_name),
                          False)['deviceType']  # get the device type
        self._id = next((item for item in devices if item["name"] == device_name),
                        False)['deviceId']  # get the device ID
        self.current_data = get_current_air_data(self._auth, device_id=self._id, device_type=self._type)
        self.score = self.current_data[0]['score']
        self.temp = self.current_data[0]['sensors'][0]['value']
        self.humid = self.current_data[0]['sensors'][1]['value']
        self.co2 = self.current_data[0]['sensors'][2]['value']
        self.voc = self.current_data[0]['sensors'][3]['value']
        self.timestamp = self.current_data[0]['timestamp']

    def refresh(self):
        self.current_data = get_current_air_data(self._auth, device_id=self._id, device_type=self._type)
        self.score = self.current_data[0]['score']
        self.temp = self.current_data[0]['sensors'][0]['value']
        self.humid = self.current_data[0]['sensors'][1]['value']
        self.co2 = self.current_data[0]['sensors'][2]['value']
        self.voc = self.current_data[0]['sensors'][3]['value']
        self.timestamp = self.current_data[0]['timestamp']

