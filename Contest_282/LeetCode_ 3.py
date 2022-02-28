# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        time.sort()
        lo, hi = 0, totalTrips * time[-1]
        while lo < hi:
            mid = (lo + hi) // 2
            trips = sum(mid // t for t in time)
            if trips >= totalTrips:
                hi = mid
            else:
                lo = mid + 1
        return lo
        
        
sol = Solution()
tests = [
    ([1, 2, 3], 5, 3),
    ([2], 1, 2),
]

for i, (time, totalTrips, ans) in enumerate(tests):
    res = sol.minimumTime(time, totalTrips)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
