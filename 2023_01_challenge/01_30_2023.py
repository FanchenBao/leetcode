# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def tribonacci(self, n: int) -> int:
        """LeetCode 1137

        27 ms, faster than 90.72% 
        """
        if n == 0:
            return 0
        if n <= 2:
            return 1
        ppp, pp, p = 0, 1, 1
        for _ in range(3, n + 1):
            ppp, pp, p = pp, p, p + pp + ppp
        return p


sol = Solution()
tests = [
    (4, 4),
    (25, 1389537),
]

for i, (n, ans) in enumerate(tests):
    res = sol.tribonacci(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
