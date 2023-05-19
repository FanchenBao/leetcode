# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        """Find the positions of each step, and then trace it from start to end
        and see if each step is valid.

        O(N^2), 87 ms, faster than 5.77%
        """
        N = len(grid)
        pos = [None] * (N * N)
        for i in range(N):
            for j in range(N):
                pos[grid[i][j]] = (i, j)
        if pos[0] != (0, 0):
            return False
        deltas = {(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)}
        for k in range(1, N * N):
            if (pos[k][0] - pos[k - 1][0], pos[k][1] - pos[k - 1][1]) not in deltas:
                return False
        return True


class Solution2:
    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        """O(1) space.
        """
        if grid[0][0] != 0:
            return False
        i = j = step = 0
        N = len(grid)
        while step < N * N - 1:
            for di, dj in [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == step + 1:
                    step += 1
                    i, j = ni, nj
                    break
            else:
                return False
        return True


sol = Solution2()
tests = [
    ([[0,11,16,5,20],[17,4,19,10,15],[12,1,8,21,6],[3,18,23,14,9],[24,13,2,7,22]], True),
    ([[0,3,6],[5,8,1],[2,7,4]], False),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.checkValidGrid(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
