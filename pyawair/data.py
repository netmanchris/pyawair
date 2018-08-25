from pyawair.devices import *
import pyawair.conn
import pyawair.objects


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
    if device_type is None or device_id is None:
        awair_device = pyawair.objects.AwairDev(device_name, auth)
        device_type = awair_device.type()
        device_id = awair_device.id()

    base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
    data_url = "/air-data/latest"
    data = pyawair.conn.get_data(auth, device_id, device_type, base_url, data_url)

    return data


def get_5_min_average(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get air data that is averaged over each 5 minutes from a single specific Awair Device linked
    to your account
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_type: str which matches the awair device type
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which contains current air data
    """
    if device_type is None or device_id is None:
        awair_device = pyawair.objects.AwairDev(device_name, auth)
        device_type = awair_device.type()
        device_id = awair_device.id()

    base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
    data_url = "/air-data/5-min-avg"
    data = pyawair.conn.get_data(auth, device_id, device_type, base_url, data_url)

    return data


def get_15_min_average(auth, device_name=None, device_type=None, device_id=None):
    """
    Function to get air data that is averaged over each 5 minutes from a single specific Awair Device linked
    to your account
    :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
    :param device_type: str which matches the awair device type
    :param device_name: str which matches exactly to the name of a specific device
    :param device_id: str or int which matches the specific awair device internal id number
    :return: Object of Dict type which contains current air data
    """
    if device_type is None or device_id is None:
        awair_device = pyawair.objects.AwairDev(device_name, auth)
        device_type = awair_device.type()
        device_id = awair_device.id()

    base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
    data_url = "/air-data/15-min-avg"
    data = pyawair.conn.get_data(auth, device_id, device_type, base_url, data_url)

    return data


def get_raw_data(auth, device_name=None, device_type=None, device_id=None):
    """
        Function to get air data that is averaged over each 5 minutes from a single specific Awair Device linked
        to your account
        :param auth: pyawair.auth.AwairAuth object which contains a valid authentication token
        :param device_type: str which matches the awair device type
        :param device_name: str which matches exactly to the name of a specific device
        :param device_id: str or int which matches the specific awair device internal id number
        :return: Object of Dict type which contains current air data
        """
    if device_type is None or device_id is None:
        awair_device = pyawair.objects.AwairDev(device_name, auth)
        device_type = awair_device.type()
        device_id = awair_device.id()

    base_url = "http://developer-apis.awair.is/v1/users/self/devices/"
    data_url = "/air-data/raw"
    data = pyawair.conn.get_data(auth, device_id, device_type, base_url, data_url)

    return data
