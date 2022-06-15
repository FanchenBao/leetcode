# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """LeetCode 583

        This is the same logic as LCS.

        O(MN), 450 ms, faster than 34.74%

        UPDATE: use only one array
        """
        M, N = len(word1), len(word2)
        dp = list(range(N + 1))
        for i in range(1, M + 1):
            dp[0] = i
            i_1_j_1 = i - 1
            for j in range(1, N + 1):
                cur = dp[j]  # essentially DP[i - 1][j]
                if word1[i - 1] == word2[j - 1]:
                    dp[j] = i_1_j_1
                else:
                    dp[j] = min(dp[j], dp[j - 1]) + 1
                i_1_j_1 = cur
        return dp[-1]


sol = Solution()
tests = [
    ("sea", "eat", 2),
    ("leetcode", "etco", 4),
    ("a", "b", 2),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.minDistance(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
