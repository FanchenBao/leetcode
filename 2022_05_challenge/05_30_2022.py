# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """LeetCode 29

        This is not the original solution I have submitted, but my original
        one is quite close to this, despite having less elegant implementation.
        The basic idea is to keep removing divisor, and each round double the
        divisor, until a point is reached where a doubled divisor can no longer
        be removed. At that point, we drop down to the original divisor and
        try again.

        O(log(dividend))
        """
        if dividend == -(1 << 31) and divisor == -1:
            return (1 << 31) - 1
        res, c = 0, 1
        dd, ds = abs(dividend), abs(divisor)
        while dd >= ds:
            d = ds
            while dd >= d:
                dd -= d
                res += c
                d <<= 1
                c <<= 1
            c = 1
        return -res if (dividend > 0) ^ (divisor > 0) else res


sol = Solution()
tests = [
    (10, 3, 3),
    (7, -3, -2),
]

for i, (dividend, divisor, ans) in enumerate(tests):
    res = sol.divide(dividend, divisor)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
