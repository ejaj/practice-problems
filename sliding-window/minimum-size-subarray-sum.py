def min_sub_array_len(nums, target):
    current_sum = 0
    min_count = float("inf")
    start = 0
    for i in range(len(nums)):
        current_sum += nums[i]
        while current_sum >= target:
            min_count = min(min_count, i - start + 1)
            current_sum -= nums[start]
            start += 1
    return min_count


nums = [2, 3, 1, 2, 4, 3]
target = 7
print(min_sub_array_len(nums, target))
