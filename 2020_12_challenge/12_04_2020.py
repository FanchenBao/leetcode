# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def kthFactor(self, n: int, k: int) -> int:
        """Most native solution. 32 ms, 63% ranking"""
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
            if k == 0:
                return i
        return -1


class Solution2:
    def kthFactor(self, n: int, k: int) -> int:
        """O(sqrt(n)) 20ms, 99% ranking"""
        factors = [(i, n // i) for i in range(1, int(math.sqrt(n)) + 1) if not n % i]
        len_f = len(factors)
        total = 2 * len_f - (1 if factors[-1][0] == factors[-1][1] else 0)
        if k > total:
            return -1
        return factors[k - 1][0] if k <= len_f else factors[-k % len_f][1]


sol = Solution2()
tests = [
    (12, 3, 3),
    (7, 2, 7),
    (4, 4, -1),
    (1, 1, 1),
    (1000, 3, 4),
    (24, 6, 8),
]

for i, (n, k, ans) in enumerate(tests):
    res = sol.kthFactor(n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
