# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(d[11:13]) > 60 for d in details)


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
