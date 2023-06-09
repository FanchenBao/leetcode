# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        """LeetCode 1351

        Zigzag from top right to bottom left. Each time a negative is found, the
        rest of the col must all be negative. Then we move left and keep search
        downwards.

        O(M + N), 141 ms, faster than 14.35%

        UPDATE: use better condition for the while loop, we can simplify the
        implementation a bit
        """
        M, N = len(grid), len(grid[0])
        i, j = 0, N - 1
        res = 0
        while j >= 0:
            while i < M and grid[i][j] >= 0:
                i += 1
            res += M - i
            j -= 1
        return res
                    

sol = Solution()
tests = [
    ([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]], 8),
    ([[3,2],[1,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.countNegatives(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
