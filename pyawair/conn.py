import requests
import ast
import json

def check_response(response):
    if response.status_code != 200:
        raise ConnectionError("No connection with the API. Status code {}. Message: '{}'.".format(response.status_code,
                                                                                               ast.literal_eval(response.text)['message']))
    return

def get_data(auth, id, type, base_url, data_url):
    dev_url = type + "/" + str(id)
    f_url = base_url + dev_url + data_url
    response = requests.get(f_url, headers=auth.headers)
    check_response(response)
    return json.loads(response.text)['data']