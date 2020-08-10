#! /usr/bin/env python3

"""07/28/2019

This solution is a hack. Since n <= 37, I simply put res array size at 38 so
that I don't have to consider edge cases.
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        res = [0] * 38
        res[0], res[1], res[2] = 0, 1, 1
        for i in range(3, n + 1):
            res[i] = res[i - 1] + res[i - 2] + res[i - 3]
        return res[n]
