# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left
import math
from collections import defaultdict


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        """We have to take a hint. And the hint is there are at most 100 unique
        y values for the rectangles. Ya, I didn't read the question
        specification carefully. Since there are so few ys, it is possible to
        list all xs for each y in ascending order. Then we binary search on y
        first to identify which ys are likely to hold a point. Then, we iterate
        through all lists of xs of each y and use another binary search to see
        how many xs are able to hold the point.

        N be the length of rectangles, M be the length of points
        O(NlogN + MlogN), 2475 ms, faster than 77.11%
        """
        rectangles.sort(key=lambda rec: (rec[1], rec[0]))
        tab = defaultdict(list)
        for l, h in rectangles:
            tab[h].append(l)
        ys = list(tab.keys())
        res = []
        for x, y in points:
            yi = bisect_left(ys, y)
            res.append(0)
            for j in range(yi, len(ys)):
                res[-1] += len(tab[ys[j]]) - bisect_left(tab[ys[j]], x)
        return res
        

sol = Solution()
tests = [
    ([[1,2],[2,3],[2,5]], [[2,1],[1,4]], [2, 1]),
    ([[1,1],[2,2],[3,3]], [[1,3],[1,1]], [1, 3]),
]

for i, (rectangles, points, ans) in enumerate(tests):
    res = sol.countRectangles(rectangles, points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
