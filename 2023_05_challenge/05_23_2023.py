# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        """LeetCode 703

        Use heap to keep track of the k larget values in the stream

        O(logN) for add. 115 ms, faster than 21.59%
        """

        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heappushpop(self.heap, val)
        return self.heap[0]



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
