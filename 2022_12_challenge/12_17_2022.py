# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def evalRPN(self, tokens: List[str]) -> int:
        """LeetCode 150

        Stack. The difficult part is handling division given negative values.

        O(N), 75 ms, faster than 84.55%
        """
        res = 0
        stack = []
        ops = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: abs(a) // abs(b) * (1 if a * b >= 0 else -1),
        }
        for t in tokens:
            if t.isdecimal() or (t[0] == '-' and len(t) > 1):
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                stack.append(ops[t](a, b))
        return stack[-1]


class Solution2:
    def evalRPN(self, tokens: List[str]) -> int:
        """Actually it is not difficult handling the division. All we need to
        do is int(a / b)

        71 ms, faster than 90.29%
        """
        stack = []
        ops = {
            '+': lambda b, a: a + b,
            '-': lambda b, a: a - b,
            '*': lambda b, a: a * b,
            '/': lambda b, a: int(a / b),
        }
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                stack.append(ops[t](stack.pop(), stack.pop()))
        return stack[-1]


sol = Solution2()
tests = [
    (["2","1","+","3","*"], 9),
    (["4","13","5","/","+"], 6),
    (["10","6","9","3","+","-11","*","/","*","17","+","5","+"], 22),
    (["10"], 10),
    (["4","-2","/","2","-3","-","-"], -7),
]

for i, (tokens, ans) in enumerate(tests):
    res = sol.evalRPN(tokens)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
