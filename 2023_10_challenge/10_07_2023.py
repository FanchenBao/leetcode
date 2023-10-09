# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """LeetCode 1420 (Fail)

        Initially try to math it, but didn't work. So pretty clear it is DP. Yet
        I was not able to find the correct state for DP.

        The official solution defines the dp as
        dp(index, previous max used, remaining max to use)

        Then for transition, we think like this: what is the options for the
        current idx. It can either be any value no bigger than the previous max
        OR it can be one of the new max.

        That is it. O(M^2 NK), 730 ms, faster than 70.48%
        """
        MOD = 10**9 + 7
        
        @lru_cache(maxsize=None)
        def dp(i: int, p: int, r: int) -> int:
            if i == n:
                return 0 if r else 1
            if r < 0:
                return 0
            # option 1, the current value is no bigger than previous max
            res = (p * dp(i + 1, p, r)) % MOD
            # option 2, the current value is bigger than previous max
            for c in range(p + 1, m + 1):
                res = (res + dp(i + 1, c, r - 1)) % MOD
            return res

        return dp(0, 0, k)



class Solution2:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """New way of defining DP.

        This is the preparation for the ultimate prefix sum solution.

        O(M^2NK)
        """
        # dp[l][mx][c] is the number of ways to create an array of length l
        # with max value mx and cost c
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        # when n == k == 1, there is one way to make the array
        for i in range(1, m + 1):
            dp[1][i][1] = 1

        MOD = 10**9 + 7

        for l in range(1, n + 1):
            for mx in range(1, m + 1):
                for c in range(1, k + 1):
                    # the added value to make length l does not create mx
                    dp[l][mx][c] += (mx * dp[l - 1][mx][c]) % MOD
                    # the added value to make length l is mx
                    for pre in range(1, mx):
                        dp[l][mx][c] = (dp[l][mx][c] + dp[l - 1][pre][c - 1]) % MOD
        res = 0
        for i in range(1, m + 1):
            res = (res + dp[n][i][k]) % MOD
        return res



class Solution3:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        """Use prefix sum to make Solution2 O(MNK)
        """
        # dp[l][mx][c] is the sum of ways to create an array of length l
        # with cost c and max value 1, 2, 3, ..., mx
        # In other words, given l and c, dp[l][mx][c] is a prefix sum
        dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n + 1)]
        # when n == k == 1, there is one way to make the array
        # Notice that we are storing the prefix sum here
        for i in range(1, m + 1):
            dp[1][i][1] = i

        MOD = 10**9 + 7

        for l in range(1, n + 1):
            for mx in range(1, m + 1):
                for c in range(1, k + 1):
                    # the added value to make length l does not create mx
                    cur_res = (mx * (dp[l - 1][mx][c] - dp[l - 1][mx - 1][c])) % MOD
                    # the added value to make length l is mx. We need to sum up
                    # all the previous possible max values
                    cur_res = (cur_res + dp[l - 1][mx - 1][c - 1]) % MOD
                    if l == 1 and c == 1:
                        # Already considered during initiation
                        continue
                    dp[l][mx][c] = (dp[l][mx][c] + dp[l][mx - 1][c] + cur_res) % MOD
        return dp[n][m][k]


sol = Solution3()
tests = [
    (4, 2, 1, 9),
    (5, 4, 3, 160),
]

for i, (n, m, k, ans) in enumerate(tests):
    res = sol.numOfArrays(n, m, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
