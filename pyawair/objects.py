
#!/usr/bin/env python3
# coding=utf-8
# author: @netmanchris
# -*- coding: utf-8 -*-

from pyawair.data import get_current_air_data

class AwairDev:
    def __init__(self, device_name, auth):
        self.auth = auth
        self.device_name = device_name
        self.currentdata = get_current_air_data(auth, device_name=device_name)
        self.score = self.currentdata[0]['score']
        self.temp = self.currentdata[0]['sensors'][0]['value']
        self.humid = self.currentdata[0]['sensors'][1]['value']
        self.co2 = self.currentdata[0]['sensors'][2]['value']
        self.voc = self.currentdata[0]['sensors'][3]['value']
        self.timestamp = self.currentdata[0]['timestamp']

    def refresh(self):
        self.currentdata = get_current_air_data(self.auth, device_name=self.device_name)
        self.score = self.currentdata[0]['score']
        self.temp = self.currentdata[0]['sensors'][0]['value']
        self.humid = self.currentdata[0]['sensors'][1]['value']
        self.co2 = self.currentdata[0]['sensors'][2]['value']
        self.voc = self.currentdata[0]['sensors'][3]['value']
        self.timestamp = self.currentdata[0]['timestamp']

