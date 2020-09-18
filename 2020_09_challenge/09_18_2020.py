# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Thinking in terms of state machine"""
        bp, sp, res = -math.inf, 0, 0
        for p in prices:
            bp, sp = max(bp, -p), max(bp + p, sp)
            res = max(res, sp)
        return res



sol = Solution()
tests = [
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
