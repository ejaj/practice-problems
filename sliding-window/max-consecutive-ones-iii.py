""""
Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
"""

def longest_ones(nums, k):
    left = 0
    max_length = 0
    zero_count = 0

    for right in range(len(nums)):
        # If we encounter a 0, increment the zero_count
        if nums[right] == 0:
            zero_count += 1

        # If zero_count exceeds k, shrink the window from the left
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        # Update max_length with the current window size
        max_length = max(max_length, right - left + 1)

    return max_length

# Test the function
nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
print(longest_ones(nums, k))  # Output: 6
