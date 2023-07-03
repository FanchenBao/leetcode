# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        """185 ms, faster than 62.40%
        """
        return ((m := max(nums)) + m + k - 1) * k // 2


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
