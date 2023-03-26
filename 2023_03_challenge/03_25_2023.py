# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from itertools import accumulate


class Solution1:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """LeetCode 2316

        Find the number of nodes in each clique, then sum all pair-wise products
        from the list of clique sizes.

        We use DFS to find clique size, and prefix sum to speed up the pair-wise
        product sum.

        O(N + E + N), 2229 ms, faster than 52.31%
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        not_visited = set(range(n))

        def dfs(i: int) -> None:
            if i in not_visited:
                not_visited.remove(i)
                for j in graph[i]:
                    dfs(j)

        pre_size = n
        clique_sizes = []
        for i in range(n):
            if i in not_visited:
                dfs(i)
                clique_sizes.append(pre_size - len(not_visited))
                pre_size = len(not_visited)
        presum = list(accumulate(clique_sizes))
        return sum(clique_sizes[i] * presum[i - 1] for i in range(len(clique_sizes) - 1, 0, -1))


class Solution2:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        """Without using prefix sum. Everything else is the same as Solution1,
        but we can find the sum of the remaining nodes along the way.

        2559 ms, faster than 14.59%
        """
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        not_visited = set(range(n))

        def dfs(i: int) -> None:
            if i in not_visited:
                not_visited.remove(i)
                for j in graph[i]:
                    dfs(j)

        remain_size = n
        res = 0
        for i in range(n):
            if i in not_visited:
                dfs(i)
                curr_clique_size = remain_size - len(not_visited)
                remain_size = len(not_visited)
                res += curr_clique_size * remain_size
        return res


sol = Solution2()
tests = [
    (3, [[0,1],[0,2],[1,2]], 0),
    (7, [[0,2],[0,5],[2,4],[1,6],[5,4]], 14),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.countPairs(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
