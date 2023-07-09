# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        """Count the number of cells painted on each row and col as we go
        through arr. The first time either a row or col reaches N or M, we will
        have found the answer.

        O(MN), 1233 ms, faster than 80.24%
        """
        M, N = len(mat), len(mat[0])
        positions = {mat[i][j]: (i, j) for i in range(M) for j in range(N)}
        row_cnts, col_cnts = [0] * M, [0] * N
        for k, a in enumerate(arr):
            i, j = positions[a]
            row_cnts[i] += 1
            col_cnts[j] += 1
            if row_cnts[i] == N or col_cnts[j] == M:
                return k


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
