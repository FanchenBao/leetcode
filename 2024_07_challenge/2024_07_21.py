# from pudb import set_trace; set_trace()
from typing import List, Set, Tuple
import math


class Solution:
    def _create_graph(
        self, k: int, conditions: List[List[int]]
    ) -> Tuple[List[Set[int]], List[int]]:
        graph: List[Set[int]] = [set() for _ in range(k + 1)]
        indegrees = [0] * (k + 1)
        for u, v in conditions:
            if v not in graph[u]:
                graph[u].add(v)
                indegrees[v] += 1
        return graph, indegrees

    def _top_sort(
        self, k: int, graph: List[Set[int]], indegrees: List[int]
    ) -> List[int]:
        queue = [i for i in range(1, k + 1) if indegrees[i] == 0]
        nodes_pos = [0] * (k + 1)
        p = 0
        while queue:
            tmp = []
            for node in queue:
                nodes_pos[node] = p
                p += 1
                for child in graph[node]:
                    indegrees[child] -= 1
                    if indegrees[child] == 0:
                        tmp.append(child)
            queue = tmp
        return nodes_pos if p == k else []

    def buildMatrix(
        self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]
    ) -> List[List[int]]:
        """
        LeetCode 2392 (Fail)

        I know this is a graph and also know we need to find the order based
        on depth. But I cannot figure out how to merge the two orders together
        (row order and col order) into the matrix. In particular, I have
        difficulty handling the situation where multiple nodes have the same
        depth in the graph.

        I didn't read the solution completely, but it seems that it simply
        assign some ordering index for the row and col orders. The absolute
        ordering does not matter. What matters is the relative order, which
        can be obtained via topological sort.

        In other words, if our absolute order is [[1, 3], [2]] which means nodes
        1 and 3 both must occur before 2, yet there is no requirement on the
        ordering of 1 and 3. Then we can assign their order as
        1: 0
        3: 1
        2: 2

        We maintain the relative order between 1 and 2, and 3 and 2, yet we
        can be flexible in the order between 1 and 3.

        We do this for both the row and col absolute orders and we will have
        the row and col indices for each value.

        582 ms, faster than 61.07%
        """
        row_graph, row_ins = self._create_graph(k, rowConditions)
        col_graph, col_ins = self._create_graph(k, colConditions)
        row_nodes_pos = self._top_sort(k, row_graph, row_ins)
        if not row_nodes_pos:
            return []
        col_nodes_pos = self._top_sort(k, col_graph, col_ins)
        if not col_nodes_pos:
            return []
        res = [[0] * k for _ in range(k)]
        for v in range(1, k + 1):
            res[row_nodes_pos[v]][col_nodes_pos[v]] = v
        return res


sol = Solution()
tests = [
    # (3, [[1, 2], [3, 2]], [[1, 2], [3, 2]], [[3, 1, 0], [0, 0, 2], [0, 0, 0]]),
    # (3, [[1, 2], [3, 2]], [[2, 1], [3, 2]], [[3, 0, 0], [0, 0, 1], [0, 2, 0]]),
    (
        8,
        [
            [1, 2],
            [7, 3],
            [4, 3],
            [5, 8],
            [7, 8],
            [8, 2],
            [5, 8],
            [3, 2],
            [1, 3],
            [7, 6],
            [4, 3],
            [7, 4],
            [4, 8],
            [7, 3],
            [7, 5],
        ],
        [[5, 7], [2, 7], [4, 3], [6, 7], [4, 3], [2, 3], [6, 2]],
        [
            [0, 0, 0, 0, 0, 0, 7, 0],
            [0, 6, 0, 0, 0, 0, 0, 0],
            [0, 0, 5, 0, 0, 0, 0, 0],
            [0, 0, 0, 4, 0, 0, 0, 0],
            [8, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 3, 0, 0],
            [0, 0, 0, 0, 2, 0, 0, 0],
        ],
    ),
]

for i, (k, rowConditions, colConditions, ans) in enumerate(tests):
    res = sol.buildMatrix(k, rowConditions, colConditions)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
