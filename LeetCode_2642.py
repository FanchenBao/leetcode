# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import defaultdict
import heapq


class Graph:
    """Perform Dijkstra for each node when the node is queried. When we perform
    Dijkstra, we do it for all reachable nodes. Thus, if in the future a
    different query is needed from the same starting point, we can directly
    return the min dist.

    The addition of an edge requires all previous Dijkstras from all nodes except
    from the end node of the newly added edge to be anulled and performed again
    when queried in the future.

    917 ms, faster than 63.35% 
    """

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = self._build_graph(edges)
        self.N = n
        self.should_redo_dijkstra = [True] * n
        self.dijkstra = [[math.inf] * n for _ in range(n)]

    def _build_graph(self, edges: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
        graph = defaultdict(list)
        for a, b, cost in edges:
            graph[a].append((b, cost))
        return graph

    def _do_dijkstra(self, start: int) -> None:
        heap = [(0, start)]
        self.dijkstra[start] = [math.inf] * self.N
        self.dijkstra[start][start] = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if dist != self.dijkstra[start][node]:
                continue
            for child, cost in self.graph[node]:
                new_dist = dist + cost
                if new_dist < self.dijkstra[start][child]:
                    self.dijkstra[start][child] = new_dist
                    heapq.heappush(heap, (new_dist, child))
        
    def addEdge(self, edge: List[int]) -> None:
        a, b, cost = edge
        self.graph[a].append((b, cost))
        # redo Dijkstra for all starting nodes except b, because the added edge
        # from a to b does not affect the Dijkstra starting from b
        original_b = self.should_redo_dijkstra[b]
        self.should_redo_dijkstra = [True] * self.N
        self.should_redo_dijkstra[b] = original_b

    def shortestPath(self, node1: int, node2: int) -> int:
        if self.should_redo_dijkstra[node1]:
            self._do_dijkstra(node1)
            self.should_redo_dijkstra[node1] = False
        return self.dijkstra[node1][node2] if self.dijkstra[node1][node2] < math.inf else -1



sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
