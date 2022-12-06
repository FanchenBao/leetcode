# from pudb import set_trace; set_trace()
from typing import List, Dict
import math
from collections import defaultdict


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


class Solution:
    def max_lvl(self, nodes: List[int], graph: Dict[int, List[int]]) -> int:
        res = -1
        for i in nodes:
            queue = {i}
            visited = set()
            lvl = 0
            while queue:
                tmp = set()
                lvl += 1
                for node in queue:
                    visited.add(node)
                    for nn in graph[node]:
                        if nn not in visited:
                            if nn in queue:
                                return -1
                            tmp.add(nn)
                queue = tmp
            res = max(res, lvl)
        return res

    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        """The problem can be converted to finding the max level (height) of a
        graph. Given that n <= 500, we can choose any node as the starting node
        and run BFS to find the max level we can reach in that configuration.

        Two tricky parts. First, we have to also make sure that none of the
        nodes on the same level connect with each other. If there is connection,
        this configuration is impossible.

        Two, since the graph can be disconnected, we need to run the BFS on each
        connected clique, and add the max levels of all the cliques together.
        The caveat is that if one clique is impossible to form magnificent sets,
        then we must return -1 immediately.

        To find all the cliques, we can use our best friend union-find.
        
        O(N^2), 3160 ms, faster than 81.53%
        
        UPDATE: the max_lvl method can return -1 immediately. No need to use
        a flag `impossible`.
        """
        dsu = DSU(n + 1)
        for a, b in edges:
            dsu.union(a, b)

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        groups = defaultdict(list)
        for i in range(1, n + 1):
            groups[dsu.find(i)].append(i)

        res = 0
        for g in groups.values():
            cur_max_lvl = self.max_lvl(g, graph)
            if cur_max_lvl == -1:  # not possible to form magnificant sets with g
                return -1
            res += cur_max_lvl
        return res


sol = Solution()
tests = [
    (6, [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]], 4),
    (3, [[1,2],[2,3],[3,1]], -1),
    (92, [[67,29],[13,29],[77,29],[36,29],[82,29],[54,29],[57,29],[53,29],[68,29],[26,29],[21,29],[46,29],[41,29],[45,29],[56,29],[88,29],[2,29],[7,29],[5,29],[16,29],[37,29],[50,29],[79,29],[91,29],[48,29],[87,29],[25,29],[80,29],[71,29],[9,29],[78,29],[33,29],[4,29],[44,29],[72,29],[65,29],[61,29]], 57),
    (32, [[29,12],[29,9],[17,11],[1,9],[31,19],[22,1],[11,1],[3,16],[28,3],[15,30],[28,17],[14,17],[1,7],[20,22],[3,25],[16,19],[13,22],[18,28],[5,13],[3,32],[22,29],[14,25],[20,11],[21,27],[26,9],[20,31],[11,21],[31,11],[30,11],[5,20],[9,3],[12,16],[20,6],[1,28],[3,26],[28,21],[24,28],[11,14],[32,10],[29,13],[7,12],[1,21],[10,25],[24,15],[11,16],[28,22],[15,28],[10,24],[3,27],[27,2]], -1),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.magnificentSets(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
