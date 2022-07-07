# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """LeetCode 97

        I almost gave up on this one. Got a hint from the solution that I shall
        use DP. What is the target of DP. Turns out we can make dp[i][j] be a
        boolean value, indicating whether interleaving s1[:i] and s2[:j] can
        form s3[:i + j], where i and j are the lengths of s1 and s2. To find
        dp[i][j], we check dp[i][j - 1] and dp[i - 1][j]. If dp[i][j - 1] is
        True, then we want to compare s2[j] with s3[i + j - 1]. Since
        dp[i][j - 1] is True, as long as s2[j] == s3[i + j - 1], we can always
        append s2[j] and still make the interleaving work. However, if
        dp[i][j - 1] is False or s2[j] != s3[i + j - 1], then interleaving
        won't work this way, we have to check dp[i - 1][j].

        At the end, we have to also go both ways, making i, j => s1, s2, and
        i, j => s2, s1

        O(MN) time, with O(N) space. 69 ms, faster than 44.76%
        """
        if len(s3) != len(s1) + len(s2):
            return False

        def dp(s1: str, s2: str) -> bool:
            dp = [False] * (len(s2) + 1)
            dp[0] = True
            dp[len(s2)] = s2 == s3
            for i in range(1, len(s1) + 1):
                dp[0] = s1[:i] == s3[:i]
                for j in range(1, len(s2) + 1):
                    dp[j] = (dp[j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[j] and s1[i - 1] == s3[i + j - 1])
            return dp[-1]

        return dp(s1, s2) or dp(s2, s1)


class Solution2:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """This is my solution from a year ago. Much smarter back then than the
        solution I have today.
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        @lru_cache
        def helper(i1: int, i2: int, i3: int) -> bool:
            if [i1, i2, i3] == [n1, n2, n3]:  # anchor case
                return True
            if i1 < n1 and s1[i1] == s3[i3] and helper(i1 + 1, i2, i3 + 1):
                return True
            if i2 < n2 and s2[i2] == s3[i3] and helper(i1, i2 + 1, i3 + 1):
                return True
            return False

        return helper(0, 0, 0)



sol = Solution2()
tests = [
    ("aabcc", "dbbca", "aadbbcbcac", True),
    ("aabcc", "dbbca", "aadbbbaccc", False),
    ("", "", "", True),
    ("aaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", False),
    ("aa", "ab", "abaa", True),
]

for i, (s1, s2, s3, ans) in enumerate(tests):
    res = sol.isInterleave(s1, s2, s3)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
