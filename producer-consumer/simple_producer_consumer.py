#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : simple_producer_consumer.py
@Time : 4/3/22 2:01 PM
@Desc:
"""

from threading import Thread
from queue import Queue

q = Queue()
final_results = []


def producer():
    """
    Put the value into queue
    Returns:

    """
    for i in range(100):
        q.put(i)


def consumer():
    """
    Consume value from the queue
    Returns:

    """
    while True:
        number = q.get()
        result = (number, number ** 2)
        final_results.append(result)
        q.task_done()


def main():
    """
    Main function for drive the code
    Returns:

    """
    for i in range(5):
        t = Thread(target=consumer)
        t.daemon = True
        t.start()
    producer()
    q.join()
    print(final_results)


if __name__ == '__main__':
    main()
