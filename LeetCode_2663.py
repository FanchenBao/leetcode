# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def smallestBeautifulString(self, s: str, k: int) -> str:
        if len(s) == 1:
            if ord(s[0]) - 97 < k - 1:
                return chr(ord(s[0]) + 1)
            return ''
        for i in range(len(s) - 1, -1, -1):
            rlen = len(s) - i - 1
            rs = 0
            if i - 1 >= 0 and rlen > 0 and ord(s[i - 1]) - 97 == 0:
                rs = 1
            cur = ord(s[i]) - 97 + 1
            while cur < k:
                checks = [
                    i - 1 < 0 or (i - 1 == 0 and ord(s[i - 1]) - 97 != cur) or (i - 1 > 0 and ord(s[i - 1]) - 97 != cur and ord(s[i - 2]) - 97 != cur),
                    rlen == 0 or (rlen == 1 and rs != cur) or (rlen >= 2 and rs != cur and ((cur != 1) if rs == 0 else (cur != 0))),
                ]
                if all(checks):
                    break
                cur += 1
            else:
                continue
            rpat = 'abc' if rs == 0 else 'bac'
            q, r = divmod(rlen, 3)
            return s[:i] + chr(cur + 97) + q * rpat + rpat[:r]
        return ''


sol = Solution()
tests = [
    ('abcz', 26, 'abda'),
    ('dc', 4, ''),
    ('abca', 4, 'abcd'),
    ('b', 6, 'c'),
    ("dacd", 4, 'dbac'),
]

for i, (s, k, ans) in enumerate(tests):
    res = sol.smallestBeautifulString(s, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
