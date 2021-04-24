# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """LeetCode 1192

        I did not come up with this all by myself. I got stuck and the hint
        suggested that I take a look at Tarjan's Algo
        https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/

        The central of Tarjan is that we find the head of a graph. The
        definition of a head inside a graph is a node which does NOT have any
        back edge towards a node that has been visited before in DFS. In other
        words, a head is the root of a subtree inside a graph. From the head,
        we can only traverse forward. We cannot traverse backward (not counting
        the edge leading to the head).

        Tarjan is used on DAG. Although our graph is undirected, we can simulate
        it as a directed by traversing from small node to big node. In other
        words, a forward traversal follows an edge going from a small to big
        node. A backward edge is from a big node to a small node. Using Tarjan,
        we create two arrays. One is called disc (discovery) and the other low
        (the lowest node that can be reached with one backedge). It is important
        to stress that only ONE backedge is allowed to traverse backward when
        computing the low array.

        Once we finishes DFS, we populate the disc and low arrays. disc[i] is
        the number of steps needed to reach i in the DFS. low[i] is the value
        of disc[j] where j is the most previous node reachable from i using one
        backedge.

        A head is a node k where disc[k] == low[k], which means from node k, we
        cannot reach any other node before it.

        Our goal is to find all the head node k in the given graph, and the
        critical edges are the edge directly leading from a smaller node to k.

        2188 ms, 89% ranking.
        """
        graph = [[] for _ in range(n)]
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)

        disc = [0] * n
        low = [0] * n
        visited = set()

        def dfs(parent: int, node: int, step: int) -> None:
            disc[node] = step
            low[node] = step
            visited.add(node)
            for child in graph[node]:
                if child in visited and child != parent:
                    low[node] = min(low[node], disc[child])
                elif child not in visited:
                    dfs(node, child, step + 1)
                    low[node] = min(low[node], low[child])

        dfs(-1, 0, 0)
        res = []
        for i in range(n):
            if disc[i] == low[i] and i != 0:
                for pre in graph[i]:
                    if pre < i:
                        res.append([pre, i])
        return res


class Solution2:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        """This is a reproduction of the answer in this post:

        https://leetcode.com/problems/critical-connections-in-a-network/discuss/382638/DFS-detailed-explanation-O(orEor)-solution

        It has similar sense as Tarjan, but I think is better suited for this
        problem. Bascially, we DFS and if any child can lead to a node that has
        been visited before, then we are confident that the edge from current
        node to child is in a loop, and it must not be critical. We remove it.

        """
        graph = [[] for _ in range(n)]
        res = set()
        for n1, n2 in connections:
            graph[n1].append(n2)
            graph[n2].append(n1)
            res.add((min(n1, n2), max(n1, n2)))

        disc = [0] * n
        visited = set()

        def dfs(parent: int, node: int, step: int) -> None:
            disc[node] = step
            visited.add(node)
            # the number of steps to reach the earliest node reachable from the
            # current node
            back = n
            for child in graph[node]:
                if child == parent:
                    continue
                child_back = disc[child] if child in visited else dfs(node, child, step + 1)
                if child_back <= step:  # loop exists, can remove current edge
                    res.remove((min(node, child), max(node, child)))
                back = min(back, child_back)
            return back

        dfs(-1, 0, 0)
        return [list(r) for r in res]


sol = Solution2()
tests = [
    (4, [[0, 1], [1, 2], [2, 0], [1, 3]], [[1, 3]]),
    (4, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 0]], []),
    (6, [[0, 1], [1, 2], [2, 0], [1, 3], [3, 4], [3, 5], [4, 5]], [[1, 3]]),
    (4, [[0, 1], [1, 3], [3, 2], [2, 0]], []),
]

for i, (n, connections, ans) in enumerate(tests):
    res = sol.criticalConnections(n, connections)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
