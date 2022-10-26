# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        """Prefix max on the left side, prefix min on the right side. We go
        from right to left, compare to the max on the left and min on the right
        to decide the score of the current value.

        O(N) time, O(N) space, 3412 ms, faster than 12.44%
        """
        premax = [nums[0]]
        for i in range(1, len(nums)):
            premax.append(max(premax[-1], nums[i]))
        res = 0
        premin = nums[-1]
        for j in range(len(nums) - 2, 0, -1):
            if premax[j - 1] < nums[j] < premin:
                res += 2
            elif nums[j - 1] < nums[j] < nums[j + 1]:
                res += 1
            premin = min(premin, nums[j])
        return res


sol = Solution()
tests = [
    ([1,2,3], 2),
    ([2,4,6,4], 1),
    ([3,2,1], 0),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.sumOfBeauties(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
