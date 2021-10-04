# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """LeetCode 463

        Count the total number of lands and total number of redundant edges.
        Then the answer is 4 * land - redundant.

        O(MN), 682 ms, 34% ranking.
        """
        land, redundant = 0, 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    land += 1
                    for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                        if 0 <= ni < m and 0 <= nj < n and grid[ni][nj]:
                            redundant += 1
        return land * 4 - redundant


sol = Solution()
tests = [
    ([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]], 16),
    ([[1]], 4),
    ([[1, 0]], 4),
    
]

for i, (grid, ans) in enumerate(tests):
    res = sol.islandPerimeter(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
