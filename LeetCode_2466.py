# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        """DP. And use MOD along the way.

        O(High), 275 ms, faster than 94.20%
        """
        min_ = min(zero, one)
        if high < min_:
            return 0
        MOD = 10**9 + 7
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(min_, high + 1):
            dp[i] = (dp[i] + int(i >= zero) * dp[i - zero] + int(i >= one) * dp[i - one]) % MOD
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
