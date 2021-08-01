# from pudb import set_trace; set_trace()
from typing import List
from collections import Counter


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


class Solution1:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """LeetCode 827

        This problem screams union-find at me. Fortunately, we have a snippet
        for union-find, which makes this problem drastically easier. The idea is
        to first find all the islands using union-find. Then we iterate through
        all the zeros and record the islands that surround the zero. Each
        surrounding island can be connected by turning the current zero into a
        one. The solution is to find the zero position that can connect the
        largest islands.

        Time complexity O(N^2log(N)), where N is the length of the side of the
        grid. Union-find and extra path compression takes O(N^2log(N)). Finding
        the zero takes O(N^2). 4196 ms.
        """
        n = len(grid)
        dsu = DSU(n * n)
        pot_zeros = []
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    for di, dj in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            if grid[ni][nj]:
                                dsu.union(i * n + j, ni * n + nj)
                            else:
                                pot_zeros.append((ni, nj))
        if not pot_zeros:  # grid is either all ones or all zeros
            return n * n if grid[0][0] else 1
        for k in range(n * n):  # solely used to compress the path
            dsu.find(k)
        count = Counter(dsu.par)
        res = 0
        for i, j in pot_zeros:
            islands = set()
            for di, dj in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj]:
                        islands.add(dsu.par[ni * n + nj])
            res = max(res, sum(count[p] for p in islands) + 1)
        return res


class Solution2:
    def largestIsland(self, grid: List[List[int]]) -> int:
        """We don't need union-find. We can simply run DFS to obtain the size
        of each island. This can reduce the time complexity to O(N^2).

        Courtesy of the official solution:
        https://leetcode.com/problems/making-a-large-island/solution/

        3236 ms, 81% ranking.
        """
        n = len(grid)
        pot_zeros = []

        def dfs(i: int, j: int, island_idx: int) -> int:
            size = 1
            grid[i][j] = island_idx
            for di, dj in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj] == 1:
                        size += dfs(ni, nj, island_idx)
                    elif grid[ni][nj] == 0:
                        pot_zeros.append((ni, nj))
            return size

        island_idx = 2
        count = {}
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    count[island_idx] = dfs(i, j, island_idx)
                    island_idx += 1
        if not pot_zeros:  # grid is either all ones or all zeros
            return n * n if grid[0][0] else 1
        res = 0
        for i, j in pot_zeros:
            islands = set()
            for di, dj in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n:
                    if grid[ni][nj]:
                        islands.add(grid[ni][nj])
            res = max(res, sum(count[p] for p in islands) + 1)
        return res


sol = Solution2()
tests = [
    ([[0, 0], [0, 0]], 1),
    ([[1, 0], [0, 0]], 2),
    ([[1, 0], [0, 1]], 3),
    ([[1, 1], [1, 0]], 4),
    ([[1, 1], [1, 1]], 4),
    ([[1, 0, 0, 1, 1], [1, 0, 0, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 1, 0]], 16),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.largestIsland(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
