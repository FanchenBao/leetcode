# from pudb import set_trace; set_trace()
from typing import List
import math
from operator import add


class Solution:
    def calculate(self, s: str) -> int:
        """LeetCode 224

        Use cur_num to hold onto the current number in view. Once we hit an
        operator or a right paren, we decide how to combine the current number
        with whatever is already on the stack.

        If the current element is an operator, it is guaranteed that the top
        of the stack is either a left paren, stack is empty, or another opeartor
        We handle each situation accordingly.

        If the current element is a left paren, we push it to stack.

        If the current element is a right paren, there is a trap here. The top
        of the stack could be a left paren, corresponding to edge cases like
        this: "(1)", or an operator. We need to handle each situation separately

        O(N), 155 ms, faster than 68.21% 
        """
        cur_num = 0
        stack = []
        s += '+'  # this allows the loop to handle all situations
        ops = {'+': add, '-': lambda a, b: add(a, -b)}
        for i in range(len(s)):
            if s[i] == ' ':
                continue
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == '+' or s[i] == '-':
                if not stack or stack[-1] == '(':
                    stack.append(cur_num)
                    stack.append(s[i])
                else:  # top of stack is '+' or '-'
                    op = stack.pop()
                    a = stack.pop()
                    stack.append(ops[op](a, cur_num))
                    stack.append(s[i])
                cur_num = 0
            elif s[i] == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    op = stack.pop()
                    a = stack.pop()
                    stack.pop()  # pop the left paren
                    cur_num = ops[op](a, cur_num)
            elif '0' <= s[i] <= '9':
                cur_num = cur_num * 10 + int(s[i])
        return stack[0]


sol = Solution()
tests = [
    ("1 + 1", 2),
    (" 2-1 + 2 ", 3),
    ("(1+(4+5+2)-3)+(6+8)", 23),
    ("( -123  + ( -14  + (-225 - 78)  + 25 )  - (4333 - 123)  ) +  (226+ 678 )", -3721),
    ('(1)', 1),
]

for i, (s, ans) in enumerate(tests):
    res = sol.calculate(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
