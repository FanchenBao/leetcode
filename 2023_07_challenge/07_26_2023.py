# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        """LeetCode 1870

        Binary search. But pay attention that we have to handle the last time
        differently from the others, as the last time does not need to be
        ceilinged.

        O(NlogN), 3188 ms, faster than 60.68%
        """
        max_speed = 10**7 + 1
        lo, hi = 1, max_speed
        while lo < hi:
            mid = (lo + hi) // 2
            time = sum(math.ceil(d / mid) for d in dist[:-1])
            time += dist[-1] / mid
            if time <= hour:
                hi = mid
            else:
                lo = mid + 1
        return lo if lo < max_speed else -1


sol = Solution()
tests = [
    ([1,3,2], 6, 1),
    ([1,3,2], 2.7, 3),
    ([1,3,2], 1.9, -1),
]

for i, (dist, hour, ans) in enumerate(tests):
    res = sol.minSpeedOnTime(dist, hour)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
