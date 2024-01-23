# from pudb import set_trace; set_trace()
from typing import List
import math
from sortedcontainers import SortedList


class Solution1:
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
        
        In addition, we also have a deficit-surplus system. As we go from right
        to left, if a position does not have enough repeats to satisfy the
        requirement, we accumulate deficit. Such deficit can be repaid by
        surpluce repeats on the left hand side. However, surplus can only be
        used to supplement deficits on the right side, but not on the left
        side. This is because any additional repeats can be used to supplement
        previous groups. But it cannot be used to supplement future groups because
        all the future groups already contain the current number and we cannot
        allow duplicates.
        
        O(NlogN) 2257 ms, faster than 6.67%
        """
        usageLimits.sort()
        lo, hi = 0, len(usageLimits) + 1
        while lo < hi:
            mid = (lo + hi) // 2
            req = mid
            deficit = 0
            for i in range(len(usageLimits) - 1, -1, -1):
                ds = usageLimits[i] - req
                if ds <= 0:
                    deficit += ds
                else:
                    deficit = min(0, deficit + ds)
                if req > 0:
                    req -= 1
            if deficit < 0:  # failed. We cannot make mid number of groups
                hi = mid
            else:
                lo = mid + 1
        return lo - 1


class Solution2:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        """
        This uses the same idea, but we might be able to simplify the procedure
        drastically.

        After sorting usageLimits, if the large values are bigger or equal
        to the max repeats possible, then we don't even have to consider them
        anymore, because they will always be able to contribute to one
        additional group. In other words, if we have m usageLimits that are
        bigger or equal to the max requirements, we will have at least m number
        of additional groups for free.

        We only need to consider the limits that are smaller or equal to the
        max repeats. And we don't have to consider them one by one. Instead,
        we can simply add them together to see if the total number of repeats
        is larger or equal to the required repeats. If yes, we can form the
        required number of groups, otherwise not.
        """
        usageLimits.sort()
        N = len(usageLimits)
        while N > 0 and usageLimits[N - 1] >= N:
            N -= 1
        free = len(usageLimits) - N  # we get these additional groups for free
        lo, hi = 0, N + 1
        total_reps = sum(usageLimits[:N])
        while lo < hi:
            mid = (lo + hi) // 2
            req = (1 + mid) * mid // 2
            if total_reps >= req:
                lo += 1
            else:
                hi = mid
        return lo - 1 + free


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
