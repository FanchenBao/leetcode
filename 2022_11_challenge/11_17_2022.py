# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """LeetCode 223

        This is a pretty dumb method. Basically we analyze all possible overlap
        situations. There is an easier way. Refer to Solution2

        93 ms
        """
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if by1 >= ay2 or bx1 >= ax2:
            return s
        if bx1 <= ax1 and by1 >= ay1:
            if bx2 <= ax1:
                return s
            if ax1 <= bx2 <= ax2 and by2 >= ay2:
                return s - (bx2 - ax1) * (ay2 - by1)
            if bx2 >= ax2 and by2 >= ay2:
                return s - (ax2 - ax1) * (ay2 - by1)
            if ax1 <= bx2 <= ax2 and by2 <= ay2:
                return s - (bx2 - ax1) * (by2 - by1)
            if bx2 >= ax2 and by2 <= ay2:
                return s - (ax2 - ax1) * (by2 - by1)
        if ax1 <= bx1 <= ax2 and ay1 <= by1 <= ay2:
            if ax1 <= bx2 <= ax2 and by2 >= ay2:
                return s - (bx2 - bx1) * (ay2 - by1)
            if bx2 >= ax2 and by2 >= ay2:
                return s - (ax2 - bx1) * (ay2 - by1)
            if ax1 <= bx2 <= ax2 and ay1 <= by2 <= ay2:
                return s - (bx2 - bx1) * (by2 - by1)
            if bx2 >= ax2 and by2 <= ay2:
                return s - (ax2 - bx1) * (by2 - by1)
        if bx1 <= ax1 and by1 <= ay1:
            if bx2 <= ax1 or by2 <= ay1:
                return s
            if ax1 <= bx2 <= ax2 and by2 >= ay2:
                return s - (bx2 - ax1) * (ay2 - ay1)
            if bx2 >= ax2 and by2 >= ay2:
                return s - (ax2 - ax1) * (ay2 - ay1)
            if ax1 <= bx2 <= ax2 and ay1 <= by2 <= ay2:
                return s - (bx2 - ax1) * (by2 - ay1)
            if bx2 >= ax2 and ay1 <= by2 <= ay2:
                return s - (ax2 - ax1) * (by2 - ay1)
        if ax1 <= bx1 <= ax2 and by1 <= ay1:
            if by2 <= ay1:
                return s
            if ax1 <= bx2 <= ax2 and by2 >= ay2:
                return s - (bx2 - bx1) * (ay2 - ay1)
            if bx2 >= ax2 and by2 >= ay2:
                return s - (ax2 - bx1) * (ay2 - ay1)
            if ax1 <= bx2 <= ax2 and ay1 <= by2 <= ay2:
                return s - (bx2 - bx1) * (by2 - ay1)
            if bx2 >= ax2 and ay1 <= by2 <= ay2:
                return s - (ax2 - bx1) * (by2 - ay1)


class Solution2:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        """This is the smarter way, which is from the official solution.

        The insight is that the width of the overlap area is always going to be
        w = min(ax2, bx2) - max(ax1, bx1) If w < 0, then there is no overlap.

        The height of the overlap area is
        h = min(ay2, by2) - max(ay1, by1) If h < 0, then there is no overlap

        95 ms, faster than 70.16% 
        """
        w = min(ax2, bx2) - max(ax1, bx1)
        h = min(ay2, by2) - max(ay1, by1)
        s = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if w < 0 or h < 0:
            return s
        return s - w * h






sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
