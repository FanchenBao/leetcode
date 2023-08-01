# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minLength(self, s: str) -> int:
        """Similar to parenthesis. Use stack

        O(N), 50 ms, faster than 93.23% 
        """
        stack = []
        for le in s:
            if stack and ((stack[-1] == 'A' and le == 'B') or (stack[-1] == 'C' and le == 'D')):
                stack.pop()
            else:
                stack.append(le)
        return len(stack)


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
