import requests
import ast
import json


def check_response(response):
    """
    Function to check the typical response coming from the Awair API. If something is not right, this function will
    throw an error.
    :param response: The response from the Awair API
    :return: If all is fine, returns nothing. Throws an error if something is wrong.
    """
    if response.status_code != 200:
        raise ConnectionError("No connection with the API. Status code {}. Message: '{}'.".format(
            response.status_code,
            ast.literal_eval(response.text)['message']))
    return


def get_data(auth, id, type, base_url, data_url, args=''):
    """
    Builds the Awair API string and returns the response.
    :param auth: Authentication object as created by pyawair.auth.AwairAuth
    :param id: The Awair ID
    :param type: The Awair Type
    :param base_url: The basic URL to the Awair API ("http://developer-apis.awair.is/v1/users/self/devices/")
    :param data_url: The data URL contains the specific data for a specific query (e.g. "/air-data/5-min-avg")
    :param args: Optional arguments
    :return: The response from the Awair API, as a JSON object.
    """
    dev_url = type + "/" + str(id)
    f_url = base_url + dev_url + data_url + args

    response = requests.get(f_url, headers=auth.headers) # Get the response from this URL
    check_response(response) # check if the response satisfies normal API results. If it doesn't it throws an error.

    return json.loads(response.text)['data']
