# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """LeetCode 785

        Definitely not a difficult one, but took me so long. I am not in the
        best shape today. I started with union and find, but that didn't work.
        Then I played around with sets, yet the naive way of setting up sets
        also doesn't work. Then I realize that we have to traverse the graph and
        use sets along the way. It works.

        O(N), 204 ms, faster than 17.47% 
        """
        N = len(graph)
        groups = [set(), set()]
        
        def dfs(node: int, group_idx: int) -> None:
            if node in groups[group_idx]:
                return
            groups[group_idx].add(node)
            for child in graph[node]:
                dfs(child, group_idx ^ 1)

        for i in range(N):
            if i not in groups[0] and i not in groups[1]:
                dfs(i, 0)
            if i in groups[0] and i in groups[1]:
                return False
        return True


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """Use coloring. Each time we visit a node, we change the color. Then
        we can decide whether the coloring is correct.

        O(N), 185 ms, faster than 46.22%
        """
        N = len(graph)
        colors = [0] * N

        def dfs(node: int, color: int) -> bool:
            if colors[node]:  # node has been visited, it must match the required color
                return colors[node] == color
            colors[node] = color
            for child in graph[node]:
                if not dfs(child, -color):
                    return False
            return True

        for i in range(N):
            if not colors[i] and not dfs(i, 1):
                return False
        return True


sol = Solution2()
tests = [
    ([[1,2,3,4],[0,2,3,4],[0,1,4],[0,1,4],[0,1,2,3],[6,7,9],[5,7,9],[5,6,8,9],[7,9],[5,6,7,8],[11,12,13],[10,12,13,14],[10,11,13,14],[10,11,12,14],[11,12,13],[16,17],[15,18],[15,19],[16],[17],[22,24],[22,23,24],[20,21],[21],[20,21],[26,27,29],[25,27,28,29],[25,26],[26,29],[25,26,28],[31,32,33,34],[30,32,34],[30,31,33,34],[30,32,34],[30,31,32,33],[37,38,39],[37,38,39],[35,36,38,39],[35,36,37,39],[35,36,37,38],[42,43,44],[42,43,44],[40,41,43,44],[40,41,42],[40,41,42],[48,49],[47,48,49],[46,48,49],[45,46,47,49],[45,46,47,48]], False),
    ([[3],[2,4],[1],[0,4],[1,3]], True),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.isBipartite(graph)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
