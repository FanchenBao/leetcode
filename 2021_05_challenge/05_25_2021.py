# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """LeetCode 150

        Straightforward stack solution. Nothing more to say about it, but it
        is interesting to notice that in Python, -a // b or a // -b equals -1,
        if a < b. I was bitten by this gotcha, and I will take a look online to
        see how is the // defined in Python.

        Found the cause. See SO answer here:
        https://stackoverflow.com/a/5535239/9723036

        Briefly, Python's // performs floor(), thus a -0.xxx turns into -1,
        because -1 is the largest integer that is smaller than -0.xxx

        O(N), 64 ms, 76% ranking.
        """
        stack = []
        op = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a / b),
        }
        for t in tokens:
            if t in op:
                stack.append(op[t](stack.pop(), stack.pop()))
            else:
                stack.append(int(t))
        return stack[0]


sol = Solution()
tests = [
    (['2', '1', '+', '3', '*'], 9),
    (['4', '13', '5', '/', '+'], 6),
    (['10', '6', '9', '3', '+', '-11', '*', '/', '*', '17', '+', '5', '+'], 22),
]

for i, (tokens, ans) in enumerate(tests):
    res = sol.evalRPN(tokens)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
