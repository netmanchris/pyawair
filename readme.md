
# Python Wrapper for Awair Air Quality Sensor

[![Build Status](https://travis-ci.com/netmanchris/pyawair.svg?branch=master)](https://travis-ci.com/netmanchris/pyawair)
[![Coverage Status](https://coveralls.io/repos/github/netmanchris/pyawair/badge.svg?branch=master)](https://coveralls.io/github/netmanchris/pyawair?branch=master)
This project is a alpha wrapper for the Awair Air Quality Sensor API.



https://www.getawair.com


## Using the Library

The Awair Developer program is currently under beta. You may request a personal token
with the awair team. 


#### Creating yor Auth object
Once you get the token create a new object of the AwairAuth type by passing in the token
from the Awair Dev site as a str.

```python
>>> auth = AwairAuth('''My_Token''')

>>> auth.token
My_Token'

```

This object of type AwairAuth must be passed into all API calls to ensure that you can 
successfully pass your authentication request to the Awair API.
 
 
 ## Example Functions
 
 The following functions shows some basic examples of working with the Awair Python binding to 
 gather data from the Awair API. 
 
 #### Getting you User Data
 
 Issue the following command to get your user data
 
```python
 >>> from pyawair.devices import *
 >>> get_user_data(auth)
  Out[3]: 
{'dobDay': 23,
 'dobMonth': 11,
 'dobYear': 1975,
 'email': 'user_email@example.com',
 'firstName': 'Bob',
 'id': '55555',
 'lastName': 'McUser',
 'sex': 'MALE'}
```

Issue the following command to get all devices registered to your account

```python
get_all_devices(auth)
Out[4]: 
[{'deviceId': 55555,
  'deviceType': 'awair',
  'latitude': 45.45370287113559,
  'locationName': 'Brossard, QC',
  'longitude': -73.48057550995341,
  'name': 'Bedroom_Awair',
  'preference': 'SLEEP',
  'spaceType': 'Home',
  'timezone': 'America/Montreal'},
 {'deviceId': 55556,
  'deviceType': 'awair-glow',
  'latitude': 45.45391109636124,
  'locationName': 'Brossard, QC',
  'longitude': -73.48050358533686,
  'name': 'Bedroom_Glow',
  'preference': 'SLEEP',
  'spaceType': 'Home',
  'timezone': 'America/Montreal'}]
```

We've also created a helper function to allow you to request just the data on the a single Awair 
device by specifying the name of the device

The following command will get the details for a device named **Bedroom_Awair**

```python
get_dev_details(auth, device_name='Bedroom_Awair')
Out[4]: 
{'deviceId': 55555,
 'deviceType': 'awair',
 'latitude': 45.45370287113559,
 'locationName': 'Brossard, QC',
 'longitude': -73.48057550995341,
 'name': 'Bedroom_Awair',
 'preference': 'SLEEP',
 'spaceType': 'Home',
 'timezone': 'America/Montreal'}

```
