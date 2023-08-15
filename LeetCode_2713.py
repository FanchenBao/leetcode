# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        M, N = len(mat), len(mat[0])
        row_max_cells = [[0, 0, 0, 0] for _ in range(M)]  # each element is [num_cells, cell_value, cell_value_visited, total_cell_visited]
        col_max_cells = [[0, 0, 0, 0] for _ in range(N)]
        res = 0
        for v, i, j in sorted(((mat[i][j], i, j) for i in range(M) for j in range(N)), reverse=True):
            if row_max_cells[i][1] == v:
                if row_max_cells[i][2] < row_max_cells[i][3]:
                    # v is not the only value visited on the current row
                    r = row_max_cells[i][0]
                else:
                    r = 1
                row_max_cells[i][2] += 1
            else:
                r = row_max_cells[i][0] + 1
                row_max_cells[i][1] = v
                row_max_cells[i][2] = 1
            row_max_cells[i][3] += 1

            if col_max_cells[j][1] == v:
                if col_max_cells[j][2] < col_max_cells[j][3]:
                    # v is not the only value visited on the current col
                    c = col_max_cells[j][0]
                else:
                    c = 1
                col_max_cells[j][2] += 1
            else:
                c = col_max_cells[j][0] + 1
                col_max_cells[j][1] = v
                col_max_cells[j][2] = 1
            col_max_cells[j][3] += 1


            cur_max_cells = max(r, c)
            res = max(res, cur_max_cells)
            row_max_cells[i][0] = col_max_cells[j][0] = cur_max_cells
        return res


sol = Solution()
tests = [
    ([[3,1],[3,4]], 2),
    ([[1,1],[1,1]], 1),
    ([[3,1,6],[-9,5,7]], 4),
]

for i, (mat, ans) in enumerate(tests):
    res = sol.maxIncreasingCells(mat)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
