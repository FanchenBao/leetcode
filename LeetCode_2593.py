# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        """Priority queue.

        O(NlogN), 1512 ms, faster than 39.70%
        """
        heap = []
        for i, n in enumerate(nums):
            heapq.heappush(heap, (n, i))
        marked = [0] * len(nums)
        res = 0
        while heap:
            n, i = heapq.heappop(heap)
            if not marked[i]:
                res += n
                marked[i] = 1
                if i - 1 >= 0:
                    marked[i - 1] = 1
                if i + 1 < len(nums):
                    marked[i + 1] = 1
        return res



sol = Solution()
tests = [
    ([2,1,3,4,5,2], 7),
    ([2,3,5,1,3,2], 5),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.findScore(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
