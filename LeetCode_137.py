# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def singleNumber(self, nums: List[int]) -> int:
        """LeetCode 137

        Extremely difficult. The link below offers a very detailed explanation
        of the solution.

        https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers

        But I will try to explain it again in my own language. Let's first
        generalize the problem into finding the single p-repeat numbers in a
        list of k-repeat numbers (p % k != 0).

        Let's represent each number as a 32-bit integer. The idea is to count
        the number of occurrences of each bit in the 32 bits. Given a number,
        if its ith bit is a zero, we don't count it. But if it is a one, we
        count it. The counter resets itself when it hits k. Thus for any number
        that has k-repeats, the counter for all its bits will be zero. For the
        single value with p-repeats, since p % k != 0, then the counter for the
        one bit in the single value will record p counts (the zero bit in the
        single value will still record 0 counts).

        Now, let's produce 32 counters, one per bit for the numbers. After going
        through nums and keep counting each bit, we will have 32 counted
        counters. Some of these counters will be zero, some will be p. Say the
        ith counter is 0, that means the ith bit of the single value is 0 (
        because otherwise, we will have counted p in this counter). Thus, the
        only bits in the single value that are one are the bits where the
        counter is p. We can loop through each counter to identify where those
        one bits are and we have the solution.

        Note that Python handles negative value differently. To obtain two's
        complement form of the binary we need to AND the given number with
        (1 << 32) - 1. When the result is obtained, we need to also check
        whether it is a positive or negative value. If it is negative, we need
        to do res - (1 << 32) to obtain the negative form.
        """

        def generic(nums: List[int], k: int, p: int) -> int:
            counters = [0] * 32
            pp = p % k
            twos_mask = (1 << 32) - 1  # for handling two's complement
            limit = (1 << 31) - 1
            for n in nums:
                for i, bit in enumerate(format(n & twos_mask, '032b')):
                    if bit == '1':
                        counters[i] = (counters[i] + 1) % k
            res = int(''.join('1' if c == pp else '0' for c in counters), 2)
            return res if res <= limit else res - (twos_mask + 1)

        return generic(nums, 3, 1)


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        """Now comes the REAL deal, the full bit manipulation approach. The
        general idea is the same as Solution1, but instead of creating 32
        counters, we use m 32-bit integers, where m is the smallest such that
        2^m >= k. Basically, we break down each counter into its binary form,
        with has m bits. Let the m 32-bit integers be x1, x2, ..., xm.

        The ith bit of x1 is the 1st bit of the counter corresponding to the ith
        bit of the given array of integers.

        The ith bit of x2 is the 2nd bit of the counter corresponding to the ith
        bit of the given array of integers.

        The jth bit of x1 is the 1st bit of the counter corresponding to the jth
        bit of the given array of integers.

        etc.

        With this implementation, counting of ith bit in the given number
        is no longer plus one to the ith counter, but bit manipulation to the
        ith bit of x1, x2, ..., xm. If the ith bit of the number is a zero
        none of the ith bit of x1, x2, ..., xm change. If the ith bit of
        the number is a one, the ith bit of xm changes iff the ith bit of x1, x2
        , ..., xm-1, are all ones (think of +1 causing carry to go through every
        previous bit). If any of the previous bits is zero, xm remains unchanged
        This logic can be expressed as

        xm = xm ^ (x1 & x2 & ... & xm-1 & num)

        We use XOR because if xm is currently one, and all the previous bits are
        one, then xm needs to become zero.

        Also note that although we are talking about the ith bit of x1, x2, ...,
        xm, the formula above does not distinguish any particular bits. We are
        performing the same logic to all 32 counters (bits). This is the benefit
        of using a 32-bit integer to represent 32 counters. A single operation
        updates the mth bit of all counters.

        The next challenge is the modulo operation. When we hit k counts, all
        bits of all counters must revert to 0. That is, we need to make x1, x2,
        ..., xm all equal to 0 when we have counted k. The way to achieve this
        is to note that when ith bit in number achieves a count of k, we want to
        create a mask 0, such that when the ith bit of x1, x2, ..., xm AND with
        the mask, they become 0. On the other hand, before the counter reaches
        k, we want the mas to be 1, such that none of the ith bit of x1, x2, ...
        , xm would change. This mask can be created like this: given each bit of
        the binary representation of k', if k' = 1, the individual mask is the
        bit of the current counter. If k' = 0, the individual mask is the
        reverse of the bit of the current counter. We then AND all these
        individual masks and take the reverse of the result to become
        the final mask. This way, when the current
        counter reaches k, all of its bits are equal to k', thus for the
        individual masks, all the one bit remains one and all the zero bits are
        also one. Their AND value is one; its reverse is zero. Thus the final
        mask is zero, as expected. If the current counter is smaller than k,
        then at least one of its bit is not equal to the same bit in k. If this
        bit is one in k, then the current counter has it zero, and the individual
        mask is one. If this bit is zero in k, then the current counter has it
        as one, and the individual mask would be zero. This way, the final mask
        is one, as expected.

        Once all the numbers are scanned, x1, x2, ..., xm represents the m bits
        of counters for each of the 32 bits in the numbers. To find the result,
        we need to identify which of the 32 bits are one in the result. We know
        that the result number must have its one bit counted p times. After
        counting p times, some bit in k must be one. Suppose the rth bit in k
        is one, then if the ith bit in the single number is ONE, the ith bit of
        xr must be one (because the ith bit has total of p counts, and since the
        rth bit in k is one, thus the ith bit in xr must be one). On the other
        hand, if the ith bit in the single numebr is zero, the ith bit of xr
        must also be zero (because none of the single number would contribute to
        the count, and all the other possible contributions come from the k-
        repeats, which are all set to zero after the scan is done). Thus we can
        conclude that the single number is the same as xr. In fact, if the r1th,
        r2th, ..., rrth bit in k is one, then xr1 = xr2 = ... = xrr = single
        numebr.
        """
        # in the current problem, we have k = 3, p = 1. Thus our counter needs
        # two bits.
        x1, x2 = 0, 0
        for n in nums:
            x2 = x2 ^ (x1 & n)
            x1 = x1 ^ n
            mask = ~(x1 & x2)  # k = 3 = b'11'
            x1 &= mask
            x2 &= mask
        return x1  # p = 1 = b'01'. Thus we x1 is the single number


sol = Solution2()
tests = [
    ([2, 2, 2, 3], 3),
    ([0, 1, 0, 1, 0, 1, 99], 99),
    ([-2,-2,1,1,4,1,4,4,-4,-2],-4),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.singleNumber(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
