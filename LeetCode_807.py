# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        """Find the max value each cell can take by first finding the max of
        each row and col. Then the answer is the difference in each cell
        between the max it can take and the original value.

        O(N^2), 71 ms, faster than 98.42%
        """
        N = len(grid)
        rows = [max(row) for row in grid]
        cols = []
        for j in range(N):
            cols.append(max(grid[i][j] for i in range(N)))
        return sum(min(rows[i], cols[j]) - grid[i][j] for i in range(N) for j in range(N))
        

sol = Solution()
tests = [
    ([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]], 35),
    ([[0,0,0],[0,0,0],[0,0,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maxIncreaseKeepingSkyline(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
