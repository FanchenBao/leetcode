#! /usr/bin/env python3
"""07/17/2019

Original Solution was vanila recursion, straightforward with no optimization.
It was not surprising that it timed out.

Solution2 was DP with memoization. It passed OJ, clocking in at 40 ms (61%)

Solution3 was bottom up DP, clocking in at 36 ms (85%)
"""
from typing import Dict


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        c1 = self.numDecodings(s[1:]) if int(s[0]) != 0 else 0
        c2 = (
            self.numDecodings(s[2:])
            if len(s) >= 2 and 10 <= int(s[:2]) <= 26
            else 0
        )
        return c1 + c2


class Solution2:
    def numDecodings(self, s: str) -> int:
        memo = {"": 1}
        return self.helper(s, memo)

    def helper(self, s: str, memo: Dict[str, int]) -> int:
        if s not in memo:
            c1 = self.helper(s[1:], memo) if int(s[0]) != 0 else 0
            c2 = (
                self.helper(s[2:], memo)
                if len(s) >= 2 and 10 <= int(s[:2]) <= 26
                else 0
            )
            memo[s] = c1 + c2
        return memo[s]


class Solution3:
    """ Bottom up DP """

    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i, le in enumerate(s, start=1):
            c1 = dp[i - 1] if le != "0" else 0
            c2 = dp[i - 2] if i > 1 and "10" <= s[i - 2 : i] <= "26" else 0
            dp[i] = c1 + c2
        return dp[len(s)]


sol2 = Solution2()
sol3 = Solution3()
s = "9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253"
# s = '101'
print(sol2.numDecodings(s))
print(sol3.numDecodings(s))
