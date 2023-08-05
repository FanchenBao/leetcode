# from pudb import set_trace; set_trace()
from typing import List, Set, Tuple, Dict
import math
from collections import defaultdict
import heapq


class Solution1:
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
        

class Solution2:
    def dijkstra(self, n: int, graph: Dict, src: int, dst: int) -> Tuple[List[int], int]:
        """graph is weighted"""
        min_weights = [math.inf] * n
        min_weights[src] = 0
        par = [-1] * n
        queue = [(0, src)]
        while queue:
            while queue and queue[0][0] > min_weights[queue[0][1]]:
                heapq.heappop(queue)
            cur_w, node = heapq.heappop(queue)
            if node == dst:
                break
            for child, w in graph[node].items():
                if cur_w + w < min_weights[child]:
                    heapq.heappush(queue, (cur_w + w, child))
                    min_weights[child] = cur_w + w
                    par[child] = node
        node = dst
        path = []
        while node != src:
            path.append(node)
            node = par[node]
        return [node] + path[::-1], min_weights[dst]

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        MAX_VAL = 2 * 10**9
        graph_max = defaultdict(dict)
        graph_ones = defaultdict(dict)
        neg_edges = set()
        for a, b, w in edges:
            if w > 0:
                graph_max[a][b] = w
                graph_max[b][a] = w
                graph_ones[a][b] = w
                graph_ones[b][a] = w
            else:
                graph_max[a][b] = MAX_VAL
                graph_max[b][a] = MAX_VAL
                graph_ones[a][b] = 1
                graph_ones[b][a] = 1
                neg_edges.add((a, b))

        path_max, min_weight_max = self.dijkstra(n, graph_max, source, destination)
        # a shortest path can be formed by non-neg edges, and the weight is
        # less than the target.
        # print(path_max, min_weight_max)
        if min_weight_max < target:
            return []
        # special case, we can set neg edges to any large value we want
        if min_weight_max == target:
            return [[u, v, w if w > 0 else MAX_VAL] for u, v, w in edges]

        path_ones, min_weight_ones = self.dijkstra(n, graph_ones, source, destination)
        # print(path_ones, min_weight_ones)
        # shortest path does require neg-edges, but when the neg-edges are all
        # assigned the smallest weight possible, the path weight is still larger
        # than the target.
        if min_weight_ones > target:
            return []

        def modify_edges(graph: Dict, reset_val: int) -> List:
            # try every pair of negative edges and return the answer when the first
            # such pair give the correct answer
            for a, b in neg_edges:
                graph[a][b] = 1
                graph[b][a] = 1
                cur_path, cur_weight = self.dijkstra(n, graph, source, destination)
                cur_neg_edges = set()
                for i in range(len(cur_path) - 1):
                    u, v = cur_path[i], cur_path[i + 1]
                    if (u, v) in neg_edges or (v, u) in neg_edges:
                        cur_neg_edges.add((u, v))
                non_neg_edge_weight = cur_weight - (len(cur_neg_edges) - 1) * reset_val - 1
                if ((a, b) in cur_neg_edges or (b, a) in cur_neg_edges) and non_neg_edge_weight + len(cur_neg_edges) <= target:
                    req_weight = target - non_neg_edge_weight
                    q, r = divmod(req_weight, len(cur_neg_edges))
                    for u, v in cur_neg_edges:
                        graph[u][v] = q
                        graph[v][u] = q
                    graph[a][b] += r
                    graph[b][a] += r
                    _, check_weight = self.dijkstra(n, graph, source, destination)
                    if check_weight == target:
                        return [[u, v, graph[u][v]] for u, v, w in edges]
                # backtrack
                for u, v in cur_neg_edges:
                    graph[u][v] = reset_val
                    graph[v][u] = reset_val
            return []

        res_from_graph_max = modify_edges(graph_max, MAX_VAL)
        if res_from_graph_max:
            return res_from_graph_max
        return modify_edges(graph_ones, 1)


sol = Solution2()
tests = [
    # (5, [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], 0, 1, 5, [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]),
    # (3, [[0,1,-1],[0,2,5]], 0, 2, 6, []),
    # (4, [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], 0, 2, 6, [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]),
    # (4, [[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]], 2, 3, 8, []),
    # (5, [[0,1,-1],[3,1,4],[4,2,3],[3,4,5],[1,4,6],[0,3,8],[2,1,-1],[3,2,2]], 0, 2, 6, [[0,1,5],[3,1,4],[4,2,3],[3,4,5],[1,4,6],[0,3,8],[2,1,1],[3,2,2]]),
    # (5, [[0,3,1],[1,2,-1],[2,3,7],[4,2,1],[2,0,-1],[4,1,9],[3,4,9]], 0, 1, 18, [[0,3,1],[1,2,10],[2,3,7],[4,2,1],[2,0,17],[4,1,9],[3,4,9]]),
    # (10, [[7,0,68],[1,2,61],[2,9,16],[4,7,95],[7,6,-1],[6,5,73],[8,5,42],[5,3,21],[9,3,13],[5,1,-1],[8,3,78],[5,7,-1],[6,9,38],[0,8,26],[0,6,-1],[4,8,68],[9,5,52],[8,2,90],[7,8,37]], 0, 1, 122, [[7,0,68],[1,2,61],[2,9,16],[4,7,95],[7,6,1000000005],[6,5,73],[8,5,42],[5,3,21],[9,3,13],[5,1,54],[8,3,78],[5,7,1000000005],[6,9,38],[0,8,26],[0,6,119],[4,8,68],[9,5,52],[8,2,90],[7,8,37]]),
    (20, [[0,10,40],[1,11,20],[6,2,53],[7,4,66],[5,10,41],[14,10,79],[9,11,69],[3,9,50],[13,8,51],[14,17,31],[16,17,14],[16,15,62],[15,8,37],[8,7,19],[7,3,-1],[18,12,50],[12,6,85],[3,6,29],[3,19,-1],[15,14,14],[0,17,29],[4,6,87],[7,9,-1],[14,12,54],[14,3,72],[9,1,-1],[19,0,-1],[2,14,17],[16,8,80],[19,4,52],[17,5,16],[0,2,73],[18,15,68]], 0, 1, 177, [[0,10,40],[1,11,20],[6,2,53],[7,4,66],[5,10,41],[14,10,79],[9,11,69],[3,9,50],[13,8,51],[14,17,31],[16,17,14],[16,15,62],[15,8,37],[8,7,19],[7,3,1000000005],[18,12,50],[12,6,85],[3,6,29],[3,19,1000000005],[15,14,14],[0,17,29],[4,6,87],[7,9,46],[14,12,54],[14,3,72],[9,1,1],[19,0,173],[2,14,17],[16,8,80],[19,4,52],[17,5,16],[0,2,73],[18,15,68]]),
]

for i, (n, edges, source, destination, target, ans) in enumerate(tests):
    res = sol.modifiedGraphEdges(n, edges, source, destination, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
