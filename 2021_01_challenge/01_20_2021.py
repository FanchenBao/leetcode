# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """Standard stack solution. I have done this before.

        O(N), 28 ms, 85% ranking.
        """
        stack = []
        pairs = {')': '(', ']': '[', '}': '{'}
        for le in s:
            if le in {'(', '[', '{'}:
                stack.append(le)
            elif not stack or stack.pop() != pairs[le]:
                return False
        return not stack


sol = Solution()
tests = [
    ('()', True),
    ('[]', True),
    ('{}', True),
    ('()[]{}', True),
    ('(]', False),
    ('([)]', False),
    ('({[]})', True),
    ('(', False),
    (')', False),
    ('[', False),
    (']', False),
    ('{', False),
    ('}', False),
]

for i, (s, ans) in enumerate(tests):
    res = sol.isValid(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
