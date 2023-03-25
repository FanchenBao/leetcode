# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """LeetCode 1466

        Treat all the connections as bi-directional and perform DFS from node 0.
        Any edge encountered in the traversal must be pointing the other way to
        satisfy the requirement. Thus, if the edge exists in connections, it
        must be reversed. If the edge does not exist in connections, that means
        it has been reversed already. We simply count the number of edges in
        connections during the traversal.

        O(N + E), 1314 ms, faster than 45.71%
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)
        con_set = set(tuple(c) for c in connections)
        visited = set([0])
        self.res = 0

        def dfs(i: int) -> None:
            visited.add(i)
            for j in graph[i]:
                if j not in visited:
                    if (i, j) in con_set:
                        self.res += 1
                    dfs(j)

        dfs(0)
        return self.res


class Solution2:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """This is the official solution, which uses a sign to denote whether
        the edge during the DFS is artificial or original. If the edge is
        original, it must be reversed. Thus, we can set the sign to be 1 for
        original and 0 for artificial.

        Also, since we are travering a tree, we don't have to use the visited
        set. We can just make sure that the child is not equal to the parent.

        O(N + E) = O(N) becuase E = N - 1, 1321 ms, faster than 42.86%
        """
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append((b, 1))  # original
            graph[b].append((a, 0))  # artificial

        self.res = 0

        def dfs(i: int, par: int) -> None:
            for j, sign in graph[i]:
                if j != par:
                    self.res += sign
                    dfs(j, i)

        dfs(0, -1)
        return self.res


sol = Solution2()
tests = [
    (6, [[0,1],[1,3],[2,3],[4,0],[4,5]], 3),
    (5, [[1,0],[1,2],[3,2],[3,4]], 2),
    (3, [[1,0],[2,0]], 0),
]

for i, (n, connections, ans) in enumerate(tests):
    res = sol.minReorder(n, connections)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
