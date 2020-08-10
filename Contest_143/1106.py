from collections import deque
from typing import Deque

"""
07/03/2019

Although marked as hard, this was actually one of the easiest problems in
contest 143. A straightforward solution was provided in the parseBoolExpr()
where a stack was used to assist the evaluation process. This was very similar
to the evaluation of a prefix expression.

parsBoolExpr2() was a fun soluion I saw on the discussion, where the built-in
functions any(), all(), not, and eval() were leveraged to make the solution
one line. However, time performance suffered (112 ms vs. 52 ms using stack)
"""


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack: Deque[str] = deque()
        for sym in expression:
            if sym == ",":
                continue
            if sym == ")":
                # record true or false in the expression
                tf = set()
                while stack[-1] != "(":
                    tf.add(stack.pop())
                stack.pop()  # pop the left parenthesis
                op = stack.pop()  # operator
                if op == "!":
                    if tf.pop() == "t":
                        stack.append("f")
                    else:
                        stack.append("t")
                elif op == "|":
                    if "t" in tf:
                        stack.append("t")
                    else:
                        stack.append("f")
                elif op == "&":
                    if "f" in tf:
                        stack.append("f")
                    else:
                        stack.append("t")
            else:
                stack.append(sym)
        return stack.pop() == "t"

    def parseBoolExpr2(self, expression: str) -> bool:
        s = expression
        return eval(
            s.replace("t", "True")
            .replace("f", "False")
            .replace("!", "not |")
            .replace("|(", "any([")
            .replace("&(", "all([")
            .replace(")", "])")
        )


sol = Solution()
if sol.parseBoolExpr("!(f)"):
    print("Test Case 1: Pass")
else:
    print("Test Case 1: Fail")

if not sol.parseBoolExpr("!(t)"):
    print("Test Case 2: Pass")
else:
    print("Test Case 2: Fail")

if sol.parseBoolExpr("|(f,t)"):
    print("Test Case 3: Pass")
else:
    print("Test Case 3: Fail")

if not sol.parseBoolExpr("&(t,f)"):
    print("Test Case 4: Pass")
else:
    print("Test Case 4: Fail")

if not sol.parseBoolExpr("|(&(t,f,t),!(t))"):
    print("Test Case 5: Pass")
else:
    print("Test Case 5: Fail")
