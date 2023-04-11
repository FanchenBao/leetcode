# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def isValid(self, s: str) -> bool:
        """LeetCode 20

        Use stack.

        O(N), 28 ms, faster than 86.39%
        """
        stack = []
        paren = {')': '(', '}': '{', ']': '['}
        for le in s:
            if le in paren.values():
                stack.append(le)
            elif stack and stack[-1] == paren[le]:
                stack.pop()
            else:
                return False
        return len(stack) == 0



sol = Solution()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
