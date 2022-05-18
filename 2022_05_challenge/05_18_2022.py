# from pudb import set_trace; set_trace()
from typing import List, Set


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """LeetCode 1192

        Very tough. Not only do I not remember Tarjan's algo, but I also
        struggle with adapting Tarjan, which is used on a directed graph, to
        this undirected graph problem.

        The breakthrough is realizing that if we do not visit backwards towards
        parent, we can treat a undirected graph as a directed graph. Thus,
        Tarjan works. Another important thing is that we have to consolidate
        all the nodes on the current path to the same low link when the root
        of this path is discovered. This is to ensure that we can correctly
        label all the nodes that do not share any critical link to the same
        value.

        O(V + E), 2318 ms, faster than 90.13%
        """
        adj = [[] for _ in range(n)]
        edgeset = set()
        for a, b in connections:
            adj[a].append(b)
            adj[b].append(a)
            edgeset.add((min(a, b), max(a, b)))

        low_links = [-1] * n
        indices = [-1] * n
        self.idx = 0

        def dfs(par: int, node: int, stk: List[int], stkset: Set[int]) -> None:
            low_links[node] = self.idx
            indices[node] = self.idx
            self.idx += 1
            stk.append(node)
            stkset.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if indices[nei] < 0:
                    dfs(node, nei, stk, stkset)
                    low_links[node] = min(low_links[node], low_links[nei])
                elif nei in stkset:
                    low_links[node] = min(low_links[node], indices[nei])
            if low_links[node] == indices[node]:
                while stk[-1] != node:
                    temp = stk.pop()
                    # consolidate the low link of all the nodes on the current path
                    # to that of the root of the current path
                    low_links[temp] = low_links[node]
                    stkset.remove(temp)
                stkset.remove(stk.pop())

        dfs(-1, 0, [], set())
        # critical links are those that connect two subgraphs of different
        # low_link
        return [[a, b] for a, b in connections if low_links[a] != low_links[b]]


sol = Solution()
tests = [
    (4, [[0,1],[1,2],[2,0],[1,3]], [[1, 3]]),
    (2, [[0,1]], [[0, 1]]),
    (5, [[1,0],[2,0],[3,0],[4,1],[4,2],[4,0]], [[0,3]]),
]

for i, (n, connections, ans) in enumerate(tests):
    res = sol.criticalConnections(n, connections)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
