def getConcatenation(nums):
    print(2 * nums)


def getConcatenation2(nums):
    ans = []
    for i in range(2):
        for num in nums:
            ans.append(num)
    return ans


def getConcatenation3(nums):
    n = len(nums)
    ans = [0] * (2 * n)
    for i, num in enumerate(nums):
        ans[i] = ans[i + n] = num
    return ans


nums = [1, 3, 2, 1]
getConcatenation(nums)
