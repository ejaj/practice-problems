#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : async_request_2.py
@Time : 4/2/22 10:16 PM
@Desc: 
"""

import asyncio
import aiohttp
import time
import os

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        # tasks.append(
        #     session.get(
        #         url.format(symbol, api_key), ssl=False
        #     )
        # )
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(
            *tasks
        )
        # for response in responses:
        #     results.append(await response.json())


# loop = asyncio.get_event_loop()
# loop.run_until_complete(get_symbols())
# loop.close()
asyncio.run(get_symbols())
end = time.time()
total_time = end - start
print("It took {} seconds to make {} API calls".format(total_time, len(symbols)))
print('You did it')
