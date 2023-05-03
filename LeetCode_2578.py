# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def splitNum(self, num: int) -> int:
        """Sort num's digits, and take even indices to be one value, and odd
        indices to be the other value.

        47 ms, faster than 7.28%
        """
        num_str = sorted(str(num))
        return int(''.join(num_str[::2])) + int(''.join(num_str[1::2]))


class Solution2:
    def splitNum(self, num: int) -> int:
        """Do not use int(str)

        44 ms, faster than 7.28%
        """
        num_str = sorted(str(num))
        v1 = v2 = 0
        for i in range(0, len(num_str), 2):
            v1 = v1 * 10 + int(num_str[i])
            if i + 1 < len(num_str):
                v2 = v2 * 10 + int(num_str[i + 1])
        return v1 + v2


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
