# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """LeetCode 878

        If n is small, this problem can be solved by merging two sorted list in
        O(N). However, n is too big for O(N). Thus, intuitively, we need to use
        a solution of O(logN). This means our target solution is most likely
        binary search.

        We can binary search for the multiplier. THe higher bound of multiplier
        at the beginning must be 2 * n. Let's assume a <= b, then we will search
        based on a first. We know mid is the mid-th value in the multiples of a;
        mid * a // b is the (mid * a // b)-th value in the multiples of b; and
        mid * a // lcm is the (mid * a // lmc)-th duplicate values for a, b.
        Thus, the actual count is mid + mid * a // b - mid * a // lcm. If this
        count is larger than n, we shrink on r, otherwise we expand on l.

        If we find the solution during this binary search, that's good.
        Otherwise we know that the solution must not be a multiple of a. Thus,
        we perform the same binary search on b and will be guaranteed to find
        the solution.

        O(logN), 32 ms, 72% ranking.
        """
        lcm = a * b // math.gcd(a, b)
        l, r = 1, 2 * n
        MOD = 10**9 + 7
        a, b = min(a, b), max(a, b)
        # search for l such that l - 1 is too small but l too larger for a
        while l < r:
            ma = (l + r) // 2
            mb = ma * a // b
            md = ma * a // lcm
            if ma + mb - md == n:
                return ma * a % MOD
            if ma + mb - md > n:
                r = ma
            else:
                l = ma + 1
        # Now we know that l from the previous binary search is the upper bound
        # So we will search for b.
        l, r = 1, l
        while l < r:
            mb = (l + r) // 2
            ma = mb * b // a
            md = mb * b // lcm
            if ma + mb - md == n:
                return mb * b % MOD
            if ma + mb - md > n:
                r = mb
            else:
                l = mb + 1
        

class Solution2:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """Math-based solution from the official solution.

        The idea is that if a value x < lcm is a magical number, then x + lcm
        must also be a magical number. Thus, once we have found all magical
        numbers x smaller or equal to lcm, all other magical numbers must be x +
        q * lcm. The number of magical numbers smaller or equal to lcm is L =
        lcm // a + lcm // b - 1. Thus, we can shrink our search range down to
        q, r = divmod(n, L), where lcm * q is the lower bound for the value, and
        the actual value will be found within r iterations.
        """
        MOD = 10**9 + 7
        lcm = a * b // math.gcd(a, b)
        a, b = min(a, b), max(a, b)
        L = lcm // a + lcm // b  - 1
        q, r = divmod(n, L)
        count = L * q
        head_a = head_b = lcm * q
        head_b += b
        while count < n:
            if head_a <= head_b:
                head_a = head_a + a
            else:
                head_b = head_b + b
            count += 1
        return min(head_a, head_b) % MOD


class Solution3:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        """Binary search directly on the result, from the official solution.

        log(N * min(a, b)), 28 ms
        """
        MOD = 10**9 + 7
        lcm = a * b // math.gcd(a, b)
        l, r = 1, min(a, b) * n
        while l < r:
            mid = (l + r) // 2
            if mid // a + mid // b - mid // lcm >= n:
                r = mid
            else:
                l = mid + 1
        return l % MOD


sol = Solution3()
tests = [
    (1, 2, 3, 2),
    (2, 2, 3, 3),
    (3, 2, 3, 4),
    (4, 2, 3, 6),
    (5, 2, 3, 8),
    (6, 2, 3, 9),
    (7, 2, 3, 10),
    (8, 2, 3, 12),
    (9, 2, 3, 14),
    (10, 2, 3, 15),
    (3, 4, 6, 8),
    (5, 2, 4, 10),
    (885, 389, 256, 136928),
    (424674981, 13759, 36659, 612848151),
    (887859796, 29911, 37516, 257511204),
]

for i, (n, a, b, ans) in enumerate(tests):
    res = sol.nthMagicalNumber(n, a, b)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
