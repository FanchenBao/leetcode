# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        """We had the correct idea from yesterday (2022-05-30). In fact, our
        idea was exactly the same as the hints. But our initial implementation
        was not optimal. We tried to create a set of coordinates of fire at
        after i minutes of wait for each minute. This led to memory limit
        exceed. We then tried to only record the front line of fire and iterate
        through all the fires over the waited minutes, that caused TLE.

        Eventually, I was able to modify grid and use number to record when
        a fire has reached a cell. e.g. grid[i][j] = 3, that means after
        waiting for 3 minutes, grid[i][j] has turned into fire. This set up
        is both memory and time efficient.

        The rest is just two rounds of BFS, one for fire and the other for
        finding the path from source to dest. And we need to use binary search
        to approach the max amount of waiting time.

        O(MNlog(MN)). 585 ms, faster than 87.37%
        """
        M, N = len(grid), len(grid[0])
        max_fire_tick = 0
        queue = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 0:
                    grid[i][j] = math.inf
                elif grid[i][j] == 1:
                    grid[i][j] = 0
                    queue.append((i, j))
                else:
                    grid[i][j] = -1
        while queue:
            temp = []
            for i, j in queue:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] == math.inf:
                        temp.append((ni, nj))
                        grid[ni][nj] = grid[i][j] + 1
                        max_fire_tick = max(max_fire_tick, grid[ni][nj])
            queue = temp
        # binary search
        # Set lo and hi to some negative value and very large value. This
        # guarantees that if it is not possible to reach the dest, lo will
        # always end up negative. And if it is always possible to reach, then
        # hi will always not be smaller than max_fire_tick
        lo, hi = -2, M * N
        while lo < hi:
            mid = (lo + hi) // 2
            queue = [(0, 0)]
            visited = set([(0, 0)])
            tick = mid + 1
            while queue:
                temp = []
                for i, j in queue:
                    for di, dj in [(0, 1), (1, 0), (-1 ,0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] >= 0 and (ni, nj) not in visited:
                            if max_fire_tick == 0 or tick < grid[ni][nj] or (tick == grid[ni][nj] and ni == M - 1 and nj == N - 1):
                                temp.append((ni, nj))
                                visited.add((ni, nj))
                queue = temp
                tick += 1
                if (M - 1, N - 1) in visited:
                    break
            else:
                hi = mid
                continue
            lo = mid + 1
        return -1 if lo < 0 else lo - 1 if lo < max_fire_tick else 10**9


sol = Solution()
tests = [
    ([[0,2,0,0,0,0,0],[0,0,0,2,2,1,0],[0,2,0,0,1,2,0],[0,0,2,2,2,0,2],[0,0,0,0,0,0,0]], 3),
    ([[0,0,0,0],[0,1,2,0],[0,2,0,0]], -1),
    ([[0,0,0],[2,2,0],[1,2,0]], 1000000000),
    ([[0,2,0,0,1],[0,2,0,2,2],[0,2,0,0,0],[0,0,2,2,0],[0,0,0,0,0]], 0),
    ([[0,0],[0,0]], 1000000000),
    ([[0,0,0,0,2,0,2,2,0,2,0,2,2,0,0,0,2,2,0,2,0,2,0,2,0,0,0,0,0,2,2,0,2,0,0,0,2,0,2,0,0,0,0,0,0,0,2,2,0,2],[2,0,2,2,2,0,2,0,0,0,0,0,2,0,2,2,2,2,0,0,0,0,0,0,0,2,2,2,2,2,0,0,2,0,2,2,2,0,2,0,2,0,2,2,2,2,2,2,0,0],[0,0,0,0,0,0,0,0,2,0,2,0,0,0,0,0,0,2,0,2,2,2,2,2,2,2,0,0,0,2,2,0,0,0,0,0,0,0,0,0,2,2,2,2,0,2,0,2,2,0],[0,2,0,2,0,2,0,2,2,2,2,2,0,2,2,2,2,2,0,2,2,0,2,0,0,2,2,2,0,0,0,0,2,2,0,2,2,0,2,0,0,0,0,2,0,2,0,0,0,0],[0,2,0,2,0,2,0,0,0,2,2,0,0,0,2,0,2,2,0,0,0,0,0,0,2,2,0,2,0,2,2,2,2,2,0,2,2,0,2,0,2,2,0,2,0,0,0,2,2,2],[0,2,0,2,0,2,0,2,0,0,2,0,2,0,0,0,2,2,0,2,2,2,2,0,2,2,0,2,0,0,0,2,0,2,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,0],[0,2,2,2,2,2,2,2,2,0,2,0,2,0,2,2,2,2,0,0,0,2,2,0,0,0,0,0,0,2,2,2,0,0,2,0,2,2,0,2,2,0,2,0,0,0,2,2,0,0],[0,0,0,0,0,2,2,2,0,0,2,0,2,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,0,0,2,2,0,2,2,0,2,0,0,0,0,0,0,0,2,2,2,0,0,2],[0,2,0,2,0,0,0,2,2,2,2,0,2,0,2,0,2,2,2,2,0,0,0,0,2,2,0,2,2,2,2,0,0,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,2,2],[0,2,0,2,0,2,0,2,2,2,2,0,2,0,2,0,0,0,0,2,0,2,2,2,2,0,0,0,2,0,2,0,2,2,2,2,0,2,2,2,2,2,2,2,2,2,2,2,2,2],[0,2,2,2,0,2,0,0,0,0,2,2,2,0,2,2,0,2,0,2,0,0,0,0,0,0,2,0,0,0,0,0,0,0,2,2,0,2,0,2,0,2,0,2,2,1,2,2,0,2],[0,2,2,0,0,2,0,2,2,0,2,2,0,0,2,2,0,2,0,0,0,2,2,2,2,0,2,2,0,2,2,0,2,2,2,2,0,0,0,0,0,0,0,0,2,0,0,0,0,0],[0,2,2,0,2,2,0,2,2,0,0,2,0,2,2,0,0,2,2,2,0,0,0,0,2,2,2,2,0,2,2,0,0,0,0,2,0,2,2,2,0,2,2,0,0,0,2,2,2,2],[0,2,0,0,0,2,0,2,0,0,2,2,2,2,2,2,0,2,2,0,0,2,2,0,0,0,0,2,0,0,2,0,2,0,2,2,2,2,0,0,0,2,2,0,2,0,0,0,0,0],[2,2,0,2,2,2,0,2,2,0,2,0,2,0,0,0,0,0,2,2,0,0,2,0,2,0,2,2,0,2,2,2,2,0,0,2,2,2,0,2,0,2,2,0,2,0,2,2,2,0],[2,2,0,0,2,2,2,2,2,0,0,0,2,2,0,2,0,2,2,2,2,0,2,0,2,0,2,2,0,0,2,2,2,2,0,0,0,2,2,2,0,2,2,0,2,0,0,2,2,0],[0,0,0,2,2,0,2,2,0,0,2,2,2,2,0,2,2,2,0,0,2,0,2,2,2,2,2,2,2,0,0,0,0,2,0,2,2,2,2,2,2,2,0,0,2,0,2,2,2,2],[0,2,0,0,0,0,0,2,2,0,0,2,2,0,0,0,2,2,2,0,0,0,0,0,0,2,2,2,2,0,2,2,2,2,2,2,2,0,0,0,0,2,2,0,2,0,0,0,0,0],[2,2,2,0,2,0,2,2,2,2,0,0,2,2,2,0,0,2,2,0,2,0,2,2,0,0,2,2,0,0,0,0,0,0,2,0,0,0,2,2,2,2,2,0,2,2,0,2,2,2],[0,0,0,0,2,0,2,0,0,2,2,0,0,0,2,2,0,0,2,0,2,0,0,2,2,0,0,2,2,0,2,0,2,0,0,0,2,0,0,0,0,0,2,0,0,2,0,0,0,0],[2,2,0,2,2,0,0,0,2,2,2,2,0,2,2,0,0,2,2,2,2,0,2,2,0,0,2,2,0,0,2,0,2,0,2,2,2,0,2,0,2,2,2,2,0,2,2,2,2,0],[0,0,0,2,0,0,2,0,0,0,0,2,0,0,2,2,0,2,0,0,0,0,2,2,0,2,2,2,2,0,2,0,2,0,0,0,2,0,2,0,0,0,0,2,0,0,2,2,2,2],[2,0,2,2,2,0,2,2,0,2,2,2,2,2,2,2,0,2,2,0,2,0,0,2,2,2,0,2,0,0,2,0,2,0,2,0,2,2,2,2,0,2,2,2,2,0,0,0,0,2],[0,0,2,2,0,0,2,2,0,0,0,0,0,0,0,2,2,2,2,0,2,2,0,0,0,0,0,2,2,0,2,0,2,0,2,0,2,2,2,0,0,0,0,2,2,2,2,2,0,0],[2,0,2,2,2,2,2,2,0,2,2,2,2,2,0,2,2,0,0,0,2,2,0,2,2,2,2,2,2,2,2,0,2,0,2,0,0,0,2,2,0,2,0,0,0,2,2,2,2,2],[2,0,2,0,0,0,0,0,0,0,0,0,2,2,2,2,2,0,2,0,2,2,0,0,0,0,0,0,0,0,2,2,2,0,2,0,2,2,2,0,0,2,0,2,0,0,0,0,0,0],[0,0,2,2,2,0,2,2,0,2,0,2,2,0,0,0,0,0,2,0,0,2,2,2,0,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2,0,2,2,2,2,0,2,2,2,2],[2,0,2,0,0,0,2,0,0,2,2,2,2,2,0,2,0,2,2,2,2,2,2,0,0,0,2,2,2,0,0,0,2,2,2,2,2,0,2,2,0,0,0,0,2,0,0,0,2,2],[2,0,2,2,0,2,2,2,0,0,0,0,0,2,0,2,0,0,0,2,2,0,0,0,2,0,0,0,0,0,2,2,2,0,0,2,0,0,0,2,2,0,2,2,2,0,2,0,0,0],[0,0,2,2,0,2,0,2,2,0,2,2,0,2,2,2,0,2,0,2,0,0,2,0,2,0,2,0,2,0,0,0,0,0,2,2,0,2,2,2,0,0,0,0,2,2,2,0,2,0],[0,2,2,2,2,2,0,0,0,0,0,2,0,0,0,2,0,2,0,2,0,2,2,2,2,0,2,2,2,0,2,0,2,0,2,2,0,2,2,2,2,0,2,2,2,2,2,2,2,2],[0,2,0,0,2,2,2,2,0,2,2,2,0,2,0,2,0,2,2,2,0,2,2,0,0,0,0,0,2,0,2,0,2,0,0,0,0,0,0,2,2,0,0,0,2,0,0,0,0,0],[2,2,2,0,0,0,0,0,0,0,0,2,2,2,0,2,2,2,2,2,0,2,2,0,2,0,2,0,2,2,2,2,2,0,2,0,2,0,2,2,2,0,2,0,0,0,2,0,2,0],[2,2,0,0,2,0,2,2,2,0,2,2,0,0,0,0,0,0,0,2,0,2,2,0,2,0,2,0,0,0,2,2,2,0,2,2,2,0,2,0,2,2,2,2,0,2,2,2,2,0],[0,0,0,2,2,0,2,2,0,0,0,2,0,2,2,2,0,2,0,2,2,2,2,2,2,0,2,0,2,0,0,0,2,0,0,0,2,0,0,0,0,2,0,2,0,0,2,2,2,2],[2,2,2,2,2,0,2,2,2,0,2,2,2,2,0,0,0,2,0,0,0,0,2,2,0,0,2,0,2,2,0,2,2,0,2,0,2,2,0,2,2,2,0,2,2,0,0,0,0,0],[0,0,0,0,0,0,0,2,2,0,0,0,2,2,0,2,0,2,2,0,2,2,2,0,0,2,2,0,2,0,0,2,2,0,2,2,2,0,0,0,0,0,0,2,2,0,2,2,2,2],[2,2,2,2,0,2,0,2,2,2,2,2,2,2,0,2,0,2,2,0,2,0,0,0,2,2,2,0,2,2,0,2,2,0,0,2,2,0,2,2,0,2,0,2,2,0,0,0,2,0],[2,2,1,0,0,2,0,0,0,0,0,2,2,0,0,2,0,2,2,0,2,2,2,0,0,0,2,2,2,0,0,2,2,0,2,2,2,0,0,2,0,2,2,2,0,0,2,0,0,0],[0,2,2,2,0,2,2,2,2,0,2,2,0,0,2,2,0,2,2,0,2,2,0,0,2,2,2,2,2,0,2,2,2,0,0,0,2,2,0,2,0,0,0,2,0,2,2,0,2,0],[0,0,0,0,0,0,0,2,2,0,0,2,2,0,2,2,0,2,2,0,0,2,0,2,2,2,0,0,0,0,2,2,0,0,2,0,0,2,0,2,2,0,2,2,0,0,2,0,2,0],[2,0,2,0,2,2,2,2,2,0,2,2,0,0,2,2,2,2,2,2,0,2,0,2,2,0,0,2,0,2,2,2,0,2,2,0,2,2,0,0,2,0,0,2,2,0,2,0,2,0],[0,0,2,0,0,0,0,0,2,2,2,2,2,0,0,0,0,0,2,2,0,2,0,0,2,2,0,2,0,2,2,0,0,2,2,0,2,2,0,2,2,2,0,0,2,2,2,0,2,0],[2,0,2,0,2,0,2,0,2,2,0,0,0,0,2,0,2,0,2,0,0,2,0,2,2,2,0,2,0,2,2,2,0,0,2,0,0,2,2,2,0,2,2,0,0,2,2,0,2,0],[0,0,2,0,2,0,2,0,0,2,2,0,2,0,2,0,2,2,2,2,0,2,2,2,0,0,0,2,0,2,0,0,0,2,2,2,0,0,0,0,0,0,2,0,2,2,2,0,2,0],[0,2,2,0,2,0,2,0,2,2,0,0,2,2,2,0,0,0,2,2,0,0,0,2,2,0,2,2,0,2,2,0,2,2,0,2,2,0,2,2,0,2,2,0,0,0,2,0,2,0],[0,2,0,0,2,0,2,0,0,2,2,0,2,2,0,0,2,2,2,2,2,0,2,2,2,0,2,2,2,2,0,0,0,0,0,0,2,0,2,0,0,0,2,2,0,2,2,2,2,0],[0,2,2,0,2,2,2,2,2,2,0,0,2,0,0,2,2,2,2,0,0,0,0,0,2,0,0,2,2,2,0,2,0,2,0,2,2,2,2,0,2,0,2,2,0,0,0,0,2,2],[0,2,0,0,2,2,0,0,0,0,0,2,2,2,0,0,0,0,2,2,0,2,2,2,2,2,2,2,0,0,0,2,0,2,2,2,0,2,2,0,2,0,0,2,2,0,2,0,0,2],[2,2,2,0,2,2,2,2,0,2,0,0,0,2,2,2,0,2,2,0,0,0,0,2,0,2,2,2,0,2,0,2,0,2,2,2,0,0,2,2,2,0,2,2,0,0,2,2,0,0],[0,0,0,0,2,0,0,0,0,2,2,2,2,2,2,2,0,0,2,2,0,2,0,0,0,0,0,2,0,2,0,2,0,0,0,2,2,0,2,2,2,2,2,2,2,0,0,2,2,0],[2,0,2,0,2,0,2,2,0,0,2,0,2,2,0,0,0,2,2,2,0,2,0,2,0,2,2,2,0,2,2,2,0,2,0,0,2,0,2,0,2,2,2,0,0,0,2,2,2,0],[2,2,2,0,2,2,2,0,0,2,2,0,0,0,0,2,2,2,0,0,0,2,2,2,0,0,0,2,0,2,0,0,0,2,2,0,0,0,0,0,0,0,2,2,0,2,2,2,0,0],[0,2,0,0,2,0,0,0,2,2,2,2,0,2,0,0,0,2,0,2,0,0,2,2,2,2,2,2,2,2,0,2,0,0,2,0,2,0,2,2,2,2,2,0,0,0,0,2,2,0],[0,0,0,2,2,0,2,0,0,0,0,2,2,2,2,0,2,2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,0,2,2,0,2,0,0,0,0,2,2,2,0,2,0,2,2,0],[2,0,2,2,0,0,2,2,0,2,0,2,0,0,0,0,0,2,2,0,0,0,2,0,2,0,2,0,2,2,0,0,0,0,2,0,2,2,0,2,0,0,2,2,0,2,0,0,2,0]], 2),
    ([[0,2],[2,0]], -1),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maximumMinutes(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
