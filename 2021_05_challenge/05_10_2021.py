# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_left


class Solution1:
    def countPrimes(self, n: int) -> int:
        """LeetCode 204

        Using Eratosthenes sieve directly. But keep in mind that the
        requirment is smaller than n, not smaller or equal to n.

        O(N sqrt(N)), 2112 ms, 27% ranking.

        NOTE: from the official solution, the runtime is bounded by
        O(sqrt(N) loglog(N)).

        The proof is here: https://www.cs.umd.edu/~gasarch/BLOGPAPERS/sump.pdf
        But it is a bit over my current math level. I have worked through two
        pages, and currently stopped at Proposition 3.2.
        """
        if n <= 2:
            return 0
        sieve = [0] * n
        sieve[0] = 1
        sieve[1] = 1
        for i in range(2, n, 2):
            sieve[i] = 1
        sieve[2] = 0
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            j = i
            while i * j < n:
                sieve[i * j] = 1
                j += 2
        return sieve.count(0)


class Solution2:
    primes = []

    def countPrimes(self, n: int) -> int:
        """Cache the sieve.

        1684 ms, 32% ranking.
        """
        if not self.primes:
            max_n = 5 * 10**6
            sieve = [0] * max_n
            sieve[0] = 1
            sieve[1] = 1
            for i in range(2, max_n, 2):
                sieve[i] = 1
            sieve[2] = 0
            for i in range(3, int(math.sqrt(max_n)) + 1, 2):
                j = i
                while i * j < max_n:
                    sieve[i * j] = 1
                    j += 2
            for i, s in enumerate(sieve):
                if s == 0:
                    self.primes.append(i)
        return bisect_left(self.primes, n)


class Solution3:
    def countPrimes(self, n: int) -> int:
        """The same sieve but MUCH MUCH nicer and simpler to implement.

        It is also the same as the official solution.

        https://leetcode.com/problems/count-primes/discuss/153528/Python3-99-112-ms-Explained%3A-The-Sieve-of-Eratosthenes-with-optimizations

        Splicing is fast. 316 ms, 90% ranking.
        """
        if n <= 2:
            return 0
        sieve = [1] * n
        sieve[0], sieve[1] = 0, 0
        for i in range(2, int(math.sqrt(n)) + 1):
            if sieve[i]:
                sieve[i * i:n:i] = [0] * ((n - 1 - i * i) // i + 1)  # Gauss formula
        return sum(sieve)


sol = Solution3()
tests = [
    (10, 4),
    (0, 0),
    (1, 0),
    (2, 0),
    (3, 1),
    (4, 2),
    (5, 2),
    (6, 3),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countPrimes(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
