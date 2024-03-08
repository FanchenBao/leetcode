# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution1:
    def bfs(self, thresh: int, manhattan: List[List[int]]) -> bool:
        if manhattan[0][0] < thresh:
            return False
        N = len(manhattan)
        queue = [(0, 0, manhattan[0][0])]
        visited = [[0] * N for _ in range(N)]
        visited[0][0] = 1
        while queue:
            tmp = []
            for i, j, s in queue:
                if i == N - 1 and j == N - 1:
                    return True
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                        next_s = min(s, manhattan[ni][nj])
                        if next_s >= thresh:
                            tmp.append((ni, nj, next_s))
                            visited[ni][nj] = 1
            queue = tmp
        return False

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        I started with a barebone BFS, keeping track of all paths that
        can potentially get a bigger safeness. However, it times out.

        Then I tried Dijkstra, but due to some technical issues with the
        computation of manhattan, that method didn't pan out. But I wil try
        it again.

        Finally, I went for the first hint, which immediately pointed me
        to the right direction. We will simply binary search this. Pick some
        threshold, and then BFS the grid and see if it is possible to get
        from top left to bottom right.

        O(N^2logN), 4388 ms, faster than 52.78%
        """
        N = len(grid)
        manhattan = [[1000000000] * N for _ in range(N)]
        # find all the thieves, and put them in the queue
        queue = []
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    queue.append((i, j, 0))
                    manhattan[i][j] = 0
        # fill out manhattan by finding the min Manhattan distance of each cell
        while queue:
            tmp = []
            for i, j, d in queue:
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and d + 1 < manhattan[ni][nj]:
                        manhattan[ni][nj] = d + 1
                        tmp.append((ni, nj, d + 1))
            queue = tmp

        lo, hi = -1, 2 * N
        while lo < hi:
            mid = (lo + hi) // 2
            if self.bfs(mid, manhattan):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1


class Solution2:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        """
        Try Dijkstra.

        Dijkstra works. I did try it yesterday and before but it didn't work
        out. Now that I think about it, the failure was due to the problem
        of computing the manhattan matrix. Once we fixed that isssue, both
        the binary search and Dijkstra methods work.

        3353 ms, faster than 76.10%
        """
        N = len(grid)
        manhattan = [[1000000000] * N for _ in range(N)]
        # find all the thieves, and put them in the queue
        queue = []
        for i in range(N):
            for j in range(N):
                if grid[i][j]:
                    queue.append((i, j, 0))
                    manhattan[i][j] = 0
        # fill out manhattan by finding the min Manhattan distance of each cell
        while queue:
            tmp = []
            for i, j, d in queue:
                for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and d + 1 < manhattan[ni][nj]:
                        manhattan[ni][nj] = d + 1
                        tmp.append((ni, nj, d + 1))
            queue = tmp
        # Dijstra
        queue = [(-manhattan[0][0], 0, 0)]
        safeness = [[0] * N for _ in range(N)]
        safeness[0][0] = manhattan[0][0]
        while queue:
            while queue and queue[0][0] != safeness[queue[0][1]][queue[0][2]]:
                heapq.heappop(queue)
            s, i, j = heapq.heappop(queue)
            if i == N - 1 and j == N - 1:
                return -s
            for di, dj in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N:
                    cur = min(-s, manhattan[ni][nj])
                    if cur > safeness[ni][nj]:
                        safeness[ni][nj] = cur
                        heapq.heappush(queue, (-cur, ni, nj))
        return 0  # will not hit this line


sol = Solution()


tests = [
    # ([[1,0,0],[0,0,0],[0,0,1]], 0),
    # ([[0, 0, 1], [0, 0, 0], [0, 0, 0]], 2),
    # ([[0, 1, 1], [0, 1, 1], [1, 1, 1]], 0),
    ([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 2),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maximumSafenessFactor(grid)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
