# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict


class Solution_Wrong:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """This is the WRONG solution. But it took me so much effort to get here,
        I will just let this solution be.
        """
        M, N = len(matrix), len(matrix[0])
        row_sorted = [sorted((v, j) for j, v in enumerate(row)) for row in matrix]
        row_pos_map = []
        for r in row_sorted:
            row_pos_map.append({})
            for p, (v, _) in enumerate(r):
                row_pos_map[-1][v] = min(row_pos_map[-1].get(v, math.inf), p)
        col_sorted = [sorted((matrix[i][j], i) for i in range(M)) for j in range(N)]
        col_pos_map = []
        for c in col_sorted:
            col_pos_map.append({})
            for p, (v, _) in enumerate(c):
                col_pos_map[-1][v] = min(col_pos_map[-1].get(v, math.inf), p)
        res = [[1] * N for _ in range(M)]  # this is initial row_ranks
        for i, r in enumerate(row_sorted):
            for k, (v, j) in enumerate(r):
                if k > 0:
                    res[i][j] = (res[i][r[k - 1][1]] + 1) if v > r[k - 1][0] else res[i][r[k - 1][1]]
        col_ranks = [[1] * N for _ in range(M)]
        for j, c in enumerate(col_sorted):
            for k, (v, i) in enumerate(c):
                if k > 0:
                    col_ranks[i][j] = (col_ranks[c[k - 1][1]][j] + 1) if v > c[k - 1][0] else col_ranks[c[k - 1][1]][j]

        def check(i: int, j: int, check_row: bool):
            """res[i][j] has just been updated with delta. We need to check
            whether other elements in the row (col) need to be updated as well.
            If some need to be updated, we have to run check on their col (row).
            """
            if check_row:
                row_pos = row_pos_map[i][matrix[i][j]]
                cur_j = j
                for p in range(row_pos, N):
                    nv, nj = row_sorted[i][p]
                    if nv == matrix[i][cur_j]:
                        if res[i][nj] != res[i][cur_j]:
                            res[i][nj] = res[i][cur_j]
                            check(i, nj, not check_row)
                    elif nv > matrix[i][cur_j]:
                        if res[i][nj] <= res[i][cur_j]:
                            res[i][nj] = res[i][cur_j] + 1
                            check(i, nj, not check_row)
                    cur_j = nj
            else:  # check column
                col_pos = col_pos_map[j][matrix[i][j]]
                cur_i = i
                for p in range(col_pos, M):
                    nv, ni = col_sorted[j][p]
                    if nv == matrix[cur_i][j]:
                        if res[ni][j] != res[cur_i][j]:
                            res[ni][j] = res[cur_i][j]
                            check(ni, j, not check_row)
                    elif nv > matrix[cur_i][j]:
                        if res[ni][j] <= res[cur_i][j]:
                            res[ni][j] = res[cur_i][j] + 1
                            check(ni, j, not check_row)
                    cur_i = ni

        for j in range(N):
            for i in range(M):
                if res[i][j] != col_ranks[i][j]:
                    res[i][j] = max(res[i][j], col_ranks[i][j])
                    check(i, j, True)
                    check(i, j, False)
        return res


class DSU:
    """Disjoint Set Union.

    It supports union and find in log(N) time. It has rank and path compression.
    Shamelessly copied from:

    https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained

    Update 06/25/2021: Improved functionality by returning boolean value in
    self.union function. Reference:

    https://leetcode.com/problems/redundant-connection/solution/
    """

    def __init__(self, N: int):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            elif self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr
            else:
                self.par[yr] = xr
                self.rnk[xr] += 1
            return True
        return False  # x, y already in the same union


class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        """LeetCode 1632

        I wasn't able to solve this question. It was still difficult even
        after reading the solution. BTW, the solution was from here:

        https://leetcode.com/problems/rank-transform-of-a-matrix/discuss/1391380/C%2B%2BPython-HashMap-and-Sort-and-UnionFind-Visualize-picture-Clean-and-Concise


        But after some further thought, I have a bit
        better understanding of it. The idea is to go from the smallest value
        in the matrix up to the largest. At each value, we can group the cells
        that share at least one row or one col together, because they must have
        the same rank. This is where the trick comes: we use Union-Find to
        group the row index and a representation of the column index. This is
        equivalent to saying any cell of the same value that also shares one
        row or one col with another belongs to the same group.

        After obtaining the groups for a value, we can compute its rank. The
        way to compute it is the second trick: its rank must be the max rank of
        all the rows and cols involved in the group plus one. This is to ensure
        that the new value's rank must be bigger than all the other ranks that
        have already been computed. In the implementation, we use a rank array
        to record the max rank of all rows and cols (col is represented by col
        index plus number of rows). We iterate through all the rows and cols
        of the current value and record the max rank encountered for its group.
        Then we iterate through all the rows and cols again but update the rank
        array and the result matrix based on the max rank just obtained.

        This procedure repeats itself until all the unique vals in the matrix
        have been processed.
        """
        M, N = len(matrix), len(matrix[0])
        vals_map = defaultdict(list)
        res = [[0] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                vals_map[matrix[i][j]].append((i, j))
        rank = [0] * (M + N)  # max ranking of each row and col (col = j + M)
        for v in sorted(vals_map):
            dsu = DSU(M + N)  # we use Union-Find ONLY for cells of the same value
            for i, j in vals_map[v]:
                dsu.union(i, j + M)  # union the row and col (col = j + M)
            max_rank = defaultdict(int)
            for i, j in vals_map[v]:
                group = dsu.find(i)  # find the max rank for the group
                max_rank[group] = max([max_rank[group], rank[i], rank[j + M]])
            for i, j in vals_map[v]:
                group = dsu.find(i)
                rank[i] = rank[j + M] = max_rank[group] + 1  # update max_rank
                res[i][j] = rank[i]
        return res


sol = Solution()
tests = [
    ([[1, 2], [3, 4]], [[1, 2], [2, 3]]),
    ([[7, 3, 6], [1, 4, 5], [9, 8, 2]], [[5, 1, 4], [1, 2, 3], [6, 3, 1]]),
    ([[20, -21, 14], [-19, 4, 19], [22, -47, 24], [-19, 4, 19]], [[4, 2, 3], [1, 3, 4], [5, 1, 6], [1, 3, 4]]),
    ([[7, 7], [7, 7]], [[1, 1], [1, 1]]),
    ([[-37, -50, -3, 44], [-37, 46, 13, -32], [47, -42, -3, -40], [-17, -22, -39, 24]], [[2, 1, 4, 6], [2, 6, 5, 4], [5, 2, 4, 3], [4, 3, 1, 5]]),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.matrixRankTransform(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail.')
        print('Ans:')
        for r in ans:
            print(r)
        print('Res')
        for r in res:
            print(r)
