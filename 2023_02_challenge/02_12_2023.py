# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter, defaultdict


class Solution1:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """LeetCode 2477

        Topological sort. The core idea is to hold all the people at one
        node until this node has only one outgoing edge. Then we decide the
        min number of cars needed to transport all the people. This reqiures a
        BFS that only pushes a new node to the queue when that node has one
        edge. Thus, the graph we create use set to hold all its neighbors. We
        will update it as we visit a new node. We also use people_map to keep
        track of the number of people that have arrived at a node.

        O(N + E), 2298 ms, faster than 34.58%

        UPDATE: use math.ceil. Slightly faster 2180 ms, faster than 40.81%
        """
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        people_map = defaultdict(lambda: 1)
        queue = [node for node in graph if node and len(graph[node]) == 1]
        res = 0
        while queue:
            tmp = []
            for node in queue:
                nex = list(graph[node])[0]
                res += math.ceil(people_map[node] / seats)
                graph[nex].remove(node)
                people_map[nex] += people_map[node]
                if nex and len(graph[nex]) == 1:
                    tmp.append(nex)
            queue = tmp
        return res


class Solution2:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """DFS. What solution 1 does is to compute, for each node, the total
        number of children it has. This can be easily accomplished via DFS

        O(N), 2047 ms, faster than 62.31% 
        """
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        self.res = 0
        visited = set()

        def dfs(node: int) -> int:
            total = 1
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    total += dfs(child)
            if node:
                self.res += math.ceil(total / seats)
            return total

        dfs(0)
        return self.res


sol = Solution2()
tests = [
    ([[0,1],[0,2],[0,3]], 5, 3),
    ([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2, 7),
    ([], 1, 0),
    ([[0,1],[0,2],[1,3],[1,4]], 5, 4),
    ([[1,0],[1,2]], 1, 3),
    ([[1,0],[2,0],[1,3],[4,3],[4,5],[6,2],[4,7],[4,8],[9,1],[10,8],[11,10],[12,3],[13,10],[14,3],[15,7],[16,3],[16,17],[18,1],[19,4],[20,17]], 14, 22),
]

for i, (roads, seats, ans) in enumerate(tests):
    res = sol.minimumFuelCost(roads, seats)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
