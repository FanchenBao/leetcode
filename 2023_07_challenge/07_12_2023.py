# from pudb import set_trace; set_trace()
from typing import List, Set
import math
# import heapq
from collections import deque


class Solution1:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """LeetCode 802

        I use topological sort, going from the terminal nodes backwards. It is
        guaranteed that each node in the safe path must also be terminal nodes
        when their adjacent terminal nodes are removed. Thus, we keep track of
        the number of out edges for each node and BFS from terminal nodes back.
        We add to the answer all the nodes during BFS that end up with zero
        out edges.

        O(M + N), M is the number of edges and N is the number of nodes.
        715 ms, faster than 26.47%
        """
        N = len(graph)
        parents = [[] for _ in range(N)]
        num_out_edges = [0] * N
        queue = deque()
        for i, children in enumerate(graph):
            for child in children:
                parents[child].append(i)
            num_out_edges[i] = len(children)
            if num_out_edges[i] == 0:
                queue.append(i)
        res = []
        while queue:
            node = queue.popleft()
            res.append(node)
            for par in parents[node]:
                num_out_edges[par] -= 1
                if num_out_edges[par] == 0:
                    queue.append(par)
        return sorted(res)


class Solution2:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """DFS. Inspired by the official solution. The idea is to traverse the
        graph. A node is safe if all the paths lead to safe nodes. As long as
        one path has cycle, the node is unsafe.

        Each node only needs to be visited once.

        O(M + N), M is the number of edges and N is the number of nodes.
        715 ms, faster than 26.47%
        """
        N = len(graph)
        is_safe = [-1] * N

        def dfs(node: int, path: Set[int]) -> bool:
            if node in path or is_safe[node] == 0:
                is_safe[node] = 0
                return False
            if is_safe[node] == 1 or not graph[node]:
                is_safe[node] = 1
                return True
            path.add(node)
            if all(dfs(child, path) for child in graph[node]):
                is_safe[node] = 1
                path.remove(node)
                return True
            is_safe[node] = 0
            path.remove(node)
            return False

        for i in range(N):
            if is_safe[i] < 0:
                dfs(i, set())
        return [i for i in range(N) if is_safe[i] == 1]


sol = Solution2()
tests = [
    ([[1,2],[2,3],[5],[0],[5],[],[]], [2,4,5,6]),
    ([[1,2,3,4],[1,2],[3,4],[0,4],[]], [4]),
]

for i, (graph, ans) in enumerate(tests):
    res = sol.eventualSafeNodes(graph)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
