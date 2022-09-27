#!usr/bin/env python3

"""
This program use API from Open Trivia Database to get random set of questions.
Program also send API params to get specific values.
"""

import requests

api_endpoint = "https://opentdb.com/api.php"

parameters = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
#print(response.json())
question_data = response.json()["results"]
