# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        LeetCode 73

        Do not return anything, modify matrix in-place instead.

        I use math.inf as a flag to turn values other than the original zeroes
        into zeroes.

        O(MN(M + N)), where M is the number of rows, N the number of columns.
        O(1) space

        140 ms, 20% ranking.
        """
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    for k in range(N):
                        matrix[i][k] = math.inf if matrix[i][k] else 0
                    for k in range(M):
                        matrix[k][j] = math.inf if matrix[k][j] else 0
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == math.inf:
                    matrix[i][j] = 0


class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Record the rows and cols
        O(MN) time and O(M + N) space
        """
        rows = set()
        cols = set()
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(M):
            for j in range(N):
                if i in rows or j in cols:
                    matrix[i][j] = 0


class Solution3:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Official solution approach 2 (originally approach 3. I eve left a
        comment there)

        https://leetcode.com/problems/set-matrix-zeroes/solution/

        Apparently, I have marveled at this approach more than two years ago,
        but still it took me a while to fully comprehend. It is very smart. It
        uses the first row and first column as markers to indicate whether a
        col and a row will be zero. If we iterate first row and first col, then
        second row second col, etc. we can avoid hitting the marker zeroes. This
        means we can separate the marker zeroes from the real zeroes.
        """
        first_col_zero = False
        M, N = len(matrix), len(matrix[0])
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    if j == 0:
                        first_col_zero = True
                    else:
                        matrix[i][0] = 0  # use first col to mark the row that will all turn into zero
                        matrix[0][j] = 0  # use first row to mark the col that will all turn into zero
        # Notice that we will treat the first row and col separately
        for i in range(1, M):
            for j in range(1, N):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        # Handle first row
        if not matrix[0][0]:
            for j in range(N):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(M):
                matrix[i][0] = 0




# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
