# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
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


sol = Solution()
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
