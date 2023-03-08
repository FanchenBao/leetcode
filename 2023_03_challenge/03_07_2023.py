# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        """LeetCode 2187

        Binary search.

        O(Nlog(MK)), where M is the largest of time and K is totalTrip.

        3644 ms, faster than 21.75% 
        """
        time.sort()
        lo, hi = 0, time[-1] * totalTrips + 1
        while lo < hi:
            mid = (lo + hi) // 2
            trips = 0
            for t in time:
                if t > mid:
                    break
                trips += mid // t
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo


sol = Solution()
tests = [
    ([1,2,3], 5, 3),
    ([2], 1, 2),
]

for i, (time, totalTrips, ans) in enumerate(tests):
    res = sol.minimumTime(time, totalTrips)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
