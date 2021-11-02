# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """The same algorithm as I did more than a year ago. Brute force it. We
        count the required number of steps to reach the destination with all
        open cells traversed. Then we traverse the entire grid and see how many
        paths that reache the destination have the same number of steps as
        required.

        This is slow, but since the grid size is 20x20 at most, it works.

        O(3^(MN)), 68 ms, 62% ranking.

        UPDATE: the previous version only registers 62% ranking, which is due
        to the use of modulo. We can avoid that by changing when grid cell is
        marked as visited. Instead of marking it before visiting it, we now
        visit it first, and then mark it. This allows us to mark the visited
        with -2 without having to worry about changing the value of the end
        point as well. We simply examine the endpoint first. If the endpoint has
        not been reached, then we mark the cell as visited.
        """
        M, N = len(grid), len(grid[0])
        total_steps = 1
        si, sj = 0, 0
        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    si, sj = i, j
                elif grid[i][j] == 0:
                    total_steps += 1
        self.res = 0

        def dfs(i: int, j: int, steps: int) -> None:
            if grid[i][j] == 2:
                self.res += (steps == total_steps)
            elif steps < total_steps:
                grid[i][j] = -2  # mark as visited
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] >= 0:
                        dfs(ni, nj, steps + 1)
                grid[i][j] = 0

        dfs(si, sj, 0)
        return self.res


sol = Solution()
tests = [
    ([[1,0,0,0],[0,0,0,0],[0,0,2,-1]], 2),
    ([[1,0,0,0],[0,0,0,0],[0,0,0,2]], 4),
    ([[0,1],[2,0]], 0),
    ([[0,1],[0,2]], 1),
    ([[1,0],[2,0]], 1),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.uniquePathsIII(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
