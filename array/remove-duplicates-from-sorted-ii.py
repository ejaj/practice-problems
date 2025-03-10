# inplace true
# allow twice duplicate

# def removeDuplicates(nums):
#     if len(nums) <= 2:
#         return len(nums)
#     k = 2
#     for i in range(2, len(nums)):
#         if nums[i] != nums[k - 2]:
#             nums[k] = nums[i]
#             k += 1
#     return k


def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    count = 1
    for j in range(1, len(nums)):
        if nums[j] == nums[i]:
            count += 1
        else:
            count = 1

        if count <= 2:  # Allow at most 2 occurrences
            i += 1
            nums[i] = nums[j]
    return i + 1


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates(nums))  # output: 5, [1,1,2,2,3,_]
