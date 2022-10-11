#!usr/bin/env python3

"""
This program checks the stock change in last 2 days.
If the stock change is more than 1% then it search for the news related to that stock.
Send that news as SMS using twilio.
"""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
from twilio.rest import Client
import time


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def price_change():

    api_endpoint = "https://www.alphavantage.co/query"

    parameters = {
        "function": "TIME_SERIES_DAILY",
        "symbol": "ZOMATO.BSE",
        "apikey": "xxxxxxx"
    }

    response = requests.get(url=api_endpoint, params=parameters)
    response.raise_for_status()
    print(response.json())

    yesterday_sp = response.json()["Time Series (Daily)"]
    print(yesterday_sp.items())
    stock_list = yesterday_sp.items()
    print(len(stock_list))
    len_of_list = 0

    for key, value in yesterday_sp.items():
        if len_of_list == 0:
            yesterday_open_value = float(value["1. open"])
            len_of_list += 1
        elif len_of_list == 1:
            day_before_yesterday_close_value = float(value["4. close"])
            print(day_before_yesterday_close_value)
            len_of_list += 1

    stock_change = (abs(yesterday_open_value - day_before_yesterday_close_value) / yesterday_open_value) * 100
    print(stock_change)
    if yesterday_open_value > day_before_yesterday_close_value and stock_change >= 0.75:
        company_news = get_news()
        for nw in company_news:
            send_message("zomato 🔺 by 1%" + nw)
            time.sleep(10)
    elif yesterday_open_value < day_before_yesterday_close_value and stock_change >= 0.75:
        company_news = get_news()
        for nw in company_news:
            send_message("zomato 🔻 by 1%" + nw)
            time.sleep(10)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    api_endpoint = "https://newsapi.org/v2/everything"

    parameters = {
        "q": "zomato",
        "from": "today_key",
        "apikey": "xxxxxx"
    }

    response = requests.get(url=api_endpoint, params=parameters)
    news_article = response.json()
    response.raise_for_status()
    news = [f"headline: {news_article['articles'][itemno]['description']} brief: {news_article['articles'][itemno]['title']}" for itemno in range(0, 3)]
    return news


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
def send_message(mssg_to_send):
    print(mssg_to_send)
    account_sid = 'xxxx'
    auth_token = "xxxx"
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body=mssg_to_send,
        from_='+xxx',
        to='+xxx'
    )

    print(message.sid)


price_change()


#Optional: Format the SMS message like this:



"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

