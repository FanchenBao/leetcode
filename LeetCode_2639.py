# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        """O(MN), 149 ms, faster than 7.30%
        """
        M, N = len(grid), len(grid[0])
        res = [0] * N
        for row in grid:
            for i, v in enumerate(row):
                res[i] = max(res[i], len(str(v)))
        return res


class Solution2:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(grid[i][j])) for i in range(len(grid))) for j in range(len(grid[0]))]

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
