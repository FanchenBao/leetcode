# from pudb import set_trace; set_trace()
from typing import List
import math
from collections import defaultdict
from sortedcontainers import SortedList


class MinSegTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.tree = {}

    def _update(self, idx: int, rs: int, re: int, val: int, pos: int) -> None:
        if rs == re == pos:
            self.tree[idx] = val
        else:
            mid = (rs + re) // 2
            if pos <= mid:
                self._update(2 * idx + 1, rs, mid, val, pos)
            else:
                self._update(2 * idx + 2, mid + 1, re, val, pos)
            self.tree[idx] = min(
                self.tree.get(2 * idx + 1, math.inf),
                self.tree.get(2 * idx + 2, math.inf),
            )

    def update(self, val: int, pos: int) -> None:
        self._update(0, 0, self.N - 1, val, pos)

    def _query(self, idx: int, rs: int, re: int, qs: int, qe: int) -> int:
        if qs > re or qe < rs or qs > qe:
            return math.inf
        if qs <= rs and qe >= re:
            return self.tree[idx]
        mid = (rs + re) // 2
        if qe <= mid:
            return self._query(2 * idx + 1, rs, mid, qs, qe)
        if qs > mid:
            return self._query(2 * idx + 2, mid + 1, re, qs, qe)
        return min(
            self._query(2 * idx + 1, rs, mid, qs, mid),
            self._query(2 * idx + 2, mid + 1, re, mid + 1, qe)
        )

    def query(self, qs: int, qe: int) -> int:
        return self._query(0, 0, self.N - 1, qs, qe)


class LazyMinSegTree:
    def __init__(self, N: int) -> None:
        self.N = N
        self.tree = defaultdict(lambda: math.inf)
        self.lazy = defaultdict(lambda: math.inf)

    def _update(self, idx: int, ss: int, se: int, us: int, ue: int, val: int) -> None:
        if self.lazy[idx] < math.inf:
            self.tree[idx] = min(self.tree[idx], self.lazy[idx])
            # propagate to children
            self.lazy[2 * idx + 1] = min(self.lazy[2 * idx + 1], self.lazy[idx])
            self.lazy[2 * idx + 2] = min(self.lazy[2 * idx + 2], self.lazy[idx])
            self.lazy[idx] = math.inf

        if ss > se or us > se or ue < ss:
            return
        if ss >= us and se <= ue:
            self.tree[idx] = min(self.tree[idx], val)
            self.lazy[2 * idx + 1] = min(self.lazy[2 * idx + 1], val)
            self.lazy[2 * idx + 2] = min(self.lazy[2 * idx + 2], val)
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
        if self.lazy[idx] < math.inf:
            self.tree[idx] = min(self.tree[idx], self.lazy[idx])
            # propagate to children
            self.lazy[2 * idx + 1] = min(self.lazy[2 * idx + 1], self.lazy[idx])
            self.lazy[2 * idx + 2] = min(self.lazy[2 * idx + 2], self.lazy[idx])
            self.lazy[idx] = math.inf

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


class Solution1:
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


class Solution2:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """Using lazy segment tree, it's actually slower.
        """
        M, N = len(grid), len(grid[0])
        row_seg_trees = [LazyMinSegTree(N) for _ in range(M)]
        col_seg_trees = [LazyMinSegTree(M) for _ in range(N)]
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


class Solution3:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """BFS as the base method, and use SortedList to reduce the search space
        efficiently. This is the second time in a ROW that we have seen the
        application of SortedList as a way to reduce search space. This owing to
        its fast indexing and removal while maintaining the sorted order of the
        underlying list. It's just a wrapper of a cleverly implemented self-
        balancing binary search tree.

        O(MNlog(max(M, N))), 9172 ms, faster than 10.72%
        """
        M, N = len(grid), len(grid[0])
        unused_rows = [SortedList(range(N)) for _ in range(M)]
        unused_cols = [SortedList(range(M)) for _ in range(N)]
        queue = [(0, 0)]
        steps = 0
        while queue:
            tmp = []
            for i, j in queue:
                if i == M - 1 and j == N - 1:
                    return steps + 1
                for k in list(unused_rows[i].irange(j + 1, min(j + grid[i][j], N - 1))):
                    tmp.append((i, k))
                    unused_rows[i].remove(k)
                for k in list(unused_cols[j].irange(i + 1, min(i + grid[i][j], M - 1))):
                    tmp.append((k, j))
                    unused_cols[j].remove(k)
            queue = tmp
            steps += 1
        return -1


class DSU:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        # no need to set up rank, because all the unioned elements must point to
        # the largest member

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> None:
        px, py = self.find(x), self.find(y)
        if px < py:
            self.par[px] = py
        else:
            self.par[py] = px


class Solution4:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        """Union Find. Use Union Find to quickly identify what the next unused
        index is for each row and col. Within each row and col, all the used
        indices are grouped together.

        Used the implementation from https://leetcode.com/problems/minimum-number-of-visited-cells-in-a-grid/discuss/3397126/BFS-%2B-DSU-keep-tracking-the-next-point
        regarding how to find the next index for each row and col

        7608 ms, faster than 61.43% 
        """
        M, N = len(grid), len(grid[0])
        used_rows = [DSU(N) for _ in range(M)]
        used_cols = [DSU(M) for _ in range(N)]
        queue = [(0, 0)]
        steps = 0
        while queue:
            tmp = []
            for i, j in queue:
                if i == M - 1 and j == N - 1:
                    return steps + 1
                while used_rows[i].find(j) < min(j + grid[i][j], N - 1):
                    k = used_rows[i].find(j) + 1
                    tmp.append((i, k))
                    used_rows[i].union(j, k)
                while used_cols[j].find(i) < min(i + grid[i][j], M - 1):
                    k = used_cols[j].find(i) + 1
                    tmp.append((k, j))
                    used_cols[j].union(i, k)
            queue = tmp
            steps += 1
        return -1


sol = Solution4()
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
