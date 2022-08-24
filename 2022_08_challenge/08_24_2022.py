# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        """LeetCode 326

        Recursion.

        116 ms, faster than 68.32%
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        q, r = divmod(n, 3)
        if r:
            return False
        return self.isPowerOfThree(q)


class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        """Since n is bounded, we can pick the largest n possible, and use that
        to check all other ns. The largest n in 32 bits signed integer is 3**19
        = 1162261467
        """
        return n > 0 and 1162261467 % n == 0
        
        

sol = Solution()
tests = [
    (27, True),
    (0, False),
    (9, True),
    (-9, False),
    (243, True),
    (45, False),
]

for i, (n, ans) in enumerate(tests):
    res = sol.isPowerOfThree(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
