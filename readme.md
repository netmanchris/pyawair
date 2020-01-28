
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
 Out[10]: 
[{'deviceId': 0,
  'deviceType': 'awair',
  'latitude': 123.4567,
  'locationName': 'My Home',
  'longitude': 123.4567,
  'name': 'Bedroom',
  'preference': 'GENERAL',
  'spaceType': 'HOME',
  'timezone': 'US/Pacific'}]
```

Issue the following command to get all devices registered to your account

```python
get_all_devices(auth)
Out[4]: 
Out[11]: 
[{'deviceId': 0,
  'deviceType': 'awair',
  'latitude': 123.4567,
  'locationName': 'My Home',
  'longitude': 123.4567,
  'name': 'Bedroom',
  'preference': 'GENERAL',
  'spaceType': 'HOME',
  'timezone': 'US/Pacific'}]
```

We've also created a helper function to allow you to request just the data on the a single Awair 
device by specifying the name of the device

The following command will get the details for a device named **Bedroom_Awair**

```python
get_dev_details(auth, device_name='Bedroom')
Out[12]: 
{'deviceId': 0,
 'deviceType': 'awair',
 'latitude': 123.4567,
 'locationName': 'My Home',
 'longitude': 123.4567,
 'name': 'Bedroom',
 'preference': 'GENERAL',
 'spaceType': 'HOME',
 'timezone': 'US/Pacific'}
```

#### Getting Device Data

To access device data functions, you must first import the data module into your coding environment

```python
from pyawair.data import *
```

##### Get Current Air Data

```python
get_current_air_data(auth, device_name='Bedroom')
Out[21]: 
[{'indices': [{'comp': 'TEMP', 'value': 0.0},
   {'comp': 'HUMID', 'value': 0.0},
   {'comp': 'CO2', 'value': 0.0},
   {'comp': 'VOC', 'value': 0.0},
   {'comp': 'PM10', 'value': 0.0},
   {'comp': 'PM25', 'value': 0.0}],
  'score': 100.0,
  'sensors': [{'comp': 'TEMP', 'value': 100.0},
   {'comp': 'HUMID', 'value': 100.0},
   {'comp': 'CO2', 'value': 100.0},
   {'comp': 'VOC', 'value': 100.0},
   {'comp': 'PM10', 'value': 100.0},
   {'comp': 'PM25', 'value': 100.0}],
  'timestamp': '1970-01-01T00:00:00.000Z'}]
```
  
##### Get 5 Minute Average

```python
get_5_min_average(auth, device_name='Bedroom')
Out[22]: 
[{'indices': [{'comp': 'TEMP', 'value': 0.0},
   {'comp': 'HUMID', 'value': 0.0},
   {'comp': 'CO2', 'value': 0.0},
   {'comp': 'VOC', 'value': 0.0},
   {'comp': 'PM10', 'value': 0.0},
   {'comp': 'PM25', 'value': 0.0}],
  'score': 100.0,
  'sensors': [{'comp': 'TEMP', 'value': 100.0},
   {'comp': 'HUMID', 'value': 100.0},
   {'comp': 'CO2', 'value': 100.0},
   {'comp': 'VOC', 'value': 100.0},
   {'comp': 'PM10', 'value': 100.0},
   {'comp': 'PM25', 'value': 100.0}],
  'timestamp': '1970-01-01T00:00:00.000Z'}]
  ```
  
##### Get 15 minute average

```python
get_15_min_average(auth, device_name='Bedroom')
Out[23]: 
[{'indices': [{'comp': 'TEMP', 'value': 0.0},
   {'comp': 'HUMID', 'value': 0.0},
   {'comp': 'CO2', 'value': 0.0},
   {'comp': 'VOC', 'value': 0.0},
   {'comp': 'PM10', 'value': 0.0},
   {'comp': 'PM25', 'value': 0.0}],
  'score': 100.0,
  'sensors': [{'comp': 'TEMP', 'value': 100.0},
   {'comp': 'HUMID', 'value': 100.0},
   {'comp': 'CO2', 'value': 100.0},
   {'comp': 'VOC', 'value': 100.0},
   {'comp': 'PM10', 'value': 100.0},
   {'comp': 'PM25', 'value': 100.0}],
  'timestamp': '1970-01-01T00:00:00.000Z'}]
```
##### Get Raw Data

```python
get_raw_data(auth, device_name='Bedroom')
Out[24]: 
[{'indices': [{'comp': 'TEMP', 'value': 0.0},
   {'comp': 'HUMID', 'value': 0.0},
   {'comp': 'CO2', 'value': 0.0},
   {'comp': 'VOC', 'value': 0.0},
   {'comp': 'PM10', 'value': 0.0},
   {'comp': 'PM25', 'value': 0.0}],
  'score': 100.0,
  'sensors': [{'comp': 'TEMP', 'value': 100.0},
   {'comp': 'HUMID', 'value': 100.0},
   {'comp': 'CO2', 'value': 100.0},
   {'comp': 'VOC', 'value': 100.0},
   {'comp': 'PM10', 'value': 100.0},
   {'comp': 'PM25', 'value': 100.0}],
  'timestamp': '1970-01-01T00:00:00.000Z'}]
```

#### AwairDev Class

The AwairDev class has been provided as a way to interface with an Awair Air quality device
in an object oriented manner. The primary use-case for the AwairDev class is to provide the 
base for building device driver support for the Home-Assistant project (HassIO). If you are 
interested in exposing your Awair Device to your Home-Assistant instance, you can see an early 
example of this work [here](https://github.com/netmanchris/awair_component)

*thanks to @danielsjf for this work!

```python
from pyawair.objects import AwairDev
my_awair = AwairDev('Bedroom', auth)
my_awair.type()
Out[27]: 'awair'
my_awair.get_state('score')
Out[29]: 100.0
my_awair.get_state('humid')
Out[30]: 100.0

```
