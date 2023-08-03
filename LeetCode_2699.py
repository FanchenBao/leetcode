# from pudb import set_trace; set_trace()
from typing import List, Set
import math
from collections import defaultdict


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        """TLE.

        The basic idea is correct, but the process of finding all the paths is
        too slow because there could be a LOT OF paths. Not all of them shall
        be included.
        """
        MAX_VAL = 2 * 10**9
        graph = defaultdict(list)
        edges_dict = {}
        for a, b, w in edges:
            graph[a].append([b, w])
            graph[b].append([a, w])
            edges_dict[(min(a, b), max(a, b))] = w

        all_paths = []
        self.min_weight = math.inf
        self.min_neg_edges = math.inf

        def dfs(node: int, group_edges, visited: Set[int]) -> None:
            if node in visited:
                return
            # print(node, group_edges)
            if node == destination:
                self.min_weight = min(self.min_weight, group_edges[0])
                self.min_neg_edges = min(self.min_neg_edges, len(group_edges[1]))
                all_paths.append([group_edges[0], [tup for tup in group_edges[1]]])
                return
            visited.add(node)
            for child, w in graph[node]:
                if w > 0:
                    group_edges[0] += w
                else:
                    group_edges[1].append((min(node, child), max(node, child)))
                if group_edges[0] <= target and (not all_paths or (group_edges[0] <= self.min_weight or len(group_edges[1]) <= self.min_neg_edges)):
                    dfs(child, group_edges, visited)
                if w > 0:
                    group_edges[0] -= w
                else:
                    group_edges[1].pop()
            visited.remove(node)

        dfs(source, [0, []], set())
        # print(all_paths)

        # filter all_paths
        filtered_paths = []
        for cur_w, neg_edges in all_paths:
            if cur_w == target and neg_edges:
                continue
            if cur_w < target and not neg_edges:
                return []
            if cur_w == target and not neg_edges:
                # we can turn all the -1 edges into whatever large value
                return [[a, b, w if w > 0 else MAX_VAL] for a, b, w in edges]
            # cur_w < target and there are neg_edges
            filtered_paths.append((cur_w, neg_edges))
        if not filtered_paths:
            return []
        filtered_paths.sort(key=lambda tup: (len(tup[1]), tup[0]))
        tgt_path = filtered_paths[0]
        for edge in tgt_path[1][:-1]:
            edges_dict[edge] = 1
        edges_dict[tgt_path[1][-1]] = target - tgt_path[0] - (len(tgt_path[1]) - 1)
        return [[a, b, w if w > 0 else MAX_VAL] for (a, b), w in edges_dict.items()]
        

sol = Solution()
tests = [
    # (5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5, [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]),
    # (3, [[0,1,-1],[0,2,5]], 0, 2, 6, []),
    # (4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6, [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]),
    # (4, [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]], 2, 3, 8, []),
    (5, [[0,1,-1],[3,1,4],[4,2,3],[3,4,5],[1,4,6],[0,3,8],[2,1,-1],[3,2,2]], 0, 2, 6, [[0,1,5],[3,1,4],[4,2,3],[3,4,5],[1,4,6],[0,3,8],[2,1,1],[3,2,2]]),
]

for i, (n, edges, source, destination, target, ans) in enumerate(tests):
    res = sol.modifiedGraphEdges(n, edges, source, destination, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
