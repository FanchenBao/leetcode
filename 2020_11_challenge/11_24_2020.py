# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import deque


class Solution1:

    def get_num(self, exp_str, i) -> Tuple[int, int]:
        n = 0
        while i < len(exp_str):
            if '0' <= exp_str[i] <= '9':
                n = n * 10 + int(exp_str[i])
            elif exp_str[i] in ['/', '*', '+', '-']:
                break
            i += 1
        return n, i - 1

    def calculate(self, s: str) -> int:
        """14% ranking. Kinda slow"""
        stack = deque()
        i = 0
        while i < len(s):  # parse s and compute division and multiplication
            if '0' <= s[i] <= '9':
                n, i = self.get_num(s, i)
                stack.append(n)
            elif s[i] in ['/', '*']:
                op = s[i]
                n, i = self.get_num(s, i + 1)
                prev_n = stack.pop()
                stack.append(prev_n // n if op == '/' else prev_n * n)
            elif s[i] in ['+', '-']:
                stack.append(s[i])
            i += 1
        while len(stack) > 1:  # compute add and minus
            n1 = stack.popleft()
            op = stack.popleft()
            n2 = stack.popleft()
            stack.appendleft(n1 - n2 if op == '-' else n1 + n2)
        return stack[0]


class Solution2:

    def get_num(self, exp_str, i) -> Tuple[int, int]:
        n = 0
        while i < len(exp_str):
            if '0' <= exp_str[i] <= '9':
                n = n * 10 + int(exp_str[i])
            elif exp_str[i] in ['/', '*', '+', '-']:
                break
            i += 1
        return n, i - 1

    def helper(self, exp: str, i: int, is_rev: bool) -> int:
        stack = []
        while i < len(exp):  # parse s and compute division and multiplication
            if '0' <= exp[i] <= '9':
                n, i = self.get_num(exp, i)
                stack.append(n)
            elif exp[i] in ['/', '*']:
                op = exp[i]
                n, i = self.get_num(exp, i + 1)
                prev_n = stack.pop()
                stack.append(prev_n // n if op == '/' else prev_n * n)
            elif exp[i] in ['+', '-']:
                op = exp[i]
                n = self.helper(exp, i + 1, op == '-')
                prev_n = stack.pop()
                if is_rev:
                    stack.append(prev_n + n if op == '-' else prev_n - n)
                else:
                    stack.append(prev_n - n if op == '-' else prev_n + n)
                break
            i += 1
        return stack[0]

    def calculate(self, s: str) -> int:
        """7% ranking. Use recursion is even worse."""
        return self.helper(s, 0, False)


class Solution3:

    def calculate(self, s: str) -> int:
        """Assume the + and - operation is always +, and put - to the number
        to form negative numbers.

        98% ranking. We can keep accumulating the numbers in the same main
        loop. There is no need to have a separate function for it.
        """
        stack = []
        num = 0
        op = '+'  # previous operation
        for le in s + '+':
            if le.isdigit():
                num = num * 10 + int(le)
            elif le in '-+*/':
                if op in '-+':
                    stack.append(num if op == '+' else -num)
                else:
                    prev_n = stack.pop()
                    stack.append(int(prev_n / num) if op == '/' else prev_n * num)
                op = le
                num = 0
        return sum(stack)


class Solution4:

    def calculate(self, s: str) -> int:
        """Space-optimized from Solution 3. No stack needed. 96% ranking."""
        res, cur_n, prev_n = 0, 0, 0
        op = '+'  # previous operation
        for le in s + '+':
            if le.isdigit():
                cur_n = cur_n * 10 + int(le)
            elif le in '-+*/':
                if op in '-+':
                    res += prev_n
                    prev_n = cur_n if op == '+' else -cur_n
                else:
                    prev_n = int(prev_n / cur_n) if op == '/' else prev_n * cur_n
                op = le
                cur_n = 0
        return res + prev_n


sol = Solution4()
tests = [
    ('3+2*2', 7),
    (' 3/2 ', 1),
    (' 3+5 / 2 ', 5),
    ('14/3*2', 8),
    ('3', 3),
    ("1-1+1", 1),
    ("14-3/2", 13),
]

for i, (s, ans) in enumerate(tests):
    res = sol.calculate(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
