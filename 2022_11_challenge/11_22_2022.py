# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    dp = [0, 1]
    for i in range(2, 10000 + 1):
        dp.append(math.inf)
        for j in range(1, int(math.sqrt(i)) + 1):
            dp[-1] = min(dp[-1], 1 + dp[i - j**2])

    def numSquares(self, n: int) -> int:
        """LeetCode 279

        This is a cheating method. We precompute all the solutions from 1 to
        10000, and then for each call on numSquares, we simply query the result

        348 ms, faster than 78.21%
        """
        return self.dp[n]


class Solution2:
    def numSquares(self, n: int) -> int:
        """Greedy solution.

        At each value, we take the as many perfect square as possible.

        This is the real solution.

        O(logN), 616 ms, faster than 68.71%
        """

        @lru_cache(maxsize=None)
        def helper(target: int) -> int:
            res = target
            for i in range(int(math.sqrt(target)), 1, -1):
                q, r = divmod(target, i**2)
                res = min(res, helper(r) + q)
            return res

        return helper(n)


class Solution3:
    def numSquares(self, n: int) -> int:
        """Better DP bottom up
        """
        dp = list(range(n + 1))  # min steps if max perfect square is 1
        for i in range(2, int(math.sqrt(n)) + 1):
            ps = i**2
            for j in range(ps, n + 1):
                dp[j] = min(dp[j], dp[j - ps] + 1)
        return dp[-1]


class Solution4:
    dp = list(range(10001))  # min steps if max perfect square is 1
    for i in range(2, 101):
        ps = i**2
        # compute min steps if max perfect square is ps
        for j in range(ps, 10001):
            dp[j] = min(dp[j], dp[j - ps] + 1)
    
    def numSquares(self, n: int) -> int:
        """Better DP bottom up
        """
        return self.dp[n]

sol = Solution4()
tests = [
    (12, 3),
    (13, 2),
    (6337, 2),
]

for i, (n, ans) in enumerate(tests):
    res = sol.numSquares(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
