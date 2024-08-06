# from pudb import set_trace; set_trace()
from typing import Dict, List, Tuple
import math
from collections import defaultdict
import heapq

GraphT = Dict[int, List[Tuple[int, int]]]


class Solution1:
    def dijkstra(self, root: int, graph: GraphT, thresh: int, n: int) -> int:
        """
        Return the number of cities reachable from root with weights not bigger
        than threshold

        271 ms, faster than 66.57%

        Dijkstra is O(MlogN), where M is the number of edges and N is the number
        of nodes. Since M = N(N - 1) / 2, Dijkstra is O(N^2logN)

        On the outside, we loop through all the nodes. Thus, the total runtime
        is O(N^3logN)
        """
        weights = [math.inf] * n
        weights[root] = 0
        queue = [(root, 0)]
        reachable = set()
        while queue:
            node, accW = heapq.heappop(queue)
            if accW != weights[node]:
                continue
            for child, w in graph[node]:
                newW = accW + w
                if newW < weights[child] and newW <= thresh:
                    weights[child] = newW
                    heapq.heappush(queue, (child, newW))
                    reachable.add(child)
        return len(reachable)

    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        minCnt = math.inf
        res = -1
        for i in range(n):
            cnt = self.dijkstra(i, graph, distanceThreshold, n)
            if cnt <= minCnt:
                minCnt = cnt
                res = i
        return res


class Solution2:
    def findTheCity(
        self, n: int, edges: List[List[int]], distanceThreshold: int
    ) -> int:
        """
        We will use Floyd-Warshall method to find the min distance between any
        pairs of nodes.

        O(N^3), 482 ms, faster than 17.94%
        """
        dists = [[math.inf] * n for _ in range(n)]
        for u, v, w in edges:
            dists[u][v] = min(dists[u][v], w)
            dists[v][u] = min(dists[v][u], w)
        # Floyd-Warshall
        for k in range(n):
            for u in range(n):
                for v in range(n):
                    if u == v:
                        dists[u][v] = 0
                    else:
                        dists[u][v] = min(dists[u][v], dists[u][k] + dists[k][v])

        minCnt = math.inf
        res = -1
        for i in range(n):
            cnt = 0
            for j in range(n):
                if i != j and dists[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt <= minCnt:
                minCnt = cnt
                res = i
        return res


sol = Solution2()
tests = [
    ("hello", "holle"),
    ("leetcode", "leotcede"),
]

for i, (s, ans) in enumerate(tests):
    res = sol.reverseVowels(s)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
