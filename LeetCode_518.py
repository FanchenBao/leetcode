# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache


class Solution1:
    def change(self, amount: int, coins: List[int]) -> int:
        """Pretty naive DP solution. helper(idx, target) returns the total
        number of ways that coins[idx:] can make up for target amount of value.

        Note that it is possible to have a combination of coins where the number
        of coins used is zero.

        4301 ms, 5% ranking.
        """
        coins.sort()
        N = len(coins)

        @lru_cache(maxsize=None)
        def helper(idx: int, target: int) -> int:
            if target == 0:
                return 1
            if idx == N or coins[idx] > target:
                return 0
            res, i = 0, 0
            while target - coins[idx] * i >= 0:
                res += helper(idx + 1, target - coins[idx] * i)
                i += 1
            return res

        return helper(0, amount)


class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        """Bottom up. Same time complexity as solution1. No improvement.
        
        6366 ms.
        """
        N = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(N - 1, 0, -1):
            temp = [0] * (amount + 1)
            for tgt in range(amount, -1, -1):
                j = 0
                while tgt - coins[i] * j >= 0:
                    temp[tgt] += dp[tgt - coins[i] * j]
                    j += 1
            dp = temp
        res = j = 0
        while amount - coins[0] * j >= 0:
            res += dp[amount - coins[0] * j]
            j += 1
        return res


sol = Solution2()
tests = [
    (5, [1, 2, 5], 4),
    (3, [2], 0),
    (10, [10], 1),
    (0, [1, 2], 1),
]

for i, (amount, coins, ans) in enumerate(tests):
    res = sol.change(amount, coins)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
