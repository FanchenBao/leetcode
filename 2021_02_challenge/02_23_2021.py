# from pudb import set_trace; set_trace()
from typing import List, Tuple
from bisect import bisect_right
import math


class Solution1:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """LeetCode 240

        This is a very straightforward solution. We go row by row, and
        run a binary search. This is apparently not the best solution, because
        we only used one condition, that is each row is in ascending order.
        We did not use the other condition.

        O(mlog(n)), 148 ms, 99% ranking.
        """
        for row in matrix:
            idx = bisect_right(row, target)
            if row[idx - 1] == target:
                return True
        return False


class Solution2:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Another solution of mine, in an attempt to get a O(m + n) solution.
        However, this one feels very convoluted. I am trying to go row first to
        eliminate rows that are out of range wrt target. Then go columns to
        eliminate columns that are out of range. Repeat this process until we
        either find the target or realize that the target does not exist.

        I am not sure of the run time. Could be O(m + n), but I don't know.

        168 ms, 52% ranking.
        """

        def check(left: int, right: int, top: int, bottom: int) -> Tuple:
            ntop, nbottom = math.inf, -1
            for i in range(top, bottom + 1):
                small, big = matrix[i][left], matrix[i][right]
                if small > target:
                    break
                elif big < target:
                    continue
                elif small == target:  # handle situation of repeated numbers
                    return left, left, i, i
                else:
                    ntop, nbottom = min(ntop, i), i
            nleft, nright = math.inf, -1
            if nbottom != -1:
                for j in range(left, right + 1):
                    small, big = matrix[ntop][j], matrix[nbottom][j]
                    if small > target:
                        break
                    elif big < target:
                        continue
                    elif small == target:  # handle situation of repeated numbers
                        return j, j, ntop, ntop
                    else:
                        nleft, nright = min(nleft, j), j
            return nleft, nright, ntop, nbottom

        top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while left != right or top != bottom:
            left, right, top, bottom = check(left, right, top, bottom)
            if right == -1 or bottom == -1:  # not found
                return False
        return matrix[top][left] == target


class Solution3:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """The correct solution. Very smart. We start from top right corner, and
        zigzag towards the target.

        Inspired by:
        https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66140/My-concise-O(m%2Bn)-Java-solution

        O(m + n)
        """
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False


sol = Solution3()
tests = [
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5, True),
    ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 20, False),
    ([[-5]], -2, False),
    ([[1, 1]], 1, True),
    ([[2, 2], [2, 2]], 2, True),
]

for i, (matrix, target, ans) in enumerate(tests):
    res = sol.searchMatrix(matrix, target)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
