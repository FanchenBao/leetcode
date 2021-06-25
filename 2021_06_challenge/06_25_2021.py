# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution1:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """LeetCode 684

        The idea is to DFS the graph and identify the loop contained within
        it. Then we know severing any edge within the loop would satisfy the
        requirement of bringing the graph back into a tree. The tricky part is
        to find the edge with the largest index in edges. We can rely on the
        unwinding of stack in recursion to track the largest index of each edge
        inside the loop. One tricky part that got me was that I did not stop
        the tracking once all the edges in the loop have been considered. To
        resolve that, I have to set up a sentinel self.loop_start,
        which is used to identify when we have counted all the edges in the loop.

        O(N), because each node in the graph is only visited once.
        44 ms, 99% ranking.
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        indices_map = {a + (b * 1j): i for i, (a, b) in enumerate(edges)}

        self.max_idx, self.loop_start = -1, 0
        visited = set()

        def dfs(parent, node) -> bool:
            if node in visited:
                self.loop_start = node
                return True
            visited.add(node)
            for child in graph[node]:
                if child == parent:
                    continue
                if dfs(node, child):
                    if self.loop_start > 0:
                        self.max_idx = max(
                            self.max_idx,
                            indices_map[min(node, child) + max(node, child) * 1j],
                        )
                        if node == self.loop_start:
                            self.loop_start = 0
                    return True
            return False

        dfs(0, 1)
        return edges[self.max_idx]


class DSU:
    """Disjoint Set Union.

    It supports union and find in log(N) time. It has rank and path compression.
    Shamelessly copied from:

    https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained

    Update 06/25/2021: Improved functionality by returning boolean value in
    self.union function. Reference:

    https://leetcode.com/problems/redundant-connection/solution/
    """

    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            elif self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr
            else:
                self.par[yr] = xr
                self.rnk[xr] += 1
            return True
        return False  # x, y already in the same union


class Solution2:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """I gave Union Find a teeny tiny consideration before ditching it. This
        proved wrong. I should've spent more time thinking about using Union
        Find. The idea is very simple. For any two nodes, if they currently do
        not belong to the same union, we union them. If they already belong to
        the same union, then their edge must be the one to sever. Since we go
        from the beginning of edges, the first such redundant edge is the one
        we are looking for.

        ~O(N)
        """
        dsu = DSU(len(edges) + 1)
        for a, b in edges:
            if not dsu.union(a, b):
                return [a, b]


sol = Solution2()
tests = [
    ([[1, 2], [1, 3], [2, 3]], [2, 3]),
    ([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]], [1, 4]),
    ([[2, 7], [7, 8], [3, 6], [2, 5], [6, 8], [4, 8], [2, 8], [1, 8], [7, 10], [3, 9]], [2, 8]),
]

for i, (edges, ans) in enumerate(tests):
    res = sol.findRedundantConnection(edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
