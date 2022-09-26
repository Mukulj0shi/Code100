#!usr/bin/env python3

"""
This program make a API call to weather site and gets data for the local city.
When it is supposed to rain as per the weather forecast then program should suggest to
take umbrella.
"""

import requests

api_endpoints = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": 28.613939,
    "lon": 77.209023,
    "exclude": "current,minutely,daily",
    "appid": "b6bdcd3b831b7aca5fbcf086ef244eb8"
}

response = requests.get(url=api_endpoints, params=parameters)
response.raise_for_status()
#print(response.json())
hourly_data = response.json()["hourly"]
#print(hourly_data[0]["weather"][0]["id"])

will_rain = False

for index_range in range(0, 12):
    weather_condition = hourly_data[index_range]["weather"][0]["id"]
    if int(weather_condition) <= 802:
        will_rain = True

if will_rain == True:
    print("Take umbrella it can rain")

