# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList


class Solution:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        """
        Got a hint about a potential method: greedy + binary search.

        We can sort usageLimits, and then binary search the max possible
        number of groups. The question is "can we create x number of groups"
        To answer this question, we can greedily always start from the highest
        number of repeats. To make x number of groups, the max repeats must be
        no smaller than x itself. The second max repeats must be no smaller
        than x - 1, so on and so forth. Thus we can go through usageLimits
        and check if all the requirments can be met. If so, we can increase x
        otherwise decrease it.
        """
        usageLimits.sort()
        lo, hi = 0, len(usageLimits) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            req = mid
            for i in range(len(usageLimits) - 1, -1, -1):
                if req == 0:
                    break
                if usageLimits[i] < req:
                    break
                req -= 1
            if req:  # failed. We cannot make mid number of groups
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


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
