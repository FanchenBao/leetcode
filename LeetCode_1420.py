# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        MOD = 1000000007
        
        @lru_cache(maxsize=None)
        def dp(i: int, p: int, r: int) -> int:
            """
            i is the index on the created arr.
            p is the previous max value encountered in arr.
            r is the remaining new max value allowed (this is related to k)
            """
            if r < 0:
                return 0
            if i == n:
                return 0 if r > 0 else 1 
            # Let current value be not larger than p
            res = p * dp(i + 1, p, r) % MOD
            # Let current value be larger than p
            for np in range(p + 1, m + 1):
                res = (res + dp(i + 1, np, r - 1)) % MOD
            return res

        return dp(0, 0, k)



sol = Solution()
tests = [
    (2, 3, 1, 6),
    (5, 2, 3, 0),
    (9, 1, 1, 1),
]

for i, (n, m, k, ans) in enumerate(tests):
    res = sol.numOfArrays(n, m, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
