# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        indices = {}
        res = 0
        N = len(nums1)
        for i, n in enumerate(nums1):
            if n != nums2[i]:
                continue
            j = indices.get(n, 0)
            while j < N and (nums2[j] == n or nums1[j] == n):
                j += 1
            if j == N:
                return -1
            if j > 0:
                nums1[i], nums1[j] = nums1[j], nums1[i]
                res += i + j
                indices[n] = j

        queue = list(range(N))
        while queue:
            tmp = []
            for i in queue:
                if nums1[i] == nums2[i]:
                    if nums1[i] == nums1[0] or nums1[i] == nums2[0]:
                        tmp.append(i)
                    else:
                        nums1[i], nums1[0] = nums1[0], nums1[i]
                        res += i
            if queue == tmp:
                return -1
            queue = tmp
        return res


sol = Solution()
tests = [
    ([1,2,3,4,5], [1,2,3,4,5], 10),
    ([2,2,2,1,3], [1,2,2,3,3], 10),
    ([1,2,2], [1,2,2], -1),
    ([2, 4, 3, 1, 1], [4, 4, 3, 1, 5], 6),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.minimumTotalCost(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
