# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        """TLE
        """
        if p == 0:
            return 0
        nums.sort()
        dp1, dp2 = [math.inf] * (p + 1), [math.inf] * (p + 1)
        dp1[0] = 0
        dp2[0] = 0
        N = len(nums)
        for i in range(len(nums) - 2, -1, -1):
            tmp = [math.inf] * (p + 1)
            tmp[0] = 0
            for j in range(1, min(p, (N - i) // 2) + 1):
                tmp[j] = min(max(nums[i + 1] - nums[i], dp2[j - 1]), dp1[j])
            dp1, dp2 = tmp, dp1
        return dp1[p]


sol = Solution()
tests = [
    ([10,1,2,7,1,3], 2, 1),
    ([4,2,1,2], 1, 0),
    ([1,1,0,3], 2, 2),
]

for i, (nums, p, ans) in enumerate(tests):
    res = sol.minimizeMax(nums, p)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
