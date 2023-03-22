# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        """Use heap.

        O(KlogN), 47 ms, faster than 85.40%
        """
        heap = [-g for g in gifts]
        heapq.heapify(heap)
        for _ in range(k):
            max_gift = -heapq.heappop(heap)
            heapq.heappush(heap, -math.floor(math.sqrt(max_gift)))
        return -sum(heap)
        

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
