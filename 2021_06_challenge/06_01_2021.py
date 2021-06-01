# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """LeetCode 695

        Whenever we reach a part of an island, we run a DFS to traverse
        through all the cells inside the island. This allows us to compute the
        total area of this island. Furthermore, each cell visited will be
        converted to -1, such that we will not visit it again later.

        O(MN), where M is the number of rows in grid and N the number of columns

        176 ms, 11% ranking.
        """
        m, n = len(grid), len(grid[0])

        def dfs(i, j) -> int:
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] <= 0:
                return 0
            grid[i][j] = -1
            return 1 + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1)

        return max(dfs(i, j) for i in range(m) for j in range(n))


sol = Solution()
tests = [
    ([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]], 6),
    ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.maxAreaOfIsland(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
