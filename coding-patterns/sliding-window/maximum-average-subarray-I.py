"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.



Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
"""

from typing import List


def find_max_average(nums: List[int], k: int) -> float:
    n = len(nums)
    if n < k:
        return float('-inf')
    current_sum = sum(nums[:k])
    max_average = current_sum / k
    for i in range(1, n - k + 1):
        current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
        average = current_sum / k
        max_average = max(max_average, average)
    print(max_average)


nums = [1, 12, -5, -6, 50, 3]
k = 4

find_max_average(nums, k)
