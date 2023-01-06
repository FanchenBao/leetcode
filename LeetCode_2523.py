# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right, bisect_left


class Solution1:
    def get_primes(self, MIN: int, MAX: int) -> List[int]:
        primes = []
        sieve = [1] * (MAX + 1)
        sieve[0] = sieve[1] = 0
        for i in range(max(4, (MIN + 1) if MIN % 2 else MIN), MAX + 1, 2):
            sieve[i] = 0
        for p in range(3, int(math.sqrt(MAX)) + 1, 2):
            q = max(MIN // p, p)
            if q % 2 == 0:
                q += 1
            while p * q <= MAX:
                sieve[p * q] = 0
                q += 2
        for i in range(MIN, MAX + 1):
            if sieve[i]:
                primes.append(i)
        return primes

    def closestPrimes(self, left: int, right: int) -> List[int]:
        """Use the sieve to get all the primes between left and right. Then
        check consecutive pairs.

        Note that the first time we find a diff of 1 or 2, we can stop the
        search and return the current pair.

        3895 ms, faster than 39.37%
        """
        if left == right or (right - left == 1 and left != 2 and right != 3):
            return [-1, -1]
        primes = self.get_primes(left, right)
        li = bisect_left(primes, left)
        ri = bisect_right(primes, right) - 1
        if ri - li + 1 < 2:
            return [-1, -1]
        min_diff = math.inf
        res = []
        for i in range(li, ri):
            if primes[i + 1] - primes[i] < min_diff:
                min_diff = primes[i + 1] - primes[i]
                res = [primes[i], primes[i + 1]]
            if min_diff == 1 or min_diff == 2:
                break
        return res



PRIMES = []
MAX = 10**6 + 1
sieve = [1] * MAX
sieve[0] = sieve[1] = 0
for i in range(4, MAX, 2):
    sieve[i] = 0
for p in range(3, int(math.sqrt(MAX)) + 1, 2):
    q = p
    while p * q < MAX:
        sieve[p * q] = 0
        q += 2
for i in range(2, MAX):
    if sieve[i]:
        PRIMES.append(i)

class Solution2:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        """Use global primes. Apparently, we cannot set up global prime as a
        member of the Solution class. But we can still prepare primes OUTSIDE
        the class.

        Global primes is the way to go: 859 ms, faster than 67.76%
        """
        if left == right or (right - left == 1 and left != 2 and right != 3):
            return [-1, -1]
        li = bisect_left(PRIMES, left)
        ri = bisect_right(PRIMES, right) - 1
        if ri - li + 1 < 2:
            return [-1, -1]
        min_diff = math.inf
        res = []
        for i in range(li, ri):
            if PRIMES[i + 1] - PRIMES[i] < min_diff:
                min_diff = PRIMES[i + 1] - PRIMES[i]
                res = [PRIMES[i], PRIMES[i + 1]]
            if min_diff == 1 or min_diff == 2:
                break
        return res


sol = Solution2()
tests = [
    (10, 19, [11, 13]),
    (4, 6, [-1, -1]),
    (1, 1000000, [2, 3]),
    (1, 1, [-1, -1]),
    (2, 2, [-1, -1]),
]

for i, (left, right, ans) in enumerate(tests):
    res = sol.closestPrimes(left, right)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
