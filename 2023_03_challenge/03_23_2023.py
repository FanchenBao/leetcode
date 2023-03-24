# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """LeetCode 1319

        Given n nodes, the min number of edges needed to make it connected is
        n - 1. Thus, we can find all the cliques in the graph. For each clique,
        we find the number of nodes in it. We will then know the minimal needed
        edges to maintain the clique connected. Any additional edges can be
        used for other purposes.

        After going through the entire graph, we will accumulate the number of
        minimal needed edges. We also know the total number of edges. Thus their
        difference is the total number of available edges.

        We also know the minimal number of edges to make the entire graph
        connected is n - 1. Thus, the additional edges needed is n - 1 - min_needed_edges

        Finally, the question is whether additional edges is smaller or equal to
        available edges. If it is, we return additional edges. Otherwise, we
        return -1.

        O(N + E), 518 ms, faster than 57.14%
        """
        not_visited = set(range(n))
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i: int) -> None:
            if i in not_visited:
                not_visited.remove(i)
                for j in graph[i]:
                    dfs(j)

        min_needed_edges = 0
        for i in range(n):
            if i in not_visited:
                before = len(not_visited)
                dfs(i)
                min_needed_edges += before - len(not_visited) - 1
        available = len(connections) - min_needed_edges
        additional = n - 1 - min_needed_edges
        return additional if additional <= available else -1


class Solution2:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        """Even simpler, all I need to find is the number of cliques (including
        single node that is not connected to anyone else). The answer should be
        the number of cliques minus one.

        Another important observation is that if the number of connections is
        smaller than n - 1, there is no way to make the graph connected. We
        check that first. As long as the number of total connections is larger
        or equal to n - 1, we can always rearrange the connections to make the
        graph connected.

        O(N + E), 526 ms, faster than 50.38%
        """
        if len(connections) < n - 1:
            return -1

        not_visited = set(range(n))
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(i: int) -> None:
            if i in not_visited:
                not_visited.remove(i)
                for j in graph[i]:
                    dfs(j)

        num_cliques = 0
        for i in range(n):
            if i in not_visited:
                dfs(i)
                num_cliques += 1
        return num_cliques - 1


sol = Solution2()
tests = [
    (4, [[0,1],[0,2],[1,2]], 1),
    (6, [[0,1],[0,2],[0,3],[1,2],[1,3]], 2),
    (6, [[0,1],[0,2],[0,3],[1,2]], -1)
]

for i, (n, connections, ans) in enumerate(tests):
    res = sol.makeConnected(n, connections)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
