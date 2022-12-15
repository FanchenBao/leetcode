# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        N = len(nums1)
        for i in range(N - 1, -1, -1):
            if nums1[i] == nums2[i]:
                for j in range(N):
                    if nums1[i] != nums1[j] and nums2[j] != nums1[i]:
                        nums1[i], nums1[j] = nums1[j], nums1[i]
                        res += i + j
                        break
                else:
                    return -1
        return res


sol = Solution()
tests = [
    # ([1,2,3,4,5], [1,2,3,4,5], 10),
    # ([2,2,2,1,3], [1,2,2,3,3], 10),
    # ([1,2,2], [1,2,2], -1),
    ([2, 4, 3, 1, 1], [4, 4, 3, 1, 5], 6),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.minimumTotalCost(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
