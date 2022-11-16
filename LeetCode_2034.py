# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class StockPrice:

    def __init__(self):
        self.ts_heap = []  # max heap
        self.max_heap = []
        self.min_heap = []
        self.ts_price_pos = {}
        self.ts_price_neg = {}

    def update(self, timestamp: int, price: int) -> None:
        if timestamp not in self.ts_price_pos:
            self.ts_price_pos[timestamp] = [0]
            self.ts_price_neg[timestamp] = [0]
            heapq.heappush(self.ts_heap, -timestamp)
            heapq.heappush(self.ts_price_pos, self.ts_price_pos[timestamp])
            heapq.heappush(self.ts_price_neg, self.ts_price_neg[timestamp])
        self.ts_price_pos[timestamp][0] = price
        self.ts_price_neg[timestamp][0] = -price

    def current(self) -> int:
        return self.ts_price_pos[-self.ts_heap[0]]

    def maximum(self) -> int:
        heapq.heapify(self.max_heap)
        return -self.max_heap[0]

    def minimum(self) -> int:
        heapq.heapify(self.min_heap)
        return self.min_heap[0]


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
