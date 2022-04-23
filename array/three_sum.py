#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : three_sum.py
@Time : 4/23/22 12:20 PM
@Desc:
nums = [1, 4, 45, 6, 10, 8]
target = 22

output = [1,4,5], index of value
"""
from typing import List


def three_sum_brute(nums: List[int], target: int) -> List[int]:
    """
    Brute Force Approach
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    Args:
        nums:
        target:

    Returns:

    """
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i, j, k]


def three_sum_sorting_pointers(nums, target):
    """
    Sorting and Two-Pointers technique.
    Args:
        nums:
        target:

    Returns:

    """
    arr_size = len(nums)
    nums.sort()
    for i in range(0, arr_size - 2):
        l = i + 1
        r = arr_size - 1
        while l < r:
            if nums[i] + nums[l] + nums[r] == target:
                return [i, l, r]
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return []


def three_sum_has_map(nums, target):
    """
    Hash Map / Set Method
    Time complexity: O(N^2)
    Auxiliary Space: O(N)
    Args:
        nums:
        target:

    Returns:

    """
    arr_size = len(nums)
    for i in range(0, arr_size - 1):
        s = {}
        curr_sum = target - nums[i]
        for j in range(i + 1, arr_size):
            triple_current_sum = curr_sum - nums[j]
            if triple_current_sum in s:
                return [i, j, s[triple_current_sum]]
            s[nums[j]] = j
    return []


def main():
    nums = [1, 4, 45, 6, 10, 8]
    target = 22
    # print(three_sum_brute(nums, target))
    # print(three_sum_sorting_pointers(nums, target))
    print(three_sum_has_map(nums, target))


if __name__ == '__main__':
    main()
