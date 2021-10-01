# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """LeetCode 1143

        This is one of the most classical DP problems. It's good to practice
        it from time to time. The trick is compare any pair of letters i, j in
        text1 and text2. If text1[i] == text2[j], then the length of LCS ending
        at i and j must be 1 + the length of LCS ending at i - 1 and j - 1.

        If text1[i] != text2[j], then the length of LCS ending at i and j must
        be the longer between the length of LCS ending at i - 1 and j or i and
        j - 1.

        We continue until exhausting both strings. The DP can be built as a 2D
        array, but the space complexity can be reduced by using only a 1D array.

        O(MN), where M is the length of text1 and N the length of Text2.

        332 ms, 96% ranking.
        """
        m, n = len(text1), len(text2)
        dp = [0] * (n + 1)
        for i in range(1, m + 1):
            temp = [0] * (n + 1)
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    temp[j] = dp[j - 1] + 1
                else:
                    temp[j] = max(dp[j], temp[j - 1])
            dp = temp
        return dp[-1]


sol = Solution()
tests = [
    ('abcde', 'ace', 3),
    ('abc', 'abc', 3),
    ('abc', 'def', 0),
]

for i, (text1, text2, ans) in enumerate(tests):
    res = sol.longestCommonSubsequence(text1, text2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
