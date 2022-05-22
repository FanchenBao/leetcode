# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """TLE"""
        N = len(coins)
        coins.sort()
        dp = [[math.inf] * N for _ in range(amount + 1)]
        for i in range(N):
            dp[0][i] = 0
        for i, c in enumerate(coins):
            for a in range(1, amount + 1):
                q, r = divmod(a, c)
                if i == 0:
                    if not r:
                        dp[a][i] = q
                else:
                    while q:
                        dp[a][i] = min(dp[a][i], q + min(dp[r][:i]))
                        q -= 1
                        r += c
        res = min(dp[amount])
        return -1 if res == math.inf else res


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """TLE"""
        N = len(coins)
        coins.sort(reverse=True)

        @lru_cache(maxsize=None)
        def helper(idx: int, rem: int) -> int:
            if not rem:
                return 0
            if idx == N:
                return math.inf
            q, r = divmod(rem, coins[idx])
            res = math.inf
            while q >= 0:
                res = min(res, q + helper(idx + 1, r))
                q -= 1
                r += coins[idx]
            return res

        res = helper(0, amount)
        return -1 if res == math.inf else res


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """LeetCode 322

        This is waht DP does to you. If you approach it incorrectly, it is
        very difficult for me to get out of the wrong mindset. We want to use
        a DP such that dp[i] is the min number of coins to make up i. Our goal
        is to find dp[amount]. For each dp[i], the last coin to make it to
        i can be any of the coins. Thus, we iterate through all coins and find
        the min dp[i - c]. That min plus 1 is the value of dp[i]

        1763 ms, faster than 61.24% 
        """
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        coins.sort()
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                else:
                    break
        return -1 if dp[amount] == math.inf else dp[amount]


sol = Solution3()
tests = [
    ([1,2,5], 11, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1,2147483647], 2, 2),
    ([346,29,395,188,155,109], 9401, 26),
]

for i, (coins, amount, ans) in enumerate(tests):
    res = sol.coinChange(coins, amount)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
