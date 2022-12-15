# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def rob(self, nums: List[int]) -> int:
        """LeetCode 198

        Standard DP

        O(N), 43 ms, faster than 75.87%
        """
        dp = [0, nums[0]]
        for i in range(1, len(nums)):
            dp.append(max(dp[-1], nums[i] + dp[-2]))
        return dp[-1]


sol = Solution()
tests = [
    ([1,2,3,1], 4),
    ([2,7,9,3,1], 12),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.rob(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
