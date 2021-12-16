# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import math


class Solution:
    def getMoneyAmount(self, n: int) -> int:
        """I tried to find a rule for splitting, but failed. Thus, the current
        solution is brute force. I find out the max amount of money needed when
        each value from 1 to n is taken as root. And then return the min of them

        O(N^2), 4089 ms, 35% ranking.

        UPDATE: instead of checking from 1 to n, now I say we only need to check
        from the middle to the n, because it is always worse splitting closer
        to the smaller end.

        This one runs at 568 ms, 92% ranking. It worked!
        """
        
        @lru_cache(maxsize=None)
        def helper(lo: int, hi: int) -> int:
            if lo >= hi:
                return 0
            res = math.inf
            for root in range((lo + hi) // 2, hi + 1):
                res = min(res, root + max(helper(lo, root - 1), helper(root + 1, hi)))
            return res

        return helper(1, n)


sol = Solution()
tests = [
    (1, 0),
    (2, 1),
    (10, 16),
    (7, 10),
    (20, 49),
    (11, 18),
    (12, 21),
    (13, 24),
    (14, 27),
    (15, 30),
    (16, 34),
    (17, 38),
]

for i, (n, ans) in enumerate(tests):
    res = sol.getMoneyAmount(n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
