# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """BFS

        O(MN), 1310 ms, faster than 76.04%
        """
        M, N = len(grid), len(grid[0])
        queue = [(i, 0) for i in range(M)]
        steps = 0
        while queue:
            tmp = set()
            for i, j in queue:
                for di, dj in [(1, 1), (0, 1), (-1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] > grid[i][j]:
                        tmp.add((ni, nj))
            queue = tmp
            steps += 1
        return steps


class Solution2:
    def maxMoves(self, grid: List[List[int]]) -> int:
        """DP also works
        """
        M, N = len(grid), len(grid[0])

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            res = 0
            for di, dj in [(1, 1), (0, 1), (-1, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] > grid[i][j]:
                    res = max(res, 1 + dp(ni, nj))
            return res

        return max(dp(i, 0) for i in range(M))
        

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
