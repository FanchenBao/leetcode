# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq
from collections import deque


class Solution0:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """TLE"""
        M, N = len(grid), len(grid[0])
        dp = [[math.inf] * N for _ in range(M)]
        queue = [(M - 1, N - 1)]
        dp[M - 1][N - 1] = grid[M - 1][N - 1]
        while queue:
            temp = set()
            for i, j in queue:
                for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N:
                        old = dp[ni][nj]
                        dp[ni][nj] = min(dp[ni][nj], dp[i][j] + grid[ni][nj])
                        if old != dp[ni][nj]:
                            temp.add((ni, nj))
            queue = temp
        return dp[0][0]


class Solution1:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """Use the first hint, and try Dijkstra

        Two things:
            * the good: I can code up Dijkstra from scratch
            * the not so bad: the intuition to turn a grid path problem to a
                graph problem still needs improvement.

        The key is to realize that we can consider a path going into a cell
        with obstacle as a path of weight 1, whereas a path going into an empty
        cell as a path of weight 0. Then the problem becomes to find a path
        with min weight from top left to bottom right. This is exactly what
        Dijkstra does.

        O(MNlogMN), 5857 ms, faster than 60.79%

        UPDATE: no need to use a visited set, because whether to add a node to
        the heap is entirely dependent on whether the new weight is smaller
        than the old weight.
        """
        heap = [(0, 0, 0)]
        M, N = len(grid), len(grid[0])
        weights = [[math.inf] * N for _ in range(M)]
        weights[0][0] = 0
        while heap:
            w, i, j = heapq.heappop(heap)
            if i == M - 1 and j == N - 1:
                break
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and w + grid[ni][nj] < weights[ni][nj]:
                    weights[ni][nj] = w + grid[ni][nj]
                    heapq.heappush(heap, (weights[ni][nj], ni, nj))
        return w


class Solution2:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        """0-1 BFS

        Ref: https://www.geeksforgeeks.org/0-1-bfs-shortest-path-binary-graph/

        0-1 BFS is a special case of Dijkstra where each edge's weight is
        either 0 or 1. This allows us to use a deque to ensure only the nodes
        with the smallest cum-weights get popped (i.e. no need for a heap).
        Basically, if the current edge has 0 weight, the node goes to the left
        of the deque (i.e. it will be popped first), otherwise it goes to the
        right. This works because the cum-weights of the left node in the deque
        is always one smaller than the cum-weights of the right node.

        O(MN), 6117 ms, faster than 54.35%
        """
        dq = deque([(0, 0)])
        M, N = len(grid), len(grid[0])
        weights = [[math.inf] * N for _ in range(M)]
        weights[0][0] = 0
        while dq:
            i, j = dq.popleft()
            if i == M - 1 and j == N - 1:
                break
            for di, dj in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                ni, nj = i + di, j + dj
                if M > ni >= 0 <= nj < N and weights[ni][nj] == math.inf:
                    weights[ni][nj] = grid[ni][nj] + weights[i][j]
                    if grid[ni][nj] == 0:
                        dq.appendleft((ni, nj))
                    else:
                        dq.append((ni, nj))
        return weights[M - 1][N - 1]



sol = Solution2()
tests = [
    ([[0,1,1],[1,1,0],[1,1,0]], 2),
    ([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.minimumObstacles(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
