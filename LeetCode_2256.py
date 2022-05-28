# from pudb import set_trace; set_trace()
from typing import List
from itertools import accumulate
import math


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """O(N) time and O(1) space.

        We can use prefix sum, but this method does not even need to set up a
        prefix sum array.

        961 ms, faster than 98.42%
        """
        N = len(nums)
        l, r = 0, sum(nums)
        dif, idx = math.inf, -1
        for i in range(N - 1):
            l += nums[i]
            r -= nums[i]
            d = abs(l // (i + 1) - r // (N - i - 1))
            if d < dif:
                dif = d
                idx = i
        return idx if dif <= (l + nums[-1]) // N else N - 1


sol = Solution()
tests = [
    ([2,5,3,9,5,3], 3),
    ([0], 0),
    ([1,2,3,4,5], 0)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumAverageDifference(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
