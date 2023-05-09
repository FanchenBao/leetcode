# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter
from functools import lru_cache


class Solution:
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        """This is NOT difficult at all, but I struggled tremendously, because
        I messed up with the edge case checks. This is a very typical DP problem.
        Nothing special actually.

        O(N * T * C), 7493 ms, faster than 5.94%
        """
        MOD = 10**9 + 7

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if rem < 0:
                return 0
            if rem == 0:
                return 1
            if idx == len(types):
                return 0
            res = 0
            for num_to_use in range(types[idx][0] + 1):
                res = (res + dp(idx + 1, rem - num_to_use * types[idx][1])) % MOD
            return res

        return dp(0, target)


sol = Solution()
tests = [
    (6, [[6,1],[3,2],[2,3]], 7),
    (5, [[50,1],[50,2],[50,5]], 4),
    (18, [[6,1],[3,2],[2,3]], 1),
    (6, [[6,1],[6,1]], 7),
]

for i, (target, types, ans) in enumerate(tests):
    res = sol.waysToReachTarget(target, types)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
