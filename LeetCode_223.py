# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """Two rounds of merging intervals.

        O(1), 56 ms, 57% ranking.

        Update: A little trick from https://leetcode.com/problems/rectangle-area/discuss/62149/Just-another-short-way
        to avoid explict if clause.
        """
        oxl, oyb = max(ax1, bx1), max(ay1, by1)
        oxr, oyt = max(min(ax2, bx2), oxl), max(min(ay2, by2), oyb)
        return (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1) - (oxr - oxl) * (oyt - oyb)


sol = Solution()
tests = [
    (-3, 0, 3, 4, 0, -1, 9, 2, 45),
    (-2, -2, 2, 2, -2, -2, 2, 2, 16),
]

for i, (ax1, ay1, ax2, ay2, bx1, by1, bx2, by2, ans) in enumerate(tests):
    res = sol.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
