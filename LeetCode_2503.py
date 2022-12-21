# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        """Keep track of the edge nodes
        """
        qq = sorted([(q, i) for i, q in enumerate(queries)])
        M, N = len(grid), len(grid[0])
        visited = set()

        def dfs(i: int, j: int, q: int, next_starts) -> None:
            if grid[i][j] >= q:
                next_starts.add((i, j))
                return
            visited.add((i, j))
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in visited:
                    dfs(ni, nj, q, next_starts)

        queue = [[0, 0]]
        mix_res = []
        for q, _ in qq:
            tmp = set()
            for a, b in queue:
                dfs(a, b, q, tmp)
            queue = tmp
            mix_res.append(len(visited))
        res = [0] * len(queries)
        for (_, i), r in zip(qq, mix_res):
            res[i] = r
        return res


sol = Solution()
tests = [
    ([[1,2,3],[2,5,7],[3,5,1]], [5,6,2], [5, 8, 1]),
    ([[5,2,1],[1,1,2]], [3], [0]),
]

for i, (grid, queries, ans) in enumerate(tests):
    res = sol.maxPoints(grid, queries)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
