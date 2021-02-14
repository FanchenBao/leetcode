# from pudb import set_trace; set_trace()
from typing import List
from collections import deque


class Solution1:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """DFS solution. We assign each node either 1 or -1. As we traverse
        through the graph, we check whether a parent node and its child have the
        same signs. If they do, then the graph cannot be a bipartite. We do this
        until we visit all the nodes.

        The on trick is to start DFS at all nodes, because the graph can be
        disconnected.

        O(N), 180 ms, 47% ranking.
        """
        n = len(graph)
        groups = [0] * n
        visited = set()

        def dfs(parent: int) -> bool:
            visited.add(parent)
            for child in graph[parent]:
                if not groups[child]:
                    groups[child] = groups[parent] * (-1)
                elif groups[child] == groups[parent]:
                    return False
            for child in graph[parent]:
                if child not in visited and not dfs(child):
                    return False
            return True

        for i in range(n):
            if not groups[i]:
                groups[i] = 1
            if not dfs(i):
                return False
        return True


class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """BFS version

        O(N), 176 ms, 63% ranking.
        """
        n = len(graph)
        groups = [0] * n
        visited = set()

        def bfs(parent: int) -> bool:
            queue = deque([parent])
            while queue:
                node = queue.popleft()
                for child in graph[node]:
                    if not groups[child]:
                        groups[child] = groups[node] * (-1)
                    elif groups[child] == groups[node]:
                        return False
                    if child not in visited:
                        queue.append(child)
                        visited.add(child)
            return True

        for i in range(n):
            if not groups[i]:
                groups[i] = 1
            if i not in visited:
                visited.add(i)
                if not bfs(i):
                    return False
        return True


class Solution3:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """This is from https://leetcode.com/problems/is-graph-bipartite/discuss/115487/Java-Clean-DFS-solution-with-Explanation
        I feel it is a more concise DFS than my version, and it's also clearer
        what the algorithm is trying to do. We assign colors to all the nodes.
        What we want to see is that all adjacent nodes have different colors.
        If not, then the graph cannot be bipartitie.

        We start from color any node that has not been colored before. Then we
        go to all of its children, and want to color them with a different color.
        As we visit the child, if the child does not have a color yet, we assign the
        desired color to it. Otherwise, we compare the child's current color
        with the desired color. If the two match, we end the search and return
        True. Otherwise, False, which means a bipartite cannot be found.

        We also need the trick to treat each node as root, just to handle the
        case of disconnected graph.

        O(N), 172 ms, 78% ranking.
        """
        n = len(graph)
        colors = [0] * n

        def dfs(node: int, color: int):
            if colors[node]:
                return colors[node] == color
            colors[node] = color
            for child in graph[node]:
                if not dfs(child, -color):
                    return False
            return True

        for node in range(n):
            if not colors[node] and not dfs(node, 1):
                return False
        return True


sol = Solution3()
tests = [
    ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
    ([[1, 3], [0, 2], [1, 3], [0, 2]], True),
    ([[1, 3], [0], [], [0]], True),
    ([[], [2, 4, 6], [1, 4, 8, 9], [7, 8], [1, 2, 8, 9], [6, 9], [1, 5, 7, 8, 9], [3, 6, 9], [2, 3, 4, 6, 9], [2, 4, 5, 6, 7, 8]], False),
    ([[1], [0, 3], [3], [1, 2]], True),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.isBipartite(graph)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
