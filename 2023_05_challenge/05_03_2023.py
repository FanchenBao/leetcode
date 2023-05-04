# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        """LeetCode 2215

        195 ms, faster than 35.70%
        """
        set1, set2 = set(nums1), set(nums2)
        return [
            list(set(n for n in nums1 if n not in set2)),
            list(set(n for n in nums2 if n not in set1)),
        ]

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
