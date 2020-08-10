#! /usr/bin/env python3
from typing import List, Tuple
from random import choice

"""08/01/2019

Solution1:
I brewed the idea for this solution for about two days, and spent about one hour
writing it down. So it is pretty impossible for me to come up with a solution
in the actual contest. I feel like writing a project instead of solving a
contest problem. Anyway, the thought process is like this: I will first find
a stretch ones of a row. Then I find the max square that exists if the top side
resides on this row, with the condition that the max square must be bigger than
the previous max square already found. In other words, at each search for max
square, the return value is always the largest max square. I repeat the process
for each stretch on each row, and eventually I will get the answer.

One trick to reduce run time: at each search, the starting side length
of a potential square must be bigger than the current max square. If this
condition cannot satisfy, e.g. not enough col or row to fit such side length,
we quit the search immediately.

I broke down the algorithm into several functions, which allowed me to concep-
tualize the algorithm more easily. breakpoint() was used to debug the code and
it is quite useful I have to admit.

The code eventually passed OJ with runtime at 380 ms, 50% mark.


Solution2:
This solution came from the discussion post. See this:
https://leetcode.com/problems/largest-1-bordered-square/discuss/345265/c%2B%2B-beats-100-(both-time-and-memory)-concise-with-algorithm-and-image

It is indeed a very smart solution. It creates two auxillary 2D array to record
the horizontal and vertical stretches of 1s for each row and col, respectively.
Then start from the bottom right corner, we check ver_grid[i][j] and hor_grid[i][j].
The min of the two is the largest square side length that cell i, j can be a
part of. Next, we check every single possible side length from min down to 1 by
examining the hor_grid value of upper right corner and ver_grid value of bottom
left corner. If these two values are both larger or equal to the side length,
then a square can be formed. We record the max for the square length.

This method, without any trick for optimization, clocked in at 216 ms, 75% mark.
"""


class Solution1:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        max_square: int = 0
        for ri, row in enumerate(grid):
            s: int = 0
            while True:
                stretch_start, stretch_end = self.find_next_stretch(row, s)
                if stretch_start >= 0:
                    max_square = self.find_max_square(
                        grid, ri, stretch_start, stretch_end, max_square
                    )
                else:
                    break
                s = stretch_start + 1
        return max_square ** 2

    def find_next_stretch(self, row: List[int], s: int) -> Tuple[int, int]:
        """ given a starting position s, find the next stretch of 1s in row.
            Return the next stretch's start and end values (inclusive)
        """
        first_one_encountered = False
        stretch_start, stretch_end = -1, -1
        for i in range(s, len(row)):
            if row[i] == 1:
                if not first_one_encountered:
                    stretch_start = i
                    first_one_encountered = True
                stretch_end = i
            elif first_one_encountered:
                return stretch_start, stretch_end
        return stretch_start, stretch_end

    def find_max_square(
        self,
        grid: List[List[int]],
        ri: int,
        stretch_start: int,
        stretch_end: int,
        max_square: int,
    ) -> int:
        """
            Given a stretch of 1s in a row from stretch_start to stretch_end
            (inclusive), find the max legitimate square that uses part of this
            stretch as its side. If no such max square can be found,
            return the max_square value that is passed in.
        """
        # stretch length <= max_square, no need to compute
        # remaining number of rows <= max_square, no need to compute
        # breakpoint()
        remain_rows = len(grid) - ri
        if (
            stretch_end - stretch_start + 1 <= max_square
            or remain_rows <= max_square
        ):
            return max_square
        for i in range(stretch_start, stretch_end + 1):
            if i + max_square > stretch_end:
                break
            for square_end in range(i + max_square, stretch_end + 1):
                side_len = square_end - i + 1
                if remain_rows < side_len:
                    break
                if self.check_square(grid, ri, i, square_end):
                    max_square = side_len
        return max_square

    def check_square(
        self,
        grid: List[List[int]],
        ri: int,
        square_start: int,
        square_end: int,
    ) -> bool:
        """
            Suppose grid[ri][square_start] to grid[ri][square_end] forms the
            top side of the square, see if this square actually exists by checking
            all the remaining sides. It is guaranteed that we will not go out
            of bound in grid in this validation
        """
        side_len = square_end - square_start + 1
        # check right and left side
        for i in range(ri, ri + side_len):
            if grid[i][square_end] * grid[i][square_start] == 0:
                return False
        # check bottom side
        for j in range(square_start, square_end + 1):
            if grid[ri + side_len - 1][j] != 1:
                return False
        return True


class Solution2:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        row_n = len(grid)
        col_n = len(grid[0])
        ver_grid = [[0] * col_n for _ in range(row_n)]
        hor_grid = [[0] * col_n for _ in range(row_n)]
        # populate hor_grid
        for i, row in enumerate(grid):
            count = 0
            for j, ele in enumerate(row):
                if ele == 1:
                    count += 1
                    hor_grid[i][j] = count
                else:
                    count = 0
        # populate ver_grid
        for j in range(col_n):
            count = 0
            for i in range(row_n):
                if grid[i][j] == 1:
                    count += 1
                    ver_grid[i][j] = count
                else:
                    count = 0
        max_square = 0
        # make each cell the bottom right corner of the square
        for i in range(row_n - 1, -1, -1):
            for j in range(col_n - 1, -1, -1):
                # check all possibilities for side length
                for curr_square in range(
                    min(ver_grid[i][j], hor_grid[i][j]), 0, -1
                ):
                    # check for possibility of forming square
                    if (
                        curr_square
                        and ver_grid[i][j - curr_square + 1] >= curr_square
                        and hor_grid[i - curr_square + 1][j] >= curr_square
                    ):
                        max_square = max(max_square, curr_square)
        return max_square ** 2


def gen_random_testcases(width: int, length: int) -> List[List[int]]:
    return [[choice((1, 0)) for _ in range(length)] for _ in range(width)]


# grid = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# grid = [[1, 1, 0, 0]]
t = 100
width, length = 100, 100
for _ in range(t):
    grid = gen_random_testcases(width, length)
    sol1 = Solution1()
    sol2 = Solution2()
    res1 = sol1.largest1BorderedSquare(grid)
    res2 = sol2.largest1BorderedSquare(grid)
    if res1 != res2:
        print(f"res1 = {res1}\nres2 = {res2}")
        print(grid)

# print(gen_random_testcases(100, 100))
