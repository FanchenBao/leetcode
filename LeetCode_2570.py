# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        """Merge sort.

        O(N), 58 ms, faster than 93.72%
        """
        i = j = 0
        M, N = len(nums1), len(nums2)
        res = []
        while i < M and j < N:
            if nums1[i][0] == nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append(nums1[i][:])
                i += 1
            else:
                res.append(nums2[j][:])
                j += 1
        if i < M:
            res += nums1[i:]
        if j < N:
            res += nums2[j:]
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
