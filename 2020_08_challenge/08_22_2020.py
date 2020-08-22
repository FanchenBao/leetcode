# from pudb import set_trace; set_trace()
from typing import List
from random import randrange, randint, choices
from collections import Counter
from bisect import bisect_right


"""
I spent way too long on this problem because I was misled by an expected
output, and because I forgot to include the edges when working on my first
serialization solution.

The misleading output shows that the smaller rect gets the same number of hits
as the larger one. This indicates that a full serialized solution would be
wrong. I was stuck there for a LONG time, until I checked the solution and
found that fully serialized method is correct. This can only mean that the
output was misleading.
"""


class Solution1:
    """Fully serialize all points.

    To save space, only the start and end points are used.
    """

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.serial, self.range = self.serialize()

    def serialize(self):
        serial = []
        pre = 0
        for i, rect in enumerate(self.rects):
            x1, y1, x2, y2 = rect
            serial.append(
                (pre, pre + (x2 - x1 + 1) * (y2 - y1 + 1)),
            )
            pre = serial[-1][1]
        print(serial)
        return serial, (0, serial[-1][1])

    def find_idx(self, sel):
        for i, (l, r) in enumerate(self.serial):
            if l <= sel < r:
                return i

    def pick(self) -> List[int]:
        sel = randrange(*self.range)
        idx = self.find_idx(sel)
        x1, y1, x2, y2 = self.rects[idx]
        return [randint(x1, x2), randint(y1, y2)]


class Solution2:
    """Use weights to select rects"""

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]

    def pick(self) -> List[int]:
        rect = choices(self.rects, weights=self.weights)[0]
        return [randint(rect[0], rect[2]), randint(rect[1], rect[3])]


class Solution3:
    """Full serialize but use bisect to locate target rect.

    And use random function ONLY ONCE.
    """

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.ranges = self.get_ranges()

    def get_ranges(self):
        ranges = [0]
        for x1, y1, x2, y2 in self.rects:
            ranges.append(ranges[-1] + (x2 - x1 + 1) * (y2 - y1 + 1))
        return ranges

    def pick(self) -> List[int]:
        target = randrange(0, self.ranges[-1])
        idx = bisect_right(self.ranges, target)
        n = target - self.ranges[idx - 1]
        x1, y1, x2, y2 = self.rects[idx - 1]
        dy, dx = divmod(n, x2 - x1 + 1)
        return [x1 + dx, y1 + dy]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
def print_res(lst):
    res = [tuple(l) for l in lst]
    res_count = Counter(res)
    for p in sorted(res_count.keys(), key=lambda x: (x[0], x[1])):
        print(f'{p}: {res_count[p]}')


rects = [
    [82918473, -57180867, 82918476, -57180863],
    [83793579, 18088559, 83793580, 18088560],
    [66574245, 26243152, 66574246, 26243153],
    [72983930, 11921716, 72983934, 11921720],
]
sol = Solution3(rects)
# sol.pick()
res = [sol.pick() for _ in range(10000)]

print_res(res)
