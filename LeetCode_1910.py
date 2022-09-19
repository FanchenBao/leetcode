# from pudb import set_trace; set_trace()
from typing import List
import math
import re


class Solution1:
    def removeOccurrences(self, s: str, part: str) -> str:
        """This is probably a cheat by using regex to do the replacement.

        102 ms, faster than 15.51%
        """
        num = 1
        while num:
            s, num = re.subn(part, '', s, count=1)
        return s


class Solution2:
    def removeOccurrences(self, s: str, part: str) -> str:
        """Use string replace directly.

        No regex, much faster

        43 ms, faster than 83.52%
        """
        while True:
            new_s = s.replace(part, '', 1)
            if new_s == s:
                break
            s = new_s
        return s


class Solution3:
    def removeOccurrences(self, s: str, part: str) -> str:
        """From hint, we know that the problem is about stack.

        82 ms
        """
        stack = ''
        N = len(part)
        for le in s:
            stack += le
            if len(stack) >= N and stack[-N:] == part:
                stack = stack[:-N]
        return stack


class Solution4:
    def removeOccurrences(self, s: str, part: str) -> str:
        """Using a real stack

        55 ms, faster than 63.17%. Also faster than string concat and slicing.
        """
        stack = []
        N = len(part)
        for le in s:
            stack.append(le)
            if len(stack) >= N and ''.join(stack[-N:]) == part:
                stack = stack[:-N]
        return ''.join(stack)


sol = Solution4()
tests = [
    ("daabcbaabcbc", "abc", 'dab'),
    ("axxxxyyyyb", "xy", 'ab'),
    ("aabababa", "aba", 'ba'),
]

for i, (s, part, ans) in enumerate(tests):
    res = sol.removeOccurrences(s, part)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
