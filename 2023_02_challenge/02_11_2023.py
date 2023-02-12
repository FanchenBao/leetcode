# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        """LeetCode 1127

        Use BFS. During traversal, the state of each node is the node itself and
        the color of the edge leading to this node. This allows to decide which
        node to add to the queue in the next step. The next combination of node
        and color must not appear before. This means we do allow revisiting a
        node that has been visited before, as long as the edge color leading to
        the node is different.

        Other than that, it's a standard BFS. I do run BFS twice, because the
        initial node has no color edge leading to it. So from the initial node,
        we can go out with red or blue.

        O(N + E), where N is the number of nodes and E the number of edges.

        89 ms, faster than 73.46%
        """
        graph = [[[] for _ in range(n)], [[] for _ in range(n)]]
        for a, b in redEdges:
            graph[0][a].append(b)
        for a, b in blueEdges:
            graph[1][a].append(b)
        res = [math.inf] * n

        def bfs(first_color: int) -> None:
            """first_color == 0 => red, first_color == 1 => blue"""
            queue = [(0, first_color)]
            visited = set()
            visited.add((0, first_color))
            steps = 0
            while queue:
                tmp = []
                for node, pre_color in queue:
                    res[node] = min(res[node], steps)
                    nex_color = pre_color ^ 1
                    for nex in graph[nex_color][node]:
                        if (nex, nex_color) not in visited:
                            visited.add((nex, nex_color))
                            tmp.append((nex, nex_color))
                queue = tmp
                steps += 1

        bfs(0)
        bfs(1)
        return [r if r < math.inf else -1 for r in res]


sol = Solution()
tests = [
    (3, [[0,1],[1,2]], [], [0, 1, -1]),
    (3, [[0,1]], [[2,1]], [0, 1, -1]),
    (3, [[0,1],[1,2]], [[1,1]], [0, 1, 3]),
]

for i, (n, redEdges, blueEdges, ans) in enumerate(tests):
    res = sol.shortestAlternatingPaths(n, redEdges, blueEdges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
