def canJump(nums):
    max_reach = 0
    for i in range(len(nums)):
        if i > max_reach:  # If we reach a point we cannot jump to, return False
            return False
        max_reach = max(max_reach, i + nums[i])

        if max_reach >= len(nums) - 1:  # If we can reach the last index, return True
            return True
    return True


nums = [2, 3, 1, 1, 4]  # Output true

print(canJump(nums))
