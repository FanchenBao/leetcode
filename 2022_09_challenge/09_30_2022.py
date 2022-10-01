# from pudb import set_trace; set_trace()
from typing import List
import math
from bisect import bisect_right


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        """LeetCode 218

        My God. I did it by myself. Could've passed on the first try, but got
        a little confused about the first if condition. It was fixed very
        quickly.

        This solution is pure analysis. We sort the buildings in descent for
        heights, and if heights are the same, sort left ascend.

        Then we build the range for each contour. We use the left bound as key,
        and the value is [right bound, left height, right height]

        For each new building, we sort the keys, so that we can use binary
        search to see where the new building shall be placed. Since the height
        of the new building is not heigher than all the existing contours,
        any time the new building has left or right side stuck out, we record
        the results. Also, if the new building touches or merges with some of
        the existing contour, we update the contour or delete it.

        It's convoluted, but it can be done if one is patient enough.

        106 ms, faster than 99.75%
        """
        buildings.sort(key=lambda lst: (lst[2], -lst[0]), reverse=True)
        # the values are [right bound, left height, right height]
        left_bounds = {buildings[0][0]: [buildings[0][1], buildings[0][2], buildings[0][2]]}
        res = [[buildings[0][0], buildings[0][2]]]
        for l, r, h in buildings[1:]:
            sorted_left = sorted(left_bounds)
            idx = bisect_right(sorted_left, l)
            if idx == len(sorted_left) and l > left_bounds[sorted_left[idx - 1]][0]:
                pl = sorted_left[idx - 1]
                pr, plh, prh = left_bounds[pl]
                if pr < l:
                    res.append([l, h])
                    left_bounds[l] = [r, h, h]
                else:
                    left_bounds[pl][0] = r
                    if prh > h:
                        res.append([pr, h])
                        left_bounds[pl][0] = r
                        left_bounds[pl][2] = h
            elif idx == 0:
                res.append([l, h])
                if r < sorted_left[0]:
                    left_bounds[l] = [r, h, h]
                else:
                    some_r_bigger = False
                    for sl in sorted_left:
                        if left_bounds[sl][0] < r:
                            if left_bounds[sl][2] > h:
                                res.append([left_bounds[sl][0], h])
                            del left_bounds[sl]
                        else:
                            some_r_bigger = True
                            break
                    if not some_r_bigger or r < sl:
                        left_bounds[l] = [r, h, h]
                    else:
                        left_bounds[l] = [left_bounds[sl][0], h, left_bounds[sl][2]]
                        del left_bounds[sl]
            else:
                pl = sorted_left[idx - 1]
                if r <= left_bounds[pl][0]:
                    continue
                if l > left_bounds[pl][0]:
                    res.append([l, h])
                elif left_bounds[pl][2] > h:
                    res.append([left_bounds[pl][0], h])
                i = idx
                some_r_bigger = False
                while i < len(sorted_left):
                    sl = sorted_left[i]
                    if left_bounds[sl][0] < r:
                        if left_bounds[sl][2] > h:
                            res.append([left_bounds[sl][0], h])
                        del left_bounds[sl]
                    else:
                        some_r_bigger = True
                        break
                    i += 1
                if not some_r_bigger or r < sorted_left[i]:
                    if l > left_bounds[pl][0]:
                        left_bounds[l] = [r, h, h]
                    else:
                        left_bounds[pl][0] = r
                        left_bounds[pl][2] = h
                else:
                    sl = sorted_left[i]
                    if l > left_bounds[pl][0]:
                        left_bounds[l] = [left_bounds[sl][0], h, left_bounds[sl][2]]
                    else:
                        left_bounds[pl][0] = left_bounds[sl][0]
                        left_bounds[pl][2] = left_bounds[sl][2]
                    del left_bounds[sl]
            # print(l, r, h)
            # print(left_bounds)
        for r, _, _ in left_bounds.values():
            res.append([r, 0])
        return sorted(res)


sol = Solution()
tests = [
    ([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]], [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]),
    ([[0,2,3],[2,5,3]], [[0,3],[5,0]]),
    ([[1,2,1],[1,2,2],[1,2,3]], [[1,3],[2,0]]),
    ([[1,2,1],[1,2,2],[1,2,3],[2,3,1],[2,3,2],[2,3,3]], [[1,3],[3,0]]),
]

for i, (buildings, ans) in enumerate(tests):
    res = sol.getSkyline(buildings)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
