# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution1:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        """This solution does not terminate BFS early, but it seems to be
        running faster.

        2777 ms
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = math.inf

        def bfs(root: int) -> int:
            visited = set()
            queue = set([root])
            lvl = 0
            size = math.inf
            while queue:
                tmp = set()
                for node in queue:
                    visited.add(node)
                    if node in tmp:  # odd number of nodes in cycle
                        size = min(size, 2 * lvl + 1)
                    for nei in graph[node]:
                        if nei in tmp:  # even number of nodes in cycle
                            size = min(size, 2 * (lvl + 1))
                        if nei not in visited:
                            tmp.add(nei)
                queue = tmp
                lvl += 1
            return size

        for i in range(n):
            res = min(res, bfs(i))
        return res if res < math.inf else -1


class Solution2:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        """Used the hint. That said, the hint was as simple as

        'How can BFS be used?'

        The solution here uses the most generic BFS, but with two checks for
        even-numbered cycle or odd-numbered cycle, and a counter for each level.

        For even-numbered cycle, we will put the same node in the next level,
        thus when we hit the next level, the problematic node will have more
        than one occurrences. That's the signal of an even-numbered cycle.

        For odd-numbered cycle, we will notice that a node at the current level
        has been put into the next level.

        O(V * (V + E)), 4147 ms, faster than 8.03%

        Although we terminate early, I think the overhead of using counter is
        costing more time.
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        res = math.inf

        def bfs(root: int) -> int:
            visited = set()
            queue = Counter([root])
            lvl = 0
            size = math.inf
            while queue:
                tmp = Counter()
                for node, c in queue.items():
                    if c > 1:  # even number of nodes in cycle
                        return 2 * lvl
                    visited.add(node)
                    if node in tmp:  # odd number of nodes in cycle
                        return min(size, 2 * lvl + 1)
                    for nei in graph[node]:
                        if nei not in visited:
                            tmp[nei] += 1
                queue = tmp
                lvl += 1
            return size

        for i in range(n):
            res = min(res, bfs(i))
        return res if res < math.inf else -1


class Solution3:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        """Inspired by https://leetcode.com/problems/shortest-cycle-in-a-graph/discuss/3366500/JavaC%2B%2BPython-BFS

        BFS from each node as root. We keep track of the distance from a node
        to the root. If during BFS, a node has already been visited, we check
        whether its distance to root is smaller than the distance from the
        current node to the root. If it is smaller, than the already-visited
        node must be a parent, which is allowed. Otherwise, the already-visited
        node is not a parent, which means we either have an edge connecting two
        peers, or an edge connecting a child up to a different parent. That is
        the signal for a cycle.

        When that happens, we simply add the distance of the current node to the
        distance of the already-visited node and add one more, which is the
        edge connecting these two nodes.

        O(N^2), 2794 ms, faster than 40.15%
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def bfs(root: int) -> int:
            """return the smallest cycle size when starting at root"""
            dists = [math.inf] * n
            queue = [root]
            dists[root] = 0
            res = math.inf
            while queue:
                tmp = []
                for node in queue:
                    for child in graph[node]:
                        if dists[child] == math.inf:  # not visited yet
                            dists[child] = 1 + dists[node]
                            tmp.append(child)
                        elif dists[child] >= dists[node]:  # child has been visited, and it is not the node's parent
                            res = min(res, dists[child] + dists[node] + 1)
                queue = tmp
            return res

        res = min(bfs(i) for i in range(n))
        return res if res < math.inf else -1


sol = Solution3()
tests = [
    (7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]], 3),
    (4, [[0,1],[0,2]], -1),
    (8, [[0,1],[1,2],[2,3],[3,4],[4,5],[0,7],[0,6],[5,7],[5,6]], 4),
    (8, [[7,3],[1,5],[0,6],[3,1],[6,2],[7,4],[3,2],[5,2],[6,5],[0,3]], 3),
    (6, [[4,2],[5,1],[5,0],[0,3],[5,2],[1,4],[1,3],[3,4]], 3),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findShortestCycle(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
