# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """What a problem!!

        There is a lot of math at the beginning.

        Given pf number of prime factors, we can decide to use n unique prime
        numbers. Say we use two prime numbers. Then the nice divisor must use
        the two unique prime numbers at least once. Thus, the number of free
        prime numbers to form other nice divisors is pf - 2

        Then we say the number of the first free prime number is a, and the
        number of the second free prime number is b.

        We have a + b = pf - 2

        To form all the nice divisors, we have a number of unique factors formed
        by all the free first prime number. We have b number of unique factors
        formed by all the free second prime number. Then the total number of
        nice divisors is a + b + 1 + ab = (a + 1)(b + 1)

        Let's say we have three unique prime numbers.

        a + b + c = pf - 2

        Thus the total number of nice divisors is
        a + b + c + 1 + ab + ac + bc + abc = (a + 1)(b + 1)(c + 1)

        Thus, given n unique prime numbers, we have
        x1 + x2 + ... + xn = pf - n

        Total number of nice divisors is
        (x1 + 1)(x2 + 1)...(xn + 1)

        The problem converts to finding the max product of n values when we know
        the sum of the n values.

        This is a solved math problem. The answer is that the n values must not
        be different more than 1. The proof is here: https://math.stackexchange.com/a/2299922

        Using that proof, we can obtain the max number of nice divisors given
        any number of unique prime numbers.

        Then from observation (no proof at the moment), the optimal number of
        nice divisors is round(pf / 3). Then we just need to compute the max
        value once.

        However, the computation itself can involve giant number in power. Thus
        we have to handle the power computation ourselves by including MOD in it.

        Hence we have to write the power() function ourselves.

        O(logN), 22 ms, faster than 100.00%
        """
        if primeFactors == 1:
            return 1
        MOD = 10**9 + 7

        def modulo_power(a: int, b: int) -> int:
            res = 1
            while b:
                if b % 2:
                    res = (res * a) % MOD
                a = (a * a) % MOD
                b //= 2
            return res

        n = round(primeFactors / 3)
        # the s, a, b, k method derives from https://math.stackexchange.com/a/2299922
        s = primeFactors - n
        a = s // n
        b = a + 1
        k = s % n
        res = modulo_power(a + 1, n - k) * modulo_power(b + 1, k)
        return res % MOD


class Solution2:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """Use python's built-in pow that has an option for Modulo
        """
        if primeFactors == 1:
            return 1
        MOD = 10**9 + 7

        n = round(primeFactors / 3)
        # the s, a, b, k method derives from https://math.stackexchange.com/a/2299922
        s = primeFactors - n
        a = s // n
        b = a + 1
        k = s % n
        res = pow(a + 1, n - k, MOD) * pow(b + 1, k, MOD)
        return res % MOD


class Solution3:
    def maxNiceDivisors(self, primeFactors: int) -> int:
        """Better proof of why we shall divide primeFactors by three.

        https://leetcode.com/problems/maximize-number-of-nice-divisors/discuss/1130607/Python-logN-Solution

        The proof also uses the fact that given bunch of values added up to
        primeFactor, their product reaches the max when these valuses are all
        the same.
        """
        if primeFactors == 1:
            return 1
        if primeFactors == 2:
            return 2
        MOD = 10**9 + 7
        # use as many factor 3 as possible. The remaining is filled with 2
        q, r = divmod(primeFactors, 3)
        if r == 0:
            return pow(3, q, MOD)
        if r == 1:
            return pow(3, q - 1, MOD) * 4 % MOD  # use q - 1 number of three and two twos
        if r == 2:
            return pow(3, q, MOD) * 2 % MOD  # use q number of three and one two


sol = Solution3()
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


