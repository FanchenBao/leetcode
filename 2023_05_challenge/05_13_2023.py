# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """LeetCode 2466

        The first DP attempt was not correct. I was making dp(i) the number of
        ways to create string starting from position i. However, that will not
        help with the size of the string.

        The second attempt changes the DP, such that dp[i] is the number of ways
        to create string of size i. This way, the DP relation is very clear:

        dp[i] = dp[i - zero] + dp[i - one] (provided that i - zero and i - one
        are non-negative)

        O(N), 310 ms, faster than 58.27%
        """
        MOD = 10**9 + 7
        # dp[i] is the number of ways to make a string of length i
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] * int(i - zero >= 0) + dp[i - one] * int(i - one >= 0)) % MOD

        return sum(dp[low:high + 1]) % MOD


sol = Solution()
tests = [
    (3, 3, 1, 1, 8),
    (2, 3, 1, 2, 5),
]

for i, (low, high, zero, one, ans) in enumerate(tests):
    res = sol.countGoodStrings(low, high, zero, one)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
