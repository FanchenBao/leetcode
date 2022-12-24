# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """LeetCode 309

        I knew the gimmick, but I screwed up on the state machine.

        Holding -> Cool down -> Empty -> Holding

        That is the correct order. Initially, I put cool down after empty, and
        it was never correct.

        O(N), 85 ms, faster than 49.10%
        """
        h, e, c = -math.inf, 0, 0
        for p in prices:
            h, e, c = max(h, e - p), max(e, c), h + p
        return max(c, e)


sol = Solution()
tests = [
    ([1,2,3,0,2], 3),
    ([1], 0),
]

for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
