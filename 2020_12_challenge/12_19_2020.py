# from pudb import set_trace; set_trace()
from typing import List
from functools import lru_cache
import math


class Solution1:
    def get_possible_vals_from_last_row(self, grid):
        """Get all possible values from any pair of elements in the last row"""
        col_n = len(grid[0])
        row_idx = len(grid) - 1
        vals = [[0] * col_n for _ in range(col_n)]
        for j in range(col_n):
            for k in range(col_n):
                vals[j][k] = grid[row_idx][j] + grid[row_idx][k] if j != k else grid[row_idx][j]
        return vals

    def search_max(self, next_vals, r1_j, r2_j, col_n):
        """Given the current position of the two robots at r1_j and r2_j, what
        is the max value they can achieve in the next round?

        Since we already know all the possible combinations of the two robots
        in the next round, we only need to search next_vals based on the
        possible locations the two robots can be (this is restricted by r1_j
        and r2_j) and return the max value. This max value is the max cherries
        the two robots can pick going from r1_j, r2_j to the next level.
        """
        if r1_j == 0:  # on left edge
            r1_range = [r1_j, r1_j + 1]
        elif r1_j == col_n - 1:  # on right edge
            r1_range = [r2_j - 1, r2_j]
        else:  # not on edge
            r1_range = [r1_j - 1, r1_j, r1_j + 1]
        # r2_j follows the same logic as r1_j
        if r2_j == 0:
            r2_range = [r2_j, r2_j + 1]
        elif r2_j == col_n - 1:
            r2_range = [r2_j - 1, r2_j]
        else:
            r2_range = [r2_j - 1, r2_j, r2_j + 1]
        max_val = 0  # find the max value within the range given above.
        for j in r1_range:
            for k in r2_range:
                max_val = max(max_val, next_vals[j][k])
        return max_val

    def cherryPickup(self, grid: List[List[int]]) -> int:
        """This is the first hard problem that I have solved all by myself in a
        long time. Very happy with the outcome.

        Use DP. We fill in all the possible values the two robots can take at
        each depth, going from the bottom up. At each current level, the
        positions of the two robots determine the range they can reach in the
        next level. Since we already compute all the possible cherries the two
        robots can pick in the next level, we only need to search all the
        possible locations in the next level to acquire the max number of
        cherries that can possibly be obtained given the current location.
        We repeat this process to fill up all the max values that can be
        obtained at the current level. Then we go upwards and repeat the entire
        thing until we reach the top.

        O(MN^2), 584 ms, 97% ranking.
        """
        col_n = len(grid[0])
        row_n = len(grid)
        next_vals = self.get_possible_vals_from_last_row(grid)  # bottom case
        for i in range(row_n - 2, -1, -1):
            cur_vals = [[0] * col_n for _ in range(col_n)]
            for j in range(0, min(i + 1, col_n)):  # robot 1 range
                for k in range(max(col_n - i - 1, 0), col_n):  # robot 2 range
                    max_val = self.search_max(next_vals, j, k, col_n)
                    cur_vals[j][k] = grid[i][j] + grid[i][k] + max_val if j != k else grid[i][k] + max_val
            next_vals = cur_vals
        return next_vals[0][col_n - 1]


class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Standard top down DP solution. Notice the good use of lru_cache to
        eliminate the need of building a memo.
        
        O(M*N^2), 780 ms, 91% ranking.
        """
        col_n = len(grid[0])
        row_n = len(grid)

        @lru_cache(None)
        def dfs(row_idx, r1_j, r2_j):
            """r1_j is the col index of robot1, r2_j the col index of robot2"""
            if r1_j < 0 or r1_j >= col_n or r2_j < 0 or r2_j >= col_n:
                return -math.inf
            cur_count = grid[row_idx][r1_j]
            if r1_j != r2_j:
                cur_count += grid[row_idx][r2_j]
            if row_idx < row_n - 1:
                cur_count += max(dfs(row_idx + 1, j1, j2) for j1 in [r1_j - 1, r1_j, r1_j + 1] for j2 in [r2_j - 1, r2_j, r2_j + 1])
            return cur_count

        return dfs(0, 0, col_n - 1)


class Solution3:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        """Standard bottom up solution.

        Note that we intentionally use two dp arrays: next_vals and cur_vals to
        reduce memory footprint.

        O(MN^2), 496 ms, 98% ranking. It is essentially the same algo as
        Solution1, yet with fewer function calls, this approach has the fastest
        runtime.
        """
        col_n = len(grid[0])
        row_n = len(grid)
        next_vals = [[0] * (col_n + 2) for _ in range(col_n + 2)]
        for row_idx in range(row_n - 1, -1, -1):
            cur_vals = [[0] * (col_n + 2) for _ in range(col_n + 2)]
            for r1_j in range(0, min(row_idx + 1, col_n)):
                for r2_j in range(max(col_n - row_idx - 1, 0), col_n):
                    cur_vals[r1_j][r2_j] = grid[row_idx][r1_j]
                    if r1_j != r2_j:
                        cur_vals[r1_j][r2_j] += grid[row_idx][r2_j]
                    cur_vals[r1_j][r2_j] += max(next_vals[j1][j2] for j1 in [r1_j - 1, r1_j, r1_j + 1] for j2 in [r2_j - 1, r2_j, r2_j + 1])
            next_vals = cur_vals
        return next_vals[0][col_n - 1]


sol = Solution3()
tests = [
    ([[3, 1, 1], [2, 5, 1], [1, 5, 5], [2, 1, 1]], 24),
    ([[1, 0, 0, 0, 0, 0, 1], [2, 0, 0, 0, 0, 3, 0], [2, 0, 9, 0, 0, 0, 0], [0, 3, 0, 5, 4, 0, 0], [1, 0, 2, 3, 0, 0, 6]], 28),
    ([[1, 0, 0, 3], [0, 0, 0, 3], [0, 0, 3, 3], [9, 0, 3, 3]], 22),
    ([[1, 1], [1, 1]], 4),
    ([[8, 8, 10, 9, 1, 7], [8, 8, 1, 8, 4, 7], [8, 6, 10, 3, 7, 7], [3, 0, 9, 3, 2, 7], [6, 8, 9, 4, 2, 5], [1, 1, 5, 8, 8, 1], [5, 6, 5, 2, 9, 9], [4, 4, 6, 2, 5, 4], [4, 4, 5, 3, 1, 6], [9, 2, 2, 1, 9, 3]], 146),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.cherryPickup(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
