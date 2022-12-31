# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        self.res = 0
        to_go = 2
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    si, sj = i, j
                to_go += int(grid[i][j] == 0)
        
        def dfs(i: int, j: int, steps: int) -> None:
            steps += 1
            if grid[i][j] == 2:
                if steps == to_go:
                    self.res += 1
            else:
                original = grid[i][j]
                grid[i][j] = -1
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] != -1:
                        dfs(ni, nj, steps)
                grid[i][j] = original

        dfs(si, sj, 0)
        return self.res


sol = Solution()
tests = [
    ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2),
    ([[1,0,0,0],[0,0,0,0],[0,0,0,2]], 4),
    ([[0,1],[2,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.uniquePathsIII(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
