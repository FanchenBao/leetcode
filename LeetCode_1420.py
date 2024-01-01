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


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """
        Another attempt to solve this problem (2023-12-30), and this time
        we pretty smoothly succeeded in the first try.
        
        O(MNK), 1115 ms, faster than 78.86%
        """
        MOD = 1000000007

        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int, pre_max: int) -> int:
            if idx == n and rem == 0:
                return 1
            if rem < 0 or (idx == n and rem > 0):
                return 0
            res = (pre_max * dp(idx + 1, rem, pre_max)) % MOD
            for v in range(pre_max + 1, m + 1):
                res = (res + dp(idx + 1, rem - 1, v)) % MOD
            return res

        return dp(0, k, 0)



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
