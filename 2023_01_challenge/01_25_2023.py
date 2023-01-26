# from pudb import set_trace; set_trace()
from typing import List, Set
import math


class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        """LeetCode 2359

        The fact that each node has at most one outgoing edge means that any
        node can only be reached by node1 or node2 in a unique path, or not
        reached at all. Therefore, we can start from node1, traverse the entire
        path to obtain the unique distance from it to all the nodes accessible
        to it. We do the same to node2. Any nodes not accessible have the
        distance set to inf.

        Then, we jsut compare the two distances to each node from node1 and
        node2, get their max, and find the overall min, along with the node that
        allows such min.

        O(N), 2369 ms, faster than 27.59%
        """
        N = len(edges)
        dist1 = [math.inf] * N
        dist2 = [math.inf] * N

        def dfs(node: int, visited: Set[int], dist: int, dist_list: List[int]) -> None:
            visited.add(node)
            dist_list[node] = dist
            nex = edges[node]
            if nex == -1 or nex in visited:
                return
            dfs(nex, visited, dist + 1, dist_list)

        dfs(node1, set(), 0, dist1)
        dfs(node2, set(), 0, dist2)
        d, idx = min((max(d1, d2), i) for i, (d1, d2) in enumerate(zip(dist1, dist2)))
        return idx if d < math.inf else -1


sol = Solution()
tests = [
    ([2,2,3,-1], 0, 1, 2),
    ([1,2,-1], 0, 2, 2),
    ([-1, 2, -1], 0, 2, -1),
    ([1, 0], 1, 0, 0),
]

for i, (edges, node1, node2, ans) in enumerate(tests):
    res = sol.closestMeetingNode(edges, node1, node2)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
