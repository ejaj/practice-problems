#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : substring.py
@Time : 3/27/22 2:43 PM
@Desc: Substring of a string
"""


def print_all_substrings(string):
    """
    Print all sub string of a string
    Args:
        string:

    Returns:

    """
    for i in range(len(string)):
        for j in range(i, len(string)):
            print(string[i: j + 1], end=' ')


'''
s = 'ab'
possible sub string = a, b, ab
'''


def main():
    """
    main function to drive code
    Returns:

    """
    string = 'abc'
    print_all_substrings(string)


if __name__ == "__main__":
    main()
