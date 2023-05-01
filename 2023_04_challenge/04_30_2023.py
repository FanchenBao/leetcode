# from pudb import set_trace; set_trace()
from typing import List
import math


class DSU1:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1
            return True
        return False


class Solution1:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """LeetCode 1579

        The challenge yesterday definitely helps, because it points us to the
        right direction when solving this problem. Immediately, I go for union
        find to check for connectedness. There is also a bit greedy here,
        because I always want to use type 3 edges first. After exhausting all
        type 3 edges, we then try to put in type 1 and type 2.

        Use two separate union and find for Alice and Bob. We include edges that
        connect nodes not connected already, and discard the ones that connect
        nodes that have already been connected. This way, the final edges
        included are the minimum amount of edges to allow the graph to be
        connected.

        O(E + N + E * Union + N * Find) = O(E + N), 2320 ms, faster than 25.79% 
        """
        dsu_a, dsu_b = DSU1(n + 1), DSU1(n + 1)
        discarded = 0
        edges_a, edges_b = [], []
        for t, a, b in edges:  # take full advantage of all type 3 edges
            if t == 1:
                edges_a.append((a, b))
            elif t == 2:
                edges_b.append((a, b))
            else:
                if not dsu_a.union(a, b):
                    discarded += 1
                dsu_b.union(a, b)
        for a, b in edges_a:
            if not dsu_a.union(a, b):
                discarded += 1
        for a, b in edges_b:
            if not dsu_b.union(a, b):
                discarded += 1
        # check if all the nodes are connected
        for i in range(1, n + 1):
            dsu_a.find(i)
            dsu_b.find(i)
        # the total number of groups in the DSU must be two, because node 0 is
        # not part of the graph
        return discarded if len(set(dsu_a.par)) == len(set(dsu_b.par)) == 2 else -1


class DSU2:
    def __init__(self, N: int) -> None:
        """This DSU contains ifo about the number of components, so we don't
        have to compute it again.
        """
        self.par = list(range(N))
        self.rnk = [0] * N
        self.components = N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px != py:
            if self.rnk[px] > self.rnk[py]:
                self.par[py] = px
            elif self.rnk[px] < self.rnk[py]:
                self.par[px] = py
            else:
                self.par[py] = px
                self.rnk[px] += 1
            # if two nodes need to be unioned, the number of total components
            # must decrease by one
            self.components -= 1
            return True
        return False


class Solution2:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """UPDATE: use DSU2 where we keep track of the number of components in
        DSU, such that we don't have to check at the end.

        Also, we won't bother separating type 1 and type 2 edges in additional
        space.

        O(E + N + E * Union), 2226 ms, faster than 47.80%
        """
        dsu_a, dsu_b = DSU2(n + 1), DSU2(n + 1)
        discarded = 0
        for t, a, b in edges:  # take full advantage of all type 3 edges
            if t == 3:
                if not dsu_a.union(a, b):
                    discarded += 1
                dsu_b.union(a, b)
        for t, a, b in edges:
            if t == 1:
                if not dsu_a.union(a, b):
                    discarded += 1
            elif t == 2:
                if not dsu_b.union(a, b):
                    discarded += 1
        # the final number of components is two, because node 0 is not in the
        # graph
        return discarded if dsu_a.components == dsu_b.components == 2 else -1


sol = Solution2()
tests = [
    (4, [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]], 2),
    (4, [[3,1,2],[3,2,3],[1,1,4],[2,1,4]], 0),
    (4, [[3,2,3],[1,1,2],[2,3,4]], -1),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.maxNumEdgesToRemove(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
