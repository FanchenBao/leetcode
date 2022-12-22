# from pudb import set_trace; set_trace()
from typing import List, Tuple
import math
from collections import defaultdict


class Solution1:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """The observation is that given two connected nodes a and b. If we know
        the total distance of node a is Sa, we can express it as such

        Sa = X + M + Y,
            where X is the total distance of going from node a to all the other
            nodes NOT passing through node b.
            where Y is the total distance of going from node b to all the other
            nodes NOT passing through node a.
            where M is the total number of nodes in the substree (including b)
            rooted at b NOT passing through node a.

        We can also write the total distance of node b as such

        Sb = Y + N + X,
            where X and Y are the same as defined above.
            where N is the total number of nodes in the subtree (including a)
            rooted at a NOT passing through node b.

        Thus, given Sa, we can compute Sb = Sa - M + N

        In other words, since the graph is connected, once we know the total
        distance of one node, and the size of the subtree rooted at each node,
        we can directly compute the total distance of all the other nodes.

        We use DFS to find the total distance with regard to node 0, as well as
        recording the subtree size of each node.

        Then we use BFS to traverse from node 0 down, and use the formula above
        to find the total distance of all the other nodes.

        O(N), 1004 ms, faster than 93.33%
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0] * n
        subtree_size = [0] * n
        visited = set()

        def dfs(idx: int) -> int:
            subtree_size[idx], dist = 1, 0
            visited.add(idx)
            for nex in graph[idx]:
                if nex not in visited:
                    dist += dfs(nex) + subtree_size[nex]
                    subtree_size[idx] += subtree_size[nex]
            return dist

        res[0] = dfs(0)
        queue = [[nex, 0] for nex in graph[0]]
        while queue:
            tmp = []
            for nex, idx in queue:
                res[nex] = res[idx] - subtree_size[nex] + n - subtree_size[nex]
                for nn in graph[nex]:
                    if not res[nn]:
                        tmp.append([nn, nex])
            queue = tmp
        return res


class Solution2:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """This is the solution from the official solution. It's exactly the
        same as solution1, but with two DFS and much simpler implementation.

        The key difference is that we don't need to use a visited set, because
        the graph is a tree. The only way for a node to go back is to go back
        to its parent. So we only have to check if the next node is equal to the
        parent.

        Furthermore, using a second DFS is simpler than BFS.

        O(N), 949 ms, faster than 100.00% 
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0] * n
        subtree_size = [1] * n

        def dfs1(idx: int, parent: int) -> None:
            for nex in graph[idx]:
                if nex != parent:
                    dfs1(nex, idx)
                    subtree_size[idx] += subtree_size[nex]
                    res[idx] += res[nex] + subtree_size[nex]

        def dfs2(idx: int, parent: int) -> None:
            for nex in graph[idx]:
                if nex != parent:
                    res[nex] = res[idx] - subtree_size[nex] + n - subtree_size[nex]
                    dfs2(nex, idx)

        dfs1(0, -1)
        dfs2(0, -1)
        return res


sol = Solution2()
tests = [
    (6, [[0,1],[0,2],[2,3],[2,4],[2,5]], [8,12,6,10,10,10]),
    (1, [], [0]),
    (2, [[1,0]], [1,1]),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.sumOfDistancesInTree(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
