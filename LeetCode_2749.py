# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        I think this is a good problem. Took me quite some efforts.

        What we want to find is the smallest k such that
        num1 - (2^i0 + 2^i1 + ... + 2^ik) = k * num2

        This means we want to find a way to break num1 - k * num2 into k binary
        values all in the form of 100..000

        Apparently, if num1 - k * num2 is negative, it is not possible.

        Otherwise, the min k for any num1 - k * num2 is the number of bits in
        that value. Thus, if the number of bits is equal to k, we have found k.

        If the number of bits is larger than k, it is not possible. We have to
        increment k.

        If the number of bits is smaller than k, then we can decompose each bit
        into 2 more bits. This means for a pth bit, it can be decomposed into
        2^p - 1 bits. So we simply try to obtain the max number of bits
        decomposable. And as long as that value is larger than k, we have found
        the answer.
        
        37 ms, faster than 73.08%
        """
        k = 1
        while (tmp := (num1 - k * num2)) >= 0:
            bitcount = tmp.bit_count()
            if bitcount == k:
                return k
            if bitcount < k:
                bin_tmp = bin(tmp)[2:]
                decomp_bits = 0
                for i, b in enumerate(bin_tmp):
                    if b == '1':
                        decomp_bits += (1 << (len(bin_tmp) - i)) - 1
                        if decomp_bits >= k:
                            return k
            k += 1
        return -1


class Solution2:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Inspired by lee215

        https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/discuss/3679281/JavaC%2B%2BPython-Bit-count-4-lines

        He pointed out that the max possible k given num1 + k * num2 is the
        value num1 + k * num2 itself, because it can be broken down into 1 + 1
        + 1 + ... + 1, in total num1 + k * num2 ones.

        31 ms, faster than 97.12%
        """
        k = 1
        while (max_k := (num1 - k * num2)) >= 0:
            min_k = max_k.bit_count()
            if min_k <= k <= max_k:
                return k
            k += 1
        return -1



sol = Solution2()
tests = [
    (71, -13, 5),
    (135, 26, 5),
]

for i, (num1, num2, ans) in enumerate(tests):
    res = sol.makeTheIntegerZero(num1, num2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
