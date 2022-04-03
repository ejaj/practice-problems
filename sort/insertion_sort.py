#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : insertion_sort.py
@Time : 4/4/22 12:48 AM
@Desc: Insertion Sort
Time Complexity:
    Best Case - 0(n)
    Worst Case - O(n2)
    Average Case - O(n2)
Space Complexity: 0(1)
"""


def insertion_sort(arr):
    """
    Insertion Sort
    Args:
        arr:

    Returns:

    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def main():
    """
    Main function for drive code
    Returns:

    """
    arr = [9, 5, 1, 4, 3]
    insertion_sort(arr)
    print('Sorted Array in Ascending Order:')
    print(arr)


if __name__ == '__main__':
    main()
