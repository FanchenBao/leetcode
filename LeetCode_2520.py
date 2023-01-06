# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countDigits(self, num: int) -> int:
        """58 ms, faster than 5.10%"""
        return sum(num % int(d) == 0 for d in str(num))

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
