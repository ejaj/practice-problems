def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        corrected_index = nums[i] - 1
        if nums[i] != nums[corrected_index]:
            nums[i], nums[corrected_index] = nums[corrected_index], nums[i]  # Swap
        else:
            i += 1
    return nums


arr = [3, 5, 2, 1, 4]
sorted_arr = cyclic_sort(arr)
print("Sorted Array:", sorted_arr)
