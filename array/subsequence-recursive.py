#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : subsequence-recursive.py
@Time : 3/27/22 4:22 PM
@Desc: 
"""


def all_subsequence(arr, index, subarray):
    """
    Print all subsequence of an array
    Args:
        arr:
        index:
        subarray:

    Returns:

    """
    if index == len(arr):
        if len(subarray) != 0:
            print(subarray)
    else:
        all_subsequence(arr, index + 1, subarray)
        all_subsequence(arr, index + 1, subarray + [arr[index]])


'''
a = [1,2]
possible subsequence = [1], [2], [1,2] 
'''


def main():
    """
    main function to drive code
    Returns:

    """
    arr = [1, 2, 3]
    all_subsequence(arr, 0, [])


if __name__ == "__main__":
    main()
