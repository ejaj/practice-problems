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
    for i in range(len(nums) - 1):
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


def sorting_array_two_sum(nums: List[int], target: int) -> List[int]:
    """
    Sorting and Two-Pointers technique.
    Time Complexity:
        Merge Sort or Heap Sort is used: (-)(nlogn)
        Quick Sort: O(n^2)
    Space Complexity: O(1)
    Args:
        nums:
        target:

    Returns:

    """

    arr_size = len(nums) - 1
    l = 0
    r = arr_size
    while l < r:
        if nums[l] + nums[r] == target:
            return [l, r]
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    return []


def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1


def quick_sort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quick_sort(array, low, pivot - 1)
        quick_sort(array, pivot + 1, high)


def main():
    """
    Main function for drive code
    Returns:

    """
    nums = [1, 2, 6, 8]
    target = 9
    # print(two_sum_b(nums, target))
    # print(two_sum(nums, target))
    print(sorting_array_two_sum(nums, target))


if __name__ == '__main__':
    main()
