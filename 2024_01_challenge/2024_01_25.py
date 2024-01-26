# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """LeetCode 1143
        
        The good old LCS problem
        
        O(MN), 400 ms, faster than 96.69%
        """
        M, N = len(text1), len(text2)
        dp = [0] * (N + 1)
        for i in range(1, M + 1):
            tmp = [0] * (N + 1)
            for j in range(1, N + 1):
                if text1[i - 1] == text2[j - 1]:
                    tmp[j] = dp[j - 1] + 1
                else:
                    tmp[j] = max(dp[j], tmp[j - 1])
            dp = tmp
        return dp[-1]


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]
#
# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
