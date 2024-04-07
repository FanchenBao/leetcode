# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Greedy. We fill the array from 1. By doing so we
        create a ceil of k - 1. If the new value is larger
        than k - 1, then there is no risk of any two-sum
        to hit k.

        Then we hit 2, 3, 4, ... each time the value increment
        by 1. These values also create a floor, which is k - val.
        If a new value is smaller than k - val, there is also no
        risk of hitting k. However, if the new value is in between
        floor and ceil, we cannot take it and have to go for the
        next one.

        O(N), 49 ms, faster than 36.53%
        """
        res = val = 1
        ceil = floor = k - 1
        n -= 1
        while n:
            val += 1
            if val > ceil or val < floor:
                res += val
                n -= 1
                floor = max(floor, k - val)
        return res


class Solution2:
    def minimumSum(self, n: int, k: int) -> int:
        """
        Math solution.

        We add from 1, 2, 3, ... x, x + 1

        Let's say x + 1 is the first value that fails. Then we have
        x + 1 >= k - x => x >= (k - 1) / 2

        Thus, we can take x = k // 2

        Then we add from 1, 2, 3, ... k // 2
        If more numbers are needed, we start from k until all n values are
        considered.

        O(1), 48 ms, faster than 40.18%
        """
        x = k // 2
        if x >= n:
            return (n + 1) * n // 2
        return (x + 1) * x // 2 + (k + k + n - x - 1) * (n - x) // 2


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
