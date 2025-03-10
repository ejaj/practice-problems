def rotate(nums, k):
    # Brut force
    n = len(nums)
    k = k % n

    for _ in range(k):  # Repeat k times
        last = nums[-1]  # Take the last element
        for i in range(len(nums) - 1, 0, -1):  # Shift elements right
            nums[i] = nums[i - 1]
        nums[0] = last  # Place last element in front
    print(nums)


def rotate_math(nums, k):
    n = len(nums)
    k = k % n
    nums.reverse()  # [7,6,5,4,3,2,1]
    # Reverse first k elements
    nums[:k] = reversed(nums[:k])  # [5, 6, 7, 4, 3, 2, 1]
    nums[k:] = reversed(nums[k:])  # [5,6,7,1,2,3,4]

    # alternative
    # nums[:] = nums[-k:] + nums[:-k]


nums = [1, 2, 3, 4, 5, 6, 7]  # Output: [5,6,7,1,2,3,4]
k = 3
rotate(nums, k)
