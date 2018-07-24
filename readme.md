# Python Wrapper for Awair Air Quality Sensor

This project is a alpha wrapper for the Awair Air Quality Sensor API.



https://www.getawair.com


## Using the Library

The Awair Developer program is currently under beta. You may request a personal token
with the awair team. 


Once you get the token create a new variable called **token** and paste in the contents of the 
token

```python
>>> token = """paste_your_token_here"
```
Now that you've captured the contents of your token, this will automatically be inserted into the
 auth headers during the HTTP request to the Awair API
 
 #### Getting you User Data
 
 Issue the following command to get your user data
 
```python
 >>> from pyawair.devices import \**
 >>> get_user_data()
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
get_all_devices()
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
get_dev_details('Bedroom_Awair')
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