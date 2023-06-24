# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        """LeetCode 1027

        DP with O(N^2), 4463 ms, faster than 18.47%

        UPDATE: since j goes from left to right, we don't need to call max()
        3037 ms, faster than 68.37%
        """
        dp = [{}]
        res = 1
        for i in range(1, len(nums)):
            dp.append({})
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[-1][diff] = dp[j].get(diff, 1) + 1
                res = max(res, dp[-1][diff])
        return res


sol = Solution()
tests = [
    ([3,6,9,12], 4),
    ([9,4,7,2,10], 3),
    ([20,1,15,3,10,5,8], 4),
    ([1,1,1,1], 4),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.longestArithSeqLength(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
