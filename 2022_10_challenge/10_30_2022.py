# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import deque


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """LeetCode 1293

        If four directions are allowed, use BFS. Keep in mind that Dijkstra is
        BFS as well.

        I solve this problem with the help of the hint. Use BFS to go from top
        left to bottom right, and keep the number of remaining obstacles to
        remove in each BFS step. The first time we hit bottom right, that is
        the shortest path.

        O(MNK), 715 ms, faster than 46.44%
        """
        queue = [(0, 0, k)]
        visited = set([(0, 0, k)])
        M, N = len(grid), len(grid[0])
        res = 0
        while queue:
            tmp = []
            for i, j, r in queue:
                if i == M - 1 and j == N - 1:
                    return res
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N:
                        if grid[ni][nj] == 0 and (ni, nj, r) not in visited:
                            tmp.append((ni, nj, r))
                            visited.add((ni, nj, r))
                        elif grid[ni][nj] == 1 and r - 1 >= 0 and (ni, nj, r - 1) not in visited:
                            tmp.append((ni, nj, r - 1))
                            visited.add((ni, nj, r - 1))
            if tmp:
                res += 1
            queue = tmp
        return -1


sol = Solution()
tests = [
    ([[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], 1, 6),
    ([[0,1,1],[1,1,1],[1,0,0]], 1, -1),
]

for i, (grid, k, ans) in enumerate(tests):
    res = sol.shortestPath(grid, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
