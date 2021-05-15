# from pudb import set_trace; set_trace()
from typing import List
import re


class Solution1:
    def isNumber(self, s: str) -> bool:
        """LeetCode 65

        Naive regex, following exactly the description of the problem

        40 ms, 18% ranking.
        """
        return re.match(r'^(\+|-)?(((\d+\.(\d+)?)|(\.\d+))|(\d+))((e|E)(\+|-)?\d+)?$', s) is not None


class Solution2:
    def isNumber(self, s: str) -> bool:
        """This is a cheating method, but we did learn that float() can handle
        'infinity' or 'inf' in any combinations of upper or lower case, and with
        or without +/- sign. Therefore, these special cases must be considered
        separately.
        """
        s = s.lower()
        if s in {
            'inf',
            '-inf',
            '+inf',
            'infinity',
            '+infinity',
            '-infinity',
        }:
            return False
        try:
            float(s)
            return True
        except Exception:
            return False


class Solution3:
    def is_integer(self, frag: str) -> bool:
        return re.match(r'^(\+|-)?\d+$', frag) is not None

    def is_decimal(self, frag: str) -> bool:
        return re.match(r'^(\+|-)?((\d+\.(\d+)?)|(\.\d+))$', frag) is not None

    def isNumber(self, s: str) -> bool:
        lst = s.lower().split('e')
        n = len(lst)
        if n > 2:
            return False
        return (self.is_integer(lst[0]) or self.is_decimal(lst[0])) and (n == 1 or self.is_integer(lst[1]))


class Solution4:
    def isNumber(self, s: str) -> bool:
        """Better regex.
        """
        return re.match(r'^[\+-]?((\d+\.?\d*)|(\.\d+))([eE][\+-]?\d+)?$', s) is not None


class Solution5:
    def is_integer(self, frag: str) -> bool:
        if not frag:
            return False
        return all(frag[i].isnumeric() for i in range(len(frag)))

    def is_decimal(self, frag: str) -> bool:
        if not frag:
            return False
        lst = frag.split('.')
        n = len(lst)
        if n > 2:
            return False
        elif n == 1:
            return self.is_integer(lst[0])
        elif lst[0] == '':
            return self.is_integer(lst[1])
        elif lst[1] == '':
            return self.is_integer(lst[0])
        else:
            return self.is_integer(lst[0]) and self.is_integer(lst[1])

    def isNumber(self, s: str) -> bool:
        """Non-regex solution

        36 ms, 53% ranking.
        """
        lst = s.lower().split('e')
        n = len(lst)
        if n > 2:
            return False
        elif n == 1:
            return (lst[0][0] in {'+', '-'} and self.is_decimal(lst[0][1:])) or self.is_decimal(lst[0])
        elif lst[0] != '' and lst[1] != '':
            check1 = (lst[0][0] in {'+', '-'} and self.is_decimal(lst[0][1:])) or self.is_decimal(lst[0])
            check2 = (lst[1][0] in {'+', '-'} and self.is_integer(lst[1][1:])) or self.is_integer(lst[1])
            return check1 and check2
        else:
            return False


sol = Solution5()
tests = [
    ('2', True),
    ('0089', True),
    ('-0.1', True),
    ('+3.14', True),
    ('4.', True),
    ('-.9', True),
    ('2e10', True),
    ('-90E3', True),
    ('3e+7', True),
    ('+6e-1', True),
    ('53.5e93', True),
    ('-123.456e789', True),
    ('abc', False),
    ('1a', False),
    ('1e', False),
    ('e3', False),
    ('99e2.5', False),
    ('--6', False),
    ('-+3', False),
    ('95a54e53', False),
    ('inf', False),
    ('+inf', False),
    ('-inf', False),
    ('infe1', False),
    ('--inf', False),
    ('.', False),
    ('i.1', False),
    ('4e+', False)
]

for i, (s, ans) in enumerate(tests):
    res = sol.isNumber(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}, Test: {s}')
