# from pudb import set_trace; set_trace()
from typing import List
import math
import numpy as np


class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        nums1 = np.array(nums1)
        nums2 = np.array(nums2)
        res = []
        for q, a, b in queries:
            if q == 1:
                nums1[a:b + 1] ^= np.ones(b - a + 1, dtype=int)
            elif q == 2:
                nums2 += nums1 * a
            else:
                res.append(np.sum(nums2))
        return res


sol = Solution()
tests = [
    ([1,0,1], [0,0,0], [[1,1,1],[2,1,0],[3,0,0]], [3]),
    ([1], [5], [[2,0,0],[3,0,0]], [5]),
]

for i, (nums1, nums2, queries, ans) in enumerate(tests):
    res = sol.handleQuery(nums1, nums2, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
