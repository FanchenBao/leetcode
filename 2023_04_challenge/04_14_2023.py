# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def longestPalindromeSubseq(self, s: str) -> int:
        """LeetCode 516
        
        Use 2D DP where dp[i][j] is the longest palindromic subsequence from
        s[i] to s[j], inclusive.

        Then we go through s using sliding window with incrementingly increasing
        window size. In DP, we essentially traverse it diagonally.

        For some i and j, if s[i] != s[j], dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        Otherwise, we have to also consider matching s[i][j] and thus use
        dp[i + 1][j - 1] + 2.

        O(N^2), 3503 ms, faster than 8.95%
        """
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 1
        for l in range(2, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                if i + 1 == j:
                    dp[i][j] = 2 if s[i] == s[j] else 1
                else:
                    dp[i][j] = max(
                        int(s[i] == s[j]) * (dp[i + 1][j - 1] + 2),
                        dp[i + 1][j],
                        dp[i][j - 1],
                    )
        return dp[0][N - 1]


class Solution2:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Top down DP. Notice that when s[i] == s[j], we can directly return
        dp(i + 1, j - 1) + 2, because dp(i + 1, j) and dp(i, j - 1) will not be
        any better.

        O(N^2), 950 ms, faster than 94.73%
        """

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i > j:
                return 0
            if i == j:
                return 1
            if s[i] == s[j]:
                return dp(i + 1, j - 1) + 2
            return max(dp(i, j - 1), dp(i + 1, j))

        return dp(0, len(s) - 1)


class Solution3:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Bottom up again, hoping to reduce run time by following the logic of
        top down.

        A little bit faster: 2252 ms, faster than 36.05%
        """
        N = len(s)
        dp = [[1] * N for _ in range(N)]
        for l in range(2, N + 1):
            for i in range(N - l + 1):
                j = i + l - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] * int(i + 1 <= j - 1)
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][N - 1]


class Solution4:
    def longestPalindromeSubseq(self, s: str) -> int:
        """Bottom up from the official solution.

        To make bottom up faster, we must avoid if statement as much as possible.
        By initializing dp matrix with 0, we can avoid checking i + 1 <= j - 1,
        because once i + 1 > j - 1, the dp value is 0.

        Also, if we go from bottom right to top left as the starting position of
        j for each row, we can initialize dp[i][i] = 1 directly at the beginning
        of each row.

        O(N^2), 1349 ms, faster than 69.41% 
        """
        N = len(s)
        dp = [[0] * N for _ in range(N)]
        for i in range(N - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, N):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        return dp[0][N - 1]


sol = Solution4()
tests = [
    ("bbbab", 4),
    ('cbbd', 2),
]

for i, (s, ans) in enumerate(tests):
    res = sol.longestPalindromeSubseq(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
