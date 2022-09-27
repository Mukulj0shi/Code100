#!usr/bin/env python3

"""
This program make a API call to weather site and gets data for the local city.
When it is supposed to rain as per the weather forecast then program should suggest to
take umbrella.
"""

import requests
from twilio.rest import Client

api_endpoints = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 28.613939,
    "lon": 77.209023,
    "exclude": "current,minutely,daily",
    "appid": "b6bdcd3b831b7aca5fbcf086ef244eb8"
}

response = requests.get(url=api_endpoints, params=parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"]

# This function uses twilio API to send SMS.
# Client class takes account_sid and auth_token as parameters to be sent.
def send_message():
    account_sid = 'AC741ffc69c1685f9cca9463023b9bbef4'
    auth_token = '8baaedf946572ae1db351708b4a301a2'
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Take Umbrella it gonna rain today",
        from_='+1xxxx',
        to='+1xxxx'
    )
    print(message.status)

will_rain = False

for index_range in range(0, 12):
    weather_condition = hourly_data[index_range]["weather"][0]["id"]
    if int(weather_condition) <= 802:
        will_rain = True

if will_rain == True:
    send_message()