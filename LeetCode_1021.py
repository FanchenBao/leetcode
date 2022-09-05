# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def removeOuterParentheses(self, s: str) -> str:
        """Not difficult to code the solution, but it did take a while for me
        to understand what the problem is asking for. Basically, it just wants
        to deomposition s, and remove the top level outer parenthesis. There is
        no recursion, because we are only interested in the top level. All the
        inner level parentheses shall be left intact.

        O(N), 76 ms, faster than 20.78% 
        """
        stack = []
        res = ''
        for j, le in enumerate(s):
            if le == ')':
                i = stack.pop()
                if not stack:
                    res += s[i + 1: j]
            else:
                stack.append(j)
        return res


class Solution2:
    def removeOuterParentheses(self, s: str) -> str:
        """https://leetcode.com/problems/remove-outermost-parentheses/discuss/270022/JavaC%2B%2BPython-Count-Opened-Parenthesis

        We only ignore the parentheses of the first '(' and last ')' in the
        decomposition. This means if we keep track of the number of open paren,
        then we ignore '(' if there is no open paren at the moment (i.e. the
        current '(' is the first '('). Similarly, we ignore ')' if there is
        only one open paren (i.e. the only open paren is the first '(').
        """
        res = []
        open_paren = 0
        for le in s:
            if le == '(' and open_paren > 0:
                res.append(le)
            elif le == ')' and open_paren > 1:
                res.append(le)
            open_paren += 1 if le == '(' else -1
        return ''.join(res)


sol = Solution2()
tests = [
    ("(()())(())(()(()))", '()()()()(())'),
    ("(()())(())", "()()()"),
    ("()()", ""),
]

for i, (s, ans) in enumerate(tests):
    res = sol.removeOuterParentheses(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
