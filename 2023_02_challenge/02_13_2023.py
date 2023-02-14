# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countOdds(self, low: int, high: int) -> int:
        """LeetCode 1523

        21 ms, faster than 98.52%
        """
        rl, rh = low % 2, high % 2
        if rl + rh == 1:
            return (high - low + 1) // 2
        if rl == 0 and rh == 0:
            return (high - low) // 2
        return (high - low) // 2 + 1

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
