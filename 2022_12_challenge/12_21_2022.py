# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """LeetCode 886

        Form a graph, each edge is a pair of disliking people. Traverse the
        graph and assign each person a label. Partition is not possible if a
        loop forms and the start of the loop belongs to different labels.

        O(N + E), 1850 ms, faster than 40.30%
        """
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        visited = {}

        def dfs(idx: int, lab: int) -> bool:
            if idx in visited:
                return lab == visited[idx]
            visited[idx] = lab
            for nex in graph[idx]:
                if not dfs(nex, lab * (-1)):
                    return False
            return True

        for i in range(1, n + 1):
            if i not in visited and not dfs(i, 1):
                return False
        return True


class DSU:
    def __init__(self, n:int):
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


class Solution2:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        """Union Find method.

        Group all the neighbors together, and check whether the current node
        is in the same group as the neighbors.

        1366 ms, faster than 62.89% 
        """
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)

        dsu = DSU(n + 1)
        for k, v in graph.items():
            for i in range(1, len(v)):
                dsu.union(v[0], v[i])
            if dsu.find(k) == dsu.find(v[0]):
                return False
        return True


sol = Solution2()
tests = [
    (4, [[1,2],[1,3],[2,4]], True),
    (3, [[1,2],[1,3],[2,3]], False),
    (5, [[1,2],[2,3],[3,4],[4,5],[1,5]], False),
]

for i, (n, dislikes, ans) in enumerate(tests):
    res = sol.possibleBipartition(n, dislikes)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
