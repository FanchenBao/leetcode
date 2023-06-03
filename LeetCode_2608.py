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
        

sol = Solution()
tests = [
    (7, [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]], 3),
    (4, [[0,1],[0,2]], -1),
    (8, [[0,1],[1,2],[2,3],[3,4],[4,5],[0,7],[0,6],[5,7],[5,6]], 4),
    (8, [[7,3],[1,5],[0,6],[3,1],[6,2],[7,4],[3,2],[5,2],[6,5],[0,3]], 3),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findShortestCycle(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
