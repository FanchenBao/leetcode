# from pudb import set_trace; set_trace()
from typing import List
import re


class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        """For IPv4, regex is not the easiest to use, at least for me, because
        we have to ideantify range for number. Using number comparison is easy
        to restrict the range for each number to 0-255. However, the check for
        leading zero requires some effort. In this case, I left strip all the
        '0' and compare the result to the original. If the two are not the same
        and if the value itself is not '0', then we have leading zeroes.

        For IPv6, regex is sufficient.

        41 ms, 32% ranking.
        """
        if '.' in queryIP:
            qlst = queryIP.split('.')
            if len(qlst) == 4 and all(q.isnumeric() and (q == '0' or (q.lstrip('0') == q and 0 <= int(q) <= 255)) for q in qlst):
                return 'IPv4'
        elif ':' in queryIP:
            qlst = queryIP.split(':')
            if len(qlst) == 8:
                p = re.compile(r'^[\da-fA-F]{1,4}$')
                if all(p.match(q) for q in qlst):
                    return 'IPv6'
        return 'Neither'


sol = Solution()
tests = [
    ('172.16.254.1', 'IPv4'),
    ('2001:0db8:85a3:0:0:8A2E:0370:7334', 'IPv6'),
    ('256.256.256.256', 'Neither'),
    ('172.16.254.a', 'Neither'),
    ('172.16.254.01', 'Neither'),
    ('172.16..1', 'Neither'),
    ('2001:0db8:85a3::0:8A2E:0370:7334', 'Neither'),
    ('2001:0db8:85a3:0:0:8A2E:0370:73341', 'Neither'),
    ('20G1:0db8:85a3:0:0:8A2E:0370:7334', 'Neither'),
]

for i, (queryIP, ans) in enumerate(tests):
    res = sol.validIPAddress(queryIP)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
