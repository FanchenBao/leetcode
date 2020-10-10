# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """83% ranking. I think I used greedy and tried to rationalize it. But
        let's see what the discussion says.
        
        The discussion says about the same thing.
        """
        points.sort(key=lambda p: p[0])
        length = len(points)

        def helper(idx: int) -> int:
            ol_l, ol_r = points[idx]
            for i in range(idx + 1, length):
                cur_l, cur_r = points[i]
                if cur_l <= ol_r:
                    ol_l, ol_r = max(cur_l, ol_l), min(cur_r, ol_r)
                else:
                    break
            else:
                return 1
            return 1 + helper(i)

        return helper(0) if length else 0


class Solution2:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Let's try iterative instead of recursion.
        93% ranking.
        """
        points.sort(key=lambda p: p[0])
        length, res = len(points), 0
        if not length:
            return 0
        ol_r = math.inf
        for cur_l, cur_r in points:
            if cur_l <= ol_r:
                ol_r = min(cur_r, ol_r)
            else:
                res += 1
                ol_r = cur_r
        return res + 1


class Solution3:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """Sort by end instead of start can simplify code
        """
        points.sort(key=lambda p: p[1])
        end, res = -math.inf, 0
        for p in points:
            if p[0] > end:
                res += 1
                end = p[1]
        return res


sol = Solution3()
tests = [
    ([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
    ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
    ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
    ([[1, 2]], 1),
    ([[2, 3], [2, 3]], 1),
    ([], 0),
]

for i, (points, ans) in enumerate(tests):
    res = sol.findMinArrowShots(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
