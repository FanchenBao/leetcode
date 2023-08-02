# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import defaultdict


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        MAX_VAL = 2 * 10**9
        graph = defaultdict(list)
        edges_dict = {}
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])
            edges_dict[(min(node, child), max(node, child))] =  w

        all_paths = []

        def dfs(node: int, group_edges: List[List[int]], visited: Set[int]) -> None:
            if node in visited:
                return
            if node == destination:
                cur_w = 0
                neg_edges = []
                for a, b, w in group_edges:
                    if w > 0:
                        cur_w += w
                    else:
                        neg_edges.append((a, b))
                if w <= target:
                    all_paths.append([cur_w, neg_edges])
                return
            visited.add(node)
            for child, w in graph[node]:
                group_edges.append([min(node, child), max(node, child), w])
                dfs(child, group_edges, visited)
                group_edges.pop()
            visited.remove(node)

        dfs(source, [], set())

        # filter all_paths
        filtered_paths = []
        for cur_w, neg_edges in all_paths:
            if cur_w > target or (cur_w == target and len(neg_edges) > 0) or (cur_w < target and not neg_edges):
                continue
            if cur_w == target and not neg_edges:
                # we can turn all the -1 edges into whatever large value
                return [[a, b, w if w > 0 else MAX_VAL] for a, b, w in edges]
            # cur_w < target and there are neg_edges
            filtered_paths.append((cur_w, neg_edges))
        if not filtered_paths:
            return []
        filtered_paths.sort(key=lambda tup: (len(tup[1]), tup[0]))
        for edge in filtered_paths[1][:-1]:
            edges_dict[edge] = 1
        edges_dict[filtered_paths[-1]] = target - filtered_paths[0] - (len(filtered_paths) - 1)
        return [[a, b, w if w > 0 else MAX_VAL] for (a, b), w in edges_dict.items()]
        

sol = Solution()
tests = [
    (5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5, [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]),
    (3, [[0,1,-1],[0,2,5]], 0, 2, 6, []),
    (4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6, [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]),
]

for i, (n, edges, source, destination, target, ans) in enumerate(tests):
    res = sol.modifiedGraphEdges(n, edges, source, destination, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
