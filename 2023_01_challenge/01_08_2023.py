# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class DSU:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.rnk = [0] * n

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rnk[px] > self.rnk[py]:
            self.par[py] = px
        elif self.rnk[px] < self.rnk[py]:
            self.par[px] = py
        else:
            self.rnk[px] += 1
            self.par[py] = px
        return True


class Solution1:
    def maxPoints(self, points: List[List[int]]) -> int:
        """LeetCode 149

        Solved this last time in January 2019, with cpp, and much much faster.
        I am pretty sure this is not the way to go. I basically use Union Find
        for each possible slope. Then we identify the max number of memebers in
        each union find.

        O(N^2 * union-find), 3344 ms, faster than 5.85% 
        """
        N = len(points)
        if N == 1:
            return 1
        slopemap = defaultdict(lambda: DSU(N))
        for i in range(N):
            for j in range(i + 1, N):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                g = math.gcd(abs(dx), abs(dy))
                k = (dx // g, dy // g)
                slopemap[k].union(i, j)
        return max(Counter(dsu.find(i) for i in range(N)).most_common(1)[0][1] for dsu in slopemap.values())



class Solution2:
    def maxPoints(self, points: List[List[int]]) -> int:
        """We set each point as the starting point, and check its slope against
        all the other points. Record the number of points that can form the same
        slope with the current point.

        We keep track the max count of points among all the slope when starting
        at each point. The result must be the max among the max count.

        O(N^2), 148 ms, faster than 64.26%
        """
        N = len(points)
        if N == 1:
            return 1
        res = 0
        for i in range(N):
            slopemap = Counter()
            for j in range(N):
                if i == j:
                    continue
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                g = math.gcd(abs(dx), abs(dy))
                k = (dx // g, dy // g)
                slopemap[k] += 1
            res = max(res, slopemap.most_common(1)[0][1] + 1)
        return res


sol = Solution2()
tests = [
    ([[1,1],[2,2],[3,3]], 3),
    ([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]], 4),
    ([[0,0]], 1),
    ([[0,0], [1,1]], 2),
]

for i, (points, ans) in enumerate(tests):
    res = sol.maxPoints(points)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
