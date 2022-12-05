# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        """LeetCode 2256

        Keep track of the left and right sum.

        O(N), 1006 ms, faster than 95.91% 
        """
        ls, rs = 0, sum(nums)
        res, min_diff = -1, math.inf
        N = len(nums)
        for i, n in enumerate(nums):
            ls += n
            rs -= n
            cur_diff = abs(
                ls // (i + 1) - ((rs // (N - i - 1)) if N - i - 1 else 0),
            )
            if cur_diff < min_diff:
                res = i
                min_diff = cur_diff
        return res


sol = Solution()
tests = [
    ([2,5,3,9,5,3], 3),
    ([0], 0)
]

for i, (nums, ans) in enumerate(tests):
    res = sol.minimumAverageDifference(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
