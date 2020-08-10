#! /usr/bin/env python3
from typing import List, Tuple
from random import choice
from bisect import bisect_left

"""08/23/2019

Solution1:
Most naive solution. Expected to time out.
And as expected. It timed out. But at least we have a correct solution to test
against.


Solution2:
This solution finally passed OJ. The idea is that for each row of water, the
land in each column that result in min distance is the same for the entire row.
Thus, we only need to find out the min_lands for each row of water, and check
each water in the row against min_lands to retrieve the max min distance of the
row. We can use binary search to find the min_lands for each col, because the
land's row index must be the closest to the index of the row of water.

This solution clocked in at 2704 ms, not even on the map. The fastest is below
500 ms.

Solution3:
BFS for the win. I read the discussion and realized that BFS is such a powerful
method for this problem. The idea is to expand from each land, and count the
min step to reach each water. I had vaguely a similar idea to eliminate water
of the min distance to each land, but I was thinking about extending always
from the land, which makes things very complicated. The essence for BFS is that
we are not extending from the original land. Each time we expand to water, the
water becomes the new land and we expand from this new land. Since the first
step of expansion is only four steps, this is easy to do for each new land. We
can expand simultaneously for all lands of the same number of steps away from
any land, and then push their next expansion to a queue. This marvelous solution
clocked in at 488 ms, 97%. Truly amazing.
"""


class Solution1:
    def maxDistance(self, grid: List[List[int]]) -> int:
        lands: List[Tuple[int, int]] = []
        waters: List[Tuple[int, int]] = []
        for i, r in enumerate(grid):
            for j, c in enumerate(r):
                if c == 1:
                    lands.append((i, j))
                else:
                    waters.append((i, j))
        if not lands or not waters:
            return -1
        max_distance = 0
        for water in waters:
            min_dis = min(
                abs(water[0] - land[0]) + abs(water[1] - land[1])
                for land in lands
            )
            max_distance = max(max_distance, min_dis)
        return max_distance


class Solution2:
    def maxDistance(self, grid: List[List[int]]) -> int:
        size = len(grid)
        # each element of lands represents a column, in which the row index for each land is stored
        lands: List[List[int]] = [[] for _ in range(size)]
        # each element of waters represents a row, in which the col index for each water is stored
        waters: List[List[int]] = [[] for _ in range(size)]
        for j in range(size):
            for i in range(size):
                if grid[i][j]:
                    lands[j].append(i)
                else:
                    waters[i].append(j)
        max_dis = -1
        for r, water in enumerate(waters):
            min_lands = []
            for c in range(size):
                if lands[c]:
                    m = bisect_left(lands[c], r)
                    if m < len(lands[c]) and lands[c][m] == r:
                        land = (r, c)
                    elif m == len(lands[c]):
                        land = (lands[c][m - 1], c)
                    elif m == 0:
                        land = (lands[c][m], c)
                    else:
                        if lands[c][m] - r <= r - lands[c][m - 1]:
                            land = (lands[c][m], c)
                        else:
                            land = (lands[c][m - 1], c)
                    min_lands.append(land)
            if not min_lands:  # no land in the grid
                return -1
            for c in water:
                min_dis = min(
                    abs(r - land[0]) + abs(c - land[1]) for land in min_lands
                )
                max_dis = max(max_dis, min_dis)
        return max_dis


class Solution3:
    def maxDistance(self, grid: List[List[int]]) -> int:
        bfs: List[Tuple[int, int]] = []
        size = len(grid)
        for i in range(size):
            for j in range(size):
                if grid[i][j]:
                    bfs.append((i, j))
        for i, j in bfs:  # bfs, expand from land or newly conquered land
            if j + 1 < size and grid[i][j + 1] == 0 and grid[i][j + 1] != 1:
                grid[i][j + 1] = grid[i][j] + 1
                bfs.append((i, j + 1))
            if i + 1 < size and grid[i + 1][j] == 0 and grid[i + 1][j] != 1:
                grid[i + 1][j] = grid[i][j] + 1
                bfs.append((i + 1, j))
            if j - 1 >= 0 and grid[i][j - 1] == 0 and grid[i][j - 1] != 1:
                grid[i][j - 1] = grid[i][j] + 1
                bfs.append((i, j - 1))
            if i - 1 >= 0 and grid[i - 1][j] == 0 and grid[i - 1][j] != 1:
                grid[i - 1][j] = grid[i][j] + 1
                bfs.append((i - 1, j))
        res = max(max(row) for row in grid)
        return res - 1 if res >= 2 else -1


def gen_grid(length: int) -> List[List[int]]:
    return [[choice([0, 1]) for _ in range(length)] for _ in range(length)]


def print_grid(grid: List[List[int]]) -> None:
    for r in grid:
        print(r)


sol1 = Solution1()
sol2 = Solution2()
# grid = [[0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 0, 0], [0, 1, 1, 1]]
# print_grid(grid)
# print(sol.maxDistance(grid))
for t in range(100):
    grid = gen_grid(50)
    res2 = sol2.maxDistance(grid)
    res1 = sol1.maxDistance(grid)
    if res2 != res1:
        print_grid(grid)
        print(f"res2 = {res2}, res1 = {res1}")
