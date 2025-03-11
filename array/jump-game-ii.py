def jump(nums):
    n = len(nums)
    if n == 1:
        return 0
    jumps = 0
    farthest = 0
    current_end = 0
    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps
    return jumps


def jump_recursive(nums, index):
    if index >= len(nums) - 1:
        return 0  # Reached last index

    min_jumps = float('inf')  # Initialize with a large value
    max_jump = nums[index]
    for j in range(1, max_jump + 1):
        next_index = index + j
        if next_index < len(nums):
            jumps = 1 + jump_recursive(nums, next_index)
            min_jumps = min(min_jumps, jumps)
    return min_jumps


def min_jumps(nums):
    return jump_recursive(nums, 0)


nums = [2, 3, 1, 1, 4]
print(min_jumps(nums))  # Output: 2
