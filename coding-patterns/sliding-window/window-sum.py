"""
Problem
Given an array of integers and a window size k, calculate the sum of elements in each sliding window of size k.

Example
Input: nums = [1, 3, 2, 5, 4, 7, 8], k = 3

Output: [6, 10, 11, 16, 19]
"""


def window_sum_option_1(nums: list, k: int) -> list:
    # print(len(nums))
    n = len(nums)
    if n < k:
        return []

    output = []
    for i in range(n - k + 1):
        output.append(sum(nums[i:i + k]))
    print(output)


def window_sum_option_2(nums: list, k: int) -> list:
    n = len(nums)
    if n < k:
        return []
    current_sum = sum(nums[:k])
    output = [current_sum]
    for i in range(1, n - k + 1):
        current_sum = current_sum - nums[i - 1] + nums[i + k - 1]
        output.append(current_sum)
    print(output)


if __name__ == '__main__':
    nums = [1, 3, 2, 5, 4, 7, 8]
    # print(sum(nums[0:3]))
    k = 3

    window_sum_option_2(nums, k)
