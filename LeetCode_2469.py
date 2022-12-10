# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        """36 ms, faster than 83.75%
        """
        return [celsius + 273.15, celsius * 1.80 + 32.00]


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
