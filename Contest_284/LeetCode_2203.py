# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict
import math
import heapq


class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        """Can't solve this, because my dumbass didn't realize that finding
        the path with the min weight is Dijkstra. Below I will reproduce the
        popular solution of three Dijkstras (ref: https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1844130/Python-3-Dijkstras-explained.)

        However, this solution (https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/discuss/1844479/Simultaneous-Dijkstra-beats-100-(only-1-dijkstra))
        uses only one Dijkstra.

        O(ElogV + N) as according to Wikipedia. 3249 ms, 71% ranking.
        """
        # first produce two graphs, one in the original order, and the other
        # reversed order
        G1, G2 = defaultdict(list), defaultdict(list)
        for f, t, w in edges:
            G1[f].append((t, w))
            G2[t].append((f, w))  # reverse

        def Dijkstra(graph, start) -> List[int]:
            queue, weights = [(0, start)], {}
            while queue:
                w, node = heapq.heappop(queue)
                if node not in weights:  # weights always record the min weight
                    weights[node] = w
                    for child, weight in graph.get(node, []):
                        heapq.heappush(queue, (w + weight, child))
            return [weights.get(i, math.inf) for i in range(n)]

        s1toall = Dijkstra(G1, src1)
        s2toall = Dijkstra(G1, src2)
        dstoall = Dijkstra(G2, dest)

        res = min(s1toall[i] + s2toall[i] + dstoall[i] for i in range(n))
        return res if res < math.inf else -1


sol = Solution()
tests = [
    (6, [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], 0, 1, 5, 9),
    (3, [[0,1,1],[2,1,1]], 0, 1, 2, -1),
]

for i, (n, edges, src1, src2, dest, ans) in enumerate(tests):
    res = sol.minimumWeight(n, edges, src1, src2, dest)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
