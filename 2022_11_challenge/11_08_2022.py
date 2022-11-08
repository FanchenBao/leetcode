# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def makeGood(self, s: str) -> str:
        """LeetCode 1544

        Use stack.

        O(N), 30 ms, faster than 99.40%
        """
        stack = []
        for le in s:
            if stack and stack[-1] != le and stack[-1].lower() == le.lower():
                stack.pop()
            else:
                stack.append(le)
        return ''.join(stack)


sol = Solution()
tests = [
    ("leEeetcode", 'leetcode'),
    ("abBAcC", ''),
    ('s', 's'),
]

for i, (s, ans) in enumerate(tests):
    res = sol.makeGood(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
