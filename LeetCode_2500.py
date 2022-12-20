# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        """
        O(MNlogN + MN), 96 ms, faster than 96.99%
        """
        for row in grid:
            row.sort(reverse=True)
        res = 0
        for j in range(len(grid[0]) - 1, -1, -1):
            res += max(grid[i][j] for i in range(len(grid)))
        return res


sol = Solution()
tests = [
    ([[1,2,4],[3,3,1]], 8),
    ([[10]], 10),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.deleteGreatestValue(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
