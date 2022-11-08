# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def removeStars(self, s: str) -> str:
        """LeetCode 2390

        Use stack

        O(N), 249 ms, faster than 90.33%
        """
        stack = []
        for le in s:
            if stack and le == '*':
                stack.pop()
            else:
                stack.append(le)
        return ''.join(stack)


sol = Solution()
tests = [
    ("leet**cod*e", "lecoe"),
    ("erase*****", ""),
]

for i, (s, ans) in enumerate(tests):
    res = sol.removeStars(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
