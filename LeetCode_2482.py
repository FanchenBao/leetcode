# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        """Straightforward solution.

        4962 ms, faster than 23.31%
        """
        M, N = len(grid), len(grid[0])
        ones_row, ones_col = [], []
        for row in grid:
            ones_row.append(sum(row))
        for j in range(N):
            ones_col.append(sum(grid[i][j] for i in range(M)))
        res = []
        for i in range(M):
            res.append([])
            for j in range(N):
                res[-1].append(2 * ones_row[i] - N + 2 * ones_col[j] - M)
        return res
        

sol = Solution()
tests = [
    ([[0,1,1],[1,0,1],[0,0,1]], [[0,0,4],[0,0,4],[-2,-2,2]]),
    ([[1,1,1],[1,1,1]], [[5,5,5],[5,5,5]]),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.onesMinusZeros(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
