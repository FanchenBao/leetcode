# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import defaultdict, Counter


class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        trip_dicts = defaultdict(Counter)
        for a, b in trips:
            if a > b:
                a, b = b, a
            trip_dicts[a][b] += 1

        required_nodes = Counter()

        def dfs(root: int, node: int, path: Set[int]) -> None:
            path.add(node)
            if node in trip_dicts[root]:
                for p in path:
                    required_nodes[p] += trip_dicts[root][node]
                del trip_dicts[root][node]
            if trip_dicts[root]:
                for child in graph[node]:
                    if child not in path:
                        dfs(root, child, path)
            # backtracking
            path.remove(node)

        for root in trip_dicts:
            dfs(root, root, set())
        
        memo = {}
        def dp(node: int, slashed: bool, par: int) -> int:
            if (node, slashed) not in memo:
                memo[(node, slashed)] = 0
                if slashed:
                    for child in graph[node]:
                        if child != par:
                            memo[(node, slashed)] += dp(child, False, node)
                    memo[(node, slashed)] += required_nodes[node] * price[node] // 2
                else:
                    for child in graph[node]:
                        if child != par:
                            memo[(node, slashed)] += min(dp(child, True, node), dp(child, False, node))
                    memo[(node, slashed)] += required_nodes[node] * price[node] 
            return memo[(node, slashed)]

        return min(dp(0, True, -1), dp(0, False, -1))


sol = Solution()
tests = [
    (4, [[0,1],[1,2],[1,3]], [2,2,10,6], [[0,3],[2,1],[2,3]], 23),
    (2, [[0,1]], [2,2], [[0,0]], 1),
    (5, [[1,2],[2,0],[0,3],[3,4]], [12,26,22,12,2], [[3,3],[3,2],[3,0],[3,4],[1,1],[2,2],[4,0],[0,2],[2,3],[2,1],[4,2],[0,1],[4,2],[0,4],[0,3],[4,0],[4,0],[3,3],[4,3],[2,2],[4,2],[1,4],[3,2],[4,4],[4,2],[2,3],[4,3],[4,4],[4,2],[0,4],[4,2],[3,4],[4,0],[3,2],[3,1],[2,0],[0,4],[3,4],[2,0],[1,4],[4,2],[4,4],[2,1],[0,1],[4,1],[3,4],[0,4],[2,0],[2,0],[3,3],[4,4],[0,1],[0,1],[0,1],[2,0],[0,1],[3,1],[3,4],[3,4],[4,2],[0,4],[4,4],[3,2],[2,1],[3,2],[1,4],[1,0],[4,2],[4,3],[3,1],[4,4],[3,1],[1,0],[0,0],[0,0],[3,0],[0,2],[2,2],[3,3],[0,3]], 2037),
    (40, [[0,28],[6,29],[7,34],[8,5],[5,20],[9,12],[12,3],[13,11],[14,32],[18,3],[3,20],[22,15],[15,28],[26,25],[25,20],[20,17],[27,16],[28,2],[31,2],[2,21],[21,23],[23,4],[4,35],[32,19],[33,39],[34,10],[10,11],[11,16],[16,17],[17,1],[1,24],[24,30],[30,19],[19,39],[35,29],[29,38],[36,38],[37,39],[38,39]], [4,14,4,8,26,26,12,6,10,30,30,28,2,20,8,26,10,30,18,30,18,30,16,14,18,6,20,24,20,18,8,4,12,30,12,6,30,22,28,8], [[10,15],[5,21],[16,28],[0,31],[13,37],[22,27],[13,7],[23,10],[7,4],[0,11],[35,20],[7,12],[16,15],[21,6],[7,4],[5,25],[10,22],[10,1],[20,8],[20,23],[38,39],[20,2]], 3041),
    (10, [[0,4],[2,4],[6,3],[8,3],[3,4],[4,7],[7,5],[5,1],[1,9]], [10,6,4,8,8,6,10,8,2,2], [[9,6],[5,5],[8,4],[7,8],[4,5],[0,8],[3,4],[6,1],[8,0],[4,5],[7,5],[9,0],[6,3],[0,1],[3,9],[6,7],[1,5],[0,9],[0,4],[2,0],[0,3],[1,8],[5,3],[6,0],[6,4],[9,0],[8,7],[5,6],[3,6],[8,8],[7,8],[6,3],[5,7],[5,3],[8,7],[7,7],[2,5],[4,2],[0,8],[3,2],[7,2],[1,6],[2,7],[1,7]], 826),
]

for i, (n, edges, price, trips, ans) in enumerate(tests):
    res = sol.minimumTotalPrice(n, edges, price, trips)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
