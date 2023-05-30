# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        N = len(coins)
        graph = defaultdict(set)
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)
        dists = defaultdict(int)
        queue = [n for n in graph if len(graph[n]) == 1]
        while len(graph) > 3:
            tmp = []
            for n in queue:
                for nei in graph[n]:
                    graph[nei].remove(n)
                    if coins[n] or dists[n]:
                        dists[nei] = max(dists[nei], dists[n] + 1)
                    if len(graph[nei]) == 1:
                        tmp.append(nei)
                del graph[n]
            queue = tmp
            print(graph, queue)
        print(dists[queue[0]], dists[queue[1]])
        if len(queue) == 2:
            if len(graph) == 2:
                return max(0, dists[queue[0]] + dists[queue[1]] + 1 - 4) * 2
            if len(graph) == 3:
                return max(0, dists[queue[0]] + dists[queue[1]] + 2 - 4) * 2
        return 0


sol = Solution()
tests = [
    # ([1,0,0,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5]], 2),
    # ([0,0,0,1,1,0,0,1], [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]], 2),
    # ([1,1], [[0,1]], 0),
    # ([0], [], 0),
    # ([1,1,0,0,1,0,0,1,0,1,0,0,1,0,0,1,0,0,1], [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[8,10],[9,11],[10,12],[11,13],[13,14],[13,15],[15,16],[16,17],[17,18]], 22),
    # ([1,0,0,1], [[0,1],[1,2],[2,3]], 0),
    # ([1,0,1,1,1,0,0,0,1,0,1,1,1,0,1], [[0,1],[0,2],[2,3],[1,4],[2,5],[2,6],[3,7],[3,8],[8,9],[4,10],[10,11],[7,12],[11,13],[12,14]], 10),
    ([1,0,0,1,1,1,0,1,0,1,0,0,1,1,1,1,0,0,0,0], [[0,1],[1,2],[1,3],[3,4],[3,5],[5,6],[5,7],[5,8],[8,9],[5,10],[6,11],[10,12],[11,13],[8,14],[8,15],[9,16],[12,17],[16,18],[14,19]], 4),
]

for i, (coins, edges, ans) in enumerate(tests):
    res = sol.collectTheCoins(coins, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
