# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math


class Solution1:
    """Use state machine.
    
    45% ranking on speed. Very verbose. I am sure the standard answer will be
    like only 5 lines.

    Time complexity is less than O(n^2) but higher than O(n)
    """
    def get_state_maxes(self, prices: List[int]) -> Tuple[List[int], List[int]]:
        length = len(prices)
        p_hold = [0] * length
        p_empty = [0] * length
        p_hold[0] = -prices[0]
        for i, p in enumerate(prices[1:], 1):
            p_hold[i] = max(p_hold[i - 1], p_empty[i - 1] - p)
            p_empty[i] = max(p_empty[i - 1], p_hold[i - 1] + p)
        return p_hold, p_empty

    def get_best_buy_sell(self, prices: List[int], p_hold: List[int], p_empty: List[int]) -> Tuple[List[int], List[int]]:
        # find best buy and sell prices for best atomic profits
        buys = []
        sells = []
        j = len(prices) - 1
        while j >= 0:
            cur_profit = p_empty[j]
            sell_price = prices[j]
            k = j
            while k >= 0 and p_hold[k] == cur_profit - sell_price:
                k -= 1
            buy_price = prices[k + 1]
            # some times buy_price and sell_price is the same. This is
            # considered a valid state transaction, but doesn't make sense in
            # reality.
            if buy_price != sell_price:
                buys.append(buy_price)
                sells.append(sell_price)
            j = k
        return buys[::-1], sells[::-1]

    def get_max_single_transaction(self, buys, sells) -> List[int]:
        max_cache = [0] * (len(buys) + 1)
        for i in range(len(buys)):
            for j in range(i, len(sells)):
                max_cache[i] = max(max_cache[i], sells[j] - buys[i])
        for i in range(len(max_cache) - 2, -1, -1):
            max_cache[i] = max(max_cache[i], max_cache[i + 1])
        return max_cache

    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        p_hold, p_empty = self.get_state_maxes(prices)
        buys, sells = self.get_best_buy_sell(prices, p_hold, p_empty)
        # brute force the best two transaction deals
        max_single_trans = self.get_max_single_transaction(buys, sells)
        max_prof = 0
        for i, buy in enumerate(buys):
            for j in range(i, len(sells)):
                max_prof = max(max_prof, sells[j] - buy + max_single_trans[j + 1])
        # print(p_hold)
        # print(p_empty)
        # print(buys)
        # print(sells)
        # print(max_single_trans)
        return max_prof


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        """Classic DP solution. However, it will timeout"""
        length = len(prices)
        profits = [[0] * (length + 1) for _ in range(3)]
        for k in range(1, 3):  # max transaction is 2
            for i in range(1, length + 1):  # check profit for each day at each transaction
                for j in range(1, i + 1):
                    max_curr_prof = max(profits[k][i - 1], prices[i - 1] - prices[j - 1] + profits[k - 1][j - 1])
                    profits[k][i] = max(profits[k][i], max_curr_prof)
        # print(profits)
        return profits[2][length]


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        """Optimized DP solution."""
        length = len(prices)
        profits = [[0] * (length + 1) for _ in range(3)]
        for k in range(1, 3):  # max transaction is 2
            min_val = math.inf
            for i in range(1, length + 1):  # check profit for each day at each transaction
                min_val = min(min_val, prices[i - 1] - profits[k - 1][i - 1])
                profits[k][i] = max(profits[k][i - 1], prices[i - 1] - min_val)
        # print(profits)
        return profits[2][length]


class Solution4:
    def maxProfit(self, prices: List[int]) -> int:
        """Most brilliant solution"""
        b1, p1, b2, p2 = math.inf, 0, math.inf, 0
        for i in range(len(prices)):
            b1 = min(b1, prices[i])  # first buy price
            p1 = max(p1, prices[i] - b1)  # profit after first sell
            b2 = min(b2, prices[i] - p1)  # second buy price, taking into consideration the current profit
            p2 = max(p2, prices[i] - b2)  # profit after second sell
        return p2


class Solution5:
    def maxProfit(self, prices: List[int]) -> int:
        """Good state machine solution"""
        h1, e1, h2, e2 = -math.inf, 0, -math.inf, 0
        for i in range(len(prices)):
            h1 = max(h1, -prices[i])
            e1 = max(e1, h1 + prices[i])
            h2 = max(h2, e1 - prices[i])
            e2 = max(e2, h2 + prices[i])
        return e2

tests = [
    ([3, 3, 5, 0, 0, 3, 1, 4], 6),
    ([1, 2, 3, 4, 5], 4),
    ([7, 6, 4, 3, 1], 0),
    ([1, 2, 4, 2, 5, 7, 2, 4, 9, 0], 13),
    ([3, 2, 6, 5, 0, 3], 7),
    ([0, 8, 5, 7, 4, 7], 11),
]

sol = Solution5()

for i, (test, ans) in enumerate(tests):
    res = sol.maxProfit(test)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}: FAIL. Expected: {ans}, Received: {res}')