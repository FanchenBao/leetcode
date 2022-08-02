# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def uniquePaths(self, m: int, n: int) -> int:
        """LeetCode 62
        1D DP
        O(MN), 49 ms, faster than 52.07% 
        """
        dp = [1] * n
        for _ in range(m - 1):
            for i in range(1, n):
                dp[i] += dp[i - 1]
        return dp[-1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        """Pascal triangle solution
        (m + n - 2) C (n - 1)

        26 ms, faster than 98.87%
        """
        return math.factorial(m + n - 2) // (math.factorial(n - 1) * math.factorial(m - 1))


sol = Solution2()
tests = [
    (3, 7, 28),
    (3, 2, 3),
]

for i, (m, n, ans) in enumerate(tests):
    res = sol.uniquePaths(m, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
