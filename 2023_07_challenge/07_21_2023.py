# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        """LeetCode 673

        DP contains two values, one is the max length of LIS so far, and the
        other is the total number of LISes that can reach such length ending
        at the current index.

        O(N^2), 1282 ms, faster than 41.58%
        """
        # dp[i] = (length of LIS, count of LIS)
        dp = []
        max_lis = 0
        for i, n in enumerate(nums):
            cur = [1, 1]
            for j in range(i):
                if nums[j] < n:
                    if dp[j][0] + 1 == cur[0]:
                        cur[1] += dp[j][1]
                    elif dp[j][0] + 1 > cur[0]:
                        cur = [dp[j][0] + 1, dp[j][1]]
            dp.append(cur)
            max_lis = max(max_lis, cur[0])
        return sum(c for l, c in dp if l == max_lis)
        

sol = Solution()
tests = [
    ([1,3,5,4,7], 2),
    ([2,2,2,2,2], 5),
    ([1,2,4,3,5,4,7,2], 3)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findNumberOfLIS(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
