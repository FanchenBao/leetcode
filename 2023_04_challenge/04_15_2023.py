# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        """LeetCode 2218

        Use DP, where dp[i][j] is the max value of j coins taken from piles[i]
        to the end.

        O(SK), where S is the total number of coins in piles.
        6047 ms, faster than 20.76%
        """
        N = len(piles)

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if idx >= N or rem == 0:
                return 0
            res = dp(idx + 1, rem)
            s = 0  # accumulate the coin values in the current pile
            for i, c in enumerate(piles[idx]):
                if rem - i - 1 < 0:  # no more coin to take
                    break
                s += c
                res = max(res, s + dp(idx + 1, rem - i - 1))
            return res

        return dp(0, k)


sol = Solution()
tests = [
    ([[1,100,3],[7,8,9]], 2, 101),
    ([[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], 7, 706),
]

for i, (piles, k, ans) in enumerate(tests):
    res = sol.maxValueOfCoins(piles, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
