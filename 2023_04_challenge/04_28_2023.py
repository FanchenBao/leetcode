# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class DSU:
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
    def is_sim(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        return sum(a != b for a, b in zip(s1, s2)) <= 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        """LeetCode 839

        The grouping part can be resolved by union and find. Thus the only thing
        we need to worry about is determining whether two strings are similar.

        Two strings are similar if their differences are smaller or equal to 2.

        Also, we have to compress the path at the end to make sure each
        element's parent has been fully determined.

        O(N^2 * (union + M)), 2021 ms, 24.92%
        """
        N = len(strs)
        dsu = DSU(N)
        for i in range(N):
            for j in range(i + 1, N):
                if self.is_sim(strs[i], strs[j]):
                    dsu.union(i, j)
        # compress path one more time
        for i in range(N):
            dsu.find(i)
        return len(set(dsu.par))


class Solution2:
    def is_sim(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        return sum(a != b for a, b in zip(s1, s2)) <= 2

    def numSimilarGroups(self, strs: List[str]) -> int:
        """DFS solution.

        Each pair that is similar can form an edge. Then we traverse the graph
        to find all the cliques.

        O(N^2*M), 2012 ms, faster than 25.24% 
        """
        graph = defaultdict(list)
        N = len(strs)
        for i in range(N):
            for j in range(i + 1, N):
                if self.is_sim(strs[i], strs[j]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()

        def dfs(node: int) -> None:
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    dfs(child)

        res = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                res += 1
        return res


sol = Solution2()
tests = [
    (["tars","rats","arts","star"], 2),
    (["omv","ovm"], 1),
]

for i, (strs, ans) in enumerate(tests):
    res = sol.numSimilarGroups(strs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
