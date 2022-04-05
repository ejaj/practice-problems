#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : thread_pool.py
@Time : 4/4/22 2:26 PM
@Desc: 
"""
import time
import concurrent.futures

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
    return f'Done Sleeping...{seconds}'


def main():
    """
    Main function for drive code
    Returns:

    """
    with concurrent.futures.ThreadPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, sec) for sec in secs]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        results = executor.map(do_something, secs)
        for result in results:
            print(result)
    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 1)} seconds(s)')


if __name__ == '__main__':
    main()
