# from pudb import set_trace; set_trace()
from typing import List
import heapq


class Solution1:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """LeetCode 7

        This idea is that at each time point, we find the farthest cell we
        can reach from the starting point. Once we hit the end point, we return.

        We use a BFS-type of searching strategy. For each time point, we run
        the BFS as many times as necessary until all the cells in the queue are
        at the farthest they can go. Then we increment time and do this again.

        Runtime is terrible, 4048 ms. We pass, but might as well consider this
        as TLE.
        """
        M, N = len(grid), len(grid[0])
        t = grid[0][0]
        queue = [(0, 0)]
        grid[0][0] = -1
        while True:
            while True:
                temp = []
                explored = False
                for i, j in queue:
                    unexplored = False
                    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < M and 0 <= nj < N:
                            if 0 <= grid[ni][nj] <= t:
                                if ni == N - 1 and nj == M - 1:
                                    return t
                                grid[ni][nj] = -1
                                temp.append((ni, nj))
                                explored = True
                            elif grid[ni][nj] > t:
                                unexplored = True
                    if unexplored:
                        temp.append((i, j))
                queue = temp
                if not explored:
                    break
            t += 1


class Solution2:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """This is according to the hint, using something similar to Dijkstra.
        The idea is that for each cell we visit, we push all its neighbors that
        have not been visited before into a priority queue, with the grid value
        being the one to compare. At each time point, we look at the top of the
        priority queue and visit the one with the smallest grid value that is
        smaller or equal to the current time stamp. We keep doing this, ensuring
        that each time the cell that is visited must be the one with the
        smallest grid value currently reachable. Once the end point pops up,
        we end the search.

        We can use Dijkstra, because we do not care about the actual path.
        Every cell we push into the priority queue is guaranteed to be reachable
        from the start one way or another. All we care about is that the cell
        with the minimum grid value gets visited every time.

        O(N^2log(N)), 88 ms, 98% ranking.
        """
        N = len(grid)
        heap = [(grid[0][0], 0, 0)]
        t = grid[0][0]
        grid[0][0] = -1
        while True:
            while heap[0][0] <= t:
                _, i, j = heapq.heappop(heap)
                if i == N - 1 and j == N - 1:
                    return t
                for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] >= 0:
                        heapq.heappush(heap, (grid[ni][nj], ni, nj))
                        grid[ni][nj] = -1
            t += 1


class Solution3:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Binary search. Courtesy of:

        https://leetcode.com/problems/swim-in-rising-water/discuss/1285099/Easy-Solution-w-Explanation-or-Optimization-from-Brute-Force-to-Binary-Search-or-Beats-100

        The idea is given any max time point, we use a very generic DFS to see
        if we can go from top left to bottom right. Sine the time point must
        be a value from 1 to N * N - 1, we can use binary search to locate the
        target time point. Say we have l and r and mid. If we can find a path
        with max time point being mid, that means it is possible for us to do
        better. Then we do r = mid - 1. Otherwise, we need to raise the time
        point, so we do l = mid + 1. We continue this until the target time
        point is reached.

        O(N^2 log(N)). DFS takes O(N^2) and the binary search takes O(log(N))
        """
        N = len(grid)

        def dfs(i: int, j: int, visited, t: int) -> bool:
            if i == N - 1 and j == N - 1:
                return True
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in visited and grid[ni][nj] <= t:
                    visited.add((ni, nj))
                    if dfs(ni, nj, visited, t):
                        return True
            return False

        l = max(grid[0][0], grid[N - 1][N - 1])
        r = N * N - 1
        while l <= r:
            mid = (l + r) // 2
            if dfs(0, 0, set(), mid):
                r = mid - 1
            else:
                l = mid + 1
        return l


class DSU:
    """Disjoint Set Union.

    It supports union and find in log(N) time. It has rank and path compression.
    Shamelessly copied from:

    https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained
    """

    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        if xr != yr:
            if self.rnk[xr] < self.rnk[yr]:
                self.par[xr] = yr
            elif self.rnk[xr] > self.rnk[yr]:
                self.par[yr] = xr
            else:
                self.par[yr] = xr
                self.rnk[xr] += 1


class Solution4:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """Union Find, courtesy of:

        https://leetcode.com/problems/swim-in-rising-water/discuss/1284843/Python-2-solutions%3A-Union-FindHeap-explained

        The idea is to go from time point 1 to N * N - 1. At each time point, we
        mark which cell has become available. And we look at all neighboring
        cells and see which ones can be unioned with the current cell. After
        each time point and the associated union, we check whether the top left
        and bottom right cells belong to the same union.
        """
        N = len(grid)
        dsu = DSU(N * N)
        mapping = {grid[i][j]: (i, j) for i in range(N) for j in range(N)}
        for t in range(N * N):
            i, j = mapping[t]
            grid[i][j] = -1  # sentinel that this cell is available for union
            for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == -1:
                    dsu.union(N * i + j, N * ni + nj)
            if dsu.find(0) == dsu.find(N * N - 1):
                return t


sol = Solution4()
tests = [
    ([[0, 2], [1, 3]], 3),
    ([[0, 1, 2, 3, 4], [24, 23, 22, 21, 5], [12, 13, 14, 15, 16], [11, 17, 18, 19, 20], [10, 9, 8, 7, 6]], 16),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.swimInWater(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
