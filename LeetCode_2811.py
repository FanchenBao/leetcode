# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate
from functools import lru_cache


class Solution1:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        """
        DP, where dp(i, j) is whether it is possible to split
        nums[i:j + 1] into j - i + 1 number of subarrays.

        The tricky part is when nums[i] == nums[j]

        O(N^2), 278 ms, faster than 41.07%
        """
        psum = list(accumulate(nums))

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> bool:
            if j - i <= 1:
                return True
            res = False
            if psum[j] - psum[i] >= m:
                res |= dp(i + 1, j)
            if psum[j - 1] - (psum[i - 1] if i > 0 else 0) >= m:
                res |= dp(i, j - 1)
            return res

        return dp(0, len(nums) - 1)


class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        """
        Inspired by the solution in the forum:

        https://leetcode.com/problems/check-if-it-is-possible-to-split-array/discuss/3869991/Explained-O(n)-oror-Check-consecutive-sum-only

        There must be an adjacent pair whose sum is larger or equal to m to
        make the array splitable.

        If no such adjacent pair exists, there will be no way to split the
        array once it reaches the size of three.

        O(N), 47 ms, faster than 91.96%
        """
        if len(nums) <= 2:
            return True
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] >= m:
                return True
        return False


sol = Solution()
tests = [
    ([1, 2, 1, 1], 4, False),
]

for i, (nums, m, ans) in enumerate(tests):
    res = sol.canSplitArray(nums, m)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
