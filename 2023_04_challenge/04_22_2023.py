# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minInsertions(self, s: str) -> int:
        """LeetCode 1312

        DP. dp[i][j] is the minimum steps to make s[i:j + 1] a palindrome. The
        condition to find dp[i][j] is the min of dp[i + 1][j] + 1, dp[i][j - 1]
        + 1, and if s[i] == s[j], dp[i + 1][j - 1].

        This insight is obtained after playing around with some test cases.

        O(N^2), 843 ms, faster than 66.13% 
        """
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for l in range(2, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                dp[i][j] = min(
                    dp[i + 1][j] + 1,
                    dp[i][j - 1] + 1,
                    dp[i + 1][j - 1] if s[i] == s[j] else math.inf,
                )
        return dp[0][-1]


sol = Solution()
tests = [
    ('zzazz', 0),
    ('mbadm', 2),
    ('leetcode', 5),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minInsertions(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
