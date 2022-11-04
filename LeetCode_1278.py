# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        """We use two DPs for this. The first one is the overall DP, which
        answers the question of the min number of changes to turn s[idx:] into
        rem number of disjoint palindrome substrings.

        For each pair of (idx, rem), we can separate out one letter on the left
        as a substring, or two letters, or three letter, etc. Then throw the
        same problem to the remaining string. This DP can be done using
        lru_cache. The time complexity of this DP is O(NK)

        The second DP is to find the min number of changes to make s[i:j + 1]
        palindrome. This DP can be achieved using memoization. The time
        complexity of this DP is O(N^3)

        O(NK + N^3) = O(N^3), 260 ms, faster than 80.25%
        """
        N = len(s)
        # dp[i][j] is the min number of changes to make s[i:j + 1] palindrome
        dp = [[-1] * N for _ in range(N)]
        for i in range(N):
            dp[i][i] = 0

        def min_changes(i: int, j: int) -> int:
            """the min number of changes to make s[i:j + 1] palindrome
            """
            res = 0
            while i < j:
                res += int(s[i] != s[j])
                i += 1
                j -= 1
            return res

        @lru_cache(maxsize=None)
        def helper(idx: int, rem: int) -> int:
            """Find the min number of changes to turn s[idx:] into rem
            number of disjoint palindromic substrings
            """
            if rem == 1:
                if dp[idx][N - 1] < 0:
                    dp[idx][N - 1] = min_changes(idx, N - 1)
                return dp[idx][N - 1]
            res = math.inf
            for i in range(idx, N - rem + 1):
                t = helper(i + 1, rem - 1)
                if dp[idx][i] < 0:
                    dp[idx][i] = min_changes(idx, i)
                res = min(res, dp[idx][i] + t)
            return res

        return helper(0, k)



sol = Solution()
tests = [
    ("abc", 2, 1),
    ("aabbc", 3, 0),
    ("leetcode", 8, 0),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.palindromePartition(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
