# from pudb import set_trace; set_trace()
from typing import List
import math
import operator


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        LeetCode 150

        Stack. Pay attention to the division, because the Python default
        floor division works differently with negative values.

        O(N), 63 ms, faster than 82.29%
        """
        stack = []
        operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: abs(a) // abs(b) * (1 if a * b >= 0 else -1),
        }
        for t in tokens:
            if t not in operators:
                stack.append(t)
            else:
                b, a = int(stack.pop()), int(stack.pop())
                stack.append(operators[t](a, b))
        return int(stack[0])


sol = Solution()
tests = [
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["18"], 18),
]

for i, (tokens, ans) in enumerate(tests):
    res = sol.evalRPN(tokens)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
