# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        This is a 0/1 Knapsack problem. Essentially we are putting items from
        1^x, 2^x, ... to a container of capacity n.

        With DP, the run time can be O(N^2),  1901 ms, faster than 49.05%
        """
        MOD = 1000000007

        @lru_cache(maxsize=None)
        def dp(m: int, rem: int) -> int:
            if rem == 0:
                return 1
            pm = m**x
            if rem < 0 or rem < pm:
                return 0
            return (dp(m + 1, rem) + dp(m + 1, rem - pm)) % MOD
        
        return dp(1, n)


sol = Solution()
tests = [
    (10, 2, 1)
]

for i, (n, x, ans) in enumerate(tests):
    res = sol.numberOfWays(n, x)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
