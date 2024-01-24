def find_first_k_missing_positive(nums, k):
    n = len(nums)
    i = 0
    while i < n:
        correct_index = nums[i] - 1
        if 0 <= correct_index < n and nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    missing_numbers = []
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])

    # Add the remaining missing numbers
    i = 1
    while len(missing_numbers) < k:
        candidate = i + n
        if candidate not in extra_numbers:
            missing_numbers.append(candidate)
        i += 1
    return missing_numbers


arr = [3, -1, 4, 5, 5]
k = 3
print("The first", k, "missing positive numbers are:", find_first_k_missing_positive(arr, k))
