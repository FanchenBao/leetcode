# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict, Counter


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        """Hint.

        I tried many methods, but not able to figure it out. The hints are very
        very helpful. It's more of how we leverage the property of the tree
        rather than finding a data structure to traverse the tree.

        The underlying method is topological sort, which we have been using. But
        we were not able to figure out the key element of removing both the
        nodes with coin and their parents, if applicable.

        O(N + E), 2448 ms, faster than 20.49%
        """
        N = len(coins)
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        # round 1, remove all the leaves that are not coins
        queue = [n for n in graph if len(graph[n]) == 1 and not coins[n]]
        while queue:
            tmp = []
            for n in queue:
                for nei in graph[n]:
                    graph[nei].remove(n)
                    if len(graph[nei]) == 1 and not coins[nei]:
                        tmp.append(nei)
                del graph[n]
            queue = tmp
        # round 2, remove all the leaves that are coins and its parent, if its
        # parent is removable (i.e., the parent has only indegree 1 after its
        # child is removed)
        queue = [n for n in graph if len(graph[n]) == 1 and coins[n]]
        for _ in range(2):
            tmp = []
            for n in queue:
                for nei in graph[n]:
                    graph[nei].remove(n)
                    if len(graph[nei]) == 1:
                        tmp.append(nei)
                del graph[n]
            queue = tmp
        # the remaining nodes in the graph are the ones we must visit. Since we
        # have to start at some node and end at that node again, all the edges
        # in between the nodes must be traversed twice.
        return max(0, len(graph) - 1) * 2


sol = Solution()
tests = [
    ([1,0,0,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5]], 2),
    ([0,0,0,1,1,0,0,1], [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]], 2),
    ([1,1], [[0,1]], 0),
    ([0], [], 0),
    ([1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[8,10],[9,11],[10,12],[11,13],[13,14],[13,15],[15,16],[16,17],[17,18]], 22),
    ([1,0,0,1], [[0,1],[1,2],[2,3]], 0),
    ([1,0,1,1,1,0,0,0,1,0,1,1,1,0,1], [[0,1],[0,2],[2,3],[1,4],[2,5],[2,6],[3,7],[3,8],[8,9],[4,10],[10,11],[7,12],[11,13],[12,14]], 10),
    ([1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0], [[0,1],[1,2],[1,3],[3,4],[3,5],[5,6],[5,7],[5,8],[8,9],[5,10],[6,11],[10,12],[11,13],[8,14],[8,15],[9,16],[12,17],[16,18],[14,19]], 4),
]

for i, (coins, edges, ans) in enumerate(tests):
    res = sol.collectTheCoins(coins, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
