# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """LeetCode 976

        Sort nums, and try the largest three values. If they can form a
        triangle, we are done. Otherwise, pop the largest, and try again.

        O(NlogN), 399 ms, faster than 47.02%
        """
        nums.sort()
        while len(nums) > 2:
            if nums[-3] + nums[-2] > nums[-1]:
                return nums[-3] + nums[-2] + nums[-1]
            nums.pop()
        return 0


sol = Solution()
tests = [
    ([2,1,2], 5),
    ([1,2,1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.largestPerimeter(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
