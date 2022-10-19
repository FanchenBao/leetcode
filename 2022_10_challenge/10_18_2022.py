# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby


class Solution:
    def countAndSay(self, n: int) -> str:
        """LeetCode 38

        54 ms, faster than 86.17%
        """
        s = '1'
        if n == 1:
            return s
        for i in range(2, n + 1):
            s = ''.join(f'{len(list(g))}{k}' for k, g in groupby(s))
        return s        


sol = Solution()
tests = [
    (4, '1211'),
]

for i, (n, ans) in enumerate(tests):
    res = sol.countAndSay(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
