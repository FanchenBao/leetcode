# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        """LeetCode 1962

        I was confused earlier. We remove the floor number of stones, which means
        the remaining number of stones is the ceiling of each pile divided by 2.
        But it'd be better if we implement it according to the definition.

        O(NLogN), 1786 ms, faster than 94.85%
        """
        heap = [-p for p in piles]
        heapq.heapify(heap)
        for _ in range(k):
            p = -heapq.heappop(heap)
            heapq.heappush(heap, -(p - p // 2))
        return -sum(heap)
        

sol = Solution()
tests = [
    ([5,4,9], 2, 12),
    ([4,3,6,7], 3, 12),
]

for i, (piles, k, ans) in enumerate(tests):
    res = sol.minStoneSum(piles, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
