# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import defaultdict


class Solution1:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """Record a set of edges to avoid duplicates. There got to be a better
        way.

        O(V + E), 697 ms, faster than 63.95%
        """
        visited = set()
        edge_set = []
        node_count = []
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node: int) -> None:
            node_count[-1] += 1
            visited.add(node)
            for child in graph[node]:
                edge_set[-1].add((min(node, child), max(node, child)))
                if child not in visited:
                    dfs(child)

        for i in range(n):
            if i not in visited:
                node_count.append(0)
                edge_set.append(set())
                dfs(i)
        return sum(nc * (nc - 1) // 2 == len(es) for nc, es in zip(node_count, edge_set))


class Solution2:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        """The number of edges from a node can be easily obtained by the graph

        O(V + E), 624 ms, faster than 100.00%
        """
        visited = set()
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dfs(node: int) -> Tuple[int, int]:
            # return number of nodes in the graph and twice the number of edges
            if node in visited:
                return 0, 0
            visited.add(node)
            num_node, twice_num_edges = 1, len(graph[node])
            for child in graph[node]:
                child_nodes, twice_child_edges = dfs(child)
                num_node += child_nodes
                twice_num_edges += twice_child_edges
            return num_node, twice_num_edges

        res = 0
        for i in range(n):
            if i not in visited:
                num_nodes, twice_num_edges = dfs(i)
                res += int(num_nodes * (num_nodes - 1) == twice_num_edges)
        return res
        

sol = Solution2()
tests = [
    (6, [[0,1],[0,2],[1,2],[3,4]], 3),
    (6, [[0,1],[0,2],[1,2],[3,4],[3,5]], 1),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.countCompleteComponents(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
