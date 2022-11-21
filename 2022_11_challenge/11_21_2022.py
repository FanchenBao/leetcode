# from pudb import set_trace; set_trace()
from typing import List
import math



class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        """LeetCode 1926

        BFS.

        O(MN), 2434 ms, faster than 14.80%

        UPDATE:

        we can mark visited cells with '+' in-place. Courtesy of official
        solution.

        2181 ms, faster than 33.05%
        """
        queue = [tuple(entrance)]
        maze[entrance[0]][entrance[1]] = '+'  # in-place mark visited cell
        M, N = len(maze), len(maze[0])
        steps = 0
        while queue:
            tmp = []
            for i, j in queue:
                if (i == 0 or j == 0 or i == M - 1 or j == N - 1) and [i, j] != entrance:
                    return steps
                for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < M and 0 <= nj < N and (ni, nj) and maze[ni][nj] == '.':
                        tmp.append((ni, nj))
                        maze[ni][nj] = '+'
            queue = tmp
            steps += 1
        return -1


sol = Solution()
tests = [
    ([["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], [1,2], 1),
    ([["+","+","+"],[".",".","."],["+","+","+"]], [1,0], 2),
    ([[".","+"]], [0,0], -1),
]

for i, (maze, entrance, ans) in enumerate(tests):
    res = sol.nearestExit(maze, entrance)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
