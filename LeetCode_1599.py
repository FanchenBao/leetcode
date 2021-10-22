# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        """This is a weird problem. There is no optimization, because we are
        forced to keep rotating the wheel, because otherwise, new customers will
        not arrive. So everything is deterministic. All we are doing is keeping
        track of the profit at each rotation, and record the earliest rotation
        that leads to maximum profit.

        O(N / 4), N is the sum of all customers. 2436 ms, 58% ranking.
        """
        max_prof, res = -math.inf, 0
        rot, rem, ttgo = 0, 0, 0
        N = len(customers)
        while rem or rot < N:
            if rot < N:
                rem += customers[rot]
            go = min(4, rem)
            rem -= go
            ttgo += go
            rot += 1
            new_prof = ttgo * boardingCost - rot * runningCost
            if new_prof > max_prof:
                max_prof = new_prof
                res = rot
        return res if max_prof > 0 else -1


sol = Solution()
tests = [
    ([8, 3], 5, 6, 3),
    ([10, 9, 6], 6, 4, 7),
    ([3, 4, 0, 5, 1], 1, 92, -1),
    ([10, 10, 6, 4, 7], 3, 8, 9),
]

for i, (customers, boardingCost, runningCost, ans) in enumerate(tests):
    res = sol.minOperationsMaxProfit(customers, boardingCost, runningCost)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
