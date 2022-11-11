# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def removeDuplicates(self, s: str) -> str:
        """LeetCode 1047

        Use stack

        O(N), 156 ms, faster than 65.04% 
        """
        stack = []
        for le in s:
            if stack and stack[-1] == le:
                stack.pop()
            else:
                stack.append(le)
        return ''.join(stack)


sol = Solution()
tests = [
    ("abbaca", 'ca'),
    ("azxxzy", 'ay'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.removeDuplicates(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
