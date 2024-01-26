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
        This uses the same idea, but we can omit the repeats if they are no
        smaller than the max number of groups allowed for the associated
        number.

        The omission can reduce the run time, because the total length of
        usageLimits that goes into the binary search may be smaller than the
        original length.

        O(NlogN), 2126 ms, faster than 6.67%
        """
        usageLimits.sort()
        N = len(usageLimits)
        while N > 0 and usageLimits[N - 1] >= N:
            N -= 1
        free = len(usageLimits) - N  # we get these additional groups for free
        lo, hi = 0, N + 1
        while lo < hi:
            mid = (lo + hi) // 2
            req = mid
            deficit = 0
            for i in range(N - 1, -1, -1):
                d = usageLimits[i] - req
                if d <= 0:
                    deficit += d
                else:
                    # we cannot increase deficit to above 0, becau:wqse once the
                    # deficit is cleared, any extra repeats of the current
                    # number cannot count towards the deficit in the subsequent
                    # iteration
                    deficit = min(0, deficit + d)
                req = max(0, req - 1)
            if deficit == 0:
                lo = mid + 1
            else:
                hi = mid
        return lo - 1 + free


class Solution3:
    def maxIncreasingGroups(self, usageLimits: List[int]) -> int:
        """
        This is the solution from lee215
        https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/discuss/3803904/JavaC%2B%2BPython-Math-O(n)

        For a breakdown of this method, refer to my own comment:
        https://leetcode.com/problems/maximum-number-of-groups-with-increasing-length/discuss/3803904/JavaC++Python-Math-O(n)/2227246

        O(NlogN) but without binary search part. 750 ms, faster than 67.21%
        """
        total = 0
        res = 1
        for u in sorted(usageLimits):
            total += u
            if total >= (1 + res) * res // 2:  # is res number of groups possible?
                res += 1
        return res - 1






sol = Solution2()
tests = [
    # ([1,2,5], 3),
    # ([2,1,2], 2),
    # ([1,7,7,1], 3),
    ([2,8,5,8,1,4,5,1,10,2], 8),
]

for i, (usageLimits, ans) in enumerate(tests):
    res = sol.maxIncreasingGroups(usageLimits)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
