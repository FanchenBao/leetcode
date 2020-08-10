#! /usr/bin/env python3
from typing import List
from random import randint

"""07/28/2019

This is from last week's contest. I was only able to come up with the naive
brute force method (solution1), which unsurprisingly timed out. I had to check
the discussion and boy oh boy did my mind get blown away.

This is essentially a Manhatten Distance problem. The two arrays are x and y
coordinates, and we are tasked to find the two points that are furthest apart
in terms of Manhatten Distance.

There are two ways to think about this problem. The easier way is to consider
four corners of the grid on which all the points reside. Have all points go to
each corner. Since when they are heading to the corner, all points are going in
the same direction. Then we can compute the distance between each pair of points
by substracting their Manhatten distance to the corner. Since we only need the
max distance between the points, we only need to find the max distance to the
corner and min distance to the corner. Their difference is the max distance
between the points going in the direction of that particular corner. We repeat
the same procedure for the other three points to cover all possible directions.
And the max distance among the four is the answer. Solution2 reflects this way
of thinking.

The other way of thinking is to use only one anchor point, typically (0, 0), and
have all points go to (0, 0) in four directions
[1, 1] = going left and down
[1, -1] = going left and up
[-1, -1] = going right and up
[-1, 1] = going right and down
We compute the max distance between any two points going in each direction, and
take the max of the four directions as our final outcome. Solution3 reflects
this way of thinking.

"""


class Solution1:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        maxVal: int = abs(arr1[0] - arr1[1]) + abs(arr2[0] - arr2[1]) + 1
        for k in range(2, len(arr1)):
            submax = 0
            for m in range(k):
                temp = (
                    abs(arr1[m] - arr1[k])
                    + abs(arr2[m] - arr2[k])
                    + abs(m - k)
                )
                submax = max(submax, temp)
            maxVal = max(maxVal, submax)
        return maxVal


class Solution2:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        corners = [
            [10 ** 6 + 1, 10 ** 6 + 1],
            [-10 ** 6 - 1, 10 ** 6 + 1],
            [-10 ** 6 - 1, -10 ** 6 - 1],
            [10 ** 6 + 1, -10 ** 6 - 1],
        ]
        maxVal = 0
        for corner in corners:
            distances = [
                abs(corner[0] - arr1[i]) + abs(corner[1] - arr2[i]) + i
                for i in range(len(arr1))
            ]
            maxVal = max(maxVal, max(distances) - min(distances))
        return maxVal


class Solution3:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        dirctions = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
        maxVal = 0
        for x, y in dirctions:
            distances = [
                x * arr1[i] + y * arr2[i] + i for i in range(len(arr1))
            ]
            maxVal = max(maxVal, max(distances) - min(distances))
        return maxVal


def test():
    for t in range(100):
        n = 100
        limit = 100
        arr1 = []
        arr2 = []
        for _ in range(n):
            arr1.append(randint(-limit, limit))
            arr2.append(randint(-limit, limit))

        sol1 = Solution1()
        sol2 = Solution2()
        sol1_res = sol1.maxAbsValExpr(arr1, arr2)
        sol2_res = sol2.maxAbsValExpr(arr1, arr2)
        if sol1_res != sol2_res:
            print(f"sol1 = {sol1_res}")
            print(f"sol2 = {sol2_res}")
            print(arr1)
            print(arr2)


test()
