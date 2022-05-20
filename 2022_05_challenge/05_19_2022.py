# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """LeetCode 329

        DP solution. DFS from each cell and find the max length of increasing
        path starting from each cell. If the max length of a cell has been
        found already, we don't have to compute it again.

        O(MN), 692 ms, faster than 36.57% 
        """
        M, N = len(matrix), len(matrix[0])
        dp = [[0] * N for _ in range(M)]
        self.res = 0

        def dfs(i: int, j: int) -> None:
            dp[i][j] = 1
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] > matrix[i][j]:
                    if not dp[ni][nj]:
                        dfs(ni, nj)
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
            self.res = max(self.res, dp[i][j])

        for i in range(M):
            for j in range(N):
                if not dp[i][j]:
                    dfs(i, j)
        return self.res



class Solution2:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        """Bottom up solution. Sort the matrix by its value descend, then we
        can go through each value in a deterministic fashion.

        391 ms, faster than 96.41% (so much faster)
        """
        M, N = len(matrix), len(matrix[0])
        dp = [[1] * N for _ in range(M)]
        flat_m = [(v, i, j) for i, row in enumerate(matrix) for j, v in enumerate(row)]
        res = 0
        for v, i, j in sorted(flat_m, reverse=True):
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and matrix[ni][nj] > v:
                    dp[i][j] = max(dp[i][j], 1 + dp[ni][nj])
            res = max(res, dp[i][j])
        return res


sol = Solution2()
tests = [
    ([[9,9,4],[6,6,8],[2,1,1]], 4),
    ([[3,4,5],[3,2,6],[2,2,1]], 4),
    ([[1]], 1),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.longestIncreasingPath(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
