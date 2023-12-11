# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        """
        Count the number of 0s in between any two 1s. The number of dividers
        that one can put in between the two 1s is the number of 0s plus 1. Then
        we just need to multiple all these numbers of dividers between any
        consecutive pairs of 1s.

        O(N), 1944 ms, faster than 83.07%
        """
        MOD = 1000000007
        res = 1
        pre = 0
        while pre < len(nums) and nums[pre] == 0:
            pre += 1
        if pre == len(nums):  # there is no 1s in nums
            return 0
        for i in range(pre + 1, len(nums)):
            if nums[i] == 1:
                res = (res * (i - pre)) % MOD
                pre = i
        return res


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
