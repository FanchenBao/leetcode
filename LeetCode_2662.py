# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
import heapq


class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        """Dijkstra.

        We pick out the special roads that result in cost saving and put the
        start and end of those roads into a list of potential node to travel
        through.

        Then we Dijkstra the list of nodes from start to target. At each node,
        we try all the others until we hit the target for the first time.

        Since there are at most 400 nodes, this O(N^2logN) solution will work.

        657 ms, faster than 32.63%
        """
        nodes = [tuple(start), tuple(target)]
        special_edges = defaultdict(lambda: math.inf)
        for x1, y1, x2, y2, cost in specialRoads:
            if abs(x1 - x2) + abs(y1 - y2) > cost:
                nodes.append((x1, y1))
                nodes.append((x2, y2))
                special_edges[(x1, y1, x2, y2)] = min(special_edges[(x1, y1, x2, y2)], cost)
        total_cost = defaultdict(lambda: math.inf)
        total_cost[tuple(start)] = 0
        queue = [(0, start[0], start[1])]
        while queue:
            while queue and queue[0][0] != total_cost[(queue[0][1], queue[0][2])]:
                heapq.heappop(queue)
            cur_cost, i, j = heapq.heappop(queue)
            if i == target[0] and j == target[1]:
                return cur_cost
            for ni, nj in nodes:
                n_cost = cur_cost + min(abs(i - ni) + abs(j - nj), special_edges[(i, j, ni, nj)])
                if n_cost < total_cost[(ni, nj)]:
                    total_cost[(ni, nj)] = n_cost
                    heapq.heappush(queue, (n_cost, ni, nj))

        

sol = Solution()
tests = [
    ([1,1], [4,5], [[1,2,3,3,2],[3,4,4,5,1]], 5),
    ([3,2], [5,7], [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]], 7),
]

for i, (start, target, specialRoads, ans) in enumerate(tests):
    res = sol.minimumCost(start, target, specialRoads)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
