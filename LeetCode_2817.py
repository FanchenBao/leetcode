# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        """
        Try binary search
        """
        N = len(nums)
        premax = [nums[0]]
        premin = [nums[0]]
        for i in range(1, N):
            premax.append(max(premax[-1], nums[i]))
            premin.append(min(premin[-1], nums[i]))
        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            for i in range(N - 1, x - 1, -1):
                if premax[i - x] >= nums[i] and premax[i - x] <= nums[i] + mid:
                    break
                if premin[i - x] <= nums[i] and 0 < nums[i] - mid <= premin[i - x]:
                    break
            else:



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
