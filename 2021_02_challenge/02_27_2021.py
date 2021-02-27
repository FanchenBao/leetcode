# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def divide(self, dividend: int, divisor: int) -> int:
        """LeetCode 29

        The sign is pretty tricky to handle, so we do not handle it when we
        actually perform the division. This means we will perform abs() on both
        dividend and divisor.

        During division, we take away divisor from dividend. Each time we can
        perform a take-way, we double divisor. This speeds up the division
        process. We continue until the remaining dividend is smaller than the
        current and enhanced divisor. When this happens, we run the function
        again by passing in the smaller dividend and the ORIGINAL divsior. The
        quotient is the number of times the original divisor has been taken
        away from the dividend.

        Once the positive value division is complete, we think about the sign.
        We can use a bit manipulation trick to get whether the dividend and
        divisor have the same sign.

        Finally, the only chance of overflow is when the quotient is 2^31, which
        is calused by -2^31 // -1. We check this special case before return.

        O(log(dividend)), 32 ms, 76% ranking.
        """
        OVERFLOW = 2**31 - 1
        MASK = 2**31
        dd, ds = abs(dividend), abs(divisor)
        c, q = 0, 0
        x = ds
        while dd >= x:
            dd -= x
            c += c if c else 1  # counter
            x += x
            q += c
        res = q + (self.divide(dd, ds) if dd >= ds else 0)
        if (dividend ^ divisor) & MASK == 0:
            return OVERFLOW if res > OVERFLOW else res
        else:
            return -res


class Solution2:
    OVERFLOW = 2**31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        """A better solution without recursion. It is the same as before, but
        using loops instead of recursion to handle the remaining of dividend
        after the current enhanced divisor has been exhausted from it. I like
        this one better, because it's shorter and uses bit manipulation to
        handle the doubling.

        Reference: https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations

        28 ms, 92% ranking.
        """
        if dividend == -(self.OVERFLOW + 1) and divisor == -1:
            return self.OVERFLOW
        dd, ds = abs(dividend), abs(divisor)
        c, q = 1, 0
        while dd >= ds:
            temp = ds
            while dd >= temp:
                dd -= temp
                q += c
                c <<= 1
                temp <<= 1
            c = 1
        return -q if (dividend > 0) ^ (divisor > 0) else q


class Solution3:
    OVERFLOW = 2**31 - 1

    def divide(self, dividend: int, divisor: int) -> int:
        """Solution from lee215. It's very very smart

        Reference: https://leetcode.com/problems/divide-two-integers/discuss/142849/C%2B%2BJavaPython-Should-Not-Use-%22long%22-Int

        24 ms, 97% ranking!
        """
        if dividend == -(self.OVERFLOW + 1) and divisor == -1:
            return self.OVERFLOW
        dd, ds, q = abs(dividend), abs(divisor), 0
        for c in range(31, -1, -1):
            # check how many times ds can be doubled and still removable from dd
            if (dd >> c) >= ds:
                q += 1 << c
                dd -= ds << c  # remove the c times doubled ds from dd
        return -q if (dividend > 0) ^ (divisor > 0) else q


sol = Solution3()
tests = [
    (10, 3, 3),
    (7, -3, -2),
    (0, 1, 0),
    (1, 1, 1),
    (-2147483648, 1, -2147483648),
    (-2147483648, -1, 2147483647),
]

for i, (dividend, divisor, ans) in enumerate(tests):
    res = sol.divide(dividend, divisor)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
