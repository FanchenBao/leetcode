# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """LeetCode 714

        Typical state machine solution. The only difference from all the
        other stock transaction problem is that we need to include fee when we
        perform sell.

        O(N), 692 ms, 77% ranking.

        Read this: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108870/Most-consistent-ways-of-dealing-with-the-series-of-stock-problems
        """
        E, H = 0, -math.inf
        for p in prices:
            E = max(E, H + p - fee)
            H = max(H, E - p)
        return E


sol = Solution()
tests = [
    ([1, 3, 2, 8, 4, 9], 2, 8),
    ([1, 3, 7, 5, 10, 3], 3, 6),
]

for i, (prices, fee, ans) in enumerate(tests):
    res = sol.maxProfit(prices, fee)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
