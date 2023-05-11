# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """LeetCode 59

        The automatic rotation strategy from yesterday works extremely well with
        this problem.

        O(N^2) 48 ms, faster than 10.60%
        """
        res = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for v in range(1, n * n + 1):
            res[i][j] = v
            if i + di < 0 or i + di >= n or j + dj < 0 or j + dj >= n or res[i + di][j + dj] != 0:
                di, dj = dj, -di
            i += di
            j += dj
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
