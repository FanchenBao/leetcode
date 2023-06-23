# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """LeetCode 714

        The problem shall be more clear that the transaction fee is only paid
        when you sell the stock.

        O(N), 686 ms, faster than 83.41% 
        """
        h, e = -math.inf, 0
        for p in prices:
            h, e = max(h, e - p), max(e, h + p - fee)
        return e


sol = Solution()
tests = [
    ([1,3,2,8,4,9], 2, 8),
    ([1,3,7,5,10,3], 3, 6),
]

for i, (prices, fee, ans) in enumerate(tests):
    res = sol.maxProfit(prices, fee)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
