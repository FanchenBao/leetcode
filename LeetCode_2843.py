# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        """
        There are only two posibilities for symmetric integers: either two
        digits or four digits.

        There are only nine two-digit possibilies, we can check them one by one.

        For four digits, we do the actual check.

        120 ms, faster than 97.39%
        """
        res = 0
        two_digits = [11, 22, 33, 44, 55, 66, 77, 88, 99]
        for td in two_digits:
            if low <= td <= high:
                res += 1
        for fd in range(max(low, 1000), min(high, 9999) + 1):
            digsum1 = fd % 10 + fd // 10 % 10
            digsum2 = fd // 100 % 10 + fd // 1000 % 10
            if digsum1 == digsum2:
                res += 1
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
