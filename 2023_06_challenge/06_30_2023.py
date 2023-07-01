# from pudb import set_trace; set_trace()
from typing import List, Tuple, Set
import math
from collections import defaultdict

class DSU1:
    def __init__(self, M: int, N: int) -> None:
        self.par = {(i, j): (i, j) for i in range(M) for j in range(N)}
        self.rows = {(i, j): {i} for i in range(M) for j in range(N)}
        self.M = M
        self.N = N

    def find(self, c: Tuple[int, int]) -> int:
        if self.par[c] != c:
            self.par[c] = self.find(self.par[c])
        return self.par[c]

    def union(self, c1: Tuple[int, int], c2: Tuple[int, int]) -> int:
        p1, p2 = self.find(c1), self.find(c2)
        if p1 == p2:
            return len(self.rows[p1])
        if len(self.rows[p1]) >= len(self.rows[p2]):
            self.par[p2] = p1
            self.rows[p1] = self.rows[p1].union(self.rows[p2])
            return len(self.rows[p1])
        self.par[p1] = p2
        self.rows[p2] = self.rows[p2].union(self.rows[p1])
        return len(self.rows[p2])


class Solution1:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """LeetCode 1970

        Union Find works!!! I did read the hint, but I couldn't figure out how
        binary search can fashion into this problem. Therefore, I went back to
        union find and realized that instead of using an arbitrary rank, I can
        use the number of unique rows as the ranking for each parent. In
        addition, I can make union function return the largest count of unique
        rows in the unioned parent. Thus, each time we do union, we immediately
        know the effect of the union.

        The basic idea is to go from right to left in cells, which means we are
        adding available cells one at a time. Any cells that are adjacent can
        be unioned and we will know how many unique rows are in the union. The
        first time that any parent has all the rows is the time that the last
        available path from top to bottom appears. And we can return the result
        then.

        O(MN + 4KM), 2831 ms, faster than 40.76%
        """
        dsu = DSU1(row, col)
        unblocked = set()
        for k in range(len(cells) - 1, -1, -1):
            i, j = cells[k][0] - 1, cells[k][1] - 1
            unblocked.add((i, j))
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col and (ni, nj) in unblocked:
                    num_rows = dsu.union((i, j), (ni, nj))
                    if num_rows == row:
                        return k
        return -1


class DSU2:
    def __init__(self, N: int) -> None:
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x: int) -> int:
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x: int, y: int) -> bool:
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rnk[px] > self.rnk[py]:
            self.par[py] = px
        elif self.rnk[px] < self.rnk[py]:
            self.par[px] = py
        else:
            self.par[py] = px
            self.rnk[px] += 1
        return True


class Solution2:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """This is the Union Find solution from the official solution.

        It is brilliant because it creates two additional, non-existent members
        for union find, which is top and bottom. We will union top and bottom to
        any cell that is on top or bottom. Then after each union, we check if
        top and bottom belong to the same group. If they are, we have found the
        day when a path is available.

        Very smart.

        O(MN + K), 2063 ms, faster than 62.50%
        """
        dsu = DSU2(row * col + 2)
        unblocked = set()
        top, bottom = 0, row * col + 1
        for k in range(len(cells) - 1, -1, -1):
            i, j = cells[k][0] - 1, cells[k][1] - 1
            unblocked.add((i, j))
            if i == 0:
                dsu.union(top, i * col + j + 1)
            elif i == row - 1:
                dsu.union(bottom, i * col + j + 1)
            for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < row and 0 <= nj < col and (ni, nj) in unblocked:
                    dsu.union(i * col + j + 1, ni * col + nj + 1)
                    if dsu.find(top) == dsu.find(bottom):
                        return k
        return -1


class Solution3:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        """BFS + binary search, from the official solution.

        The part where I got stuck was how to use BFS to quickly determine
        whether there is a path from top to bottom. The answer is NOT to start
        from a single cell from the top. Instead, start the queue with all
        available cells on the top. Then we flood it by BFS and we can stop when
        we hit the bottom for the first time.

        BFS is used as a way to decide which cells to flood. We choose half of
        the cells first, run BFS and see if we can reach the bottom. If we can,
        that means we need to move to the right half. Otherwise left half.

        A good method. If I had thought about filling the first row as the
        starting queue, I would've come up with this method.

        O(MNlog(MN)), 3593 ms, faster than 19.56%
        """

        def bfs(queue: List[Tuple[int, int]], forbidden: Set[Tuple[int, int]]) -> bool:
            visited = set(queue)
            while queue:
                tmp = []
                for i, j in queue:
                    if i == row - 1:
                        return True
                    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < row and 0 <= nj < col and not (ni, nj) in visited and not (ni, nj) in forbidden:
                            visited.add((ni, nj))
                            tmp.append((ni, nj))
                queue = tmp
            return False

        lo, hi = 0, len(cells)
        while lo < hi:
            mid = (lo + hi) // 2
            forbidden = set((cells[i][0] - 1, cells[i][1] - 1) for i in range(mid + 1))
            can_reach = bfs(
                [(0, j) for j in range(col) if (0, j) not in forbidden],
                forbidden
            )
            if can_reach:
                lo = mid + 1
            else:
                hi = mid
        return lo



sol = Solution3()
tests = [
    (2, 2, [[1,1],[2,1],[1,2],[2,2]], 2),
    (2, 2, [[1,1],[1,2],[2,1],[2,2]], 1),
    (3, 3, [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]], 3),
    (6, 2, [[4,2],[6,2],[2,1],[4,1],[6,1],[3,1],[2,2],[3,2],[1,1],[5,1],[5,2],[1,2]], 3),
]

for i, (row, col, cells, ans) in enumerate(tests):
    res = sol.latestDayToCross(row, col, cells)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
