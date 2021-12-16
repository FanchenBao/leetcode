# from pudb import set_trace; set_trace()
from typing import List
from collections import defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """LeetCode 310

        I remembered solving this problem using a quite convoluted method. But
        I am not able to recreat that method again today. Thus, I have to resort
        to the smarter and easier method of pruning. The rule of pruning is that
        we always prune the nodes that have only one edge. After each pruning,
        we add to the queue new nodes that have only one edge. This method can
        obtain the root of MHT if the root is singluar. For the case where there
        are two MHT roots, I have to set up a separate check for this case.

        O(N), 244 ms, 51% ranking.

        UPDATE: use `remain` to indicate when topological sort ends
        """
        if not edges:
            return [0]
        adj = [set() for _ in range(n)]
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        queue = [i for i in range(n) if len(adj[i]) == 1]
        remain = n
        while remain > 2:
            temp = []
            remain -= len(queue)
            for node in queue:
                nei = list(adj[node])[0]
                adj[nei].remove(node)
                if len(adj[nei]) == 1:
                    temp.append(nei)
            queue = temp
        return queue


sol = Solution()
tests = [
    (4, [[1,0],[1,2],[1,3]], [1]),
    (6, [[3,0],[3,1],[3,2],[3,4],[5,4]], [3, 4]),
    (1, [], [0]),
    (2, [[0, 1]], [0, 1]),
    (3, [[0,1],[0,2]], [0]),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findMinHeightTrees(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
