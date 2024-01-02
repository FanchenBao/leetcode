# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Create two dp arrays, in which dp1[i] = longest length of non-decreasing
        subarray ending at nums1[i], and dp2[i] = the same concept with regards
        to nums2.

        O(N), 838 ms, faster than 95.31%
        """
        N = len(nums1)
        dp1 = [1] * N
        dp2 = [1] * N
        res = 1
        for i in range(1, N):
            # handle nums1
            if nums1[i] >= nums1[i - 1]:
                dp1[i] = dp1[i - 1] + 1
            if nums1[i] >= nums2[i - 1]:
                dp1[i] = max(dp1[i], dp2[i - 1] + 1)
            # handle nums2
            if nums2[i] >= nums2[i - 1]:
                dp2[i] = dp2[i - 1] + 1
            if nums2[i] >= nums1[i - 1]:
                dp2[i] = max(dp2[i], dp1[i - 1] + 1)
            res = max(res, dp1[i], dp2[i])
        return res


# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
