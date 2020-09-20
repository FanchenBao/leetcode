# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        """Classic backtrack problem. Finished with 97% percentile."""
        obstacles = 0
        lim_i, lim_j = len(grid), len(grid[0])
        # find number of squares to visit
        for row in grid:
            obstacles += row.count(-1)
        n_squares = lim_i * lim_j - obstacles
        # find start and end point
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == 1:
                    start = (i, j)
                elif val == 2:
                    end = (i, j)
        # use backtrack to search the map
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # S, N, E, W
        res = [0]

        def backtrack(cur_path) -> None:
            if cur_path[-1] == end:
                res[0] += 1 if len(cur_path) == n_squares else 0
            else:
                ci, cj = cur_path[-1]
                for di, dj in dirs:
                    ni, nj = ci + di, cj + dj
                    if 0 <= ni < lim_i and 0 <= nj < lim_j and grid[ni][nj] in {0, 2}:
                        cur_path.append((ni, nj))
                        grid[ni][nj] = -2  # visited
                        backtrack(cur_path)
                        grid[ni][nj] = 0
                        cur_path.pop()
        
        backtrack([start])
        return res[0]


sol = Solution()
tests = [
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]], 2),
    ([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]], 4),
    ([[0, 1], [2, 0]], 0),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.uniquePathsIII(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
