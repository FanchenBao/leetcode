# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        """
        479 ms, faster than 58.12% 
        """
        return sorted(score, key=lambda row: -row[k])

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
