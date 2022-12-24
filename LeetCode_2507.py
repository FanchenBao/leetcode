# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def smallestValue(self, n: int) -> int:
        """Just brute force the prime factors. We did do it with a little trick,
        where we take away all factors of 2. Thus, we only need to check odd
        numbers for the remaining factors.

        O(logN), 67 ms, faster than 66.44% 
        """
        
        def helper(n: int) -> int:
            res = 0
            while n % 2 == 0:
                n //= 2
                res += 2
            cur = 3
            while n > 1:
                if n % cur == 0:
                    n //= cur
                    res += cur
                else:
                    cur += 2
            return res

        while True:
            next_n = helper(n)
            if next_n == n:
                return next_n
            n = next_n


sol = Solution()
tests = [
    (15, 5),
    (3, 3),
]

for i, (n, ans) in enumerate(tests):
    res = sol.smallestValue(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
