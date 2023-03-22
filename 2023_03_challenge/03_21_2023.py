# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution1:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """LeetCode 2348

        Find the count of each segment of consecutive zeros.

        Maybe more than O(N), depending on how slow list() is. Judging on the
        time, it does not seem to be fast.

        1137 ms, faster than 35.69%
        """
        res = 0
        for k, g in groupby(nums):
            n = len(list(g))
            res += int(k == 0) * n * (n + 1) // 2
        return res


class Solution2:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """Not using groupby

        O(N), 1078 ms, faster than 81.98%
        """
        zeros = res = 0
        for i, n in enumerate(nums):
            if n:
                res += zeros * (zeros + 1) // 2
                zeros = 0
            else:
                zeros += 1
        res += zeros * (zeros + 1) // 2
        return res


sol = Solution2()
tests = [
    ([1,3,0,0,2,0,0,4], 6),
    ([0,0,0,2,0,0], 9),
]

for i, (nums, ans) in enumerate(tests):
    res = sol.zeroFilledSubarray(nums)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
