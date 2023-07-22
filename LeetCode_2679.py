# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        M, N = len(nums), len(nums[0])
        for row in nums:
            row.sort()
        return sum(max(nums[i][j] for i in range(M)) for j in range(N))

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
