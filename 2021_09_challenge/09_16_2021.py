# from pudb import set_trace; set_trace()
from typing import List
import math


class Solution1:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """LeetCode 54

        Nothing complicated, but it does require good planning on how the
        values from the matrix can be accessed. We are peeling off the matrix
        layer by layer. To determine the elements in each layer, all we need is
        the top left corner and the number of rows and cols demarcated by the
        layer to be peeled off. Then we simply go through the layer in clockwise
        motion to record all the values.

        One trick needed is to prevent duplicated counts of values when there is
        only one row or one col. We have to add additional check for this.

        O(MN), 28 ms, 85% ranking.
        """
        i, j = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        res = []
        while rows > 0 and cols > 0:
            for k in range(j, j + cols):
                res.append(matrix[i][k])
            for k in range(i + 1, i + rows):
                res.append(matrix[k][j + cols - 1])
            if i + rows - 1 != i:
                for k in range(j + cols - 2, j - 1, -1):
                    res.append(matrix[i + rows - 1][k])
            if j != j + cols - 1:
                for k in range(i + rows - 2, i, -1):
                    res.append(matrix[k][j])
            i += 1
            j += 1
            rows -= 2
            cols -= 2
        return res


class Solution2:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """From DBabichev. Very smart trick to rotate orientation automatically.

        https://leetcode.com/problems/spiral-matrix/discuss/1466413/Python-simulate-process-explained
        """
        res = []
        i, j, di, dj = 0, 0, 0, 1
        M, N = len(matrix), len(matrix[0])
        for _ in range(M * N):  # another good trick to avoid duplication
            if i + di < 0 or i + di >= M or j + dj < 0 or j + dj >= N or matrix[i + di][j + dj] == math.inf:
                di, dj = dj, -di  # automatic rotation
            res.append(matrix[i][j])
            matrix[i][j] = math.inf
            i += di
            j += dj
        return res


sol = Solution2()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
    ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    ([[1, 2, 3, 4]], [1, 2, 3, 4]),
    ([[1], [2], [3], [4]], [1, 2, 3, 4]),
]

for i, (matrix, ans) in enumerate(tests):
    res = sol.spiralOrder(matrix)
    if res == ans:
        print(f'Test {i}: PASS')
    else:
        print(f'Test {i}; Fail. Ans: {ans}, Res: {res}')
