#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : merge_sort.py
@Time : 4/4/22 1:18 AM
@Desc: Merge Sort
Time Complexity:
    Best Case - O(n*log n)
    Worst Case - O(n*log n)
    Average Case - O(n*log n)
Space Complexity: 0(n)
"""


def merge_sort(arr):
    """
    Merge Sort
    Args:
        arr:

    Returns:

    """
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        M = arr[mid:]

        merge_sort(L)
        merge_sort(M)
        i = j = k = 0
        # Until we reach either end of either L or M, pick larger among
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = M[j]
                j += 1
            k += 1
        # When we run out of elements in either L or M,
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(M):
            arr[k] = M[j]
            j += 1
            k += 1


def print_arr(arr):
    """
    Print array values
    Args:
        arr:

    Returns:

    """
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def main():
    """
    Main function for drive code
    Returns:

    """
    arr = [6, 5, 12, 10, 9, 1]
    merge_sort(arr)
    print("Sorted array is: ")
    print_arr(arr)


if __name__ == '__main__':
    main()
