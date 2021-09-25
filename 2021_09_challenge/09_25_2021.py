# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """LeetCode 1293

        This is a hard question. And I got stuck on a stupid mistake. If I
        had not commited that mistake, I would've finished 45 min earlier.

        First of all, I compute a matrix that records the min number of
        obstacles each cell must encounter if we reach the destination in min
        number of steps. It is deterministic that the min number of steps from
        (i, j) to (m - 1, n - 1) is m + n - i - j - 2, and the path must be a
        zigzag going right or down. So we can compute this num_obs matrix by
        going from bottom right to top left. At each (i, j), the min number of
        obstacles is min(num_obs[i + 1][j], num_obs[i][j + 1]) plus 1 if (i, j)
        is an obstacle, or 0 otherwise.

        The purpose of num_obs is that when we reach a cell with the current
        quota >= num_obs[i][j], that means we can reach the destination with the
        min number of steps.

        Next, we perform a regular DFS on the original grid. The only trick is
        that if the next step is an obstacle, we can choose to still visit that
        cell, but we must reduce our quota by one. Therefore, to memoize DFS, we
        need three levels: i, j, quota. At each cell (i, j), we look over all
        its valid neighbors (i.e. within the bound and not been visited). If
        the valid neighbor is a 0, we visit it without decreasing quota.
        Otherwise, we visit it with quota decreased, except when quota is
        already zero, then we cannot visit a cell that is an obstacle.

        That's basically it. The answer is memo[k][0][0]

        O(MNK), where M is num rows, N num of cols, and K = k.
        128 ms
        """
        m, n = len(grid), len(grid[0])
        num_obs = [[0] * n for _ in range(m)]
        ai, aj = m - 1, n - 1
        while ai >= 0 and aj >= 0:
            for i in range(ai, -1, -1):
                if aj == n - 1 and i == m - 1:
                    num_obs[i][aj] = 0
                else:
                    num_obs[i][aj] = int(grid[i][aj] == 1) + min(
                        num_obs[i + 1][aj] if i + 1 < m else math.inf,
                        num_obs[i][aj + 1] if aj + 1 < n else math.inf,
                    )
            for j in range(aj - 1, -1, -1):
                num_obs[ai][j] = int(grid[ai][j] == 1) + min(
                    num_obs[ai + 1][j] if ai + 1 < m else math.inf,
                    num_obs[ai][j + 1] if j + 1 < n else math.inf,
                )
            ai -= 1
            aj -= 1

        memo = [[[-1] * n for _ in range(m)] for _ in range(k + 1)]
        for q in range(k + 1):
            memo[q][m - 1][n - 1] = 0

        def dfs(i: int, j: int, quota: int, path) -> None:
            if quota >= num_obs[i][j]:
                memo[quota][i][j] = m + n - i - j - 2
                return
            res = math.inf
            for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in path:
                    path.add((ni, nj))
                    if grid[ni][nj] == 0:
                        if memo[quota][ni][nj] < 0:
                            dfs(ni, nj, quota, path)
                        res = min(res, 1 + memo[quota][ni][nj])
                    elif quota > 0:
                        if memo[quota - 1][ni][nj] < 0:
                            dfs(ni, nj, quota - 1, path)
                        res = min(res, 1 + memo[quota - 1][ni][nj])
                    path.remove((ni, nj))
            memo[quota][i][j] = res

        dfs(0, 0, k, set([(0, 0)]))
        return -1 if memo[k][0][0] == math.inf else memo[k][0][0]


class Solution2:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        """This is from DBabichev

        https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/1484735/Python-short-bfs-explained

        It is very simple. The benefit of using BFS is that the moment we hit
        the destination, we have accumulated the shorest distance. There are two
        tricks. First, when we add a new cell to the path, we need to check the
        quota as well. Second, when we cache the cells already visited, we need
        to also include quota. Basically, each cell can be represented by three
        dimensions: i, j, and q.

        O(MNK), 72 ms.
        """
        m, n = len(grid), len(grid[0])
        if k >= m + n - 2:
            # quota is larger than min steps, we can always take min steps
            return m + n - 2
        queue, visited = [(0, 0, 0, k)], set([(0, 0, k)])
        while queue:
            temp = []
            for steps, i, j, quota in queue:
                if i == m - 1 and j == n - 1:
                    return steps
                for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= ni < m and 0 <= nj < n and quota >= grid[ni][nj]:
                        new = (ni, nj, quota - grid[ni][nj])
                        if new not in visited:
                            temp.append((steps + 1,) + new)
                            visited.add(new)
                queue = temp
        return -1


sol = Solution2()
tests = [
    ([[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]], 1, 6),
    ([[0, 1, 1], [1, 1, 1], [1, 0, 0]], 1, -1),
    ([[0, 0, 0, 0], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]], 2, -1),
    ([[0, 0, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0]], 2, -1),
    ([[0, 0], [1, 1], [1, 1], [1, 1], [0, 0]], 2, -1),
]

for i, (grid, k, ans) in enumerate(tests):
    res = sol.shortestPath(grid, k)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
