# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict



class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        """LeetCode 2492

        The smallest score is the shortest path in the connected graph that
        includes 1 and n. Thus, we just need to traverse the entire graph
        starting from 1, and find the min of the distance along the way.

        O(N + E), 1788 ms, faster than 66.11% 
        """
        scores = set()
        visited = set()
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))

        def dfs(i: int) -> None:
            if i not in visited:
                visited.add(i)
                for j, d in graph[i]:
                    scores.add(d)
                    dfs(j)

        dfs(1)
        return min(scores)
        

sol = Solution()
tests = [
    (4, [[1,2,9],[2,3,6],[2,4,5],[1,4,7]], 5),
    (4, [[1,2,2],[1,3,4],[3,4,7]], 2),
    (3, [[3,2,1],[1,3,3]], 1),
]

for i, (n, roads, ans) in enumerate(tests):
    res = sol.minScore(n, roads)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
