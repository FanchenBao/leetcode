# from pudb import set_trace; set_trace()
from typing import List
import math


class BIT:
    def __init__(self, N: int):
        """Initialize a binary indexed tree.

        :param N: The size of the range, including min and max.
        """
        # use 1-based BIT, thus array size must be one larger than the range.
        self.bit = [0] * (N + 1)

    def update(self, pos: int, delta: int) -> None:
        """Update the value at `pos` by adding `delta`.

        Also update all the other ranges that contain `pos`.

        :param pos: The position inside a range whose value needs to be
            updated. Note that this position is one less than the index
            of the self.bit array.
        :param delta: The additional value that needs to be added to
            the value at the given position, and all the other ranges
            including the given position.
        """
        # KEY POINT: BIT index is 1-based, thus its index is one larger
        # than the given position.
        i = pos + 1
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i

    def query(self, max_r: int) -> int:
        """Query the sum of values in the range 0 to `max_r`.

        The meaning of "values" us defined by the `delta` parameter
        in self.update(). It is not necessarily prefix sum.

        :param max_r: The end of the range which we want to query.
        :return: Sum of values in the range 0 to `max_r`.
        """
        # KEY POINT: Bit index is 1-based, thus its index is one larger
        # than the given max range.
        i, res = max_r + 1, 0
        while i:
            res += self.bit[i]
            i -= i & -i
        return res


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        """
        Use BIT to compute the number of elements that are smaller or bigger
        to the left or right of the value currently under consideration.

        O(N * log(MAX)), 122 ms, faster than 82.65%
        """
        M = max(rating)
        bit2 = BIT(M + 1)
        for r in rating:
            bit2.update(r, 1)
        res = 0
        bit1 = BIT(M + 1)
        for r in rating:
            lsmall = bit1.query(r - 1)
            rbig = bit2.query(M) - bit2.query(r) - (bit1.query(M) - bit1.query(r))
            lbig = bit1.query(M) - bit1.query(r)
            rsmall = bit2.query(r - 1) - bit1.query(r - 1)
            res += lsmall * rbig + lbig * rsmall
            bit1.update(r, 1)
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
