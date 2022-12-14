# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        """65 ms, faster than 36.03%
        """
        return max(int(s) if s.isdecimal() else len(s) for s in strs)

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
