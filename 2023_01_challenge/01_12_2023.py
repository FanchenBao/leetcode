# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import Counter


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        """LeetCode 1519

        DFS

        O(N), 3023 ms, faster than 74.36%
        """
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        res = [0] * n

        def dfs(idx, par) -> Counter:
            cur = Counter()
            cur[labels[idx]] += 1
            for nex in graph[idx]:
                if nex != par:
                    cur += dfs(nex, idx)
            res[idx] = cur[labels[idx]]
            return cur

        dfs(0, -1)
        return res


sol = Solution()
tests = [
    (7, [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], "abaedcd", [2,1,1,1,1,1,1]),
    (4, [[0,1],[1,2],[0,3]], "bbbb", [4,2,1,1]),
    (5, [[0,1],[0,2],[1,3],[0,4]], "aabab", [3,2,1,1,1]),
]

for i, (n, edges, labels, ans) in enumerate(tests):
    res = sol.countSubTrees(n, edges, labels)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
