# from pudb import set_trace; set_trace()
from typing import List
import random
import math


class Solution1:
    """LeetCode 478

    This solution generates a random point in the square enclosing the circle
    We discard the point that is outside the circle and return the ones that are
    inside.

    We also perform the point generation on a circle centered in the origin, and
    simply add the given coordinates of the center to the generated points when
    they are returned.

    148 ms, 53% ranking.
    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center
        self.r_sqd = self.radius**2

    def randPoint(self) -> List[float]:
        while True:
            x = random.uniform(-self.radius, self.radius)
            y = random.uniform(-self.radius, self.radius)
            if x**2 + y**2 <= self.r_sqd:
                return x + self.x_center, y + self.y_center


class Solution2:
    """Using polar coordinates

    There is a trick here: use sqrt(random()) when generating r. Read this post
    for a rigorous proof: https://leetcode.com/problems/generate-random-point-in-a-circle/discuss/1113679/Python-Polar-coordinates-explained-with-diagrams-and-math

    For a visual guide on how the inverse transform sampling, read this:
    https://meyavuz.wordpress.com/2018/11/15/generate-uniform-random-points-within-a-circle/
    """

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        r = math.sqrt(random.random()) * self.radius
        a = random.uniform(0, 2 * math.pi)
        return self.x_center + r * math.cos(a), self.y_center + r * math.sin(a)


# sol = Solution3()
# tests = [
#     ('abab', True),
#     ('aba', False),
#     ('abcabcabcabc', True),
#     ('abcabcababcabcab', True),
#     ('abcbac', False),
#     ('aabaabaab', True),
#     ('a', False),
#     ('aaaaaaa', True),
#     ('aaaaab', False),
# ]

# for i, (s, ans) in enumerate(tests):
#     res = sol.repeatedSubstringPattern(s)
#     if res == ans:
#         print(f'Test {i}: PASS')
#     else:
#         print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
