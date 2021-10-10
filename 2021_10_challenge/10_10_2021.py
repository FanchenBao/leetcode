# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """LeetCode 201

        This is not a hard question. I feel bad that it took so long. It's
        basically bit manipulation. We know that any value larger than left with
        more bits on the left side don't matter. Therefore, all we need to check
        is whether the ones in left can be maintained. To do so, we need to find
        where the one bits are in left, and create the smallest value that will
        have zero at that one bit position. If this smallest value is within
        range, then we know the one bit in left cannot be maintained. Otherwise,
        we can stop searching because all the rest of the one bits at higher
        positions can be maintained.

        For instance, given left = 1001001. To check for the right most one bit,
        we need to see whether 1001010 is within range. To check for the second
        right most one bit, we need to see whether 1010000 is within range.
        Therefore, the algo is basically to figure out how to acquire the value
        for checking.

        O(1) because there are at most 31 position to check in the loop.
        72 ms, 40% ranking.

        UPDATE: from reading the discussion, it is clear that if the number of
        bits in left and right are not the same, the result must be 0. I should
        have realized this. So the updated version adds this extra check which
        can reduce quite a few computation.

        48 ms, 96% ranking
        """
        if left == right:
            return left
        if len(bin(left)) != len(bin(right)):
            return 0
        res, c = left, 0
        while left:
            if left & 1:
                if (res ^ (1 << c)) + (1 << (c + 1)) <= right:
                    res ^= (1 << c)
                else:
                    break
            left >>= 1
            c += 1
        return res


class Solution2:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        """From DBabichev

        Ref: https://leetcode.com/problems/bitwise-and-of-numbers-range/discuss/1514018/Python-O(log-n)-short-solution-explained

        The idea is that for any given left and right pair, we return 0 if the
        number of bits in them are different. If they are the same, that means
        the highest one bit can be maintained. Thus, we reduce left to the
        second highest bit, and reduce the same amount on right as well, then
        recurse.
        """
        if left == right or left == 0:
            return left
        if len(bin(left)) != len(bin(right)):
            return 0
        lmb = 1 << (len(bin(left)) - 3)
        return lmb | self.rangeBitwiseAnd(left - lmb, right - lmb)


sol = Solution2()
tests = [
    (5, 7, 4),
    (0, 0, 0),
    (1, 2147483647, 0),
    (3, 3, 3),
    (0, 1, 0),
]

for i, (left, right, ans) in enumerate(tests):
    res = sol.rangeBitwiseAnd(left, right)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
