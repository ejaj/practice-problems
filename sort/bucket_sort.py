#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : bucket_sort.py
@Time : 4/3/22 12:28 AM
@Desc: Bucket Sort
Time Complexity:
    Best Case - O(n+k)
    Worst Case - O(n2)
    Average Case - O(n)
Space Complexity: O(n+k)
"""
from typing import List


def bucket_sort(array: List[float]) -> List[float]:
    """
    Bucket sort.
    Args:
        array:

    Returns:

    """
    bucket = []
    for i in range(len(array)):
        bucket.append([])
    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array


def main():
    """
    main function to drive code.
    Returns:

    """
    array = [.42, .32, .33, .52, .37, .47, .51]
    print("Sorted Array in descending order is")
    print(bucket_sort(array))


if __name__ == '__main__':
    main()
