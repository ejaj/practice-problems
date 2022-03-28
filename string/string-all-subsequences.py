#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : string-all-subsequences.py
@Time : 3/27/22 12:42 AM
@Desc: 
"""


def string_subsequence(input_string, output_string):
    """
    Program with recursion with pick and don't pick approach.
    Args:
        input_string:
        output_string:

    Returns:

    """

    if len(input_string) == 0:
        print(output_string, end=' ')
        return
    string_subsequence(input_string[1:], output_string)
    string_subsequence(input_string[1:], output_string + input_string[0])


def string_subsequence_fix(string, n, index=-1, curr=""):
    """
    Program with recursion with fixing approach.
    Args:
        string:
        n:
        index:
        curr:

    Returns:

    """
    if index == n:
        return
    if len(curr) > 0:
        print(curr)
    i = index + 1

    while i < n:
        curr = curr + string[i]
        string_subsequence_fix(string, n, i, curr)
        curr = curr[:len(curr) - 1]
        i = i + 1


def print_sub_seq(string):
    """
    Print all sub sequence
    Args:
        string:

    Returns:

    """
    string_subsequence_fix(str, len(string))


'''
s = ab
output = b a ab
'''


def main():
    """
    main function to drive code
    Returns:

    """
    output_string = ""
    input_string = "abc"
    string_subsequence(input_string, output_string)
    print_sub_seq(input_string)


if __name__ == "__main__":
    main()
