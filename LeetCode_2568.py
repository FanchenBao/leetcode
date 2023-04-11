# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        """Sort nums first. For any instance where nums[i] - nums[i - 1] > 1,
        we can compute the largest possible integers that can be formed by all
        the consecutive values uptill nums[i - 1], which is the value of the
        same binary size as nums[i - 1] but with all positions being 1.

        Then we check if this largest possible ORed value can continue the
        consecutive trend with nums[i]. If it can, we keep going. If not, we
        have found the answer.

        O(NlogN), 532 ms, faster than 14.12%
        """
        nums.sort()
        pre = i = 0
        while i < len(nums):
            if nums[i] - pre > 1 and pre != 0 and pre != 1:
                # update pre when a consecutive subarray ends
                pre = ((1 << len(bin(pre)[2:])) - 1)
            if nums[i] - pre <= 1:
                if nums[i] - pre == 1:
                    pre = nums[i]
                i += 1
            else:
                return pre + 1
        return 1 << len(bin(nums[-1])[2:])


sol = Solution()
tests = [
    ([1,25,2,72], 4),
    ([5,3,2], 1),
    ([4,2,8,1,87,16,6], 32),
    ([1,3,4,5,6], 2),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minImpossibleOR(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
