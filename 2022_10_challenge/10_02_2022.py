# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        """LeetCode 1155

        Very classic DP problem.

        O(TN), where T is target. 330 ms, faster than 86.00% 
        """
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(idx: int, tgt: int) -> int:
            if tgt <= 0:
                return 0
            if idx == n:
                return int(tgt <= k)
            return sum(dp(idx + 1, tgt - i) for i in range(1, k + 1))

        return dp(1, target) % MOD
        

sol = Solution()
tests = [
    (1, 6, 3, 1),
    (2, 6, 7, 6),
    (30, 30, 500, 222616187),
    (3, 6, 12, 25),
    (5, 6, 20, 651),
]

for i, (n, k, target, ans) in enumerate(tests):
    res = sol.numRollsToTarget(n, k, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
