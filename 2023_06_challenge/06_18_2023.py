# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        """LeetCode 2328

        Use DP, where dp(i, j) is the total number of ways to produce strictly
        increasing paths starting from (i, j). Use an external memo to record
        the result and add together dp(i, j) for each i, j pair.

        O(MN), 2956 ms, faster than 16.51% 
        """
        memo = defaultdict(int)
        M, N = len(grid), len(grid[0])
        MOD = 10**9 + 7

        def dp(i: int, j: int) -> int:
            if memo[(i, j)]:
                return memo[(i, j)]
            memo[(i, j)] = 1
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j +dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] > grid[i][j]:
                    memo[(i, j)] = (memo[(i, j)] + dp(ni, nj)) % MOD
            return memo[(i, j)]

        res = 0
        for i in range(M):
            for j in range(N):
                res = (res + dp(i, j)) % MOD
        return res
        

sol = Solution()
tests = [
    ([[1,1],[3,4]], 8),
    ([[1],[2]], 3),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.countPaths(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
