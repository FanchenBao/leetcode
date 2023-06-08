# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """LeetCode 1318

        Check the positions one by one.

        48 ms, faster than 37.80%
        """
        res = 0
        for aa, bb, cc in zip(f'{a:030b}', f'{b:030b}', f'{c:030b}'):
            if cc == '1':
                if aa == '0' and bb == '0':
                    res += 1
            else:
                if aa == '1' and bb == '1':
                    res += 2
                elif aa == '1' or bb == '1':
                    res += 1
        return res


class Solution2:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """This is the first solution from the official solution. We also go
        bit by bit, but we don't convert the stirng to binary. Instead, we
        simply check each bit from right to left and shift the values to the
        right.
        """
        res = 0
        while a or b or c:
            aa, bb, cc = a & 1, b & 1, c & 1
            if cc == 1:
                if aa | bb == 0:
                    res += 1
            else:
                if aa & bb == 1:
                    res += 2
                elif aa | bb == 1:
                    res += 1
            a >>= 1
            b >>= 1
            c >>= 1
        return res


class Solution3:
    def minFlips(self, a: int, b: int, c: int) -> int:
        """This is the second solution from the official solution. We perform
        pure bit analysis.

        We do a | b and compare it to c. Whichever bits that are the same, we
        don't have to manipulate. We only need to manipulate the bits that are
        different between a | b and c. To locate the positions of the different
        bits, we can do (a | b) ^ c. Then all the positions with 1 are the bits
        that require manipulation.

        Furthermore, if at a bit, c has zero yet both a and b have one, that
        would require two flips. Therefore, we need to obtain all the positions
        in a and b that are both ones. This can be done via a & b. Then we AND
        that result with (a | b) ^ c. Any one bit after that must be the bits
        that require two flips.
        """
        to_flip, both_one = (a | b) ^ c, a & b
        return (both_one & to_flip).bit_count() + to_flip.bit_count()


sol = Solution3()
tests = [
    (2, 6, 5, 3),
    (4, 2, 7, 1),
    (1, 2, 3, 0),
]

for i, (a, b, c, ans) in enumerate(tests):
    res = sol.minFlips(a, b, c)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
