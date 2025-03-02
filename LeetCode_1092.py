# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        This solution follows the most optimal solution in the editorial.

        We use dp[i][j] to represent the shortest common supersequence (SCS)
        between str1[:i] and str2[:j]

        Then we backtrack the dp matrix to build out the answer.

        Note that we make the dp matrix of size (M + 1) * (N + 1)

        O(MN), 432 ms, 62.85%
        """
        M, N = len(str1), len(str2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        # prefill first row and col. The key insight here is that the SCS
        # between a string and an empty string is always the string itself
        for i in range(M + 1):
            dp[i][0] = i
        for j in range(N + 1):
            dp[0][j] = j
        # fill the rest
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # here is another piece of important insight.
                    # when the two letters mismatch, we must include one of
                    # them in the SCS. We compare dp[i - 1][j] and dp[i][j - 1]
                    # We pick the smaller, and then add the etra letter from
                    # either str1[i] (if dp[i - 1][j] is smaller) or str2[j]
                    # (if dp[i][j - 1] is smaller)
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        # backtrack to build the answer
        res = ""
        i, j = M, N
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res += str1[i - 1]
                i -= 1
                j -= 1
            elif dp[i - 1][j] <= dp[i][j - 1]:
                res += str1[i - 1]  # dp[i][j] is reached by adding str1[i - 1]
                i -= 1
            else:
                res += str2[j - 1]
                j -= 1
        # Fill the rest of the SCS
        while i > 0:
            res += str1[i - 1]
            i -= 1
        while j > 0:
            res += str2[j - 1]
            j -= 1
        return res[::-1]


for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
