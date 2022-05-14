# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """LeetCode 743

        This is a pretty bad solution. We DFS everything and visit a node if
        visiting it leads to reduction in the cost. However, this also requires
        revisiting the same node multiple times. Hence, it is not efficient
        at all.

        6583 ms, faster than 5.00%
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        costs = [math.inf] * (n + 1)
        
        def dfs(node: int, cost: int, visited) -> None:
            for nei, w in adj[node]:
                if nei not in visited and cost + w < costs[nei]:
                    visited.add(nei)
                    costs[nei] = min(costs[nei], cost + w)
                    dfs(nei, cost + w, visited)
                    visited.remove(nei)

        costs[0] = costs[k] = 0
        dfs(k, 0, set())
        max_cost = max(costs)
        return max_cost if max_cost < math.inf else -1


class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Dijkstra

        Just keep Dijkstra running until we exhaust all possible nodes to visit
        This will guarantee that each visited node has min cost to reach.

        O(V + ElogV), 538 ms, faster than 64.40% 
        """
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))
        costs = [math.inf] * (n + 1)
        costs[k] = 0
        heap = [(0, k)]

        while heap:
            c, node = heapq.heappop(heap)
            for nei, w in adj[node]:
                if -c + w < costs[nei]:
                    costs[nei] = -c + w
                    heapq.heappush(heap, (c - w, nei))

        max_cost = max(costs[1:])
        return max_cost if max_cost < math.inf else -1


class Solution3:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """Bellman-Ford

        First time writing Bellman-Ford. It is a beefier version of Dijkstra.
        While Dijkstra is greedy and specialized in finding the shortest path
        from one source to one dest, Bellman-Ford takes into consideration one
        source and all dest in a non-greedy manner.

        O(VE), 1135 ms, faster than 7.35%
        """
        costs = [math.inf] * (n + 1)  # cost to reach each node
        costs[k] = 0
        # each round can update at least one edge. Thus at most we need to
        # run n - 1 times to update all the edges.
        for _ in range(n - 1):
            for u, v, w in times:
                if costs[v] > costs[u] + w:
                    costs[v] = costs[u] + w
        max_cost = max(costs[1:])
        return max_cost if max_cost < math.inf else -1


sol = Solution3()
tests = [
    ([[2,1,1],[2,3,1],[3,4,1]], 4, 2, 2),
    ([[1,2,1]], 2, 1, 1),
    ([[1,2,1]], 2, 2, -1),
    ([[1,2,1],[2,3,2],[1,3,4]], 3, 1, 3),
]

for i, (times, n, k, ans) in enumerate(tests):
    res = sol.networkDelayTime(times, n, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
