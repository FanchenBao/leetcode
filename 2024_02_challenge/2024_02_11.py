# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """
        LeetCode 1463
        
        DP, in which dp[(j1, j2)] is the max value for any path ending
        at a certain row with j1 and j2 being the cells.
        
        We use BFS to go through each row, and a separate DP dict to record
        the max value for each possible (j1, j2) pair. The answer is the max
        value for all the (j1, j2) pairs of the last row.
        
        O(MN^2 * 9), 1081 ms, faster than 57.46%
        """
        M, N = len(grid), len(grid[0]);
        dp = defaultdict(int)
        dp[(0, N - 1)] = grid[0][0] + grid[0][N - 1]
        queue = set([(0, N - 1)])
        for i in range(1, M):
            tmp_queue = set()
            tmp_dp = defaultdict(int)
            for j1, j2 in queue:
                for nj1 in range(max(0, j1 - 1), min(N, j1 + 2)):
                    for nj2 in range(max(nj1 + 1, j2 - 1), min(N, j2 + 2)):
                        tmp_dp[(nj1, nj2)] = max(tmp_dp[(nj1, nj2)], dp[(j1, j2)] + grid[i][nj1] + grid[i][nj2])
                        tmp_queue.add((nj1, nj2))
            queue = tmp_queue
            dp = tmp_dp
        return max(dp.values())



sol = Solution()
tests = [
    ([[3,1,1],[2,5,1],[1,5,5],[2,1,1]], 24),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.cherryPickup(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
