# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        """We use a hashmap. The first level has point index as key, and the
        value is the second level hashmap. In the second level, we have
        distance as key, and the number of points that have such distance as
        values. This set up gives us the number of points that are a certain
        distance away from any points[i]. If this number is larger than 1, then
        any permutation of the other points can be counted as boomerangs.

        O(N^2), 904 ms, 94% ranking.
        """
        res = 0
        hashmap = defaultdict(lambda: defaultdict(int))
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = (x2 - x1)**2 + (y2 - y1)**2
                hashmap[i][dist] += 1
                hashmap[j][dist] += 1
            res += sum(cnt * (cnt - 1) for cnt in hashmap[i].values() if cnt > 1)
        return res


sol = Solution()
tests = [
    ([[0,0],[1,0],[2,0]], 2),
    ([[1,1],[2,2],[3,3]], 2),
    ([[1,1]], 0)
]

for i, (points, ans) in enumerate(tests):
    res = sol.numberOfBoomerangs(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
