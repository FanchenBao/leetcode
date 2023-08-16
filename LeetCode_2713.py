# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        """Not tough in terms of implementation or intuition, but quite
        difficult to figure out all the edge cases without trial-and-error.

        The general idea is DP for each row and col, where rows[i] (or cols[j])
        records the max cell count, the value at the max cell count, and the
        max cell count at a cell value different from the max cell count value.
        for rows (or cols).

        We traverse the matrix from largest value to smallest, and for each val,
        we check its rows[i] and cols[j]. If the val is different from the val
        that results in the max count, the current max cell count is the
        previous max cell count + 1. Otherwise, the current max cell count is
        the previous max cell count other than the max cell count val + 1.

        After obtaining the current max cell count (go through rows and cols),
        we need to update rows and cols. Update only happens if the current max
        cell count is bigger than before, but pay attention that when the
        current val is the same as the previous val that leads to max cell count
        we do not update the max cell count at a cell value different from the
        max cell count value.

        O(MNlog(MN)), 1723 ms, faster than 97.73%
        """
        M, N = len(mat), len(mat[0])
        rows = [[0, math.inf, 0] for _ in range(M)]  # each element is [max_cell_count, cell_val_at_max_cell_count, max_cell_count_from_diff_cell_val]
        cols = [[0, math.inf, 0] for _ in range(N)]
        res = 0
        for v, i, j in sorted(((mat[i][j], i, j) for i in range(M) for j in range(N)), reverse=True):
            r = (rows[i][2] if rows[i][1] == v else rows[i][0]) + 1
            c = (cols[j][2] if cols[j][1] == v else cols[j][0]) + 1            
            cur = max(r, c)
            res = max(res, cur)
            # Update rows and cols
            if cur > rows[i][0]:
                if rows[i][1] != v:
                    rows[i][0], rows[i][2] = cur, rows[i][0]
                    rows[i][1] = v
                else:
                    rows[i][0] = cur
            if cur > cols[j][0]:
                if cols[j][1] != v:
                    cols[j][0], cols[j][2] = cur, cols[j][0]
                    cols[j][1] = v
                else:
                    cols[j][0] = cur
        return res


sol = Solution()
tests = [
    ([[3,1],[3,4]], 2),
    ([[1,1],[1,1]], 1),
    ([[3,1,6],[-9,5,7]], 4),
    ([[-2],[8],[-4],[-2],[-1],[7],[-2]], 5),
    ([[-1,-9,7,2,2],[5,-5,7,8,-5],[9,5,0,-2,2],[6,6,6,-9,2],[-3,7,4,-2,5],[-3,-6,9,6,2]], 7),
]

for i, (mat, ans) in enumerate(tests):
    res = sol.maxIncreasingCells(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
