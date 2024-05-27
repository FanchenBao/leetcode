# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def checkRecord(self, n: int) -> int:
        """
        LeetCode 552

        Use DP, dp[i][j] = number of records ending at i with j number of consecutive Ls when no A is present.

        Then we can put one A at each position from the start to the end, and
        wherever it is present, the n positions get separated into two
        independent sections, where the total number of ways is the product
        of the number of ways within each section.

        O(3N). Must do bottom up DP. Otherwise, will hit memory limit exceeded

        1025 ms, faster than 70.14%
        """
        if n == 1:  # edge case
            return 3
        MOD = 10**9 + 7

        # dp[i][j] = number of records ending at i with j number of
        # consecutive Ls
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0][0] = 1
        dp[0][1] = 1
        for i in range(1, n):
            # use P
            dp[i][0] = sum(dp[i - 1]) % MOD
            # use L
            dp[i][1] = dp[i - 1][0]
            dp[i][2] = dp[i - 1][1]

        # no A exists
        res = sum(dp[n - 1]) % MOD

        # one A exists
        for k in range(n):
            if k == 0 or k == n - 1:
                res = (res + sum(dp[n - 2])) % MOD
            else:
                res = (res + sum(dp[k - 1]) * sum(dp[n - k - 2])) % MOD
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
