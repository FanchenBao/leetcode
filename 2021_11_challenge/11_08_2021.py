# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution:
    def numTrees(self, n: int) -> int:
        """LeetCode 96

        Top down DP.

        O(N^2), 32 ms, 67% ranking.
        """
        
        @lru_cache(maxsize=None)
        def dfs(lo: int, hi: int) -> int:
            if lo >= hi:
                return 1
            res = 0
            for i in range(lo, hi + 1):
                res += dfs(lo, i - 1) * dfs(i + 1, hi)
            return res

        return dfs(1, n)


sol = Solution()
tests = [
    (3, 5),
    (1, 1),
]

for i, (n, ans) in enumerate(tests):
    res = sol.numTrees(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
