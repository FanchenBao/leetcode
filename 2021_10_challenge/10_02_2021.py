# from pudb import set_trace; set_trace()
from typing import List
from collections import deque
import math


class Solution1:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """TLE
        """
        m, n = len(dungeon), len(dungeon[0])
        hp = [[math.inf] * n for _ in range(m)]

        def dfs(i: int, j: int, health: int) -> None:
            init_health = max(health - dungeon[i][j], 1)
            if hp[i][j] > init_health:
                hp[i][j] = init_health
                for ni, nj in [(i - 1, j), (i, j - 1)]:
                    if ni >= 0 and nj >= 0:
                        dfs(ni, nj, init_health)

        dfs(m - 1, n - 1, 1)
        return hp[0][0]


class Solution2:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """LeetCode 174

        This is a bottom up DP solution similar to Solution1. We start from
        the lower right corner. We know the min exit health for this cell is 1.
        So we can compute the min entry health for this cell, which is

        max(1 - dungeon[m - 1][n - 1], 1)

        It means if the cell has a negative number, we do 1 minus that negative
        number. If it a positive number smaller than 1, than we do 1 minus that
        number as well. However, if the positive number is bigger than 1, that
        means the min entry health can be just 1. This logic will be used to
        compute the entry health for all the other cells.

        Then, we can compute the min entry health for the right most col and the
        bottom row. Once that is done, we can shift one layer inward, to compute
        the min entry health of row n - 2 and col m - 2. We continue doing so
        until we reach position [0, 0] and compute the min entry health of the
        start.

        O(MN), where M is the number of rows and N cols.

        72 ms, 80% ranking.
        """
        m, n = len(dungeon), len(dungeon[0])
        dungeon[m - 1][n - 1] = max(1 - dungeon[m - 1][n - 1], 1)
        for i in range(m - 2, -1, -1):
            dungeon[i][n - 1] = max(dungeon[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
            dungeon[m - 1][j] = max(dungeon[m - 1][j + 1] - dungeon[m - 1][j], 1)
        i, j = m - 2, n - 2
        while i >= 0 and j >= 0:
            for p in range(i, -1, -1):
                dungeon[p][j] = max(min(dungeon[p + 1][j], dungeon[p][j + 1]) - dungeon[p][j], 1)
            for q in range(j - 1, -1, -1):
                dungeon[i][q] = max(min(dungeon[i + 1][q], dungeon[i][q + 1]) - dungeon[i][q], 1)
            i -= 1
            j -= 1
        return dungeon[0][0]


class Solution3:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        """This is from the discussion linked below.

        https://leetcode.com/problems/dungeon-game/discuss/1498367/C%2B%2BPython-2-solutions%3A-Binary-Search-DP-Clean-and-Concise

        It's the same solution as Solution2, but with much less clutter in the
        implementation.
        """
        m, n = len(dungeon), len(dungeon[0])
        dp = [[math.inf] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = max(min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j], 1)
        return dp[0][0]



sol = Solution3()
tests = [
    ([[-2, -3, 3], [-5, -10, 1], [10, 30, -5]], 7),
    ([[0]], 1),
]

for i, (dungeon, ans) in enumerate(tests):
    res = sol.calculateMinimumHP(dungeon)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
