# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import accumulate


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        """85 ms, faster than 34.74%
        """
        leftSum = list(accumulate(nums))
        rs = 0
        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            rs += nums[i]
            res[i] = abs(leftSum[i] - rs)
        return res
        

# sol = Solution2()
# tests = [
#     ("hello", "holle"),
#     ("leetcode", "leotcede"),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.reverseVowels(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
