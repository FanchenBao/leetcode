# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def calculate(self, s: str) -> int:
        """LeetCode 227

        I forgot how I solved this problem in the past. The solution below
        feels contrived. Since there is no parenthesis, any '*' and '/' can be
        computed immediately. For '+' and '-', I use recursion to obtain the
        right-hand-side.

        There are a few obstacles to jump through. For instance, when to
        transfer the value in cur to left. And what to return when the
        traversal of s has ended.

        O(N), 136 ms, 18% ranking.
        """
        N = len(s)
        
        def helper(idx: int, is_rev: bool) -> int:
            left, cur, op = 0, 0, ''
            for i in range(idx, N):
                if s[i] == ' ':
                    continue
                if '0' <= s[i] <= '9':
                    cur = 10 * cur + int(s[i])
                else:
                    if op == '*' or op == '/':
                        left = (left * cur) if op == '*' else (left // cur)
                    else:
                        left = cur
                    if s[i] == '+':
                        return (left - helper(i + 1, False)) if is_rev else (left + helper(i + 1, False))
                    elif s[i] == '-':
                        return (left + helper(i + 1, True)) if is_rev else (left - helper(i + 1, True))
                    elif s[i] == '*' or s[i] == '/':
                        op, cur = s[i], 0
            if op:
                return (left * cur) if op == '*' else (left // cur)
            return cur

        return helper(0, False)


class Solution2:
    def calculate(self, s: str) -> int:
        """This is the good solution from my previous attempt in 2020-11-24

        A couple things. First, op points to the previous operator. pre points
        to the value to the left of op. cur points to the value to the right
        of op. We check op whenever the current letter hits an operator.

        If op is plus or minus, that means the pre value has ended its journey
        and we can add it to res. Also, since we convert all subtraction to
        addition of negative value, when combining into res, we always perform
        addition.

        Then, based on op being + or -, we reassign pre based on cur.

        If, however, op is * or /, then pre's journey has not ended. We combine
        cur with pre based on op to create a new pre.

        O(N), 68 ms, 94% ranking.
        """
        pre, cur, op = 0, 0, '+'  # op is the PREVIOUS operator
        res = 0
        for le in s + '+':
            if le.isdigit():
                cur = cur * 10 + int(le)
            elif le != ' ':
                if op in '+-':  # no more op is needed for pre
                    res += pre
                    # deduction turned into addition of negative values
                    pre = cur if op == '+' else (-cur)
                else:
                    pre = (pre * cur) if op =='*' else int(pre / cur)
                op = le
                cur = 0
        return res + pre


sol = Solution2()
tests = [
    ('3+2*2', 7),
    (' 3/2 ', 1),
    (" 3+5 / 2 ", 5),
    ('1-2*3-4+6/5+7-8', -9),
    ('14-3/2', 13),
]

for i, (s, ans) in enumerate(tests):
    res = sol.calculate(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
