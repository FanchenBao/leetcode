# from pudb import set_trace; set_trace()
from typing import List, Tuple
from collections import deque
from functools import lru_cache
from itertools import chain


class Solution1:
    def __init__(self):
        self.MOD = 1000000007

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """
        LeetCode 850
        
        TLE
        """

        @lru_cache(None)
        def helper(rectangles: Tuple[Tuple]) -> int:
            """TLE"""
            x01, y01, x02, y02 = rectangles[0]
            area = ((x02 - x01) * (y02 - y01)) % self.MOD
            for i in range(1, len(rectangles)):
                xi1, yi1, xi2, yi2 = rectangles[i]
                overlaps = set()
                for j in range(i):
                    xj1, yj1, xj2, yj2 = rectangles[j]
                    if not (xi2 <= xj1 or xj2 <= xi1 or yi2 <= yj1 or yj2 <= yi1):
                        # there is overlap
                        overlaps.add((max(xi1, xj1), max(yi1, yj1), min(xi2, xj2), min(yi2, yj2)))
                # print(overlaps)
                if len(overlaps) == 1:
                    xo1, yo1, xo2, yo2 = list(overlaps)[0]
                    area += (xi2 - xi1) * (yi2 - yi1) % self.MOD - (xo2 - xo1) * (yo2 - yo1) % self.MOD
                elif len(overlaps) == 0:
                    area += (xi2 - xi1) * (yi2 - yi1) % self.MOD
                else:
                    area += ((xi2 - xi1) * (yi2 - yi1)) % self.MOD - self.rectangleArea(tuple(sorted(overlaps)))
            return area % self.MOD

        return helper(tuple(sorted(tuple(rec) for rec in rectangles)))


class Solution2:
    def __init__(self):
        self.MOD = 1000000007

    def find_area(self, xl: int, yl: int, top_rights: List[List[int]]) -> int:
        area = 0
        for xr, yr in top_rights:
            if xr >= xl and yr >= yl:
                area += (xr - xl) * (yr - yl) % self.MOD
            yl = yr
        return area % self.MOD

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """This one is close but still WRONG"""
        rectangles.sort(key=lambda rec: (rec[0], rec[1]))
        print(rectangles)
        xl, yl = rectangles[0][0], rectangles[0][1]
        top_rights = [[rectangles[0][2], rectangles[0][3]]]
        area = 0
        for x1, y1, x2, y2 in rectangles[1:]:
            temp = []
            new_top_right = True
            for xr, yr in top_rights:
                if x2 <= xr and y2 <= yr:
                    temp.append([xr, yr])
                    new_top_right = False
                elif x2 > xr and y2 > yr:
                    continue
                else:
                    temp.append([xr, yr])
            # old area minus the overlap
            area += (self.find_area(xl, yl, top_rights) - self.find_area(x1, max(y1, yl), top_rights)) % self.MOD
            xl, yl = x1, y1
            if new_top_right:
                temp.append([x2, y2])
            top_rights = sorted(temp, key=lambda par: par[1])
        return (area + self.find_area(xl, yl, top_rights)) % self.MOD


class Solution3:
    def __init__(self):
        self.MOD = 1000000007

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """coordinate compression

        https://leetcode.com/problems/rectangle-area-ii/discuss/1419181/Python-4-solutions-n3-greater-n2-log-n-greater-n2-greater-n-log-n-explained

        O(N^3), 172 ms
        """
        # xs and ys are unique x and y coordinates of all rectangles
        xs = sorted(set(chain(*[[x1, x2] for x1, y1, x2, y2 in rectangles])))
        ys = sorted(set(chain(*[[y1, y2] for x1, y1, x2, y2 in rectangles])))
        # mapping from x and y value to its index in xs and ys. These indices
        # form the compressed grid
        x_map = {v: i for i, v in enumerate(xs)}
        y_map = {v: i for i, v in enumerate(ys)}
        m, n = len(ys), len(xs)
        # check which cell in the compressed grid is occupied
        grid = [[0] * n for _ in range(m)]
        for x1, y1, x2, y2 in rectangles:
            for j in range(x_map[x1], x_map[x2]):
                for i in range(y_map[y1], y_map[y2]):
                    grid[i][j] = 1
        # compute area of all the compressed grid cells
        res = 0
        for i in range(m - 1):
            for j in range(n - 1):
                res = (res + grid[i][j] * (xs[j + 1] - xs[j]) * (ys[i + 1] - ys[i])) % self.MOD
        return res


class Solution4:
    def __init__(self):
        self.MOD = 1000000007

    def query(self, active_ranges: List[Tuple[int, int]]) -> int:
        rng = 0
        cur_l, cur_r = active_ranges[0]
        for l, r in active_ranges[1:]:
            if l > cur_r:
                rng += cur_r - cur_l
                cur_l, cur_r = l, r
            elif r > cur_r:
                cur_r = r
        return rng + cur_r - cur_l

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        """Merge interval

        https://leetcode.com/problems/rectangle-area-ii/solution/

        O(N^2logN), 44 ms.

        Sweeping line by line horizontally. For each line, we compute the active
        range of x via merging interval. The most important trick is to consider
        when a range is added and when it is removed. We use OPEN and CLOSE to
        indicate that the bottom of a rectangle is encountered, we add its x
        range. When its top is encountered, we remove the same range.
        """
        OPEN, CLOSE = 1, 0
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append((y1, OPEN, x1, x2))
            events.append((y2, CLOSE, x1, x2))
        events.sort()

        cur_y = events[0][0]
        active = [(events[0][2], events[0][3])]
        cur_x_rng = active[0][1] - active[0][0]
        res = 0
        for y, typ, x1, x2 in events[1:]:
            res += (y - cur_y) * cur_x_rng
            if typ:
                active.append((x1, x2))
                active.sort()
            else:
                active.remove((x1, x2))
            cur_x_rng = self.query(active) if active else 0
            cur_y = y
        return res % self.MOD


sol = Solution4()
tests = [
    ([[0, 0, 2, 2], [1, 0, 2, 3], [1, 0, 3, 1]], 6),
    ([[0, 0, 1000000000, 1000000000]], 49),
    ([[0, 0, 1, 1], [2, 2, 3, 3]], 2),
    ([[471, 0, 947, 999], [780, 0, 823, 320], [868, 0, 948, 538], [907, 0, 911, 673], [929, 0, 952, 596], [458, 0, 889, 669], [156, 0, 364, 754], [900, 0, 973, 236], [406, 0, 620, 454], [773, 0, 946, 538], [407, 0, 834, 23], [759, 0, 858, 526], [431, 0, 776, 599], [969, 0, 979, 30], [642, 0, 737, 339], [239, 0, 448, 183], [260, 0, 517, 903], [14, 0, 674, 976], [251, 0, 850, 112], [57, 0, 794, 395], [595, 0, 728, 149], [970, 0, 989, 36], [496, 0, 954, 791], [447, 0, 832, 805], [829, 0, 939, 100], [169, 0, 568, 501], [704, 0, 969, 411], [607, 0, 609, 221], [935, 0, 953, 437], [47, 0, 670, 130], [794, 0, 799, 230], [943, 0, 959, 90], [332, 0, 337, 732], [123, 0, 228, 344], [281, 0, 487, 598], [381, 0, 732, 443], [235, 0, 391, 548], [646, 0, 930, 20], [219, 0, 675, 95], [8, 0, 212, 227], [138, 0, 704, 658], [368, 0, 782, 707], [810, 0, 826, 957], [543, 0, 697, 654], [887, 0, 986, 180], [837, 0, 900, 228], [280, 0, 391, 331], [180, 0, 229, 42], [201, 0, 489, 687], [648, 0, 680, 732], [228, 0, 630, 922], [886, 0, 960, 56], [946, 0, 955, 522], [903, 0, 992, 464], [557, 0, 860, 38], [89, 0, 268, 642], [669, 0, 774, 185], [1, 0, 724, 374], [395, 0, 923, 782], [82, 0, 230, 550], [166, 0, 166, 808], [441, 0, 644, 435], [497, 0, 823, 224], [372, 0, 973, 556], [188, 0, 846, 127], [226, 0, 396, 535], [869, 0, 945, 575], [406, 0, 526, 795], [781, 0, 795, 569], [563, 0, 831, 991], [466, 0, 486, 641], [274, 0, 855, 529], [61, 0, 819, 364], [285, 0, 421, 101], [193, 0, 950, 748], [320, 0, 655, 836], [207, 0, 627, 945], [782, 0, 899, 56], [578, 0, 970, 913], [499, 0, 684, 205], [490, 0, 877, 16], [483, 0, 668, 915], [364, 0, 741, 16]], 957901),
    ([[47, 0, 94, 99], [78, 0, 82, 32], [86, 0, 94, 53], [90, 0, 91, 67]], 4653),
    ([[471, 0, 947, 999], [780, 0, 823, 320], [868, 0, 948, 538], [907, 0, 911, 673]], 476062),
    ([[0, 0, 3, 3], [2, 0, 5, 3], [1, 1, 4, 4]], 18),
]

for i, (rectangles, ans) in enumerate(tests):
    res = sol.rectangleArea(rectangles)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
