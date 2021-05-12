# from pudb import set_trace; set_trace()
from typing import List


class NumMatrix1:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Very straightforward, sum the rows first, and then sum the columns.

        O(NM), 1524 ms, 15% ranking.

        The numpy solution gives us 240 ms, 24% ranking.
        """
        return sum(sum(self.matrix[r][col1:(col2 + 1)]) for r in range(row1, row2 + 1))


class NumMatrix2:

    def __init__(self, matrix: List[List[int]]):
        """Caching sum of rectangles marked by the lower right corner, as
        as described in the official solution:

        https://leetcode.com/problems/range-sum-query-2d-immutable/solution/

        Since the O(MN) caching is only done once, this solution is blazing fast
        reaching 100 ms, 96% ranking.
        """
        self.M = len(matrix)
        self.N = len(matrix[0])
        self.dp = [[0] * self.N for _ in range(self.M)]
        # cumulative sum of each row
        for i, row in enumerate(matrix):
            for j in range(self.N):
                self.dp[i][j] = row[j] if j == 0 else row[j] + self.dp[i][j - 1]
        # cumulative sum of each rectangle marked by lower right corner.
        for i in range(1, self.M):
            for j in range(self.N):
                self.dp[i][j] += self.dp[i - 1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top = self.dp[row1 - 1][col2] if row1 > 0 else 0
        left = self.dp[row2][col1 - 1] if col1 > 0 else 0
        topleft = self.dp[row1 - 1][col1 - 1] if row1 > 0 and col1 > 0 else 0
        return self.dp[row2][col2] - top - left + topleft

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
