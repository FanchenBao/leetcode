# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """LeetCode 452

        The idea is to find overlapping intervals after sorting points based
        on x-coord. Each time a new overlapping interval is found, we update
        the interval. If a new range cannot form an overallping interval, we
        set the new range as the new overlapping interval and burst all the
        balloons of the previous overlapping interval.

        O(NlogN), 1504 ms, 39% ranking (there are more test cases now, 48 to
        be exact, than the last time I solved this problem).
        """
        lo, hi, res = -math.inf, -math.inf, 0
        for nl, nh in sorted(points):
            if nl > hi:
                res += 1
                lo, hi = nl, nh
            else:
                lo, hi = nl, min(hi, nh)
        return res


class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Sort by end position
        """
        hi, res = -math.inf, 0
        for nl, nh in sorted(points, key=lambda p: p[1]):
            if nl > hi:
                res += 1
                hi = nh
        return res


sol = Solution2()
tests = [
    ([[10,16],[2,8],[1,6],[7,12]], 2),
    ([[1,2],[3,4],[5,6],[7,8]], 4),
    ([[1,2],[2,3],[3,4],[4,5]], 2)
]

for i, (points, ans) in enumerate(tests):
    res = sol.findMinArrowShots(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
