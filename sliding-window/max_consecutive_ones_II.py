def max_consecutive_ones_II(nums):
    count = 0  # Count of current consecutive ones
    prev_count = 0  # Count of consecutive ones before the most recent zero
    max_count = 0  # Maximum count of consecutive ones

    for num in nums:
        if num == 1:
            count += 1
        else:
            # If we encounter a zero, update max_count and reset count
            # Store the previous count of ones and start counting again, allowing a flip
            max_count = max(max_count, prev_count + count + 1)
            prev_count = count  # Previous consecutive ones
            count = 0  # Reset count after encountering a zero
            
    # After loop, check if max_count needs to be updated with the last sequence
    max_count = max(max_count, prev_count + count + 1)
    return max_count


def max_consecutive_ones_II_sliding_window(nums):
    left = 0
    max_length = 0
    zero_count = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        # If zero_count is more than 1, we need to shrink the window from the left
        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length        

nums = [1, 0, 1, 1, 0]
print(max_consecutive_ones_II_sliding_window(nums)) 
