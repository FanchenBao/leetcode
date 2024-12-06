# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def countUnguarded(
        self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]
    ) -> int:
        """
        This is a simulation method from the official solution.

        We create a grid for simulation. First of all, we fill in all the
        guards and walls.

        Then for each guard, we go horizontal and fill as many cells as possible
        We stop if we hit another guard or a wall or a cell that has been
        horizontally guarded.

        Then we go vertical and follow the same method.

        O(MN), 310 ms, faster than 68.35%
        """
        EMPTY = 0
        GUARD = 1
        WALL = 2
        GUARD_ROW = 3
        GUARD_COL = 4
        grid = [[0] * n for _ in range(m)]
        for i, j in walls:
            grid[i][j] = WALL
        for i, j in guards:
            grid[i][j] = GUARD
            # horizontal
            for k in range(j + 1, n):
                if grid[i][k] == EMPTY or grid[i][k] == GUARD_COL:
                    grid[i][k] = GUARD_ROW
                else:
                    break
            for k in range(j - 1, -1, -1):
                if grid[i][k] == EMPTY or grid[i][k] == GUARD_COL:
                    grid[i][k] = GUARD_ROW
                else:
                    break
            # vertical
            for k in range(i + 1, m):
                if grid[k][j] == EMPTY or grid[k][j] == GUARD_ROW:
                    grid[k][j] = GUARD_COL
                else:
                    break
            for k in range(i - 1, -1, -1):
                if grid[k][j] == EMPTY or grid[k][j] == GUARD_ROW:
                    grid[k][j] = GUARD_COL
                else:
                    break
        return sum(e == 0 for row in grid for e in row)


sol = Solution()
tests = [
    (4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]], 7),
]

for i, (m, n, guards, walls, ans) in enumerate(tests):
    res = sol.countUnguarded(m, n, guards, walls)
    if res == ans:
        print(f"Test {i}: PASS")
    else:
        print(f"Test {i}; Fail. Ans: {ans}, Res: {res}")
