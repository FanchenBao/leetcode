#! /usr/bin/env python3
"""
07/21/2019

Solution1 is an optimized DFS. The main magic happens in the to_dest() function.
Although this solution passed OJ, the performance was terrible, clocking at
240 ms, while the general solution is 48 ms. The main issue I had with this
problem was to determine how cyclic graph may occur. One situation is that a
cycle occurs within the same path: 0 -> 1 -> 2 -> 0 -> 1. This is resolved by
introducing the "edge" set which records each edge and its color in the path
to check for cycle. The other situation, which took me a long time to figure
out is visiting the same node repeatedly from a different path. This is allowed
if the repeated visit can yield smaller steps, but should be banned otherwise.
This is resolved by adding the "visited" dictionary.

Solution2 is BFS. The main logic is to use BFS to visit all nodes and record
the level of each node as the number of min steps the first time such node is
visited. The trick is that we need to keep a record of which node has been
visited on WHICH COLORED EDGE to prevent revisiting the same node. This yields
a much cleaner code, which passes OJ at 108 ms. Apparently, there is still room
for improvement.

Solution3 is also BFS, but much much cleaner. I copied the idea from here
https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339964/Python-BFS
Two things really blew my mind:
1. iterating through a growing list to serve as queue, never thought of that;
2. The magic of "res[n][c] = res[s][c ^ 1] + 1" to find the step without the
need to keep track of the level.
"""
from typing import List, Dict, Deque, Set
from collections import defaultdict, deque


class Solution1:
    def shortestAlternatingPaths(
        self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:
        red_dict: Dict[int, List[int]] = defaultdict(list)
        blue_dict: Dict[int, List[int]] = defaultdict(list)
        # create red edge and blue edge dict to make accessing the next node
        # easier
        for re in red_edges:
            red_dict[re[0]].append(re[1])
        for be in blue_edges:
            blue_dict[be[0]].append(be[1])
        MAX = 2 ** 31 - 1
        res = [MAX] * n
        res[0] = 0
        # red to blue
        self.to_dest(
            red_dict,
            blue_dict,
            0,
            set(),
            {"red": [MAX] * n, "blue": [MAX] * n},
            "red",
            "blue",
            res,
            1,
        )
        # blue to red
        self.to_dest(
            blue_dict,
            red_dict,
            0,
            set(),
            {"red": [MAX] * n, "blue": [MAX] * n},
            "blue",
            "red",
            res,
            1,
        )
        return [r if r != MAX else -1 for r in res]

    def to_dest(
        self, dict1, dict2, start, edges, visited, color1, color2, res, step
    ):
        """ edges record all the edges that have been visited in a single
            path. If there is a repeated edge, we have encountered a cycle.

            visited is a dictionary that records the number of steps to reach
            a certain start node for blue or red edge. If in the future, the
            same start node is reached again for the same colored edge, we
            check whether this time the number of steps is larger than last
            time. If it is larger, then there is no need to continue because
            the subsequent steps will all be larger than before. This serves
            as an anchor case for the recursion.
        """
        if step >= visited[color1][start]:
            return
        for node in dict1.get(start, []):
            # trapped in circle if the same colored-edge appears again
            if (color1, start, node) in edges:
                return
            edges.add((color1, start, node))
            res[node] = min(res[node], step)  # record min steps
            self.to_dest(
                dict2,
                dict1,
                node,
                edges,
                visited,
                color2,
                color1,
                res,
                step + 1,
            )
            edges.remove((color1, start, node))
        visited[color1][start] = step


class Solution2:
    def shortestAlternatingPaths(
        self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:
        # updated method of graph representation (learned from the discussion
        # post). I find it much cleaner than my original dictinary method.
        # However, it did not improve upoin runtime.
        graph: List[List[List[int]]] = [[[], []] for i in range(n)]
        for start, end in red_edges:
            graph[start][0].append(end)
        for start, end in blue_edges:
            graph[start][1].append(end)
        red_to_blue = self.bfs(graph, n, 0)
        blue_to_red = self.bfs(graph, n, 1)
        # breakpoint()
        return [
            min(red_to_blue[i], blue_to_red[i])
            if red_to_blue[i] != -1 and blue_to_red[i] != -1
            else max(red_to_blue[i], blue_to_red[i])
            for i in range(n)
        ]

    def bfs(self, graph, n, color):
        res: List[int] = [-1] * n
        queue: Deque[int] = deque()
        queue.append(0)
        lvl: int = 0
        num_nodes: int = 1  # number of nodes at the current level
        # record the nodes visited for each colored edge
        visited: List[Set[int]] = [set(), set()]
        while num_nodes:
            count: int = 0  # count the number of new nodes added to the queue
            for i in range(num_nodes):
                curr = queue.popleft()
                if res[curr] == -1:  # update res the first time a node is hit
                    res[curr] = lvl
                if curr not in visited[color]:  # keep bfs for unvisited nodes
                    next_nodes = graph[curr][color]
                    for node in next_nodes:
                        queue.append(node)
                        count += 1
                    visited[color].add(curr)
            num_nodes = count
            color ^= 1  # change color
            lvl += 1
        return res


class Solution3:
    def shortestAlternatingPaths(
        self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]
    ) -> List[int]:
        """ Inspired by the solution in the discussion post """
        # prepare the graph. It is a list of nodes; within each node, we have
        # two additional lists, one for all the edges in red, the other blue
        graph: List[List[List[int]]] = [[[], []] for i in range(n)]
        for s, e in red_edges:
            graph[s][0].append(e)
        for s, e in blue_edges:
            graph[s][1].append(e)
        # Prepare the results. It is a list of nodes; within each node, we have
        # two values, node[0] is the min steps coming from red edge, node[1]
        # blue edge. Everything initialized to -1
        res: List[List[int]] = [[-1, -1] for i in range(n)]
        res[0] = [0, 0]
        # Prepare the "queue" for BFS. Note the magic here that uses a list to
        # implement queue without having to do any pop. Each element represents
        # a node and the colored edge leading AWAY from the node. element[0] is
        # the node, element[1] color
        queue: List[List[int]] = [[0, 0], [0, 1]]
        for s, c in queue:
            # visit all nodes connected to the start s via color c
            for n in graph[s][c]:
                if res[n][c] == -1:
                    res[n][c] = res[s][c ^ 1] + 1  # magic happens here
                    queue.append([n, c ^ 1])
        return [
            min(r[0], r[1]) if r[0] != -1 and r[1] != -1 else max(r[0], r[1])
            for r in res
        ]


sol = Solution3()
red_edges = [[0, 1], [1, 2], [2, 3]]
blue_edges = [[1, 1], [2, 2]]
n = 4
print(sol.shortestAlternatingPaths(n, red_edges, blue_edges))
