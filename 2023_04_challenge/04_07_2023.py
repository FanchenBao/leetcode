# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        """LeetCode 1020

        The same as the challenge yesterday. DFS, but this time we need to count
        the number of cells in the desired group of connected cells.

        O(MN), 782 ms, faster than 38.76%
        """
        M, N = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            can_go_out = False
            grid[i][j] = 0
            res = 1
            if i == 0 or i == M - 1 or j == 0 or j == N - 1:
                can_go_out = True
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj]:
                    count = dfs(ni, nj)
                    if count > 0:
                        res += count
                    else:
                        can_go_out = True
            return res if not can_go_out else -1

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    res += max(dfs(i, j), 0)
        return res
        

sol = Solution()
tests = [
    ([[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]], 3),
    ([[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.numEnclaves(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
