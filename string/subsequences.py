#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : subsequences.py
@Time : 3/27/22 3:55 PM
@Desc: 
"""

import itertools as it


def sub_sequences(string):
    """
    "Print all sub sequence of a string using itertools.
    Args:
        string:

    Returns:

    """
    result = []
    for i in range(1, len(string) + 1):
        result.append(list(it.combinations(string, i)))
    for c in result:
        for t in c:
            print(''.join(t), end=' ')


'''
s = 'ab'
possible subsequence = a, b, c, ab, ac, bc, abc
'''


def main():
    """
    main function to drive code
    Returns:

    """
    sub_sequences('abc')


if __name__ == "__main__":
    main()
