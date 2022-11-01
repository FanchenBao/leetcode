# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        """LeetCode 1706

        Brute force. Trace each ball.

        O(MN), 580 ms, faster than 16.76%
        """
        M, N = len(grid), len(grid[0])
        
        def next_cell(i: int, j: int) -> Tuple[int, int]:
            if any([
                grid[i][j] == 1 and (j + 1 == N or grid[i][j]  * grid[i][j + 1] == -1),
                grid[i][j] == -1 and (j - 1 < 0 or grid[i][j]  * grid[i][j - 1] == -1),
            ]):
                return -1, -1
            return i + 1, (j + 1) if grid[i][j] == 1 else (j - 1)

        res = []
        for j in range(N):
            i, jj = 0, j
            while i < M:
                i, jj = next_cell(i, jj)
                if i < 0:
                    break
            res.append(jj)
        return res


sol = Solution()
tests = [
    ([[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]], [1,-1,-1,-1,-1]),
    ([[-1]], [-1]),
    ([[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]], [0,1,2,3,4,-1]),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.findBall(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
