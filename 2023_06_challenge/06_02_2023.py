# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        """LeetCode 2101

        Very fun problem. We can convert the bomb detonation relationship to a
        directed graph. Then the problem is converted to finding the size of
        the largest connected graph.

        Converting the bombs to graph takes O(N^2).

        Finding the largest connected graph also takes O(N^3), because the number
        of edges is to the order of O(N^2).

        806 ms, faster than 64.35%
        """
        graph = defaultdict(list)
        N = len(bombs)
        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, r2) in enumerate(bombs):
                if i != j:
                    if r1**2 >= (x2 - x1)**2 + (y2 - y1)**2:
                        graph[i].append(j)

        def dfs(node: int, visited) -> int:
            visited.add(node)
            num_nodes = 1
            for nei in graph[node]:
                if nei not in visited:
                    num_nodes += dfs(nei, visited)
            return num_nodes

        res = 0
        for node in range(N):
            res = max(res, dfs(node, set()))
        return res


sol = Solution()
tests = [
    ([[2,1,3],[6,1,4]], 2),
    ([[1,1,5],[10,10,5]], 1),
    ([[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]], 5),
]

for i, (bombs, ans) in enumerate(tests):
    res = sol.maximumDetonation(bombs)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
