# from pudb import set_trace; set_trace()
from typing import List
from collections import deque
from functools import lru_cache


class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """LeetCode 97

        This is a pretty naive DP solution. The logic is that for each letter
        in s3, we can try to match it to s1 or s2. If it matches to any one of
        them, we move on to match the remaining. If it matches to both of them,
        then we bifurcate. With this logic, each recursion call has a state
        represented by the current indices on s1, s2, and s3. Therefore, we can
        build a cache on top of it to save repeated computation.

        O(MNK), where M, N, K are the lengths of s1, s2, and s3.
        44 ms, 35% ranking.

        NOTE: according to the solution, the runtime is O(MN), K does not play
        a part.
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)

        @lru_cache(maxsize=None)
        def helper(i1: int, i2: int, i3: int) -> bool:
            if [i1, i2, i3] == [n1, n2, n3]:
                return True
            if i3 == n3 and (i1 < n1 or i2 < n2):
                return False
            if i1 < n1 and s3[i3] == s1[i1]:
                if helper(i1 + 1, i2, i3 + 1):
                    return True
            if i2 < n2 and s3[i3] == s2[i2]:
                if helper(i1, i2 + 1, i3 + 1):
                    return True
            return False

        return helper(0, 0, 0)


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """My attempt at bottom up, but very poorly done. Took me an hour and
        half just to come up with this, which itself is very slow.
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        dp = [[[False] * (n1 + 1) for _ in range(n2 + 1)] for _ in range(n3 + 1)]
        dp[n3][n2][n1] = True
        for i3 in range(n3 - 1, -1, -1):
            for m in range(1, min(n1 + 1, n3 - i3 + 1)):
                i1 = n1 - m
                i2 = n2 - (n3 - i3 - m)
                if 0 <= i1 < n1 and 0 <= i2 <= n2 and s1[i1] == s3[i3] and not dp[i3][i2][i1]:
                    dp[i3][i2][i1] = dp[i3 + 1][i2][i1 + 1]
            for n in range(1, min(n2 + 1, n3 - i3 + 1)):
                i2 = n2 - n
                i1 = n1 - (n3 - i3 - n)
                if 0 <= i1 <= n1 and 0 <= i2 < n2 and s2[i2] == s3[i3] and not dp[i3][i2][i1]:
                    dp[i3][i2][i1] = dp[i3 + 1][i2 + 1][i1]
        return dp[0][0][0]


class Solution3:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Same recursion but with different implementation"""
        n1, n2, n3 = len(s1), len(s2), len(s3)

        @lru_cache(maxsize=None)
        def helper(i1: int, i2: int, i3: int) -> bool:
            if i1 == n1:
                return s2[i2:] == s3[i3:]
            if i2 == n2:
                return s1[i1:] == s3[i3:]
            if i3 == n3:
                return i1 == n1 and i2 == n2
            if (s1[i1] == s3[i3] and helper(i1 + 1, i2, i3 + 1)) or (s2[i2] == s3[i3] and helper(i1, i2 + 1, i3 + 1)):
                return True
            return False

        return helper(0, 0, 0)


class Solution4:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """The correct way to do bottom up DP"""
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = True
        for j in range(1, n2 + 1):
            dp[0][j] = s2[j - 1] == s3[j - 1] and dp[0][j - 1]
        for i in range(1, n1 + 1):
            dp[i][0] = s1[i - 1] == s3[i - 1] and dp[i - 1][0]
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])
        return dp[n1][n2]


class Solution5:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """Same DP but using 1D table"""
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [False] * (n2 + 1)
        dp[0] = True
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                dp[j] = (i == j == 0) or (i >= 1 and s3[i + j - 1] == s1[i - 1] and dp[j]) or (j >= 1 and s3[i + j - 1] == s2[j - 1] and dp[j - 1])
        return dp[-1]


sol = Solution5()
tests = [
    ('aabcc', 'dbbca', 'aadbbcbcac', True),
    ('aabcc', 'dbbca', 'aadbbbaccc', False),
    ('', '', '', True),
    ('', '', 'a', False),
    ('aabc', 'abad', 'aabcabad', True),
]

for i, (s1, s2, s3, ans) in enumerate(tests):
    res = sol.isInterleave(s1, s2, s3)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
