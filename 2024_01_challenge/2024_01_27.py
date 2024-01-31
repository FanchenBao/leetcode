# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
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


class Solution2:
    def kInversePairs(self, n: int, k: int) -> int:
        """
        This is the GOOD solution originally from the 2022 solution:
        https://leetcode.com/submissions/detail/749254069/

        The idea is that we have dp[i][j] = the total number of arrays with
        length i that can make j number of inverse pairs. We also require that
        we only use numbers 1 to i to form these arrays.

        Now we want to compute dp[i + 1][j], we can add a new number i + 1 to
        the array. i + 1 is the largest number. Thus, if we add i + 1 to the
        end, then we will have dp[i][j] number of inverse pairs in the new
        array length of i + 1

        If we shit i + 1 one position to the left, we will have an additional
        inverse pair. Thus, the number of arrays to make j inverse pairs is
        dp[i][j - 1]. If we shift i + 1 two positions to the left, we will have
        two additional inverse pairs. Thus, we need dp[i][j - 2] from the
        previous DP value to satisfy the current need.

        So on and so forth, we can write dp[i + 1][j] = dp[i][j] + dp[i][j - 1]
        + dp[i][j - 2] + ... + dp[i][max(j - i, 0)]

        Now, if we do this in 1D DP, we can call cur[j] for the length of i + 1
        and pre[j] for the length of i.

        Then cur[j] = pre[j] + pre[j - 1] + pre[j - 2] + ... + (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)
        Interestingly, cur[j - 1] = pre[j - 1] + pre[j - 2] + ... + (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)

        Hence cur[j] - cur[j - 1] = pre[j] - (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)
        => cur[j] = cur[j - 1] + pre[j] - (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)
        """
        pre = [0] * (1 + k)
        pre[0] = 1
        for i in range(2, n + 1):
            cur = [0] * (1 + k)
            cur[0] = 1
            for j in range(1, 1 + k):
                cur[j] = cur[j - 1] + pre[j] - (pre[j - 1 - (i - 1)] if j - 1 >= i - 1 else 0)
            pre = cur
        return pre[-1] % 1000000007


sol = Solution2()
tests = [
    (5, 3, 15),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.kInversePairs(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
