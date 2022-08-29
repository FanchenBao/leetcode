# from pudb import set_trace; set_trace()
from typing import List


class Solution1:
    def numIslands(self, grid: List[List[str]]) -> int:
        """LeetCode 200

        DFS to mark all the cells in an island once one cell of the island is
        visited. This way, we can count island each time a '1' is encountered.

        O(MN), 499 ms, faster than 48.07%
        """
        M, N = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> None:
            if 0 <= i < M and 0 <= j < N and grid[i][j] == '1':
                grid[i][j] = '*'
                for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    ni, nj = i + di, j + dj
                    dfs(ni, nj)

        res = 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Better implementation. No need to traverse twice.

        468 ms, faster than 56.16%
        """
        M, N = len(grid), len(grid[0])
        
        def dfs(i: int, j: int) -> int:
            if 0 <= i < M and 0 <= j < N and grid[i][j] == '1':
                grid[i][j] = '*'
                for di, dj in ((0, 1), (0, -1), (-1, 0), (1, 0)):
                    ni, nj = i + di, j + dj
                    dfs(ni, nj)
                return 1
            return 0

        return sum(dfs(i, j) for i in range(M) for j in range(N))


sol = Solution2()
tests = [
    ([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
], 1),
    ([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
], 3)
]

for i, (grid, ans) in enumerate(tests):
    res = sol.numIslands(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
