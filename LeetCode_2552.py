# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i, n in enumerate(nums):
            stack = [n]
            for j in range(i + 1, N):
                while 

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
