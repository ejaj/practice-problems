#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : hello.py
@Time : 3/31/22 12:00 AM
@Desc: 
"""
import asyncio
import time


async def count():
    print("Hello")
    await asyncio.sleep(1)
    print("World !")


async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
