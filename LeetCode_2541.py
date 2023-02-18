# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """This is deterministic. Just analyze it step by step.

        O(N), 726 ms, faster than 88.82%
        """
        if sum(nums1) != sum(nums2):
            return -1
        diff = [n1 - n2 for n1, n2 in zip(nums1, nums2) if n1 != n2]
        if not diff:
            return 0
        if k == 0:
            return -1
        if any(d % k != 0 for d in diff):
            return -1
        return sum(d // k for d in diff if d > 0)


sol = Solution()
tests = [
    ([4,3,1,4], [1,3,7,1], 3, 2),
    ([3,8,5,2], [2,4,1,6], 1, -1),
    ([10,5,15,20], [20,10,15,5], 0, -1),
]

for i, (nums1, nums2, k, ans) in enumerate(tests):
    res = sol.minOperations(nums1, nums2, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
