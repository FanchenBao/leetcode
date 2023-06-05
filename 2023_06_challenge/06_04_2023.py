# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """LeetCode 547

        Find the total number of connected cliques in the graph.

        O(N^2), 194 ms, faster than 62.73%
        """
        graph = defaultdict(list)
        N = len(isConnected)
        for i in range(N):
            for j in range(i + 1, N):
                if isConnected[i][j]:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()

        def dfs(node: int) -> None:
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        res = 0
        for i in range(N):
            if i not in visited:
                dfs(i)
                res += 1
        return res
        

sol = Solution()
tests = [
    ([[1,1,0],[1,1,0],[0,0,1]], 2),
    ([[1,0,0],[0,1,0],[0,0,1]], 3),
]

for i, (isConnected, ans) in enumerate(tests):
    res = sol.findCircleNum(isConnected)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
