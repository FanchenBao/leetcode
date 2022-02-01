# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        """LeetCode 121

        State machine method.

        O(N), 1356 ms, 41% ranking
        """
        e, h = 0, -math.inf
        for p in prices:
            e, h = max(e, h + p), max(h, -p)
        return e if e > 0 else 0


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """Kadane's algo
        """
        max_p, pre_p = -math.inf, -math.inf
        for i in range(1, len(prices)):
            dif = prices[i] - prices[i - 1]
            pre_p = max(dif, dif + pre_p)
            max_p = max(max_p, pre_p)
        return max_p if max_p > 0 else 0


sol = Solution2()
tests = [
    ([7,1,5,3,6,4], 5),
    ([7,6,4,3,1], 0),
    ([1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
