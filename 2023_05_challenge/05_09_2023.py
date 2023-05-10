# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """LeetCode 54

        Old problem, but requires a little bit work. The main idea is to set up
        limits on each direction of movement, and check whether we have fulfilled
        all the cells after going through each direction.

        O(MN), 43 ms, faster than 14.13%
        """
        M, N = len(matrix), len(matrix[0])
        lr_top, ud_right, rl_bot, du_left = N - 1, M - 1, 0, min(M - 1, 1)
        res = []
        ii, jj = 0, -1
        while True:
            # left to right, top
            for j in range(jj + 1, lr_top + 1):
                res.append(matrix[ii][j])
            if len(res) == M * N:
                break
            jj = j
            lr_top -= 1
            # up to down, right
            for i in range(ii + 1, ud_right + 1):
                res.append(matrix[i][jj])
            if len(res) == M * N:
                break
            ii = i
            ud_right -= 1
            # right to left, bottom
            for j in range(jj - 1, rl_bot - 1, -1):
                res.append(matrix[ii][j])
            if len(res) == M * N:
                break    
            jj = j
            rl_bot += 1
            # down to up, left
            for i in range(ii - 1, du_left - 1, -1):
                res.append(matrix[i][jj])
            ii = i
            du_left += 1
        return res


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Same as solution1, but easier to reason with.
        """
        M, N = len(matrix), len(matrix[0])
        lr_top, ud_right, rl_bot, du_left = N - 1, M - 1, 0, min(M - 1, 1)
        res = []
        ii, jj = 0, -1
        while len(res) < M * N:
            # left to right, top
            if lr_top < jj + 1:  # no more move possible
                break
            for j in range(jj + 1, lr_top + 1):
                res.append(matrix[ii][j])
            jj = lr_top
            lr_top -= 1
            # up to down, right
            if ud_right < ii + 1:  # no more move possible
                break
            for i in range(ii + 1, ud_right + 1):
                res.append(matrix[i][jj])
            ii = ud_right
            ud_right -= 1
            # right to left, bottom
            if rl_bot > jj - 1:  # no more move possible
                break
            for j in range(jj - 1, rl_bot - 1, -1):
                res.append(matrix[ii][j])
            jj = rl_bot
            rl_bot += 1
            # down to up, left
            if du_left > ii - 1:  # no more move possible
                break
            for i in range(ii - 1, du_left - 1, -1):
                res.append(matrix[i][jj])
            ii = du_left
            du_left += 1
        return res


class Solution3:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """From a solution on 2021-09-16. This involves automatic direction
        change. It's much simpler in implementation, but it requires either
        modifying the matrix or using an auxilary set to make sure that we do
        not visit the same cell twice.
        """
        M, N = len(matrix), len(matrix[0])
        i, j, di, dj = 0, 0, 0, 1
        res = []
        for _ in range(M * N):  # nice trick to avoid duplication
            res.append(matrix[i][j])
            matrix[i][j] = math.inf
            if i + di < 0 or i + di >= M or j + dj < 0 or j + dj >= N or matrix[i + di][j + dj] == math.inf:
                # change direction
                di, dj = dj, -di
            i += di
            j += dj
        return res


sol = Solution3()
tests = [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7]),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.spiralOrder(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
