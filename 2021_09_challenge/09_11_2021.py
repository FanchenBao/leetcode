# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import deque
import operator


class Solution1:
    def transform(self, s: str):
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ' ':
                if s[i] in {'(', ')', '+', '-'}:
                    stack.append(s[i])
                else:
                    j = i + 1
                    while j < len(s) and '0' <= s[j] <= '9':
                        j += 1
                    stack.append(int(s[i:j]))
                    i = j - 1
            i += 1
        return stack[::-1]

    def calculate(self, s: str) -> int:
        """LeetCode 224

        This does not seem to be a hard question. There is no specific trick.
        We first transform the original string s into a stack where we eliminate
        all the white spaces and convert each number token (tokenization). Then
        we reverse this stack so that we can perform all operations on its tail.

        Then we build another stack for computation. The rule is if we encounter
        a left paren or plus, we push it into the stack. If we encounter a minus
        we first check whether top of stack is a number. If it is, the minus
        must be an operator. Otherwise, the minus is a unary operator, in which
        case we simply push a zero to the stack. Then we push the minus onto 
        the stack as well. If we encounter a number, we check top of stack as
        well. If it is an operator, we perform operation with the number that
        is second to the top on the stack. We then push the result back into the
        stack. If the top of stack is not a number, we push the current number
        in. Finally, if we encounter a right paren, it is guaranteed that the
        top of stack is a number and second top a left paren. We pop the top and
        push it to the transformed stack, and then pop the left paren. Then we
        continue. This probably is the only trick involved.

        O(N), 168 ms, 17% ranking
        """
        rev_s = self.transform(s)
        stack = []
        ops = {
            '+': lambda a, b: operator.add(a, b),
            '-': lambda a, b: operator.sub(a, b),
        }
        while rev_s:
            cur = rev_s.pop()
            if cur in {'(', '+'}:
                stack.append(cur)
            elif cur == '-':
                if not stack or not isinstance(stack[-1], int):
                    stack.append(0)
                stack.append(cur)
            elif isinstance(cur, int):
                if not stack or stack[-1] not in {'+', '-'}:
                    stack.append(cur)
                else:
                    op = stack.pop()
                    stack.append(ops[op](stack.pop(), cur))
            elif cur == ')':
                rev_s.append(stack.pop())
                stack.pop()  # pop the left parenthesis
        return stack[0]


class Solution2:
    def calculate(self, s: str) -> int:
        """This is a generic solution to handle not only plus minus and paren,
        but also multiple and divide. This is from DBabichev. He has a very
        unique way of using stack to separate a non-paren expression based on
        plus and minus operation, and group the multiply and divide in each
        element of the stack. When encountering a parenthesis, he just use
        recursion to avoid all the complexity.

        Ref:

        https://leetcode.com/problems/basic-calculator/discuss/1456850/Python-Basic-Calculator-I-II-III-easy-solution-detailed-explanation
        """
        N = len(s)

        def update(op: str, val: int, stack: List[int]) -> None:
            if op == '+':
                stack.append(val)
            elif op == '-':
                stack.append(-val)
            elif op == '*':
                stack.append(stack.pop() * val)
            elif op == '/':
                stack.append(stack.pop() // val)

        def helper(i: int) -> Tuple[int, int]:
            stack, op, num = [], '+', 0
            while i < N:
                if s[i].isdigit():
                    num = 10 * num + int(s[i])
                elif s[i] in '+-*/':
                    update(op, num, stack)
                    op, num = s[i], 0
                elif s[i] == '(':
                    num, j = helper(i + 1)
                    i = j
                elif s[i] == ')':
                    update(op, num, stack)
                    return sum(stack), i
                i += 1
            update(op, num, stack)
            return sum(stack), i

        return helper(0)[0]


sol = Solution2()
tests = [
    ('1 + 1', 2),
    (' 2-1 + 2', 3),
    ('(1+(4+5+2)-3)+(6+8)', 23),
    ('(9-(10-(10-0-(3+(8+(0+(8-(10-8-(7-(2+(5+(6+(10+(3+(8+(3-(9+(1+(10+(1-(1+(6-2+0+(10-(9-(3-(3-9-(1-(7+(4-(2+(2-(10+(3+(7-(1-(4+(1+(1-(10-(5-(9+(9-4-(5-(1+8-(2-(1+(1-10-(4-(1+(4-(7)-(3-(8)+(5+5-(5-(9-(8+(8-4-1+(0-(1+(1+(10-(7+(2-(5-(4-(6+(2+(1-(2-(9+8+(2+(9-(9-(7+(10+1+(5)))-(2-(8+3+(5-(7-(3+(9)+(10+(0+(8-(1-(9)-(0+10-(3+(9-(0-(5-(7-(4-4+1+(7)-(10+(5+(9-(3+(5+(6-(0-(7-(1-(4+(6+(4-2-(4+(9-(6+9-8+1+(5+(7-9+3)+(10-(10+(2+(0-(5-(2+(10-(4-5-(7-(4-(7+(4)+6+10+(2-(7+(2))+(1)+(5-(7)-(10-(5+(7-(6-(2+(1-4)+(10-(5)+(4+(10+(4+(0+(10+(8-(8+(6+5-(1-(6-(1-(2+(4+(9-(3+(1+(10+(4)+(0+(3-(2-(9-(2-(3-(4-(2+(7-(6-(5+(7+(5+(5-(4+(0-(7+(2-(7+(9)-(6-(10)+(7+(2-(9-(9)+(4+(1-(8+(2-0-(2+(2+10)-(7-9-(9+(8-(5-8-(5)+(6+(10-(3-(2-(2+(7-2+(9+(3+(9+(2-(8+(5-(4+(4-(1-(9+(0+(6-(4-(3+(5-(2-(4-(6+(0+(4+3)-(8-(6+(9+(1+(2)-(8-(1+1+(5+(4-(3-(1-(7-4+(6+(9+(1+(4)+(6+(4+(2+(7-(1+(4-(8+(6+(8-(9-(2)-3-(0-(0)+(5+(7-(8)+(8-(2+(1)+1+(3+(6-(10-(2-4-(2-(2)+(8)+(3-(1-(1)+(6+(1+(9+(9+(5)-(4+(9+(10)+(0-(3+(3+0)+(6)-(6+(6)+(4-(8-1-5-(6)-(0))-(3)+(3-(3-(8-(10-(0-(4+(7)+(6-4))+1-(2-(1-(0-(0+(1-(0)-0+(5+(10-(2-(9-(9-10)+(3+(5-(6-(6-9-(5+5))+(7+(0)-(2-(7+2+(7-(2+(7+(4-(10+(4+(10-(3-(0-2+(9+(4-4-(3-(2)+(8+(5)+(1+1-(7+(3+(10+5-(0+(10-(9+(8-(0-(0+(8-(1+(0)+(6+(5+(5+(9)))+(4-(1-(3+(7+(9+(8-(1-8-(8+(0+(1+(1-(1)+(7+(6-(7-(8+(10)+1+(0-(10)+(8+(7+(10+(6+(10+(6)-(2+(2+(10-(8)-(5)))+(9-(1)+(4)+(5)-(6-(9)-(1+(6-(9+(10)+2-(4+(9-(4+1)-(0-(9)-(3)+(0)+(10)))+9)+(6+4+(6))+(5-(9))-(9-(2-(6+(7))-(6-(3+(5+(5-(0)-(5+(6-(5+(9-(2+(9+(1+(0+2+(7)-(3-(5+(2)+(4)+(6+(7-(3-(4)+(10+(4))+(3))-(3-(2)-(2+(2+(10+(3)+(3+(5)-(3-(0+(1)+(6+(4-(4)-(7-(9-(9)+(1)+(4)+(7))-(9))))-(3-(1+5-7-(7))-(4+(3+(7-(9+(8)-(9+(8-(3)+(10-(1)+(5)-(2-(4)+(0-(10-(7-(10+(1)+(1)-(4)-(10)))+(7)+(4-4)+0+9-(6))-(6+(5)))))-(8-(6)-(10+(5-(8)-(10+(3+(0+(6-(9)-(1)))-(0)-(9+(0+(1+(8+2-(4-(9-(4+(3+4)-(10+(1-(5)+(10-(4-(6-(4-(2+(4)-(9)-(4))))-3))))+(9)+(9+(0-(1+(5-(5+(7)-6-(8-(3-(3+(1)-(9-(7-(6)))-(2+(1))-(1+(2+(10))))+(6)+(0+(9-(1)-(10)))+(10-(1-(1)))-(0+(0-(2-(4-(6+(1))+(0)+(5)-(5+(5)-(4+(6)-(5)+(1-(7))))+(8)-(7))-3))-(7+(7+(9+(0+(10)-(7-(0-(2)-(6))-(2+(10)))+(7)+(3))+(8-(8+(10)-(8)+(0+(6-(2)-(1))+(3+(10+(10-(4+(7-(2)-(9-(2+(8))))+(7)-(7+10+(9-(2)+(0))-(6+(1)))+(10)+(2)-(7)-(4)-(10+(3-(6))))+(8-(1))-(10)))+(5+(3-(0-(1-(2+(3-(6-(4)-(1)+(4+(7+(3)-(7)+(4-(9))+(0-(4)+(9+(3-(9)+(4-(10+(6+(4)))+(4))+(10+(0-3-(8+(0-(6))-(5))-(9))-(6))))+2))+6+(6)+(1-(6))-(7-(1))-(8)+(9-(8))+(4)))-(0+7-(1)))-(2))+(0)))+(4-(7))-(5)-(8)-4+(1-(3-(8+(2+0)+(7)))))))-(4-(2))+(9))))+(7)-(2-(10+(4)-(8+(7)+(5-(4)-(6+6))-(2+(6)-(2+(4-(2-(8-(4)-(7+(5)-(10-(7)))))-(10+(9+(8)-(10)+(3-(7+(4+(2+(5)-(10+7+(2-(10)-(10+(3))+(0-(10+(8+(4+(7-(2)+(3+9))))+(7-(6+(2)-(2)+7+(5+(7+(10+(5-(4)-2+(5)+(1))+(0))))-(9))-5-(8)-(9-(4)-(10))-(8-(5)-(10)-7)+(5))-(4)))))+6+3+(3+(6+(9)))-10+(6)+(0)))))+(7)))+(1-(5)+(3-(3+6))+(5)+(7)-(9-(1))+(4+(1))+(2)))-(3))-(10)+(1)))))))))+(3)+2+(8-(4)))-(1))+(6-(8-(0)-(8-(0))-(2-(4+2)))-(9+1)))-(8-(8+(1-8-(7))))+7-(5+(5+(6+(10)+(8)))))))-(4))))-(4)-(6)+(10)-(5)))+(0+(2+(4))-(4-(2)+(0-(10-(4))))))+3-(10)))-(9+(9-(8-(7)-4))))+(6))-(4-(9))))-(1))+(10))))-(0+(9+7-(1)))))-(7)-(4)))-(9))))-7))))+(9))+(10))-(8-(9)))+(8))-(6)-(4)-(8)))))))))))))-(7)))))+(2-(6)-(0))))-(0)-(5+(9)+(9))+(3-(9))))+(8))))))))-(0-(0))+(7-(2))))))))-(6))-(8+(9))-(9+(2))-(2)+(9))-(4))+(7)-(1)-(6))-(2-0)))))))-(0)))))-(8+(0-(5))))+(9)-(1-(0)-(3)))-(3)-(0)))+(4)+(6))))-(5)+(1-(5)))))+(10))))-(5)+(0))))))-(6)))))))+(1))))))))-(5)))))))))+(8))))))))))))))))))-(7)+(10)))))))))))))-(4))))))-(10)-(4))+(1)+(3))-(1))))+(9))))))))+(2-(7-(4-(3+(0))))-(10)))))+0))))+(10)))))+(4)))))))))))+(3)))))))-(5)))))+(3)))))))))))))-(7)-(5-(2+(9))-(0))+(4)))+(10)))))-(1)))-(0))+(1))-(8+(10))))))-(10)-(10+(9)+(2))))-(1)))-(2))))+(4+(5))))))+(8))))))))))))))))))))))-(7)))-(3)))))))+(1))))-(7)-(3)+(4))))))-(6)))))))-(9-(3)))))))))))+(8))))))))))+(6))))))))))))))))))))))))))))))))))+(5))+(7))))))))))))))))))))))))-(10))))))+9)))))))', -56),
]

for i, (s, ans) in enumerate(tests):
    res = sol.calculate(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
