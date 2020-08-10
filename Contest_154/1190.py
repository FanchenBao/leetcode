#! /usr/bin/env python3
from typing import Deque, List, Dict
from collections import deque

"""09/19/2019

Solution1:
A stack and a queue. Once a pair of parentheses are found, pop all letters in
between out of a stack into a queue, then pop from front of the queue back into
stack to complete reverse option. Do this until we reach the end of the string.
Stack now contains the correctly reversed string.

This solution clocked in at 48 ms.


Solution2:
Read it from here

https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/discuss/383670/JavaC%2B%2BPython-Why-not-O(N)

And my mind is blown away. In order to solve the problem in O(N), we must do the
reverse in one pass. This means we have to follow the correct order in the final
string to traverse the original string. The way to do that is to jump to new
starting place every time a parenthesis is encountered. After the jump, we also
have to reverse the traversing direction.

This solution is so beautiful, I have to call it black magic. The fact that once
we jump to the inner parentheses and seemingly have nowhere else to go, the
algorithm can unfuck itself by jumping to some parentheses already seen before
but this time going in the opposite direction. Essentially, we are able to use
this jumping and reversing direction method to traverse the entire string only
once. Truly brilliant.

This solution clocked in at 36 ms.
"""


class Solution1:
    def reverseParentheses(self, s: str) -> str:
        stack: Deque[str] = deque()
        queue: Deque[str] = deque()
        for c in s:
            if c == ")":
                while stack[-1] != "(":
                    queue.append(stack.pop())
                stack.pop()  # pop '('
                while queue:
                    stack.append(queue.popleft())
            else:
                stack.append(c)
        return "".join(stack)


class Solution2:
    def reverseParentheses(self, s: str) -> str:
        left: List[int] = []
        # key is the pos of a parenthesis, value is the pos of its paired parenthesis
        paired: Dict[int, int] = {}
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == ")":
                j = left.pop()
                paired[i], paired[j] = j, i
        res: str = ""
        i = 0
        d: int = 1
        while i < len(s):
            if s[i] in {
                "(",
                ")",
            }:  # jump to the other end of paired parenthesis
                i = paired[i]
                d *= -1  # reverse direction
            else:
                res += s[i]
            i += d  # depending on d, this can be going to the right or left
        return res


sol = Solution2()
s = "(ed(et(oc))el)"
print(sol.reverseParentheses(s))
