"""
You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty
subarray
 of nums, or return -1 if no special subarray exists.



Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:

The subarray [3] has OR value of 3. Hence, we return 1.

Example 2:

Input: nums = [2,1,8], k = 10

Output: 3

Explanation:

The subarray [2,1,8] has OR value of 11. Hence, we return 3.

Example 3:

Input: nums = [1,2], k = 0

Output: 1

Explanation:

The subarray [1] has OR value of 1. Hence, we return 1.
"""


def shortest_special_subarray(nums, k):
    n = len(nums)
    min_length = float('inf')

    # Loop through all possible start indices
    for start in range(n):
        current_or = 0
        # Extend the subarray from start to end
        for end in range(start, n):
            current_or |= nums[end]
            # Check if the current OR is at least k
            if current_or >= k:
                min_length = min(min_length, end - start + 1)
                break  # No need to extend this subarray further once condition is met

    return min_length if min_length != float('inf') else -1


# Test cases
print(shortest_special_subarray([1, 2, 3], 2))  # Output: 1
print(shortest_special_subarray([2, 1, 8], 10))  # Output: 3
print(shortest_special_subarray([1, 2], 0))  # Output: 1
