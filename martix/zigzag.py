#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""

@Author : kazi
@File : zigzag.py
@Time : 7/21/22 10:20 PM
@Desc: 
"""

ROW = 5
COL = 4


def diagonal_order_1(arr, r, c):
    ans = [[] for i in range(r + c - 1)]
    for i in range(c):
        for j in range(r):
            ans[i + j].append(arr[j][i])
    for i in range(len(ans)):
        for j in range(len(ans[i])):
            print(ans[i][j], end=" ")
        print()


def diagonal_order(matrix):
    for line in range(1, (ROW + COL)):
        start_col = max(0, line - ROW)
        count = min(line, COL - start_col, ROW)
        for i in range(0, count):
            print(matrix[min(ROW, line) - i - 1][start_col + i], end="\t")


def print_matrix(matrix):
    for i in range(0, ROW):
        for j in range(0, COL):
            print(matrix[i][j], end="\t")
        print()


M = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],
     [17, 18, 19, 20]]
# print("Given matrix is ")
# # print_matrix(M)
# print("\nDiagonal printing of matrix is ")
# diagonal_order(M)
diagonal_order_1(M, ROW, COL)
