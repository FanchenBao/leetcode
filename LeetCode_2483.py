# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        """Also straightforward solution

        O(N), 302 ms, faster than 75.84%
        """
        cn, cy = 0, customers.count('Y')
        res, pen = -1, math.inf
        for i in range(len(customers)):
            if cn + cy < pen:
                pen = cn + cy
                res = i
            cn += int(customers[i] == 'N')
            cy -= int(customers[i] == 'Y')
        if cn + cy < pen:
            pen = cn + cy
            res = len(customers)
        return res


sol = Solution()
tests = [
    ("YYNY", 2),
    ("NNNNN", 0),
    ("YYYY", 4),
]

for i, (customers, ans) in enumerate(tests):
    res = sol.bestClosingTime(customers)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
