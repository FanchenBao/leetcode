# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """LeetCode 1971

        DFS

        O(N), 2703 ms, faster than 71.92%
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int, visited) -> bool:
            if node == destination:
                return True
            if node in visited:
                return False
            visited.add(node)
            for child in graph[node]:
                if dfs(child, visited):
                    return True
            return False

        return dfs(source, set())


sol = Solution()
tests = [
    (3, [[0,1],[1,2],[2,0]], 0, 2, True),
    (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5, False),
]

for i, (n, edges, source, destination, ans) in enumerate(tests):
    res = sol.validPath(n, edges, source, destination)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
