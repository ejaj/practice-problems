"""
Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""

def subarray_roduct_less_than_k(nums, k):
    if k <= 1:
        return 0
    count = 0
    product = 1
    start = 0
    for end in range(len(nums)):
        product *= nums[end]
        # Shrink the window from the start if product is >= k
        while product >= k:
            product /= nums[start]
            start +=1
        # All subarrays ending at `end` with starting indices between `start` and `end` are valid
        count += end - start + 1
    return count
       
        
 
nums = [10,5,2,6] # Output: 8
k = 100

print(subarray_roduct_less_than_k(nums, k))