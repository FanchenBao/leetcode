# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """LeetCode 452

        Sort by left ascending; if left is the same, sort by right descending.
        One by one, find all the internals that overlap. Each time, we compare
        the new interval's left to the smallest right currently encountered.

        Once all the overlapping intervals are found, we record one arrow.
        O(NlogN + N), 4614 ms, faster than 5.01%
        """
        points.sort(key=lambda tup: (tup[0], -tup[1]))
        res = 0
        i = 0
        while i < len(points):
            end = points[i][1]
            j = i + 1
            while j < len(points) and points[j][0] <= end:
                end = min(end, points[j][1])
                j += 1
            res += 1
            i = j
        return res


class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """No need to sort by both left and right. Sort by left is sufficient

        O(NlogN + N), 3339 ms, faster than 27.47% 
        """
        points.sort()
        res = 0
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                res += 1
                end = points[i][1]
            else:
                end = min(end, points[i][1])
        return res + 1


class Solution3:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Sort based on the right

        O(NlogN + N), 3055 ms, faster than 39.46%
        """
        points.sort(key=lambda tup: tup[1])
        res = 0
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                res += 1
                end = points[i][1]
        return res + 1


sol = Solution3()
tests = [
    ([[10,16],[2,8],[1,6],[7,12]], 2),
    ([[1,2],[3,4],[5,6],[7,8]], 4),
    ([[1,2],[2,3],[3,4],[4,5]], 2),
    ([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]], 2)
]

for i, (points, ans) in enumerate(tests):
    res = sol.findMinArrowShots(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
