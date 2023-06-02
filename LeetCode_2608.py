# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        dists = [0] * n
        visited = set()
        self.res = math.inf

        def dfs(node: int, d: int, par: int) -> None:
            visited.add(node)
            if dists[node]:
                if d > dists[node]:  # cycle found
                    self.res = min(self.res, d - dists[node])
            else:
                dists[node] = d
                for nei in graph[node]:
                    if nei != par:
                        dfs(nei, d + 1, node)
                dists[node] = 0

        for i in range(n):
            if i not in visited:
                dfs(i, 1, -1)
        return self.res if self.res < math.inf else -1
        

sol = Solution()
tests = [
    (7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]], 3),
    (4, [[0,1],[0,2]], -1),
    (8, [[0,1],[1,2],[2,3],[3,4],[4,5],[0,7],[0,6],[5,7],[5,6]], 4),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findShortestCycle(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
