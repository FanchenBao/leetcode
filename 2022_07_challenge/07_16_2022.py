# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """Memory limit exceeded.
        """
        queue = [(startRow, startColumn)]
        res = 0
        while queue and maxMove:
            temp = []
            for i, j in queue:
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        res += 1
                    else:
                        temp.append((ni, nj))
            maxMove -= 1
            queue = temp
        return res % (10**9 + 7)


class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """LeetCode

        Seems to be easy enough but I got kinda stuck and made a silly mistake.
        My initial idea of BFS takes way too much memory. This one builds the
        grid, and sequentially increment the number of ways each cell can reach
        out of bound in the current number of ways. We start with the number
        of ways to go out of bound in one move. Then we say the number of ways
        to go out of bound in two moves is equal to the sum of the number of
        ways to go out of bound in one move, whose cell we can reach in one
        move from the current cell. We keep doing this until hitting maxMove.

        O(4MNK), where K = maxMove.  593 ms, faster than 8.69%

        UPDATE: doing MOD only at the end: 452 ms, faster than 15.85%
        """
        if not maxMove:
            return 0
        MOD = 10**9 + 7
        mat = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if ni < 0 or ni >= m or nj < 0 or nj >= n:
                        mat[i][j] += 1
        maxMove -= 1
        res = mat[startRow][startColumn]
        while maxMove:
            temp = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for di, dj in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            temp[i][j] += mat[ni][nj]
            mat = temp
            res += mat[startRow][startColumn]
            maxMove -= 1
        return res % MOD


class Solution3:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """I struggled putting tihs top down DP together, but it is actually
        quite straightforward. dp(i, j, move) represents the max number of
        moves to go from i, j to out of bound given maxMove = move. So for any
        cell i, j, to know dp(i, j, move), we only need to know the max number
        of moves of move - 1 in its neighbors.

        O(4MNK). 183 ms, faster than 62.66% 

        It's faster, because we start from the target, and don't have to go
        through all the cells.
        """
        @lru_cache(maxsize=None)
        def dp(i: int, j: int, move: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if not move:
                return 0
            return sum([
                dp(i + 1, j, move - 1),
                dp(i - 1, j, move - 1),
                dp(i, j + 1, move - 1),
                dp(i, j - 1, move - 1),
            ])

        return dp(startRow, startColumn, maxMove) % (10**9 + 7)


sol = Solution3()
tests = [
    (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12),
    (7, 6, 13, 0, 2, 1659429),
    (10, 10, 0, 5, 5, 0),
]

for i, (m, n, maxMove, startRow, startColumn, ans) in enumerate(tests):
    res = sol.findPaths(m, n, maxMove, startRow, startColumn)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
