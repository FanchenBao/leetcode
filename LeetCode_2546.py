# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """154 ms, faster than 21.09%

        To convert 0 to 1 or 1 to 0, we need a 1. Thus, if we have a free
        standing 1, i.e. a 1 that does not need to be converted, we can always
        make the convertion.

        If there is no free standing 1, we can create a free standing 1 if we
        have a zero to convert and a one to convert. We can use the one to
        convert to convert zero to one, that one will be the free standing 1.
        And it can facilitate all the remaining convertion.

        Of course, if we don't need to convert anything, that is also a valid
        case.

        If none of the above is satisfied, we cannot make the convertion.
        """
        free_ones = conv_ones = conv_zeros = 0
        for a, b in zip(s, target):
            if a == '1':
                free_ones += int(a == b)
                conv_ones += int(a != b)
            else:
                conv_zeros += int(a != b)
        if free_ones or (conv_ones and conv_zeros) or (not conv_ones and not conv_zeros):
            return True
        return False


class Solution2:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        """lee215's reasoning is solid: https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/discuss/3083831/JavaC%2B%2BPython-1-line-Check-1

        Basically, as long as we have 1 in s, we can change anything into
        anything. But the consequence is that the changed string also at least
        contains one 1. Thus, as long as s and target both contains 1, we can
        make the convertion. Of course, if neither contains 1, they must be
        equal to begin with, and that works as well. Thus, we only need to check
        whether 1 is in both s and target

        33 ms, faster than 94.49%
        """
        return ('1' in s) == ('1' in target)


sol = Solution2()
tests = [
    ("001000", "000100", True),
    ("1010", "0110", True),
    ("11", "00", False),
    ("00", '11', False),
    ('00', '00', True),
]

for i, (s, target, ans) in enumerate(tests):
    res = sol.makeStringsEqual(s, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
