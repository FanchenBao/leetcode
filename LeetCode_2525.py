# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        is_bulky = any([
            length >= 10**4,
            width >= 10**4,
            height >= 10**4,
            length * width * height >= 10**9,
        ])
        is_heavy = mass >= 100
        if is_bulky and is_heavy:
            return 'Both'
        if not is_bulky and not is_heavy:
            return 'Neither'
        if is_bulky:
            return 'Bulky'
        return 'Heavy'


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
