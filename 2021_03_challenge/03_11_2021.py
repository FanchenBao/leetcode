# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import math


class Solution1:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """This one takes a LONG time. I was stuck initially with a greedy
        solution. But soon, I realize that greedy is not going to work. Then I
        started with a DP solution, but I got the DP part wrong and ended up
        with TLE. The wrong part is that in order to find how a number can be
        broken down into the sum of two numbers, I simply iterate through all
        options. This is not necessary, because we know that one of the option
        must be one of the coins. So we easily loop through the coins, which has
        a set length. Thus, we can reduce the run time from O(N^2) to O(N)

        O(N), 1548 ms, 34% ranking.
        """
        dp = [0] * (amount + 1)
        for c in coins:
            if c <= amount:
                dp[c] = 1
        for a in range(1, amount + 1):
            if not dp[a]:
                dp[a] = math.inf
                for c in coins:
                    if c < a and dp[a - c] >= 0:
                        dp[a] = min(dp[a], 1 + dp[a - c])
                if dp[a] == math.inf:
                    dp[a] = -1
        return dp[amount]


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """Micro-optimization. Doesn't really improve the performance much. That
        said, it does make the code shorter.

        Update: after further modification based on my previous solution a year
        and half ago, I am able to reduce the runtime to 1284 ms, 61% ranking.
        """
        coins.sort()
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        for a in range(1, amount + 1):
            for c in coins:
                if c <= a:
                    dp[a] = min(dp[a], 1 + dp[a - c])
                elif c > a:
                    break
        return dp[amount] if dp[amount] != math.inf else -1


sol = Solution2()
tests = [
    ([1, 2, 5], 11, 3),
    ([3, 8], 9, 3),
    ([2], 3, -1),
    ([1], 0, 0),
    ([1], 1, 1),
    ([1], 2, 2),
    ([419, 408, 186, 83], 6249, 20),
    ([431, 62, 88, 428], 9084, 26),
]

for i, (coins, amount, ans) in enumerate(tests):
    res = sol.coinChange(coins, amount)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
