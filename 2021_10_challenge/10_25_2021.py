# from pudb import set_trace; set_trace()
from typing import List
import math


class MinStack:

    def __init__(self):
        """LeetCode 155

        Very disappointed that I needed a hint to solve this easy question. What
        eluded me was the concept of prefix-min.

        64 ms, 68% ranking.
        """
        self.stack = []
        
    def push(self, val: int) -> None:
        if stack:
            self.stack.append((val, min(val, stack[-1][1])))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
