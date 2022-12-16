# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """LeetCode 1143

        Still got it. Still remembered how LCS is done.

        O(MN), 316 ms, faster than 99.30%
        """
        dp = [0] * (len(text2) + 1)
        for i in range(len(text1)):
            tmp = [0] * (len(text2) + 1)
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    tmp[j + 1] = 1 + dp[j]
                else:
                    tmp[j + 1] = max(dp[j + 1], tmp[j])
            dp = tmp
        return dp[-1]


sol = Solution()
tests = [
    ("abcde", "ace" , 3),
    ("abc", "abc", 3),
    ("abc", "def", 0),
]

for i, (text1, text2, ans) in enumerate(tests):
    res = sol.longestCommonSubsequence(text1, text2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
