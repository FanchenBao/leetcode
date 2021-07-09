# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
import math


class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """LeetCode 300

        The goal is to record the smallest value in nums that is the end of
        any length of LIS. We can keep these smallest values in an array, with
        the array index being the length of LIS corresponding to each value.

        Since this array must also be sorted (this can be proved like this:
        suppose we have dp[4] = 9 and dp[3] = 10, which means 9 is the smallest
        end to an LIS of length 4, whereas 10 is the smallest end to an LIS of
        length 3. This is not possible, because if 10 occurrs after 9, then we
        shall have dp[5] = 10. If 10 occurrs before 9, then we shall have dp[3]
        = 9. Therefore, the dp array must be sorted), we can binary search this
        array to find where the current value is going to be located. If the
        current value is the largest, we simply append it to the end. Otherwise,
        we replace the value in dp that is just larger than the current value,
        because the current value can achieve the same LIS length as the value
        just larger. If the current value is a repeat, then we discard it.

        O(Nlog(N)), 92 ms, 78% ranking.
        """
        dp = [-math.inf]
        for n in nums:
            if n > dp[-1]:
                dp.append(n)
            else:
                idx = bisect_right(dp, n)
                if dp[idx - 1] != n:
                    dp[idx] = n
        return len(dp) - 1


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
            self.bit[i] = max(self.bit[i], delta)
            i += (i & -i)

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
            res = max(res, self.bit[i])
            i -= (i & -i)
        return res


class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """BIT solution following this:

        https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/Python-DP-BIT-Solutions-Clean-and-Concise-O(NlogN)

        This is not a prefix sum BIT, but a prefix max BIT. Each query returns
        the longest LIS ending in a given value (starting with min value). This
        way, we can obtain the length of LIS of current value minus 1, and
        derive the longest LIS of the current value.

        I was having issue figuring out the logic inside BIT. I thought we will
        keep the longest LIS of each segment, which will then require addition
        when doing query and update. But this is not correct, because each
        index shall hold the longest LIS directly. Hence, there is no addition.

        Keep in mind, BIT (or segment tree) obtains the sum, min, or max of a
        range. In our case, we shall get the max of a range.
        """
        N = 2 * 10**4 + 1
        BASE = 10**4
        bit = BIT(N)
        for n in nums:
            pre_len = bit.query(n - 1 + BASE)
            bit.update(n + BASE, pre_len + 1)
        return bit.query(2 * BASE)


sol = Solution2()
tests = [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1),
    ([1], 1),
    ([5, 4, 3, 2, 1], 1),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.lengthOfLIS(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
