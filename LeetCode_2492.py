# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class DSU:
    def __init__(self, n: int):
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
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """Union find everything. Then try the smallest distance and see if its
        nodes are in the union of cities 1 and n.

        1602 ms, faster than 100.00%
        """
        dsu = DSU(n + 1)
        for a, b, _ in roads:
            dsu.union(a, b)
        for a, b, dis in sorted(roads, key=lambda tup: tup[2]):
            if dsu.find(1) == dsu.find(a):
                return dis


class Solution2:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """BFS. Just visit all the nodes that can be reached from node 1, and
        pick the smallest edge

        NOTE: the visited has to check on edges. And since we only want to visit
        each edge once, we have to put both (a, b) and (b, a) as edges into the
        visited set when either of them is encountered.

        O(M), where M = len(roads). 6686 ms, faster than 11.11%
        """
        graph = defaultdict(list)
        for a, b, dis in roads:
            graph[a].append((b, dis))
            graph[b].append((a, dis))
        # BFS
        queue = [1]
        visited = set()  # record visited edges
        res = math.inf
        while queue:
            tmp = []
            for a in queue:
                for b, dis in graph[a]:
                    if (a, b) not in visited and (b, a) not in visited:
                        tmp.append(b)
                        visited.add((a, b))
                        visited.add((b, a))
                        res = min(res, dis)
            queue = tmp
        return res


sol = Solution2()
tests = [
    (4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]], 5),
    (4, [[1,2,2],[1,3,4],[3,4,7]], 2),
    (7, [[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]], 579),
]

for i, (n, roads, ans) in enumerate(tests):
    res = sol.minScore(n, roads)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
