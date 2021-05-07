# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        """LeetCode 583

        This is essentially finding the max length of Longest Common Subsequence
        between word1 and word2. Once the max length is found, the
        answer is the sum of the difference between the length of each word and
        the max length.

        The tricky part is to find the max length, which itself is a
        classic DP problem that I have learned in class and done in LeetCode for
        many times. So it would've been una vergüenza verdadera if I couldn't
        write the solution in the first try. But fortunately, I didn't
        disappoint myself today.

        O(NM), 264 ms, 90% ranking.
        """
        N, M = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return N + M - 2 * dp[-1][-1]


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        """From the official solution. Directly using DP to solve the problem.
        """
        N, M = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(M + 1):
            for j in range(N + 1):
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[j - 1] == word2[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        """1D DP, using the LCS method. It's quite tricky to wrap my head around
        but this comment helped a lot:

        https://leetcode.com/problems/delete-operation-for-two-strings/solution/225830

        The basic idea is to save the [i - 1][j - 1] before making change to
        the current do[j], because the current dp[j] is going to be
        [i - 1][j - 1] for dp[j + 1]. So we take it out first to prevent its
        value being modified. Then we do the normal DP stuff. Take a while to
        go through the code it you get stuck.
        """
        N, M = len(word1), len(word2)
        dp = [0] * (N + 1)
        for i in range(1, M + 1):
            i_minus_j_minus = dp[0]
            for j in range(1, N + 1):
                cur = dp[j]
                if word1[j - 1] == word2[i - 1]:
                    dp[j] = i_minus_j_minus + 1
                else:
                    dp[j] = max(dp[j], dp[j - 1])
                i_minus_j_minus = cur
        return N + M - 2 * dp[-1]


sol = Solution3()
tests = [
    ('sea', 'eat', 2),
    ('leetcode', 'etco', 4),
]

for i, (word1, word2, ans) in enumerate(tests):
    res = sol.minDistance(word1, word2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
