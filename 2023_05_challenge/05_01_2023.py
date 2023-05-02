# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def average(self, salary: List[int]) -> float:
        """LeetCode 1491

        46 ms, faster than 5.49%
        """
        return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2)
        

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
