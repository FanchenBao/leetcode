# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """LeetCode 1046

        Pay attention to the situation where heap is empty at the end.

        O(NlogN), 33 ms, faster than 59.77%
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        return -heap[0] if heap else 0
        

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
