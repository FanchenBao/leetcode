# from pudb import set_trace; set_trace()
from typing import List
import math
from itertools import groupby
from functools import lru_cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        """

        1252 ms, faster than 40.00%
        """
        
        @lru_cache(maxsize=None)
        def dp(l: int, r: int) -> int:
            if l == r:
                return 0
            res = math.inf
            for j in range(l, r):
                if s[j] != s[r]:
                    for i in range(j, r):
                        res = min(res, 1 + dp(j, i) + dp(i + 1, r))
                    break
            return res if res < math.inf else 0

        return dp(0, len(s) - 1) + 1



sol = Solution()
tests = [
    ('aaabbb', 2),
    ('aba', 2),
    ('sdsdsds', 4),
    ("abcabc", 5),
    ("oifofi", 4),
]

for i, (s, ans) in enumerate(tests):
    res = sol.strangePrinter(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
