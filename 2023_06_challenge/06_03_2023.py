# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution1:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """LeetCode 1376

        BFS. When BFS, each level has to also record the number of minutes
        passed so far for the current node.

        O(E + V), 1302 ms, faster than 68.03%
        """
        tree = defaultdict(list)
        for i, m in enumerate(manager):
            tree[m].append(i)
        queue = [(headID, 0)]
        res = 0
        while queue:
            tmp = []
            for m, t in queue:
                res = max(res, t)
                for child in tree[m]:
                    tmp.append((child, t + informTime[m]))
            queue = tmp
        return res


class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        """DFS

        1496 ms, faster than 19.30%
        """
        tree = defaultdict(list)
        for i, m in enumerate(manager):
            tree[m].append(i)

        def dfs(node: int) -> int:
            if not tree[node]:
                return 0
            return informTime[node] + max(dfs(child) for child in tree[node])

        return dfs(headID)


sol = Solution2()
tests = [
    (1, 0, [-1], [0], 0),
    (6, 2, [2,2,-1,2,2,2], [0,0,1,0,0,0], 1),
    (7, 6, [1,2,3,4,5,6,-1], [0,6,5,4,3,2,1], 21),
]

for i, (n, headID, manager, informTime, ans) in enumerate(tests):
    res = sol.numOfMinutes(n, headID, manager, informTime)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
