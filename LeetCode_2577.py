# from pudb import set_trace; set_trace()
from typing import List
import math
import heapq


class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        """Dijkstra!

        Dijkstra is definitely the first trick. We record the min time needed to
        reach each cell. The next cell to visit must be the one with the current
        smallest time.

        Another trick is that if a cell's required time is not smaller than
        its previous one, then the min time to reach it is the required time
        plus one, if the required time has the same oddity as the previous time.
        Otherwise, we can reach it with the required time.

        The third trick is that as long as grid[0][1] and grid[1][0] are not
        both larger than 1, then we can always visit every single cell, because
        we can go back and forth between two cells in order to accumulate time
        to reach the requirement of the next cell.

        O(MNlog(MN)), 2185 ms, faster than 90.13%
        """
        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        M, N = len(grid), len(grid[0])
        dp = [[math.inf] * N for _ in range(M)]
        dp[0][0] = 0
        heap = [(0, 0, 0)]  # (time, i, j)
        while heap:
            while heap and dp[heap[0][1]][heap[0][2]] != heap[0][0]:
                heapq.heappop(heap)
            t, i, j = heapq.heappop(heap)
            if i == M - 1 and j == N - 1:
                return t
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N:
                    if grid[ni][nj] >= t:
                        pot_t = grid[ni][nj] + int((grid[ni][nj] + t) % 2 == 0)
                    else:
                        pot_t = t + 1
                    if pot_t < dp[ni][nj]:
                        dp[ni][nj] = pot_t
                        heapq.heappush(heap, (pot_t, ni, nj))
        return -1


sol = Solution()
tests = [
    ([[0,1,3,2],[5,1,2,5],[4,3,8,6]], 7),
    ([[0,2,4],[3,2,1],[1,0,4]], -1),
    ([[0,1,5,1],[100,1,100,1],[100,100,100,100000]], 100001),
    ([[0,1,1,1,1],[100,100,100,100,1],[1,1,1,1,1],[1,100,100,100,100],[1,1,1,1,1]], 16),
    ([[0,0,1],[0,1,2]], 3),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.minimumTime(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
