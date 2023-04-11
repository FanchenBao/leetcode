# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        """Sort nums and try all possible modifications. Either we chang the
        smallest and largest to the second smallest and second largest, or we
        change the smallest and second smallest to the third smallest, or we
        change the largest and second largest to the third largest. No other
        change needs to be considered.

        O(NlogN), 343 ms, faster than 71.05%
        """
        nums.sort()
        return min(nums[-2] - nums[1], nums[-1] - nums[2], nums[-3] - nums[0])
        

sol = Solution()
tests = [
    ([43,345,45,657,65,43,4,567,86,5,78976,543,42,567,865,4,367,5], 653),
    ([1,2,3,10,1000,10000], 9)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimizeSum(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
