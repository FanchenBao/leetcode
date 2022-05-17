# from pudb import set_trace; set_trace()
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """LeetCode 1091

        Turn the problem into graph, and our objective is to find the shortest
        path from source to destination, with all edges having the same weight.
        Thus, BFS suffices.

        O(N^2) where N = len(grid). 957 ms, faster than 35.01%

        UPDATE: change grid to avoid the use of an additional `visited` set.

        The update improves speed tremendously: 569 ms, faster than 95.13% 
        """
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        N = len(grid)
        if N == 1:  # edge case [[0]]
            return 1
        queue = [(0, 0)]
        grid[0][0] = -2
        length = 0
        while queue:
            temp = []
            length += 1
            for i, j in queue:
                for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, -1), (-1, 1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < N and 0 <= nj < N and grid[ni][nj] == 0:
                        if ni == N - 1 and nj == N - 1:
                            return length + 1
                        temp.append((ni, nj))
                        grid[ni][nj] = -2
            queue = temp
        return - 1


sol = Solution()
tests = [
    ([[0,1],[1,0]], 2),
    ([[0,0,0],[1,1,0],[1,1,0]], 4),
    ([[1,0,0],[1,1,0],[1,1,0]], -1),
    ([[0]], 1),
    ([[1]], -1),
]

for i, (grid, ans) in enumerate(tests):
    res = sol.shortestPathBinaryMatrix(grid)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
