# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        """
        We go from right to left. As long as the value/sum on the right is
        larger than the last element in nums, we can add them together. If
        the sum from right to left cannot overpower whatever is the last
        element in nums, then we have to restart.

        O(N), 671 ms, faster than 98.54%
        """
        res = 0
        cur = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] <= cur:
                cur += nums[i]
            else:
                res = max(res, cur)
                cur = nums[i]
        return max(res, cur)


sol = Solution()
tests = [
    ([2,3,7,9,3], 21),
    ([5,3,3], 11),
    ([40,15,35,98,77,79,24,62,53,84,97,16,30,22,49], 781),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.maxArrayValue(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
