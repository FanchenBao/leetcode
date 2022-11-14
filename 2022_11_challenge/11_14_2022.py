# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution1:
    def removeStones(self, stones: List[List[int]]) -> int:
        """LeetCode 947

        Turn this problem into a graph. The stones on the same row and col are
        connected. We can see that all the nodes in a connected graph can be
        removed, except for one. Thus, the problem is to find the total number
        of cliques in the graph and the number of nodes in each clique.

        O(N^2), 206 ms, faster than 86.23%
        """
        rows, cols = defaultdict(list), defaultdict(list)
        adj = defaultdict(list)
        for i, (x, y) in enumerate(stones):
            for j in rows[x]:
                adj[i].append(j)
                adj[j].append(i)
            rows[x].append(i)
            for j in cols[y]:
                adj[i].append(j)
                adj[j].append(i)
            cols[y].append(i)


        def dfs(node: int, visited) -> None:
            if node in visited:
                return
            visited.add(node)
            for nei in adj[node]:
                dfs(nei, visited)


        visited = set()
        res = pre = 0
        for i in adj.keys():
            dfs(i, visited)
            cur = len(visited)
            if cur > pre:
                res += cur - pre - 1
                pre = cur
        return res


class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        """Direct DFS without creating the adj list

        O(N^2)
        """

        def dfs(idx: int, unvisited) -> None:
            if idx not in unvisited:
                return
            unvisited.remove(idx)
            for i in list(unvisited):
                if stones[idx][0] == stones[i][0]:
                    dfs(i, unvisited)
                if stones[idx][1] == stones[i][1]:
                    dfs(i, unvisited)

        unvisited = set(range(len(stones)))
        res, pre = 0, len(stones)
        for i in range(len(stones)):
            if i in unvisited:
                dfs(i, unvisited)
                cur = len(unvisited)
                if cur < pre:
                    res += pre - cur - 1
                    pre = cur
        return res



class DSU:
    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already unioned
        if self.rnk[px] > self.rnk[py]:
            self.par[py] = px
        elif self.rnk[px] < self.rnk[py]:
            self.par[px] = py
        else:
            self.par[py] = px
            self.rnk[px] += 1


class Solution3:
    def removeStones(self, stones: List[List[int]]) -> int:
        """DSU solution.

        Use union-find to obtain the number of members in each clique.

        O(N^2)
        """
        dsu = DSU(len(stones))
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    dsu.union(i, j)
        counter = Counter()
        for i in range(len(stones)):
            counter[dsu.find(i)] += 1
        return sum(v - 1 for v in counter.values())
        

sol = Solution3()
tests = [
    ([[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]], 5),
    ([[0,0],[0,2],[1,1],[2,0],[2,2]], 3),
    ([[0,0]], 0)
]

for i, (stones, ans) in enumerate(tests):
    res = sol.removeStones(stones)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
