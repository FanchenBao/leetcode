# from pudb import set_trace; set_trace()
from typing import List, Set
import math
import heapq
from collections import defaultdict, Counter


class Solution1:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """This solution works, but it's very slow.

        The idea is that we go from outside in, considering at each round the
        out-most nodes, i.e., the nodes with degree 1. They must transport all
        of their people to the next city, so the fuel cost for them is
        deterministic.

        Once they are done, we obtain the next out-most nodes and compute the
        fuel cost from them. So on and so forth until we reach capital.

        O(NlogN), 3213 ms, faster than 62.89%
        """
        if not roads:
            return 0
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        people = [1] * (max(graph) + 1)
        heap = [(len(children), node) for node, children in graph.items() if node != 0]
        heapq.heapify(heap)
        res = 0
        while heap:
            deg, node = heapq.heappop(heap)
            if deg != len(graph[node]):
                continue
            res += math.ceil(people[node] / seats)
            child = list(graph[node])[0]  # there should be only one child
            if child:
                people[child] += people[node]
                graph[child].remove(node)
                heapq.heappush(heap, (len(graph[child]), child))
            del graph[node]
        return res


class Solution2:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """O(N), DFS. Go from the capital out. Basically at each node, we want
        to find out the total number of nodes of its subtree.

        2049 ms, faster than 91.59%
        """
        if not roads:
            return 0
        graph = defaultdict(list)
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)

        self.res = 0

        def dfs(node: int, visited: Set[int]) -> int:
            tot = 1
            visited.add(node)
            for child in graph[node]:
                if child not in visited:
                    tot += dfs(child, visited)
            self.res += math.ceil(tot / seats)
            return tot

        for node in graph[0]:
            dfs(node, set([0]))
        return self.res


class Solution3:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        """This is the real topological sort. Use queue, instead of priority
        queue.

        O(N)
        """
        if not roads:
            return 0
        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)
        people = [1] * (max(graph) + 1)
        queue = [node for node, children in graph.items() if node != 0 and len(children) == 1]
        res = 0
        while queue:
            tmp = []
            for node in queue:
                res += math.ceil(people[node] / seats)
                child = list(graph[node])[0]  # there should be only one child
                if child:
                    people[child] += people[node]
                    graph[child].remove(node)
                    if len(graph[child]) == 1:
                        tmp.append(child)
                del graph[node]
            queue = tmp
        return res


sol = Solution3()
tests = [
    ([[0,1],[0,2],[0,3]], 5, 3),
    ([[3,1],[3,2],[1,0],[0,4],[0,5],[4,6]], 2, 7),
    ([], 1, 0),
]

for i, (roads, seats, ans) in enumerate(tests):
    res = sol.minimumFuelCost(roads, seats)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
