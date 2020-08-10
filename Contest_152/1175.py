#! /usr/bin/env python3
from typing import List
from bisect import bisect_right
from math import sqrt

"""09/03/2019

Solution1:
Use a pre-made prime list up to 100. Count the number of primes below n, and
the number of non-primes. To ensure primer numbers are all on the prime
positions, since the prime positions and prime numbers have one-to-one relation,
we do factorial on the number of primes. The non-prime numbers can occupy the
non-prime positions freely, so we have to multiply with the factorial of the
number of non-primes.


Solution2:
Same basic idea as Solution1, but using eratosthenes sieve to generate the prime
list.

BOTH solutions clocked in at 40 ms, 48.55%
"""


class Solution1:
    def numPrimeArrangements(self, n: int) -> int:
        primes: List[int] = [
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
            29,
            31,
            37,
            41,
            43,
            47,
            53,
            59,
            61,
            67,
            71,
            73,
            79,
            83,
            89,
            97,
        ]
        if n == 1:
            return 1  # OJ requires this to be 1, but I think it should be 0
        else:
            num_prime: int = bisect_right(primes, n)
            num_non_prime: int = n - num_prime
            return (
                self.factorial(num_prime)
                * self.factorial(num_non_prime)
                % (10 ** 9 + 7)
            )

    def factorial(self, n: int) -> int:
        res: int = 1
        while n > 1:
            res *= n
            n -= 1
        return res


class Solution2:
    def numPrimeArrangements(self, n: int) -> int:
        raw_primes = self.sieve(100)
        prime_counts = self.count_primes(raw_primes, 100)
        return (
            self.factorial(prime_counts[n])
            * self.factorial(n - prime_counts[n])
            % (10 ** 9 + 7)
        )

    def sieve(self, n: int) -> List[int]:
        res: List[int] = [1] * (n + 1)
        res[0], res[1] = 0, 0
        for i in range(4, n + 1, 2):
            res[i] = 0
        for i in range(3, int(sqrt(n)) + 1, 2):
            j = i
            while j * i < n:
                res[j * i] = 0
                j += 2
        return res

    def count_primes(self, raw_primes: List[int], n: int) -> List[int]:
        res: List[int] = [0] * (n + 1)
        acc: int = 0
        for i in range(1, n + 1):
            if raw_primes[i]:
                acc += 1
            res[i] = acc
        return res

    def factorial(self, n: int) -> int:
        res: int = 1
        while n > 1:
            res *= n
            n -= 1
        return res


sol = Solution2()
print(sol.numPrimeArrangements(1))
