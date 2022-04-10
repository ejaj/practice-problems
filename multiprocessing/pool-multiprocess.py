#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : coroutine-multiprocess.py
@Time : 4/9/22 4:15 PM
@Desc: 
"""
import concurrent.futures
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'


def main():
    """
    Main function for drive code
    Returns:

    """

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, sec) for sec in range(secs)]
        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())
        results = executor.map(
            do_something, secs
        )
        for result in results:
            print(result)

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 1)} seconds(s)')


if __name__ == '__main__':
    main()
