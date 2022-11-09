# from pudb import set_trace; set_trace()
from typing import List
import math


class StockSpanner1:

    def __init__(self):
        self.prices = [math.inf]
        self.dp = [0]

    def next(self, price: int) -> int:
        """LeetCode 901

        DP solution. what I did was basically monotonic stack, but implemented
        with DP (not a good implementation, waste of space)

        O(N), 1170 ms, faster than 14.24%
        """
        i = len(self.prices) - 1
        res = 1
        while self.prices[i] <= price:
            res += self.dp[i]
            i -= self.dp[i]
        self.prices.append(price)
        self.dp.append(res)
        return res


class StockSpanner2:

    def __init__(self):
        self.stack = [(math.inf, 0)]

    def next(self, price: int) -> int:
        """This is the monotonic decreasing stack solution. We don't have to
        use the dp array.

        1138 ms, faster than 18.58%
        """
        cur_cnt = self.stack[-1][1] + 1
        while price >= self.stack[-1][0]:
            stack.pop()
        stack.append((price, cur_cnt))
        return stack[-1][1] - stack[-2][1]




# sol = Solution()
# tests = [
#     ([7,1,5,3,6,4], 7),
#     ([1,2,3,4,5], 4),
#     ([7,6,4,3,1], 0),
# ]

# for i, (prices, ans) in enumerate(tests):
#     res = sol.maxProfit(prices)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
