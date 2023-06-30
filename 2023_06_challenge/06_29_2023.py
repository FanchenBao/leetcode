# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        """LeetCode 864

        First of all, when the direction to go is all four directions and the
        goal is to find the shortest path in a grid, BFS is usually the
        preferred method. This problem requires one to carry the state of the
        keys currently obtained at each cell. Visiting a cell does not preclude
        this cell from being visited again, but if we revisit a cell with the
        same number of keys, that is a repeated visit and shall not happen.

        Therefore, the state we have to keep in the visited set is the cell
        itself and the state of the keys currently obtained. Since the number
        of keys is at most 6, we can use bit to represent what keys have been
        captured.

        The rest is just BFS.

        O(4 * MN * 2^K), 267 ms, faster than 95.21%
        """
        M, N = len(grid), len(grid[0])
        num_keys = 0
        queue = []
        for i in range(M):
            for j in range(N):
                if grid[i][j] == '@':
                    queue.append((i, j, 0))
                elif ord(grid[i][j]) >= 97:
                    num_keys += 1
        visited = set()
        end_state = (1 << num_keys) - 1
        steps = 0
        while queue:
            tmp = []
            # print(queue, steps, keys)
            for i, j, keys in queue:
                if ord(grid[i][j]) >= 97:
                    keys |= 1 << (ord(grid[i][j]) - 97)
                    if keys == end_state:
                        return steps
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and grid[ni][nj] != '#' and (ni, nj, keys) not in visited:
                        if 65 <= ord(grid[ni][nj]) <= 70 and not (1 << (ord(grid[ni][nj]) - 65)) & keys:
                            continue
                        tmp.append((ni, nj, keys))
                        visited.add((ni, nj, keys))
            queue = tmp
            steps += 1
        return -1


sol = Solution()
tests = [
    (["@.a..","###.#","b.A.B"], 8),
    (["@..aA","..B#.","....b"], 6),
    (["@Aa"], -1),
    (["b","A","a","@","B"], 3),
    (["@...a",".###A","b.BCc"], 10),
    (["@abcdeABCDEFf"], -1),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.shortestPathAllKeys(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
