#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : two_sum.py
@Time : 4/3/22 2:25 AM
@Desc:
"""
from typing import List

'''
nums = [1,2,6,8]
target = 9
output = [0, 3]
'''


def two_sum_b(nums: List[int], target: int) -> List[int]:
    """
    Brute Force Approach
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    Args:
        nums:
        target:

    Returns:
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Hash Map / Set Method
    Time Complexity: O(n)
    Space Complexity: O(n)
    Args:
        nums:
        target:

    Returns:


    """
    values = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in values:
            return [i, values[diff]]
        values[nums[i]] = i


def main():
    """
    Main function for drive code
    Returns:

    """
    nums = [1, 2, 6, 8]
    target = 9
    print(two_sum_b(nums, target))
    print(two_sum(nums, target))


if __name__ == '__main__':
    main()
