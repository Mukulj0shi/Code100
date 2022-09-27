#!usr/bin/env python3

"""
This program sends a email notification when ISS is overhead so we can check ISS at sky.
Using 2 API >> ISS rest API and Sunrise&sunset rest api to compare current date and time.
"""

import requests
from datetime import datetime
import re

current_time = datetime.now()
today_date = current_time.date()
my_lat = 28.593200
my_lon = 77.072266

def iss_position():
    api_endpoint = "http://api.open-notify.org/iss-now.json"
    response = requests.get(url=api_endpoint)
    response.raise_for_status()
    iss_latitude = float(response.json()["iss_position"]["latitude"])
    iss_longitude = float(response.json()["iss_position"]["longitude"])
    if (my_lon - 5.0) <= iss_longitude <= (my_lon + 5.0) and (my_lat - 5.0) <= iss_latitude <= (my_lat + 5.0):
        print(yes)

def detect_dark():
    api_url = "https://api.sunrise-sunset.org/json"

    # These parameters are sent with the API request
    parameters = {
        "lat": 28.593200,
        "lng": 77.072266,
        "formatted": 0
    }
    response = requests.get(url=api_url, params=parameters)
    response.raise_for_status()
    sunrise_time = response.json()["results"]["sunrise"]
    sunset_time = response.json()["results"]["sunset"]

    # Use regex to extract hour from the sunrise and sunset time and use respective group() method.
    sunrise = re.search("(\d+?)-(\d\d-\d\dT)(\d{2}:\d{2}):(.*)", sunrise_time)
    sunrise_hour = sunrise.group(3)
    sunset = re.search("(\d+?)-(\d\d-\d\dT)(\d{2}:\d{2}):(.*)", sunset_time)
    sunset_hour = sunset.group(3)
    print((sunrise_hour))
    current_hour = current_time.hour
    print((current_hour))



detect_dark()