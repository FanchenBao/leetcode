# from pudb import set_trace; set_trace()
from typing import List, Dict, Tuple
import math
from collections import defaultdict
import heapq



class Solution1:
    def dijkstra(self,
        graph: Dict[int, List[Tuple[int, int]]],
        source: int,
        n: int,
    ) -> Tuple[List[int], List[int]]:
        """No priority queue implementation.

        :param graph: graph's keys are the nodes and value is a list of tuples
            with this format (node, edge_length)
        :param source: The starting node
        :param n: Total number of nodes
        """
        nodes_set = set(graph)
        dist = [math.inf] * n
        prev = [-1] * n
        dist[source] = 0
        prev[source] = source

        while nodes_set:
            cur, cur_d = -1, math.inf
            for node, d in enumerate(dist):
                if node in nodes_set and d < cur_d:
                    cur, cur_d = node, d
            if cur == -1:
                break
            nodes_set.remove(cur)
            for neigh, length in graph[cur]:
                if neigh in nodes_set:
                    alt = cur_d + length
                    if alt < dist[neigh]:
                        dist[neigh] = alt
                        prev[neigh] = cur
        return dist, prev

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """LeetCode 882

        The online judge is very lenient, and this solution passed. The idea
        is to convert the given graph into a graph with weighted edges. The
        weight of each edge is the cnt + 1. By doing this, we can compute the
        shortest distance from source to each node using Dijkstra. This allows
        us to find which nodes of the original graph can be included in the
        result.

        Then, we consider the smaller nodes in between the original node. Given
        the original edge, we find the shortest distance going to each node that
        does NOT come pass the other node. For instance, if u has neighbors a,
        b, and c. The shortest distance from source to u goes through a. Then
        when considering the edge u <-> a, the shortest distance to u must be
        the one going through b or c, but NOT a. Note that when we are
        considering edge u <-> b or u <-> c, the shortest distance will always
        be u <-> a. Therefore, we only need to find one alternative distance
        for each node.

        Once the shortest distances are found for both nodes in an edge, we can
        compute the number of smaller nodes to include mathematically.
        
        Time complexity O(N^2), 5345 ms, 6% ranking.
        """
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        dist, prev = self.dijkstra(graph, 0, n)
        
        res = sum(d <= maxMoves for d in dist)
        alt_dist = [math.inf] * n
        for node, neighbors in graph.items():
            all_other_dists = [l + dist[nei] for nei, l in neighbors if nei != prev[node]]
            if all_other_dists:
                alt_dist[node] = min(all_other_dists)
        for u, v, cnt in edges:
            dist_u = dist[u] if prev[u] != v else alt_dist[u]
            dist_v = dist[v] if prev[v] != u else alt_dist[v]
            res += min(max(maxMoves - dist_u, 0) + max(maxMoves - dist_v, 0), cnt)
        return res


class Solution2:
    def dijkstra(self,
        graph: Dict[int, List[Tuple[int, int]]],
        source: int,
        n: int,
    ) -> Tuple[List[int], List[int]]:
        """Priority queue implementation.

        :param graph: graph's keys are the nodes and value is a list of tuples
            with this format (node, edge_length)
        :param source: The starting node
        :param n: Total number of nodes
        """
        nodes_set = set(graph)
        dist = [[math.inf, i] for i in range(n)]
        prev = [-1] * n
        dist[source][0] = 0
        prev[source] = source
        pq = dist[:]

        while nodes_set:
            heapq.heapify(pq)
            cur_d, cur = heapq.heappop(pq)
            if cur_d == math.inf or cur not in nodes_set:
                break
            nodes_set.remove(cur)
            for neigh, length in graph[cur]:
                if neigh in nodes_set:
                    alt = cur_d + length
                    if alt < dist[neigh][0]:
                        dist[neigh][0] = alt
                        prev[neigh] = cur
        return [d for d, _ in dist], prev

    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """Exactly the same solution as Solution1, but we change the
        implementation of dijkstra to use priority queue to find the min dist
        at each step.

        With priority queue implementation, we reach 3107 ms, 7% ranking.
        """
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        dist, prev = self.dijkstra(graph, 0, n)
        
        res = sum(d <= maxMoves for d in dist)
        alt_dist = [math.inf] * n
        for node, neighbors in graph.items():
            all_other_dists = [l + dist[nei] for nei, l in neighbors if nei != prev[node]]
            if all_other_dists:
                alt_dist[node] = min(all_other_dists)
        for u, v, cnt in edges:
            dist_u = dist[u] if prev[u] != v else alt_dist[u]
            dist_v = dist[v] if prev[v] != u else alt_dist[v]
            res += min(max(maxMoves - dist_u, 0) + max(maxMoves - dist_v, 0), cnt)
        return res


class Solution3:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        """From the official solution

        https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/solution/

        We are using similar method, but it is much clearer in the official
        solution that we can compute the number of smaller nodes used when an
        original node is reached during Dijkstra. We don't have to Dijkstra the
        entire graph. We just need to go through the nodes that are within
        maxMoves, and for each viable node encountered, we can directly compute
        the number of smaller nodes accessible from the current node to all of
        its neighbors.
        """
        graph = defaultdict(list)
        for u, v, cnt in edges:
            graph[u].append((v, cnt + 1))
            graph[v].append((u, cnt + 1))
        pq = [(0, 0)]
        dist = {0: 0}
        included = {}
        res = 0
        while pq:
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                # node has been added to pq from multiple other nodes, thus d
                # might not reflect the actual smallest distance. The actual
                # smallest distance is always recorded in dist[node]. Thus, by
                # checking with dist[node], we are sure that the current node
                # is only considered when its distance is also the smallest.
                continue
            res += 1
            for neigh, length in graph[node]:
                included[(node, neigh)] = min(maxMoves - d, length - 1)
                alt = d + length
                if alt < dist.get(neigh, maxMoves + 1):
                    dist[neigh] = alt
                    heapq.heappush(pq, (alt, neigh))
        for u, v, cnt in edges:
            res += min(cnt, included.get((u, v), 0) + included.get((v, u), 0))
        return res


sol = Solution3()
tests = [
    ([[0, 1, 4], [1, 2, 6], [0, 2, 8], [1, 3, 1]], 10, 4, 23),
    ([[0, 1, 10], [0, 2, 1], [1, 2, 2]], 6, 3, 13),
    ([[1, 2, 4], [1, 4, 5], [1, 3, 1], [2, 3, 4], [3, 4, 5]], 17, 5, 1),
]

for i, (edges, maxMoves, n, ans) in enumerate(tests):
    res = sol.reachableNodes(edges, maxMoves, n)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
