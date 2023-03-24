# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """TLE
        """
        N = len(nums)
        dp = [0] * (N + 1)
        for j in range(1, k + 1):
            tmp = [math.inf] * (2 * j - 1)
            for i in range(2 * j - 1, N + 1):
                tmp.append(min(tmp[i - 1], max(dp[i - 2], nums[i - 1])))
            dp = tmp
        return min(dp)


sol = Solution()
tests = [
    ([2,3,5,9], 2, 5),
    ([2,7,9,3,1], 2, 2),
    ([3,1,2,4], 2, 3),
]

for i, (nums, k, ans) in enumerate(tests):
    res = sol.minCapability(nums, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
