# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict

class MinSegTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.tree = {}
        self.lazy = {}

    def _update(self, idx: int, ss: int, se: int, us: int, ue: int, val: int) -> None:
        if idx in self.lazy:
            self.tree[idx] = val
            ???

        if ss > se or us > se or ue < ss:
            return
        if ss >= us and se <= ue:
            self.tree[idx] = val
        else:
            mid = (ss + se) // 2
            self._update(2 * idx + 1, ss, mid, us, ue, val)
            self._update(2 * idx + 2, mid + 1, se, us, ue, val)
            self.tree[idx] = min(
                self.tree.get(2 * idx + 1, math.inf),
                self.tree.get(2 * idx + 2, math.inf),
            )

    def update(self, val: int, pos: int) -> None:
        self._update(0, 0, self.N - 1, pos, pos, val)

    def _query(self, idx: int, ss: int, se: int, qs: int, qe: int) -> int:
        if ss > se or qs > se or qe < ss:
            return math.inf
        if qs <= ss and qe >= se:
            return self.tree[idx]
        mid = (ss + se) // 2
        return min(
            self._query(2 * idx + 1, ss, mid, qs, qe),
            self._query(2 * idx + 2, mid + 1, se, qs, qe)
        )

    def query(self, qs: int, qe: int) -> int:
        return self._query(0, 0, self.N - 1, qs, qe)


class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """It works, but TLE. My guess is that we have to use a better
        implementation of segment tree, e.g. lazy seg tree.
        """
        M, N = len(grid), len(grid[0])
        row_seg_trees = [MinSegTree(N) for _ in range(M)]
        col_seg_trees = [MinSegTree(M) for _ in range(N)]
        row_seg_trees[M - 1].update(1, N - 1)
        col_seg_trees[N - 1].update(1, M - 1)
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):
                if i == M - 1 and j == N - 1:
                    continue
                cur = min(
                    row_seg_trees[i].query(j + 1, min(j + grid[i][j], N - 1)),
                    col_seg_trees[j].query(i + 1, min(i + grid[i][j], M - 1)),
                ) + 1
                row_seg_trees[i].update(cur, j)
                col_seg_trees[j].update(cur, i)
        res = row_seg_trees[0].query(0, 0)
        return res if res < math.inf else -1


sol = Solution()
tests = [
    ([[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]], 4),
    ([[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]], 3),
    ([[2,1,0],[1,0,0]], -1),
    ([[0]], 1)
]

for i, (grid, ans) in enumerate(tests):
    res = sol.minimumVisitedCells(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
