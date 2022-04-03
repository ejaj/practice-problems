#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : bubble_sort.py
@Time : 4/4/22 12:01 AM
@Desc: Bubble Sort
Time Complexity:
    Best Case - 0(n)
    Worst Case - O(n2)
    Average Case - O(n2)
Space Complexity: 0(1)
"""


def bubble_sort(arr):
    """
    Bubble Sort
    Args:
        arr:

    Returns:

    """
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp


def optimized_bubble_sort(arr):
    """
    Optimized Bubble Sort. The value of swapped is set true if there occurs swapping of elements.
    Otherwise, it is set false.
    Args:
        arr:

    Returns:

    """
    for i in range(len(arr)):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True
        if not swapped:
            break


def main():
    """
    Main function for driving code
    Returns:

    """
    arr = [-2, 45, 0, 11, -9]
    bubble_sort(arr)
    optimized_bubble_sort(arr)
    print('Sorted Array in Ascending Order:')
    print(arr)


if __name__ == '__main__':
    main()
