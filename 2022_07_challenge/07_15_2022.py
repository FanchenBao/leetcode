# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """LeetCode 695

        Only DFS when we hit an island.

        O(MN), 217 ms, faster than 51.20%
        """
        M, N = len(grid), len(grid[0])
        self.res = 0
        visited = set()

        def dfs(i: int, j: int) -> int:
            area = 1
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < M and 0 <= nj < N and (ni, nj) not in visited and grid[ni][nj]:
                    visited.add((ni, nj))
                    area += dfs(ni, nj)
            return area

        for i in range(M):
            for j in range(N):
                if grid[i][j]:
                    visited.add((i, j))
                    self.res = max(self.res, dfs(i, j))
        return self.res


class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """better implementation

        O(MN) but without the overhead of using a set.
        145 ms, faster than 90.60%
        """
        M, N = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if i < 0 or i >= M or j < 0 or j >= N or grid[i][j] <= 0:
                return 0
            grid[i][j] = -1
            return 1 + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j - 1)

        return max(dfs(i, j) for i in range(M) for j in range(N))


sol = Solution2()
tests = [
    ([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
    ([[0,0,0,0,0,0,0,0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maxAreaOfIsland(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
