#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : simple_threading.py
@Time : 4/4/22 2:07 PM
@Desc: 
"""
import time
import threading

start = time.perf_counter()


def do_something(seconds):
    """
    Go to sleep
    Args:
        seconds:

    Returns:

    """
    print(f'Sleeping {seconds} second...')
    time.sleep(seconds)
    print('Done Sleeping...')


def main():
    """
    Main function for drive code
    Returns:

    """
    threads = []
    for _ in range(10):
        t = threading.Thread(target=do_something, args=[1.5])
        t.start()
        threads.append(t)
    for thread in threads:
        thread.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 1)} seconds(s)')


if __name__ == '__main__':
    main()
