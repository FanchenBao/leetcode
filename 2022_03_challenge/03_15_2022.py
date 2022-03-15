# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """LeetCode 1249

        I am surprised that this one passes OJ. There is no DP. All I did was
        identifying the wrongly placed parenthesis. This is because if a paren
        is wrongly placed, it has to be removed for the string to be valid.
        Therefore, the min remove of paren is equivalent to removing all wrong
        paren.

        O(N), 80 ms, 98% ranking.
        """
        slist = list(s)
        stack = []
        for i, le in enumerate(slist):
            if le == '(':
                stack.append(i)
            elif le == ')':
                if not stack:
                    slist[i] = ''
                else:
                    stack.pop()
        for j in stack:
            slist[j] = ''
        return ''.join(slist)


sol = Solution()
tests = [
    ('lee(t(c)o)de)', 'lee(t(c)o)de'),
    ('a)b(c)d', 'ab(c)d'),
    ('))((', ''),
    ("lee(t(c)o)(de)", "lee(t(c)o)(de)"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.minRemoveToMakeValid(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
