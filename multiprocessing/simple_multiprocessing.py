#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : simple_multiprocessing.py
@Time : 4/5/22 3:17 PM
@Desc: 
"""
import multiprocessing
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    print('Done Sleeping...')


def main():
    """
    Main function for drive code
    Returns:

    """

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        processes.append(p)
    for process in processes:
        process.join()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 1)} seconds(s)')


if __name__ == '__main__':
    main()
