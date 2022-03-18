# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def scoreOfParentheses(self, s: str) -> int:
        """LeetCode 856

        Use a stack to keep track of left paren and the most recent score. Each
        time a left paren is encountered, push it into the stack. Otherwise,
        we keep popping the stack until reaching a left paren. All the popped
        elements are scores of the parens contained within. Thus, sum them up
        and then multiply it by two before pushing it back to the stack.

        O(N), 32 ms, 86% ranking.
        """
        stack = []
        for c in s:
            if c == '(':
                stack.append(c)
            else:
                score = 0
                while stack[-1] != '(':
                    score += stack.pop()
                stack[-1] = max(score * 2, 1)
        return sum(stack)



class Solution2:
    def scoreOfParentheses(self, s: str) -> int:
        """Better stack solution, I have demoed this a year ago.
        """
        stack = [0]
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                score = stack.pop()
                stack[-1] += (2 * score) if score else 1
        return stack[0]



class Solution3:
    def scoreOfParentheses(self, s: str) -> int:
        """Onion solution. I have also demoed this a year ago.
        """
        res, layer = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                layer += 1
            else:
                layer -= 1
                if s[i - 1] == '(':  # hit the core
                    res += 1 << layer
        return res


sol = Solution3()
tests = [
    ('()', 1),
    ('()()', 2),
    ('(())', 2),
    ("()(()())()()(()(()()))()()(()()()())(())()()", 31),
]

for i, (s, ans) in enumerate(tests):
    res = sol.scoreOfParentheses(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
