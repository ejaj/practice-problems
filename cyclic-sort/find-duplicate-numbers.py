def find_duplicate_numbers(nums):
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]  # Swap
        else:
            i += 1

    # Find duplicates
    duplicate_numbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])

    return duplicate_numbers


# Example Usage
arr = [3, 4, 4, 5, 5]
print("Duplicate numbers:", find_duplicate_numbers(arr))
