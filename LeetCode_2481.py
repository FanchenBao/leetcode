# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def numberOfCuts(self, n: int) -> int:
        """I got stuck. Didn't realize when you make the first two a long cut,
        they don't have to be perpendicular.

        Also, n == 1 is an edge case.
        34 ms, faster than 86.71% 
        """
        if n == 1:
            return 0
        if n % 2:
            return n
        return n // 2


# sol = Solution()
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
