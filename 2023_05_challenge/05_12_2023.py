# from pudb import set_trace; set_trace()
from typing import List
import math
from functools import lru_cache


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        """LeetCode 2140

        The sentence "solve or skip each question" is a strong signal that this
        problem shall be solved using DP.

        O(N), 1745 ms, faster than 33.34%
        """
        N = len(questions)

        @lru_cache(maxsize=None)
        def dp(idx: int) -> int:
            if idx >= N:
                return 0
            op1 = questions[idx][0] + dp(idx + questions[idx][1] + 1)
            op2 = dp(idx + 1)
            return max(op1, op2)

        return dp(0)


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
