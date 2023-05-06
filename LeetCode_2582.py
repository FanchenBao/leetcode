# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        """Find quotient and remainder. If quotient is odd, that means we have
        gone to the end from left to right, and the remainder signifies the
        pass from right to left.

        If quotient is even, that means the remainder is going from left to right.

        O(1), 45 ms, faster than 5.22%
        """
        q, r = divmod(time, n - 1)
        return n - r if q % 2 else r + 1

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
