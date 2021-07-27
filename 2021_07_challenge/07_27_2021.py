# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """LeetCode 16

        We use the same technique as the regular 3Sum problem. We sort the
        nums first, and then fix one value, and use lo and hi pointers on the
        remaining values. If the 3Sum is bigger than target, we shrink on lo,
        otherwise we shrink on hi. At each step, we record the 3Sum if its gap
        to target is smaller than previous.

        O(N^2), 104 ms, 92% ranking.
        """
        nums.sort()
        N = len(nums)
        res, gap = 0, math.inf
        for i in range(N - 2):
            lo, hi = i + 1, N - 1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                if abs(target - s) < gap:
                    res = s
                    gap = abs(target - s)
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    return target
        return res


sol = Solution()
tests = [
    ([-1, 2, 1, -4], 1, 2),
]

for i, (nums, target, ans) in enumerate(tests):
    res = sol.threeSumClosest(nums, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
