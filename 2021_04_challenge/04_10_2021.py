# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """LeetCode 329

        DP solution. At each cell of the dp table, we record the longest
        path that starts from the value in that cell. As we iterate through the
        entire matrix, we can build up the dp table, and the result will be the
        max of the dp table.

        O(N), since we visit each cell only once. 452 ms, 75% ranking.
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        def dfs(i: int, j: int) -> int:
            if dp[i][j]:
                return dp[i][j]
            dp[i][j] = 1
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dfs(ni, nj))
            return dp[i][j]

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))
        return res


class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Bottom up solution"""
        m, n = len(matrix), len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        flat_m = [(v, i, j) for i, row in enumerate(matrix) for j, v in enumerate(row)]
        res = 1
        for v, i, j in sorted(flat_m, reverse=True):
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
            res = max(res, dp[i][j])
        return res


sol = Solution2()
tests = [
    ([[9, 9, 4], [6, 6, 8], [2, 1, 1]], 4),
    ([[3, 4, 5], [3, 2, 6], [2, 2, 1]], 4),
    ([[1]], 1)
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.longestIncreasingPath(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
