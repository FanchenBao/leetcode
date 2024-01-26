# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """
        LeetCode 576

        DP with memoization

        O(MNK), where K = maxMove, 85 ms, faster than 75.43%
        """
        MOD = 1000000007
         
        @lru_cache(maxsize=None)
        def dp(i: int, j: int, rem: int) -> int:
            if i < 0 or i == m or j < 0 or j == n:
                return 1
            if rem == 0:
                return 0
            res = 0
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                res = (res + dp(ni, nj, rem - 1)) % MOD
            return res

        return dp(startRow, startColumn, maxMove)




sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
