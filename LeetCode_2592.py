# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        """Sort the nums and two pointer. Each time the hi points to a value
        larger than lo, that is greatness.

        O(NlogN), 563 ms, faster than 74.03% 
        """
        nums.sort()
        lo = res = 0
        for hi in range(len(nums)):
            if nums[hi] > nums[lo]:
                res += 1
                lo += 1
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
