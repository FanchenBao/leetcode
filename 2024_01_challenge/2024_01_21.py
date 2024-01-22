# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        LeetCode 198

        One of the classic entry level DP problems.

        O(N), 40 ms, faster than 46.58%
        """
        N = len(nums)
        if N == 1:
            return nums[0]
        pp, p = nums[0], max(nums[1], nums[0])
        for i in range(2, N):
            pp, p = p, max(p, pp + nums[i])
        return p


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
