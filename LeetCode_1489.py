# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU:
    def __init__(self, n: int) -> None:
        self.par = list(range(n))
        self.cnt = [1] * n  # self.cnt[i] counts the number of nodes in the graph rooted at i

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.cnt[px] >= self.cnt[py]:
            self.par[py] = px
            self.cnt[px] += self.cnt[py]
        else:
            self.par[px] = py
            self.cnt[py] += self.cnt[px]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        """Python implementation. It is cleaner than the Java one, because the
        find_mst_weight function input only requires one init_edge and one
        banned_edge (the Java version uses HashSet for both).

        O(N^2 * UnionFind), 834 ms, faster than 85.18%
        """
        sortedEdges = sorted([w, a, b, i] for i, (a, b, w) in enumerate(edges))
        def find_mst_weight(init_edge: int, banned_edge: int) -> int:
            dsu = DSU(n)
            edge_cnt = 0
            weight = 0
            if init_edge >= 0:
                dsu.union(edges[init_edge][0], edges[init_edge][1])
                edge_cnt += 1
                weight += edges[init_edge][2]
            for w, a, b, i in sortedEdges:
                if edge_cnt == n - 1:
                    break
                if i != banned_edge and dsu.union(a, b):
                    weight += w
                    edge_cnt += 1
            return weight if edge_cnt == n - 1 and dsu.cnt[dsu.find(0)] == n else math.inf

        min_w = find_mst_weight(-1, -1)
        criticals = set()
        for i in range(len(edges)):
            if find_mst_weight(-1, i) > min_w:
                criticals.add(i)
        pseudo_criticals = []
        for i in range(len(edges)):
            if i not in criticals and find_mst_weight(i, -1) == min_w:
                pseudo_criticals.append(i)
        return [list(criticals), pseudo_criticals]


        

sol = Solution()
tests = [
    # (5, [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]], [[0,1],[2,3,4,5]]),
    (6, [[0,1,1],[1,2,1],[0,2,1],[2,3,4],[3,4,2],[3,5,2],[4,5,2]], [[3],[0,1,2,4,5,6]]),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findCriticalAndPseudoCriticalEdges(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
