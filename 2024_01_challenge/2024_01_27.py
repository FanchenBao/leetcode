# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    """
    LeetCode 629

    Use DP to solve this problem and prefix sum to speed it up. The DP rule
    is that DP[i][j] is the number of ways to create j or fewer inverse pairs
    given an array of length i.

    The important insight is that the actual values in the array does not
    matter, because each number is unique and there is always a deterministic
    order given an array of any size.

    O(NK), 451 ms, faster than 21.02%
    """
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 1000000007
        # dp[i][j] = the number of ways to create j or fewer inverse pairs
        # given a length of i
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        for j in range(k + 1):
            dp[1][j] = 1
        for i in range(1, n + 1):
            dp[i][0] = 1
        for i in range(2, n + 1):
            for j in range(1, k + 1):
                # use prefix sum to speed up the computation
                allowed = min(i, j + 1)
                cur = (dp[i - 1][j] - (dp[i - 1][j - allowed] if j - allowed >= 0 else 0) + MOD) % MOD
                dp[i][j] = (dp[i][j - 1] + cur) % MOD
        return (dp[-1][-1] - (dp[-1][-2] if k > 0 else 0) + MOD) % MOD


sol = Solution()
tests = [
    (5, 3, 15),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.kInversePairs(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
