#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : simple_gen.py
@Time : 4/3/22 12:47 PM
@Desc: 
"""


def fib():
    """
    Returns:
    """
    current, next_number = 0, 1
    while True:
        current, next_number = next_number, current + next_number
        yield current


result = fib()
for n in result:
    print(n, end=', ')
    if n > 10000:
        break
print()
print("Done")
