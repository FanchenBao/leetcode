# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word in {word.upper(), word.lower(), word.title()}


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
