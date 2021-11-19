# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """DFS. Since we only need to return the total number of islands, the
        problem is actually simplied.

        O(MN), 336 ms, 49% ranking.
        """
        m, n = len(grid), len(grid[0])

        def dfs(i: int, j: int) -> int:
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1':
                grid[i][j] = '0'
                # courtesy of Mr. Pochmann
                # https://leetcode.com/problems/number-of-islands/discuss/56349/7-lines-Python-~14-lines-Java
                list(map(dfs, [i + 1, i - 1, i, i], [j, j, j + 1, j - 1]))
                return 1
            return 0

        return sum(dfs(i, j) for i in range(m) for j in range(n))


sol = Solution()
tests = [
    (
        [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ],
        1,
    ),
    (
        [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ],
        3,
    )
]

for i, (grid, ans) in enumerate(tests):
    res = sol.numIslands(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
