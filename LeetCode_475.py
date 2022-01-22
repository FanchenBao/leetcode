# from pudb import set_trace; set_trace()
from typing import List
from bisect import bisect_right
import math


class Solution1:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """First remove dups and sort houses and heaters.

        Then consider heater one by one. The first heater produces two radii,
        one covers the left most house and the other the right most. We put
        both radii in an array min_radii. For each subsequent heater considered
        only the last radius in min_radii is disturbed. We pop the last radius
        and produce two more radii. One of them concerns covering the houses
        in between the current heater and the previous heater. This is a bit
        tricky to do but not too complex if one calms down and think it through.
        The other covers the right most house.

        We continue this pattern until all heaters are considered. The largest
        in min_radii is the answer.

        O(NlogN), 380 ms, 47% ranking.
        """
        sorted_houses = sorted(set(houses))
        sorted_heaters = sorted(set(heaters))
        pre_idx = bisect_right(sorted_houses, sorted_heaters[0]) - 1
        min_radii = [
            max(sorted_heaters[0] - sorted_houses[0], 0),
            max(sorted_houses[-1] - sorted_heaters[0], 0),
        ]
        for i in range(1, len(sorted_heaters)):
            idx = bisect_right(sorted_houses, sorted_heaters[i]) - 1
            min_radii.pop()
            min_between = math.inf
            for j in range(pre_idx + 1, idx + 2):
                # j is the index of the left most house within all the houses
                # enclosed by the previous and current heater that are to be
                # covered by the current heater.
                pre_inc = sorted_heaters[i - 1] if j == pre_idx + 1 else sorted_houses[j - 1]
                cur_inc = sorted_heaters[i] if j == idx + 1 else sorted_houses[j]
                # Compute the min radius needed for the previous and current
                # heater to cover all the houses in between.
                min_between = min(
                    min_between,
                    max(
                        pre_inc - sorted_heaters[i - 1],
                        sorted_heaters[i] - cur_inc,
                    ),
                )
            min_radii.append(min_between)
            # Cover the right most house, if applicable
            min_radii.append(max(sorted_houses[-1] - sorted_heaters[i], 0))
            pre_idx = idx
        return max(min_radii)


class Solution2:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        """Change perspective. Consider fiting houses to heaters, then the
        problem is vastly simplified

        Ref: https://leetcode.com/problems/heaters/discuss/95886/Short-and-Clean-Java-Binary-Search-Solution
        O(NlogN), 292 ms, 61% ranking
        """
        heaters.sort()
        N = len(heaters)
        res = 0
        for h in houses:
            idx = bisect_right(heaters, h)
            pre_heater = -math.inf if idx == 0 else heaters[idx - 1]
            post_heater = math.inf if idx == N else heaters[idx]
            res = max(res, min(h - pre_heater, post_heater - h))
        return res


sol = Solution2()
tests = [
    ([1, 2, 3], [2], 1),
    ([1, 2, 3, 4], [1, 4], 1),
    ([1, 5], [2], 3),
    ([1, 5], [10], 9),
]

for i, (houses, heaters, ans) in enumerate(tests):
    res = sol.findRadius(houses, heaters)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
