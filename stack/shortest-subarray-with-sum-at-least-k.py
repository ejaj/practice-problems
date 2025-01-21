import collections
from typing import List


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)

        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]

        # print(prefix_sum)
        dq = collections.deque()
        result = float('inf')

        for j in range(n + 1):

            while dq and prefix_sum[j] - prefix_sum[dq[0]] >= k:
                result = min(result, j - dq.popleft())
            while dq and prefix_sum[j] <= prefix_sum[dq[-1]]:
                dq.pop()

            dq.append(j)
        return result if result != float('inf') else -1


nums = [2, -1, 2]
k = 3
s = Solution()
print(s.shortestSubarray(nums, k))
