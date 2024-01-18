# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        pp, p = 1, 1
        for i in range(2, n + 1):
            pp, p = p, p + pp
        return p


class Solution2:
    def climbStairs(self, n: int) -> int:
        """
        LeetCode 70

        Fibonacci number.

        O(1), 29 ms, faster than 93.70%
        """
        fib = [
            1,
            1,
            2,
            3,
            5,
            8,
            13,
            21,
            34,
            55,
            89,
            144,
            233,
            377,
            610,
            987,
            1597,
            2584,
            4181,
            6765,
            10946,
            17711,
            28657,
            46368,
            75025,
            121393,
            196418,
            317811,
            514229,
            832040,
            1346269,
            2178309,
            3524578,
            5702887,
            9227465,
            14930352,
            24157817,
            39088169,
            63245986,
            102334155,
            165580141,
            267914296,
            433494437,
            701408733,
            1134903170,
            1836311903,
        ]
        return fib[n]


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
