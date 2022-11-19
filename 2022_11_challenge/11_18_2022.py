# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def isUgly(self, n: int) -> bool:
        """LeetCode 263

        Must add check for n <= 0.

        68 ms, faster than 25.67% 
        """
        if n <= 0:
            return False

        def div(num: int, d: int) -> int:
            while num % d == 0:
                num //= d
            return num

        return div(div(div(n, 2), 3), 5) == 1


sol = Solution()
tests = [
    (6, True),
    (1, True),
    (14, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isUgly(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
