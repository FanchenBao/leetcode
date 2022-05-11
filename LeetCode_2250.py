# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_left
import math


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        xs = sorted((rec[0], i) for i, rec in enumerate(rectangles))
        ys = sorted((rec[1], i) for i, rec in enumerate(rectangles))
        res = []
        for x, y in points:
            idx_xs = bisect_left(xs, (x, -math.inf))
            set_x = set(xs[j][1] for j in range(idx_xs, len(xs)))
            idx_ys = bisect_left(ys, (y, -math.inf))
            set_y = set(ys[j][1] for j in range(idx_ys, len(ys)))
            res.append(len(set.intersection(set_x, set_y)))
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
