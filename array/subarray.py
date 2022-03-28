#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : subarray.py
@Time : 3/27/22 2:07 PM
@Desc: Subarray of an array
"""


def print_all_subarray(nums):
    """
    Print all sub array of an array
    Args:
        nums:

    Returns:
        possible sub array's
    """
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            print(nums[i: j + 1])


'''
array = [1,2,3]
output = [1], [1,2], [1,2,3],[2],[2,3],[3]
'''


def main():
    """
    main function to drive code
    Returns:

    """
    nums = [1, 2, 3, 4, 5]
    print_all_subarray(nums)


if __name__ == '__main__':
    main()
