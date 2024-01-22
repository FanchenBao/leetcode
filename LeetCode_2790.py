# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        N = len(usageLimits)
        debts = 0
        for i, u in enumerate(sorted(usageLimits)):
            # At each i, if u == i + 1, we have exactly the number of
            # repeats to achieve the max number of groups, which is N.
            # If u > i + 1, then u - (i + 1) is the surplus.
            # But not all the surplus can be used, because at each position
            # the capacity for the surplus is limited to N - i - 1 (for
            # example, the surplus at i = 0 can help numbers at i = 1, 2, ... 
            # N - 1. Anything more than that cannot be used.)
            # If u < i + 1, then we have debts, which can be paid by the
            # surplus from before.
            # At the end we want to compute the net debts. If it is larger
            # or equal to 0, we can achieve max number of groups N.
            # Otherwise, we achieve N + debts.
            ds = u - (i + 1)
            if ds <= 0:
                debts += ds
            else:
                debts += min(ds, N - i - 1)
            print(i, u, ds, N - i - 1, debts)
        return min(N, N + debts)

sol = Solution()
tests = [
    # ([1,2,5], 3),
    # ([2,1,2], 2),
    ([1,7,7,1], 3),
]

for i, (usageLimits, ans) in enumerate(tests):
    res = sol.maxIncreasingGroups(usageLimits)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
