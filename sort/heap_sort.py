#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : heap_sort.py.py
@Time : 4/3/22 11:43 PM
@Desc: Heap Sort
Time Complexity:
    Best Case - O(nlog n)
    Worst Case - O(nlog n)
    Average Case - O(nlog n)
Space Complexity - 0(1)
"""


def heapify(arr, n, i):
    """
    Heapify the array/tree
    Args:
        arr:
        n:
        i:

    Returns:

    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Sort the array
    Args:
        arr:

    Returns:

    """
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def main():
    """
    Main function for drive the code.
    Returns:

    """
    arr = [1, 12, 9, 5, 6, 10]
    heap_sort(arr)
    n = len(arr)
    print("Sorted array is")
    for i in range(n):
        print("%d " % arr[i], end='')


if __name__ == '__main__':
    main()
