# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        """TLE
        """
        mat = defaultdict(set)
        for a, b in edges:
            mat[a].add(b)
            mat[b].add(a)
        vals_map = defaultdict(list)
        for i, v in enumerate(vals):
            vals_map[v].append(i)
        self.res = sum(len(lst) for lst in vals_map.values())

        def helper(mat, vals_map) -> None:
            if not mat or not vals_map:
                return
            max_nodes = vals_map[max(vals_map)]
            n = len(max_nodes)
            self.res += n * (n - 1) // 2
            for x in max_nodes:
                for y in mat[x]:
                    mat[y].remove(x)
                del mat[x]
            visited = set()
            for node in mat:
                if node not in visited:
                    visited.add(node)
                    queue = [node]
                    hashmap = defaultdict(list)
                    adj_mat = defaultdict(set)
                    while queue:
                        temp = []
                        for node in queue:
                            hashmap[vals[node]].append(node)
                            for child in mat[node]:
                                if child not in visited:
                                    visited.add(child)
                                    adj_mat[node].add(child)
                                    adj_mat[child].add(node)
                                    temp.append(child)
                        queue = temp
                    helper(adj_mat, hashmap)

        helper(mat, vals_map)
        return self.res


sol = Solution()
tests = [
    ([1,3,2,1,3], [[0,1],[0,2],[2,3],[2,4]], 6),
    ([1,1,2,2,3], [[0,1],[1,2],[2,3],[2,4]], 7),
    ([1], [], 1),
]

for i, (vals, edges, ans) in enumerate(tests):
    res = sol.numberOfGoodPaths(vals, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
