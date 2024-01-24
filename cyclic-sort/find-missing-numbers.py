def find_missing_numbers(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] > 0 and nums[i] <= len(nums) and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  # Swap
        else:
            i += 1

    # Find the missing numbers
    missing_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
    return missing_numbers


arr = [2, 1, 6, 5, 4]
print("Missing numbers:", find_missing_numbers(arr))
