# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        """O(MN), 128 ms, faster than 86.97%
        """
        es = sum(nums)
        ds = 0
        for n in nums:
            while n:
                ds += n % 10
                n //= 10
        return abs(es - ds)


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
