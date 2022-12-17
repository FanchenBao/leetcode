# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, deque


class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:
        indices = defaultdict(deque)
        N = len(nums1)
        for i, n in enumerate(nums1):
            if n == nums2[i]:
                indices[n].append(i)
        # print(indices)
        if not indices:
            return 0
        res = 0
        keys = sorted(indices.keys(), key=lambda k: -len(indices[k]))
        # make sure we have best chance of swapping with 0 index
        if nums1[0] in indices and nums2[0] in indices and nums1[0] != nums2[0]:
            while indices[nums1[0]] and indices[nums2[0]]:
                ii = indices[nums1[0]].popleft()
                jj = indices[nums2[0]].popleft()
                res += ii + jj
                nums1[ii], nums1[jj] = nums1[jj], nums1[ii]
        if nums1[0] in indices:
            j = 0
            while indices[nums1[0]]:
                while j < len(keys) and (not indices[keys[j]] or nums1[0] == keys[j]):
                    j += 1
                if j == len(keys):
                    break
                ii = indices[nums1[0]].popleft()
                jj = indices[keys[j]].popleft()
                res += ii + jj
                nums1[ii], nums1[jj] = nums1[jj], nums1[ii]
        if nums2[0] in indices:
            j = 0
            while indices[nums2[0]]:
                while j < len(keys) and (not indices[keys[j]] or nums2[0] == keys[j]):
                    j += 1
                if j == len(keys):
                    break
                ii = indices[nums2[0]].popleft()
                jj = indices[keys[j]].popleft()
                res += ii + jj
                nums1[ii], nums1[jj] = nums1[jj], nums1[ii]


        # print(keys)
        i, j = 0, len(keys) - 1
        # pair the numbers that need to be swapped. This way each swap handles
        # two numbers.
        while True:
            while i < j and not indices[keys[i]]:
                i += 1
            while i < j and not indices[keys[j]]:
                j -= 1
            if i == j:
                break
            ii = indices[keys[i]].popleft()
            jj = indices[keys[j]].popleft()
            res += ii + jj
            nums1[ii], nums1[jj] = nums1[jj], nums1[ii]
            
        # handle the remaining unswapped numbers, which are all the same.
        if indices[keys[i]]:
            for t in range(len(nums1)):
                if nums1[t] != keys[i] and nums2[t] != keys[i]:
                    res += t + indices[keys[i]].popleft()
                    if not indices[keys[i]]:
                        break
        return res if not indices[keys[i]] else -1


sol = Solution()
tests = [
    ([1,2,3,4,5], [1,2,3,4,5], 10),
    ([2,2,2,1,3], [1,2,2,3,3], 10),
    ([1,2,2], [1,2,2], -1),
    ([2, 4, 3, 1, 1], [4, 4, 3, 1, 5], 6),
    ([1,2,3], [3,1,2], 0),
    ([1, 3, 2, 2, 2, 5, 2, 5, 1, 3], [1, 5, 5, 2, 2, 2, 2, 5, 1, 2], 28),
    ([3, 4, 4, 3, 5, 1, 2, 2, 3, 4], [4, 4, 2, 3, 4, 2, 5, 2, 5, 1], 11),
    ([3, 4, 1, 4, 1, 1, 2, 3, 2, 2], [4, 4, 5, 3, 4, 3, 1, 3, 2, 4], 16),
    ([2,1,2,2,1,4,1,5], [2,1,2,2,1,4,1,5], 28),
]

for i, (nums1, nums2, ans) in enumerate(tests):
    res = sol.minimumTotalCost(nums1, nums2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
