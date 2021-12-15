# from pudb import set_trace; set_trace()
from typing import List
import heapq
import math


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """LeetCode 373

        Ref: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84551/simple-Java-O(KlogK)-solution-with-explanation/232946

        This is merging k sorted list. It's just that I didn't see it.

        nums1 = [-10,-4,0,0,6]
        nums2 = [3,5,6,7,8,100]
        k = 10, then we need at most 10 linked list. We can pick either list
        as the anchor points. Let's pick nums2

        L1: (-10, 3) -> (-4, 3) -> (0, 3) -> (0, 3) -> (6, 3)
        L2: (-10, 5) -> (-4, 5) -> (0, 5) -> (0, 5) -> (6, 5)
        L3: (-10, 6) -> (-4, 6) -> (0, 6) -> (0, 6) -> (6, 6)
        L4: (-10, 7) -> (-4, 7) -> (0, 7) -> (0, 7) -> (6, 7)
        L5: (-10, 8) -> (-4, 8) -> (0, 8) -> (0, 8) -> (6, 8)
        L6: (-10, 10) -> (-4, 10) -> (0, 10) -> (0, 10) -> (6, 10)

        Then we simply merge these six sorted list based on sum.

        O(KlogK), 990 ms, 18% ranking.
        """
        heap = [(nums1[0] + nums2[j], 0, j) for j in range(min(k, len(nums2)))]
        res, M = [], len(nums1)
        res_len = min(k, len(nums1) * len(nums2))
        while len(res) < res_len:
            _, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if i + 1 < M:
                heapq.heappush(heap, (nums1[i + 1] + nums2[j], i + 1, j))
        return res
        

sol = Solution()
tests = [
    ([1,7,11], [2,4,6], 3, [[1,2],[1,4],[1,6]]),
    ([1,1,2], [1,2,3], 2, [[1,1],[1,1]]),
    ([1, 2], [3], 3, [[1, 3], [2, 3]]),
    ([-10,-4,0,0,6], [3,5,6,7,8,100], 10, [[-10,3],[-10,5],[-10,6],[-10,7],[-10,8],[-4,3],[-4,5],[-4,6],[-4,7],[0,3]]),
]

for i, (nums1, nums2, k, ans) in enumerate(tests):
    res = sol.kSmallestPairs(nums1, nums2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
