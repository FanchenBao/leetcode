# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def longestCycle(self, edges: List[int]) -> int:
        """LeetCode 2360

        First check we do is to identify the potential nodes in a cycle. To be
        in a cycle, a node must have at least one in-edge and one out-edge. We
        can go through all the edges and keep only those with at leaset one edge
        in and out as the potentials.

        Then we can start from any of the potentials and DFS it. We only continue
        if the next node is also in the potential list. And each time we visit
        a node, we remove it from the potential set. Thus If DFS ends, we either
        have come back to a cycle or we have hit some node that was discarded
        before. We can keep an index list for all the nodes visited to compute
        the size of the cycle.

        O(N), 1509 ms, faster than 40.50%
        """
        N = len(edges)
        edge_counts = [[0, 0] for _ in range(N)]
        for i, e in enumerate(edges):
            edge_counts[i][1] += 1
            edge_counts[e][0] += 1

        pots = set()
        for i, (in_, out_) in enumerate(edge_counts):
            if in_ * out_ > 0:
                pots.add(i)

        res = -1
        for i in list(pots):
            node = i
            indices = {}
            j = 0
            while node in pots:
                indices[node] = j
                pots.remove(node)
                node = edges[node]
                j += 1
            if node in indices:
                res = max(res, j - indices[node])
        return res


class Solution2:
    def longestCycle(self, edges: List[int]) -> int:
        """Straightforward DFS

        No need to bother with a pre-screening.

        O(N), 1280 ms, faster than 77.57%
        """
        N = len(edges)
        not_visited = set(range(N))
        res = -1
        for i in range(N):
            node = i
            indices = {}
            j = 0
            while node in not_visited:
                indices[node] = j
                not_visited.remove(node)
                node = edges[node]
                j += 1
            if node in indices:
                res = max(res, j - indices[node])
        return res


class Solution3:
    def longestCycle(self, edges: List[int]) -> int:
        """Using Kahn's algorithm (topological sort) to eliminate the impossible
        nodes. This method is similar to Solution1, but it removes more nodes
        that are not possible. Basically, solution1 only removes the impossible
        nodes at the top level, but the Kahn's algorithm keeps going to remove
        the nodes with no indegree on the second, third, etc. levels. Thus, the
        remaining potential nodes are much fewer compared to Solution1. This can
        speed up the remainder of the algo.
        """
        N = len(edges)
        edge_counts = [[0, 0] for _ in range(N)]
        for i, e in enumerate(edges):
            if e >= 0:  # in case e == -1
                edge_counts[i][1] += 1
                edge_counts[e][0] += 1

        queue = [i for i, (ind, _) in enumerate(edge_counts) if ind == 0]
        pots = set(range(N))
        while queue:
            tmp = []
            for node in queue:
                if node >= 0:  # in case node == -1
                    pots.remove(node)
                    nex = edges[node]
                    edge_counts[nex][0] -= 1
                    if edge_counts[nex][0] == 0:
                        tmp.append(nex)
            queue = tmp

        res = -1
        for i in list(pots):
            node = i
            indices = {}
            j = 0
            while node in pots:
                indices[node] = j
                pots.remove(node)
                node = edges[node]
                j += 1
            if node in indices:
                res = max(res, j - indices[node])
        return res


sol = Solution3()
tests = [
    ([3,3,4,2,3], 3),
    ([2,-1,3,1], -1),
    ([3,4,0,2,-1,2], 3),
    ([-1,2,1], 2),
    ([-1,2,-1,5,3,3], 2),
]

for i, (edges, ans) in enumerate(tests):
    res = sol.longestCycle(edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
