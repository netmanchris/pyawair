from pyawair.devices import *


def get_current_air_data(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get the current air data from a single specific Awair Device linked
    to your account
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_type: str which matches the awair device type
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which contains current air data
    """
    if device_name is None:
        base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/air-data/latest"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)['data']
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/air-data/latest"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)['data']


def get_5_min_average(auth, device_name=None, device_type=None, device_id=None):
    if device_name is None:
        base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/air-data/5-min-avg"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)['data']
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/air-data/5-min-avg"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)['data']


def get_15_min_average(auth, device_name=None, device_type=None, device_id=None):
    if device_name is None:
        base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/air-data/15-min-avg"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)['data']
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/air-data/15-min-avg"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)['data']


def get_raw_data(auth, device_name=None, device_type=None, device_id=None):
    if device_name is None:
        base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
        dev_url = device_type + "/" + str(device_id)
        data_url = "/air-data/raw"
        f_url = base_url + dev_url + data_url
        print(f_url)
        response = requests.get(f_url, headers=auth.headers)
        return json.loads(response.text)['data']
    else:
        devices = get_all_devices(auth)
        for dev in devices:
            if dev['name'] == device_name:
                base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
                dev_url = dev['deviceType'] + "/" + str(dev['deviceId'])
                data_url = "/air-data/raw"
                f_url = base_url + dev_url + data_url
                print(f_url)
                response = requests.get(f_url, headers=auth.headers)
                return json.loads(response.text)['data']
