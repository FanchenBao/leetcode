# from pudb import set_trace; set_trace()
from typing import List, Set
from functools import lru_cache


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """LeetCode 797

        DFS with cache.

        O(2^N), 104 ms, 53% ranking.
        """
        N = len(graph)
        
        @lru_cache(maxsize=None)
        def dfs(node: int) -> List[List[int]]:
            if node == N - 1:
                return [[node]]
            res = []
            for nei in graph[node]:
                res.extend([[node] + path for path in dfs(nei)])
            return res

        return dfs(0)


sol = Solution()
tests = [
    ([[4,3,1],[3,2,4],[3],[4],[]], [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]),
    ([[1,2],[3],[3],[]], [[0,1,3],[0,2,3]]),
    ([[1],[]], [[0,1]]),
    ([[1,2,3],[2],[3],[]], [[0,1,2,3],[0,2,3],[0,3]]),
    ([[1,3],[2],[3],[]], [[0,1,2,3],[0,3]]),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.allPathsSourceTarget(graph)
    if sorted(res) == sorted(ans):
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
