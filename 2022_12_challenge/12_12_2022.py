# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        """LeetCode 70

        Basic DP.
        O(N), 56 ms, faster than 43.40%
        """
        if n < 3:
            return n
        pp, p = 1, 2
        for _ in range(3, n + 1):
            pp, p = p, p + pp
        return p


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
