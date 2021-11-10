# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """LeetCode 122

        State machine. O(N), 68 ms, 42% ranking.
        """
        h, e = -math.inf, 0
        for p in prices:
            h, e = max(h, e - p), max(e, h + p)
        return e


sol = Solution()
tests = [
    ([7,1,5,3,6,4], 7),
    ([1,2,3,4,5], 4),
    ([7,6,4,3,1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
