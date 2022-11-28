# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def pivotInteger(self, n: int) -> int:
        """Use math
        """
        q = n * (n + 1) // 2
        sqrt_q = int(math.sqrt(q))
        if sqrt_q**2 == q:
            return sqrt_q
        return -1


sol = Solution()
tests = [
    (8, 6),
    (1, 1),
    (4, -1),
]

for i, (n, ans) in enumerate(tests):
    res = sol.pivotInteger(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
