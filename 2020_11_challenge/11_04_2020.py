# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def get_height(self, adj_list, root, seen, cache):
        seen.add(root)
        children_h = 0
        for child in adj_list[root]:
            if child not in seen:
                if child not in cache[root]:
                    cache[root][child] = self.get_height(adj_list, child, seen, cache)
                children_h = max(children_h, cache[root][child])
        return children_h + 1

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """34% ranking.
        
        Without a cache, this method times out. However, after adding a cache,
        which records the height of a branch from a root to each of its child,
        we are able to reduce computation tremendously and pass the OJ.
        """
        cache = [dict() for _ in range(n)]  # key component in the algo
        adj_list = [[] for _ in range(n)]
        min_h = math.inf
        res = []
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        for root, children in enumerate(adj_list):
            if len(children) > 1:
                height = self.get_height(adj_list, root, set(), cache)
                if height < min_h:
                    min_h = height
                    res = [root]
                elif height == min_h:
                    res.append(root)
        return res if res else list(range(n))


class Solution2:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """From the solution, topological sort. Removing the leaves layer
        by layer, then the last two or one node left are the roots that can
        generate min height trees.
        """
        if n <= 2:
            return list(range(n))
        adj_list = [[] for _ in range(n)]
        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        leaves = [root for root, children in enumerate(adj_list) if len(children) == 1]
        remains = n
        while remains > 2:
            # update adjacency list to remove the current leaves and convert
            # some interval nodes to new leaves
            remains -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                for child in adj_list[leaf]:
                    adj_list[child].remove(leaf)
                    if len(adj_list[child]) == 1:
                        new_leaves.append(child)
            leaves = new_leaves
        return leaves


sol = Solution2()
tests = [
    (4, [[1, 0], [1, 2], [1, 3]], [1]),
    (6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]], [3, 4]),
    (1, [], [0]),
    (2, [[0, 1]], [0, 1]),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.findMinHeightTrees(n, edges)
    if sorted(res) == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
