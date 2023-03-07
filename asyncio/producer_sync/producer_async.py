#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : producer_async.py
@Time : 4/3/22 3:30 PM
@Desc: 
"""
import asyncio
import datetime
from asyncio import AbstractEventLoop

import colorama
import random
import time


async def generate_data(num: int, data: asyncio.Queue):
    """
    Generate the data, work as a producer
    Args:
        num:
        data:

    Returns:

    """
    for idx in range(1, num + 1):
        item = idx * idx
        work = (item, datetime.datetime.now())
        await data.put(work)
        print(colorama.Fore.YELLOW + " generated item {}".format(idx), flush=True)
        await asyncio.sleep(random.random() + .5)


async def process_data(num: int, data: asyncio.Queue):
    """
    Process the data, work as q consumer
    Args:
        num:
        data:

    Returns:

    """
    processed = 0
    while processed < num:
        item = await data.get()
        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(colorama.Fore.CYAN +
              " Processed value {} after {:,.2f} sec.".format(value, dt.total_seconds()), flush=True)
        await asyncio.sleep(.5)


def main():
    """
    Main function for drive code
    Returns:

    """
    loop: AbstractEventLoop = asyncio.get_event_loop()
    start = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = asyncio.Queue()
    task = asyncio.gather(
        generate_data(10, data),
        generate_data(10, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data),
        process_data(5, data)
    )
    loop.run_until_complete(task)
    end = datetime.datetime.now()
    diff = end - start
    print(colorama.Fore.WHITE + "App exiting, total time: {:,.2f} sec.".format(diff.total_seconds()), flush=True)


if __name__ == '__main__':
    main()
