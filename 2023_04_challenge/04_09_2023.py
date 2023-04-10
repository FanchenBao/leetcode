# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import Counter, defaultdict


class Solution1:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """LeetCode 1857

        Didn't feel like a hard one. We need to dfs all the paths, but we can
        save the state for each node. The state represents the max number of a
        certain color in the path starting from the node. Thus, when a new node
        is going to lead to a visited node, we don't have to visit again, we
        just use the previous result to update the new node's state.

        During DFS, we have to keep a path to determine whether we have
        encountered a cycle. Once a cycle is detected, we can return immediately.

        O(26N + 26M), 2551 ms, faster than 55.36%
        """
        N = len(colors)
        visited = [Counter() for _ in range(N)]
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)


        def dfs(idx: int, path: Set) -> bool:
            if idx in path:
                return False
            if visited[idx]:
                return True
            path.add(idx)
            visited[idx][colors[idx]] += 1
            # current node is the end of a path
            if not graph[idx]:
                path.remove(idx)
                return True
            # there are more nodes on the path
            for ni in graph[idx]:
                if not dfs(ni, path):
                    return False
                for k, v in visited[ni].items():
                    visited[idx][k] = max(visited[idx][k], v + int(colors[idx] == k))
            path.remove(idx)
            return True


        res = 0
        for i in range(N):
            if not dfs(i, set()):
                return -1
            res = max(res, max(visited[i].values() or [0]))
        return res


class Solution2:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        """Use Kahn's algo for topological sort (from the official solution).

        We start with indegree = 0, and then go to indegree = 1, 2, etc. At each
        node, we collect the max number of nodes in each color in all the paths
        from parents (so this is essentially a reversed version of solution1).

        O(26(N + M)), 2102 ms, faster than 90.48%
        """
        N = len(colors)
        graph = defaultdict(list)
        indegrees = [0] * N
        for a, b in edges:
            graph[a].append(b)
            indegrees[b] += 1
        queue = [i for i in range(N) if indegrees[i] == 0]
        scores = [Counter() for _ in range(N)]
        while queue:
            tmp = []
            for idx in queue:
                scores[idx][colors[idx]] += 1
                for ni in graph[idx]:
                    indegrees[ni] -= 1  # update indegrees
                    for k, v in scores[idx].items():  # update next node's state
                        scores[ni][k] = max(scores[ni][k], v)
                    if indegrees[ni] == 0:
                        tmp.append(ni)
            queue = tmp
        res = 0
        for i in range(N):
            if indegrees[i]:
                return -1
            res = max(res, max(scores[i].values() or [0]))
        return res


sol = Solution2()
tests = [
    ("abaca", [[0,1],[0,2],[2,3],[3,4]], 3),
    ("a", [[0,0]], -1),
    ("abacbe", [[1,4],[0,2],[2,3],[5,5]], -1),
    ("a", [], 1),
    ("eeyyeeyeye", [[0,1],[1,2],[2,3],[3,4],[4,5],[4,6],[5,7],[6,8],[8,9]], 5),
]

for i, (colors, edges, ans) in enumerate(tests):
    res = sol.largestPathValue(colors, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
