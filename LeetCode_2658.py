# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        """This is equivalent to find all the cliques and compute the
        total sum of the nodes. Then find the largest sum among the cliques.

        O(MN), 262 ms, faster than 95.26% 
        """
        M, N = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            res = grid[i][j]
            grid[i][j] = 0
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj]:
                    res += dfs(ni, nj)
            return res

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    res = max(res, dfs(i, j))
        return res
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
