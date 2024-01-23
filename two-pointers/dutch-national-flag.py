"""
Problem Statement:
Given an array containing only 0s, 1s, and 2s (representing the colors red, white, and blue respectively),
sort the array so that all 0s are at the beginning, all 1s are in the middle, and all 2s are at the end.

Concept:
The idea is to use three pointers to keep track of the rightmost boundary of 0s (let's call it low), the leftmost
boundary of 2s (high), and the current element under consideration (mid).
The algorithm segregates the 0s, 1s, and 2s without the need for sorting.
Explanation:
Initialization: low and mid are initialized at the start of the array, and high is initialized at the end of the array.
Iterate Through Array: The mid pointer is used to traverse the array.
Sorting Logic:
If arr[mid] is 0, swap it with arr[low] and increment both low and mid.
If arr[mid] is 1, just increment mid.
If arr[mid] is 2, swap it with arr[high] and decrement high.
Termination: The process continues until mid passes high.
This algorithm effectively groups all 0s to the beginning, 1s in the middle, and 2s to the end of the array.
The use of swaps ensures that the space complexity is O(1), and since the array is traversed only once,
the time complexity is O(n).
"""


def dutch_national_flag(arr):
    low, mid, high = 0, 0, len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low, mid = low + 1, mid + 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


arr = [2, 0, 1, 2, 1, 0]
sorted_arr = dutch_national_flag(arr)
print("Sorted Array: ", sorted_arr)
