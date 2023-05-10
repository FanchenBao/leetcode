# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        """Sort nums in reverse order, and count the total number of positive
        prefix sums.

        O(NlogN), 734 ms, faster than 70.62% 
        """
        return sum(ps > 0 for ps in accumulate(sorted(nums, reverse=True)))


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
