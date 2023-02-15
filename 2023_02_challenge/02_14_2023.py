# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """LeetCode 67

        36 ms, faster than 63.95% 
        """
        return bin(int(a, 2) + int(b, 2))[2:]

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
