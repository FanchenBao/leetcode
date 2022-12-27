# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """LeetCode 55

        DP. We record the earliest position from nums[i + 1, ... N - 1] that can
        reach the end. Thus, at nums[i], all we need to check is whether i +
        nums[i] can reach the earliest position.

        O(N), 468 ms, faster than 97.81%
        """
        N = len(nums)
        earliest = N - 1
        for i in range(N - 2, -1, -1):
            if i + nums[i] >= earliest:
                earliest = i
        return earliest == 0


sol = Solution()
tests = [
    ([2,3,1,1,4], True),
    ([3,2,1,0,4], False),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.canJump(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
