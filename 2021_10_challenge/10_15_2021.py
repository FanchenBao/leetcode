# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """LeetCode 309

        I have done this type of problems many times before. State machine
        is the way to go. But we probably should revisit the concept again to
        refresh our memory.

        For this implementation, we have holding, empty, and cool down state.
        Holding state can be reached from holding state via no-op or emtpy state 
        via buy. Empty sate can be reached from empty state via no-op or cool
        down state via no-op. Cool down state can be reached only from holding
        state via sell.

        We go through each price and keep track of the max profit on each state
        for each day. The answer is the max profit between empty or cool down
        state at the end of the day.

        O(N), 50 ms, 39% ranking.
        """
        h, e, c = -math.inf, 0, 0
        for p in prices:
            nh = max(h, e - p)
            ne = max(e, c)
            nc = h + p
            h, e, c = nh, ne, nc
        return max(c, e)


sol = Solution()
tests = [
    ([1, 2, 3, 0, 2], 3),
    ([1], 0),
    ([1, 4, 2], 3),
]


for i, (prices, ans) in enumerate(tests):
    res = sol.maxProfit(prices)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
