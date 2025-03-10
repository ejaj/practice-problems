from collections import Counter


def majorityElement(nums):
    # counts = Counter(nums)
    # return max(counts, key=counts.get)

    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    print(candidate)


nums = [3, 2, 3]  # Output: 3

print(majorityElement(nums))
