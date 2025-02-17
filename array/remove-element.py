def removeElement(nums, val):
    k = 0
    for i in range(len(nums) - 1):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    print(k)


nums = [3, 2, 2, 3]
val = 3
removeElement(nums, val)
