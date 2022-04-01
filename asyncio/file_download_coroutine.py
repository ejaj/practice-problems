#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : file_download_coroutine.py
@Time : 4/2/22 1:38 AM
@Desc: 
"""

import aiohttp
import asyncio
import async_timeout
import os


async def download_coroutine(session, url):
    """
    Coroutine function for file downloads.
    Args:
        session:
        url:

    Returns:

    """
    with async_timeout.timeout(10):
        async with session.get(url) as response:
            pdf = os.path.basename(url)
            with open(pdf, 'wb') as f_handle:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    f_handle.write(chunk)
            return await response.release()


async def main(loop):
    """
    main function to drive code.
    Args:
        loop:

    Returns:

    """
    urls = [
        "http://xyz/1.pdf",
        "http://xyz/2.pdf",
        "http://xyz/3.pdf",
        "http://xyz/4.pdf",
        "http://xyz/5.pdf",
    ]
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [download_coroutine(session, url) for url in urls]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(loop))
