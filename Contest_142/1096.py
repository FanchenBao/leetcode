from collections import deque
from itertools import product

"""
Date: 06/24/2019

Intuition: first turn the original expression in to postfix, then evaluate postfix.
Four things to keep in mind:
1. Since multiplication was not displayed using any operator, we must add it during conversion from infix to postfix.
2. Each operands could contain multiple letters.
3. One cannot push list or set into another set, since list and set are not hashable. Thus, we must make sure after each evaluation, the result is a set of strings.
4. The returned value must be a sorted list, as per the problem's request.

Included at the end (commented out) was a very good solution using very similar intuition, but evaluting the expression along side parsing. It was brilliant! Orginal site: "https://leetcode.com/problems/brace-expansion-ii/discuss/317878/stack-3-types-of-ops-with-details-analysis.-Python"
"""


class Solution:
    def braceExpansionII(self, expression):
        exp = self.inToPos(
            expression
        )  # exp is a list of operands and operators, each operands is a set, each operator a string
        i = 2
        while len(exp) != 1:
            if type(exp[i]) != set:
                if exp[i] == ",":  # perform union
                    temp = exp[i - 2].union(exp[i - 1])
                elif exp[i] == "*":  # perform cartesian product
                    temp = set()
                    for item in product(exp[i - 2], exp[i - 1]):
                        temp.add(
                            item[0] + item[1]
                        )  # each element of the set must be a string
                for j in range(3):
                    del exp[i - 2]
                exp.insert(i - 2, temp)
                i -= 2
            i += 1

        return sorted(list(exp[0]))

    def inToPos(self, exp):
        """ Turn the infix exp into its postfix version """
        res = []
        op = deque()
        i = 0
        while i < len(exp):
            c = exp[i]
            if c == "{":
                if (
                    i != 0 and exp[i - 1] != "," and exp[i - 1] != "{"
                ):  # fill in the multiplication operator
                    op.append("*")
                op.append(c)
            elif c == "}":
                while (
                    op and op[-1] != "{"
                ):  # pop all operators currently enclosed in the brackets
                    res.append(op.pop())
                op.pop()  # pop the left parenthesis
            elif c == ",":
                while (
                    op and op[-1] != "{"
                ):  # since there are only two operators, and ',' is the smaller one, any operator currently on stack needs to be popped until the left bracket
                    res.append(op.pop())
                op.append(c)
            else:
                if (
                    i != 0 and exp[i - 1] == "}"
                ):  # before append the operand, check whether there is a multiplication operator missing
                    op.append("*")
                j = i
                while i < len(exp) and exp[i] not in {
                    "{",
                    "}",
                    ",",
                }:  # For each operand, make sure to include the full string, not just a single char
                    i += 1
                res.append({exp[j:i]})
                i -= 1
            i += 1
        while op:  # append the remaining operators if any
            res += op.pop()
        return res


# class Solution(object):
#     def braceExpansionII(self, exp):
#         stack = []
#         for c in exp:
#             if c == '{':
#                 stack.append('{')
#             elif c == '}':
#                 while stack[-2] == ',':
#                     set2 = stack.pop()
#                     stack.pop()
#                     stack[-1].update(set2)
#                 assert(stack[-2] == '{')
#                 tail = stack.pop()
#                 stack[-1] = tail
#             elif c == ',':
#                 stack.append(',')
#             else:
#                 stack.append(set(c))
#             while len(stack) > 1 and isinstance(stack[-1], set) and isinstance(stack[-2], set):
#                 set2 = stack.pop()
#                 set1 = stack.pop()
#                 stack.append(set(w1 + w2 for w1 in set1 for w2 in set2))
#         assert(len(stack) == 1)
#         return list(sorted(stack[-1]))


sol = Solution()
print(sol.braceExpansionII("{abc,d}"))
