#! /usr/bin/env python3
from typing import List
from random import randint

"""09/29/2019

Solution1:

First, we preprocess `a`,`b`, and `c`. We order them first, and then choose only
the ones that are relative prime to each other for further computation.

Then, we set the max value that the answer could be `res = a * n`. Then for each
increment in `b` (i.e `b`, `2b`, `3b`, ...), we decrease `res` by the amount of `a`. In
other words, as an additional multiple of `b` is added, we remove `a` from `res`.
If multiple of `b` is also a multiple of `a`, we do no remove `a`. We continue this
process until multiple of `b` is larger or equal to `res`.

Finally, we consider `c`. This is tricker because now when we remove, it could be
`a`, or `b`, or the next biggest number that is a multiple of `a` or `b`. It is clear
that if `res` currently is only a multiple of `a`, we shall compare `res - a` and the
next biggest multiple of `b`, and choose the larger of the two. The same applies
to `res` being only a multiple of `b`. When `res` is both a multiple of `a` and `b`, since
`a < b`, we choose to remove `a`. Continute this process until multiple of `c` is
larger or equal to `res`.

This solution is corrected constantly based on trial and error with the test
cases. There are so many cases I haven't thought about, so I am really NOT
happy with the outcome. It clocks in at 40ms, 61%.


UPDATE: 10/07/2019

Solution2:

This is the standard solution using binary search. Refer to this post for explanation

https://leetcode.com/problems/ugly-number-iii/discuss/387539/cpp-Binary-Search-with-picture-and-Binary-Search-Template

The key is to count the number of ugly numbers up to a limit via an implementation
of Vinn diagram. Then binary search from 1 to 2 * 10^9 to find a limit whose
count is equal to n. Then count down from that limit to find the FIRST limit
that allows its count to reach n. Such first limit is the answer.

It clocks in at 36 ms, 85%
"""


class Solution1:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # make sure there is no repeition in the inputs and rearrange a, b, c
        # from small to big
        inputs: List[int] = sorted(list({a, b, c}))
        # Currently the nth number. As we include b and c, res shall decrease
        res: int = n * inputs[0]
        # investigate b, do this only if b and a are coprime
        if len(inputs) > 1 and inputs[1] % inputs[0]:
            mb: int = inputs[1]  # multiple of b, starts from 1 * b
            while mb < res:
                if mb % inputs[0]:  # if mb and a are coprime, reduce res by a
                    res -= inputs[0]
                    if (
                        res < mb
                    ):  # anchor case. mb is larger than res, mb becomes new res
                        res = mb
                mb += inputs[1]  # increment mb by b each time
        # investigate c, do this only if c is coprime with both a and b
        if len(inputs) > 2 and inputs[2] % inputs[0] and inputs[2] % inputs[1]:
            mc: int = inputs[2]  # multiple of c, starts from 1 * c
            while mc < res:
                # If mc is coprime with a and b, we need to add mc,
                # and reduce res.
                if mc % inputs[0] and mc % inputs[1]:
                    if (
                        res % inputs[0] == 0 and res % inputs[1]
                    ):  # res divisible by a but not b
                        res = max(
                            res - inputs[0], res // inputs[1] * inputs[1]
                        )
                    elif (
                        res % inputs[1] == 0 and res % inputs[0]
                    ):  # res divisible by b but not a
                        res = max(
                            res - inputs[1], res // inputs[0] * inputs[0]
                        )
                    else:
                        res -= inputs[0]
                    if res < mc:  # anchor case
                        res = mc
                mc += inputs[2]  # increment mc by c each time
        return res


class Solution2:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        lcm_ab: int = a * b // self.gcd(a, b)
        lcm_bc: int = c * b // self.gcd(c, b)
        lcm_ac: int = a * c // self.gcd(a, c)
        lcm_abc: int = lcm_ab * c // self.gcd(lcm_ab, c)

        def count(lim: int):
            return (
                lim // a
                + lim // b
                + lim // c
                - lim // lcm_ab
                - lim // lcm_ac
                - lim // lcm_bc
                + lim // lcm_abc
            )

        lo, hi = 1, 2 * 10 ** 9
        while lo <= hi:
            mid: int = (lo + hi) // 2
            if count(mid) > n:
                hi = mid - 1
            elif count(mid) < n:
                lo = mid + 1
            else:
                break
        while count(mid) == n:
            mid -= 1
        return mid + 1

    def gcd(self, a: int, b: int) -> int:
        return a if b == 0 else self.gcd(b, a % b)


def unit_tests(Sol):
    sol = Sol()
    # Test case 1
    n, a, b, c = 3, 2, 3, 5
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 4:
        print("Test case 1: PASS")
    else:
        print(f"Test case 1: fail. Wrong answer {res}")

    # Test case 2
    n, a, b, c = 4, 2, 3, 4
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 6:
        print("Test case 2: PASS")
    else:
        print(f"Test case 2: fail. Wrong answer {res}")

    # Test case 3
    n, a, b, c = 5, 2, 11, 13
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 10:
        print("Test case 3: PASS")
    else:
        print(f"Test case 3: fail. Wrong answer {res}")

    # Test case 4
    n, a, b, c = 1000000000, 2, 217983653, 336916467
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 1999999984:
        print("Test case 4: PASS")
    else:
        print(f"Test case 4: fail. Wrong answer {res}")

    # Test case 5
    n, a, b, c = 9, 5, 9, 8
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 24:
        print("Test case 5: PASS")
    else:
        print(f"Test case 5: fail. Wrong answer {res}")

    # Test case 6
    n, a, b, c = 8, 5, 7, 3
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 14:
        print("Test case 6: PASS")
    else:
        print(f"Test case 6: fail. Wrong answer {res}")

    # Test case 7
    n, a, b, c = 26, 14, 25, 14
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 238:
        print("Test case 7: PASS")
    else:
        print(f"Test case 7: fail. Wrong answer {res}")

    # Test case 8
    n, a, b, c = 200, 46, 12, 101
    res = sol.nthUglyNumber(n, a, b, c)
    if res == 1812:
        print("Test case 8: PASS")
    else:
        print(f"Test case 8: fail. Wrong answer {res}")


def gen_random_input() -> List[int]:
    """ Return [n, a, b, c] """
    return [randint(1, 10 ** 9) for _ in range(4)]


def random_test(Sol):
    n, a, b, c = gen_random_input()
    sol = Sol()
    for val in gen_random_input():
        print(val)
    print(sol.nthUglyNumber(n, a, b, c))


def single_test(Sol):
    n, a, b, c = 200, 46, 12, 101
    sol = Sol()
    print(sol.nthUglyNumber(n, a, b, c))


unit_tests(Solution2)
# random_test(Solution)
# single_test(Solution)
