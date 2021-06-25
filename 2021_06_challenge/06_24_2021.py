# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """LeetCode 576

        Not very difficult. A typical DP problem. We record the number of
        ways to move out of bound for each consecutive moves. For instance, with
        move 1, we have all the edges eligible to move out of bound. We record
        the number of ways each eligible cell can move out of bound (basically
        everyone on the edge has one way to move out of bound, except for the
        four corners, which have two ways). Then we consider the second move.
        We go through each cell and see if a cell's next move can end up at a
        cell that is eligible for one-move out of bound. If it's possible, we
        increment the number of ways for the two-move eligible cell with the
        number of ways in the one-move eligible cell. We continue this operation
        until reaching maxMove.

        At each round, we increment the result by adding the number of ways at
        location startRow, startColumn for the current move.

        The tricky part that got to me was that I forgot to consider the zero
        move situation. But it was resolved by simply setting up a check at the
        very beginning for maxMove == 0.

        O(KMN), where K = maxMove, M is the number of rows in the grid, and N
        the numbre of columns. 364 ms, 18% ranking.
        """
        if not maxMove:
            return 0
        pre = [[0] * n for _ in range(m)]
        for j in range(n):  # base case for one move
            pre[0][j] += 1
            pre[-1][j] += 1
        for i in range(m):
            pre[i][0] += 1
            pre[i][-1] += 1
        res = pre[startRow][startColumn]
        for _ in range(maxMove - 1):
            cur = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(n):
                    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < m and 0 <= nj < n and pre[ni][nj]:
                            cur[i][j] += pre[ni][nj]
            res += cur[startRow][startColumn]
            pre = cur
        return res % 1000000007


class Solution2:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        """The recursive solution. Courtesy of:

        https://leetcode.com/problems/out-of-boundary-paths/discuss/1293727/Python-Short-dp-%2B-educational-matrix-exponentiation-explained

        However, as I was trying to write it myself, I got massively blocked by
        the terminating case. I was checking for numMove first, and then the
        i and j. This is not correct, because i and j can be out of bound for
        multiple moves and eventually end up at the right position that I want.
        Yet this is not a correct case. E.g. we want to take three moves to get
        to (-1, 0), and we have (0, 0) -> (-1, 0) -> (-2, 0) -> (-1, 0). So we
        have achieved going from (0, 0) to (-1, 0) in three moves. This shall
        count as a way, right? No, because we went out of bound for multiple
        moves, which is not allowed.

        Therefore, the correct terminating case is to check for out of bound
        first. As long as we go out of bound for the first time, that is a valid
        way. After that, we check for numMoves.

        One more thing to mention is the speed. This solution has the same
        complexity as Solution1, but it runs 124 ms, much faster. This is most
        likely due to lru_cache being more optimized than preparing the DP table
        ourselves.
        """

        @lru_cache(maxsize=None)
        def dfs(i: int, j: int, numMove: int) -> int:
            if i < 0 or i >= m or j < 0 or j >= n:
                return 1
            if numMove == 0:
                return 0
            return sum(dfs(i + di, j + dj, numMove - 1) for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)])

        return dfs(startRow, startColumn, maxMove) % 1000000007


sol = Solution2()
tests = [
    # (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12),
    # (3, 8, 0, 2, 0, 0),
]

for i, (m, n, maxMove, startRow, startColumn, ans) in enumerate(tests):
    res = sol.findPaths(m, n, maxMove, startRow, startColumn)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
