# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        """No need to traverse. Just build the graph. For each node, find the
        max sum of at most k nodes, and we get the max star sum for the curernt
        node serving as center. Go through all nodes as center node, and we have
        the solution.

        O(MN), where M is the number of edges and N is the number of nodes.
        1529 ms, faster than 94.80% 
        """
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(vals[j])
            graph[j].append(vals[i])
        res = max(vals)
        for i, nodes in graph.items():
            nodes.sort(reverse=True)
            s = 0
            cur_max = 0
            for j in range(min(k, len(nodes))):
                s += nodes[j]
                cur_max = max(cur_max, s)
            res = max(res, cur_max + vals[i])
        return res
        

sol = Solution()
tests = [
    ([1,2,3,4,10,-10,-20], [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], 2, 16),
    ([-5], [], 0, -5),
]

for i, (vals, edges, k, ans) in enumerate(tests):
    res = sol.maxStarSum(vals, edges, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
