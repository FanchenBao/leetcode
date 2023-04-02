# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        """
        62 ms, faster than 44.33%
        """
        lo, hi = 0, len(nums) - 1
        res = 0
        while lo < hi:
            res += int(str(nums[lo]) + str(nums[hi]))
            lo += 1
            hi -= 1
        if lo == hi:
            res += nums[lo]
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
