# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def alternateDigitSum(self, n: int) -> int:
        """35 ms, faster than 63.27%
        """
        res = 0
        sign = 1
        for d in str(n):
            res += sign * int(d)
            sign *= -1
        return res


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
