# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def arraySign(self, nums: List[int]) -> int:
        """LeetCode 1822

        67 ms, faster than 25.47%
        """
        has_zero = False
        num_neg = 0
        for n in nums:
            if n == 0:
                has_zero = True
            elif n < 0:
                num_neg += 1
        if has_zero:
            return 0
        return -1 if num_neg % 2 else 1


class Solution2:
    def arraySign(self, nums: List[int]) -> int:
        """From the official solution. Track the sign
        """
        sign = 1
        for n in nums:
            if n == 0:
                return 0
            if n < 0:
                sign *= -1
        return sign


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
