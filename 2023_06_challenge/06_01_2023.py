# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """LeetCode 1091

        I have struggled, solved, and revisited this problem since June 2019!
        I am very glad that after years of practice, it has finally become a
        routine reflex that problems like this, i.e. shortest path, shall be
        attempted by BFS as the first approach.

        O(N^2), 501 ms, faster than 97.97%
        """
        if grid[0][0] == 1:
            return -1
        queue = [(0, 0)]
        grid[0][0] = 1
        steps, N = 1, len(grid)
        while queue:
            tmp = []
            for i, j in queue:
                if i == j == N - 1:
                    return steps
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and not grid[ni][nj]:
                        grid[ni][nj] = 1
                        tmp.append((ni, nj))
            queue = tmp
            steps += 1
        return -1


sol = Solution()
tests = [
    ([[0,1],[1,0]], 2),
    ([[0,0,0],[1,1,0],[1,1,0]], 4),
    ([[1,0,0],[1,1,0],[1,1,0]], -1),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.shortestPathBinaryMatrix(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
