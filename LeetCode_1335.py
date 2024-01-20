# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        """
        This is the DP solution.

        O(N^2D), 624 ms, faster than 70.42%
        """
        N = len(jobDifficulty)
        
        @lru_cache(maxsize=None)
        def dp(idx: int, rem: int) -> int:
            if idx == N and rem == 0:
                return 0
            if rem <= 0 or idx == N:
                return math.inf
            res = math.inf
            cur = 0
            for i in range(idx, N):
                cur = max(cur, jobDifficulty[i])
                res = min(res, cur + dp(i + 1, rem - 1))
            return res

        res = dp(0, d)
        return res if res < math.inf else -1



sol = Solution()
tests = [
    ([6,5,4,3,2,1], 2, 7),
    ([9,9,9], 4, -1),
    ([1,1,1], 3, 3),
]

for i, (jobDifficulty, d, ans) in enumerate(tests):
    res = sol.minDifficulty(jobDifficulty, d)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
