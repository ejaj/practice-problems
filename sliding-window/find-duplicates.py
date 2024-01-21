def find_duplicates(nums, k):
    d = {}
    for i in range(len(nums)):
        if nums[i] in d and i - d[nums[i]] <= k:
            return True
        else:
            d[nums[i]] = i
    return False


nums = [5, 6, 8, 2, 4, 6, 6, 9]
k = 2

print(find_duplicates(nums, k))
