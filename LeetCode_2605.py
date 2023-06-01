# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        """Got hit by the fact that there is no requirement that the first digit
        must come from nums1. Thus, we have to find the smallest between the
        min of nums1 and min of nums2 as the first digit.
        """
        overlap = set(nums1).intersection(nums2)
        if overlap:
            return min(overlap)
        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)

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
