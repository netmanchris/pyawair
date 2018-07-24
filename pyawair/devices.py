

import requests, json
from pyawair.devices import *


def get_user_data(auth):
    """
    Function to get the user data for the account linked to the token
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :return: Object of Dict type which contains current user data for this account
    """
    response = requests.get("http://developer-apis.awair.is/v1/users/self",
                                headers=auth.headers)
    return json.loads(response.text)

def get_all_devices(auth):
    """
    Function to get all devices for the account linked to the token
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :return: Object of Dict type which contains a list of all devices for this account
    """
    response = requests.get("http://developer-apis.awair.is/v1/users/self/devices",
                            headers=auth.headers)
    return json.loads(response.text)['devices']

def get_dev_details(auth, device_name):
    """
    Function to get the data for a single specific device for the account linked
    to the token
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_name: str which matches exactly to the name of a specific device
    :return: Object of Dict type  which contains device details for specific device
    """
    devices = get_all_devices(auth)
    for dev in devices:
        if dev['name'] == device_name:
            return dev
    return "Device not found"

def get_dev_led_mode(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get the LED mode for a single specific devices for the account
    linked to the token
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_name: str which matches exactly to the name of a specific device
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which describes the LED mode of the specified devices
    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/led"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)
    elif device_name is not None:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/led"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)
    else:
        return "Device Not Found"

def get_dev_timezone(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get the timezone for a single specific devices for the account
    linked to the token. Refer to column TZ in
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_name: str which matches exactly to the name of a specific device
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which describes the timezone of the specified devices
    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/timezone"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/timezone"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)


def get_dev_display_mode(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get the display mode for a single specific devices for the account
    linked to the token
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_name: str which matches exactly to the name of a specific device
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which describes the display mode of the specified devices
    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/display"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/display"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)


def get_dev_power_status(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get the power_status for a single specific devices for the account
    linked to the token.
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_name: str which matches exactly to the name of a specific device
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which describes the power status of the specified devices
    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/power-status"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/power-status"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)


"""Following section deals with changing settings on the Awair devices"""


#NOTE THE APPLICATION TYPE MUST BE DELIVERED IN JSON LOOK AT THE DOCS NEEDS TO
#BE USING THE PREFS KEY. CREATE A DICTIONARY AND THEN USE JSON DUMPS


def set_device_preference(auth, new_mode, device_name=None, device_type=None, device_id=None):
    """
    Function to set the prefered mode for a single specific devices for the account
    linked to the token.
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param new_mode: str which matches the desired preference mode. Valid modes are
    "general", "productivity", "sleep", "allergy", "baby"
    :param device_name: str which matches exactly to the name of a specific device
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which contains a message of whether or not the set request was
    implemented
    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/preference"
        f_url = base_url + dev_url + data_url
        modes = ['general', 'productivity', 'sleep', 'allergy', 'baby']
        new_mode = new_mode
        try:
            if new_mode in modes:
                print(f_url)
                data = json.dumps({'pref' : new_mode})
                response = requests.put(f_url, data= data, headers=auth.headers)
                return json.loads(response.text)
        except:
            print ("mode setting not valid")
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/preference"
                f_url = base_url + dev_url + data_url
                modes = ['general', 'productivity', 'sleep', 'allergy', 'baby']
                mode = new_mode
                if mode in modes:
                    print(f_url)
                    data = json.dumps({'pref': new_mode})
                    response = requests.put(f_url, data=data, headers=auth.headers)
                    return json.loads(response.text)

def set_device_timezone(auth, timezone, device_name=None, device_type=None, device_id=None):
    """
    This function takes a str inpu for the value timezone and applies it to a specific
    awair device. The device can be selected using the unique name of the device, or by
    using a combination of the device type and device id values specific to the API.
    :param timezone: str value of the desired timezone.
    For specific values please see
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    :param device_name: str value of the name of the device
    :param device_type: str value of the device_type
    :param device_id: int or str value of the device_id (internal API id)
    :return: dictionary


    new_timezone = "America/Montreal"
    x = set_device_timezone(new_timezone, device_name="Bedroom_Awair")

    """
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/timezone"
        f_url = base_url + dev_url + data_url
        try:
            print(f_url)
            data = json.dumps({'timezone' : timezone})
            response = requests.post(f_url, data= data, headers=auth.headers)
            return json.loads(response.text)
        except:
            print ("mode setting not valid")
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/timezone"
                f_url = base_url + dev_url + data_url
                print(f_url)
                data = json.dumps({'timezone' : timezone})
                response = requests.post(f_url, data=data, headers=auth.headers)
                return json.loads(response.text)


def set_device_led(auth, led_mode, device_name=None, device_type=None, device_id=None):
    """
    This function takes a str input for the value timezone and applies it to a specific
    awair device. The device can be selected using the unique name of the device, or by
    using a combination of the device type and device id values specific to the API.
    :param led_mode: str value of the desired LED mode. Valid inputs are:
    "on" "dim" "sleep
    :param device_name: str value of the name of the device
    :param device_type: str value of the device_type
    :param device_id: int or str value of the device_id (internal API id)
    :return: dictionary


    new_led_mode = "dim"
    x = set_device_timezone(new_timezone, device_name="Bedroom_Awair")

    """
    modes = "on, dim, sleep"
    if device_name == None:
        base_url = "http://developer-apis.awair.is/v1/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/led"
        f_url = base_url + dev_url + data_url
        try:
            if led_mode in modes:
                print(f_url)
                data = json.dumps({'mode' : led_mode})
                response = requests.post(f_url, data= data, headers=auth.headers)
                return json.loads(response.text)
        except:
            print ("mode setting not valid")
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/led"
                f_url = base_url + dev_url + data_url
                try:
                    if led_mode in modes:
                        print(f_url)
                        data = json.dumps({'mode': led_mode})
                        response = requests.post(f_url, data=data, headers=auth.headers)
                        return json.loads(response.text)
                except:
                    print("INVALID LED MODE SPECIFIED")