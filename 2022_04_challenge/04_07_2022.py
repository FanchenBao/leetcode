# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """LeetCode 1046

        Use heap.

        O(NlogN), 47 ms, 46% ranking.
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            y, x = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, y - x)
        return 0 if not heap else -heap[0]


sol = Solution()
tests = [
    ([2,7,4,1,8,1], 1),
    ([1], 1),
]

for i, (stones, ans) in enumerate(tests):
    res = sol.lastStoneWeight(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
