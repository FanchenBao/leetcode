# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution0:
    def minCut(self, s: str) -> int:
        """TLE. This seems to be O(N^3) time complexity.

        It doesn't work because we are computing the minCut for any pair of i, j
        but in reality, we only need the minCut for pair i, n - 1. This reduces
        a lot of the computation. For instance, to compute i to n - 1, we can
        go through [i, i] and [i + 1, n - 1], [i, i + 1] and [i + 2, n - 1],
        [i, i + 2] and [i + 3, n - 1], ... The trick is when [i, i + k] is not
        a palindrome, we can simply skip it, because it can be broken down into
        some [i, i + k'] and [k' + k] where [i, i + k'] is a palindrome. This
        break down has been computed before, so we don't have to repeat. In
        other words, we only have to compute the situation where [i, i + k] is
        a palindrome itself.
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for k in range(2, n + 1):
            for i in range(n - k + 1):
                j = k + i - 1
                if s[i:j + 1] != s[i:j + 1][::-1]:
                    dp[i][j] = math.inf
                    for p in range(i, j):
                        dp[i][j] = min(dp[i][j], dp[i][p] + dp[p + 1][j] + 1)
        return dp[0][n - 1]


class Solution1:
    def minCut(self, s: str) -> int:
        """Inspired by

        https://leetcode.com/problems/palindrome-partitioning-ii/discuss/1388628/Python-Simple-Top-down-DP-Clean-and-Concise

        But with bottom up mind set. Again, let me reiterate the trick: we only
        consider the span of [i, n - 1]. We want to find out the min number of
        cuts in [i, n - 1]. To do so, we iterate through [i, i] and [i + 1, n - 1],
        [i, i + 1] and [i + 2, n - 1], ..., [i, j] and [j + 1, n - 1]. If [i, j]
        is a palindrome, then we have a potential answer of 1 + dp[j + 1]. If
        [i, j] is not a palindrome, we don't have to consider it, because it
        can be always broken down into a smaller palindrome that we have already
        considered. Therefore, the problem is simplied into O(N^2). Note that
        we use another DP table called is_pal to check whether s[i:j] is
        palindrome in O(1) time.


        1008 ms, 53% ranking.
        """
        n = len(s)
        is_pal = [[0] * n for _ in range(n)]
        dp = [math.inf] * n  # dp[i] record number of cuts from i to n - 1
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                # determine whether s[i:j + 1] is a palindrome and cache it
                if i == j:
                    is_pal[i][j] = 1
                elif i + 1 == j:
                    is_pal[i][j] = 1 if s[i] == s[j] else 0
                else:
                    is_pal[i][j] = 1 if is_pal[i + 1][j - 1] and s[i] == s[j] else 0
                # if s[i:j + 1] is a palindrome, we compute the possible min
                # number of cuts. If it is not a palindrome, we can safely skip
                # it, because it can always be broken down into a smaller
                # palindrome that we have already processed.
                if is_pal[i][j]:
                    dp[i] = min(dp[i], (dp[j + 1] + 1) if j < n - 1 else 0)
        return dp[0]


sol = Solution1()
tests = [
    ('aab', 1),
    ('a', 0),
    ('ab', 1),
    ('adabdcaeb', 6),
    ('adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece', 273),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minCut(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
