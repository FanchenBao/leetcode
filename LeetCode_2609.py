# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        """Count the number of consecutive 1s and 0s.

        O(N), 58 ms, faster than 19.72%
        """
        res = 0
        zero_count = 0
        for k, g in groupby(s):
            if k == '0':
                zero_count = len(list(g))
            else:
                res = max(res, 2 * min(zero_count, len(list(g))))
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
