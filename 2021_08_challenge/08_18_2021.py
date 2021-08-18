# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def numDecodings(self, s: str) -> int:
        """LeetCode 91

        DFS suffices. What we need to do is take one or take two. Take one
        means we take one digit, and then recurse on the remaining. Take two
        means we take two digits, and then recurse on the remaining. Note that
        if a zero is at the leading position, we immediately reuturn 0 because
        we cannot decode it. If the two digits form an integer larger than 26,
        we cannot decode it.

        Another trick is to memoize for DP purpose.

        O(N), 24 ms, 96% ranking.

        UPDATE: just realize that we don't need to do lo and hi, because we
        never change hi. In other words, this is a 1D array DP.
        """
        n = len(s)

        @lru_cache(None)
        def dfs(i: int) -> int:
            if i == n or s[i] == '0':
                return 0
            # take one, then find the remaining
            if i == n - 1:
                return 1
            res = dfs(i + 1)
            # take two, then find the remaining
            if int(s[i:i + 2]) <= 26:
                res += 1 if i == n - 2 else dfs(i + 2)
            return res

        return dfs(0)


class Solution2:
    def numDecodings(self, s: str) -> int:
        """Bottom up
        
        This one is slow because it is O(N^2).
        """
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for size in range(1, len(s) + 1):
            for i in range(len(s) - size + 1):
                j = i + size - 1
                if s[i] == '0':
                    continue
                if i == j:
                    dp[i][j] += 1
                else:
                    if dp[i][i]:  # take one
                        dp[i][j] += dp[i + 1][j]
                    if int(s[i:i + 2]) <= 26:  # take two
                        dp[i][j] += 1 if i + 1 == j else dp[i + 2][j]
        return dp[0][n - 1]


class Solution3:
    def numDecodings(self, s: str) -> int:
        """Better DP. The same method that we used back in Dec. 2020

        p is the number of decoding in s[:i]; pp is the number of decoding in
        s[:i - 1]. Thus to find the number of decoding in s[:i + 1], we first
        check take two situation, which is to take s[i - 1:i + 1]. Then we check
        take one situation, which is to take s[i].

        O(N) time and O(1) space
        """
        p, pp = 0, 0
        for i in range(len(s)):
            cur = ('10' <= s[i - 1:i + 1] <= '26') * (1 if i == 1 else pp)
            if s[i] != '0':
                cur += 1 if i == 0 else p
            p, pp = cur, p
        return p


sol = Solution3()
tests = [
    ('12', 2),
    ('226', 3),
    ('0', 0),
    ('06', 0),
]

for i, (s, ans) in enumerate(tests):
    res = sol.numDecodings(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
