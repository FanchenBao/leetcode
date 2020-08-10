#! /usr/local/bin/python3
"""
07/09/2019

While the problem itself could've been clearer in its description, the problem
is somewhat interesting. The requirement is to breakdown the given valid
parenthesis string (VPS) into two subsequences (note that since we are
considering subsequences, there is no requirement that the subsequences must
be adjacent to each other or cannot overlap). The two subsequences can be any
sequence within the given VPS, overlapping or not, as long as they are both
also VPS. The outcome is to make the max depth of the two subsequences the
smallest.

My solution is to loop through the original VPS, if we encounter a '(' when
the stack is we designate it to subsequence A. If there is a '(' already in the
stack, we designate the new '(' to the other subsequence so as not minimize
the chance of nesting parentheses. Whenever a ')' is encountered, it is
designated to the same subsequence as its matching '(', currently at the end
of the stack, and we pop the matching '('.

Along the way, a res array is used to keep track of how we designate each
parenthesis.

I also wrote a separate function for fun, called depth(). It computes the depth
of any given VPS. The algorithm counts '(' to determine the nesting depth, and
uses subMax to keep track the depth of each sub VPS. When ')' is encountered,
we pop the stack. If stack becomes empty, we have reached the top level of VPS,
at which time we can update the total depth.

The one-liner was provided by the discussion section and deserves more
discussion.

"https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/328841/JavaC%2B%2BPython-Several-Ideas"

It uses the odd/even identity of left parenthesis to determine
when to switch left parenthesis to A and when to B. My method is essentially
the same, but much more verbose and has to rely on a stack. Here is more
explanation:

Left parentheses of the same depth have the same odd/even identity of their
indices. E.g. seq = '()((())())', left parentheses on the same depth are seq[0]
and seq[2] (depth 1); seq[3] and seq[7] (depth 2); seq[4] (depth 3). Left
parentheses of the same depth can be grouped to one subsequence, while
different depth the other. Thus, we need to identify the odd/even identity of
each left parenthesis index in seq, and use XOR to switch subsequences when a
different odd/even identity is encountered. i & 1 determines odd/even identity;
^ (seq[i] == '(') puts even-indexed left parenthesis to group 1 and odd-indexed
group 0. As for the right parentheses, the odd/even identity of their indices
must be different from those of their matching left parentheses. So an
even-indexed right parenthesis goes to group 0 to match the odd-indexed left
parenthesis (even & 1 ^ false = 0), while odd-indexed right parenthesis goes to
group 1 to match the even-indexed left parenthesis (odd & 1 ^ false = 1).
"""
from typing import List


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        res: List[int] = []
        stack: List[int] = []
        for s in seq:
            if s == "(":
                if stack:
                    res.append(stack[-1] ^ 1)
                    stack.append(res[-1])
                else:
                    res.append(0)
                    stack.append(0)
            elif stack:
                res.append(stack.pop())
        return res

    def depth(self, seq):
        stack = []
        d = 0  # total depth
        count = 0
        subMax = 0  # record max depth of current VPS
        for s in seq:
            if s == "(":  # whenver '(' encountered, increment count
                stack.append(s)
                count += 1
                subMax = max(subMax, count)  # update subMax if necessary
            else:  # whenever ')' encountered, decrement count
                stack.pop()
                count -= 1
                if not stack:  # when we reach the top level, update d
                    d = max(d, subMax)
        return d

    def oneLiner(self, seq):
        """ Magical oneliner. See above for explanation"""
        return [i & 1 ^ (seq[i] == "(") for i, c in enumerate(seq)]


seq = "()((()(((())))))(())((()))()((((((()))((())())))))()"
sol = Solution()
print(sol.depth(seq))
pos = sol.maxDepthAfterSplit(seq)
A = "".join(s for i, s in enumerate(seq) if not pos[i])
B = "".join(s for i, s in enumerate(seq) if pos[i])
print(sol.depth(A), sol.depth(B))
print(sol.oneLiner("()()"))
