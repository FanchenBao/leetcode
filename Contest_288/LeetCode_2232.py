# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimizeResult(self, expression: str) -> str:
        idx = expression.index('+')
        N = len(expression)
        min_eval, res = math.inf, ''
        for i in range(idx):
            for j in range(idx + 1, N):
                left = expression[:i]
                midleft = expression[i:idx]
                midright = expression[idx + 1:j + 1]
                right = expression[j + 1:N]
                e = int(midleft) + int(midright)
                if left:
                    e *= int(left)
                if right:
                    e *= int(right)
                if e < min_eval:
                    min_eval = e
                    res = left + '(' + expression[i:j + 1] + ')' + right
        return res


sol = Solution()
tests = [
    ("247+38", "2(47+38)"),
    ("12+34", "1(2+3)4"),
    ("999+999", "(999+999)"),
]

for i, (expression, ans) in enumerate(tests):
    res = sol.minimizeResult(expression)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
