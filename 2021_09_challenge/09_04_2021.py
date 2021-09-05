# from pudb import set_trace; set_trace()
from typing import List, Set


class Solution1:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """LeetCode 834

        TLE. It's O(N^2). Given that N can be 3 * 10^4, it is not surprising
        that this solution times out.

        This is a BFS-based solution.
        """
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        dist_mat = [[0] * n for _ in range(n)]
        queue = [0]
        seen = set([0])
        while queue:
            next_lvl = []
            for par in queue:
                for child in tree[par]:
                    if child not in seen:
                        for anc in seen:
                            dist_mat[child][anc] = 1 + dist_mat[par][anc]
                            dist_mat[anc][child] = 1 + dist_mat[par][anc]
                        seen.add(child)
                        next_lvl.append(child)
            queue = next_lvl
        return [sum(row) for row in dist_mat]


class Solution2:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        """I am very proud of myself solving this one. We run two rounds of dfs
        for this. The first round dfs, dist_from_root, we compute the total
        distance from a node to all of its children. And we also count the total
        number of children a node has.

        The second round dfs, solve, we compute the total distance for each
        node. The main insight in this round is that given a node and its parent,
        the total distance is the sum of the distance from the node to all its
        children (this is trivial as it has already been computed by
        dist_from_root), and the distance going from the node to its parent and
        all of distance from the parent to the nodes other than the current node
        and its children (let's call this other_dist). When we solve a node, it
        is guaranteed that we have already solved the total distance for its
        parent. So to compute other_dist, we do total dist from parent minus
        the total dist from parent to the branch that includes the current node.
        The total distance from parent to the branch that includes the current
        node is the total distance from the current node to all its children
        (computed already by dist_from_root) and the total number of nodes on
        this branch (indirectly computed by dist_from_root as well).

        There we have it. Two rounds of dfs, both O(N) because each node is
        visited once. Total time complexity O(N), 1100 ms, 26% ranking.

        UPDATE:

        We are very very close to the official solution. The only thing that
        we lack is brevity. We use more space than the official solution,
        because we fail to see two things:

        1. the set seen is not needed, because we are handling a tree. All we
        need to do to prevent revisiting node is node != parent
        2. dist_count can be split into node count and distance count. Distance
        count can be reused as res in the second round of dfs. The key insight
        for this reuse is that res[node] = res[par] - count[node] + n - count[node]
        We have discovered n - count[node] ourselves. But here
        res[par] - count[node] represents the distance from node to its children
        plus the distance from par to all the other nodes (i.e. other_dist).
        """
        tree = [[] for _ in range(n)]
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)

        def dist_from_root(node: int, seen: Set[int], dist_count: List[List[int]]) -> None:
            """dist_count[i] = [
                total_distance_from_i_to_children,
                total_number_of_children_of_i,
            ]
            """
            seen.add(node)
            for child in tree[node]:
                if child not in seen:
                    dist_from_root(child, seen, dist_count)
                    dist_count[node][1] += dist_count[child][1] + 1
                    dist_count[node][0] += dist_count[child][0] + dist_count[child][1] + 1

        def solve(node: int, par: int, seen: Set[int], dist_count: List[List[int]], res: List[int]) -> None:
            seen.add(node)
            res[node] += dist_count[node][0]
            if par >= 0:
                # other_dist is the sum of dist from par to the nodes that are
                # not node's children
                other_dist = res[par] - (dist_count[node][0] + dist_count[node][1] + 1)
                res[node] += other_dist + (n - dist_count[node][1] - 1)
            for child in tree[node]:
                if child not in seen:
                    solve(child, node, seen, dist_count, res)

        dist_count = [[0, 0] for _ in range(n)]
        dist_from_root(0, set(), dist_count)
        res = [0] * n
        solve(0, -1, set(), dist_count, res)
        return res


sol = Solution2()
tests = [
    (6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]], [8, 12, 6, 10, 10, 10]),
    (1, [], [0]),
    (2, [[1, 0]], [1, 1]),
]

for i, (n, edges, ans) in enumerate(tests):
    res = sol.sumOfDistancesInTree(n, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
