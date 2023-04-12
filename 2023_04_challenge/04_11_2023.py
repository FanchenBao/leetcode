# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def removeStars(self, s: str) -> str:
        """LeetCode 2390

        Use stack. O(N), 221 ms, faster than 85.37%
        """
        stack = []
        for le in s:
            if le == '*':
                stack.pop()
            else:
                stack.append(le)
        return ''.join(stack)


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
