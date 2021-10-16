# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        h1, e1, h2, e2 = -math.inf, 0, -math.inf, 0
        for p in prices:
            h1, e1, h2, e2 = max(h1, -p), max(e1, h1 + p), max(h2, e1 - p), max(e2, h2 + p)
        return e2


sol = Solution()
tests = [
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
