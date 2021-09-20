# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
from bisect import bisect_right
from functools import lru_cache


class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        """LeetCode 115

        First, find the indices for all letters in s.

        Let's define dp[ti][si] as the number of subsequences that form t[ti:]
        from s[si:], where t[ti] == s[si]. Going from t[-1] to t[0], s[-1] to
        s[0], we have dp[ti - 1][si0] = dp[ti][sk0] + dp[ti][sk1] + ... + dp[ti][skm]
        where si < sk1 < sk2 < ... < skm and t[ti] == s[sk0] == s[sk1] == ... ==
        s[skm].

        We can speed up this DP relationship by not computing dp[ti][sk0] +
        dp[ti][sk1] + ... + dp[ti][skm] for each ti, instead, we can form a
        prefix sum in dp[ti], such that dp[ti - 1][si0] = dp[ti][sk0] +
        dp[ti - 1][si1]

        This reduces time complexity a lot. We also use binary search to find
        sk0 from si0.

        Time complexity is O(MNlogN) where M is the length of t and N the length
        of s. 669 ms, 6% ranking.

        UPDATE: by prechecking whether all letters in t exist in s, we shrink
        the runtime to 40 ms.
        """
        if len(s) < len(t) or set(t) - set(s):
            return 0
        pos = defaultdict(list)
        for i, le in enumerate(s):
            pos[le].append(i)

        dp = [0] * len(s)
        for j in range(len(pos[t[-1]]) - 1, -1, -1):  # Fill out the last row
            dp[pos[t[-1]][j]] = 1 + (dp[pos[t[-1]][j + 1]] if j < len(pos[t[-1]]) - 1 else 0)
        for i in range(len(t) - 2, -1, -1):  # Fill out the remaining rows
            temp = [0] * len(s)
            for j in range(len(pos[t[i]]) - 1, -1, -1):
                bi = bisect_right(pos[t[i + 1]], pos[t[i]][j])
                if bi < len(pos[t[i + 1]]):
                    temp[pos[t[i]][j]] = dp[pos[t[i + 1]][bi]] + (temp[pos[t[i]][j + 1]] if j < len(pos[t[i]]) - 1 else 0)
            dp = temp
        return 0 if not pos[t[0]] else dp[pos[t[0]][0]]


class Solution2:
    def numDistinct(self, s: str, t: str) -> int:
        """From DBabichev, super duper easy

        https://leetcode.com/problems/distinct-subsequences/discuss/1472589/Python-short-dp-solution-explained

        define dp(i, j) as the number of subsequences that form t[0:j + 1] from
        s[0:i + 1]. dp(i, j) = dp(i - 1, j) + (0 if s[i] != t[j] else dp(i - 1, j - 1))
        """
        if len(s) < len(t) or set(t) - set(s):
            return 0

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            if i == -1:
                return j == -1
            if j == -1:
                # There is always one way to form an empty string t from a non-
                # empty string s
                return 1
            return dp(i - 1, j) + (s[i] == t[j]) * dp(i - 1, j - 1)

        return dp(len(s) - 1, len(t) - 1)


sol = Solution2()
tests = [
    ('rabbbit', 'rabbit', 3),
    ('babgbag', 'bag', 5),
    ('rabbbit', 'raabit', 0),
    ('a', 'a', 1),
    ('a', 'b', 0),
    ('aacaacca', 'ca', 5),
    ('aacaacca', 'ba', 0),
]

for i, (s, t, ans) in enumerate(tests):
    res = sol.numDistinct(s, t)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
