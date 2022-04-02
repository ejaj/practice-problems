#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : sync_request.py
@Time : 4/2/22 7:25 PM
@Desc: 
"""
import requests
import time
import os

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []
start = time.time()
for symbol in symbols:
    print("Working on symbol {}".format(symbol))
    response = requests.get(
        url.format(symbol, api_key)
    )
    results.append(response.json())
end = time.time()
total_time = end-start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it')
