#!usr/bin/env python3

"""
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
"""

import requests
from datetime import datetime
import math

current_day = datetime.now()
print(type(current_day.date()))

print(current_day.date())

api_endpoint = "https://www.alphavantage.co/query"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "ZOMATO.BSE",
    "apikey": "STUM887HR7PCUZ58"
}

response = requests.get(url=api_endpoint, params=parameters)
response.raise_for_status()
print(response.json())

yesterday_sp = response.json()["Time Series (Daily)"]
print(yesterday_sp.items())
stock_list = yesterday_sp.items()
print(len(stock_list))
len_of_list = 0

for key,value in yesterday_sp.items():
    if len_of_list == 0:
        yesterday_open_value = float(value["1. open"])
        len_of_list += 1
    elif len_of_list == 1:
        day_before_yesterday_close_value = float(value["4. close"])
        print(day_before_yesterday_close_value)
        len_of_list += 1

stock_change = (abs(yesterday_open_value - day_before_yesterday_close_value)/yesterday_open_value) * 100
print(stock_change)
if yesterday_open_value > day_before_yesterday_close_value and stock_change >= 0.75:
    print("price_up")
elif yesterday_open_value < day_before_yesterday_close_value and stock_change >= 0.75:
    print("price_down")





