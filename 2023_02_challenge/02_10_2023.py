# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """TLE"""
        water, land = [], []
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    land.append([i, j])
                else:
                    water.append([i, j])
        if not water or not land:
            return -1
        res = 0
        for x, y in water:
            cur = math.inf
            for a, b in land:
                cur = min(cur, abs(x - a) + abs(y - b))
            res = max(res, cur)
        return res


class Solution2:
    def maxDistance(self, grid: List[List[int]]) -> int:
        """LeetCode 1162

        BFS starting from land. We just need to find the longest steps needed
        to traverse all the water.

        O(N^2)
        """
        queue = []
        N = len(grid)
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    queue.append([i, j])
        if not queue or len(queue) == N * N:
            return -1
        steps = 0
        while queue:
            tmp = []
            for i, j in queue:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0:
                        grid[ni][nj] = 1
                        tmp.append([ni, nj])
            steps += 1
            queue = tmp
        return steps - 1


sol = Solution2()
tests = [
    ([[1,0,1],[0,0,0],[1,0,1]], 2),
    ([[1,0,0],[0,0,0],[0,0,0]], 4),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maxDistance(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
