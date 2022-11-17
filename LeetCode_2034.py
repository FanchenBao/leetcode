# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import Counter


class StockPrice1:

    def __init__(self):
        """Quite convoluted set up, but it works.

        It's trivial to keep track of the current timestamp. We just need to
        keep the largest timestamp and that's it. To know the current price
        associated with the current timestamp is also trivial. It can be
        achieved by a simple hashmap.

        The difficulty is with the max and min. It's obvious that the solution
        has something to do with heap. But, if we update the heap each time the
        update method is called, we will TLE. That means we need to do two things
        1. keep the heap as small as possible
        2. do NOT update the heap if update does not change the composition of
        the heap

        To keep the heap small, we want only unique prices to be in the heap.
        To achieve this, we use a set to keep track of the components of the
        heap and do not add duplicate price.

        To reduce the number of updates, we also use the heap set. If the new
        price is already in the heap set, it must be inside the heap as well.
        Thus, there is no need to include a duplicate.

        One last piece is to find a way to deal with the old price that has just
        been updated. Here, we use a counter. Each time the update method is
        called, we increment on the new price, and decrement on the old price
        (if there is any). This allows us to keep track the number of copies of
        the prices in the unique heaps.

        We pop the heap only when maximum and minimum methods are called. And
        we use the counter to decide whether the max or min on top of the heap
        still exists.

        O(logN) for update, O(NlogN) worst case for maximum and minimum

        2141 ms, faster than 26.55%
        """
        self.ts_price = {}
        self.price_counter = Counter()
        self.max_heap = []
        self.max_heap_set = set()
        self.min_heap = []
        self.min_heap_set = set()
        self.cur_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.cur_time = max(self.cur_time, timestamp)
        self.price_counter[price] += 1
        if timestamp in self.ts_price:
            self.price_counter[self.ts_price[timestamp]] -= 1
        self.ts_price[timestamp] = price
        
        if price not in self.max_heap_set:
            heapq.heappush(self.max_heap, -price)
            self.max_heap_set.add(price)
        if price not in self.min_heap_set:
            heapq.heappush(self.min_heap, price)
            self.min_heap_set.add(price)

    def current(self) -> int:
        return self.ts_price[self.cur_time]

    def maximum(self) -> int:
        while self.price_counter[-self.max_heap[0]] == 0:
            self.max_heap_set.remove(-heapq.heappop(self.max_heap))
        return -self.max_heap[0]

    def minimum(self) -> int:
        while self.price_counter[self.min_heap[0]] == 0:
            self.min_heap_set.remove(heapq.heappop(self.min_heap))
        return self.min_heap[0]


class StockPrice2:

    def __init__(self):
        """Inspired by https://leetcode.com/problems/stock-price-fluctuation/discuss/1513293/Python-Clean-2-Heaps-Commented-Code

        This is straightforward two heaps. But it differs from my original
        idea of updating the heap in place, this one uses timestamp to examine
        whether the top of the heap is valid. We can keep popping the top of
        the heap until a valid member shows up. This is similar to the maximim
        and minimum methods in StockPrice1.

        1993 ms, faster than 39.76%
        """
        self.ts_price = {}
        self.max_heap = []
        self.min_heap = []
        self.cur_time = 0

    def update(self, timestamp: int, price: int) -> None:
        self.cur_time = max(self.cur_time, timestamp)
        self.ts_price[timestamp] = price
        # important step. Push timestamp along with price
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.ts_price[self.cur_time]

    def maximum(self) -> int:
        # use timestamp to check whether the top of the heap exists in ts_price
        while self.ts_price[self.max_heap[0][1]] != -self.max_heap[0][0]:
            heapq.heappop(self.max_heap)
        return -self.max_heap[0][0]

    def minimum(self) -> int:
        # use timestamp to check whether the top of the heap exists in ts_price
        while self.ts_price[self.min_heap[0][1]] != self.min_heap[0][0]:
            heapq.heappop(self.min_heap)
        return self.min_heap[0][0]


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
