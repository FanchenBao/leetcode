# from pudb import set_trace; set_trace()
from typing import List
import sys
import  itertools


class Solution1:
    def getSum(self, a: int, b: int) -> int:
        """The actual bit manupulation is not that hard. But it is very
        convoluted to obtain two's complement in Python. I eventually settled on
        the method of from_bytes and to_bytes to obtain two's complement and
        convert two's complement back to integer.

        Note that the requirement of not using + and - sign also makes two's
        complement difficult to obtain.

        UPDATE: use ~ to get negative values
        """
        # a = int.from_bytes(a.to_bytes(2, sys.byteorder, signed=True), byteorder=sys.byteorder, signed=False)
        # b = int.from_bytes(b.to_bytes(2, sys.byteorder, signed=True), byteorder=sys.byteorder, signed=False)
        mask = (1 << 16) - 1
        MAX = (1 << 15) - 1
        a_or_b = (a | b) & mask
        a_xor_b = (a ^ b) & mask
        res, count, c = 0, itertools.count(), 0
        while a_or_b:
            i = next(count)
            if a_or_b & 1 and a_xor_b & (1 << i):
                res |= (c ^ 1) << i
            else:
                res |= c << i
                c = a_or_b & 1
            a_or_b >>= 1
        res = (res | c << next(count)) & mask
        return res if res <= MAX else ~(res ^ mask)


class Solution2:
    def getSum(self, a: int, b: int) -> int:
        """This is from:

        https://leetcode.com/problems/sum-of-two-integers/discuss/132479/Simple-explanation-on-how-to-arrive-at-the-solution

        Very neat solution. The idea is that a ^ b performs the operation for 
        0 + 1 and 1 + 1 without carry. To find the carry, we use (a & b) << 1
        Then we can XOR (a ^ b) with the carry to produce the next round of
        result. Meanwhile, we can do AND between (a ^ b) and the previous carry
        to produce the next round of carry. These steps repeat each other until
        carry runs out.
        """
        mask = (1 << 16) - 1
        MAX = (1 << 15) - 1
        res, c = a, b
        while c:
            res, c = (res ^ c) & mask, ((res & c) << 1) & mask
        return res if res <= MAX else ~(res ^ mask)


sol = Solution1()
tests = [
    (2, 3, 5),
    (1, 2, 3),
    (123, 654, 777),
    (-2, 3, 1),
    (2, -3, -1),
    (1, -1, 0),
    (-10, -2, -12),
]

for i, (a, b, ans) in enumerate(tests):
    res = sol.getSum(a, b)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
