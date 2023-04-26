# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        """LeetCode 2336

        Use sentinel to indicate the front of the original infinite set. Use a
        min heap to record the values smaller or equal to the sentinuel.

        The smallest value must come from the front of the heap. If the min
        value is the same as the sentinel, that means we are peeling back the
        original infinite set. Thus, we have to increment the sentinel and update
        the value in the min heap.

        Otherwise, we don't have to change the sentinel.

        When adding back, if the added value is larger or equal to the sentinel,
        that means the added value is already part of the original infinite set.
        Otherwise, we add the value to the min heap.

        One thing to note is that when popping from the heap, we must remove
        duplicates.

        129 ms, faster than 62.64%
        """
        self.sentinel = 1
        self.heap = [1]
        
    def popSmallest(self) -> int:
        s = heapq.heappop(self.heap)
        while self.heap and s == self.heap[0]:  # remove duplicates
            s = heapq.heappop(self.heap)
        if s == self.sentinel:
            heapq.heappush(self.heap, s + 1)
            self.sentinel = s + 1
        return s
        
    def addBack(self, num: int) -> None:
        if num < self.sentinel:
            heapq.heappush(self.heap, num)

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
