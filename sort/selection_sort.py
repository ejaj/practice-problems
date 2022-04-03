#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : selection_sort.py
@Time : 4/4/22 12:17 AM
@Desc: Selection Sort
Time Complexity:
    Best Case - O(n2)
    Worst Case - O(n2)
    Average Case - O(n2)
Space Complexity: 0(1)
"""


def selection_sort(arr, size):
    """
    Selection Sort
    Args:
        arr:
        size:

    Returns:

    """
    for i in range(size):
        min_idx = i

        for j in range(i + 1, size):
            if arr[j] < arr[min_idx]:
                min_idx = j
        (arr[i], arr[min_idx]) = (arr[min_idx], arr[i])


def main():
    """
    Main function for drive code
    Returns:

    """
    arr = [-2, 45, 0, 11, -9]
    size = len(arr)
    selection_sort(arr, size)
    print('Sorted Array in Ascending Order:')
    print(arr)


if __name__ == '__main__':
    main()
