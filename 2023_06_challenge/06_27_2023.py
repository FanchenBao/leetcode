# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """LeetCode 373

        Not a simple one. I was clueless for a while, but then I felt like this
        must be priority queue, so I directed myself to that thought process.

        The breakthrough is to realize that if we focus on each index in nums1,
        we have a series of increasing value as we go through nums2. The
        question is when this series stops because the next index in nums1 will
        generate a smaller sum. If we know something small with the next index
        in nums1 serving as a guard, that will help tremendously. And one way
        to do so is through a heap, where we keep the smallest possible sum
        using the next index in nums1 in the heap, such that when that becomes
        the current smallest option, it floats to the top.

        Thus, we create a heap such that it contains the smallest unused pair
        starting from each index in nums1. After we use a pair, we put the next
        smallest unsued pair starting from the same index in nums1.

        O(NlogN + KlogN), 1208 ms, faster than 24.20%
        """
        heap = []
        N, M = len(nums1), len(nums2)
        for i in range(N):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        res = []
        while k and heap:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < M:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        return res
        

sol = Solution()
tests = [
    ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]),
    ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]),
    ([1,2], [3], 3, [[1,3],[2,3]]),
]

for i, (nums1, nums2, k, ans) in enumerate(tests):
    res = sol.kSmallestPairs(nums1, nums2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
