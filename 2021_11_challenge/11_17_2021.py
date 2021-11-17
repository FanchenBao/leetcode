# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
from math import factorial


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """LeetCode 62

        DFS. O(MN), 28 ms, 88% ranking.
        """
        
        @lru_cache()
        def dfs(i: int, j: int) -> int:
            if i == m - 1 and j == n - 1:
                return 1
            if 0 <= i < m and 0 <= j < n:
                return dfs(i, j + 1) + dfs(i + 1, j)
            return 0
        
        return dfs(0, 0)


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        """Bottom up
        """
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m - 1][n - 1] = 1
        queue = set([(m - 1, n - 1)])
        while queue:
            temp = set()
            for i, j in queue:
                if (i - 1, j) not in temp and i - 1 >= 0:
                    temp.add((i - 1, j))
                    dp[i - 1][j] = dp[i][j] + dp[i - 1][j + 1]
                if (i, j - 1) not in temp and j - 1 >= 0:
                    temp.add((i, j - 1))
                    dp[i][j - 1] = dp[i][j] + dp[i + 1][j - 1]
            queue = temp
        return dp[0][0]


class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        """Math solution. The grid, if rotated, can be seen as a Pascal Triangle
        Then the problem becomes finding the mth value of the (m + n - 1)th row
        on a Pascal triangle.
        """
        a, b = m + n - 1 - 1, m - 1
        return factorial(a) // (factorial(a - b) * factorial(b))


sol = Solution3()
tests = [
    (3, 7, 28),
    (3, 2, 3),
    (7, 3, 28),
    (3, 3, 6),
]

for i, (m, n, ans) in enumerate(tests):
    res = sol.uniquePaths(m, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
