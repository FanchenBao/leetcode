# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        if primeFactors == 1:
            return 1
        MOD = 10**9 + 7
        n = round(primeFactors / 3)
        s = primeFactors - n
        a = s // n
        b = a + 1
        k = s % n
        res = (a + 1)**(n - k) * (b + 1)**k
        return res % MOD

        

sol = Solution()
tests = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 6),
    (6, 9),
    (7, 12),
    (8, 18),
    (9, 27),
    (10, 36),
]

for i, (primeFactors, ans) in enumerate(tests):
    res = sol.maxNiceDivisors(primeFactors)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
