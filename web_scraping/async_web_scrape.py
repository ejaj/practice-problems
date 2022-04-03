#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : async_web_scrape.py
@Time : 4/3/22 4:49 PM
@Desc: 
"""
import asyncio
from asyncio import AbstractEventLoop
import aiohttp
import requests
import bs4
from colorama import Fore


async def get_html(episode_number: int) -> str:
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)
    url = f'https://talkpython.fm/{episode_number}'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            html = await resp.text()
            return html


def get_title(html: str, episode_number: int) -> str:
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"

    return header.text.strip()


async def get_title_range(loop: AbstractEventLoop):
    tasks = []
    for n in range(190, 195):
        tasks.append((loop.create_task(get_html(n)), n))
    for task, n in tasks:
        html = await task
        title = get_title(
            html, n
        )
        print(Fore.WHITE + f"Title found: {title}", flush=True)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_title_range(loop))
    print("Done.")


if __name__ == '__main__':
    main()
