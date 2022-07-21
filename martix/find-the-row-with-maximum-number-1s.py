#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : find-the-row-with-maximum-number-1s.py
@Time : 7/22/22 12:45 AM
@Desc: 
"""
ROW = 4
COL = 4


def first_1(arr, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if (mid == 0 or arr[mid - 1] == 0) and arr[mid] == 1:
            return mid
        elif arr[mid] == 0:
            return first_1(arr, (mid + 1), high)
        else:
            return first_1(arr, low, (mid - 1))
    return -1


def row_with_max_1s(mat):
    row_index, max_count = 0, -1
    for i in range(ROW):
        index = first_1(mat[i], 0, COL - 1)
        if index != -1 and ROW - index > max_count:
            max_count = COL - index
            row_index = i
    return row_index


def find_the_row_maximum(arr, r, c):
    max_count = 0
    row_index = -1
    for i in range(r):
        count = 0
        for j in range(c):
            if arr[i][j] == 1:
                count = count + 1
        if count > max_count:
            max_count = count
            row_index = i
    return row_index


mat = [[0, 0, 0, 1],
       [0, 1, 1, 1],
       [1, 1, 1, 1],
       [0, 0, 0, 0]]
print(find_the_row_maximum(mat, ROW, COL))
