# from pudb import set_trace; set_trace()
from typing import List
import heapq
import math


class Solution1:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """TLE
        """
        N = len(scores)
        adj = [[] for _ in range(N)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dijkstra(start: int) -> int:
            s = [0] * N
            visited = set()
            s[start] = scores[start]
            heap = [(-s[start], start)]
            res = []
            for i in range(4):
                cur_s, node = heapq.heappop(heap)
                visited.add(node)
                res.append((node, -cur_s))
                if i == 3:
                    break
                before_size = len(heap)
                for nei in adj[node]:
                    if nei not in visited and -cur_s + scores[nei] > s[nei]:
                        s[nei] = -cur_s + scores[nei]
                        heapq.heappush(heap, (-s[nei], nei))
                if len(heap) == before_size:  # no more node to go
                    break
            return res[-1][1] if len(res) == 4 else -1

        return max(dijkstra(n) for n in range(N))


class Solution2:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """After two hints, I got this solution passed.

        The idea is that once we settle on two connected nodes, say a and b, we
        can determine the other two nodes by looking at the nodes connected to
        a that are not b, and nodes connected to be that are not a. We check
        for the max among these nodes related to a and related to b. If the max
        nodes in these two camps are not the same, then the max possible score
        is the max nodes plus the scores of a and b. Otherwise, we need to pick
        the max on one camp and the second max on the other camp. of course, if
        it is not possible to pick out max or second max properly, we know
        a path is not possible.

        O(E + VlogV) 3855 ms, faster than 9.32%
        """
        N = len(scores)
        adj = [[] for _ in range(N)]
        for a, b in edges:
            adj[a].append((scores[b], b))
            adj[b].append((scores[a], a))
        for row in adj:
            row.sort(reverse=True)
        res = -1
        for a, b in edges:
            max1_a, max2_a = None, None
            count = 2
            for tup in adj[a]:
                if not count:
                    break
                if tup[1] != b:
                    if not max1_a:
                        max1_a = tup
                    elif not max2_a:
                        max2_a = tup
                    count -= 1
            if not max1_a:
                continue
            max1_b, max2_b = None, None
            count = 2
            for tup in adj[b]:
                if not count:
                    break
                if tup[1] != a:
                    if not max1_b:
                        max1_b = tup
                    elif not max2_b:
                        max2_b = tup
                    count -= 1
            if not max1_b:
                continue
            if max1_a[1] != max1_b[1]:
                res = max(res, scores[a] + scores[b] + max1_a[0] + max1_b[0])
            elif max2_a and max2_b:
                res = max(res, scores[a] + scores[b] + max1_a[0] + max(max2_a[0], max2_b[0]))
            elif max2_a:
                res = max(res, scores[a] + scores[b] + max1_b[0] + max2_a[0])
            elif max2_b:
                res = max(res, scores[a] + scores[b] + max1_a[0] + max2_b[0])
        return res


class Solution3:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        """We only need to store the largest three neighbors in the adjacency
        list. Inspired by lee215's solution

        https://leetcode.com/problems/maximum-score-of-a-node-sequence/discuss/1953706/JavaPython-Keep-3-Biggest-Neighbours

        2968 ms, faster than 28.40%
        """
        N = len(scores)
        adj = [[] for _ in range(N)]
        for a, b in edges:
            heapq.heappush(adj[a], b)
            heapq.heappush(adj[b], a)
        for i in range(N):
            adj[i] = heapq.nlargest(3, adj[i], key=lambda v: scores[v])
        res = -1
        for a, b in edges:
            for na in adj[a]:
                for nb in adj[b]:
                    if na != nb and na != b and nb != a:
                        res = max(res, scores[a] + scores[b] + scores[na] + scores[nb])
        return res


sol = Solution3()
tests = [
    ([5,2,9,8,4], [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]], 24),
    ([9,20,6,4,11,12], [[0,3],[5,3],[2,4],[1,3]], -1),
]

for i, (scores, edges, ans) in enumerate(tests):
    res = sol.maximumScore(scores, edges)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
