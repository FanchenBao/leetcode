# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        N = len(grid)
        manhattan = [[1000000000] * N for _ in range(N)]
        # find all the thieves, and put them in the queue
        queue = []
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    queue.append((i, j, 0))
                    manhattan[i][j] = 0
        # fill out dp by finding the min Manhattan distance of each cell
        while queue:
            tmp = []
            for i, j, d in queue:
                manhattan[i][j] = d
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and d + 1 < manhattan[ni][nj]:
                        tmp.append((ni, nj, d + 1))
            queue = tmp
        # BFS one more time to find the max safeness factor of all the paths
        # ending up at cell (i, j)
        dp = [[0] * N for _ in range(N)]
        queue = [(0, 0, manhattan[0][0])]
        visited = set([(0, 0, manhattan[0][0])])
        while queue:
            tmp = []
            for i, j, safeness in queue:
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N:
                        dp[ni][nj] = min(max(safeness, dp[ni][nj]), manhattan[ni][nj])
                        cur = (ni, nj, dp[ni][nj])
                        if cur not in visited:
                            tmp.append(cur)
                            visited.add(cur)
            queue = tmp
        return dp[N - 1][N - 1]


sol = Solution()
tests = [
    # ([[1,0,0],[0,0,0],[0,0,1]], 0),
    # ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
    ([[0, 1, 1], [0, 1, 1], [1, 1, 1]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maximumSafenessFactor(grid)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
