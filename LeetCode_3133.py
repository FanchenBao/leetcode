# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minEnd(self, n: int, x: int) -> int:
        """
        This method is inspired by the official solution. Since the AND of all
        numbers in the array must equal to x, all the numbers must have set
        bits on the same set bits location as x. In addition, x itself must be
        the smallest number in the array, because it needs to provide the zero
        at the zero positions.

        Thus, the only positions we can modify are the zero positions. We can
        go from 1 to n - 1 and use their patterns to fill out only the zero
        positions. In other words, the end of the array must have all its zero
        positions match the pattern of n - 1.

        O(1), 0 ms, faster than 100.00%
        """
        res = x
        pat = n - 1
        i = 0
        while pat:
            if res & (1 << i) == 0:
                res |= (n & 1) << i
                n >>= 1
            i += 1
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
