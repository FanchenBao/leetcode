# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """LeetCode 120

        DFS with memoization. Straightforward solution. We traverse the
        entire triangle and record the min sum starting at each number going
        down.

        O(N), because each number is only visited once.
        108 ms, which is beyond the ranking range. This is pretty bad.

        The space complexity is O(N), where N is the number numbers in the
        triangle. This does not satisfy the follow up requirement, where the
        space complexity should be O(M), where M is the number of rows in the
        tirangle.
        """
        M = len(triangle)
        dp = [[math.inf] * M for _ in range(M)]

        def dfs(i: int, j: int) -> int:
            if i == M:
                return 0
            if dp[i][j] == math.inf:
                dp[i][j] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
            return dp[i][j]

        return dfs(0, 0)


class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Bottom up DP solution with O(M) space complexity. The idea is that
        we start from the last row going upwards. For instance, given

           2
          3 4
         6 5 7
        4 1 8 3

        Our dp = [4, 1, 8, 3]
        Looking at row [6, 5, 7], we know the min sum involving 6, is
        6 + min(4, 1) = 7. And this 7 can replace the first position in dp
        because the first position will not be used again when computing the min
        sum of the second value in row [6, 5, 7]. Thus, as we go through
        [6, 5, 7], dp becomes:

        [7, 1, 8, 3] (handling 6)
        [7, 6, 8, 3] (handling 5)
        [7, 6, 10, 3] (handling 7)

        We use the same technique for the row [3, 4]:

        [9, 6, 10, 3] (handling 3)
        [9, 10, 10, 3] (handling 4)

        The first row [2]:
        [11, 10, 10, 3] (handking 2)

        The result is the first element of the DP array.

        O(N), 84 ms, 5% ranking.
        """
        dp = triangle[-1]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]


class Solution3:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """Leveraging lru_cache
        76 ms
        """
        @lru_cache(maxsize=None)
        def dfs(i: int, j: int) -> int:
            return 0 if i == len(triangle) else triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))

        return dfs(0, 0)



sol = Solution3()
tests = [
    ([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
]

for i, (triangle, ans) in enumerate(tests):
    res = sol.minimumTotal(triangle)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
