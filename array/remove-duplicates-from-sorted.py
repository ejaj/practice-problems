# inplace - True

def removeDuplicates(nums):
    if not nums:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


def removeDuplicates2(nums):
    if not nums:
        return 0
    l = 1
    for r in range(1, len(nums)):
        if nums[r - 1] != nums[r]:
            l += 1
            nums[l] = nums[r]
    return l
def removeDuplicates3(nums):
    unique = sorted(set(nums))
    nums[:len(unique)] = unique
    print(unique)


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(removeDuplicates3(nums))
