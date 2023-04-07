# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        """LeetCode 1254

        Any connected 0s that do not touch the edge can form a closed island.
        Therefore, we just need to DFS on any 0, and see after the entire
        connected zero group has been traversed, whether any of them touches
        the edge. If yes, it is not a closed island. Otherwise it is.

        The part that I got bitten is the handling of an edge-touching zero. We
        cannot terminate the DFS when an edge is touched, because we have to
        traverse the entire thing to eliminate this zero group. Instead, we
        shall use a sentinel to indicate that the current group is no good.

        Also, I modify grid in place to indicate which cells have been visited.

        O(MN), 118 ms, faster than 93.84%
        """
        res = 0
        M, N = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> bool:
            grid[i][j] = 1
            success = True
            if i == M - 1 or i == 0 or j == N - 1 or j == 0:
                success = False
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == 0:
                    if not dfs(ni, nj):
                        success = False
            return success

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0 and dfs(i, j):
                    res += 1
        return res
        

sol = Solution()
tests = [
    ([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]], 2),
    ([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]], 1),
    ([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]], 2),
    ([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]], 5),
    ([[1,1,0,1,1,1,1,1,1,1],[0,0,1,0,0,1,0,1,1,1],[1,0,1,0,0,0,1,0,1,0],[1,1,1,1,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,0],[0,0,0,0,1,1,0,0,0,0],[1,0,1,0,0,0,0,1,1,0],[1,1,0,0,1,1,0,0,0,0],[0,0,0,1,1,0,1,1,1,0],[1,1,0,1,0,1,0,0,1,0]], 4),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.closedIsland(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
