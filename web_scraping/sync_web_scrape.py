#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : sync_web_scrape.py
@Time : 4/3/22 4:29 PM
@Desc: 
"""

import requests
import bs4
from colorama import Fore


def get_html(episode_number: int) -> str:
    """
    Get HTML from the website
    Args:
        episode_number:

    Returns:

    """
    print(Fore.YELLOW + f"Getting HTML for episode {episode_number}", flush=True)
    url = f'https://talkpython.fm/{episode_number}'
    resp = requests.get(url)
    resp.raise_for_status()
    return resp.text


def get_title(html: str, episode_number: int) -> str:
    """
    Get Title from html file
    Args:
        html:
        episode_number:

    Returns:

    """
    print(Fore.CYAN + f"Getting TITLE for episode {episode_number}", flush=True)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    header = soup.select_one('h1')
    if not header:
        return "MISSING"
    return header.text.strip()


def get_title_range():
    """
    Get nth title
    Returns:

    """
    for n in range(185, 190):
        html = get_html(n)
        title = get_title(html, n)
        print(Fore.WHITE + f"Title found: {title}", flush=True)


def main():
    """
    Main function for drive code
    Returns:

    """
    get_title_range()
    print("Done.")


if __name__ == '__main__':
    main()
